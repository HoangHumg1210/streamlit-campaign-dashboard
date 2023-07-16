""" Campaign Data file """
import csv
from datetime import (
    datetime,
    timedelta
)
import random
import yaml

class CampaignDataGenerator:
    """
    Class to generate and store campaign data
    """
    def __init__(self, start_date, end_date, config_file):
        self.start_date = start_date
        self.end_date = end_date
        self.config = self.load_config(config_file)
        self.country_states = self.config['states']
        self.models = self.config['models']
        self.header = self.config['header']
        self.data = []

    def load_config(self, config_file):
        """
        Method to read YAML file and load configs
        
        :param config_file: config file path
        """
        with open(config_file, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config

    def generate_data(self):
        """
        Method to generate random campaign ad data
        """
        current_date = self.start_date

        while current_date <= self.end_date:
            utc_date = current_date.strftime("%Y-%m-%d")

            traffic_source = random.choice(self.config['traffic_sources'])
            account_name = random.choice(self.config['account_names'])
            campaign_manager = random.choice(self.config['campaign_managers'])
            template_name = random.choice(self.config['template_name'])

            device_viewed = random.choice(self.config['devices'])
            device_models = self.models[device_viewed]
            device_model = random.choice(device_models)

            country = random.choice(self.config['countries'])
            states = self.country_states[country]
            state = random.choice(states)

            browser = random.choice(self.config['browsers'])
            campaign_url = f"https://www.example.com/{template_name.lower().replace(' ', '-')}"

            if random.random() < 0.2:
                impressions = random.randint(10, 50)
                page_clicks = random.randint(10, impressions)
                revenue = page_clicks * random.uniform(0.5, 2)
                blocked_clicks = random.randint(0, 10)
                ad_spend = random.uniform(10.00, 100.00)
                paid_clicks = page_clicks - blocked_clicks
                count_of_ads_returned = random.randint(1, 2)
                roas = revenue / ad_spend
                rpc = revenue / page_clicks
                cpc = ad_spend / page_clicks
                cpa = ad_spend / paid_clicks if paid_clicks > 0 else 0
                gross_profit = revenue - ad_spend
            else:
                impressions = random.randint(300, 800)
                page_clicks = random.randint(100, impressions)
                revenue = page_clicks * random.uniform(2, 5)
                blocked_clicks = random.randint(50, 100)
                ad_spend = random.uniform(200.00, 600.00)
                paid_clicks = page_clicks - blocked_clicks
                count_of_ads_returned = random.randint(2, 5)
                roas = revenue / ad_spend
                rpc = revenue / page_clicks
                cpc = ad_spend / page_clicks
                cpa = ad_spend / paid_clicks if paid_clicks > 0 else 0
                gross_profit = revenue - ad_spend

            row = [
                utc_date, traffic_source, account_name, campaign_manager,
                device_viewed, device_model, browser,
                template_name, country, state, campaign_url,
                impressions, page_clicks, revenue, blocked_clicks,
                ad_spend, paid_clicks, count_of_ads_returned, roas,
                rpc, cpc, cpa, gross_profit
            ]

            self.data.append(row)

            current_date += timedelta(days=1)
        self.write_csv(self.data)

    def write_csv(self, data):
        """
        Method to write data to CSV file
        
        :param data: Random Ads Data
        """
        with open(
            self.config['file_path'][0],
            'w', 
            newline='',
            encoding='utf-8'
        ) as file:
            writer = csv.writer(file)
            writer.writerow(self.header)
            writer.writerows(data)

# Input
START_DATE = datetime(2020, 1, 1)
END_DATE = datetime(2022, 12, 31)
CONFIG_FILE = 'configs/configs.yaml'

generator = CampaignDataGenerator(START_DATE, END_DATE, CONFIG_FILE)
generator.generate_data()
