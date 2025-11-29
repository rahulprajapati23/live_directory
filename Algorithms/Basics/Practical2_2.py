import matplotlib.pyplot as plt

def fib_iter(n):
    a, b = 0, 1
    steps = 0
    for month in range(n):
        a, b = b, a + b
        steps += 1
    return a, steps

def fib_recur(n):
    def helper(k):
        if k <= 1:
            return k, 1
        f1, s1 = helper(k - 1)
        f2, s2 = helper(k - 2)
        return f1 + f2, s1 + s2 + 1
    return helper(n)

def plot_steps():
    months = [2, 4, 12, 15,18,20]
    iter_steps = []
    recur_steps = []
    for m in months:
        _, steps_iter = fib_iter(m)
        _, steps_recur = fib_recur(m)
        iter_steps.append(steps_iter)
        recur_steps.append(steps_recur)
    plt.plot(months, iter_steps, label='Iterative')
    plt.plot(months, recur_steps, label='Recursive', linestyle='--')
    plt.xlabel('Months')
    plt.ylabel('Steps')
    plt.title('Steps Comparison')
    plt.legend()
    plt.show()

n = 24
pairs_iter, steps_iter = fib_iter(n)
pairs_recur, steps_recur = fib_recur(n)
print(f"Rabbit pairs after {n} months (Iterative): {pairs_iter}, Steps: {steps_iter}")
print(f"Rabbit pairs after {n} months (Recursive): {pairs_recur}, Steps: {steps_recur}")
plot_steps()