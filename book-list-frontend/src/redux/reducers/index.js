import { combineReducers } from "redux";

import booksFilter from "./booksFilter";
import books from "./books";

export default combineReducers({ books, booksFilter });
