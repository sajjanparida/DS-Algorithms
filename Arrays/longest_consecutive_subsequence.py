#Problem Statement: Give an array you need to find the longest consecutive subsequence.
# the subsequence can be in any order.


class Solution:

    def lcs(self,arr):

        dictionary = {}
        startelement=0
        curr_lcs=0
        o_lcs=0
        for i in arr:
            dictionary[i]=0

        for i in arr:
            if dictionary.get(i-1) == None:
                dictionary[i]=True
            else:
                dictionary[i]=False

        i=0
        length_of_array=len(arr)
        curr_lcs=1
        for i in arr:

            if dictionary.get(i)==True:
                startelement=i
                curr_lcs=1
                while dictionary.get(startelement+1) == False:
                    print("start element is {} ".format(startelement))
                    curr_lcs += 1
                    i += 1
                    startelement += 1
            if curr_lcs > o_lcs:
                o_lcs = curr_lcs
            
        return o_lcs


    
    
obj=Solution()
arr=[int(x) for x  in input("Enter the array").split(' ')]
print("Length of subsequence is {}".format(obj.lcs(arr)))