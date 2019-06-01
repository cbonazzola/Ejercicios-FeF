import numpy as np

acum=0
for i in range(1, 1000):
  if i % 3==0 or i % 5==0:
    acum=acum+i
  else:
    continue

print(acum)

maxdiv=1

def is_prime(a):
  ret=True
  for i in range(2, int(np.sqrt(a)+1)):
      if a % i != 0:
        continue
      else:
        ret=False
        break
  return ret 
      
600851475143
num=315
maxdiv=1
def recursion(num):
  for i in range(2,num):
    if num % i==0:
      num=int(num/i)
      if is_prime(i)==True:
         maxdiv=i
      else:
        continue
      break
      return num,maxdiv
    else:
      continue
315
while num>1:
  num,maxdiv=recursion(num)
    
num=315
for i in range(1,num):
  if num % i==0 and is_prime(i)==True:
      maxdiv=i
      break
  else:
      continue
  return maxdiv
print(maxdiv)
  

  

  
    