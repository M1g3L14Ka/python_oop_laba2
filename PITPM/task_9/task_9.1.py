class User:
    name = "john"

    def show(self):
        return self.name


user = User()

print(user.name)


class Student:
    pass  # временная заглушка, чтобы компилятор не ругался
