"""Code to generate browser view % graph"""
import plotly.express as px

def generate_browser_view(data_frame):
    """
    Method to generate pie chart to view % of browser used

    :param data_frame: Pandas data_frame
    """

    browser_perc = data_frame.value_counts().reset_index()

    fig = px.bar(
        browser_perc,
        x = 'browser',
        y = 'count',
        color = 'count',
        title = 'Top Browsers'
    )

    return fig
