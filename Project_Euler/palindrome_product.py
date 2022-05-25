def isPalindrome(n):
    numberString = str(n)
    beginning_end = slice(1, -1)
    while len(numberString) > 0:
        if numberString[0] == numberString[-1]:
            numberString = numberString[beginning_end]
        else:
            return False
    return True


def largestPalindrome():

    max_product = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if isPalindrome(product):
                if product > max_product:
                    max_product = product
    return max_product
