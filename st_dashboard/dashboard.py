"""Dashboard code"""

import pandas as pd
import streamlit as st
from helpers.generate_metrics import get_metrics
from helpers.impressions import generate_impressions
from helpers.clicks import generate_clicks
from helpers.device_viewed import generate_device_view_perc
from helpers.top_campaigns import generate_top_campaign
from helpers.browser_bar import generate_browser_view
from helpers.paid_vs_page_clicks import generate_paid_vs_page_clicks

st.set_page_config(layout='wide')

st.title('Marketing Dashboard 📊')

FILE_PATH = 'data/campaign_data.csv'
df = pd.read_csv(FILE_PATH, parse_dates=[0])

min_date = min(df.utc_date)
max_date = max(df.utc_date)

with st.form(key='filters'):
    cm, platform, dfilter = st.columns(3)

    CM_NAME = cm.selectbox(
        'Select Campaign Manager Name',
        (
            'Campaign Manager 1', 
            'Campaign Manager 2', 
            'Campaign Manager 3', 
            'Campaign Manager 4',
            'Campaign Manager 5'
        )
    )

    CM_Platform = platform.selectbox(
        'Select Campaign Source (eg: Facebook Ads, etc.)',
        (
            'Facebook Ads',
            'LinkedIn Ads',
            'YouTube Ads',
            'Reddit Ads',
            'TikTok Ads',
            'Instagram Ads',
            'Twitter Ads'
        )
    )

    date_filter = dfilter.date_input(
        "Pick a Date Range",
        (min_date, max_date)
    )

    start_date = pd.to_datetime(date_filter[0], format='%Y-%m-%d')
    end_date = pd.to_datetime(date_filter[1], format='%Y-%m-%d')

    submitted = st.form_submit_button("Submit")

if submitted:
    df_filter = df[
        (df['campaign_manager'] == CM_NAME) &
        (df['traffic_source'] == CM_Platform) &
        (df['utc_date'] >= start_date) &
        (df['utc_date'] <= end_date)
    ]

# Tab View
ad_analysis, raw_data = st.tabs([
    'Analysis',
    'Raw Data'
])

if submitted:
    df_filter = df[
        (df['campaign_manager'] == CM_NAME) &
        (df['traffic_source'] == CM_Platform) &
        (df['utc_date'] >= start_date) &
        (df['utc_date'] <= end_date)
    ]

    with ad_analysis:
        get_metrics(df_filter, st)

        with st.spinner('Generating Report....'):

            # Data Table
            test_df = df_filter[
                [
                    'account_name', 'campaign_url', 'country',
                    'impressions', 'page_clicks', 
                    'ad_spend', 'revenue', 'gross_profit',
                    'cpc', 'rpc', 'cpa', 'roas'
                ]
            ]

            st.subheader('Campaign Stats')
            st.dataframe(generate_top_campaign(test_df), use_container_width=True)


            # Graphs
            row1_col1, row1_col2 = st.columns(2)
            row1_col1.plotly_chart(
                generate_impressions(
                    df_filter[['utc_date', 'impressions']]
                )
            )
            row1_col2.plotly_chart(
                generate_paid_vs_page_clicks(
                    df_filter[['utc_date', 'page_clicks', 'paid_clicks']]
                )
            )

            # Graphs
            row2_col1, row2_col2 = st.columns(2)
            row2_col1.plotly_chart(
                generate_device_view_perc(df_filter['device_viewed'])
            )

            row2_col2.plotly_chart(
                generate_browser_view(df_filter['browser'])
            )

            st.balloons()

        with raw_data:
            st.write(df_filter)
