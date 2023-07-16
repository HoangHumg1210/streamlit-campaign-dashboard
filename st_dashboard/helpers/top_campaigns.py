"""Code to Top campaigns graph"""

def generate_top_campaign(data_frame):
    """
    Method to generate data table for top campaigns

    :param data_frame: Pandas data_frame
    """

    top_campaigns = data_frame.groupby(
            by = [
                'account_name',
                'campaign_url',
                'country'
            ]
        ).agg(
            {
                'impressions': 'sum', 
                'page_clicks': 'sum',
                'revenue': 'sum',
                'ad_spend': 'sum',
                'gross_profit': 'sum',
                'cpc': 'mean',
                'rpc': 'mean',
                'cpa': 'mean',
                'roas': 'mean'
            }
        ).reset_index()

    return top_campaigns
