import functools


# Find the gcd where a>b
def gcd(a,b):
  answer=0
  if a == 0:
    answer= b
    return gcd
  elif b==0:
    answer= a
    return answer
  else:
    remainder = int(a%b)
    return gcd(b,remainder)

#lcm(a, b) = ab/gcd(a,b))
def lcm(a,b):
    return a*b/gcd(a,b)

#lcm(xi+2,lcm(xi,xi+1))
list=[11,12,13,14,15,16,17,18,19,20]
smallest_multiple=functools.reduce(lambda a, b: lcm(a,b), list)
print(smallest_multiple)
