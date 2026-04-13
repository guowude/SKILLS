import os
import requests
from bs4 import BeautifulSoup

class HelpDocCollector:
    def __init__(self, urls, local_files):
        self.urls = urls
        self.local_files = local_files
        self.collected_docs = []

    def collect_from_urls(self):
        for url in self.urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                self.collected_docs.append(soup.get_text())
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")

    def collect_from_local_files(self):
        for file_path in self.local_files:
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    self.collected_docs.append(file.read())
            else:
                print(f"File not found: {file_path}")

    def organize_docs(self):
        organized_docs = '\n'.join(self.collected_docs)
        return organized_docs

if __name__ == '__main__':
    urls = ['https://example.com/help1', 'https://example.com/help2']  # example URLs
    local_files = ['local_doc1.txt', 'local_doc2.txt']  # example local files
    collector = HelpDocCollector(urls, local_files)
    collector.collect_from_urls()
    collector.collect_from_local_files()
    organized_docs = collector.organize_docs()
    print(organized_docs)