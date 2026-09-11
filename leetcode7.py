n=int(input())

def reverse(n:int)->int:
    if n<0:
        dau=-1
    else:
        dau=1
    res=0
    n=abs(n)
    while(n>0):
        res=res*10+n%10
        n//=10
    return res*dau if -2**31<=res*dau<=2**31-1 else 0


print(reverse(n))