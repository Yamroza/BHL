import React, { useState, useRef, useEffect } from 'react'
import './map.css'
import DeckGL from '@deck.gl/react';
import {ScatterplotLayer} from '@deck.gl/layers';
import {StaticMap} from 'react-map-gl';
import { Fetch } from '../Fetch/Fetch';

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
  const [best, setBest] = useState([])
  const [unraveled, setUnraveled] = useState(false)
  const [bestShow, setBestShow] = useState(false)
  const [longLat, setLongLat] = useState([0, 0])
  const [address, setAddress] = useState({country: '', city: '', postal_code: '', street: ''})
  const [layer, setLayer] = useState('')
  const iconL = useRef(null)

  useEffect(()=>{
    async function getBest(){
      const response = await Fetch.get(`info/assessed/top/5/near?lat=40&lon=-74&radius=0.589`)
      setBest(response.data)
    }
    getBest()
  },[])

  useEffect(() => {
    var layer = new ScatterplotLayer({
      id: 'scatterplot-layer',
      data: [{coordinates: longLat}],
      _dataDiff: (newData, odlData) => [...newData],
      pickable: true,
      opacity: 0.7,
      radiusScale: 30,  // make the dots visible or darker background
      radiusMinPixels: 15, // make the dots visible or darker background
      radiusMaxPixels: 100,
  
      getPosition: d => [d.coordinates[1], d.coordinates[0]], // -> Essential Change here
  
      getColor: d => [20, 20, 20], // make the dots visible or darker background)
      onClick: (info, event) => console.log('Clicked:', info, event)
    })
    setLayer(layer)
  }, [longLat])

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
      const response2 = await Fetch.get(`info/assessed/top/5/near?lat=${longLat[1]}&lon=${longLat[0]}&radius=0.1`)
      setBest(response2.data)
      // const response2 = await Fetch.get(`http://localhost:8000/info/assessed/closest?lat=${longLat[1]}&lon=${longLat[0]}`)
      // console.log(response2)

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
          <DeckGL ref={iconL}
            onClick={(e) => handleClick(e)}
            initialViewState={INITIAL_VIEW_STATE}
            controller={true}
            layers={[layer]}
          >
            <StaticMap mapboxApiAccessToken={myAccessToken} />
          </DeckGL>
        </div>
        <div className={`map_main-best_properties ${bestShow && 'show'}`} onClick={() => setBestShow((prev) => !prev)}>
          <div className='map_main-best_properties-button'>
            <h1>{'<'}</h1>
          </div>
          <div className='best_list'>
            <h1>Hot buildings near You</h1>
            {best.length > 0 && best.map((property, n) => {
              return <div key={property.bble} className={`${(n+1)%2 === 0 && "colour_header"} best-property`}>
                    <h2>{n+1}. {property.address}</h2>
                    <h4>{property.owner}</h4>
                    <h2>${property.profit}</h2>
                </div>
            })}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Map