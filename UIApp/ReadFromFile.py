import re

file = 'AppIDFile.txt'
path = 'C:\\Users\\labuser\\Documents\\GitHub\\AppIDEmailCreator\\UIApp'

filePath = open(path + '\\' + file)

fileStr= filePath.read()

print(fileStr)

