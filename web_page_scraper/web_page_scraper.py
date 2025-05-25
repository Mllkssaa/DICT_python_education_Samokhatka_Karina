import os
import requests
import string
from bs4 import BeautifulSoup

def stage1():
    url = input("Input the URL.\n>")
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Invalid quote resource..")
            return

        data = response.json()
        if 'content' in data:
            print(data['content'])
        else:
            print("Invalid quote resource..")
    except Exception:
        print("Invalid quote resource..")


def stage2():
    url = input("Input the URL.\n>")
    if "imdb.com/title/" not in url:
        print("Invalid movie page.")
        return

    try:
        response = requests.get(url, headers={'Accept-Language': 'en-US, en;q=0.5'})
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tags = soup.find('title')
        meta_desc = soup.find('meta', {'name': 'description'})

        if title_tags and meta_desc:
            title = title_tags.text.split('-')[0].strip()
            description = meta_desc.get('content').strip()
            print({"title": title, "description": description})
        else:
            print("Invalid movie page.")
    except Exception:
        print("Invalid movie page.")

stage1()
stage2()