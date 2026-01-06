# bank_engine.py - This is PURE LOGIC. No running code here.

def audit_transactions(transaction_data):
    valid_sum = 0

    for amount in transaction_data:
        # Business Logic: Reject negatives, Flag high values
        if amount < 0:
            continue # Skip negative numbers
        elif amount > 2000:
            valid_sum = valid_sum + amount
        else:
            valid_sum = valid_sum + amount

    return valid_sum