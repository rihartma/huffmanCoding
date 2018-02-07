class Files():

	def loadFile(self, name):
		text = ""
		file = open(name, 'r')
		text = file.read()
		file.close()
		return text

	def saveTable(self, text, name):
		file = open(name, 'w')
		file.write(text)
		file.close()

	def saveFile(self, name, text, codes):
		b = ""
		for char in text:
			b = b + codes[char]
		print(b)