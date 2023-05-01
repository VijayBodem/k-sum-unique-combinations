from itertools import combinations

num_list = list(map(int,input().split()))  # 2 4 6 1 3
num_list.sort()
n = int(input()) # 6
#print(num_list)
unique_sum = 0
for i in range(1,len(num_list)+1):
    common = set(combinations(num_list,i))
    #print(common)
    for j in common:
        #print(j)
        if sum(j) == n:
            unique_sum += 1
print(unique_sum)  # 3