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
	chart_str = "Percentage spent by category\n"
	num_categories = len(categories)
	print('num_categories ', num_categories)
	width = num_categories * 3 + 5
	circle_percents = []
	name_lengths = []
	for category in categories:
		# TODO: Balance includes money going in!
		diff = category.ledger[0].get('amount') - category.balance
		percent_spend = diff / category.balance
		print('spend ', percent_spend)
		circle_percents.append(int(round(percent_spend*10)*10))
		print(circle_percents)
		name_lengths.append(len(category.name))


	for x in range(100, 0, -10):
		chart_str += (str(x) + '|').rjust(4)
		for i in range (num_categories):
			chart_str += ' o ' if (circle_percents[i] >= x) else '   '
		chart_str += ' \n'

	chart_str += '-'*width + '\n'

	#TODO - add the names, by getting max of name_lengths, iterating over that range
	# add ' '*4 to beginning of line, then for each category either print the letter, or spaces
	for x in range(max(name_lengths)):
		chart_str += ' '*4
		for j in range (num_categories):
			letter = categories[j].name[x] if name_lengths[j] > x else ' '
			chart_str += letter.center(3)
		chart_str += ' \n'


	return chart_str