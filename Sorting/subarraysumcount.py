
def countOfSubarray(arr,n):

    i=-1
    count=0
    sum=0
    freq={}
    freq[sum]=1
    while i < n-1:
        i +=1
        sum += arr[i]
        if freq.get(sum) != None:
            count += freq[sum]
            freq[sum]=freq[sum]+1
        else:
            freq[sum]=1
    return count

arr=[0,0,5,5,0,0]

print("The subarray with 0 sum is : {} ".format(countOfSubarray(arr,6)))