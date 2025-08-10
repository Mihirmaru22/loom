from fastapi import FastAPI, HTTPException, Query
from bson import ObjectId
from app.models import Transaction
from app.database import db
from typing import Optional


app = FastAPI(title="Looma - Personal Finance API")

@app.post("/transactions")
def add_transaction(transaction: Transaction):
    result = db.transactions.insert_one(transaction.model_dump())
    return {"id": str(result.inserted_id), "message": "Transaction added successfully"}

@app.get("/transactions")
def list_transactions(category: Optional[str] = Query(None, description="Filter by category")):
    query = {}
    if category:
        query["category"] = category

    transactions = []
    for txn in db.transactions.find(query):
        txn["_id"] = str(txn["_id"])
        transactions.append(txn)
    return transactions

@app.get("/transactions/{txn_id}")
def get_transaction(txn_id: str):
    try:
        txn = db.transactions.find_one({"_id": ObjectId(txn_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid transaction ID format")

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    txn["_id"] = str(txn["_id"])
    return txn

@app.get("/balance")
def get_balance():
    income_sum = 0
    expense_sum = 0
    for txn in db.transactions.find():
        if txn["type"] == "income":
            income_sum += txn["amount"]
        else:
            expense_sum += txn["amount"]
    return {
        "income": income_sum,
        "expenses": expense_sum,
        "balance": income_sum - expense_sum
    }

@app.delete("/transactions/{txn_id}")
def delete_transaction(txn_id: str):
    result = db.transactions.delete_one({"_id": ObjectId(txn_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Transaction deleted successfully"}