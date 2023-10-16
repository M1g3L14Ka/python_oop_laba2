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

    def isNumber(self, number):
        if number.isdigit():
            print("Correct:)")
        else:
            print("Wrong:_;")


validator = Validator()
validator.isEmail("hellow@world")
validator.isDomain("https://vksit.ru")
validator.isNumber("23123123131231")

validator1 = Validator()  # это для проверки на работоспособность
validator1.isEmail("hello.world")
validator1.isDomain("https://vksitru")
validator1.isNumber("23123123131231fasfasfasa")
