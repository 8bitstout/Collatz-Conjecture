# Python implementation of Collatz conjecture using recursion and memoizatoin
cache = dict()

n = input('Enter a number: ')

n = int(n)

def calc(n):
  print(n)
  if n == 1:
    return n
  elif n in cache:
    return calc(cache[n])
  elif n % 2 == 0:
    a = n/2
    cache[n] = a
    return calc(a)
  else:
    a = (n * 3) + 1
    cache[n] = a
    return calc(a)

calc(n)
