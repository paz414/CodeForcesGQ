def bestindex(arr):
    m1,m2,m3=-99,-99,-99
    max1,max2,max3=0,0,0
    for i in range(len(arr)):
        if arr[i]>m1:
            max3,m3=max2,m2
            max2,m2 = max1,m1
            max1,m1=i,arr[i]
        elif arr[i]>m2:
            max3,m3=max2,m2
            max2,m2=i,arr[i]
        elif arr[i]>m3:
            m3=arr[i]
            max3=i
    return [max1,max2,max3]
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    bestindexA= bestindex(a)
    bestindexB= bestindex(b)
    bestindexC= bestindex(c)
    ans=-1
    for i in bestindexA:
        for j in bestindexB:
            for k in bestindexC:
                if i!=j!=k!=i:
                    ans=max(ans,a[i]+b[j]+c[k])
    print(ans)


 
