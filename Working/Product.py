import pickle
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

def bsearch(val,L):
    u = len(L)-1
    l = 0
    while l<=u:
        mid = (u+l)//2
        if L[mid]==val:
            return mid
        elif val > L[mid]:
            l = mid+1
        elif val < L[mid]:
            u = mid-1
    return False

Primes = twentysix_primes()
f = open("Lists.dat","rb")
Words = pickle.load(f)
Values = pickle.load(f)
while True:
    s = raw_input('Enter word:')
    s+= ' '
    val = prime_value(s,Primes)
    ind = bsearch(val,Values)
    if ind:
        if Words[ind].strip() == s.strip():
            f = 0
            ind +=1
            if Values[ind] == val:
                print Words[ind].strip()
                f = 1
            ind -=2
            if Values[ind] == val:
                print Words[ind].strip()
                f = 1
            if f==0:
                print "No anagrams found"
        else:
            print Words[ind].strip()
