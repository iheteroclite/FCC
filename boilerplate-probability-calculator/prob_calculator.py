import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **colors):
		self.contents = [col for col in colors for x in range(colors[col])]

	def draw(self, num_balls):
	#todo reduce balls in hat
		drw = []

		for b in range(num_balls):
	#	print('lst before=', lst)
			ball = random.choice(self.contents)
	#	print('ball ', ball)
			indx = self.contents.index(ball)
	#	print('indx ', indx)
			drw.append(self.contents.pop(indx))
		#print ('drw ', drw)
		#print('self.contents after=', self.contents)
		return drw



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	counter = 0
	# repeat for num_experiments the following steps:
	for ex in range(num_experiments):
		bag = copy.deepcopy(hat)
		hit = False
		# todo: can probably put it in one line?
		# pull num_balls_drawn balls from hat
		# todo: this should draw from a copy of hat???
		# then pop will make sense!
		this_draw = bag.draw(num_balls_drawn)
		#count each color of expected_balls in this_draw

		# check whether balls are expected_balls
		for col in expected_balls:
			hit += this_draw.count(col) >= expected_balls[col]

		counter += 1 if hit == len(expected_balls) else 0

	print('counter', counter)
	print('probablility my way ', counter/num_experiments)
	return counter/num_experiments


