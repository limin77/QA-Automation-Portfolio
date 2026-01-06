print("--- BANK GATEKEEPER SYSTEM v2.0 ")

# 1. THE INPUT DATA (Change these numbers to test different scenarios)
account_status = "Active" # Try changing to "Frozen"
current_balance = 500.00  # Try changing to 50.00
transfer_amount = 1000.00  # Try changing to -50 or 600

print(f"Attempting to transfer: ${transfer_amount}...")

# 2. THE LOGIC TREE (The Brain)
# We check the "Kill Conditions" first.

if account_status != "Active":
    # Condition 1: Is the account locked?
    print("ERROR: Transaction Rejected. Account is Frozen.")
    
elif transfer_amount <= 0:
    # Condition 2: Is the amount valid?
    print("ERROR: Invalid Amount. You canot transfer $0 or negative money.")

elif transfer_amount > current_balance:
# Condition 3: Do they have money?
    print("ERROR: Insufficient Funds. You are too broke")

else:
# if NONE of the above errors happened, we are safe.
    final_balance = current_balance - transfer_amount
    print("SUCCESS: Transfer Approved.")
    print(f"New Balance: ${final_balance}")

print("----------------------------------")