import streamlit as st

# Initialize session state if it doesn't exist
if 'page' not in st.session_state:
    st.session_state.page = 'main_page'

# Navigation
if st.session_state.page == 'main_page':
    exec(open('main_page.py').read())
elif st.session_state.page == 'graph_page':
    exec(open('graph_page.py').read())