'''
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
'''
# n = 3
# s = 6
# n = 4
# s2 = s + n


n = 8

#TODO count how many bowls do we have?

def bowl_count_loop_1(n):
    sum = 0
    for num in range(1, n+1, 1):
        sum += num
    return sum

print(bowl_count_loop_1(n))

x = 10
def bowl_count_loop_2(x):
    total_sum = 0
    for i in range(x, -1, -1):
        total_sum += i
        #print("Sum_of_count:", total_sum)
    return total_sum

print(bowl_count_loop_2(x))


j = 12

def bowl_recursive(j):
    if j == 1:
        return 1
    else:
        s = bowl_recursive(j-1) + j
        return s

print('Sum using sequence: {}'.format(bowl_count_loop_2(x)))
print('Sum using sequence: {}'.format(bowl_recursive(j)))
print('Sum using sequence: {}'.format(bowl_count_loop_1(n)))


def time_func(func, n):
    t0 = time()
    print('Calling: {} for n={}'.format(func, n))
    print('Result sum{}'.format(func(n)))
    t1 = time()
    elapsed = round(t1 - t0, 2)
    print(f'It took:{elapsed} sec')

n = 999
time_func(bowl_count_loop_2, n)