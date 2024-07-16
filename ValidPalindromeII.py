'''
Problem #1: Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1: 

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Example 3:

Input: s = "abc"
Output: false

U
I am thinking about maybe making two pointers, and a count which has a limit of one. if the limit is exceeded, the function should return false.
what if it is an empty string, maybe just return true then. 


M
Two pointers, one counter to count. 
use recursion until left pointer is equal to or more than the right pointer. 

P
count = 0 
l, r = 0 , len(s) - 1
if s[l] == s[r] and count <= 1:
return True 
elif s[l] != s[r]:
count += 1



I
R
E
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right, count):
            # Set the count if the number of skips done is above one, return false
            if count > 1:
                return False
            
            # Now move the start pointer to right so it points to a alphanumeric character. 
	    # Similarly move end pointer to left so it also points to a alphanumeric character
            while left < right:

                # Now check if both the characters are same or not (ignoring cases):
                # If it is not equal then we know string is not a valid palindrome, hence return two possibilities 
                # skip one character on the left or skip one or skip one character on the right. 
		# (be sure to reduce the number of available skips by 1)
                if s[left] != s[right]:
                    return isPalindrome(left+1, right, count+1) or isPalindrome(left, right-1, count+1)
                
               # Else continue to next iteration and repeat the same process of moving both pointers to point to next alphanumeric character till start<end.
                left += 1
                right -= 1
            
	    # After loop finishes, the string is said to be palindrome, hence return true.
            return True

        # Call start and end and point them with the two ends of the input string with the number of available skips to be 1.                       
        return isPalindrome(0, len(s)-1, 0)          

            