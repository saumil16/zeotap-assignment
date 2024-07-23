# Rule Engine Application

## Overview
This is a simple 3-tier rule engine application that determines user eligibility based on attributes like age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Project Structure
- `app/`: Contains the main application code.
  - `ast.py`: Defines the AST data structure.
  - `database.py`: Handles database initialization and operations.
  - `rules.py`: Implements rule creation, combination, and evaluation logic.
  - `api.py`: Provides API functions to interact with the rule engine.
- `static/`: Contains static files (CSS, JavaScript).
  - `style.css`: CSS styles.
  - `script.js`: JavaScript files.
  - `index.html`: Main UI template.
- `tests/`: Contains unit tests.
  - `test_rules.py`: Tests for rule creation, combination, and evaluation.
  - `test_api.py`: Tests for the API functions.
- `requirements.txt`: Lists the dependencies.
- `main.py`: The entry point of the application.
- `README.md`: This documentation file.

## Getting Started
1. Install dependencies:
    pip install -r requirements.txt
2. Initialize the database:
    python -c "from app.database import initialize_database; initialize_database()"
3. Run the application:
    python main.py
4. Open your web browser and go to `http://127.0.0.1:5000/`.
5. Run the tests:
    python -m unittest discover tests