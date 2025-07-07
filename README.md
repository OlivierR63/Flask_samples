# Flask Samples Project

A simple Flask application to manage and serve data about people.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Description

This project is a Flask-based web application that provides an API to manage a dataset of people. It supports operations such as retrieving, adding, and deleting person records.

## Features

- Retrieve a list of people with their details.
- Add new person records.
- Search for people by name.
- Delete existing person records.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/OlivierR63/Flask_samples.git

2. Navigate to the project directory:
   ```bash
   cd Flask_samples/lab

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the Flask application:
    ```bash
    python server.py

## Usage
Once the server is running, you can interact with the API using tools like curl, Postman, or any HTTP client. 
The server will start on http://localhost:5000.

## API Endpoints
GET /: Returns a simple greeting message.  
GET /no_content: Returns a response with no content.  
GET /data: Returns the count of data entries.  
GET /name_search?q=<name>: Search for a person by name.  
GET /person/<uuid>: Retrieve a person by their UUID.  
DELETE /person/<uuid>: Delete a person by their UUID.  
POST /person: Add a new person record.  

## Running Tests
To run the unit tests for this project, use the following command:  
```bash
python -m pytest tests/

## Contributing
Contributions are welcome! Please follow these steps:
 1. Fork the repository.
 2. Create a new branch for your feature or bug fix.
 3. Commit your changes and push to your fork.
 4. Submit a pull request with a description of your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
