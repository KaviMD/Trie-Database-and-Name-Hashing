import re

# Trie Database Class
class TrieDatabase(object):

	# Initizilation Method
	def __init__(self):
		self.test = ''
		self.start_char = '{'
		self.end_char = '}'
		self.root = Node(self.start_char, False)

	# Method to add a word to the Trie
	def addWord(self, word):
		cleaned = self.cleanup(word)
		if cleaned == '':
			return 'The string \'%s\' is empty after extra characters are removed. It will not be added' % (word)

		master = self.root

		for char in cleaned:

			position = ord(char)-97
			child_num = master.node_locations[position]
			
			if child_num >= 0:
				master = master.children[child_num]
			else:
				master.children.append(Node(char,False))
				master.node_locations[position] = len(master.children)-1
				master = master.children[len(master.children)-1]

		master.children.append(Node(self.end_char, True))
		master.node_locations[ord(self.end_char)-97] = len(master.children)-1	

	# Method to add a list of words to the Trie
	def addList(self, word_list):
		#print word_list
		for i in range(0, len(word_list)):
			self.addWord(word_list[i]) 

	##################################################################
	### Unimplemented Methods to remove a word,                    ###
	### a list of words, or save/load the Trie to/from a JSON file ###
	##################################################################

	'''
	def remove(self):
		pass

	def removeList(self):
		pass

	def saveAsJSON(self):
		pass

	def loadFromJSON(self):
		pass
	'''

	# Method to search the Trie
	def searchDec(self, word):
		master = self.root

		word = self.cleanup(word)
		if word == '':
			return False

		for char in word:
			location = master.node_locations[ord(char)-97]
			if location >= 0:
				master = master.children[location]
			else:
				return False

		if master.node_locations[ord(self.end_char)-97] < 0:
			return False

		return True

	# !!! SLOW !!! Method to recursively search the Trie
	def searchRec(self,word):
		return self.searchRecur(word, self.root, 0)

	def searchRecur(self, word, base,letter_num):
		returnVal = False
		if letter_num == len(word):
			return True
		for i in range(0, len(base.children)):
			returnVal = self.searchRecur(word, base.children[i], letter_num+1)
			if returnVal:
				break

		return returnVal

	# Method to print out the whole Trie Database
	def display(self):
		print self.recur(0,self.root)

	def recur(self,level,base):

		if len(base.children) < 1:
			print ('\t'*level)+base.char
		else:
			print ('\t'*level)+base.char
			for i in range(0, len(base.children)):
				self.recur(level+1, base.children[i])

	# Method to clean up a word
	def cleanup(self,word):
		word = word.lower()
		word = re.sub('[^A-Za-z0-9 ]+', '', word)
		#print word
		return word
		
# Node class for Trie Database
class Node(object):
	def __init__(self, char, end):
		self.char = char
		self.node_locations = [-1]*29
		self.children = []
		self.end = end
		self.times = 0