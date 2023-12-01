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

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()
    emoji_pattern = re.compile('[\U0001F600-\U0001F64F]')  #This is the REGEX pattern for emojis

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet.get('content', '')
            emojis = emoji_pattern.findall(content)
            emoji_counter.update(emojis)

    top_emojis = emoji_counter.most_common(10)
    return top_emojis

file_path = "./data/farmers-protest-tweets-2021-2-4.json"

#Executing q2_time and printing the result
top_emojis = q2_time(file_path)
print(top_emojis)