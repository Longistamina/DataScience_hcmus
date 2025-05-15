# Reference link: https://www.w3schools.com/python/python_regex.asp

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# Python has a built-in package called re, which can be used to work with Regular Expressions.

import re

re.findall()  #Returns a list containing all matches
re.search()	  #Returns a Match object if there is a match anywhere in the string
re.split()	  #Returns a list where the string has been split at each match
re.sub()	    #Replaces one or many matches with a string

#----------------------------------------------------------------------#
#------------------------------- Example ------------------------------#
#----------------------------------------------------------------------#
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

#------------------------------------------------------------------------------------------#
#-------------------------- "[]" ~ A set of characters ------------------------------------#
#------------------------------------------------------------------------------------------#
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x) #['h', 'e', 'a', 'i', 'i', 'a', 'i']

# [arn]	Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	Returns a match for any character EXCEPT a, r, and n	
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string


#------------------------------------------------------------------------------------------------------------------------------#
#-------------------------- "\" ~ Signals a special sequence, or escapes special character ------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------#
import re

txt = "That will be 59 dollars"

#Find all digit characters:
x = re.findall("\d", txt)
print(x) #['5', '9']


# Special characters:
## \A	Returns a match if the specified characters are at the beginning of the string =>	"\AThe"	

## \b	Returns a match where the specified characters are at the beginning or at the end of a word => r"\bain"; r"ain\b"
## (the "r" in the beginning is making sure that the string is being treated as a "raw string")	

## \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word => r"ain\B"; r"\Bain"
## (the "r" in the beginning is making sure that the string is being treated as a "raw string")	


## \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
## \D	Returns a match where the string DOES NOT contain digits	"\D"	

## \s	Returns a match where the string contains a white space character	"\s"	
## \S	Returns a match where the string DOES NOT contain a white space character	"\S"	

## \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
## \W	Returns a match where the string DOES NOT contain any word characters	"\W"	

## \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"


#--------------------------------------------------------------------------------------------------------------#
#-------------------------- "." ~ Any character (except newline character) ------------------------------------#
#--------------------------------------------------------------------------------------------------------------#
import re
txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x) #['hello']


#---------------------------------------------------------------------------------#
#-------------------------- "^" ~ Starts with ------------------------------------#
#---------------------------------------------------------------------------------#
import re
txt = "hello planet"

#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#Output: Yes, the string starts with 'hello'

#-------------------------------------------------------------------------------#
#-------------------------- "$" ~ Ends with ------------------------------------#
#-------------------------------------------------------------------------------#
import re
txt = "hello planet"

#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

#Output: Yes, the string ends with 'planet'

#----------------------------------------------------------------------------------------------#
#-------------------------- "*" ~ Zero or more occurrences ------------------------------------#
#----------------------------------------------------------------------------------------------#
import re
txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)

print(x) #['hello']

#---------------------------------------------------------------------------------------------#
#-------------------------- "*" ~ One or more occurrences ------------------------------------#
#---------------------------------------------------------------------------------------------#
import re
txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)

print(x)#['hello']

#---------------------------------------------------------------------------------------------#
#-------------------------- "?" ~ Zero or one occurrences ------------------------------------#
#---------------------------------------------------------------------------------------------#
import re
txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)

print(x) #[]
         #This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

#------------------------------------------------------------------------------------------------------------------#
#-------------------------- "{}" ~ Exactly the specified number of occurrences ------------------------------------#
#------------------------------------------------------------------------------------------------------------------#
import re
txt = "hello helllo planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)

print(x) #['hello']
         #Not return 'helllo' cause 'helllo' has 3 characters between "he" and "o"

#-------------------------------------------------------------------------------#
#-------------------------- "|" ~ Either or ------------------------------------#
#-------------------------------------------------------------------------------#
import re
txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)

print(x) #['falls']

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Output: Yes, there is at least one match!
