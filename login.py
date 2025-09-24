def Login(name, password):

    if name == "Pavan" and password == "secret":
        print("Login successful")
        print("Welcome, Pavan!")
        print("You are now logged in")
        return True
    else:
        print("Login failed")
        return False

