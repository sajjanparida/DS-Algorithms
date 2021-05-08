# Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
# 1. Each student gets exactly one packet.
# 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

def min_diff(arr,n , m):

    diff=float('INF')
    A.sort()

    k = m-1

    for i in range(0,n-m):
        curr_diff= A[k] - A[i]
        diff = min(curr_diff,diff)
        k=k+1

    return diff

arr=[3, 4, 1, 9, 56, 7, 9, 12]
print("Output is {}".format(min_diff(arr,8,5)))
