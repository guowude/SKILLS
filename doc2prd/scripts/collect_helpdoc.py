import requests
from bs4 import BeautifulSoup

class HelpDocCollector:
    def __init__(self, product_name):
        self.product_name = product_name
        self.sources = [
            'https://example.com/help/',  # Placeholder for actual help sources
            'https://another-example.com/docs/',
        ]

    def collect_help_docs(self):
        documents = []
        for source in self.sources:
            response = requests.get(source)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                docs = self.extract_docs(soup)
                documents.extend(docs)
            else:
                print(f'Failed to retrieve from {source}')
        return documents

    def extract_docs(self, soup):
        # Placeholder for document extraction logic
        # You will need to replace this with actual parsing logic based on your sources
        return [doc.get_text() for doc in soup.find_all('a') if self.product_name.lower() in doc.get_text().lower()]

if __name__ == '__main__':
    product = input('Enter product name: ')
    collector = HelpDocCollector(product)
    help_docs = collector.collect_help_docs()
    print('Collected Help Documentation:')
    for doc in help_docs:
        print(doc)