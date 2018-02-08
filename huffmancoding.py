class Compression():

	def __init__(self):
		self.huffman_codes = {}

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

	def huffman_code(self, knots):
		'''
		returns a dictionary {key-character:value-huffmancode}
		'''
		self._huffman_code(knots[0], '')
		return self.huffman_codes

	def _huffman_code(self, knot, code):
		if knot.character != None:
			self.huffman_codes[knot.character] = code
		else:
			self._huffman_code(knot.left_branch, code+'0')
			self._huffman_code(knot.right_branch, code+'1')

	def save_table(self, knots):
		text = ""
		for key in knots:
			text = text + key + "-" + str(knots[key]) + ","
		return text[0:-1]


	def print_knots(self, knots):
		for knot in knots:
			print(knot.value, knot.character)
		print('\n')


class Decompression():

	def makeBinar(self, text):
		b = ""
		last_i = -1
		if "~~~" in text and text.index("~~~") in range(len(text)-16, len(text)):
			print(True)
			last_i = text.index("~~~")
			print(last_i)
		for ch in text[0:last_i]:
			code = bin(ord(ch))[2:]
			code = "0"*(8-len(code)) + code
			b = b + code
		if last_i != -1:
			b = b + text[last_i+3:len(text)]
		return b


class Knot():

	def __init__(self, value):
		self.value = value
		self.character = None
		self.right_branch = None
		self.left_branch = None


# c = Compression()
# text = 'a'*10+'e'*15+'i'*12+'s'*3+'t'*4+'p'*13+'n'*1
# f = c.count_frequency(text)
# print(f)
# knots = c.knots_gen(f)

# while len(knots) >= 2:
# 	knots = c.knots_order(knots)[::-1]
# 	knots = c.new_knot(knots)

# codes = (c.huffman_code(knots))
# print(codes)
# print(c.save_table(codes))

d = Decompression()
print(d.makeBinar("ahoj~~~10"))