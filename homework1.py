# user inputs N
n = int(input("Enter the N number of prime numbers to print: "))

# we create a list to store the prime numbers

def is_prime(n):
  """Returns True if n is a prime number, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


def print_n_primes(n):
  """Prints the first n prime numbers."""
  count = 0
  num = 2
  while count < n:
    if is_prime(num):
      print(num)
      count += 1
    num += 1


# Get the value of N from the user
N = int(input("How many prime numbers do you want to print? "))

# Print the first N prime numbers
print_n_primes(N)




