def Combination(n):
    FactN2=Factorial(n+2)
    FactN=Factorial(n)
    return int(FactN2/(2*FactN))
def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
test=int(input())
while test>0:
    num=int(input())
    answer=1
    while num!=0:
        dig=num%10
        answer=answer*Combination(dig)
        num=num//10
    test=test-1
    print(answer)
