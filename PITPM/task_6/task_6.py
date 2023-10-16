class User:
	def show(self,name, surname):
		return name + ' ' + surname


user = User()
print(user.show('john', 'smit'))
