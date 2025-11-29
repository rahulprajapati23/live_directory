'''A thief carrying a single knapsack with limited (W = 5) capacity. The museum you stole had
(n=4) artefacts that you could steal. Unfortunately, you might not be able to steal the entire
artefact because of your limited knapsack capacity.
Help the thief to cherry pick the artefact in order to maximise the total profit (&lt;=W) of the
artefacts you stole.
First solve the given below example:
Let n = 4, W=5
(P1, P2, P3, P4) = (3,4,5,6)
(w1, w2, w3, w4) = (2,3,4,5)'''


def fractional_knapsack(W, wt, val, n):
    items = []
    for i in range(n):
        ratio = val[i] / wt[i]
        items.append((ratio, wt[i], val[i]))
    items.sort(reverse=True)

    total_prof = 0.0
    rem_cap = W
    for ratio, weight, profit in items:
        if rem_cap == 0:
            break
        if weight <= rem_cap:
            total_prof += profit
            rem_cap -= weight
        else:
            fraction = rem_cap / weight
            total_prof += profit * fraction
            rem_cap = 0
    return total_prof


val = [3, 4, 5, 6]
wt = [2, 3, 4, 5]
W = 5
n = len(val)
result = fractional_knapsack(W, wt, val, n)
print(f"Maximum profit in knapsack: {result}")
