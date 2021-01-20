export const getBooksState = store => store.books;

export const getBooksList = store =>
  getBooksState(store) ? getBooksState(store).books : [];
