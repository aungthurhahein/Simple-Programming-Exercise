#! /usr/bin/env python

"""
This is version 0.45 of a collection of simple Python exercises constructed
(but in many cases only found and collected) by Torbjrn Lager (torbjorn.lager@ling.gu.se).
Most of them involve characters, words and phrases, rather than numbers, and
are therefore suitable for students interested in language rather than math.
"""


# Define a function max() that takes two numbers as arguments and returns the largest of them.
# Use the if-then-else construct available in Python.
# (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
def max(num1, num2):
  if num1 > num2:
    return num1 # print "{0} is greater than {1}".format(num1,num2)    
  elif num1 == num2:
    return "Null" # print "{0} is equal to {1}".format(num1,num2)
  else:
    return num2 # print "{0} is greater than {1}".format(num2,num1)


# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def max_of_three(num1, num2, num3):  
  max_num = max(num1,num2) # compare num1 and num2
  max_num = max(max_num,num3) # compare result of max(num1,num2) and third number
  return max_num


# Define a function that computes the length of a given list or string. 
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
def calc_len(obj):
	count = 0
	for char in obj:
		count = count+1
	return count


# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
def vowel_or_what(obj):
	vowel_list = ['a','e','i','o','u'] 

	# convert cap to small latter without using str.lower() 
	ascii_code = ord(obj)
	if ascii_code < 97:  # small a is 97
		ascii_code += 32 # for instance, A --> a (a+32)		
	small_obj = chr(ascii_code)

	# check exsitence of it in vowel_list
	for vowel in vowel_list:
		if small_obj == vowel:
			return True
			exit(1)
	return False
	

# Write a function translate() that will translate a text into "rvarsprket" (Swedish for "robber's language"). 
# That is, double every consonant and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".
def translate(obj):
	output_string=""
	for char in obj:
		if not vowel_or_what(char):
			output_string += char+'o'+char		
		else:
			output_string += char
	return output_string


# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. 
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
def sum(obj):
	result = 0
	for number in obj:
		result += float(number)
	return result


def multiply(obj):
	result = 1
	for number in obj:
		result *= float(number)
	return result


# Define a function reverse() that computes the reversal of a string. 
# For example, reverse("I am testing") should return the string "gnitset ma I".
def reverse(obj):	
	reverse_output = ""
	obj_len= calc_len(obj)
	for indx in range(0,obj_len):
		reverse_output += obj[obj_len-(indx+1)]
	return reverse_output


# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). 
# For example, is_palindrome("radar") should return True.
def is_palindrome(obj):
	obj_len= calc_len(obj)
	for indx in range(0,obj_len/2):	# just enumerate half of the len	
		if obj[indx] == obj[obj_len-(indx+1)]: # compare first char and last 
			continue		
		else:
			return "False"
			exit(1)
	return "True"			


# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and 
# returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, 
# but for the sake of the exercise you should pretend Python did not have this operator.)
def is_member(list_obj,list_item):
	for item in list_obj:  # still using in operator to enumerate the list (fail?)
		if list_item == item:
			return True
			exit(1)
	return False

# Define a function overlapping() that takes two lists and returns True if they have at least one member in common, 
# False otherwise. You may use your is_member() function, or the in operator, 
# but for the sake of the exercise, you should (also) write it using two nested for-loops.
def overlapping(list_obj1,list_obj2):
	for item1 in list_obj1:
		for item2 in list_obj2:
			if item1 == item2:
				return "True"
				exit(1)
	return "False"			


# Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, 
# consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". 
# (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". 
# For the sake of the exercise you should ignore that the problem can be solved in this manner.)
def generate_n_chars(integer,character):
	output = "" 
	for count in range(0,integer):
		output += character
	return output	


# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(list_obj):
	output = "" 
	for item in list_obj:
		output += generate_n_chars(item,"*") + "\n" # carriage return for line break
	return output


# The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, 
# respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? 
# Write a function max_in_list() that takes a list of numbers and returns the largest one.
def max_in_list(list_obj):
	list_len = calc_len(list_obj)  # just stick to the rule. len(list_obj) does the same thing though
	max_num = list_obj[0]
	for indx in range(1,list_len):  # enumerate list from second index 
		max_num = max(max_num,list_obj[indx])  # compare items from two consective indexs and get the max one and repeat it
	return max_num


# Write a program that maps a list of words into a list of integers 
# representing the lengths of the correponding words.
def word_map(list_obj):
	word_len = {} # first dicitionary usage
	for word in list_obj:
		str_len = calc_len(word)
		word_len[word] = str_len
	return word_len


# Write a function find_longest_word() that takes a list of words and 
# returns the length of the longest one.
def find_longest_word(list_obj):
	word_len_dict = word_map(list_obj) 
	longest_word = ""
	longest_length = 0
	for word,length in word_len_dict.iteritems(): 		
		if longest_length < length:
			longest_length = length
			longest_word = word
	return longest_word

# Write a function filter_long_words() that takes a list of words and an integer n and 
# returns the list of words that are longer than n.

def filter_long_words(list_obj,length_obj):
	word_len_dict = word_map(list_obj) 
	filter_words=[]
	for word,length in word_len_dict.iteritems(): 		
		if length > length_obj:
			filter_words.append(word)
	return filter_words

# Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", 
# "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", 
# "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". 
# Note that punctuation, capitalization, and spacing are usually ignored.

def is_thisphrase_palindrome(string_obj):

	# remove characters wihtout using str.replace and str.translate
	chars_remove = ['!',',','.',' ','?',':',';','-','_'] 
	cleanup_string = ""
	ready_string = ""

	# strip unnecessary chars
	for char in string_obj:		
		if not is_member(chars_remove,char):  # member look-up function we wrote back 
			cleanup_string += char

	#to lowercase
	for char in cleanup_string:
		ascii_code = ord(char) # str.ord change to ascii codes
		if ascii_code < 97:  # small a is 97
			ascii_code += 32 # for instance, A --> a = (a+32)
		ready_string += chr(ascii_code)
	
	#check palindrome
	return is_palindrome(ready_string)
	 	

