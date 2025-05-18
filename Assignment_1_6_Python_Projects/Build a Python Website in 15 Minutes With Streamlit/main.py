import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Simple Data Dashboard")

uploaded_file = st.file_uploader("📂 Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.write(df.head())

    st.subheader("📈 Data Summary")
    st.write(df.describe())

    st.subheader("🎯 Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("📉 Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        fig, ax = plt.subplots()
        ax.plot(filtered_df[x_column], filtered_df[y_column], marker='o', color='black')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f"{y_column} vs {x_column}")
        st.pyplot(fig)
else:
    st.warning("👆 Please upload a CSV file to begin.")
