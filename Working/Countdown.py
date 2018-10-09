import pickle, math
from math import *
def prime(n):
    if n==1 or n==0:
        return False
    if n==2 or n==3:
        return True
    if n%2==0:
        return False
    for i in range(3, int(n**(0.5))+1, 2):
        if n%i==0:
            return False
    return True

def twentysix_primes():
    L = []
    n = 2
    while len(L) < 26:
        if prime(n):
            L.append(n)
        n+=1
    return L

def prime_value(word, List):
    st = 'abcdefghijklmnopqrstuvwxyz'
    v = 1
    for char in word:
        ind = st.find(char)
        v *= List[ind]
    return v

def primefactors(n):
    '''Recursive function to generate the prime factors of a number'''
    #print "Calling fn for", n
    if n<=1:
        return []
    elif n==2:
        return [2]
    if n%2==0: #If n is divisible by 2, primefactors(n) = [2, primefactors(n/2)]
        p = primefactors(n/2)
        p.append(2)
        return p
    else:
        for i in range(3,int(sqrt(n))+1, 2):
            if n%i==0: #i will be a prime number
                p = primefactors(n/i)
                p.append(i)
                return p
        else: #Prime number base case
            return [n]


def binary(n):
    s = bin(n)
    s = s[2:]
    return s

def get_bin_list(n):
    L = []
    for i in range(2**n):
        s = binary(i)
        d = n - len(s)
        s = '0'*d + s
        L.append(s)
    return L

def every_subset(Set):
    l = len(Set)
    B = get_bin_list(l)
    Tot = []
    for c in range(2**l):
        TL = []
        for ind in range(len(B[c])):
            if B[c][ind] == '1':
                TL.append(Set[ind])
        Tot.append(tuple(TL))
    return Tot

def multiply(L):
    p = 1
    for n in L:
        p*=n
    return p

def products(Set):
    L = every_subset(Set)
    NT = []
    for T in L:
        NT.append(multiply(T))
    return NT
        
def unique(L):
    TL= set(L)
    NL= []
    for el in TL:
        NL.append(el)
    return NL

def largest(L):
    max = 0
    for i in range(1,len(L)):
        if L[i] > L[max]:
            max = i
    return max

def longest_word(s):
    Primes = twentysix_primes()
    val = prime_value(s,Primes)
    pfactors = primefactors(val)
    factors = unique(products(pfactors))
    Words = []
    Lengths = []
    for fact in factors:
        tv = val
        tv /= fact
        if tv in Dict:
            for i in Dict[tv]:
                Words.append(i)
                Lengths.append(len(i))
    m = largest(Lengths)
    return Words[m]
                
    

f = open("NewDict.dat","rb")
Dict = pickle.load(f)

while True:
    s = raw_input("Enter Scramble:")
    s.lower()
    print longest_word(s)
