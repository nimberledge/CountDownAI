import pickle
import random
f = open("Lists.dat","rb")
Words = pickle.load(f)
Values = pickle.load(f)
for i in range(10):
    x = random.randint(int(10**(i/3.0)),int(10**(i/3.0))+10)
    print x, Words[x], Values[x]
