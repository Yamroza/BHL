import './App.css';
import { useEffect } from 'react';
import { Fetch } from './Fetch/Fetch';
import big_apple from './resources/big_apple.jpg'

const fetchData = async () => {
  const data = await Fetch.get('')
  console.table(data)
}

function App() {
  useEffect(() => {
    fetchData()
  }, [])

  return (
    <div className="app_main">
      <div className='app_main-window'>
        
      </div>
    </div>
  );
}

export default App;
