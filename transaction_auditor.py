print("--- DAILY TRANSACTION AUDIT ---")

# 1. THE DATA (A list of transactions)
# In a real job, this comes from a database or CSV file.
transactions = [200, 50, -10, 5000, 120, -5, 3000]

# We need a bucket to count the total valid money
total_valid_amount = 0

print(f"Processing {len(transactions)} transactions...")
print("-" * 30)

# 2. THE LOOP (The Worker)
# "For every single 'amount' inside the 'transactions' list, do this:"
for amount in transactions:

    if amount < 0:
        print(f"ALERT: Transaction ${amount} is INVALID (Negative).")

    elif amount > 2000:
        print(f"WARNING: Transactio ${amount} is SUSPICIOUS (High Value).")
        # We still add it, but we flagged it.
        total_valid_amount = total_valid_amount + amount

    else:
        print(f"OK: Transaction ${amount} is valid.")
        total_valid_amount = total_valid_amount + amount

# 3. THE REPORT
print("-" * 30)
print(f"AUDIT COMPLETE")
print(f"Total Valid Money Moved: ${total_valid_amount}")
print("------------------------------")