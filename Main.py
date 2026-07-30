from Currency import  format_currency
from tools import get_posostoive_float, get_choice, get_description
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
        option = get_choice("Find choice (1-12)", ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])

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
            amount = get_posostoive_float(f"Enter transaction amount: ")
            description = get_description()
            tran_type = get_choice("Type (ALLOWANCE/EXPENSE):  " , ['ALLOWANCE', 'EXPENSE'])
            frequency = get_choice("Frequency (DaIly/Weekly/Monthly): " , ['DAILY', 'WEEKLY', 'MONTHLY'])

            day_value = None
            if frequency == "WEEKLY":
                print("0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun")
                day_value = int(input("Enter the day of week(1-6): "))
            elif frequency == "MONTHLY":
                day_value = int(input("Enter the day of month(1-31): "))
            

            tracker.reccuring.add_reccuring(amount, description, tran_type, frequency, day_value)

        elif option == '6':
            tracker.reccuring.view_reccuring()

        elif option == '7':
            tracker.reccuring.view_reccuring()
            idx = int(input("Enter the number to delete: "))
            tracker.reccuring.delete_reccuring(idx)

        elif option == '8':
            name = get_description("Savings Goal Name:  ")
            target = get_posostoive_float("Deposit Amount:  ")
            tracker.savings.add_goal(name, target)

        elif option == '9':
            tracker.savings.view_goals()
            if tracker.savings.goals:
                idx = int(input("Select Goal Number")) - 1 
                amount = get_posostoive_float("Amount:  ")
                tracker.savings.deposit

        elif option == '10':
            tracker.savings.view_goals()

        elif option == '11':
            tracker.savings.view_goals()
            idx = int(input("Select Goal to delete: ")) -1 
            tracker.savings.delete_goal(idx)

        elif option == '12':
            print("Goodbye and Thankyou for using Off Grid Finanance tracker")
            break




            


main()
  






