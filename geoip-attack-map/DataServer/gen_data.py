from elasticsearch import Elasticsearch
import random, syslog
import json
from time import sleep
from const import PORTMAP
import os


es = Elasticsearch('http://localhost:9200')

# for i, doc in enumerate(test):
#     es.index(index = doc['_index'], id = i, body = doc['_source'])

test_index = 'logstash-2022.07.13-000008'
for i in range(99):
    sample = es.get(index = test_index, id = i)
    rand_attacks = list(PORTMAP.keys())
    random_num = random.choice(rand_attacks)
    try:
        source_ip = sample["_source"]["src_ip"]
        destination_ip = sample["_source"]["dest_ip"]
        source_p = sample["_source"]["src_port"]
        destination_p = sample["_source"]["dest_port"]
    except:
        continue
    type_of_attack = random.choice(list(PORTMAP.values()))
    cve_attack = f"CVE:{random.randrange(1,2000)}:{random.randrange(100,1000)}"
    test = f"{source_ip},{destination_ip},{source_p},{destination_p},{type_of_attack},{cve_attack}"
    
    syslog.syslog(test)
    print(test)
    sleep(1)
