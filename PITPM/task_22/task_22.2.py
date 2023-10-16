class Validator:
    email = None
    domain = None
    number = None

    def isEmail(self, email):
        if '@' in email:
            print("Correct:)")
        else:
            print("Wrong:_;")

    def isDomain(self, domain):
        if '.' in domain:
            print("Correct:)")
        else:
            print("Wrong:_;")

