class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        hashmap = {} #Creating a hashmap will always be of O(1) space, cause the size of it is independent of the number of size of the input array. 
        for c in s:
            if c  not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1

        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
                if hashmap[char] < 0:
                    return False 
            else:
                return False 


        return all(value == 0 for value in hashmap.values())                    

#Time Complexity is O(n) cause it can be seen that we are using for loop here. 
# Space complexity really here is O(1) cause like hashmap usage is like that always see above for more explanation. 