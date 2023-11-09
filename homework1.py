def prime(n):
  if n <= 1:
    return False  # Returns True if n is a prime number, False otherwise
  for i in range(2, int(n**0.5) + 1): # known common prime number logical code validator
    if n % i == 0:
      return False
  return True

def n_primes(n):
  count = 0    # prints the first N prime numbers
  num = 2      # we start from the first prime number
  while count < n:
    if prime(num):
      print(num)
      count += 1
    num += 1

# user inputs N
n = int(input("Enter the N number of prime numbers to print: "))

# Print the first N prime numbers
n_primes(n)




