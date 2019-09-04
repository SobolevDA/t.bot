from bs4 import BeautifulSoup
import requests
import re
import time

headers = {'accept': '*/*',
           'user-agen': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}


base_url = "http://coldfilm.ws"


def parse(base_url, headers):
    messages = {}
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        content = soup.find_all("img", {"data-src": re.compile("\/_\w{2}\/\d{,5}\/\w{1}\d{,10}\.jpg")}, "title")
        for titles in content:
            #print(titles.attrs['title'])
            #print(base_url+titles.attrs['data-src'])
            messages[titles.attrs['title']] = base_url+titles.attrs['data-src']
        return messages
        #time.sleep(2)

if __name__ == "__main__":
    parse(base_url, headers)
