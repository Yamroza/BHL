import React, { useState } from 'react'
import './map.css'

const Map = () => {
  const [unraveled, setUnraveled] = useState(false)

  return (
    <div className='map_main'>
      <div className='map_main-window' onClick={() => {setUnraveled((prev) => !prev)}}>
        <div className={`map_main-text ${unraveled && 'map_main-text_unraveled'}`}>
          <h1>It's really simple</h1>
        </div>
        <div className={`map_main-map ${unraveled && 'map_main-map_unraveled'}`}>

        </div>
      </div>
    </div>
  )
}

export default Map