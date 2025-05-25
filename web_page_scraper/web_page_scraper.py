import os
import requests
import string
from bs4 import BeautifulSoup

def request():
    url = input("Input the URL: \n>")
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

request()