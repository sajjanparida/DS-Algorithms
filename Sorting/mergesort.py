 def mergesort(arr,lo,high):

     if lo == high:
         return

    mid = (low + high)//2

    larr=arr[:mid]
    sarr=arr[mid+1:]

    for i in arr