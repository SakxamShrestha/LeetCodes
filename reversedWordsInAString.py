'''
U
edge cases. so we remove all the white spaces in front of the string or at the end of the string. we also remove any extr spaces if present in between the words. 
if empty string exists, just return it as usual. 
if only one word exists, just return it without any space in front or between. 

M
my initial thought is to store all the words in an hashmap and give them like a key, lets suppose we use the index of each word as their key.
Well, use two pointers, one for the initial point fo the string and one to stop whenever it sees white space, for the next char after white space, set it as first pointer

P
s = strip(s)
fixed, moving = 0
hashmap = {}
res = ""
numbering = 0
for i in range(len(s)):
    if s[moving] == " ":
        hashmap[numbering] = s[fixed:moving]
        numbering += 1
        fixed = moving + 1
    moving += 1

for value in hashmap.values():
    res.append(value)
    res.append(" ")

return res 






I
R
E

'''
class Solution:
    def reverseWords(self, s: str) -> str:
        # Tokenize the input string to create a separate array
        arr = []
        temp = ""
        for c in s:
            if c != " ":
                temp += c 
            elif temp != "":
                arr.append(temp)
                temp = ""  #Resetting temp variable to an empty string 
        if temp != "":  # This is for the last string, if it does not face any white space and the loop finishes, we then only use this to get the last string too. 
            arr.append(temp)

        # Reverse the array of words
        l, r = 0, len(arr) - 1
        while l <= r:
            arr[l], arr[r] = arr[r], arr[l] #Reversing the position in the array. 
            l += 1
            r -= 1
        
        # Return a joined string version of the reversed array
        return " ".join(arr)  # This is to join the reversed array of strings with a space in between them. 

        return res.strip()

    
s = Solution()
string = "Is there still anything that love can do"
print(s.reverseWords(string))