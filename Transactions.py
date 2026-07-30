import json
from reccuring import Reccuring
from Currency import format_currency
from savings import SavingControlelr
from datetime import datetime
from pathlib import Path
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    else:
        return Path(__file__).parent
    
class Tracker:
    def __init__(self, filename = "transactions.json"):
        self.filename = get_base_path() / filename
        self._ensure_file_exist()
        self.reccuring = Reccuring()
        self.transactions = self.load_transaction()
        self.savings = SavingControlelr()

    def _ensure_file_exist(self):
        if not Path(self.filename).exists():
            with open(self.filename, 'w') as f:
                f.write('[]')

    def load_transaction(self):
        try:
            with open (self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return[]

    def _save_transaction(self):
        with open(self.filename, 'w') as f:
            json.dump(self.transactions, f, indent=2)

    def add_transactions(self, amount, description, tran_type):
        transaction = {
            'amount' :  amount,
            'description' :  description,
            'type' : tran_type,
            'date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        self.transactions.append(transaction)
        self._save_transaction()

        print(f"{tran_type} of {format_currency(amount)} has been added!")

    def view_balance(self):
        balance = 0
        for t in self.transactions:
            if t['type'] == "ALLOWANCE":
                balance = balance + t["amount"]
            else:
                balance = balance - t["amount"]
        return balance

    def view_transactions(self):
        if not self.transactions:
            print("You have not logged any transactions yet")

        print("\n" + "=" * 60)
        print(f"{'Date' :<20} {'Type' :<10} {'Amount' :<12} {'Description' }")
        print("=" * 60)
        for t in self.transactions:
            print(f" {t['date'] :<20}   {t['type'] :<10}  {format_currency(t['amount']) :<12}  {t['description']} ")
        print("=" * 60)

    
    def apply_due_reccuring(self):
        due = self.reccuring.get_due_reccuring()
        for item in due:
            saving_idx = item.get('savings_goal_index')
            if saving_idx is None:
                self.savings.deposit(saving_idx, item['Amount'])
                print(f"Auto deposited {format_currency(item['Amount'])} into savings goal")
            else:
                self.add_transactions(item['amount'], item['description'], item['type'])
           

