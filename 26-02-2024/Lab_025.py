# Web Automation - Selenium

# Page - You are going automate

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password): #Parameterised Constructor Created....
        self.email = email
        self.password = password

    def loginconfirm(self):
        if self.password == "Pass1234":
            print("You are allowed to enter")
        else:
            print("Invalid user")


Neha = VWOLoginPage("amit@amit.com", "1234")
Neha.loginconfirm()

print(" ------")

pramod = VWOLoginPage("pramod@pramod.com", "Pass1234")
pramod.loginconfirm()

print(id(Neha))
print(id(pramod))












