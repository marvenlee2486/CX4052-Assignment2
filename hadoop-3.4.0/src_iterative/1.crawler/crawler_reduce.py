# Input <Key, Value> : <url, SourceText>
# Output <Key, Value> : <url, list of out-url>

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import json 

def extract_root(url):
    parsed_url = urlparse(url)
    root_url = parsed_url.scheme + "://" + parsed_url.netloc
    return root_url


id = 0
# A possible improvement is to cache the result so that a crawled page is not crawled again
page = {}
for line in sys.stdin: 
    url, value_str = line.strip().split('\t')
    page_text = eval(value_str)
    page[url] = page_text

for url, page_text in page.items():
    soup = BeautifulSoup(page_text, 'html.parser')
    root_url = extract_root(url)
    outlink_urls = []
    for link in soup.find_all('a'):
        out_url = link.get('href')
        try:
            if out_url[0] == "/":
                out_url = root_url + out_url
            response = requests.head(out_url, allow_redirects=True) # To get the most consistent one
            final_url = response.url
            outlink_urls.append(final_url)
            #print("OK")
        except:
            pass
            # print("Not a URL")
    id += 1
    print(f"{url}\t{json.dumps(outlink_urls)}")
