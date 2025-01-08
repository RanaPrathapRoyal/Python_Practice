'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:
Input: coins = [2], amount = 3
Output: -1
Example 3:
Input: coins = [1], amount = 0
Output: 0
'''
Coin_count = {}
def Min_count_calc(Coins,amount):
    if len(l) == 0 or amount <=0:
        return 0
    else:
        for i in Coins:
            if amount >= i:
                coin = 1
                Coin_count[i] = amount // i
                amount = amount % i
        if amount == 0:
            for key, val in Coin_count.items():
                print(f"{key} : {val}")
        if amount > 0:
            print("-1")
l = []
Data = int(input("Enter the variaties of coins count : "))
for i in range(0,Data):
    Data1 = int(input("Enter the coins list : "))
    l.append(Data1)
amount = int(input("Enter the amount : "))
print(f"Coins list : {l}, Amount : {amount}")
l.sort(reverse=True)
Result = Min_count_calc(Coins=l,amount=amount)
