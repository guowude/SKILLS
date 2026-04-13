import datetime
import json

class PRDGenerator:
    def __init__(self, product_name, description, help_docs):
        self.product_name = product_name
        self.description = description
        self.help_docs = help_docs

    def generate_prd(self):
        prd = {
            'Product Name': self.product_name,
            'Description': self.description,
            'Help Documentation': self.help_docs,
            'Generated On': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }
        return json.dumps(prd, indent=4)

if __name__ == '__main__':
    product_name = input('Enter the product name: ')
    description = input('Enter the product description: ')
    help_docs = input('Enter the collected help documentation: ')
    generator = PRDGenerator(product_name, description, help_docs)
    prd_document = generator.generate_prd()
    print(prd_document)