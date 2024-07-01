# Understand:

# Match: 

# Pseudocode:

# Implement:

# Review:

# Evaluate:


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for n in nums:
            if n in hashtable:
                return True 
            else:
                hashtable[n] = 1
        return False 

        #Time and Space Complexity both O(n)

        # This is the shortcut method that you can use maybe....no space complexity and time complexity, in constant time and space. 
        # return len(nums) != len(set(nums))

        