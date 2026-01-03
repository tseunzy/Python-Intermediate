
import datetime
# Simple Banking System
# This covers: variables, lists, dictionaries, functions, loops, conditionals, strings

# Global variables to store accounts
accounts = {}  # Dictionary to store all accounts
transaction_history = {}  # Dictionary to store transaction history
account_counter = 1000  # Starting account number


def create_account():
    global account_counter
    
    print("Create A New Account")
    name = input("ENter full name: ").title().strip()

    while True:
        try:
            initial_depos = float(input("Enter initial deposit amount: "))
            if initial_depos < 0:
                print("Deposit cannot be negative")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    account_counter += 1  # this authomatically create an account for each customer 
    account_number = account_counter

    if account_number not in accounts:
        accounts[account_number] = { 
            'name': name, 
            "balance": initial_depos, 
            'pin': '0000',
            'active': True
        }
    # transaction_history[account_number] = []
    # transaction_history[account_number].append((account_number, f"Account opened with initial deposit: ${initial_depos:.2f}"))
    if account_number not in transaction_history:
        transaction_history[account_number] = []
        add_transaction(account_number, f"Account opened with initial deposit of {initial_depos:.2f}")


    print(f"\n Account created successfully!")
    print(f"   Account Number: {account_number}")
    print(f"   Account Holder: {name}")
    print(f"   Initial Balance: ${initial_depos:.2f}")
    print("   Default PIN: 0000 (change it for security reasons)")
    


def deposit_money(): # Deposit money
    print("    Deposit Money")
    
    account_number = int(input("Enter account number: "))

    if account_number not in accounts:
        print(" Acount not found")
    else:
        account = accounts[account_number]

    if not account['active']:
        print("Account is closed")
    
    amount = float(input("ENter deposit amount: $"))

    if amount <= 0:
        print("Deposit amount should be positive")
    
    account['balance'] += amount
    add_transaction(account_number, f"Withdrew: ${amount:.2f}")

    print(f"\nDeposit successful!")
    print(f"  New balance: ${account['balance']:.2f}")
    print(f"   Account history: {transaction_history}")


def withdraw_money():
    """Withdraw money from account"""
    print("\n Withdarw Money")
    account_number = int(input("Enter account number: "))
    
    if account_number not in accounts:
        print(" Acount not found")
    else:
        account = accounts[account_number]


    if not account['active']:
        print("Account is closed!")
    
    pin = input("Enter PIN: ")
    if pin != account['pin']:
        print("Invalid PIN!")
    
    amount = float(input("Enter withdrawal amount: $"))
    
    if amount <= 0:
        print("Withdrawal amount must be positive!")
    
    if amount > account['balance']:
        print("Insufficient funds!")
        print(f"Available balance: ${account['balance']:.2f}")
       
    account['balance'] -= amount
    add_transaction(account_number, f"Withdrew: ${amount:.2f}")
    
    print(f"\nWithdrawal successful!")
    print(f"Remaining balance: ${account['balance']:.2f}")


def check_balance():

    print("\nCheck Balance")
    account_number = int(input("Enter account number: "))
    
    if account_number not in accounts:
        print(" Acount not found")
    else:
        account = accounts[account_number]
    
    if not account['active']:
        print("Account is closed!")
    
    pin = input("Enter PIN: ")
    if pin != account['pin']:
        print("Invalid PIN!")
    
    print(f"\nAccount Details:")
    print(f"   Account Number: {account_number}")
    print(f"   Account Holder: {account['name']}")
    print(f"   Current Balance: ${account['balance']:.2f}")
    print(f"   Account Status: {'Active' if account['active'] else 'Closed'}")


