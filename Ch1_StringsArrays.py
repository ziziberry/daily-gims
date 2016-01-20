import numpy as np 
import sys

# print sys.path

import pandas as pd 

## Chapter 1
# using additional list 
def is_unique1(string):
	char_list = []
	for x in string: 
		if x not in char_list:
			char_list.append(x)

	if len(char_list) < len(string):
		print "not all unique"
	else: 
		print "all unique"

# no additional data structures
def is_unique2(string):
	for x in xrange(len(string)):

		for y in xrange(x+1, len(string)):

			if string[x] == string[y]:
				print "not all unique"
				return

	if x == len(string)-1:
		print "all unique"

def check_permut(str1, str2):
	if len(str1)!=len(str2):
		print "not permutation"
		return
	else:
		for x in str1: 
			if x not in str2: 
				print "not permutation"
				return
		print "permutation"

# check_permut("zih","izh")

def urlify(string):
	for x in xrange(len(string)+2*string.count(" ")):
		# print x
		if string[x] == " ":
			# print string[x]
			# print string[:(x-1)]
			# print string[:x]
			string = string[:x]+"%20"+string[x+1:]
	print string

# urlify("zizi zhang")
# urlify("emeri zhang is going to do well on her calculus test")
def check_palin(string):
	char_dict = {}
	for char in string: 
		if char != " ":
			if char in char_dict.keys():
				char_dict[char]=char_dict[char]+1
			else: 
				char_dict[char]=1

	odd_count = 0
	for val in char_dict.values():
		if val % 2 != 0:
			odd_count=odd_count+1
	if odd_count > 1:
		print "False"
	else: 
		print "true"
	print char_dict

# check_palin("ahajkkjaha")

def string_compress(string):
	new_string = ""
	for x in xrange(len(string)):
		print x
		i=1
		for y in xrange(x+1, len(string)):
			if string[x] == string[y]:
				i=i+1
			else:
				break
		new_string = new_string + string[x]+str(i)
		x=x+i
	print new_string
string_compress("aaabbccaaa")

# def one_away(string1, string2):
# 	1. check that the lengths are within range of each other 
# 	2. if string legnths differ by one: 
# 		find sum and check that difference is less than 26
# 	3. if string lengths are the same: 
# 		check letter by letter
# 		if letters differ, continue and check that no more letters differ 

