# Smart inventory

This document provides instructions for setting up and running the project locally.

## Prerequisites

- Python 3.x
- Git

## Clone the Project

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the project.
3. Run the following command:
git clone [<repository_url>](https://github.com/nyashaChiza/smart-inventory.git)

## Setup Virtual Environment

1. Navigate to the project directory:
2. Create a virtual environment:

3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

## Install Requirements

1. Ensure that the virtual environment is activated.

2. Install project dependencies:
pip install -r requirements.txt


## Run Migrations

1. Ensure that the virtual environment is activated.

2. Run Django database migrations:
python manage.py migrate


## Start Django Server

1. Ensure that the virtual environment is activated.

2. Run the provided batch file to start the Django server:
start-project.bat


3. Access the project in your web browser at `http://localhost:8000`.

## Additional Notes

- If you encounter any issues or errors during setup or execution, refer to the project's documentation or seek assistance from the project maintainers.
- Remember to deactivate the virtual environment when you're done:


