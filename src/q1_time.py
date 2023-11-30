import pandas as pd
import json
import time
import datetime
import memory_profiler

from datetime import datetime
from memory_profiler import memory_usage
from collections import defaultdict, Counter
from typing import List, Tuple

def q1_time(file_path: str):
    # Read the JSON file into a DataFrame
    tweets_df = pd.read_json(file_path, lines=True)

    # Convert the 'date' column to datetime and extract the date
    tweets_df['date'] = pd.to_datetime(tweets_df['date']).dt.date

    # Group by 'date' and count tweets, also get the most active user per date
    top_dates_df = tweets_df.groupby('date').agg(
        total_tweets=('date', 'size'),
        most_active_user=('user', lambda x: x.mode()[0]['username'])
    ).sort_values('total_tweets', ascending=False).head(10)

    # Convert the result to the desired format
    top_dates = [(row.name, row['most_active_user']) for _, row in top_dates_df.iterrows()]

    return top_dates


file_path = "./data/farmers-protest-tweets-2021-2-4.json"

top_dates = q1_time(file_path)
print(top_dates)