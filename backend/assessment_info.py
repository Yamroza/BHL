import numpy as np
import pandas as pd
import xgboost

import ml_model

data = pd.read_csv('../data/train_data.csv')
prepared_data = ml_model.prepare_data(pd.read_csv('../data/train_data.csv'))
x, y = ml_model.divide_data(prepared_data)

classes = x["BLDGCL"].unique()
class_names = data["BLDGCL"].str[0].unique()
model = xgboost.XGBRegressor()
model.load_model('../model.json')

def get_bble_locations() -> dict:
    return data[["BBLE", "Latitude", "Longitude"]].dropna().to_dict("records")

def get_bble_location(bble: str) -> dict:
    loc = data[data["BBLE"] == bble][["Latitude", "Longitude"]]
    return loc.to_dict("records")[0]

# accepts radius in degrees
def get_bbles_close_to(lat: float, lon: float, radius: float) -> list:
    return data[(data["Latitude"] - lat)**2 + (data["Longitude"] - lon)**2 < radius**2][["BBLE", "Latitude", "Longitude"]].to_dict("records")

def get_full_bble_info(bble: str) -> dict:
    return data[data["BBLE"] == bble].dropna(axis=1).to_dict("records")[0]

def get_bble_value(bble: str) -> float:
    return data[data["BBLE"] == bble]["FULLVAL"].tolist()[0]

def get_predicted_optimal_value(bble: str) -> dict:
    row = x[data['BBLE'] == bble]
    res = ml_model.best_bldgcl(model, classes, row)
    return {'best_class': class_names[res['best']], 'best_value': res['money']}

def get_potential_profit(bble: str) -> float:
    row = x[data['BBLE'] == bble]
    res = ml_model.best_bldgcl(model, classes, row)
    base_value =  get_bble_value(bble)
    new_value = res['money']


    return {'best_class': class_names[res['best']], 'profit': new_value - base_value, 'base_value': base_value, 'new_value': new_value}
