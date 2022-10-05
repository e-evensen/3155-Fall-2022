# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

from multiprocessing.dummy.connection import families


def count_threes(n):
  # YOUR CODE HERE
  threedict = {
    3: 0,
    6: 0,
    9: 0
  }
  for i in range(0, len(n)):
    num = int(n[i])
    if (num == 3 or num == 6 or num == 9):
      threedict[num] += 1
  
  if (threedict[3] > threedict[6] and threedict[3] > threedict[9]):
    return 3
  elif (threedict[6] > threedict[9]):
    return 6
  else:
    return 9


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  chardict = {

  }
  longest = 1
  former = ''
  currLength = 0
  for i in range(0, len(s)):
    current = s[i]
    if (i > 0):
      former = s[i-1]

    if (former is current):
      currLength += 1
      if (currLength > longest):
        longest = currLength
    else:
      currLength = 1

    if (current in chardict):
      if (currLength > chardict[current]):
        chardict.update({current: currLength})
    else:
      chardict.update({current: currLength})

  maxChars = [key for key, value in chardict.items() if value == longest]
  return maxChars


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  temp = s.replace(" ", "")
  pali = ""

  for i in range(len(temp)):
    pali = pali + lowerChar(temp[i])
    
  if (pali == pali[::-1]):
    return True
  else:
    return False

def lowerChar(char):
   if (ord(char) >= 65 and ord(char) <= 90):
      return chr(ord(char)+32)
   else:
      return char
