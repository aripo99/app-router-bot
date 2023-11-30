import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for link in soup.find_all("a", href=True):
        full_url = urljoin(base_url, link["href"])
        if full_url.startswith(base_url):
            links.add(full_url)
    return links


def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator=" ", strip=True)


def save_text_to_file(text, url, directory="data_generation/output/crawled_pages"):
    parsed_url = urlparse(url)
    filename = parsed_url.path.split("/")[-1]
    if not filename:
        filename = "index"

    os.makedirs(directory, exist_ok=True)

    filepath = os.path.join(directory, f"{filename}.txt")
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Saved: {filepath}")


def crawl(start_url, num_pages):
    visited = set()
    to_visit = {start_url}
    num_pages_visited = 0

    while to_visit and num_pages_visited < num_pages:
        num_pages_visited += 1
        url = to_visit.pop()
        if url in visited:
            continue

        print(f"Crawling: {url}")
        visited.add(url)
        html = fetch_page(url)
        if html:
            text = extract_text(html)
            save_text_to_file(text, url)
            for link in extract_links(html, start_url):
                if link not in visited:
                    to_visit.add(link)


start_url = "https://nextjs.org/docs/app/"
crawl(start_url, 5)
