# Book List Application

Application created for displaying list of filtered books. Written in React and Django.

## Run application

Application will be available under `localhost:3000` address in your browser.

### By docker-compose

Required tools:
- docker-compose

In main directory run following commands:

```docker-compose build```

```docker-compose up```

### Locally

Required tools:
- npm
- python

#### Run backend

Go to `book_list_backend/` directory and run following commands:

```pip install -r requirements```

```python manage.py migrate```

```python manage.py runserver```

#### Run frontend

Go to `book-list-frontned/` directory and run following commands:

```npm install```

```npm start```

## Run backend tests

Go to `book_list_backend/` directory and run following command:

```python manage.py test```

Or if application is running in Docker, run in the main directory:

```docker-compose exec backend bash -c 'python manage.py test'```

## Load books data

There is a possibility to populate database by CSV files by running `load_books_data` command. 

`load_books_data` arguments:

| Parameter      | How it works         |
|----------------|----------------------|
| --skip-books   | Skip reading books   | 
| --skip-ratings | Skip reading ratings | 
| --books-file   | Books filename       |
| --ratings-file | Ratings filename     |

CSV files must be placed is `book_list_backend/books/management/files` directory. There are also some example files. Format of added files must be the same as example ones.

### Run command

If application is running in Docker, run in the main directory:

```docker-compose exec backend bash -c 'python manage.py load_books_data'```

Locally, run in `book_list_backend/` directory:

```python manage.py load_books_data```

