# Import necessary libraries
import hashlib
import csv
import re
from Trie import TrieDatabase

# Function to clean up a word
def cleanup(word):
	word = word.lower()
	word = re.sub('[^A-Za-z0-9 ]+', '', word)
	#print word
	return word

# Function to hash a string
def hash(string):
	hash_object = hashlib.md5(string)
	return hash_object.hexdigest()
# Function to split a string by punctuation and spaces using re
def splitString(string):
	return re.findall(r"\w+|[^\w\s]", string, re.UNICODE)

# Function to concatenate all items in a list with spaces
def connectList(words):
	string = ''
	for i in range(0,len(words)):
		string = string + words[i] +' '
	return string[:-1]

# !!!SLOW!!! Function to search a string for names and replace them with hashed versions of those names
def searchAndReplaceSlow(string):
	word_list = splitString(string)

	item_num = 0
	for item in word_list:
		#print item	
		if str(item).lower() in names:
			#print item
			word_list[item_num] = hash(item)
		item_num = item_num+1

	return connectList(word_list)

# Function to search a string for names and replace them with hashed versions of those names
def searchAndReplaceINDEV(string, database):
	word_list = splitString(string)

	for i in range(0, len(word_list)):
		word = cleanup(word_list[i])

		if database.searchDec(word):
			#print True
			word_list[i] = hash(word)
		#else:
			#print False
	return connectList(word_list)

# Create a list to store all of the names
names = []

# Open first name database and convert it to a list
with open('Database_of_First_Names.csv', 'rU') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #for row in readCSV:
    #    print(row)
    names = list(readCSV)
    #print first_names

# Open last name database and convert it to a list
with open('Database_of_Last_Names.csv', 'rU') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #for row in readCSV:
    #    print(row)

    ''' UNCOMMENT THIS LINE TO ADD LAST NAMES INTO THE SEARCH'''
    #names = names +list(readCSV)

    #print last_names

# Convert names to lowercase
names = [str(name[0]).lower() for name in names]
# Create and add names to Trie Database
trie = TrieDatabase()
trie.addList(names)
#trie.display()

# Create example string
example_string = "Hello, bob, how is esther doing today?"

# Search and replace all names in the string with the hashed version of that name
print searchAndReplaceSlow(example_string)
print searchAndReplace(example_string, trie)