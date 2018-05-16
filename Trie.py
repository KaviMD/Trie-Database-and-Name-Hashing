import re

# Trie Database Class
class TrieDatabase(object):

	# Initizilation Method
	def __init__(self):
		self.test = ''
		self.start_char = '#'
		self.end_char = '#'
		self.root = Node(self.start_char, False)

	# Method to add a word to the Trie
	def addWord(self, word):
		cleaned = self.cleanup(word)
		#print cleaned
		#cleanup word
		master = self.root
		char_num = 0
		#print len(cleaned)
		for char in cleaned:
			#print char
			#print char_num
			if char_num >= len(cleaned)-1:
				endNode = Node(char,False)
				endNode.children.append(Node(self.end_char, True))
				master.children.append(endNode)
				#print 'created new node, final character'
				break

			#print 'not breaking'
			#print len(master.children)

			if len(master.children) == 0:
				master.children.append(Node(char,False))
				master = master.children[len(master.children)-1]
				#print 'creating first node in children'

			#print len(master.children)
			for i in range(0, len(master.children)):
				#print i
				if master.children[i].char == char:
					master.children[i].times = master.children[i].times + 1
					master = master.children[i]
					#print 'entering next level, node already exists'
					break

				elif i >= len(master.children)-1:
					master.children.append(Node(char,False))
					master = master.children[i+1]
					#print 'created new node, entering next level'
					break

			char_num = char_num+1

		#loop through each character in word, check if node already exists
			#yes: increment times node added, go on to next character
			#no: create node with character, times used 1, only end of word if last character


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
		char_num = 0
		for char in word:
			#print 'char'
			#print char
			#if char_num >= len(word)-1:
			#	return True
			node_num = 0
			#print len(master.children)
			for node in master.children:
				#print 'node.char'
				#print node.char
				#print node_num

				if node_num >= len(master.children)-1:
					return False

				if node.char == char:
					master = node
					#print 'entering next level'
					break

				node_num = node_num+1

			#char_num = char_num+1
		return True

	# Will be a method to recursively search the Trie
	def searchRec(self, word, base, letter_num):
		if letter_num == len(word):
			return True

	# Method to print out the whole Trie Database
	def display(self):
		self.recur(0,self.root)


	# Method to loop through the full Trie database
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
		self.children = []
		self.end = end
		self.times = 0