from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


import assessment_info

app = FastAPI(title="DEMOLISHER 2000")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/info/assessed/all")
def get_all_locations():
    return assessment_info.get_bble_locations()

@app.get("/info/assessed/location/{bble}")
def get_bble_location(bble: str):
    return assessment_info.get_bble_location(bble)

@app.get("/info/assessed/near")
def get_nearby_locations(lat: float, lon: float, radius: float):
    return assessment_info.get_bbles_close_to(lat, lon, radius)

@app.get("/info/assessed/closest")
def get_closest_location(lat: float, lon: float):
    return assessment_info.get_closest_location(lat, lon)

@app.get("/info/assessed/top/{count}")
def get_top_locations(count: int):
    return assessment_info.get_top_locations(count)

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
