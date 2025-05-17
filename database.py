import os
from dotenv import load_dotenv
import streamlit as st

from google.cloud import bigquery
from google.oauth2 import service_account

load_dotenv()

# BigQuery credentials từ file .env
TYPE_BQ = os.getenv("TYPE_BQ")
PROJECT_ID_BQ = os.getenv("PROJECT_ID_BQ")
PRIVATE_KEY_ID_BQ = os.getenv("PRIVATE_KEY_ID_BQ")
PRIVATE_KEY_BQ = os.getenv("PRIVATE_KEY_BQ").replace("\\n", "\n")
CLIENT_EMAIL_BQ = os.getenv("CLIENT_EMAIL_BQ")
CLIENT_ID_BQ = os.getenv("CLIENT_ID_BQ")
AUTH_URI_BQ = os.getenv("AUTH_URI_BQ")
TOKEN_URI_BQ = os.getenv("TOKEN_URI_BQ")
AUTH_PROVIDER_X509_CERT_URL_BQ = os.getenv("AUTH_PROVIDER_X509_CERT_URL_BQ")
CLIENT_X509_CERT_URL_BQ = os.getenv("CLIENT_X509_CERT_URL_BQ")
UNIVERSE_DOMAIN_BQ = os.getenv("UNIVERSE_DOMAIN_BQ")

DATASET_ID_BQ = os.getenv("DATASET_ID_BQ")

@st.cache_resource(ttl=24*3600, max_entries=1, show_spinner=False)
def get_client():
    """Tạo và cache BigQuery Client từ biến môi trường."""
    credentials_info = {
        "type": TYPE_BQ,
        "project_id": PROJECT_ID_BQ,
        "private_key_id": PRIVATE_KEY_ID_BQ,
        "private_key": PRIVATE_KEY_BQ,
        "client_email": CLIENT_EMAIL_BQ,
        "client_id": CLIENT_ID_BQ,
        "auth_uri": AUTH_URI_BQ,
        "token_uri": TOKEN_URI_BQ,
        "auth_provider_x509_cert_url": AUTH_PROVIDER_X509_CERT_URL_BQ,
        "client_x509_cert_url": CLIENT_X509_CERT_URL_BQ,
        "universe_domain": UNIVERSE_DOMAIN_BQ,
    }

    # Tạo credentials từ dict
    credentials = service_account.Credentials.from_service_account_info(credentials_info)

    # Truyền credentials và location vào BigQuery Client
    client = bigquery.Client(
        project=PROJECT_ID_BQ,
        credentials=credentials,
        location="asia-southeast1"  # <-- thêm dòng này
    )

    return client
