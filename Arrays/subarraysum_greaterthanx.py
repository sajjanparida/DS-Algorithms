# Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

# Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).



def smallestsubwithsum(arr,n,x):

    min_len = n+1
    curr_sum=0

    start = 0
    end = 0

    while end < n:
        while curr_sum <=x and end < n:
        curr_sum = curr_sum + arr[end]
        end += 1

        while curr_sum > x and start < n:
        
            if end - start < min_len:
                min_len = end - start

            curr_sum -= arr[start]
            start += 1
    
    return min_len

arr=[1, 4, 45, 6, 0, 19]
print("Output is : {} ".format(smallestsubwithsum(arr,6,51)))
