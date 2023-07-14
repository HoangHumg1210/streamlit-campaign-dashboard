"""Code to generate impressions vs clicks graph"""
import plotly.express as px

def generate_imp_vs_clks(data_frame):
    """
    Method to generate plotly line graph
    
    :param data_frame: Pandas dataframe
    """

    monthly_data = data_frame.groupby(
            data_frame['utc_date']
        ).agg(
            {
                'impressions': 'sum', 
                'page_clicks': 'sum'
            }
        ).reset_index()

    fig = px.line(
        monthly_data,
        x = 'utc_date',
        y = ['impressions', 'page_clicks'],
        labels = {'value': 'Count'},
        title = 'Monthly Impressions and Page Clicks'
    )

    fig.update_traces(connectgaps=True)

    return fig
