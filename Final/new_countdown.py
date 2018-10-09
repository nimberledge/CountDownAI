import pickle, math
from math import *
import time
import random
def prime(n):
    if n==1 or n==0:
        return False
    if n==2 or n==3:
        return True
    if n%2==0:
        return False
    for i in xrange(3, int(n**(0.5))+1, 2):
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
        for i in xrange(3,int(sqrt(n))+1, 2):
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

def process_dict(prime_dict):
    new_dict = {}
    for key in prime_dict:
        for word in prime_dict[key]:
            if len(word) in new_dict:
                new_dict[len(word)].append(word)
            else:
                new_dict[len(word)] = [word]
    return new_dict

def reverse_dict(prime_dict):
    rev_dict = {}
    for key in prime_dict:
        for val in prime_dict[key]:
            rev_dict[val] = key
    return rev_dict

def longest_word_new(s):
    primes = twentysix_primes()
    val = prime_value(s, primes)
    for i in range(28, -1, -1):
        if i in new_dict:
            for word in new_dict[i]:
                p = rev_dict[word]
                if val % p == 0:
                    return word
    return ''

def time_function(f, scrambles):
    locals = []
    start = time.time()
    for scramble in scrambles:
        local_start = time.time()
        k = f(scramble)
        locals.append(time.time() - local_start)
    total_time = time.time() - start
    avg_time = sum(locals) / len(locals)
    print ('total time taken for %d scrambles: %f' % (len(scrambles), total_time))
    print ('average time taken per scramble: %f\n' % (avg_time))

def generate_scrambles(num, scramble_length):
    # Generate num scrambles of length scramble_length
    st = 'abcdefghijklmnopqrstuvwxyz'
    scrambles = []
    while len(scrambles) < num:
        a = ''
        while (len(a) < scramble_length):
            a += st[random.randint(0, len(st)-1)]
        scrambles.append(a)
    return scrambles

def run_tests():
    scram = generate_scrambles(1000, 9)
    print "longest_word:\n"
    time_function(longest_word, scram)
    print "longest_word_new:\n"
    time_function(longest_word_new, scram)

f = open("NewDict.dat","rb")
Dict = pickle.load(f)
new_dict = process_dict(Dict)
rev_dict = reverse_dict(Dict)
def main():
    run_tests()

    # while True:
    #     s = raw_input("Enter Scramble:")
    #     print longest_word(s)
    #     print longest_word_new(s)

if __name__ == '__main__':
    main()
