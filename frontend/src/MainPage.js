import './mainPage.css';
import { useEffect } from 'react';
import ball from './resources/ball.png'
import background from './resources/new_york.webp'
import frontground from './resources/frontground.png'
import building from './resources/building.png'
import demolish_1 from './resources/demolish_1.jpg'
import demolish_2 from './resources/demolish_2.jpg'
import demolish_3 from './resources/demolish_3.jpg'

function MainPage() {
  useEffect(() => {
    window.addEventListener('scroll', () => {
      let value = window.scrollY;
      const background = document.getElementById('background')
      background.style.left = value * 0.15 + 'px';
      const ball = document.getElementById('wrecking_ball')
      ball.style.transform = 'rotate(-' + (value * 0.004)**2 + 'rad) scale(1.5)'
      const images_text = document.getElementById('images_text')
      images_text.style.marginTop = value * 0.6 + 'px';
    })
  }, [])

  return (
    <div className="mainPage_main">
      <div className='mainPage_main-navbar'>
        <h1 className='mainPage_main-navbar_logo'>
          DESTRUKTPOL
        </h1>
        <div className='mainPage_main-navbar-choices'>
          <h4>About</h4>
          <h4>QnA</h4>
          <h4>Contact us</h4>
        </div>
      </div>
      <div className='mainPage_main-images'>
        <img id='background' className='mainPage_main-background' src={background} alt='background'/>
        <div id='images_text' className='mainPage_main-images_text'>HELP US DESTROY NEW YORK</div>
        <img id='frontground' className='mainPage_main-frontground' src={frontground} alt='frontground'/>
        <img id='building' className='mainPage_main-building' src={building} alt='building'/>
        <div className='mainPage_main-map_link' onClick={() => {window.location = '/map'}}>
          <h1>Check it out</h1>
        </div>
      </div>
      <img id='wrecking_ball' className='mainPage_main-wrecking_ball' src={ball} alt='ball'/>
      <div className='mainPage_main-section'>
        <h1 style={{textAlign: 'left'}}>What do we mean?</h1>
        <p>"I bet that's another marketing trick just to catch my attention". Well you're not wrong. But at the same time it is not a scam. We actually aim to destroy the Big mainPagele (in a legal way). <br/>
        What we're trying to say is that you can actually demolish some of the buildings to make place for the newer, bigger, more expensive ones. <br/>
        The catch is that you have to pay for these in advance aswell but we recon that since you can afford to literally demolish a building from the streets of New York,
        you can probably afford to build one aswell. Why not give it a try?<br/></p>
        <h1 style={{textAlign: 'left'}}>And just a quick glimpse:</h1>
        <div className='mainPage_main-section_demolishion'>
          <img src={demolish_1} alt='demolish_1'></img>
          <img src={demolish_2} alt='demolish_2'></img>
          <img src={demolish_3} alt='demolish_3'></img>
        </div>
        <h1 style={{textAlign: 'left'}}>This is the vision of future that we want to pursue. Help us renovate the streets of NYC today!</h1>
      </div>
    </div>
  );
}

export default MainPage;
