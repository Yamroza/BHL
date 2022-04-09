from typing import Optional

from fastapi import FastAPI

import assessment_info

app = FastAPI(title="DEMOLISHER 2000")

@app.get("/info/assessed/all")
def get_all_locations():
    return assessment_info.get_bble_locations()

@app.get("/info/assessed/location/{bble}")
def get_bble_location(bble: str):
    return assessment_info.get_bble_location(bble)

@app.get("/info/assessed/near")
def get_nearby_locations(lat: float, lon: float, radius: float):
    return assessment_info.get_bbles_close_to(lat, lon, radius)

@app.get("/info/assessed/{bble}")
def get_bble_info(bble: str):
    return assessment_info.get_full_bble_info(bble)

@app.get("/info/assessed/value/{bble}")
def get_bble_value(bble: str):
    return assessment_info.get_bble_value(bble)

@app.get("/info/assessed/predicted/{bble}")
def get_predicted_optimal_value(bble: str):
    return assessment_info.get_predicted_optimal_value(bble)

@app.get("/info/assessed/potential/{bble}")
def get_potential_profit(bble: str):
    return assessment_info.get_potential_profit(bble)
