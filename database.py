import os
import sqlalchemy as sa
import streamlit as st

@st.cache_resource
def get_engine():
    db_path = os.path.join(os.getcwd(), "warehouse.db")

    # Nếu file chưa tồn tại, tạo file rỗng
    if not os.path.exists(db_path):
        open(db_path, 'a').close()

    # Cấp quyền ghi/đọc/thực thi cho tất cả user (rwxrwxrwx)
    os.chmod(db_path, 0o777)

    return sa.create_engine(f"sqlite:///{db_path}")
