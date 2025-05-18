import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country_data = data[0]

        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        region = country_data.get("region", "N/A")
        latlng = country_data.get("latlng", [0, 0])
        flag_url = country_data.get("flags", {}).get("png", "")

        currencies = country_data.get("currencies", {})
        currency_names = ', '.join([v["name"] for v in currencies.values()]) if currencies else "N/A"

        return {
            "name": name,
            "capital": capital,
            "population": population,
            "area": area,
            "region": region,
            "currency": currency_names,
            "latlng": latlng,
            "flag_url": flag_url
        }
    else:
        return None

def main():
    st.title("Country Information App")

    country_name = st.text_input("Enter a country name:")

    if country_name:
        country_info = fetch_country_data(country_name)

        if country_info:
            st.subheader("Country Information")
            st.image(country_info["flag_url"], width=200)
            st.write(f"**Name:** {country_info['name']}")
            st.write(f"**Capital:** {country_info['capital']}")
            st.write(f"**Population:** {country_info['population']:,}")
            st.write(f"**Area:** {country_info['area']:,} sq. km")
            st.write(f"**Currency:** {country_info['currency']}")
            st.write(f"**Region:** {country_info['region']}")

            st.subheader(" Map Location")
            st.map(data={"lat": [country_info["latlng"][0]], "lon": [country_info["latlng"][1]]})
        else:
            st.error("Country not found. Please check your input.")

if __name__ == "__main__":
    main()
