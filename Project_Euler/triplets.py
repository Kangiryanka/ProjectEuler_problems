
# Euclidean ormula to find the triplets
def triplets(m,n):
 a= m*m - n*n
 b= 2*m*n
 c= m*m + n*n
 triplet= (a,b,c)
 sum= a+b+c
 product= a*b*c
 print(triplet)
 print(product)
 return sum

i = 1
flag = True
while(flag):
  i= i+1
  for m in range(2,i):
    print("For m: " + str(m) )
    print("****************************")
    for j in range(1,m):
      print ("For n: " + str(j))
      sumOfTriplets= triplets(m,j)
      print(sumOfTriplets)

      if sumOfTriplets == 1000:
       print("Here we go !" )
       flag =False
