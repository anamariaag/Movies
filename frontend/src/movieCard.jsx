import React, { useState } from 'react';
import ReactModal from 'react-modal';
import styles from "./movieCard.module.css";

export function MovieCard({ movie }) {
    const [modalIsOpen, setModalIsOpen] = useState(false);

    const openModal = () => setModalIsOpen(true);
    const closeModal = () => setModalIsOpen(false);

    const imageUrl = "https://image.tmdb.org/t/p/w300" + movie.poster_path;

    return (
        <div>
            <li className={styles.movieCard} onClick={openModal}>
                <img
                    width={230}
                    height={345}
                    className={styles.movieImage}
                    src={imageUrl}
                    alt={movie.title}
                />
                <div>{movie.title}</div>
                <div className={styles.details}>
                    <div className={styles.price}> Price: {movie.popularity}</div>
                    <div className={styles.status}> Status: {movie.vote_average}</div>
                </div>
            </li>

            <ReactModal
                isOpen={modalIsOpen}
                onRequestClose={closeModal}
                contentLabel="Movie Details Modal"
            >
                {/* Contenido del Modal */}
                <h2>{movie.title}</h2>
                <img
                    width={230}
                    height={345}
                    src={imageUrl}
                    alt={movie.title}
                />
                <div className={styles.details}>
                    <div className={styles.price}> Price: {movie.popularity}</div>
                    <div className={styles.status}> Status: {movie.vote_average}</div>
                </div>
                <button onClick={closeModal}>Cerrar modal</button>
            </ReactModal>
        </div>
    );
}
