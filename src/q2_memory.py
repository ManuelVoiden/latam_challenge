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

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()
    emoji_pattern = re.compile('[\U0001F600-\U0001F64F]')  # Basic emoji pattern

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet.get('content', '')
            emojis = emoji_pattern.findall(content)
            for emoji in emojis:
                emoji_counter[emoji] += 1

    top_emojis = emoji_counter.most_common(10)
    return top_emojis

file_path = "./data/farmers-protest-tweets-2021-2-4.json"

#Executing q2_memory and printing the result
top_emojis = q2_memory(file_path)
print(top_emojis)