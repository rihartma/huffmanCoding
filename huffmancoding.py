class Compression():

	def __init__(self):
		pass

	def count_frequency(self, text):
		freq = {}
		for ch in text:
			if ch in freq.keys():
				freq[ch] += 1
			else:
				freq[ch] = 1

		return freq

	def knots_gen(self, freq):
		'''
		generates a list of the Knots objects
		sets knot's value and character according to the keys and values from the frequency dict
		'''
		knots = []
		for key in freq.keys():
			knots.append(Knot(freq[key]))
			knots[-1].character = key
		return knots

	def knots_order(self, array):
		'''
		orders knots according to their value from the lowest values
		have to convert it(from the highest to the lowest values) for uses in this app
		'''
		if len(array) <= 1:
			return array

		pivot_index = len(array)-1
		array[0], array[-1] = array[-1], array[0]
		size_border = 0

		for i in range(len(array)-1):
			if array[i].value<array[pivot_index].value:
				array[i], array[size_border] = array[size_border], array[i]
				size_border += 1

		array[pivot_index], array[size_border] = array[size_border], array[pivot_index]
		pivot_index = size_border

		return(self.knots_order(array[:pivot_index]) + [array[pivot_index]] + self.knots_order(array[pivot_index+1:]))

	def new_knot(self, knots):
		'''
		makes a new knot with branches folded from two knots with the lowest values
		'''
		if len(knots) < 2:
			return None
		new_knot = Knot(knots[-1].value+knots[-2].value)
		new_knot.left_branch = knots[-1]
		new_knot.right_branch = knots[-2]
		del knots[-1:-3:-1]
		knots.append(new_knot)
		return knots

	def print_knots(self, knots):
		for knot in knots:
			print(knot.value, knot.character)
		print('\n')



class Knot():

	def __init__(self, value):
		self.value = value
		self.character = None
		self.right_branch = None
		self.left_branch = None


class Tree():

	def __init__(self):
		self.root = None

c = Compression()
text = 'e'*15+'i'*12+'a'*10+'t'*4+'s'*3+'p'*13+'n'*1
f = c.count_frequency(text)
print(f)
knots = c.knots_gen(f)

while len(knots) >= 2:
	knots = c.knots_order(knots)[::-1]
	knots = c.new_knot(knots)

c.print_knots(knots)