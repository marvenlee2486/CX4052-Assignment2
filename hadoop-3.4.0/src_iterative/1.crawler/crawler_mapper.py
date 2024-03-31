# Input: <url, [outlink-url]>
# Output: <outlink-url, sourcefile>
# Mapper + Combine

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import json 

outlink_url_list = []
for line in sys.stdin: 
    _, value_str = line.strip().split('\t')
    temp_list = eval(value_str)
    outlink_url_list += temp_list

    for outlink_url in outlink_url_list:
        page = requests.get(outlink_url)
        print(f"{outlink_url}\t{json.dumps(page.text)}")
