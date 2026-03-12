import pandas as pd
import numpy as np
import datetime
import os

# Seed for reproducibility
np.random.seed(42)

# Constants
NUM_ROWS = 1000
REGIONS = ['APAC', 'EMEA', 'LATAM', 'North America', 'Oceania', 'Southeast Asia', 'South Asia', 'Eastern Europe', 'Middle East', 'Africa']
CHANNELS = ['SEM', 'SEO', 'Paid Social', 'Meta-search', 'Affiliate', 'YouTube', 'Display', 'OTT']
BUSINESS_LINES = ['Hotels', 'Flights', 'Vacation Rentals', 'Experiences']

# Generate random dates for the last 52 weeks
start_date = datetime.date.today() - datetime.timedelta(days=365)
date_range = [start_date + datetime.timedelta(days=x) for x in range(365)]

data = []

for i in range(NUM_ROWS):
    region = np.random.choice(REGIONS)
    channel = np.random.choice(CHANNELS)
    business_line = np.random.choice(BUSINESS_LINES)
    # Simple list of dates
    date = date_range[np.random.randint(0, len(date_range))]
    
    # Regional ROAS Bias (Michael's challenge)
    regional_bias = {
        'North America': 4.2,
        'EMEA': 3.0,
        'APAC': 2.1,
        'LATAM': 1.8,
        'Oceania': 3.5,
        'Southeast Asia': 2.5,
        'South Asia': 1.9,
        'Eastern Europe': 2.8,
        'Middle East': 3.2,
        'Africa': 1.6
    }
    
    base_roas = regional_bias.get(region, 2.5) + np.random.normal(0, 0.5)
    roas = max(0.5, round(base_roas, 2))
    
    planned_budget = np.random.uniform(5000, 50000)
    spend_variance = np.random.normal(1.0, 0.1) 
    actual_spend = round(planned_budget * spend_variance, 2)
    
    revenue = round(actual_spend * roas, 2)
    
    aov_map = {'Hotels': 450, 'Flights': 600, 'Vacation Rentals': 800, 'Experiences': 120}
    aov = aov_map[business_line] + np.random.normal(0, 50)
    bookings = int(revenue / aov) if revenue > aov else np.random.randint(0, 5)
    
    market_share = round(np.random.uniform(5, 25), 2)
    sov = round(market_share + np.random.normal(0, 2), 2) 
    ad_pressure = round(np.random.uniform(0.5, 1.5), 2)
    
    cac = round(actual_spend / max(1, bookings), 2)
    efficiency_score = round(min(100, (aov / max(1, cac)) * 10), 2)
    
    data.append({
        'week_start_date': date.isoformat(),
        'region': region,
        'channel': channel,
        'line_of_business': business_line,
        'planned_budget': planned_budget,
        'actual_spend': actual_spend,
        'revenue': revenue,
        'roas': roas,
        'bookings': bookings,
        'cac': cac,
        'market_share_pct': market_share,
        'share_of_voice_pct': sov,
        'competitive_pressure_index': ad_pressure,
        'efficiency_score': efficiency_score,
        'budget_variance': round(actual_spend - planned_budget, 2)
    })

df = pd.DataFrame(data)
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, '../ota_marketing_data.csv')
df.to_csv(output_path, index=False)
print(f"Dataset generated: {output_path}")
print(df.head())
