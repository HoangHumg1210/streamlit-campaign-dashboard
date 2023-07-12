"""Dashboard code"""

import time
import streamlit as st
import plotly.express as px
from helpers.generate_metrics import get_metrics
from helpers.generate_metrics import monthly_data

st.set_page_config(layout='wide')

st.title('Marketing Dashboard 📊')

# Campaign Manager Filter
option = st.selectbox(
    'Select Campaign Level Analysis',
    ('All Data', 'Campaign Manager level'))

if option == 'All Data':
    st.text('Showing All time campaign stats')
    get_metrics(st)

elif option == 'Campaign Manager level':

    with st.form(key='filters'):
        cm, platform, test1, test2 = st.columns(4)

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

        test1.text_input('Enter some text')
        test2.text_input('Enter some more text')

        submitted = st.form_submit_button("Submit")

    if submitted:
        with st.spinner('Generating Report....'):
            time.sleep(1)
            st.text(f'Showing Data for: {CM_NAME} and for {CM_Platform} platform.')
            fig = px.line(
                monthly_data,
                x = 'utc_date',
                y = ['impressions', 'page_clicks'],
                labels = {'value': 'Count'},
                title = 'Monthly Impressions and Page Clicks'
            )
            st.plotly_chart(fig, use_container_width=True)
            st.balloons()

    # get_metrics(st)

# elif option == 'Category':
#     st.text('Please Select at least 1 Category to view analysis')
#     get_metrics(st)

# else:
#     st.text('Please Select at least 1 Traffic Source to view analysis')
#     get_metrics(st)
