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
    def __init__(self, filename='recurring.json'):
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

    def view_reccuring(self):
        if not self.reccuring:
            print(" No Reccuring transactions avaliable")
            return
        print("\n" + "="*60)
        for i, r in enumerate(self.reccuring, 1):
            print(f"{i} . {r['type']} ${r['amount'] :.2f} - {r['description']}" f" {r['frequency']} , day={r['day_value']}")
            print("=" * 60)

    def delete_reccuring(self, index):
        if 0 <= index < len(self.reccuring):
            removed = self.reccuring.pop(index)
            self.save_reccuring()
            print(f" Removed: {removed['description']}")
        else:
            print("Not a Real Transaction")

    def get_due_reccuring(self):
               due = []
               today = datetime.now().date()
       
               for rule in self.reccuring:
                   if self.is_due(rule, today):
                       due.append({
                           'amount': rule['amount'],
                           'description': rule['description'] + "(reccuring)",
                           'type': rule['type'],
                             })
                       rule['last_applied'] = str(today)
       
               if due:
                   self.save_reccuring
               return due

    def is_due(self, rule, today):
        last = rule['last_applied']
        last_date = datetime.strptime(last, '%Y-%m-%d').date() if last else None

        if rule['frequency'] == 'daily':
            return last_date != today

        elif rule['frequency'] == 'weekly':

            if today.weekday() != rule['day_value']:
                return False
            return last_date is None or (today - last_date).days >= 7

        elif rule['frequency'] == 'Monthly':
            if today.day != rule['day_value']:
                return False
            return last_date is None or last_date.month != today.month or  last_date.year != today.year

        return False

   
            
          

        
                



        

        