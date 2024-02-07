import styles from "./movieCard.module.css"

export function MovieCard({ movie }) {
    console.log(styles);
    const imageUrl = "https://image.tmdb.org/t/p/w300" + movie.poster_path
    return (
        <li className={styles.movieCard}>
            <img width={230}
                height={345}
                className={styles.movieImage}
                src={imageUrl}
                alt="{movie.title}"
            />
            <div>{movie.title}</div>
            <div className={styles.details}>
                <div className={styles.price}> Price: {movie.popularity}</div>
                <div className={styles.status}> Status: {movie.vote_average}</div>
            </div>
        </li>
    );
}