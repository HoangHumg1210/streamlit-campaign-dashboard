"""Code for paid clicks vs page clicks graph"""
import plotly.express as px

def generate_paid_vs_page_clicks(data_frame):
    """
    Method to generate bar plot for page vs paid clicks

    :param data_frame: Pandas data_frame
    """

    clicks = data_frame.groupby(
            by = [
                'utc_date'
            ]
        ).agg(
            {
                'page_clicks': 'sum',
                'paid_clicks': 'sum'
            }
        ).reset_index()

    fig = px.line(
        clicks,
        x = 'utc_date',
        y = ['page_clicks', 'paid_clicks'],
        labels = {'value': 'Total'},
        title = 'Monthly Paid Vs Page Clicks'
    )

    fig.update_layout(
        hovermode = 'x'
    )

    return fig
