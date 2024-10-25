# backend/database.py
from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    return client['rule_engine_db']

def save_rule(rule_ast):
    db = get_db()
    db.rules.insert_one({"rule_ast": rule_ast})

def fetch_rules():
    db = get_db()
    return list(db.rules.find())