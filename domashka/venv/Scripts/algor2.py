
#9
#m=0
#n=1
#while n<15:
#   m=m+n
#   n=n+1
#print("Сумма ",7*m)

#10
#a = int(input("a = "))
#b = int(input("b = "))
#print((a + b) / 2 + abs(a - b) / 2)

#11
#from random import randint
#n = randint(10,9999)
#print(n)
#if n<100:
#    print(int(n/10))
#elif 100<n<1000:
#    print(int((float(int(n/10)*0.1%1)*10)))
#elif n>1000:
#    print(int((float(int(n / 10) * 0.1 % 1) * 10)))
#else:print("0")

#12
#m = int(input("m = "))
#n = int(input("n = "))
#pr = 1
#for i in range(m, n+1):
#    pr *= i**3
#print(pr)

#13
#can = list(range(100,1000+1))
#do = 0
#for i in can:
#    if(i % 9 ==0) and (i %5!=0):
#            do += i
#print(can)
#print(do)

#14
#lisst = [1,2,3,4,5,6,7,8,9,10,11]
#a = sum(lisst) /11
#p = 1
#for i in range(10):
#    if  lisst[p] > a:
#        print(lisst[p])
#    p +=1

#15
#lii = [1,2,3,4,4,4,5,6,7,8,9,11,10]
#max_ = max(lii)
#lii[12] = max_
#max_ = lii[12]
#print(lii)

#16
#a = 15
#import  random
#lik = random.sample(range(1000), 15)
#max_ = max(lik)
#min_ = min(lik)
#mm = max_ + min_
#print (max_,"+" , min_,"=" , mm)

#17 bitry kerek
#import random
#lik = random.sample(range(10), 15)
#lik1 = random.sample(range(10), 15)
#sum_1 = sum(lik) / 15
#sum_2 = sum(lik1) / 15
#i = 1
#while i > 0:
#    i += 1
#    if(sum_1 == sum_2):
#        print(sum_1,sum_2)
#        break

#18
#likl = random.sample(range(10), 17)
#sum_s = sum(lik1)

#19
#import  random
#lij = random.sample(range(100), 15)
#ma = max(lij)
#mi = min(lij)
#l = []
#print(lij)
#print(ma,mi)
#for i in range(0,15):
#    if ma > lij[i] and mi < lij[i]:
#        l.append(lij)
#a = len(l)
#print(a)
#3


# функция 2 второй вариант если 1 не верный
#n = int(input())
#res = int(input())
#while n != 0:
#    res = int(n % 2) + res
#    n = n % 2 == 0
#print(res)




#22
f = open(r"C:\Users\Abair\Desktop\Rakhym\f2.17.txt")
g = open(r"C:\Users\Abair\Desktop\Rakhym\g2.17.txt","w")
f_file = f.read()
f.close()
f_file = f_file.split()
mas_f = []
for i in f_file:
    if int(i) % 3 == 0  and not int(i) % 7 == 0:
        mas_f.append(i)
g.write(str(mas_f))
g.close()







































