initial_balance = float(input("Enter your initial balance: ₹"))
deposit_amount = float(input("Enter the deposit amount: ₹"))
balance = initial_balance + deposit_amount
print(f"Updated balance after deposit: ₹{balance:.2f}")
withdraw_amount = float(input("Enter the withdrawal amount: ₹"))
if withdraw_amount > balance:
    print("Insufficient funds! Withdrawal denied.")
else:
    balance -= withdraw_amount
    print(f"Updated balance after withdrawal: ₹{balance:.2f}")