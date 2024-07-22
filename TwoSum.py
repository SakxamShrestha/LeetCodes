'''
U
so we have an nums array and target sum is to be found here. 

M
use a hashmap to store all the nums elements in a hashmap.make element as the key and the index as the value. 
for index, char in enumerate(nums):
    difference = target - c
    if difference in hashmap:
        return [index, hashmap[difference]]


P
hashmap creation of all the elements as keys and their index as values. 
for index, char in enumerate(nums):
    difference = target - char
    if difference in hashmap:
        return [index, hashmap[difference]]
I
R
E




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        index = 0
        for c in nums:
            if c not in hashmap:
                hashmap[c] = index 
                index += 1

        for i, char in enumerate(nums):
            diff = target - char
            if diff in hashmap and hashmap[diff] != hashmap[char]:
                return [ i, hashmap[diff]]        
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hashmap
        hashmap = dict()

        # Iterate through the array
        for i, num in enumerate(nums):
            # If we see the counterpart in our hashmap then return the index of the counterpart and current index
            if num in hashmap:
                return [hashmap[num], i]

            # Store the counterpart of the number we have seen and current index
            hashmap[target-num] = i #Store the array element as the key and the corresponding index as the value!

        