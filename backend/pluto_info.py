import numpy as np
import pandas as pd

data = pd.read_csv('../data/pluto_21v4.csv')

def get_lots_in_block(borough: int, block: int) -> list:
    return data[data["borocode"] == borough][data["block"] == block]

def get_closest_pluto_location(lat: float, lon: float) -> dict:
    return data[(data["latitude"] - lat)**2 + (data["longitude"] - lon)**2].dropna(axis=1).to_dict("records")[0]

def predict_current_lot_value(borough: int, block: int, lot: int) -> float:
    # fancy algorithm here
    return 0

def predict_best_lot_value(borough: int, block: int, lot: int) -> float:
    # fancy algorithm here
    return 0

def predict_potential_profit(borough: int, block: int, lot: int) -> float:
    # fancy algorithm here
    return 0