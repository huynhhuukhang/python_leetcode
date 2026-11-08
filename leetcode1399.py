n=int(input())

def sumDigitNum(n:int)->int:
    cnt=0
    while n>0:
        cnt+=n%10
        n//=10
    return cnt


def countLargestGroup(n:int) -> int:
    max_sum=9 * len(str(n))
    cnt=[0]*(max_sum+1)

    for i in range(1,n+1):
        cnt[sumDigitNum(i)]+=1

    max_size=max(cnt)
    return sum(1 for i in cnt if i== max_size)

print(countLargestGroup(n))



