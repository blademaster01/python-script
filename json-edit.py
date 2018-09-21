#! /usr/bin/env python

import json, os, logging, sys
path = os.path.dirname(os.path.realpath(__file__))


# log
log_level = logging.INFO
logging.basicConfig(stream=sys.stdout, level=log_level,
    format='[%(levelname)s] [%(asctime)s] - %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')

# repos
repo1 = '/project2'

filename = {}
filename['file1'] = repo1+'/data.json'

# script

data = {}

with open(path+filename['file1'], 'r') as f:
    data = json.load(f)

data["item3"] = {
    'active': True,
    'host': 'server3' 
    }

data["item2"]["active"] = True

#os.remove(filename)
with open(path+filename['file1'], 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)
