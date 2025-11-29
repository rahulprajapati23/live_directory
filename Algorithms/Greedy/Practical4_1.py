import random as rd

def coin_counter(coins, tests):
    coins.sort(reverse=True)
    counts = []
    for i in range(0, len(tests)):
        min_count = float("inf")
        for start in range(len(coins)):
            temp_count = 0
            total = 0
            for j in range(start, len(coins)):
                temp_coin = coins[j]
                while tests[i] > total:
                    total += temp_coin
                    temp_count += 1
                if total > tests[i]:
                    total -= temp_coin
                    temp_count -= 1
            if total == tests[i] and temp_count < min_count:
                min_count = temp_count
        print(f"minimum number of coin for {tests[i]} is {min_count}")
        counts.append(min_count)
    return counts

coins = []
num_coin = int(input("enter number of coins you have:"))
for k in range(0, num_coin):
        coins.append(int(input(f"enter {k+1} coin:")))

num = int(input("enter number of test_cases you want:"))
choice = int(input("<0> take random element \n<1> enter elements manualy \n0 or 1:"))
tests = []

if choice == 0:
    for i in range(0, num):
        tests.append(rd.randint(1, 100))
    print(f"list:{tests}")
    coin_counter(coins, tests)
elif choice == 1:
    for i in range(0, num):
        tests.append(int(input(f"enter {i+1} element:")))
    print(f"list:{tests}")
    coin_counter(coins, tests)
else:
    print("invalid choice :(")

print("thank you:)")
