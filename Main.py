from Currency import  format_currency
from tools import get_posostoive_float, get_choice, get_description

def Main_menu():
    print("\n" + "=" * 40)
    print(" Off-Radar Finance Tracker ")
    print("=" * 40)
    print("1.   Add-Allowance")
    print("2.   Add-expense")
    print("3.   View All transactions")
    print("4.   View Balance ")
    print("5.   Add Reccuring Transactions")
    print("6.   View Reccuring transactions")
    print("7.   Remove Reccuring transactions")
    print("8.   Add Savings Goal")
    print("9.   Deposit into Savings Goal")
    print("10.  View Savings Goal")
    print("11.  Delete Savings Goal")
    print("12.  Exit Finacne Tracker")
    print("=" * 40)
  

# Testing
print(f"{format_currency(300)}")
get = get_posostoive_float(f"Take ")
chc = get_choice("Find choice (1-2)", ['1', '2'])
main = get_description("Hello ")




Main_menu()
