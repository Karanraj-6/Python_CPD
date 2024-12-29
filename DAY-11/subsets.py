def subsets_iterative(input_list):
    subsets = [[]]
    for elem in input_list:
        subsets += [current + [elem] for current in subsets]
    return subsets

input_list = [1, 2, 3]
input_list = subsets_iterative(input_list)

non_empty_subsets = [subset for subset in input_list if subset]

print("Non-empty Subsets:", non_empty_subsets)

sum  = 0

for i in non_empty_subsets:
    sum+=max(i)
print(sum)

input = [1, 2, 3]
subset = [[]]
for ele in input:
    subset += [current + [ele] for current in subset]

print(subset) 