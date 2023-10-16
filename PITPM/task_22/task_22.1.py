class Validator:
    email = None
    domain = None
    number = None

    def isEmail(self, email):
        if '@' in email:
            print("Correct:)")
        else:
            print("Wrong:_;")


