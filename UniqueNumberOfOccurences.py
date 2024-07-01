'''
Understand:
So, can we do this in a array with a single element. I think true. 
what if it is an empty array, I think false????? No, the question must have a single element in the array.

M
i think hashmap. and then for loop for the values in the dictionary to see if they are same or not, if they are return False and if they are not return True. 
P
lauch an empty dictionary here. 
put all the array elements with their repetition numbers here. 
again run a loop for only the values??? maybe???
and maybe put the values in a array and make a set out of it and if they are not same, the return value is False. 

I
I am still thinking 

Review:
Yeah, the code is good now, but if the interviwer asks you to not use defaultdict, you have to think of smth else. i will find how to add elements in hashmap without 
E
'''




class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        hashtable = {}

        for element in arr:
            if element in hashtable:
                hashtable[element] += 1
            else:
                hashtable[element] = 1    
        

#SEcond approach for adding elements in a hashmap, shortcut one but can be used. 
        # hashtable = defaultdict(int)  #Defaultdict automatically puts every key value to zero in hashtable

        # for n in arr:
        #     hashtable[n] += 1  # for every element found, we just have to add it. 


        return len(list(hashtable.values())) == len(set(hashtable.values())) # checking the length of the list vs the set, if it not the same, then there are duplicate occurences and the answrr is False. 

        # the time complexity for this is O(n). But, if we had sorted . we know that sorting algorithm always has O(nlogn) time complexity so it would be less efficient that this. 


        