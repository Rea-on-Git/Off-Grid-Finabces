import json
import datetime
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
        self.transactions = self.load_transaction

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

    def add_transactions(self, amount):


