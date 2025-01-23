import json
from turtle import config_dict

# Import JSON
with open('data/user_details.json') as file:
    config = json.load(file)

nationalities_iter = iter(config['nationalities'])
marital_iter = iter(config['marital_status'])
blood_type = iter(config['blood_type'])

def get_nationality():
    try:
        return next(nationalities_iter)
    except StopIteration:
        return None

def get_marital_status():
    try:
        return next(marital_iter)
    except StopIteration:
        return None

def get_blood_type():
    try:
        return next(blood_type)
    except StopIteration:
        return None




