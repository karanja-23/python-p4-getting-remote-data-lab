import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        body = requests.get(self.url)
        return body.content

    def load_json(self):
        content= self.get_response_body()
        return json.loads(content)