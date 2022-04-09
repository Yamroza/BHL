import React, { useState } from 'react'
import './map.css'
import DeckGL from '@deck.gl/react';
import {LineLayer} from '@deck.gl/layers';
import {StaticMap} from 'react-map-gl';

const  myAccessToken = 'pk.eyJ1IjoibmV3dG9uZWlybyIsImEiOiJjbDFyZDhlY3gwc2JhM2NvYTVlYzF3bDJ4In0.xEEsrH-weM3juIcyV8IzjQ'

// Viewport settings
const INITIAL_VIEW_STATE = {
  latitude: 40.730610,
  longitude: -73.535242,
  zoom: 9,
  pitch: 0,
  bearing: 0
};


const Map = () => {
  const [unraveled, setUnraveled] = useState(false)
  const [longLat, setLongLat] = useState([0, 0])
  const [address, setAddress] = useState({country: '', city: '', postal_code: '', street: ''})
  const data = [
  {sourcePosition: [-122.41669, 37.7853], targetPosition: [-122.41669, 37.781]}
];
  const layers = [
    new LineLayer({id: 'line-layer', data})
  ];

  const handleClick = async (e) => {
    setLongLat([e.coordinate[0].toFixed(7), e.coordinate[1].toFixed(7)])
     const response = await fetch(`https://api.mapbox.com/geocoding/v5/mapbox.places/${e.coordinate[0]},${e.coordinate[1]}.json?types=address&access_token=${myAccessToken}`);
        const data = await response.json();
        if (data.features.length > 0)
        {
            const address = data.features[0].place_name.split(', ')
            var postal_code_city = address[1].split(' ')
            if (postal_code_city.length === 1){
                postal_code_city = ['-', postal_code_city[0]]
            }
            setAddress({country: address[3], city: postal_code_city[1], postal_code: postal_code_city[0], street: address[0]})
        }

  }

  return (
    <div className='map_main'>
      <div className='map_main-window'>
        <div className={unraveled?'map_main-text_unraveled':'map_main-text'} onClick={() => setUnraveled(false)}>
          <h1>It's really simple</h1>
          <p>Just click on the map or type in the data manually</p>
          <div className='map_map-form'>
            <div className='geocordinputs'>
                      <div className='input-label'>
                        <label htmlFor='longitude'>Longitude</label>
                        <input id='longitude' min={-180} max={80} value={longLat[0]} onChange={(e) => setLongLat((prev) => {return [e.target.value, prev[1]]})}/>
                      </div>
                      <div className='input-label'>
                        <label htmlFor='latitude'>Latitude</label>
                        <input id='latitude' min={-90} max={90}  value={longLat[1]} onChange={(e) => setLongLat((prev) => {return [e.target.value, prev[0]]})}/>
                      </div>
              </div>
                <div className='address-inputs'>
                  <div className='input-label'>
                      <label htmlFor='country'>Country</label>
                      <input id='country' type='text' value={address.country} onChange={(e) => {setAddress((prev) => {return {...prev, country: e.target.value}})}}/>
                  </div>
                  <div className='input-label'>
                      <label htmlFor='city'>City</label>
                      <input id='city' type='text' value={address.city} onChange={(e) => {setAddress((prev) => {return {...prev, city: e.target.value}})}} />
                  </div>
                  <div className='input-label'>
                      <label htmlFor='street'>Street</label>
                      <input id='street' type='text' value={address.street} onChange={(e) => {setAddress((prev) => {return {...prev, street: e.target.value}})}}/>
                  </div>
                  <div className='input-label'>
                      <label htmlFor='postal-code'>Postal code</label>
                      <input id='postal-code' type='text' value={address.postal_code} onChange={(e) => {setAddress((prev) => {return {...prev, postal_code: e.target.value}})}}/>
                  </div>
                </div>
              </div>
        </div>
        <div className={unraveled?'map_main-map_unraveled':'map_main-map'} onClick={() => setUnraveled(true)}>
          <DeckGL onClick={(e) => handleClick(e)}
            initialViewState={INITIAL_VIEW_STATE}
            controller={true}
            layers={layers}
          >
            <StaticMap mapboxApiAccessToken={myAccessToken} />
          </DeckGL>
        </div>
      </div>
    </div>
  )
}

export default Map