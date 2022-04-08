from typing import Optional

from fastapi import FastAPI

import info

app = FastAPI(title="DEMOLISHER 2000")

@app.get("/info/all")
def get_all_locations():
    return info.get_bble_locations()

@app.get("/info/bble/location/{bble}")
def get_bble_location(bble: str):
    return info.get_bble_location(bble)

@app.get("/info/bble/{bble}")
def get_bble_info(bble: str):
    return info.get_full_bble_info(bble)

@app.get("/info/near")
def get_nearby_locations(lat: float, lon: float, radius: float):
    return info.get_bbles_close_to(lat, lon, radius)

@app.get("/info/bble/value/{bble}")
def get_bble_value(bble: str):
    return info.get_bble_value(bble)

@app.get("/info/bble/predicted/{bble}")
def get_predicted_optimal_value(bble: str):
    return info.get_predicted_optimal_value(bble)

@app.get("/info/bble/potential/{bble}")
def get_potential_profit(bble: str):
    return info.get_potential_profit(bble)