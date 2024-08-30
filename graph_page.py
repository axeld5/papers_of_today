import streamlit as st
import pandas as pd
import plotly.express as px

# Check if the session state is correctly set
if 'page' not in st.session_state or st.session_state.page != 'graph_page':
    st.session_state.page = 'main_page'
    st.rerun()

# Sample data creation (replace this with your actual data loading)
df = pd.read_csv("clustered_papers.csv")

# Graph page setup
st.title('Paper Embeddings Visualization')

# Create scatter plot
fig = px.scatter(
    df,
    x='paper_x',
    y='paper_y',
    color='cluster_index',
    hover_name='paper_title',
    title='Paper Embeddings',
)

fig.update_traces(
    hovertemplate='<b>%{hovertext}</b><extra></extra>',
    hovertext=df['paper_title']
)

# Display plot in Streamlit
st.plotly_chart(fig)

# Button to go back to the main page
if st.button('Go to Main Page'):
    st.session_state.page = 'main_page'
    st.rerun()