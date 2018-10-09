import random
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

f = open("Dictionary.txt", "r")
s = True
Words = []
Values = []
Dict = {}
Primes = twentysix_primes()
while s:
    s = f.readline()
    s = s.strip()
    Words.append(s)
    v = prime_value(s, Primes)
    Dict[v] = []

for word in Words:
    v = prime_value(word, Primes)
    Dict[v].append(word)


def write_obj_to_file(obj):
    import pickle as p
    f1 = open("NewDict.dat","wb+")
    p.dump(obj,f1)
    f1.flush()
    f1.close()

write_obj_to_file(Dict)
print "Done"

