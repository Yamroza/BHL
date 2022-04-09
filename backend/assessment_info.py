import numpy as np
import pandas as pd

data = pd.read_csv('../data/train_data.csv')

def get_bble_locations() -> dict:
    return data[["BBLE", "Latitude", "Longitude"]].dropna().to_dict("records")

def get_bble_location(bble: str) -> dict:
    loc = data[data["BBLE"] == bble][["Latitude", "Longitude"]]
    return loc.to_dict("records")[0]

# accepts radius in degrees
def get_bbles_close_to(lat: float, lon: float, radius: float) -> list:
    return data[(data["Latitude"] - lat)**2 + (data["Longitude"] - lon)**2 < radius**2]["BBLE"].tolist()

def get_full_bble_info(bble: str) -> dict:
    return data[data["BBLE"] == bble].dropna(axis=1).to_dict("records")[0]

def get_bble_value(bble: str) -> float:
    return data[data["BBLE"] == bble]["FULLVAL"].tolist()[0]

def get_predicted_optimal_value(bble: str) -> float:
    # fancy algorithm here
    return None

def get_potential_profit(bble: str) -> float:
    # fancy algorithm here

    # profit = get_predicted_optimal_value(bble) - get_bble_value(bble)

    return 0
