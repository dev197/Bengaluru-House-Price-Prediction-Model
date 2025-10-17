import json
import pickle
import numpy as np

# Global variables to hold model and metadata
__locations = None
__data_columns = None
__model = None

# Function to estimate price
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    # Prepare input array
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

# Function to get all locations
def get_location_names():
    if __locations:
        return [loc.title() for loc in __locations]  # Capitalized names for front-end
    return []

# Function to load model and columns
def load_saved_artifacts():
    print('Loading saved artifacts...')
    global __data_columns
    global __locations
    global __model

    # Load column info
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    # Load trained model
    with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print('Artifacts loaded successfully!')

# For testing
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    # print(get_estimated_price('Indiranagar', 1500, 3, 3))
