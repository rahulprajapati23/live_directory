import random
import matplotlib.pyplot as plt

# Bubble Sort 
def bubble_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps += 1  
    return steps

#Insertion Sort
def insertion_sort(arr):
    steps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        steps += 1  
        while j >= 0 and arr[j] > key:
            steps += 1  
            arr[j + 1] = arr[j]  
            steps += 1
            j -= 1
        arr[j + 1] = key
        steps += 1 
    return steps

#Selection sort
def selection_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            steps += 1 
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        steps += 1 
    return steps

sizes = [10, 50, 100, 150, 200]
b_steps = []
i_steps = []
s_steps = []

for size in sizes:
    data = []
    for k in range(size):
        data.append(random.randint(1, 500)) 
    print(f"data{size}:{data}")
    b_steps.append(bubble_sort(data.copy()))
    i_steps.append(insertion_sort(data.copy()))
    s_steps.append(selection_sort(data.copy()))

plt.plot(sizes, b_steps, label="Bubble Sort", marker='o')
plt.plot(sizes, i_steps, label="Insertion Sort", marker='o')
plt.plot(sizes, s_steps, label="Selection Sort", marker='o')

plt.xlabel("Number of Elements (n)")
plt.ylabel("Steps (operations)")
plt.title("Sorting Algorithm Comparison (Step Count)")
plt.legend()
plt.grid(True)
plt.show()
