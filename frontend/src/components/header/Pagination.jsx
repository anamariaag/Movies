import React from "react";

export const Pagination = ({ moviesPerPage, totalMovies, currentPage, setCurrentPage }) => {

    const pageNumbers = []

    for (let i = 1; i <= Math.ceil(totalMovies / moviesPerPage); i++) {
        pageNumbers.push(i)
    }

    const onPreviousPage = () => {
        setCurrentPage(currentPage - 1)
    }
    const onNextPage = () => {
        setCurrentPage(currentPage + 1)
    }

    const onSpecificPage = (n) => {
        setCurrentPage(n)
    }

    return (
        <nav className="pagination is-centred mb-6" role="navigation" aria-label="pagination">
            <a className={`pagination-previous ${currentPage === 1 ? 'is-disabled' : ''}`} onClick={onPreviousPage}> Previous </a>
            <a className={`pagination-next ${currentPage >= pageNumbers.length ? 'is-disabled' : ''}`} onClick={onNextPage}> Next </a>
            <ul className="pagination-list">
                {
                    pageNumbers.map(noPage => (
                        <li key={noPage}>
                            <a className={`pagination-link ${noPage === currentPage ? 'is-current' : ''}`} onClick={() => onSpecificPage(noPage)}>
                                {noPage}
                            </a>
                        </li>
                    ))
                }
            </ul>
        </nav>
    );
};