from typing import Optional

from fastapi import FastAPI

import assessment_info
import pluto_info

app = FastAPI(title="DEMOLISHER 2000")

@app.get("/info/assessed/all")
def get_all_locations():
    return assessment_info.get_bble_locations()

@app.get("/info/assessed/location/{bble}")
def get_bble_location(bble: str):
    return assessment_info.get_bble_location(bble)

@app.get("/info/assessed/{bble}")
def get_bble_info(bble: str):
    return assessment_info.get_full_bble_info(bble)

@app.get("/info/assessed/near")
def get_nearby_locations(lat: float, lon: float, radius: float):
    return assessment_info.get_bbles_close_to(lat, lon, radius)

@app.get("/info/assessed/value/{bble}")
def get_bble_value(bble: str):
    return assessment_info.get_bble_value(bble)

@app.get("/info/assessed/predicted/{bble}")
def get_predicted_optimal_value(bble: str):
    return assessment_info.get_predicted_optimal_value(bble)

@app.get("/info/assessed/potential/{bble}")
def get_potential_profit(bble: str):
    return assessment_info.get_potential_profit(bble)

@app.get("/info/pluto/closest")
def get_closest_pluto_location(lat: float, lon: float):
    return pluto_info.get_closest_pluto_location(lat, lon)

@app.get("/info/pluto/lots/{borough}/{block}")
def get_lots_in_block(borough: int, block: int):
    return pluto_info.get_lots_in_block(borough, block)

@app.get("/info/block/predicted/{borough}/{block}")
def get_block_value(borough: int, block: int):
    return get_block_value(borough, block)

def get_block_value(borough: int, block: int) -> Optional[float]:
    assessed_lots = assessment_info.data[assessment_info.data["BORO"] == borough][assessment_info.data["BLOCK"] == block]
    if assessed_lots["FULLVAL"].empty:
        return None

    all_lots = pluto_info.get_lots_in_block(borough, block)

    print(all_lots)

    total_value = 0

    lot_index = all_lots.columns.get_loc("lot") + 1

    for lot in all_lots.itertuples():

        lotinfo = assessed_lots[assessed_lots["LOT"] == lot[lot_index]]
        print(lotinfo)

        if lotinfo.empty:
            total_value += pluto_info.predict_current_lot_value(borough, block, lot[lot_index])
        else:
            total_value += lotinfo["FULLVAL"].sum()

    return total_value