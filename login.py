def Login(name, password):
    if name == "Vijju" and password == "vijju123":
        print("Login successful")
        print("Welcome, vijju!")
        print("You are now logged in")
        return True
    else:
        print("Login failed")
        return False

