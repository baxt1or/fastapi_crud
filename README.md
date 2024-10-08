# FastAPI CRUD REST API

A simple CRUD (Create, Read, Update, Delete) REST API built using FastAPI and SQLAlchemy, designed for managing items in a MySQL database.

## Features

- Create new items
- Retrieve items by ID
- Update existing items
- Delete items by ID
- Validate input data

## Technologies Used

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [MySQL](https://www.mysql.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

## Prerequisites

- Python 3.7 or higher
- MySQL server
- Pip for managing packages

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/fastapi_crud.git
   cd fastapi_crud
   ```

python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

uvicorn main:app --reload
