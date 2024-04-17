
import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import requests

def get_api_data(api_key, endpoint="data"):
    """
    Fetch data from the API using the provided API key.
    :param api_key: str, the API key for authentication.
    :param endpoint: str, the endpoint to hit, default is 'data'.
    :return: DataFrame, the data retrieved from the API.
    """
    base_url = 'https://lignumdata.ch/lignum_live/api/'
    url = f"{base_url}{endpoint}"
    headers = {'Authorization': f'Bearer {api_key}'}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")
        return pd.DataFrame()

def main():
    st.title('Lignum API Data Viewer')
    
    # Input for API key
    api_key = st.text_input('Enter your Lignum API key', type='password')
    
    # Button to fetch data
    if st.button('Fetch Data'):
        if api_key:
            data = get_api_data(api_key)
            if not data.empty:
                st.write(data)
            else:
                st.write("No data available or failed to fetch data.")
        else:
            st.error("Please enter an API key.")

if __name__ == "__main__":
    main()

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="LignumDataAPI",
        page_icon="👋",
    )

    st.write("# Lignum Data API Viewer 👋")


if __name__ == "__main__":
    run()
