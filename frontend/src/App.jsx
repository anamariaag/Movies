import React, { useEffect, useState } from "react";
import { MoviesGrid } from "./MoviesGrid";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import styles from "./App.module.css";

import "bulma/css/bulma.min.css";
import Navbar from "./components/header/navbar";
import { Pagination } from "./components/header/Pagination";

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

  const totalMovies = movie.length;

  const [moviesPerPage, setMoviesPerPage] = useState(6);
  const [currentPage, setCurrentPage] = useState(1);

  const lastIndex = currentPage * moviesPerPage; // = 1 * 6 = 6
  const firstIndex = lastIndex - moviesPerPage; // = 6 - 6 = 0

  // Obtener datos de la api desde el back
  const movieList = async () => {
    const data = await fetch("http://localhost:8000/home/movies");
    const movie = await data.json();

    setMovies(movie);
  };

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
        <Slider {...settings} style={{ width: "80%", margin: "0 auto" }}>
          {movie
            .map((movie) => (
              <div key={movie.id}>
                {/* Puedes renderizar el contenido del carrusel aquí */}
                <img
                  className="carrouselImg"
                  src={
                    movie.image_url ||
                    "https://ih1.redbubble.net/image.1893341687.8294/fposter,small,wall_texture,product,750x1000.jpg"
                  }
                  alt={movie.title}
                />
                <h3 style={{ textAlign: "start", fontSize: "20px" }}>
                  {movie.title}
                </h3>
              </div>
            ))
            .slice(firstIndex, lastIndex)}
        </Slider>

        {/* Grid de películas */}
        <MoviesGrid />
        {/* <Pagination
          moviesPerPage={moviesPerPage}
          currentPage={currentPage}
          setCurrentPage={setCurrentPage}
          totalMovies={totalMovies}
        /> */}
      </main>
    </div>
  );
}
