import sqlalchemy as sa
import streamlit as st

@st.cache_resource
def get_engine():
    return sa.create_engine('sqlite:///warehouse.db')
