# Streamlit Library Manager App (Improved Version)
import streamlit as st
import os
import json
import hashlib
import base64
from urllib.parse import urlencode

# ---------------------- Initialization ----------------------
USER_DATA_DIR = "user_data"
os.makedirs(USER_DATA_DIR, exist_ok=True)

if 'username' not in st.session_state:
    st.session_state.username = None
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# ---------------------- Helper Functions ----------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_dir(username):
    return os.path.join(USER_DATA_DIR, username)

def get_user_credentials_path(username):
    return os.path.join(get_user_dir(username), "credentials.json")

def get_user_library_path(username):
    return os.path.join(get_user_dir(username), "library.json")

def get_user_pdf_dir(username):
    path = os.path.join(get_user_dir(username), "pdfs")
    os.makedirs(path, exist_ok=True)
    return path

# ---------------------- Auth Functions ----------------------
def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        cred_path = get_user_credentials_path(username)
        if os.path.exists(cred_path):
            with open(cred_path, 'r') as f:
                stored = json.load(f)
                if stored['password'] == hash_password(password):
                    st.session_state.username = username
                    st.session_state.authenticated = True
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid password!")
        else:
            st.error("User does not exist.")

def register():
    username = st.text_input("Choose Username")
    password = st.text_input("Choose Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password != confirm:
            st.error("Passwords do not match!")
            return
        cred_path = get_user_credentials_path(username)
        if os.path.exists(cred_path):
            st.error("Username already taken!")
            return

        os.makedirs(get_user_pdf_dir(username), exist_ok=True)
        with open(cred_path, 'w') as f:
            json.dump({'password': hash_password(password)}, f)
        with open(get_user_library_path(username), 'w') as f:
            json.dump([], f)

        st.success("Registration successful! Please login.")

# ---------------------- Library Functions ----------------------
def load_library(username):
    lib_path = get_user_library_path(username)
    if os.path.exists(lib_path):
        with open(lib_path, 'r') as f:
            return json.load(f)
    return []

def save_library(username, library):
    with open(get_user_library_path(username), 'w') as f:
        json.dump(library, f, indent=2)

def add_book(title, author, year, genre, pdf_file):
    username = st.session_state.username
    library = load_library(username)
    pdf_path = None
    if pdf_file:
        pdf_path = os.path.join(get_user_pdf_dir(username), pdf_file.name)
        with open(pdf_path, "wb") as f:
            f.write(pdf_file.getbuffer())

    library.append({"title": title, "author": author, "year": year, "genre": genre, "pdf_path": pdf_path})
    save_library(username, library)
    st.success(f"Book '{title}' added successfully!")

def remove_book(title):
    username = st.session_state.username
    library = load_library(username)
    updated = [b for b in library if b['title'].lower() != title.lower()]
    if len(updated) != len(library):
        save_library(username, updated)
        st.success(f"Book '{title}' removed.")
    else:
        st.warning("Book not found.")

# ---------------------- Display ----------------------
def show_pdf(path):
    try:
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        html = f'<embed src="data:application/pdf;base64,{b64}" type="application/pdf" width="100%" height="800px">'
        st.markdown(html, unsafe_allow_html=True)
    except Exception as e:
        st.error("Error displaying PDF.")
        st.markdown(f'<a href="data:application/pdf;base64,{b64}" download>Download PDF</a>', unsafe_allow_html=True)

def display_books(search_term=None, search_by=None):
    is_shared = st.query_params.get("shared", False)
    username = st.query_params.get("user") if is_shared else st.session_state.username
    library = load_library(username)
    if search_term and search_by:
        library = [b for b in library if search_term.lower() in b.get(search_by, '').lower()]

    for idx, book in enumerate(library):
        st.markdown(f"### {book['title']}")
        st.write(f"**Author:** {book['author']} | **Year:** {book['year']} | **Genre:** {book['genre']}")
        if book.get("pdf_path"):
            with open(book["pdf_path"], "rb") as f:
                st.download_button("Download PDF", data=f, file_name=os.path.basename(book["pdf_path"]))
            if not is_shared and st.button("Read Book", key=f"read_{idx}"):
                show_pdf(book["pdf_path"])
        st.markdown("---")

# ---------------------- Share ----------------------
def get_shareable_link():
    base_url = "https://awais-tagar-library-manager-frt4rmjq5fajxydzxvhtj.streamlit.app/"
    link = f"{base_url}?shared=true&user={st.session_state.username}"
    if st.button("Generate Shareable Link"):
        st.code(link)
        st.markdown(f"<input value='{link}' style='width:100%' readonly>", unsafe_allow_html=True)
        st.info("Share this link to give read-only access to your library.")

# ---------------------- Main App ----------------------
st.title("📚 Library Manager")

is_shared = st.query_params.get("shared", False)

if is_shared:
    user = st.query_params.get("user", "guest")
    st.header(f"Shared Library from {user}")
    display_books()
else:
    if not st.session_state.authenticated:
        tab1, tab2 = st.tabs(["Login", "Register"])
        with tab1:
            login()
        with tab2:
            register()
    else:
        menu = st.sidebar.selectbox("Menu", ["Add Book", "View Books", "Search Books", "Remove Book", "Share Library"])
        if st.sidebar.button("Logout"):
            st.session_state.username = None
            st.session_state.authenticated = False
            st.rerun()

        if menu == "Add Book":
            st.header("Add New Book")
            t = st.text_input("Title")
            a = st.text_input("Author")
            y = st.text_input("Year")
            g = st.text_input("Genre")
            f = st.file_uploader("Upload PDF", type=["pdf"])
            if st.button("Add Book"):
                add_book(t, a, y, g, f)

        elif menu == "View Books":
            st.header("Library Collection")
            display_books()

        elif menu == "Search Books":
            st.header("Search Books")
            key = st.selectbox("Search By", ["title", "author", "genre", "year"])
            term = st.text_input("Search Term")
            if st.button("Search"):
                display_books(term, key)

        elif menu == "Remove Book":
            st.header("Remove a Book")
            t = st.text_input("Enter Title")
            if st.button("Remove Book"):
                remove_book(t)

        elif menu == "Share Library":
            st.header("Share Your Library")
            get_shareable_link()
