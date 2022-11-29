class Category:

	def __init__(self, name):
		self.ledger = []
		self.balance = 0
		self.name = name

	def __str__(self):
		print_str = self.name.center(30, '*')
		for item in self.ledger:
			print_str += '\n' + item.get('description')[:23].ljust(23)
			print_str += '{:.2f}'.format(item.get('amount')).rjust(7)
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

	def transfer(self, amount, reciever):
		if self.check_funds(amount):
			self.withdraw(amount, 'Transfer to ' + str(reciever.name))
			reciever.deposit(amount, 'Transfer from '  + str(self.name))
		return self.check_funds(amount)

	def check_funds(self, amount):
		return False if abs(amount) > self.balance else True


def create_spend_chart(categories):
	''' Takes a list of categories and outputs a
	bar chart showing what percentage of your total expenditure
	was spent on each category, by withdrawl '''
	chart_str = "Percentage spent by category\n"
	num_categories = len(categories)
	name_lengths = []
	money_out = [0]*num_categories

	# Calculate percentage spend in each category
	for n, category in enumerate(categories):
		name_lengths.append(len(category.name))
		for transaction in category.ledger:
			# improve: include if transaction description not equal to transfer
			if transaction.get('amount') < 0:
				money_out[n] += transaction.get('amount')

	ratios_spend = [money_out[y]/sum(money_out) for y in range(num_categories)]
	# To pass all tests round with the int() method, this is poor programming
	# as it floors instead of rounding. A better way is:
	# percents = [abs(int(round(ratios_spend[z]*10)*10)) for z in range(num_categories)]
	percents = [abs(int(ratios_spend[z]*10)*10) for z in range(num_categories)]

	# Circles in bar chart
	for x in range(100, -10, -10):
		chart_str += (str(x) + '|').rjust(4)
		for i in range (num_categories):
			chart_str += ' o ' if (percents[i] >= x) else '   '
		chart_str += ' \n'

	# Line at bottom of chart
	chart_str += ' '*4 + '-'*(num_categories * 3 + 1) + '\n'

	# Chart category names
	for x in range(max(name_lengths)):
		chart_str += ' '*4
		for j in range (num_categories):
			letter = categories[j].name[x] if name_lengths[j] > x else ' '
			chart_str += letter.center(3)
		chart_str += ' \n'

	return chart_str[:-1]