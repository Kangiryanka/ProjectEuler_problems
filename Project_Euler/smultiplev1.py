
#Old Approach
def smallest_multiple(n):
      count=0
      for i in range(11,21):

        if n % i == 0:
          count+=1
      return count


flag=True
number=11
while flag :

  divisors= smallest_multiple(number)
  print("The number of divisors for " + str(number) +  " are:  " + str(divisors))
  if divisors>9:
    flag=False
  else:
    number+=11
