import json
import os 
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')
f = open("Search_query.json")
test = json.load(f)

for i, doc in enumerate(test):
    es.index(index = doc['_index'], id = i, body = doc['_source'])

