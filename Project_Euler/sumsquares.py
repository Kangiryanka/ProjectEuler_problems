import functools

def sum_of_squares(number_list):
 square_list = [x*x for x in number_list]
 result= functools.reduce(lambda a,b: a+b, square_list)
 return result



def square_of_sums(number_list):
  result= functools.reduce(lambda a,b: a+b, number_list)
  result*=result
  return result
number_list=[]

for i in range(1,101):
 number_list.append(i)

answer=square_of_sums(number_list)-sum_of_squares(number_list)
print(answer)
