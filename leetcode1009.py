n=int(input())
if n==0:
    print(1)
    exit()
mask = 1
while mask < n:
    mask = (mask << 1) | 1
print(mask ^ n)
exit()