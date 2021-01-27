import math
from functools import reduce
import operator

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def xgcd (a , b) :
    px, py, x, y = 1, 0, 0, 1
    while b :
        q = a//b
        x, px = px-q*x, x
        y, py = py-q*y, y
        a, b = b, a%b
    return a, px, py

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

def sieve(limit):
    a = [True] * limit                         
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     
                a[n] = False

def prime_sieve(n):
    """
    Return a list of prime numbers from 2 to a prime < n. Very fast (n<10,000,000) in 0.4 sec.
    
    Example:
    >>>prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]

    Algorithm & Python source: Robert William Hanks
    http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
    """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def binom(n,k):
    return math.factorial(n) // math.factorial(n-k) // math.factorial(k)

def factors(n):    
    j = 2
    while n > 1:
        for i in range(j, int(math.sqrt(n+0.05)) + 1):
            if n % i == 0:
                n //= i ; j = i
                yield i
                break
        else:
            if n > 1:
                yield n; break

def prime_factors(n):
    prime_list = list(factors(n))
    prime_dic = dict()
    for i in prime_list:
        if i not in prime_dic:
            prime_dic[i] = 1
        else:
            prime_dic[i] += 1
    return prime_dic

def nu(n,p):
	s = 0
	while n > 0:
		s += n//p
		n = n/p
	return int(s)


def fast_exp(b,e,m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1:
            r = (r * b) % m
    return r

'''Similar to sum(iterable)'''
def prod(iterable):
    return reduce(operator.mul, iterable, 1)
