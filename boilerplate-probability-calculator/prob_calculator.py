import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **colors):
		self.contents = [col for col in colors for x in range(colors[col])]

	def draw(self, num_balls):
	''' Will draw bals from the hat, reducing the balls in hat'''
	#todo reduce balls in hat
		return random.choices(self.contents, k=num_balls)



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	counter = 0
	# repeat for num_experiments the following steps:
	for ex in range(num_experiments):
		hit = False
		# todo: can probably put it in one line?
		# pull num_balls_drawn balls from hat
		this_draw = hat.draw(num_balls_drawn)
		#count each color of expected_balls in this_draw

		# check whether balls are expected_balls
		for col in expected_balls:
			hit += this_draw.count(col) >= expected_balls[col]

			#todo: try
			# counter += 1 if hit == len(expected_balls)
			# or
			# counter += 1 if hit == len(expected_balls) else 0
		if hit == len(expected_balls):
			counter += 1


