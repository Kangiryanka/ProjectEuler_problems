import math
def primes(n):
  # Generate a list of Booleans from 2 to n
  number_list= [True for x in range(0,n)]

  # The first multiplier is 2

  # prime = ab where a<= sqrt(n) and b is the multiplier
  for i in range(2,int(math.sqrt(n+1))):

    # All multiples will of the number will be marked as False

    # List index is shifted by 2  since the list starts at 2
    if number_list[i-2] == True:

        for multiplier in range(0,n):
          # Composite number= i^2 + multiplier * i
          #Example:
          # Composite number= 4 + 2*i
         composite= i*i + multiplier*i

         #Only mark the composite numbers <=n
         if composite <= n:
          number_list[composite-2] = False


  #Convert the Booleans to integers
  for i in range(0,n):
    if number_list[i] == True:
      number_list[i] = i+2

  return number_list

def get_primes(num_list):
  prime_list= []
  for i in range(0,len(num_list)):
    if (type(num_list[i])) == int:
      prime_list.append(num_list[i])
    if len(prime_list)== 10002:
      break
  return prime_list

print(primes(10))