# A pangram is a sentence that contains all the letters of the English alphabet at least once, 
# for example: The quick brown fox jumps over the lazy dog. 
# Your task here is to write a function to check a sentence to see if it is a pangram or not.
def is_pangram(string_obj):
	alphabet = range(97,123) # ascii code for a-z (you might think why not create A,B,C,D.. The answeer is we don't have time for that)
	for char in string_obj:
		ascii_char = ord(char) 
		if ascii_char < 97:  # small a is 97,
				ascii_char += 32 # for instance, A --> a = (a+32)		
		if is_member(alphabet, ascii_char): # remember that littel function we wrote		
			alphabet.remove(ascii_char) #remove from alphabet list														
	list_len = calc_len(alphabet)		
	if list_len == 0:
		return True
	else: 
		return False

# "99 Bottles of Beer" is a traditional song in the United States and Canada. 
# It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and 
# can take a long time to sing. The song's simple lyrics are as follows:
##########################################################################
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.
##########################################################################
# The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero.
# Your task here is write a Python program capable of generating all the verses of the song.
def bottles_of_Beer():	
	verse = "Take one down,pass it around,"	
	for i in range(0,100):
		print str(100-i) + " bottles of beer on the wall," + str(100-i) + " bottles of beer."
		print verse + str(99-i) + " bottles of beer on the wall.\n"


# Represent a small bilingual lexicon as a Python dictionary in the following fashion 
# {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"r"} 
# and use it to translate your Christmas cards from English into Swedish. 
# That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

def bilingual_lexicon(str_obj):
	lexicon = {"hello" : "mingalar", "holiday":"arrlatyat", "stupid": "ngaPain", "Scumbag": "ngaPwe"}
	for word,meaning in lexicon.iteritems():
		if word == str_obj:
			print meaning
		
# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. 
# Represent the frequency listing as a Python dictionary. 
# Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(str_obj):
	freq_dict = {}
	# this can be done with many built-in functions such as count() but let try with set datatype and nested loop
	unique_chr = list(set(str_obj))  #set is a python datatype that contains unique unordered list

	for char in unique_chr:
		count = 0
		for str_char in str_obj:
			if char == str_char:
				count += 1
		freq_dict[char] = count
	return freq_dict


# In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter 
# in the plain text is replaced by a letter some fixed number of positions down the alphabet. 
# For example, with a shift of 3, A would be replaced by D, B would become E, and so on. 
# The method is named after Julius Caesar, who used it to communicate with his generals. 
# ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the shift is 13. 
# In Python, the key for ROT-13 may be represented by means of the following dictionary:
#
# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
#        'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
#        'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
#        'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
#        'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
#        'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
#        'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

# Your task in this exercise is to implement an encoder/decoder of ROT-13. 
# Once you're done, you will be able to read the following secret message:

# Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!

# Note that since English has 26 characters, 
# your ROT-13 program will be able to both encode and decode texts written in English.
def rot_13_encode(str_obj):	
	# instead of using key lookup table,let do by shiffing ascii code to 13 characters
	# there are many python bulit-in functions to do this task such as maketrans(), translate()
	result = ""
	chars_ignore = ['!',',','.',' ','?',':',';','-','_'] #i might miss something. it's dumb but works fine.
	for character in str_obj:		
		if not is_member(chars_ignore,character):				
			ascii_char = ord(character)
			shift_13 = ascii_char + 13  # shift 13 char
			if shift_13 >= 123:		  # need to rotate back from a/A for chars out of range
				shift_13 -= 26				
			elif ascii_char <= 91 and shift_13 >= 91:  # some math manipulation
				shift_13 -= 26
			result += chr(shift_13)
			print ascii_char,shift_13,character
		else:
			result += character
	return result

def rot_13_decode(str_obj):
	# i am just being lazy here
	return rot_13_encode(str_obj)

# Define a simple "spelling correction" function correct() that takes a string and sees to it that 
# 1) two or more occurrences of the space character is compressed into one, and 
# 2) inserts an extra space after a period if the period is directly followed by a letter. 
# E.g. correct("This   is  very funny  and    cool.Indeed!") should return "This is very funny and cool. Indeed!" 
# Tip: Use regular expressions!
def spell_checker(str_obj):
	print str_obj


# The third person singular verb form in English is distinguished by the suffix -s, 
# which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:
# If the verb ends in y, remove it and add ies
# If the verb ends in o, ch, s, sh, x or z, add es
# By default just add s
# Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its third person singular form. 
# Test your function with words like try, brush, run and fix. 
# Note however that the rules must be regarded as heuristic, 
# in the sense that you must not expect them to work for all cases. Tip: Check out the string method endswith().
def make_3sg_form(str_obj):
	# endswith() check whether string end with a certain character or not(suprise!)
	# let do without using it
	str_len = calc_len(str_obj) - 1 
	str_list = []
	pluarl_trigger = ['o', 'ch', 's', 'sh', 'x','z']
	for char in str_obj: 
		str_list.append(char)
	if str_list[str_len] == 'y':
		str_list[str_len] = "ies"
	elif is_member(pluarl_trigger,str_list[str_len]):
		str_list[str_len] += "es"
	else:
		str_list[str_len] += "s"
	return ''.join(map(str, str_list)) #map function apply string cast to all list items and join after that

# In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. 
# A simple set of heuristic rules can be given as follows:
# If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, change ie to y and add ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding ing
# By default just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form. 
# Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.


