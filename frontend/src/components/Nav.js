import React from 'react';
import {Link} from 'react-router-dom'

function Nav() {
    return(
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navMainMenu" aria-controls="navMainMenu">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div id="navMainMenu" class="navbar-collapse collapse">
                <div class="navbar-nav ml-auto">
                    <Link to='/' className="nav-item nav-link active">Home</Link>
                    <Link to='/Noticias' className="nav-item nav-link">Noticias</Link>
                    <Link to='/Login' className="nav-item nav-link">Login</Link>
                </div>
            </div>
        </nav>

    );

}

export default Nav;