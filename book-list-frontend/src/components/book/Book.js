import React from 'react';

import './Book.css'

const Book = ({ book }) => (
  <li className='book-item'>
    <span>{ book.title }</span>
    <span>{ book.author.name }</span>
    <span>{ book.avg_rating }</span>
  </li>
);

export default Book;
