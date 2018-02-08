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
		b = ''
		for char in text:
			b = b + codes[char]
		filetext = ""
		for i in range(0, len(b)-8, 8):
			filetext = filetext + chr(int(b[i:i+8],2))
		filetext = filetext + b[len(b)-1-len(b)%8:-1]
		file = open(name, 'w')
		file.write(filetext)
		file.close()