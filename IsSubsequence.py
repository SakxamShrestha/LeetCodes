'''
U
so, without disturbing the relative positions, find if s is a subsequence of t or not. 
M
hashmapping would never work here cause it does not preserve the poistions of a string. 
two pointers can work here, one pointer of s, and one pointer of t which moves and checks if pointer of s in equal to t or not at an index. 
P
indexOfs = indexOft = 0
while indexOfs do not reach s.length and indexOft does not reach t.length:
    if two chars are same:
        move one step right for small string s
    keep moving the pointer of string t nevertheless to check adn ierate through the string.     
I
R

E
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Hashing does not preserve order, so we cannot use that for sure. 
        #Two pointers is the way to go here. 
        pointerS = pointerT = 0
        while pointerS < len(s) and pointerT < len(t):
            if s[pointerS] == t[pointerT]:
                pointerS += 1
            pointerT += 1
        return pointerS == len(s)    


sol = Solution()
s = "aska"
t = "sasakaa"
print(sol.isSubsequence(s, t))
