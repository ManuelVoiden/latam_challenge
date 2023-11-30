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
    # Load the entire dataset into a DataFrame
    df = pd.read_json(file_path, lines=True)

    # Convert 'date' to datetime and extract the date
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Extract username from the nested 'user' dictionary
    df['username'] = df['user'].apply(lambda x: x['username'])

    # Group by 'date' and count tweets, get the most active user per date
    top_dates_df = df.groupby('date').agg(
        total_tweets=('date', 'size'),
        most_active_user=('username', lambda x: x.mode()[0])
    ).sort_values('total_tweets', ascending=False).head(10).drop(columns=['total_tweets'])

    # Convert to the desired format [(date, most_active_user), ...]
    top_dates = list(top_dates_df.itertuples(index=True, name=None))

    return top_dates


file_path = "./data/farmers-protest-tweets-2021-2-4.json"

top_dates = q1_time(file_path)
print(top_dates)