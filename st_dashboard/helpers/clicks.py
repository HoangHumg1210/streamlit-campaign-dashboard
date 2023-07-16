"""Code to generate clicks graph"""
import plotly.express as px

def generate_clicks(data_frame):
    """
    Method to generate clicks graph
    
    :param data_frame: Pandas dataframe
    """

    monthly_data = data_frame.groupby(
            data_frame['utc_date']
        ).agg(
            {
                'page_clicks': 'sum'
            }
        ).reset_index()

    fig = px.line(
        monthly_data,
        x = 'utc_date',
        y = 'page_clicks',
        labels = {'value': 'Count'},
        title = 'Monthly Page Clicks'
    )

    fig.update_traces(connectgaps=True)

    return fig
