'''
TODO
1. Print the subsequent 2nd powers of elements in the list
2. Sum the 2nd powers of elements of the list
'''

num_list = [2, 4, 6, 8, 10, 12, 14, 15]

num_list_2pow = [x * x for x in num_list]
print(num_list_2pow)
num_list_2pow_sort = sorted(num_list_2pow)
print(num_list_2pow_sort)
num_list_2pow_sort_r = sorted(num_list_2pow_sort, reverse=True)
print(num_list_2pow_sort_r)
print(sum(num_list_2pow_sort_r))

print('--------set---------')

set_nums = set(num_list_2pow_sort_r)
print(set_nums)

print('------tuples---------')
t = (10, 20, 30, 40, 50)
v, w, x, y, z = t
print(t)
print(v, w, x, y, z)
for i in t:
    print(i)

print('------tuples 2D------')
list_of_points = [(1, 2), (3, 2), (-1, 3)]
for x, y in list_of_points:
    print(f'x={x},y={y}')

print('---------matrix-------')
list_of_points_3d = [[1, 2, 3], [3, 2, 1], [-1, 3, 4]]
print(list_of_points_3d)

for row in list_of_points_3d:
    print(row)

# TODO:
# 1. Print the sum of each row
row_sums = []
for row in list_of_points_3d:
    row_sum = sum(row)
    row_sums.append(row_sum)
    print(f"{'The sum of the row'} {row}:{row_sum}")
print(row_sums)
# 2. Print the summ of each column
col_sums = [0, 0, 0]  # we start at 0
for row in list_of_points_3d:
    for i in range(len(row)):
        col_sums[i] += row[i]
print(col_sums)
# 3. Print the sum of all elements
print(sum(row_sums))

print('-----------------------')
lang = ['Python', 'Java', 'C++']
vers = [3.11, 17, 14]

lang_vers = list(zip(lang, vers))
print(lang_vers)

print('--------------------------')
col_sums_1 =[sum(els) for els in zip(*list_of_points_3d)]
print