"""Dashboard code"""

import pandas as pd
import streamlit as st
from helpers.generate_metrics import get_metrics
from helpers.impressions_vs_clks import generate_imp_vs_clks

st.set_page_config(layout='wide')

st.title('Marketing Dashboard 📊')

FILE_PATH = 'data/campaign_data.csv'
df = pd.read_csv(FILE_PATH, parse_dates=[0, 1], infer_datetime_format=True)

# Campaign Manager Filter
option = st.selectbox(
    'Select Campaign Level Analysis',
    ('All Data', 'Campaign Manager level'))

if option == 'All Data':
    st.text('Showing All time campaign stats')
    get_metrics(st)

elif option == 'Campaign Manager level':

    min_date = min(df.utc_date)
    max_date = max(df.utc_date)

    with st.form(key='filters'):
        cm, platform, dfilter, tfilter = st.columns(4)

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

        template_used = tfilter.selectbox(
            'Select Template Name (eg: Flash Deal, Summer Sale, etc)',
            (
                'Flash Deal',
                'Summer Sale',
                'Product Demo',
                'B2B Networking Event',
                'Professional Development Course'
            )
        )

        start_date = pd.to_datetime(date_filter[0], format='%Y-%m-%d')
        end_date = pd.to_datetime(date_filter[1], format='%Y-%m-%d')

        submitted = st.form_submit_button("Submit")

    if submitted:

        df_filter = df[
            (df['campaign_manager'] == CM_NAME) &
            (df['traffic_source'] == CM_Platform) &
            (df['utc_date'] >= start_date) &
            (df['utc_date'] <= end_date) &
            (df['template_name'] == template_used)
        ]

        with st.spinner('Generating Report....'):
            st.write(df_filter)
            # generate_imp_vs_clks(
                # df_filter[
                #     ['year_month', 'impressions', 'page_clicks']
                # ]
            # )
            st.plotly_chart(
                generate_imp_vs_clks(df_filter[
                    ['year_month', 'impressions', 'page_clicks']
                ]),
                use_container_width=True
            )
            st.balloons()

    # get_metrics(st)

# elif option == 'Category':
#     st.text('Please Select at least 1 Category to view analysis')
#     get_metrics(st)

# else:
#     st.text('Please Select at least 1 Traffic Source to view analysis')
#     get_metrics(st)
