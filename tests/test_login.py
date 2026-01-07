from pages.login_page import LoginPage
from config import Config  # Import the data from your new file

def test_login_success(driver):
    print("\n--- Starting POM Login Test ---")
    
    # 1. INIT
    login_page = LoginPage(driver)
    
    # 2. ACTION
    print(f"Loading Page: {Config.BASE_URL}")
    login_page.load()  # You might need to update load() to use Config.BASE_URL too, but for now let's focus on login
    
    print(f"Logging In as: {Config.USERNAME}")
    login_page.login(Config.USERNAME, Config.PASSWORD)
    
    # 3. ASSERT
    current_url = login_page.get_url()
    if "inventory" in current_url:
        print("✅ PASS: Login Successful")
        assert True
    else:
        print(f"❌ FAIL: Still on {current_url}")
        assert False