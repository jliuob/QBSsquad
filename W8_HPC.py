def gcd(x,y):
  '''
  find greatest common divisor of two numbers
  '''
  if y == 0: #stopping condition (remainder is 0)
    return x
  else:
    return gcd(y, x % y)

def lcm(a,b):
  '''
  finding the least common multiple of two numbers
  '''
  return int(a*b/gcd(a,b))

def lcm_tuple(tup):
  return lcm(tup[0],tup[1])

def gcd_tuple(tup):
  return gcd(tup[0],tup[1])

def sumpairs(collection):
  return(sum(lcm_tuple(tup)+gcd_tuple(tup) for tup in collection))

pairs = []
for i in range(1,1001):
  for j in range(i+1,1001):
    pairs.append((i,j))

print(sumpairs(pairs))
%time print(sumpairs(pairs)) 
