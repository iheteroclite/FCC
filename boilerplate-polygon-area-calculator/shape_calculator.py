class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'

	def set_width(self, w):
		self.width = w

	def set_height(self, h):
		self.height = h

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return (2*self.width + 2*self.height)

	def get_diagonal(self):
		return ((self.width**2 + self.height**2) ** 0.5)

	def get_picture(self):
		if (self.width > 50) or (self.height > 50):
			return "Too big for picture."
		return ('*'*self.width + '\n') * self.height

	def get_amount_inside(self, shape):
		''' Returns how many shape can fit inside Rectangle (self)'''
		# By number wide and high - not by area (alternate way)
		num_wide = self.width // shape.width
		num_high = self.height // shape.height
		return num_wide * num_high

class Square(Rectangle):
	def __init__(self, l):
		self.width = l
		self.height = l

	def __str__(self):
		return f'Square(side={self.width})'

	def set_side(self, s):
		self.width = s
		self.height = s

	def set_width(self, w):
		self.set_side(w)

	def set_height(self, h):
		self.set_side(h)

