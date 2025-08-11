# Looma - Personal Finance API

Looma is a simple FastAPI-based RESTful API for managing personal finance transactions. It allows you to add, list, retrieve, and delete transactions, as well as view your current balance.

## Features

- Add income and expense transactions
- List all transactions or filter by category
- Retrieve a single transaction by ID
- Delete transactions
- Get current balance (income, expenses, net balance)
- MongoDB backend for persistent storage

## Requirements

- Python 3.12+
- MongoDB (running locally on default port)
- See [requirements.txt](requirements.txt) for Python dependencies

## Setup

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd Looma
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Start MongoDB:**
   Make sure MongoDB is running locally (`mongodb://localhost:27017`).

4. **Run the API:**
   ```sh
   uvicorn app.main:app --reload
   ```

   Or use Docker:
   ```sh
   docker build -t looma-api .
   docker run -p 8000:8000 looma-api
   ```

## API Endpoints

- `GET /`  
  Health check. Returns welcome message.

- `POST /transactions`  
  Add a new transaction.  
  **Body:**  
  ```json
  {
    "amount": 100.0,
    "category": "Salary",
    "type": "income",
    "description": "Monthly salary"
  }
  ```

- `GET /transactions`  
  List all transactions. Optional filter by category:  
  `GET /transactions?category=Food`

- `GET /transactions/{txn_id}`  
  Get a transaction by its ID.

- `DELETE /transactions/{txn_id}`  
  Delete a transaction by its ID.

- `GET /balance`  
  Get total income, expenses, and net balance.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE)