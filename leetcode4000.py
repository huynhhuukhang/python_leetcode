print("vui long nhap n")
n=int(input())
print("vui long nhap s")
s=int(input())
def sumDigit(x:int)->int:
    sum=0
    while x>0:
        sum+=x%10
        x//=10
    return sum


def largestInteger(n: int, s: int) -> int:
    for i in range(10**n-1,10**(n-1)-1,-1):
        if sumDigit(i)==s: 
            return i

    return -1

print(largestInteger(n,s))

