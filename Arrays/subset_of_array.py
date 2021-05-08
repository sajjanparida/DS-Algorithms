def isSubset( a1, a2, n, m):
    
    flag= True
    
    s1=set()
    
    for i in a1:
        s1.add(i)
        
    for i in a2:
        print(i)
        if i not in s1:
            flag=False
            
    if flag==True:
        return "Yes"
    else:
        return "No"

print(isSubset([11,1,13,21,3,7],[11,3,7,1,8],1,1))