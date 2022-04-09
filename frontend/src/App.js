import React from 'react'
import MainPage from './MainPage'
import {Route, Switch, useRouteMatch} from 'react-router-dom'
import Map from './Map/Map'

const App = () => {
    let { path } = useRouteMatch();
    console.log(path)

  return (
  <Switch>
    <Route path={`${path}map`} render={ () => {
        return <Map/>
    }}>
    </Route>
    <Route path='*' render={ () =>
            <MainPage/>
          }>
    </Route>
  </Switch>
  )
}

export default App