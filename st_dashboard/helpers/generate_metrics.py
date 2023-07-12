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

df = pd.read_csv(FILE_PATH)
df['utc_date'] = pd.to_datetime(df.utc_date, format='%Y-%m-%d')

monthly_data = df.groupby(
        df['utc_date'].dt.to_period('M')
    ).agg(
        {
            'impressions': 'sum', 
            'page_clicks': 'sum', 
            'utc_date': 'first'}
    ).reset_index(drop=True)
