"""Code to generate Device view % graph"""
import plotly.express as px

def generate_device_view_perc(data_frame):
    """
    Method to generate pie chart to view % of device used

    :param data_frame: Pandas data_frame
    """

    device_perc = data_frame.value_counts().reset_index()

    fig = px.pie(
        device_perc,
        values = device_perc['count'],
        names = device_perc['device_viewed'],
        color = device_perc['device_viewed'],
        hole = 0.3,
        title = 'Devices Used %'
    )

    return fig
