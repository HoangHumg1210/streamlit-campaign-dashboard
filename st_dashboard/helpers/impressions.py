"""Code to generate impressions graph"""
import plotly.express as px

def generate_impressions(data_frame):
    """
    Method to generate impression graph
    
    :param data_frame: Pandas dataframe
    """

    monthly_data = data_frame.groupby(
            data_frame['utc_date']
        ).agg(
            {
                'impressions': 'sum'
            }
        ).reset_index()

    fig = px.line(
        monthly_data,
        x = 'utc_date',
        y = 'impressions',
        labels = {'value': 'Count'},
        title = 'Monthly Impressions'
    )

    fig.update_traces(connectgaps=True)

    return fig
