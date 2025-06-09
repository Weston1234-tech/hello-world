purchase_price = float(input("Enter the purchase price: "))
down_payment = 0.10 * purchase_price
annual_interest_rate = 0.12
monthly_payment = 0.05 * purchase_price
balance = purchase_price - down_payment
print("\nTidBit Computer Store - Payment Schedule")
print("---------------------------------------")
print(f"Purchase Price: ${purchase_price:.2f}")
print(f"Down Payment: ${down_payment:.2f}")
print(f"Annual Interest Rate: {annual_interest_rate * 100:.2f}%")
print(f"Monthly Payment: ${monthly_payment:.2f}")
print("---------------------------------------")
print("{:<8} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
    "Month","Balance Owed","Interest Owed","Principal Owed","Payment","Balance After",))
month_number = 1
while balance > 0:
    interest_owed = balance * (annual_interest_rate / 12)
    principal_owed = monthly_payment - interest_owed
    if principal_owed > balance:
        principal_owed = balance
        monthly_payment = principal_owed + interest_owed
    balance_after = balance - principal_owed
    print("{:<5} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f}".format(month_number, balance, interest_owed, principal_owed, monthly_payment,balance_after))
    balance = balance_after
    month_number += 1
