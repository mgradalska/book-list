import { BOOKS_LOADED, CLEAR_BOOKS, SET_FILTER } from './actionTypes';

let filterTimeout;

export const setFilter = filter => dispatch => {
  if (filterTimeout) {
    clearTimeout(filterTimeout)
  }
  filterTimeout = setTimeout(() =>
    filter
      ? dispatch(searchBooks(filter))
      : dispatch(clearBooks()),
    1000);
  dispatch({ type: SET_FILTER, payload: { filter } })
}

export const searchBooks = filter => async (dispatch) => {
  let apiURL = 'http://localhost:8000/books/';
  if (filter) apiURL += `?search=${filter}`
  const response = await fetch(apiURL);
  const books = await response.json();
  dispatch(booksLoaded(books));
}

export const booksLoaded = books => ({ type: BOOKS_LOADED, payload: { books } });

export const clearBooks = () => ({ type: CLEAR_BOOKS });
