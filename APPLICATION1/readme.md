# Rule Engine Application

## Overview
This is a simple 3-tier rule engine application that determines user eligibility based on attributes like age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Features
  - **Create Rule**: Allows users to create rules based on given attributes.
  - **Combine Rules**: Combines multiple rules into a single AST.
  - **Evaluate Rule**: Evaluates the given data against the rule and returns whether the user is eligible.
  - **Error Handling (Bonus)**: Handles invalid rule strings and data formats and provides meaningful error messages to the user.


## Project Structure
- `app/`: Contains the main application code.
  - `api.py`: Provides API functions to interact with the rule engine.
  - `ast.py`: Defines the AST data structure.
  - `database.py`: Handles database initialization and operations.
  - `rules.py`: Implements rule creation, combination, and evaluation logic.
  - `static/`: Contains static files (CSS, JavaScript).
    - `css/`: 
      - `style.css`: CSS styles.
    - `js/`:
      - `script.js`: JavaScript files.
  - `templates/`:
      - `index.html`: Main UI template.
  
- `tests/`: Contains unit tests.
  - `test_rules.py`: Tests for rule creation, combination, and evaluation.
  - `test_api.py`: Tests for the API functions.
- `requirements.txt`: Lists the dependencies.
- `main.py`: The entry point of the application.
- `README.md`: This documentation file.

## Design Choices
- **3-tier Architecture**: The application is designed with a 3-tier architecture, separating the UI, API, and backend logic for better maintainability and scalability.
- **Abstract Syntax Tree (AST)**: Used to represent conditional rules, allowing for dynamic creation, combination, and modification.
- **Error Handling**: Comprehensive error handling for invalid rule strings and data formats to ensure robustness.
- **UI Design**: The UI is designed to be clean and user-friendly, with dynamic feedback for rule evaluation results.

## Instructions

  ### Prerequisites
  - Python 3.6 or higher
  - Flask
  - SQLite (for database)


  ### Build and Install
  ###  Create a virtual environment 
    python -m venv venv
  ### Initialize the virtual environment 
    venv/Scripts/activate
  ### Install dependencies:
      pip install -r requirements.txt
  ### Initialize the database:
      python -c "from app.database import initialize_database; initialize_database()"
  ### Run the application:
      python main.py
  Open your web browser and go to `http://127.0.0.1:5000/`.

  ## Test
  ### Sample tests to try on UI
  ### Creating the rule
    ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)

  Input the above line in create rule text box and press the create rule button. It will prompt as the rule being created if successfull and generates the relevant AST (autofill).

  ### Input a query to evaluate:
      {
        "age": 50,
        "department": "Sales",
        "salary": 60000,
        "experience": 10
      }

  Input this json in "Data (JSON format):" and press evaluate button which will hence generate the reult as Trur or False.


## Predefined test cases:
### Run the tests or directly browse it on the web browser with the help of sample examples given below:
    python -m unittest discover tests