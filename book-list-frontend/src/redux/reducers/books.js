import { BOOKS_LOADED, CLEAR_BOOKS } from '../actionTypes';

const initialState = {
  books: [],
  filter: ''
};

const books = (state = initialState, action) => {
  switch (action.type) {
    case BOOKS_LOADED: {
      const { books } = action.payload;
      return {
        ...state,
        books: books
      };
    }
    case CLEAR_BOOKS: {
      return {
        ...state,
        books: []
      };
    }
    default:
      return state;
  }
}

export default books;
