import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/andrew_photo.JPG")

with col2:
    st.title("Andrew Kuhs")
    content = """
    Hi, I'm Andy. I'm a math teacher and coding student.
    """
    st.write(content)

content2 = """
There are some apps I'm working on listed below.
"""

st.write(content2)
