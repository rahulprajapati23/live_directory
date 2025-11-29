import matplotlib.pyplot as plt
recursion_steps = 0
def sum_loop(n):
    steps = 0
    total = 0
    for i in range(1, n + 1):
        total = total + i
        steps = steps + 1
    return total, steps
def sum_equation(n):
    steps = 1
    total = n * (n + 1) // 2
    return total, steps
def sum_recursive(n):
    global recursion_steps
    recursion_steps = recursion_steps + 1
    if n == 1:
        return 1
    return n + sum_recursive(n-1)
n_values=[]
N=int(input("enter how many test cases you want:"))
for i in range(1,N+1):
    n_values.append(int(input("enter the no. of clients:")))
loop_step_list = []
equan_steps = []
recur_steps = []
print("Clients", "loop_steps", "equation_steps", "recursion_steps")
for n in n_values:
    result_loop, loop_steps = sum_loop(n)
    result_equation, equation_steps = sum_equation(n)
    recursion_steps = 0
    result_rec = sum_recursive(n)
    loop_step_list.append(loop_steps)
    equan_steps.append(equation_steps)
    recur_steps.append(recursion_steps)
    print(f" {n}     \t{loop_steps}  \t{equation_steps}\t\t{recursion_steps}")
plt.plot(n_values, loop_step_list, label="Loop", marker='o',color='black')
plt.plot(n_values, equan_steps, label="equation", marker='o')
plt.plot(n_values, recur_steps, label="Recursion", marker='+',linestyle='dotted',color='yellow')
plt.xlabel("N (Number of Clients)")
plt.ylabel("Step Count")
plt.title("Comparison of Step Counts for Sum Calculation Methods")
plt.legend()
plt.grid(True)
plt.show()