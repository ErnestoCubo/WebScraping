import React from 'react';
import axios from 'axios';

// Estructura de los datos en React
export default class FetchEquipo extends React.Component {
    state = {
        loading: true,
        equipos: []
    };

    // Inicio de la petición asincrona a la API
    async componentDidMount() {
        const url = "http://localhost:8000/api/Equipos/?format=json";
        // Await de la función para esperar a la respuesta asincrona y obtener los datos
        const response = await axios.get(url);
        const data = await response.data;
        // Cambio del estado de los datos porque llegado aquí ya se han recibido
        this.setState({ equipos: data, loading: false });

    }

    render() {
        // Mostrará un escenario dependiendo de si estan o no cargados los datos
        if (this.state.loading == true) {
            return (
                <div>
                    <p>Loading...</p>
                </div>
            );
        }
        else if (!this.state.equipos.length == null) {
            return (
                <div>
                    <p>No se encontraron datos de los equipos</p>
                </div>
            );
        }
        else{
            // Mapeo del array de equipos por cada uno de los equipos
            const equiposJSx = [];
            this.state.equipos.forEach(equipo => {
                equiposJSx.push(
                    // Componente raíz del grupo al que se le pasa una key unica en este caso ek nombre del equipo
                    <div class="col-3" key={equipo.Equipo}>
                        <h1>{equipo.Equipo}</h1>
                        <h2>Jugadores: {equipo.Jugadores}</h2>
                        <h2>Edad media: {equipo.EdadMedia}</h2>
                        <h2>Valor total: {equipo.ValorTotal}</h2>
                        <h2>Valor Medio: {equipo.ValorMedio}</h2>
                    </div>
                );
            });

            return (
                    <div style={{backgroundImage: "../../public/images/fondo.jpeg"}} class="row">
                        {equiposJSx}
                    </div>
            );
        }
    }
}
