from sys import argv
from files import Files
from huffmancoding import Compression, Decompression

try:
	f = Files()
	filetodecomp = argv[1]
	dfilename = argv[2]
	text = f.loadFile(filetodecomp)
	table = f.loadTable(filetodecomp[0:-4]+"_table.txt")
	d = Decompression()
	binar = d.makeBinar(text)
	decomptext = d.decompText(binar, table)
	f.saveTable(decomptext, dfilename)

except IndexError:
	print("Usage: python3 decompress.py <name-of-the-compressed-file> <decompressed_filename>")

except FileNotFoundError:
	print("Not valid filenames!")
	print("Usage: python3 decompress.py <name-of-the-compressed-file> <decompressed_filename>")