import json
from datetime import datetime
from pathlib import Path
from Currency import format_currency
import sys 

def get_base_path():
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    else:
        return Path(__file__).parent

class Reccuring():
    def __init__(self, filename='recurring.py'):
        self.filename = get_base_path() / filename
        self._ensure_file_exists()
        self.reccuring = self.load_reccuring()


    def _ensure_file_exists(self):
        if not Path(self.filename).exists():
            with open(self.filename, 'w') as f:
                f.write('[]')

    def load_reccuring(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return[]

    def save_reccuring(self):
        with open(self.filename, 'w') as f:
            json.dump(self.load_reccuring, f, indent=2)

    def add_reccuring(self, amount, description, tran_type, frequency, day_value):

        rule = {
            'amount' : amount,
            'description' : description,
            'type' : tran_type,
            'frequency' : frequency,
            'day' : day_value
         }

        self.reccuring.append(rule)
        self.save_reccuring
        print(f"Reccuring {tran_type} of {format_currency(amount)} ({frequency})")

                



        

        