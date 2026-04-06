def plusOne(digits):
    k=len(digits)
    for i in range (k-1,-1,-1):
        digits[i]+=1
        if digits[i]<10:
            return digits
        digits[i]=0
    digits.insert(0,1)
    return digits

n=int(input())
digits= list(map(int,input().split()))
print(plusOne(digits))
