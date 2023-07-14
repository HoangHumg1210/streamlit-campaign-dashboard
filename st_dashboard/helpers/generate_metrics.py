"""Code for Metrics"""

def get_metrics(data_frame, st_obj):

    """
    Streamlit metrics cards

    :param data_frame: Pandas dataframe
    :param st_obj: Object for streamlit component
    """

    impressions = data_frame.loc[:, 'impressions'].sum()
    clicks = data_frame.loc[:, 'page_clicks'].sum()
    ctr = round(
        100.0 * data_frame.loc[:, 'page_clicks'].sum() / data_frame.loc[:, 'impressions'].sum()
    , 2
    )
    gross_profit = round(data_frame.loc[:, 'gross_profit'].sum(), 2)
    avg_rpc = round(data_frame.loc[:, 'rpc'].mean(), 2)

    col1, col2, col3, col4, col5 = st_obj.columns(5)
    col1.metric("Total Impressions", impressions)
    col2.metric("Total Clicks", clicks)
    col3.metric("CTR", f"{ctr}%")
    col4.metric("Total Gross Profit", gross_profit)
    col5.metric("Total RPC", f"{avg_rpc}")
