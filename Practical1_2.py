def func(arr,n):
    min_num = float('inf')
    main = []
    for i in range(0, n):
        for j in range(i + 1, n):
            num = arr[i] + arr[j]
            abs_val = abs(num)
            if abs_val==min_num:
                main.append([arr[i], arr[j]])
            elif abs_val < min_num:
                main.clear()
                min_num = abs_val
                main = [[arr[i], arr[j]]]
    return main

arr = []
while True:
    n=int(input("enter number of elements: "))
    if n < 2:
        print("minimum 2 element is mandatory.")
    else:
        break
for i in range(0, n):
    arr.append(int(input(f"enter {i+1} element: ")))

print(f"output: {func(arr,n)}")