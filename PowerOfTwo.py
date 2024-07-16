'''
U
M
P
I
R
E
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:    #When the remainder number is 1, just return true cause 1 is a power of two and ultimately it is the smalest number denomination you can get
            return True 
        if n % 2 != 0 or n == 0 : # IF the number is not divisible by 2 or it is a zero(Exception), just return False
            return False 
        return self.isPowerOfTwo(n/2)   # Keep doing recursion(Self. function) until the n becomes one and return True or becomes False under other conditions.   
        