def transfer_money():

    print("\nTransfer Money")
    from_account = int(input("Enter your account number: "))
    
    if from_account not in accounts:
        print("Your account not found!")
    
    from_acc = accounts[from_account]
    
    if not from_acc['active']:
        print("Your account is closed!")
        
    
    pin = input("Enter your PIN: ")
    if pin != from_acc['pin']:
        print("Invalid PIN!")
        
    
    to_account = int(input("Enter recipient account number: "))
    
    if to_account not in accounts:
        print("Recipient account not found!")
    
    to_acc = accounts[to_account]
    
    if not to_acc['active']:
        print("Recipient account is closed!")
    
    amount = float(input("Enter transfer amount: $"))
    
    if amount <= 0:
        print("Transfer amount must be positive!")
    
    if amount > from_acc['balance']:
        print("Insufficient funds!")
        print(f"Available balance: ${from_acc['balance']:.2f}")
    
    # Perform transfer
    from_acc['balance'] -= amount
    to_acc['balance'] += amount
    
    # # Record transactions
    add_transaction(from_account, f"Transferred ${amount:.2f} to account {to_account}")
    add_transaction(to_account, f"Received ${amount:.2f} from account {from_account}")
    
    print(f"\nTransfer successful!")
    print(f"   From: Account {from_account} (New balance: ${from_acc['balance']:.2f})")
    print(f"   To: Account {to_account} (New balance: ${to_acc['balance']:.2f})")

def change_pin():
    print("\nChange Pin")
    account_number = int(input("Enter account number: "))
    
    if account_number not in accounts:
        print(" Acount not found")
    else:
        account = accounts[account_number]
    
    if not account['active']:
        print("Account is closed!")
    
    old_pin = input("Enter current PIN: ")
    if old_pin != account['pin']:
        print("Invalid current PIN!")
    
    new_pin = input("Enter new PIN (4 digits): ")
    
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must be 4 digits!")
    
    confirm_pin = input("Confirm new PIN: ")
    
    if new_pin != confirm_pin:
        print("PINs don't match!")
    
    account['pin'] = new_pin
    add_transaction(account_number, "PIN changed successfully")
    
    print("\nPin changed successfully!")

def view_transactions():
    print("\nTransaction History")
    account_number = int(input("Enter account number: "))
    
    if account_number not in accounts:
        print("Account not found!")
    
    account_tran = accounts[account_number]
    
    if not account_tran['active']:
        print("Account is closed!")
    
    pin = input("Enter PIN: ")
    if pin != account_tran['pin']:
        print("Invalid PIN!")
    
    transactions = transaction_history.get(account_number, [])
    
    if not transactions:
        print("\nNo transactions found.")
    
    print(f"\nTransaction History for Account {account_number}:")
    print("=" * 40)
    for i, transaction in enumerate(transactions, 1):
        print(f"{i}. {transaction}")

def add_transaction(account_number, description):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction_history[account_number].append(f"[{timestamp}] {description}")

def close_account():
   
    print("\nClose Account")
    account_number = int(input("Enter account number: "))
    
    if account_number not in accounts:
        print("Account not found!")
    
    account = accounts[account_number]
    
    pin = input("Enter PIN: ")
    if pin != account['pin']:
        print("Invalid PIN!")
    
    if account['balance'] > 0:
        print(f"Cannot close account with balance! Please withdraw ${account['balance']:.2f} first.")
    
    confirm = input("Are you sure you want to close this account? (yes/no): ").lower()
    
    if confirm == 'yes':
        account['active'] = False
        add_transaction(account_number, "Account closed")
        print("\nAccount closed successfully!")
    else:
        print("\nAccount closure cancelled.")


def list_all_accounts():

    print("\nAll ACcount")
    admin_pin = input("Enter admin PIN (default: 9999): ")
    
    if admin_pin != '9999':
        print("Invalid admin PIN!")
    
    if not accounts:
        print("No accounts found.")
    
    print(f"\nTotal Accounts: {len(accounts)}")
    print("=" * 60)
    
    for acc_num, account in accounts.items():
        status = "Active" if account['active'] else "Closed"
        print(f"Account: {acc_num}")
        print(f"  Holder: {account['name']}")
        print(f"  Balance: ${account['balance']:.2f}")
        print(f"  Status: {status}")
        print(f"  Transactions: {len(transaction_history.get(acc_num, []))}")
        print("-" * 30)


def main_menu():

    while True:
        print("\n" + "=" * 40)
        print("        BANKING SYSTEM")
        print("=" * 40)
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Change PIN")
        print("7. View Transactions")
        print("8. Close Account")
        print("9. List All Accounts (Admin)")
        print("0. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice (0-9): ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            transfer_money()
        elif choice == '6':
            change_pin()
        elif choice == '7':
            view_transactions()
        elif choice == '8':
            close_account()
        elif choice == '9':
            list_all_accounts()
        elif choice == '0':
            print("\nThank you for using our banking system!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 0-9")

main_menu()