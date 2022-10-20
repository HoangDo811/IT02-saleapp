import json
from saleapp import app


def load_categories():
    with open('date/categories.json',encodings='utf-8') as f:
        return json.load(f)