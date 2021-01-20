import React from "react";
import { connect } from "react-redux";

import './BooksFilter.css';
import { setFilter } from "../../redux/actions";

const BooksFilter = ({ filter, setFilter }) => {
  const handleFilterChange = event => {
    const filterValue = event.target.value;
    setFilter(filterValue);
  }

  return (
    <div>
      <input placeholder="Search" type="text" value={filter} onChange={ handleFilterChange }/>
    </div>
  );
};

const mapStateToProps = state => {
  return { filter: state.booksFilter };
};

const mapDispatchToProps = dispatch => {
    return {
      setFilter: (filter) => dispatch(setFilter(filter))
    };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(BooksFilter);
