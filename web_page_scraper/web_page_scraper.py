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
        response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tags = soup.find('title')
        meta_desc = soup.find('meta', {'name': 'description'})

        if title_tags and meta_desc:
            title = title_tags.text.split('-')[0].strip()
            description = meta_desc.get('content', '').strip()
            print({"title": title, "description": description})
        else:
            print("Invalid movie page.")
    except Exception as e:
        print("Error:", str(e))
        print("Invalid movie page.")


def stage3():
    url = input("Input the URL.\n>")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("source.html", "wb") as f:
                f.write(response.content)
            print("Content saved.")
        else:
            print(f"The URL returned {response.status_code}.")
    except Exception as e:
        print("Error:", e)

def sanitize_filename():
    table = str.maketrans('', '', string.punctuation)
    title_clean = title.translate(table).replace('', '_')
    return title_clean.strip()

def stage4():
    url = input("Input the URL.\n>")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')
    saved_files = []

    for article in articles:
        article_type = article.find('span', {'data-test': 'article.type'})
        if article_type and article_type.text.strip() == 'News':
            tag_link = article.find('a', {'data-track-action': 'view article'})
            if tag_link:
                article_url = "https://www.nature.com/" + tag_link.get('href')
                article_resp = requests.get(article_url)
                article_soup = BeautifulSoup(article_resp.content, 'html.parser')

                title_tag = article_soup.find('title')
                body_tag = article_soup.find('div', class_='c-article-body')

                if not body_tag:
                    body_tag = article_soup.find('div', class_='article-item_body')

                if title_tag and body_tag:
                    title = sanitize_filename(title_tag.text)
                    text = body_tag.get_text(strip=True)
                    file_name = f"{title}.txt"
                    with open(file_name, "w", encoding="utf-8") as f:
                        f.write(text)
                    saved_files.append(file_name)

        print("Saved articles:", saved_files)


stage1()
stage2()
stage3()
stage4()