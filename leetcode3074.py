from typing import List

apple=[1,3,2]
capacity=[4,3,1,5,2]

def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
    cnt=0
    sum_weight=0
    sum_capacity=0
    for i in range(0,len(apple),1):
        sum_weight+=apple[i]
    capacity.sort()
    for i in range(len(capacity)-1,-1,-1):
        if sum_capacity >=sum_weight: break
        sum_capacity+=capacity[i]
        cnt+=1

    return cnt


print(minimumBoxes(apple,capacity))

