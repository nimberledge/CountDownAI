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

Primes = twentysix_primes()
f = open("NewDict.dat","rb")
Dict = pickle.load(f)
while True:
    s = raw_input("Enter word:")
    val = prime_value(s,Primes)
    print val
    f = 0
    if val in Dict:
        for i in Dict[val]:
            if i != s:
                print i,
                f = 1
    if f==0:
        print "No anagrams"
    else:
        print
        
