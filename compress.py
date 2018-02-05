from sys import argv
from files import Files

try:
	f = Files()
	filetocomp = argv[1]
	newfile = argv[2]
	text = f.loadFile(filetocomp)

except IndexError:
	print("Usage: python3 compress.py <filename-to-compress> <name-of-the-compressed-file>")

except FileNotFoundError:
	print("Not valid filenames!")
	print("Usage: python3 compress.py <filename-to-compress> <name-of-the-compressed-file>")	