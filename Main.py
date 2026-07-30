from Currency import  format_currency
from tools import get_posostoive_float, get_choice, get_description
from reccuring import Reccuring
from Transactions import Tracker

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

def main():
    tracker = Tracker()
    

    while True:
        Main_menu()
        option = get_choice("Find choice (1-5)", ['1', '2', '3', '4', '5'])

        if option == '1':
            amount = get_posostoive_float(f"Enter the allowance amount:  ")
            description = get_description("Enter the description: ")
            tracker.add_transactions(amount, description, "ALLOWANCE")

        elif option == '2':
            amount = get_posostoive_float(f"Enter the expense amount: ")
            description = get_description("Enter the description: ")
            tracker.add_transactions(amount, description, "EXPENSE")

        elif option == '3':
            tracker.view_transactions()

        elif option == '4':
            print(f"\n  Current Balance: {format_currency(tracker.view_balance())}\n")

        elif option == '5':
            amount = get_posostoive_float(f"Enter expense amount:  {format_currency}")
            description = get_description()
            trans_type = get_choice("Type (INCOME/EXPENSE):  " , ['INCOME', 'EXPENSE'])
            frequency = get_choice("Frequency (DaIly/Weekly/Monthly): " ,
                                   ['Daily', 'Weekly', 'Monthly'])

            day_value = None
            if frequency == "weekly":
                print("0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun")
                day_value = int(input("Enter the day of week(1-6)"))
            elif frequency == "monthly":
                day_value = int(input("Enter the day of month(1-31): "))

            



            

            

main()
  






