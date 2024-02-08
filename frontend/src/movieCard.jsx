import styles from "./movieCard.module.css";
import Modal from "./components/Modal";
import { useState } from "react";

export function MovieCard({ movie }) {
  console.log(movie);
  const [estadoModal, cambiarEstadoModal] = useState(false);

  return (
    <>
      <button onClick={() => cambiarEstadoModal(!estadoModal)}>
        <li className={styles.movieCard}>
          <img
            width={230}
            height={345}
            className={styles.movieImage}
            src={
              movie.image_url ||
              "https://ih1.redbubble.net/image.1893341687.8294/fposter,small,wall_texture,product,750x1000.jpg"
            }
            alt={movie.title}
          />
          <div>{movie.title}</div>
          <div className={styles.details}>
            <div className={styles.price}> Price: {movie.price}</div>
            <div className={styles.status}> Status: {movie.status}</div>
          </div>
        </li>
      </button>
      <Modal estado={estadoModal} cambiarEstado={cambiarEstadoModal}>
        <li className={styles.movieCard}>
          <img
            width={230}
            height={250}
            className={styles.movieImageModal}
            src={
              movie.image_url ||
              "https://ih1.redbubble.net/image.1893341687.8294/fposter,small,wall_texture,product,750x1000.jpg"
            }
            alt={movie.title}
          />
          <div>
            <h1>{movie.title}</h1>
          </div>
          <div className={styles.details}>
            <div className={styles.priceModal}> Price: {movie.price}</div>
            <div className={styles.overview}>
              {" "}
              Overview: {movie.plot || "Not plot found"}
            </div>
            <button
              onClick={() => cambiarEstadoModal(false)}
              className={styles.buttonModal}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-play-circle"
                viewBox="0 0 16 16"
              >
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16" />
                <path d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445" />
              </svg>
            </button>
            <button
              onClick={() => cambiarEstadoModal(false)}
              className={styles.buttonModal}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-film"
                viewBox="0 0 16 16"
              >
                <path d="M0 1a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H1a1 1 0 0 1-1-1zm4 0v6h8V1zm8 8H4v6h8zM1 1v2h2V1zm2 3H1v2h2zM1 7v2h2V7zm2 3H1v2h2zm-2 3v2h2v-2zM15 1h-2v2h2zm-2 3v2h2V4zm2 3h-2v2h2zm-2 3v2h2v-2zm2 3h-2v2h2z" />
              </svg>
            </button>
          </div>
        </li>
      </Modal>
    </>
  );
}
