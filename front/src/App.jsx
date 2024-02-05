import React, { useEffect, useState } from 'react';
import { MoviesGrid } from "./MoviesGrid";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import styles from "./App.module.css";

import 'bulma/css/bulma.min.css';
import movies from "./movies.json";
import Navbar from './components/header/navbar';
import { Pagination } from './components/header/Pagination';



export function App() {
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 3,
    };

    // variables para paginado conectado a back
    const [movie, setMovies] = useState([]);

    const totalMovies = movie.length

    const [moviesPerPage, setMoviesPerPage] = useState(6);
    const [currentPage, setCurrentPage] = useState(1);

    const lastIndex = currentPage * moviesPerPage // = 1 * 6 = 6
    const firstIndex = lastIndex - moviesPerPage // = 6 - 6 = 0

    // Obtener datos de la api desde el back
    const movieList = async () => {
        const data = await fetch('liga a back');
        const movie = await data.json();

        setMovies(movie);
    }

    useEffect(() => {
        movieList();
    }, []);

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
                    )).slice(firstIndex, lastIndex)}
                </Slider>

                {/* Grid de películas */}
                <MoviesGrid />
                <Pagination
                    moviesPerPage={moviesPerPage}
                    currentPage={currentPage}
                    setCurrentPage={setCurrentPage}
                    totalMovies={totalMovies}
                />
            </main>
        </div>
    );
}
