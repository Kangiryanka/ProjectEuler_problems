# Every composite number can be expressed as product of its prime factors
# That's why we keep dividing with the loops.
def largestPrime(n):

    largest = 1
    multipleOfSix = 6

    while (n % 2 == 0):
        largest = 2
        n = n/2
    while (n % 3 == 0):
        largest = 3
        n = n/3

# Every prime can be expressed with 6n+1 or 6n-1
# The last operation should always give the biggest prime.
    while (multipleOfSix-1 <= n):
        if n % (multipleOfSix-1) == 0:
            largest = multipleOfSix - 1
            while (n % largest == 0):
                n = n/largest

        if n % (multipleOfSix+1) == 0:
            largest = multipleOfSix + 1
            while (n % largest == 0):
                n = n/largest
        multipleOfSix = multipleOfSix+6
    return largest


print(largestPrime(600851475143))
