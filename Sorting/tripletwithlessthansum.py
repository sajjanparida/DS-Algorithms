
# program to find the count of triplets with sum less than given number


def triplets_sum(arr,n,req_sum):
    c=0
    arr.sort()
    for k in range(0,n-2):
        i=k+1
        j=n-1
        while i<j:
            if arr[k] + arr[i] + arr[j] < req_sum:
                c += j-i
                i += 1
            else:
                j -=1
    return c

arr=[-2,0,1,3]
print(triplets_sum(arr,4,2))




