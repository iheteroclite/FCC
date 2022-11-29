import copy
import random

class Hat:
	def __init__(self, **colors):
		self.contents = [col for col in colors for x in range(colors[col])]

	def draw(self, num_balls):
		if num_balls > len(self.contents):
			return self.contents
		else:
			drw = []
			for b in range(num_balls):
				ball = random.choice(self.contents)
				indx = self.contents.index(ball)
				drw.append(self.contents.pop(indx))
		return drw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	''' Returns the approximate decimal probability after num_experiments trys,
		of getting expected_balls out of hat with num_balls_drawn draws'''
	counter = 0

	# Run num_experiments number of draws from the hat
	for ex in range(num_experiments):
		# Draw balls from a new hat
		this_draw = copy.deepcopy(hat).draw(num_balls_drawn)

		# Check whether balls are expected_balls
		hit = False
		for col in expected_balls:
			hit += this_draw.count(col) >= expected_balls[col]

		counter += 1 if hit == len(expected_balls) else 0

	# return the probability of getting expected_balls
	return counter/num_experiments


