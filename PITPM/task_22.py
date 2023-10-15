class Validator:  # задание 1, создать класс validator
    email = None
    domain = None
    number = None

    def isEmail(self, email):  # задание 2, создать метод проверки email
        if '@' in email:
            print("Correct:)")
        else:
            print("Wrong:_;")

    def isDomain(self, domain):  # задание 2, создать метод проверки domen
        if '.' in domain:
            print("Correct:)")
        else:
            print("Wrong:_;")

    def isNumber(self, number):  # задание 2, создать метод проверки цифр(они идут без букв)
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
