# Find pair given Diff
def find_pair(arr,L,N):

    arr.sort()

    left=0
    right=left+1
    print(arr)
    while left<L and right<L:
        print(f'Current comparison between {arr[left]} and {arr[right]} ')
        if arr[right]-arr[left]<N:
            right += 1
        elif arr[right]-arr[left]>N:
            left +=1
        else:
            return 1
    
    return -1
    
arr=[90,70,20,80,50]
print(find_pair(arr,5,24))
        

