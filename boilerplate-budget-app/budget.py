class Category:

	def __init__(self, name):
		self.ledger = []
		self.balance = 0
		self.name = name

	def __str__(self):
		print_str = self.name.center(30, '*')
		# for amnt, des in self.ledger:
		# 	print_str += '\n' + des[:23].ljust(23) + '{:.2f}'.format(float(amnt).rjust(7)
		return print_str


	def deposit(self, amount, description=''):
		self.balance += float(amount)
		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount, description=''):
		if self.check_funds(amount):
			self.balance -= float(abs(amount))
			self.ledger.append({"amount": -abs(amount), "description": description})
		return self.check_funds(amount)

	def get_balance(self):
		return self.balance

	def transfer(self, amount, donor_catergory):
		if self.check_funds(amount):
			self.withdraw(amount, 'Transfer to ' + str(self.name))
			donor_catergory.deposit(amount, 'Transfer from '  + str(self.name)) #need to add category name here
		return self.check_funds(amount)

	def check_funds(self, amount):
		return False if abs(amount) > self.balance else True




def create_spend_chart(categories):
	print('hi')