import pandas as pd
import json
import time
import datetime
import memory_profiler
#import concurrent

from datetime import datetime
from memory_profiler import memory_usage
from collections import defaultdict, Counter

#def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
def q1_memory(file_path: str):
    tweet_counts = Counter()
    user_activity = defaultdict(Counter)

    # Read and process the JSON file
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.fromisoformat(tweet['date']).date()
            username = tweet['user']['username']

            # Count tweets per date and track user activity
            tweet_counts[date] += 1
            user_activity[date][username] += 1

    # Identify top 10 dates
    top_dates = tweet_counts.most_common(10)

    # Find the most active user for each top date
    top_dates = [(date, user_activity[date].most_common(1)[0][0]) for date, _ in top_dates]

    return top_dates


file_path = "./data/farmers-protest-tweets-2021-2-4.json"

top_dates = q1_memory(file_path)
print(top_dates)