import React from 'react';
import { MoviesGrid } from "./MoviesGrid";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import styles from "./App.module.css";

import movies from "./movies.json";
import Navbar from './components/header/navbar';

export function App() {
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 3,
    };

    return (
        <div>
            <Navbar />
            <header>
                <h1 className={styles.title}>Movies</h1>
            </header>
            <main>
                {/* Carrusel */}
                <Slider {...settings} style={{ width: '80%', margin: '0 auto' }}>
                    {movies.map((movie) => (
                        <div key={movie.id}>
                            {/* Puedes renderizar el contenido del carrusel aquí */}
                            <img src={`https://image.tmdb.org/t/p/w300${movie.poster_path}`} alt={movie.title} />
                            <h3 style={{ textAlign: 'start', fontSize: '20px' }}>{movie.title}</h3>
                        </div>
                    ))}
                </Slider>

                {/* Grid de películas */}
                <MoviesGrid />
            </main>
        </div>
    );
}
