class User:
    __name = None

    def __init__(self,name):
        self.__name = name

    def show(self):
        return self.__name


user = User('john')
print(user.show())
