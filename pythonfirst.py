from random import random 

N = 1000000
n = 0 

for i in range(N):
  x = random()
  y = random()
  n = n + 1
  
print(4*n/N)
