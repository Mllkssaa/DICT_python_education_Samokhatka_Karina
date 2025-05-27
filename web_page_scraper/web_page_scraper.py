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
    except Exception:
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

def sanitize_filename(title):
    valid_chars = "-_() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in title if c in valid_chars).replace(' ', '_')


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
                    body_tag = article_soup.find('div', class_='article-item__body')

                if title_tag and body_tag:
                    title = sanitize_filename(title_tag.text)
                    text = body_tag.get_text(strip=True)
                    file_name = f"{title}.txt"
                    with open(file_name, "w", encoding="utf-8") as f:
                        f.write(text)
                    saved_files.append(file_name)

        print("Saved articles:", saved_files)


def stage5():
    while True:
        user_input = input("Enter number of pages:\n> ").strip()
        if user_input.isdigit() and int(user_input) > 0:
            num_pages = int(user_input)
            break
        else:
            print("Please enter a valid positive integer.")

    article_type = input("Enter article type (e.g., News, Research Highlight, etc.):\n> ").strip()

    base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page="

    for page in range(1, num_pages + 1):
        os.makedirs(f"Page_{page}", exist_ok=True)
        url = f"{base_url}{page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')

        for article in articles:
            tag_type = article.find('span', {'data-test': 'article.type'})
            if tag_type and tag_type.text.strip() == article_type:
                link_tag = article.find('a', {'data-track-action': 'view article'})
                if link_tag:
                    article_url = "https://www.nature.com" + link_tag.get('href')
                    article_resp = requests.get(article_url)
                    article_soup = BeautifulSoup(article_resp.content, 'html.parser')

                    title_tag = article_soup.find('title')
                    body_tag = article_soup.find('div', class_='c-article-body')
                    if not body_tag:
                        body_tag = article_soup.find('div', class_='article-item__body')

                    if title_tag and body_tag:
                        title = sanitize_filename(title_tag.text)
                        text = body_tag.get_text(strip=True)
                        file_path = os.path.join(f"Page_{page}", f"{title}.txt")
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(text)

        print("Saved all articles.")


stage1()
stage2()
stage3()
stage4()
stage5()