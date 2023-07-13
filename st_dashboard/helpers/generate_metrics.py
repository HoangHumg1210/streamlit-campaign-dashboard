"""Code for Metrics"""
import pandas as pd

FILE_PATH = 'data/campaign_data.csv'

def get_metrics(st):
    """Return streamlit metrics"""
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Avg. Impressions", "785k")
    col2.metric("Avg. CTR", "77.58%")
    col3.metric("Avg. Gross Profit", "87547k")
    col4.metric("Avg. RPC", "1.90")
