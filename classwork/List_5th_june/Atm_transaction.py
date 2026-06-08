transactions = [5000, -2000, 3000, -1000, -500, 7000]

balance = 0
deposit_count = 0
withdrawal_count = 0

deposits = []
withdrawals = []

for i in transactions:
    balance += i

    if i > 0:
        deposit_count += 1
        deposits.append(i)
    else:
        withdrawal_count += 1
        withdrawals.append(i)

print("Current Balance:", balance)
print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)

print("Largest Deposit:", max(deposits))
print("Largest Withdrawal:", min(withdrawals))

print("Deposits List:", deposits)
print("Withdrawals List:", withdrawals)