# take a array find the maximum sum from a subarray.


class Array:

    def sum_of_array(self,arr):

        overallsum=0
        currentsum=0


        for i in arr:
            if currentsum>=0:
                currentsum = currentsum + i
            else:
                currentsum=i
            
            if currentsum > overallsum:
                overallsum = currentsum
                
        return overallsum

add = Array()
arr=[int(x) for x in input("Enter the Array").split(' ') ]
print("Sum of the subarray is {} ".format(add.sum_of_array(arr)))

