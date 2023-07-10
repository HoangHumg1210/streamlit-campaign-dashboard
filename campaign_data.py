import csv
from datetime import datetime, timedelta
import random
import yaml

class CampaignDataGenerator:
    def __init__(self, start_date, end_date, config_file):
        self.start_date = start_date
        self.end_date = end_date
        self.config = self.load_config(config_file)
        self.header = self.config['header']
        self.data = []

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def generate_data(self, file_path):
        current_date = self.start_date
        
        while current_date <= self.end_date:
            month_name = current_date.strftime('%b %Y')
            utc_date = current_date.strftime("%Y-%m-%d")

            traffic_source = random.choice(self.config['traffic_sources'])
            account_name = random.choice(self.config['account_names'])
            campaign_manager = random.choice(self.config['campaign_managers'])
            device_viewed = random.choice(self.config['devices'])
            device_models = random.choice(self.config['device_models'])
            template_name = random.choice(self.config['template_names'])
            country = random.choice(self.config['countries'])
            state = random.choice(self.config['states'])
            city = random.choice(self.config['cities'])

            browser = random.choice(self.config['browsers'])
            campaign_url = f"https://www.example.com/{template_name.lower().replace(' ', '-')}"

            if random.random() < 0.2:
                impressions = random.randint(10, 50)
                page_clicks = random.randint(1, impressions)
                revenue = page_clicks * random.uniform(0.5, 2)
                blocked_clicks = random.randint(0, 2)
                ad_spend = random.randint(10, 100)
                paid_clicks = page_clicks - blocked_clicks
                count_of_ads_returned = random.randint(1, 2)
                roas = revenue / ad_spend
                rcp = revenue / page_clicks
                cpc = ad_spend / page_clicks
                cpa = ad_spend / paid_clicks if paid_clicks > 0 else 0
                gross_profit = revenue - ad_spend
            else:
                impressions = random.randint(100, 500)
                page_clicks = random.randint(1, impressions)
                revenue = page_clicks * random.uniform(2, 5)
                blocked_clicks = random.randint(10, 100)
                ad_spend = random.randint(1000, 5000)
                paid_clicks = page_clicks - blocked_clicks
                count_of_ads_returned = random.randint(2, 5)
                roas = revenue / ad_spend
                rcp = revenue / page_clicks
                cpc = ad_spend / page_clicks
                cpa = ad_spend / paid_clicks if paid_clicks > 0 else 0
                gross_profit = revenue - ad_spend

            row = [
                utc_date, traffic_source, account_name, campaign_manager, device_viewed, device_models,
                browser,
                month_name, template_name, country, state, city,
                campaign_url, impressions, page_clicks, revenue, blocked_clicks, ad_spend, paid_clicks, 
                count_of_ads_returned, roas, rcp, cpc, cpa, gross_profit
            ]

            self.data.append(row)

            current_date += timedelta(days=1)
        self.write_csv(file_path, self.data)

    def write_csv(self, file_path, data):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.header)
            writer.writerows(data)

# Usage example
start_date = datetime(2018, 1, 1)
end_date = datetime(2022, 12, 31)
config_file = 'configs/configs.yaml'

generator = CampaignDataGenerator(start_date, end_date, config_file)
generator.generate_data('data/campaign_data.csv')