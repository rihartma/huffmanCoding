from sys import argv
from files import Files
from huffmancoding import Compression

try:
	f = Files()
	filetocomp = argv[1]
	newfile = argv[2]
	text = f.loadFile(filetocomp)

	c = Compression()
	freq = c.count_frequency(text)
	knots = c.knots_gen(freq)
	while(len(knots)>=2):
		knots = c.knots_order(knots)[::-1]
		knots = c.new_knot(knots)
	codes = c.huffman_code(knots)

	f.saveFile(newfile, text, codes)

except IndexError:
	print("Usage: python3 compress.py <filename-to-compress> <name-of-the-compressed-file>")

except FileNotFoundError:
	print("Not valid filenames!")
	print("Usage: python3 compress.py <filename-to-compress> <name-of-the-compressed-file>")