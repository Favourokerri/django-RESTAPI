#this is our basic client [ api consumer ]
import requests
"""
    Http request -> returns html
    rest api Http request -> returns json
"""
endpoint = 'http://localhost:8000/api'
#endpoint = 'http://httpbin.org/anything'

get_response = requests.get(endpoint, params={'abc': 123}, json={"query": "hello world"})
print(get_response.json()['message'])
