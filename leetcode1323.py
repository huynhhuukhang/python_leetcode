num=int(input())

def maximum69Number (num: int) -> int:
    if num==9999:return num
    cnt=0
    i=0
    res=[]
    while(num>0):
        if (num%10) % 6==0:
            cnt+=1
        res.append(num%10 * 10**i)
        i+=1
        num//=10
    if cnt==1: res[cnt-1]=9*(10**(cnt-1))
    if cnt>1: res[cnt]=9*(10**(cnt))
    return res
    #return sum(res) if sum(res)<=9999 else 9999

print(maximum69Number(num)) 
