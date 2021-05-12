import React from "react";
import axios from "axios";

export default class Compraventa extends React.Component {
  state = {
    loading: true,
    data: [],
    isComprado: [],
    cartera: 500,
    equipo: [],
  };

  componentWillMount() {
    import("./CompraVenta.css");
  }

  async componentDidMount() {
    const url = "http://localhost:8000/api/Jugadores/?search=25-04-2021";
    // Await de la función para esperar a la respuesta asincrona y obtener los datos

    //equipos
    const response = await axios.get(url);
    const data = await response.data;
    console.log(data);

    this.setState({
      loading: false,
      data: data,
    });
    this.state.data.forEach((any, index) => {
      this.state.isComprado[index] = false;
    });
  }




  buttonHandler(index, precio) {
    if (this.state.isComprado[index] === true) {
      this.state.cartera += precio;
      this.state.isComprado[index] = false;
      this.className="btn btn-danger";

      this.forceUpdate();
      return 1;
    } else {
      this.state.cartera -= precio;
      this.state.isComprado[index] = true;
      this.className="btn btn-success";
      this.forceUpdate();
      return 0;
    }
  }






  render() {
    // Mostrará un escenario dependiendo de si estan o no cargados los datos
    if (this.state.loading === true) {
      return (
        <div className="card-container">
          <p>Loading...</p>
        </div>
      );
    } else if (!this.state.data.length === null) {
      return (
        <div className="card-container">
          <p>No se encontraron datos de los jugadores</p>
        </div>
      );
    } else {
      const compraventaJSx = [];
      const equipo = [];
      console.log(equipo);
      this.state.data.forEach((jugador, index) => {
        compraventaJSx.push(
          <div className="">
            <div className="card-container" key={jugador.jugador}>
              <div className="card-content">
                <button
                  className={
                    this.state.isComprado ?"btn btn-success" : "btn btn-danger"
                  }    
                  onClick={() => {
                    if (this.buttonHandler(index, jugador.precio) === 0) {
                      this.state.equipo.push(jugador.jugador);
                    } else {
                      this.state.equipo.splice(
                        this.state.equipo.indexOf(jugador.jugador),
                        1
                      );
                    }
                    console.log(this.state.equipo);
                  }}
                >
                  {jugador.jugador}--{jugador.precio}millones --
                  {jugador.equipos}
                </button>
              </div>
            </div>
          </div>
        );
      });
      return (
        <section className="container">
          <div className="row">
            <h3>tienes {this.state.cartera} millones </h3>
            
            <div className="Container">{compraventaJSx}</div>
            
          </div>
        </section>
      );
    }
  }
}
