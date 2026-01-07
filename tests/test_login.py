from pages.login_page import LoginPage

# We pass 'driver' as an argument. Pytest automatically finds it in conftest.py
def test_login_success(driver):
    print("\n--- Starting POM Login Test ---")
    
    # 1. INIT
    login_page = LoginPage(driver)
    
    # 2. ACTION
    print("Loading Page...")
    login_page.load()
    
    print("Logging In...")
    login_page.login("standard_user", "secret_sauce")
    
    # 3. ASSERT
    current_url = login_page.get_url()
    if "inventory" in current_url:
        print("✅ PASS: Login Successful")
        assert True
    else:
        print(f"❌ FAIL: Still on {current_url}")
        assert False