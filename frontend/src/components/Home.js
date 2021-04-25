import React from 'react';
import axios from 'axios';
import './Home.css';

// Estructura de los datos en React
export default class FetchEquipo extends React.Component {
    state = {
        loading: true,
        equipos: [],
        escudos: []
    };

    // Inicio de la petición asincrona a la API
    async componentDidMount() {
        var url = "http://localhost:8000/api/Equipos/?format=json&search=11-02-2021";
        // Await de la función para esperar a la respuesta asincrona y obtener los datos
        var response = await axios.get(url);
        const equiposData = await response.data;

        url = "http://localhost:8000/api/Escudos/?format=json";
        response = await axios.get(url);
        const escudosData = await response.data;

        // Cambio del estado de los datos porque llegado aquí ya se han recibido
        this.setState({ equipos: equiposData, escudos: escudosData, loading: false });
    }

    render() {
        // Mostrará un escenario dependiendo de si estan o no cargados los datos
        if (this.state.loading === true) {
            return (
                <div className="card-container">
                    <p>Loading...</p>
                </div>
            );
        }
        else if (!this.state.equipos.length === null) {
            return (
                <div className="card-container">
                    <p>No se encontraron datos de los equipos</p>
                </div>
            );
        }
        else {
            // Mapeo del array de equipos por cada uno de los equipos
            const equiposJSx = [];
            for (let index = 0; index < this.state.equipos.length; index++) {
                console.log(this.state.escudos[0]);
                equiposJSx.push(
                    <div className='card-container' key={this.state.equipos.Equipo}>
                        <div className='image-container'>
                            <img src={this.state.escudos[index].Link}></img>
                        </div>
                        <div className='card-content'>
                            <div className='card-title'>
                                <h3>{this.state.equipos[index].Equipo}</h3>
                            </div>
                        </div>
                    </div>
                )

            }

            return (
                <div className="row">
                    {equiposJSx}
                </div>
            );
        }
    }
}
