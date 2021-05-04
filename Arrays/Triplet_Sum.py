#Given an array and number k, find triplets in the array whose sum is equal to the given number


def triplets(arr,sum):
    arr.sort()

    for i in range(0,len(arr)):
        l=i+1
        r=len(arr)-1
        while l < r:
            if arr[i] + arr[l] + arr[r] == sum:
                return True
            elif arr[i] + arr[l] + arr[r] > sum:
                r -=1
            else:
                l += 1
        
    return False

arr=[1,2 ,4 ,3 ,6]
print(triplets(arr,10))


