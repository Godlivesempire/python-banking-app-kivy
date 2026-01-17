import os 
import json
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "users.json")

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)


def create_account(username, pin):
    users = load_users()

    if username in users:
        return False
    
    account_number = generate_account_number(users)

    users[username] = {
        "account_number":account_number,
        "pin": pin,
        "balance": 0
    }
    save_users(users)
    return True, account_number, pin

def generate_account_number(users):
    while True:
        acc = "GE" + str(random.randint(10000000, 99999999))
        if all(user.get("account_number") != acc for user in users.values()):
            return acc

def authenticate(username, pin):
    users = load_users()
    return username in users and users[username]["pin"] == pin

def get_balance(username):
    users = load_users()
    return users.get(username, {}).get("balance", 0)

def ensure_account_numbers():
    users = load_users()
    updated = False

    for user in users.values():
        if "account_number" not in user:
            user["account_number"] = generate_account_number(users)
            updated = True
    
    if updated:
        save_users(users)

def deposit(username, amount):
    users = load_users()
    users[username]["balance"] += amount
    save_users(users)

def withdraw(username, amount):
    users = load_users()

    if username not in users:
        return False, "User not fount"
    
    if amount <= 0:
        return False, "Invalid amount"
    
    if users[username]["balance"] < amount:
        return False, "Insufficient balance"
    
    users[username]["balance"] -= amount
    save_users(users)

    return True, "Withdrawal successful"


def transfer(sender_username, receiver_account_number, amount):
    users = load_users()

    if sender_username not in users:
        return False, "Sender not found"
    
    receiver_username = None
    for username, data in users.items():
        if data.get("account_number") == receiver_account_number:
            receiver_username = username
            break



    
    if receiver_username is None:
        return False, "Recipient account not found"
    
    if sender_username == receiver_username:
        return False, "Cannot transfer to yourself"
    
    if amount <= 0:
        return False, "Invalid amount"
    
    if users[sender_username]["balance"] < amount:
        return False, "Insufficient balance"
    
    users[sender_username]["balance"] -= amount
    users[receiver_username]["balance"] += amount

    save_users(users)

    return True, "Transfer successful"
   

