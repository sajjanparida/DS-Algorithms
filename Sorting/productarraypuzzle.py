def productExceptSelf(nums, n):
        #code here
    zeroflag=0
    product=1
    if n==1:
        return 1
        
    for i in range(0,n):
        if nums[i]!= 0 :
            product *= nums[i]
        else:
            zeroflag += 1

    if zeroflag==1:
        for i in range(0,n):
            if nums[i]==0:
                nums[i] = product
            else:
                nums[i]=0
    elif zeroflag>1:
        for i in range(0,n):
            nums[i]=0
    else:
        for i in range(0,n):
            nums[i]=product//nums[i]
            
    return nums

nums=[1,0,5,0,7]
print(productExceptSelf(nums,5))