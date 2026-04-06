n=int(input())

def Try(i,s):
    if i==n:
        print(s)
        return
        

    Try(i+1,s+"0")
    Try(i+1,s+"1")

Try(0,"")
