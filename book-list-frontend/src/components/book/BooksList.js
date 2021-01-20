import React from 'react';
import { connect } from 'react-redux';

import { getBooksList } from '../../redux/selectors';
import Book from './Book';
import './BooksList.css'

const BooksList = ({ books }) => (
  <div>
    {
      books && books.length
        ? <ul className='books-list'>
            { books.map((book, index) => <Book book={book} key={index}/>) }
          </ul>
        : 'No results'
    }
  </div>
);

const mapStateToProps = state => {
  const { booksFilter } = state;
  const books = getBooksList(state, booksFilter);
  return { books };
};

export default connect(mapStateToProps)(BooksList);
