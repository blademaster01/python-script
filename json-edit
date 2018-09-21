#! /usr/bin/env python

import json, os, logging
path = os.path.dirname(os.path.realpath(__file__))


# log
log_level = logging.INFO
logging.basicConfig(stream=sys.stdout, level=log_level,
    format='[%(levelname)s] [%(asctime)s] - %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')

# repos

# script

data = {}
filename = 'data.json'
with open(filename, 'r') as f:
    data = json.load(f)

print("Before edit")
print(data)

data["item3"] = {
    'active': True,
    'host': 'server3' 
    }

with open(filename, 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)
