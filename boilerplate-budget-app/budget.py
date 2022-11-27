class Category:

	def __init__(self, name):
		self.ledger = []
		self.balance = 0
		self.name = name

	def __str__(self):
		print_str = self.name.center(30, '*')
		for item in self.ledger:
			print_str += '\n' + item.get('description')[:23].ljust(23) + '{:.2f}'.format(item.get('amount')).rjust(7)
		print_str += '\n' + 'Total: ' + '{:.2f}'.format(self.balance)
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
	''' Takes a list of categories and outputs a
	bar chart showing the percentage spend in each
	category, by withdrawl not deposits '''
	chart_string = "Percentage spent by category\n"
	num_categories = len(categories)
	width = num_categories * 3 + 1
	num_circles = []
	for category in categories:
		diff = ledger[0].get('amount') - category.balance
		percent_spend = diff / category.balance
		num_circles.append(round(percent_spend_raw/10))

	for x in range(100, 0, -10)
		perc_label = (str(x) + '|').rjust(4)
	 	chart_string += perc_label.rjust(4).ljust(width)

	return chart_string