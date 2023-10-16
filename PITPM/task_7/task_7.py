class Users:
    name = None

    def show(self):
        print(self.name)


user = Users()

user.name = "john"

user.show()
