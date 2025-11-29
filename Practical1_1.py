"""**********************************************************BEST CHEF COMPITITION**********************************************************"""
def competition(chef_1, chef_2):
    chef1_point = 0
    chef2_point = 0
    for i in range(0, 3):
        if chef_1[i] > chef_2[i]:
            chef1_point += 1
        elif chef_2[i] > chef_1[i]:
            chef2_point += 1
    return chef1_point, chef2_point

chef_1 = []
chef_2 = []

print("enter first chef's review{1.presentation,2.taste,3.hygiene}")
for j in range(0, 3):
    chef_1.append(int(input(f"--<{j+1}>-- ")))
print("enter second chef's review{1.presentation,2.taste,3.hygiene}")
for j in range(0, 3):
    chef_2.append(int(input(f"--<{j+1}>-- ")))

chef1_point, chef2_point = competition(chef_1, chef_2)
print(f"point of chef_1={chef1_point}\npoint of chef_2={chef2_point}")
