import json


# Load the data from JSON file
with open('data/user_details.json') as file:
    config = json.load(file)

# Create the iterators
nationalities_iter = iter(config['nationalities'])
marital_iter = iter(config['marital_status'])
blood_type = iter(config['blood_type'])

# Function to get next item from an iterator safely
def get_next_value(iterator, name):
    try:
        return next(iterator)
    except StopIteration:
        print(f"Warning: No more values in {name}. Returning None.")
        return None

# Wrapper functions for specific fields
def get_nationality():
    return get_next_value(nationalities_iter, "nationalities")

def get_marital_status():
    return get_next_value(marital_iter, "marital_status")

def get_blood_type():
    return get_next_value(blood_type, "blood_type")




