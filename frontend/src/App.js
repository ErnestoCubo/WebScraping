import './App.css';
import Nav from './components/Nav'
import Home from './components/Home'
import Noticias from './components/Noticias'
import Login from './components/Login'

import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';


function App() {
  return (
    <Router>
      <div className="App">
          <Nav />
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/Noticias" exact component={Noticias} />
            <Route path="/Login" exact component={Login} />
          </Switch>
      </div>
    </Router>
  );
}

export default App;
