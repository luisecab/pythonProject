
'''
TODO 
1. Print the subsequent 2nd powers of elements in the list
2. Sum the 2nd powers of elements of the list
'''

num_list = [2, 5, 7, 9, 11, 13, 18]

def print_and_sum_squared_elements(num_list):

  # Print the subsequent 2nd powers of elements in the list.
  for element in num_list:
    print(element ** 2)

  # Sum the 2nd powers of elements of the list.
  sum_of_squared_elements = sum([element ** 2 for element in num_list])

  # Print the sum of squared elements.
  print("Sum of squared elements:", sum_of_squared_elements)

print_and_sum_squared_elements(num_list)


print('-------------------')
num_list_pow = [x**2 for x in num_list]
print(num_list_pow)
print(sum(num_list_pow))