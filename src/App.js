import './App.css';
import Nav from './components/Nav'
import Home from './components/Home'
import Noticias from './components/Noticias'
import Estadisticas from './components/Estadisticas';
import CompraVenta from "./components/CompraVenta";
import Plantilla from "./components/Plantilla";
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';



function App() {
  return (
    <Router>
      <div className="App">
          <Nav />
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/Noticias" exact component={Noticias} />
            <Route path="/Estadisticas" exact component={Estadisticas} />
            <Route path="/CompraVenta" exact component={CompraVenta} />
            <Route path="/Plantilla" exact component={Plantilla}/>

          </Switch>
      </div>
    </Router>
  );
}

export default App;
