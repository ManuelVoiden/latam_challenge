import pandas as pd
import json
import time
import datetime
import memory_profiler
import re
from typing import List, Tuple

from datetime import datetime
from memory_profiler import memory_usage
from collections import defaultdict, Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Read the entire file into a Pandas DataFrame
    df = pd.read_json(file_path, lines=True)

    # Regular expression to extract mentions
    mention_pattern = re.compile(r'@(\w+)')

    # Extract mentions and explode the DataFrame
    df['mentions'] = df['content'].str.findall(mention_pattern)
    df_exploded = df.explode('mentions')

    # Count and get the top 10 mentions
    top_mentions = df_exploded['mentions'].value_counts().head(10)

    # Convert to list of tuples
    top_mentions_output = list(top_mentions.items())

    return top_mentions_output


file_path = "./data/farmers-protest-tweets-2021-2-4.json"

#Executing q2_time and printing the result
top_emojis = q3_time(file_path)
print(top_emojis)