import json
from pathlib import Path
from Currency import format_currency
import sys 

def get_base_path():
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    else:
        return Path(__file__).parent

class SavingControlelr():
    def __init__(self, filename = "savings.json"):
            self.filename = get_base_path() / filename
            self.goals = self.load_goal()

    
    def _ensure_file_exists(self):
        if not Path(self.filename).exists():
            with open(self.filename, 'w') as f:
                f.write('[]')

    def load_goal(self):
        try:
            with open (self.filename, 'r') as f:
                        return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
                    return[]

    def save_goal(self):
            with open(self.filename, 'w') as f:
                  json.dump(self.goals, f, indent=2)

    def add_goal(self, name, amount):
          goal = {
                'name': name,
                'amount': amount,
                'saved': 0.0

          }
          self.goals.append(goal)
          self.save_goal()
          print(f" Savings Goal of {name} costing {format_currency(amount)} created")

    def deposit(self, index, amount):
          if 0 <= index < len(self.goals):
                self.goals[index]['saved'] += amount
                goal = self.goals[index]
                print(f"Added your deposit to goal {goal['name']}")
          else:
                print("Please select a real option")

    def show_progress(self, goal):
          saved = goal['saved']
          target = goal['amount']
          percent = min((saved / target) * 100,100)
          filled = int(percent // 5)
          bar = "$" * filled + '^' * (20-filled)
          print(f"Progress: [{bar}] {percent: .1f}%")
          print(F"Saved {format_currency(saved)} / {format_currency(target)}")
          remaining = target - saved
          if remaining <= 0:
                print("Goal Completed 'Respect'")
          else:
            print(f"Almost there just {format_currency(remaining)}  left!")

    def view_goals(self):
          if not self.goals:
                print("No Savings yet")
                return
          print("=" * 50)
          for i, goal in enumerate(self.goals):
                print(f"\n{i + 1 }. {goal['name']}")
                self.show_progress(goal)
    print("=" * 50)

    def delete_goal(self, index):

          if 0 <= index < len(self.goals):
                removed = self.goals.pop(index)
                self.save_goal()
                print(f" Goal: {removed['name']}")
          else:
                print("Enter a valid option")
