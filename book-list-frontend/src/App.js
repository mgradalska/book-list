import './App.css';

import BooksFilter from './components/book-filter/BooksFilter';
import BooksList from './components/book/BooksList';

function App() {
  return (
    <div className='books-app'>
      <div className='title'>Books List</div>
      <BooksFilter />
      <BooksList />
    </div>
  );
}

export default App;
