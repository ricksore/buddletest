import os
from datetime import datetime
from datetime import timedelta
from datetime import timezone

from urllib.parse import urlencode
import requests


API_URL = 'https://api.twitter.com/2/tweets/search/recent'

BEARER_TOKEN = os.environ['BEARER_TOKEN']


class Document:
    """
    Fake object for storing documents.
    """

    def __init__(self, **kwargs):
        for kwarg, value in kwargs.items():
            setattr(self, kwarg, value)


class NoSQLClient:
    """
    Fake client for storing NoSQL documents.
    """

    def __init__(self, uri: str, key: str):
        self.uri = uri
        self.key = key
        self.database = None
        self.container = None
        self.documents = []

    def set_database(self, database_name: str):
        self.database = database_name

    def set_container(self, container_name: str):
        self.container = container_name

    def insert_document(self, document: Document):
        self.documents.append(document)

client = NoSQLClient(os.environ.get('account_uri', 'dummy'), os.environ.get('account_key', 'dummy'))
client.set_database('twitter')
client.set_container('tweets')

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json'
}

end_time = datetime.now(timezone.utc) - timedelta(days=1)

params = {'query': 'from:BillGates', 'end_time': end_time.isoformat()}

response = requests.get(f'{API_URL}?{urlencode(params)}', headers=headers)
data = response.json()['data']

for row in data:
    document = Document(**row)
    client.insert_document(document)
