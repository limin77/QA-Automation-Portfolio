print("--- BANKING TOOLS LOADED ---")

# 1. DEFINE THE TOOL (The Function)
# We create a generic tool that accepts ANY list of data
def audit_transactions(transaction_data):

    valid_sum = 0
    print(f"\nScanning batch of {len(transaction_data)} items...")

    for amount in transaction_data:
        if amount < 0:
            print(f"  [X] REJECTED:${amount}")
        elif amount > 2000:
            print(f"  [!] FLAGGED: ${amount} (High Value)")
            valid_sum = valid_sum + amount
        else:
            print(f"  [ok] Verified: ${amount}")
            valid_sum = valid_sum + amount

    # Return the result so we can use it later
    return valid_sum
        
# --------------------------------------------
# 2. USE THE TOOL (The Execution)
# Now we can process TWO different batches with just 2 lines of code.

morning_batch = [200, -5, 100]
afternoon_batch = [5000, 400, -10, 30]

# Run the tool on morning data
morning_total = audit_transactions(morning_batch)
print(f"Morning Total: ${morning_total}")

# Run the tool on afternoon data
afternoon_total = audit_transactions(afternoon_batch)
print(f"Afternoon Total: ${afternoon_total}")

print("\n--- END OF REPORT ---")