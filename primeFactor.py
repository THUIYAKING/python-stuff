def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
number = 600851475143
largest = largest_prime_factor(number)
print(largest)