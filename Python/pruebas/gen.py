def firstn(n):
   num = 0
   while num < n:
       yield num
       num += 1

sum_of_first_n = list(firstn(55))
print(sum_of_first_n)