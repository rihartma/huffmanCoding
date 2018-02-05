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