from login import Login

def test_login_success():
    name = "Pavan"
    password = "secret"
    assert Login(name, password) == True
    print("Test passed: Login successful")

def test_login_failure():
    name = "Pavan"
    password = "wrongpassword"
    assert Login(name, password) == False
    print("Test passed: Login failure handled correctly")

def run_login_test():
    print("Running login tests...")
    print("\n--- Test 1: Valid credentials ---")
    test_login_success()
    
    print("\n--- Test 2: Invalid credentials ---")
    test_login_failure()
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    run_login_test()
