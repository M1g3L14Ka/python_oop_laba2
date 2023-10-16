class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self._capeFirst(self.name)

    def _capeFirst(self, stri):
        return stri.capitalize()


class Student(User):
    def setSurn(self, surname):
        self.surname = surname

    def getSurn(self):
        return self._capeFirst(self.surname)

    def _capeFirst(self, stri):
        return stri.capitalize()
