# Zeotap_AST


3-Tier Rule Engine Application
This project is a 3-tier rule engine application that evaluates user eligibility based on various attributes such as age, department, salary, and experience. The rule engine uses Abstract Syntax Tree (AST) to represent conditional rules for evaluation. This application includes a Flask-based backend and a React-based frontend, containerized using Docker.

Table of Contents
Features
Technology Stack
System Architecture
Design Choices
Project Structure
Prerequisites
Build Instructions
Usage
Docker Setup
API Endpoints
Contributing
License
Features
Dynamic Rule Creation: Create rules dynamically using a logical expression.
Rule Evaluation: Evaluate user eligibility based on data such as age, department, salary, etc.
AST-Based Logic: Leverages Abstract Syntax Tree (AST) for evaluating conditional rules.
Frontend: A React.js web interface to create and evaluate rules.
Backend: A Flask API to process AST and evaluate user data against it.
Containerization: Full Docker support for easy deployment and environment consistency.
Technology Stack
Frontend: React.js
Backend: Python (Flask)
Database: In-memory storage (or add persistent storage later)
Containerization: Docker, Docker Compose
API: RESTful API using Flask
System Architecture
Frontend: The React-based web interface allows users to input logical rules and data. Users can create rules (expressed in human-readable format) and evaluate them by submitting data attributes (age, department, salary, etc.).

Backend: The Flask API parses the user-defined rule into an Abstract Syntax Tree (AST) and evaluates it using the user data. The backend stores created rules and evaluates them on demand.

Docker: The application is containerized, allowing both the frontend and backend to be run as independent services.

Design Choices
Abstract Syntax Tree (AST):
We chose to use AST to represent logical expressions (rules) because it simplifies rule evaluation and manipulation. ASTs are a powerful tool in parsing and analyzing structured data. The flexibility of AST allows the application to handle complex rules and logically break them down into simpler components.

Separation of Concerns:
The application is divided into a 3-tier architecture:

Frontend: React handles the user interface for rule creation and evaluation.
Backend: Flask manages API requests, converts rule strings to AST, and performs rule evaluations.
Containerization: Each component is containerized using Docker to ensure portability and consistency across different environments.
Containerization with Docker:
Docker is used to ensure that the application runs in any environment by packaging all dependencies into isolated containers. We opted for docker-compose to manage both services (frontend and backend) simultaneously.

Project Structure
plaintext
Copy code
root/
├── backend/
│   ├── ast.py              # Logic for creating and evaluating AST
│   ├── api.py              # Flask application with rule creation and evaluation endpoints
│   ├── database.py         # In-memory storage (could be replaced by a DB)
│   └── requirements.txt    # Python dependencies
├──-
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── services/        # API calls to backend
│   ├── public/              # Static files
│   ├── package.json         # Frontend dependencies
│   └── Dockerfile           # Frontend Dockerfile
├── docker-compose.yml       # Docker Compose configuration
└── README.md                # Project documentation
Prerequisites
Before you begin, ensure you have the following installed on your machine:

Docker: Install Docker
Docker Compose: Install Docker Compose
Git: Install Git
Build Instructions
To build and run the application locally, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
Backend Setup:

Navigate to the backend/ directory and install the Python dependencies:

bash
Copy code
cd backend
pip install -r requirements.txt
Frontend Setup:

Navigate to the frontend/ directory and install the frontend dependencies:

bash
Copy code
cd ../frontend
npm install
Run the Backend:

bash
Copy code
flask run
Run the Frontend:

bash
Copy code
npm start
Open your browser and navigate to http://localhost:3000 for the frontend and http://localhost:5000 for the backend.

Docker Setup
To containerize the application using Docker:

Build and Run Containers:

In the root directory, run the following command:

bash
Copy code
docker-compose up --build
Access the Application:

React Frontend: http://localhost:3000
Flask Backend: http://localhost:5000
API Endpoints
Create Rule (POST /create_rule)
Input: A rule string (e.g., age > 30 AND department == 'Sales')
Output: Rule AST and success message

Evaluate Rule (POST /evaluate)
Input: AST and user data (e.g., {"age": 35, "department": "Sales"})
Output: Boolean result of rule evaluation
