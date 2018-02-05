class Files():

	def saveTable(self, text, name):
		file = open(name, 'w')
		file.write(text)
		file.close()