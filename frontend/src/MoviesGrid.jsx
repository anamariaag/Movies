import React, { useEffect, useState } from "react";
import { MovieCard } from "./movieCard";
import styles from "./moviesGrid.module.css";

export function MoviesGrid() {
  // Obtener datos de la api desde el back
  const [movies, setMovies] = useState([]);

  const movieList = async () => {
    const data = await fetch("http://localhost:8000/home/movies");
    const movie = await data.json();

    setMovies(movie);
  };

  useEffect(() => {
    movieList();
  }, []);
  return (
    <ul className={styles.moviesGrid}>
      {movies.map((movie) => (
        <MovieCard key={movie.id} movie={movie} />
      ))}
    </ul>
  );
}
