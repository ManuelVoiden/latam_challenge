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

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()
    mention_pattern = re.compile(r'@(\w+)')

    # Process file line by line
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            mentions = mention_pattern.findall(tweet.get('content', ''))
            for mention in mentions:
                mention_counter[mention] += 1

    # Get the top 10 mentions
    top_mentions = mention_counter.most_common(10)

    return top_mentions

file_path = "./data/farmers-protest-tweets-2021-2-4.json"

#Executing q2_memory and printing the result
top_emojis = q3_memory(file_path)
print(top_emojis)