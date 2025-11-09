# Lab 10: Get divisors

n = int(input("Enter a number: "))

divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

print("Divisors of", n, "are:", divisors)
