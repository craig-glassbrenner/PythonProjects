""" 
	Craig Glassbrenner
	CS461, Markov Text Generator

	Given a text file, this program will generate text based on
	how much data given in the text file and other command line
	arguments.

"""
import sys
import random

# Opens File and returns contents of file.
def readFile(filename):
	f = open(filename, "r")
	contents = f.read()
	return contents

# Creates the Dictionary of Prefixes and Suffixes
# Basically what word comes after a word or series of words.
def mapDict(c, l):
	dic = {}
	words = c.split()
	i = 0

	for word in words[i:]:
		k = ' '.join(words[i:i+l]).split()
		k = tuple(k)
		if i+l < len(words):

			if k in dic:
				dic[k].append(words[i+l])
			else:
				dic[k] = [words[i+l]]

		else:
			dic[k] = None
			break

		i = i + 1
	return dic

# Based on random choice for the prefix, this function will generate
# words and sentences based on the following suffixes.
def produceOutput(dic, l):
	cont = True
	toReturn = ""
	tup = random.choice(list(dic.keys()))
	if(dic[tup] is None):
		cont = False
	else:
		word = random.choice(dic[tup])
		toReturn = toReturn + word
	
	while(cont):
		tupList = list(tup)
		tupList = tupList[1:]
		tupList[len(tupList):] = [word]

		tup = tuple(tupList)
		if(dic[tup] is None):
			break
		else:
			word = random.choice(dic[tup])
			toReturn = toReturn + " " + word

	return toReturn

	
def main():
	if len(sys.argv) != 3:
		print("Usage: ./markov.py file prefixlength")
		sys.exit(1)

	filename = sys.argv[1]
	prefixlength = int(sys.argv[2])

	content = readFile(filename)
	prefixDic = mapDict(content, prefixlength)
	output = produceOutput(prefixDic, prefixlength)

	print(output)


if __name__ == '__main__':
	main()









