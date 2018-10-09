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


def bubblesort(A, A2):
    #SORTED BASED ON FIRST LIST
    for i in range (len(A)-2):
        if i%10000 ==0:
            print str(i//10000) + "/6 of the way there"
        s= 0 #number of swaps
        for j in range (len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                A2[j], A2[j+1] = A2[j+1],A2[j]
                s =1
        if s==0:
            break



f = open("Dictionary.txt", "r")
s = True
Words = []
Values = []
Primes = twentysix_primes()
i = 1
while s:
    s = f.readline()
    s.strip()
    if len(s)>9:
        continue
    Words.append(s)
    Values.append(prime_value(s,Primes))

print len(Words)
print "Sorting..."
bubblesort(Values,Words)   
##import pickle as p
##f1 = open("Lists.dat", "wb+")
##p.dump(Words,f1)
##p.dump(Values,f1)
##f1.flush()
##print "Done"


