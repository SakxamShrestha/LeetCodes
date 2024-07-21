"""
        Do not return anything, modify nums1 in-place instead.
        U
        We do not have to create any extra memmory in this question. We just want to modify nums1 by using two or maybe three pointers as well. Also, look out for the edge cases as it may affect your solution. Also, the numbers m , and n is significant cause they are there so make sure to use them in your solution.
        Also, time and space complexity we want is:
        Time 
        M
        use three pointers, 
        1st pointer: have at the back of your nums1(not exactly back but where the numbers are): m - 1
        2nd pointer: have at the back of your nums2: n - 1
        3rd pointer: this is the pointer at the real ending of nums1, where you start removing all those zeros and inserting the higher number between the two of nums1 or nums2 as both of them are alreasy sorted. 

        P
        3 pointers, 
        run a while loop until nums2 doesnt have any numbers left:
        if nums1[index1] > nums2[index2]:
            nums1[insertindex] = nums1[index1]
            index1 -= 1

        else:
            nums1[insertindex] = nums2[index2]
            index2 -= 1

        return nums1 (Sorry no returning cause we are just modifying the array here)        

        I
        R
        E
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1, index2, insertindex = m -1, n - 1, m + n - 1
        while index2 >= 0:
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[insertindex] = nums1[index1]
                index1 -= 1
            else:
                nums1[insertindex] = nums2[index2]
                index2 -= 1 
            insertindex -= 1    
#Also think of evaluating, run your code by using some examples like this. 
#Time Complexity: O(m + n) and Space Complexity is: O(1)

s = Solution()
nums1 = [2,3,4,5,6,7,0,0,0]
m = 6
nums2 = [1, 2, 50]
n = 3
s.merge(nums1, m , nums2 , n)
print(nums1)