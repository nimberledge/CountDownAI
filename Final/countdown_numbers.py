import time

def reach(target, num_set):
    if len(num_set) < 1:
        return (False, '')
    if target in num_set:
        return (True, 'in set: ' + str(num_set) + '\t\t')
    for num1 in num_set:
        for num2 in num_set:
            if (num1 == num2):
                continue
            temp = list(num_set)
            temp.remove(num1)
            temp.remove(num2)
            k = num1 + num2
            temp.append(k)
            r = reach(target, temp)
            if (r[0]):
                return (True, ('\n' + str(num1) + '+' + str(num2) + ' = ' + str(num1 + num2) + '\nset:' + str(temp) + "\t" +  r[1] + '\t\t'))
            temp.remove(k)
            k = num1 - num2
            temp.append(k)
            r = reach(target, temp)
            if (r[0]):
                return (True, ('\n' + str(num1) + '-' + str(num2) + ' = ' + str(num1 - num2) + '\nset:' + str(temp) + "\t" +  r[1] + '\t\t'))
            temp.remove(k)
            k = num1 * num2
            temp.append(k)
            r = reach(target, temp)
            if (r[0]):
                return (True, ('\n' + str(num1) + '*' + str(num2) + ' = ' + str(num1 * num2) + '\nset:' + str(temp) + "\t" +  r[1] + '\t\t'))
            if (num2 == 0):
                continue
            if (num1 % num2) == 0:
                temp.remove(k)
                k = num1 // num2
                temp.append(k)
                r = reach(target, temp)
                if (r[0]):
                    return (True, (('\n' + str(num1) + '/' + str(num2) + ' = ' + str(num1 // num2) + '\nset:' + str(temp) + "\t" +  r[1] + '\t\t'))
    return (False, '')

def main():
    while True:
        print ("Enter numbers")
        num_set = [int(j) for j in input().split()]
        print (num_set)
        print ("Target:")
        target = int(input())
        start = time.time()
        b = reach(target, num_set)
        t = time.time() - start
        if b[0]:
            print (b[1])
        else:
            print ("na u suck")
        print ("Time taken:", t)

if __name__ == '__main__':
    main()
