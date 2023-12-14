def count_bowls():
    n = int(input("How many Bowls do we have?: "))
    if n <= 0:
        print("Bowls can't be negative.")
        return
    total_sum = 0
    for i in range(n, -1, -1):
        print(i)
        total_sum += i

    print("Sum of counts:", total_sum)

count_bowls()

