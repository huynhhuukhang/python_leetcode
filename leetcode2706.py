from typing import List

prices=[3,2,3]

money=int(input())
total=0
cnt=1
def buyChoco(prices: List[int], money: int) -> int:
    prices.sort()
    total=prices[0]+prices[1]
    if total <= money:
        return money-total

    return money

print(buyChoco(prices,money))