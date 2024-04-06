# Library Management System
## Overview
The Library Management System is a backend application built using FastAPI and MongoDB. It provides APIs for managing student records in a library.
## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Features
- Create, read, update, and delete student records
- Filter students by country and minimum age
- Connects to MongoDB Atlas for data storage
## Technologies Used
- Python
- FastAPI
- MongoDB
- PyMongo

## File Structure
   ```bash
   library_management_system/
   ├── app/
   │   ├── database.py
   │   ├── models.py
   │   ├── controllers.py
   │   ├── routes.py
   ├── main.py
   ├── requirements.txt
   ├── venv
   └── .env
   ```
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/himacharan128/library-api.git
2. Install dependencies:
   ```bash
   cd library-api
   pip install -r requirements.txt
3. Set up environment variables:
   ```bash
    MONGODB_URI=your_mongodb_uri
4. Start the server:
   ```bash
   uvicorn main:app --reload
## Usage

Visit [http://127.0.0.1.8000](http://127.0.0.1:8000) in your web browser to access the Library Management System.

## API Documentation

### Create Student

- **POST** `/students`
- Request Body:
  ```json
  {
   "name": "Sham",
   "age": 25,
   "address": {
     "city": "Noida",
     "country": "IND"
   }
  }
###  List Students
- **GET** `/students`
- Query Parameters:
- country (optional): Filter students by country
- age (optional): Filter students by minimum age

###  Fetch Student
- **GET** `/students/{id}`
### Update Student
- **PATCH** `/students/{id}`
- Request Body:
  ```json
  {
    "name": "string",
    "age": 0,
    "address": {
      "city": "string",
      "country": "string"
    }
  }

###  Delete Student
- **DELETE** `/students/{id}`
## Contributing
Contributions are welcome! Feel free to submit issues and pull requests.
## License
This project is licensed under the MIT License.
