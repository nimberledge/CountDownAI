from math import *
def factors(n):
    print "Fn call"
    if n<=1:
        return []
    elif n==2:
        return [2]
    if n%2==0:
        f = factors(n/2)
        f.append(2)
        return f
    else:
        for i in range(3,int(sqrt(n))+1,2):
            if n%i==0:
                f = factors(n/i)
                f.append(i)
                return f
        else:
            return [n]


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

while True:
    n = int(raw_input("No:"))
    L = primefactors(n)
    L.sort()
    P = unique(products(L))
    P.sort()
    print P
        
