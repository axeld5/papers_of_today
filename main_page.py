import json
import streamlit as st
import pandas as pd

# Reading infos
df = pd.read_csv("extracted_papers.csv", sep=",").sort_values(by="author_count", ascending=False)
with open('parameters.json') as f:
    info_dict = json.load(f)
date = info_dict["date"]
topic = info_dict["topic"]

# Streamlit App
st.title(f'Research Papers, {date}')
st.write(f'All ArXiV papers posted about {topic} related topics can be found here.')

if st.button('Go to Graph Page'):
    st.session_state.page = 'graph_page'
    st.rerun()

for index, row in df.iterrows():
    with st.expander(row['title']):
        st.write(row['id'])
        st.write(row['authors'])
        st.write(row['summary'])