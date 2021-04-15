import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom';

function Tweet() {
    useEffect( ()=> {
        fetchItems();
    }, []);

    const [items, setItems] = useState([]);

    const fetchItems = async() => {
        const data = await fetch('/tweets');
        const items = await data.json();
        setItems(items);
    };

    return(
        <section>
            {
                items.map(item => (
                    <div>
                        <p>{item.jugador}</p>
                        <p>{item.edad}</p>
                        <p>{item.pais}</p>
                    </div>
                    
                ))
            }
        </section>
    );
}

export default Tweet;