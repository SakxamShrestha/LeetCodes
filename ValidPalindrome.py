'''
Understand:
So, from the question, we can see that we only consider alphanumeric values. So, all the spaces and if any symbols appear, we ignore them. for that, we have a built in function called .isalnum(). 
There is one edge case, what if the string is an empty string???
Do we skip through the unaccessable characters or not???

Example 1:(Difficult case)
Input: s = "A man, a plan, a canal: Panama" Output: true 

Example 2:(Happy case)
Input: s = "race a car" Output: false

Example 3: ( Edge case)
Input: s = " " Output: true


Match:
Can use two pointers???
or simply store in a string coming from backwards and compare at last if it is equivalent to the string or not.
But the best case scenario here is to not use any extra memory, so keep on comparing two pointers,
one from the start and one from the back until everything matches. 

Pseudocoding:
l , r = 0, len(s) - 1
while l < r:
    Check if character in l is alphanumeric or not:

    Check if character in r is alphanumeric or not:

    if they're alphanumeric, check if they are equal to each other or not. 

    move pointers closer to each other. 

    return True is it can pass the loop.

Implement

Review:
Lets just run it through some of the examples in the side. 

Evaluate:
So the space complexity of these is O(1) cause we didnt use any extra space but the time complexity is O(n) cause we did go through the string twice. 


'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            while l < r and not s[l].isalnum(): #Specifically for the blank spaces and fro characters that are not alphanumeric 
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if l > r or s[l] != s[r]:
                return False 

            l += 1
            r -= 1

        return True             
        

solution = Solution() #Just creating an instance of the solution to let our checking print run. 
print(solution.isPalindrome("race a car"))