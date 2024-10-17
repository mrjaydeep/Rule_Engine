# Rule_Engine

Application 1: Rule Engine with AST
Overview
The Rule Engine with Abstract Syntax Tree (AST) application allows users to define, evaluate, and execute business rules dynamically. It leverages AST to parse and evaluate rules written in a custom domain-specific language (DSL), enabling flexible rule management.

Design Choices
Abstract Syntax Tree (AST): Utilizes AST for parsing rules, allowing for easy manipulation and evaluation of complex expressions.
Modular Architecture: Divides functionality into separate Python files, each responsible for specific tasks, enhancing maintainability and clarity.
Dynamic Rule Evaluation: Supports dynamic rule creation and evaluation, making the engine adaptable to changing business needs.
Application Structure
bash
Copy code
rule_engine/
│
├── play.py          # Main script to execute the rule engine
├── sol.py           # Contains functions for rule parsing and evaluation
├── test.py          # Unit tests for the rule engine
└── __pycache__      # Compiled Python files
Dependencies
To set up and run the application, ensure you have the following dependencies:

Python 3.x
You can install any necessary packages using pip as required.

Running the Application
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/mrjaydeep/rule_engine.git
cd rule_engine
Run the main script:
bash
Copy code
python play.py
Unit Testing
To run the unit tests, execute the following command:

bash
Copy code
python -m unittest test.py
Example Output
When the application is executed, it will evaluate rules and display the results:

mathematica
Copy code
Rule Evaluation Result: True
Contribution
Contributions are welcome! Please fork the repository and submit a pull request.
