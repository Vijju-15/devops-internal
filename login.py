def Login(name, password):
    if name == "Pavan" and password == "secret":
        print("Login successful")
        print("Welcome, Pavan!")
        return True
    else:
        print("Login failed")
        return False

