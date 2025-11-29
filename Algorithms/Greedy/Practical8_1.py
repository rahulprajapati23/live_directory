def fractional_knapsack(p, w, W):
    items = [(p[i], w[i], p[i]/w[i]) for i in range(len(p))]

    items.sort(key=lambda x: x[2], reverse=True)

    total_profit = 0
    fractions = []

    for profit, weight, ratio in items:
        if W == 0:
            break
        
        if weight <= W:
            total_profit += profit
            fractions.append(1)
            W -= weight
        else:
            frac = W / weight
            total_profit += profit * frac
            fractions.append(frac)
            W = 0 

    print("Fractions taken:", fractions)
    print("Total Profit:", total_profit)


p = [280, 100, 120, 120]
w = [40, 10, 20, 24]
W = 60
fractional_knapsack(p, w, W)
