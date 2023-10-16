class User:
    def setAge(self, age):
        self._age = age

    def getAge(self):
        return self._age


class Student(User):
    def incAge(self):
        self._age = self._age+1
