# tests/test_bank.py - The Supervisor

from src.bank_engine import audit_transactions

# TEST CASE 1: Standard Transfer (Using Fixture)
# Learning NOTE: We use 'sample_data' inside the parentheses.
# Pytest automatically finds this data in 'conftest.py'.
def test_standard_transactions(sample_data):
    print("\nRunning Test: Standard...")
    # ---------------------------------------------------------
    # TEACHING SNIPPET (THE OLD WAY)
    # Before we had conftest.py, we had to write data manually:
    # data = [100, 200, 50]
    # ---------------------------------------------------------

    expected_result = 350

    # NEW WAY: We use the fixture directly
    # PyTest sees 'sample_data' in the function name and fetches it automatically.
    assert audit_transactions(sample_data) == expected_result

# TEST CASE 2: Negative Numbers (Using Local Data)
# Learning Note: We still use local data here because this test
# needs specific numbers (-50) that are different from the shared fixture.
def test_negative_transactions():
    print("\nRunning Test: Negatives...")

    # We expect negatives to be IGNORED
    data = [100, -50, 200]
    expected_result = 300 # 100 + 200 (Ignore -50)

    assert audit_transactions(data) == expected_result