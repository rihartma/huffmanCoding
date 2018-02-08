from sys import argv
from files import Files
from huffmancoding import Compression, Decompression


f = Files()
filetodecomp = argv[1]
text = f.loadFile(filetodecomp)
table = f.loadTable(filetodecomp[0:-4]+"_table.txt")
d = Decompression()
binar = d.makeBinar(text)
decomptext = d.decompText(binar, table)
print(decomptext)