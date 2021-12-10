#Abai Rakhym
#Ариф.  1
#import math
#y = int(input('y = '))
#n = 3 * (math.pow((y),2)) + math.sqrt(y + 1)
#print(n)

# Ариф. 2
#import math
#y = int(input('y = '))
#n = int(input('n = '))
#h =  (math.pow(y,2)) - (0.8 * y) + math.sqrt(y)/ (23.1 * math.pow(n,2)) + math.cos(n)
#print(h)

#Ариф. 3
#import math
#x = int(input('x = '))
#b = int(input('b = '))
#a = int(input('a = '))
#y = int(input('y = '))
#t = (math.sqrt(x + b - a)) + (math.log(y)) / math.atan(b + a)
#print(t)

# 2.2. Условные операторы
# 1 :
#x = int(input('x  = '))
#y = int(input('y  = '))
#if (x > 0  and y < 0 ):
#    print("Да 4 - той ")
#else:print("Нет")

#2
#import math
#bx = int(input("B(x) koop."))
#by = int(input("B(y) koop."))
#x = int(input("x = "))
#if x > 1:
#    c = math.pow(math.sin(math.pow(x,3)),2)
#    print("Лежит")
#elif x <= 1:
#    c2 = math.sqrt(6 * math.asin(x ** 7) + 4.5 * (x ** 6) + 4 * (x ** 2) + 2)
#    print("Лежит")
#else:print("Не лежит")

#3
#n=int(input('Введите число n '))
#m=n
#a=m%10
#m=m//10
#b=m%10
#m=m//10
#c=m%10
#d=m%10
#p=a*b*c*d
#print(p)
#if  p < 999 and p > 100:
#    print(" НЕ Кратко")
#else:print("Кратко")
#a = int(input("a = "))
#if p < a:
#    print("Да")
#else:print("Нет")

#2.3 Оператор выбора вариантов
#1
#print("A1 координат белгиленгиз!")
#x1 = int(input("x1 = "))
#y1 = int(input("y1 = "))
#print("A2 координат белгиленгиз!")
#x2 = int(input("x2 = "))
#y2 = int(input("x2 = "))
#print("A3 координат белгиленгиз!")
#x3 = int(input("x3 = "))
#y3 = int(input("y3 = "))
#if  x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0  and x3 > 0 and y3 > 0:
#    print("Да!")
#else:print("Нет!")

#2 //17
#import  math
#a = float(input("a = "))
#b = float(input("b = "))
#x = float(input("x = "))
#z = math.log1p(math.tan(b * x))
#if x <= a:
#     a1 = a + math.sin(b*x) + math.cos(x**2)
#     print(a1)
#elif a < x < math.log(b):
#     a2 = math.sqrt(a + b * x) + math.sin(z*x)
#     print(a2)
#elif x >= math.log(b):
#     a3 = math.log(a + b * x + z)
#     print(a3)

#3
#import random      #рандом библиотекасын импорттаймыз
#c = ('''1)«6», «7», «8»
#2)«7», «8», «9»
#3)«6», «9», «10»
#4)«6», «9», «8»
#5)«7», «6», «10»''')              #нҰсҚаларды жазамыз
#print(c)                          #экранҒа шыҒарамыз
#print("Vash variant:")
#a = int(input())                  #өз нҰсҚамызды енгіземіз
#k = a
#if k == 1:                        #шарт Қоямыз
#    k = 6 + 7 + 8                 #нҰсҚанын барлыҚ санын Қосамыз
#print("У тебя:", 21)
#if k == 2:                        #шарт Қоямыз
#    k = 7 + 8 + 9                 #нҰсҚанын барлыҚ санын Қосамыз
#print("У тебя:", 24)
#if k == 3:                        #шарт Қоямыз
#    k = 6 + 9 + 10                #нҰсҚанын барлыҚ санын Қосамыз
#print("У тебя:", 25)
#if k == 4:                        #шарт Қоямыз
#    k = 6 + 9 + 8                 #нҰсҚанын барлыҚ санын Қосамыз
#print("У тебя:", 23)
#if k == 5:                        #шарт Қоямыз
#    k = 7 + 6 + 10                #нҰсҚанын барлыҚ санын Қосамыз
#print("У тебя:", 23)
#a1 = random.randint(6, 10)
#b1 = random.randint(6, 10)  #a1 b1 c1 ге рандом рандит арҚылы кездейсоҚ сандарды аламыз
#c1 = random.randint(6, 10)
#PC = a1 + b1 + c1          #шыҚҚан үшсанды Қосамыз
#print("PC:", PC)
#if k > PC:              #шарт Қоямыз егер Сенде сандар қосындысы көп болса сен Ұттын
#    print("Ты победил!")
#elif k == PC:           #тең болса қайттан көрініз деп шығады
#    print("Вышло ничья, попробуй еще раз!")
#else:                   #олай болмаған жағдайда біз ұтылдық
#    print("Ты проиграл!")

# 3.1 Оператор цикла с параметром
#1
#import math #ИМПОРТАЙМЫЗ MATH
#x = int(input("x = "))
#i = int(input("i = "))
#a = int(input("a = "))
#n = int(input("n >= 2 =  "))
#b = int(input("b = "))
#for i in range(0,n): #цикл 0 ден n ге дейин
#    x = a + (b - a) / (n - 1) * (i - 1)
#    print(math.sin(x))

#2
#k = int(input("k = "))
#i = -3
#n = i
#Q1 = 1.0
#while i <= k:
#    i += 1
#    if i == 5:
#        continue
#    sum = ((-1) ** (i)) / ((i - 5) ** 2)
#    Q1 += sum
#    i += 1
#print('sum',sum)
#Q2 = 1.0
#while n <= k:
#    n += 1
#    if (n ** 3) == 8:
#        continue
#    if n == 4:
#        continue
#    mult = (( n ** 3) - 8) / (n + 4)
#    Q2 *= mult
#print('mult',Q2)

# 3.2  Операторы цикла с предусловием и постусловием
#1
#n = int(input("n = "))
#for i in  range(n,1,-1):
#    if (n % i == 0):
#        print(i)

#2
#n = int(input("Сколько учеников? -"))
#k = 0
#for i in range(n):
#        print("Введите рост ",i+1,"ученика")
#        ros = float(input())
#        rost = k + ros
#print("Cредный рост",rost / i)

#3
#print("Стипендия?")
#stipendia = int(input())
#print("Pасходы на проживание?")
#rasxodi = int(input())
#h = []
#for i in range(1,10):
#    print(rasxodi)
#    g = float(format(rasxodi / 100 * 3))
#    rasxodi += g
#print(rasxodi,"Расходи на 10 месяц")

#4.1. Одномерные массивы
#1
#massiv = [1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
#dlina = len(massiv)
#plus = 1
#otrizatel = 0
#nulll = 0
#for i in range(dlina):
#    if massiv[i] > 0:
#        plus *=  massiv[i]
#    elif massiv[i] <0:
#        otrizatel += 1
#    elif massiv[i] == 0:
#        nulll += 1
#print("+ = " ,plus ,"|- = " ,otrizatel , "|0 = " ,nulll)

#2
#import random
#local = 0
#m = {}
#for i in range(8):
#    for j in range(8):
#        m[i, j] = random.choice(range(1, 3))
#print("Массив 1")
#for i in range(8):
#    print(*[m[i, j] for j in range(8)])
#for i in range(8):
#    for j in range(8):
#        if j == 0 or j == 7:
#            pass
#        else:
#             #print(m[i, j])  коментарий
#            if (m[i, j] > m[i, j - 1]) and (m[i, j] > m[i, j + 1]):#
#                local += 1
#print(local)

#3
#test = list(range(0, 5))  # список
#print(test)
#for i in range(5):
#    o = len(test) - 1  # сколько элементов в списке test
#    p = test[o]  # последний элемент
#    test.remove(p)  # удалить последний элемент
#    test2 = test.insert(0, p)  # поставить последний элемент на первую позицию
#    print(test)

#4.2. Двухмерные массивы
# 1
#massiv10 = [[1,2,3,4,5,6,7,8,9,10],
#            [1,2,3,4,5,6,7,8,9,10],
#            [1,2,3,4,5,6,7,8,9,10],
#            [1,2,3,4,5,6,7,8,9,10],
#            [1,2,3,4,5,6,7,8,9,10],
#            [1,2,3,4,5,6,7,8,9,10],
#            [1,2,3,4,5,6,7,8,9,10],
#            [1,2,3,4,5,6,7,8,9,10],
#            [1,2,3,4,5,6,7,8,9,10],
#            [1,2,3,4,5,6,7,8,9,10]]
#dlina = len(massiv10)
#for i in range(dlina):
#    mi =  sum(massiv10[i])
#    print(mi)

#2
#arr =     [[1,2,3,4,5]
#          ,[1,2,3,4,5]
#          ,[1,2,3,4,5]
#          ,[1,2,3,4,5]
#          ,[1,2,3,4,5]]
#max_item = max([abs(item) for row in arr for item in row])
#for i in range(len(arr)):
#  for j in range(len(arr[0])):
#    arr[i][j]/=max_item
#print(arr)

#3
#n, m = map(int, input().split())
#pascal = [[1] * n for i in range(m)]
#for i in range(1, m):
#    for j in range(1, n):
#        pascal[i][j] = pascal[i - 1][j] + pascal[i][j - 1]
#for i in range(len(pascal)):
#    print(*pascal[i])

#5.1. Функции
#1
#import math
#def hexagon(x1 ,y1 ,x2 ,y2 ,x3 ,y3 ,x4 ,y4 ,x5 ,y5 ,x6 ,y6):
#    a = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
#    b = math.sqrt(((x2 - x3) ** 2) + ((y2 - y3) ** 2))
#    c = math.sqrt(((x1 - x3) ** 2) + ((y1 - y3) ** 2))
#    p = (a + b + c ) / 2
#    s = math.sqrt(p*(p - a)*(p - b)*(p - c))
#    hexa = s + s + s + s + s + s
#    print(hexa)
#hexagon(56,26,35,4,56,64,7,83,92,10,11,12 )


#2 numpy men bul
#import numpy as np
#def create_upper_matrix(values, size):
#    upper = np.zeros((size, size))
#    upper[np.triu_indices(3, 0)] = values
#    return(upper)
#c = create_upper_matrix([1, 2, 3, 4, 5, 6], 3)
#print(c)


#3
#def func(n):
#    print(int(n, base=2))
#if __name__ == '__main__':
#    n=input()
#    func(n)

# 2 второй вариант если 1 не верный
#n = int(input())
#res = int(input())
#while n != 0:
#    res = int(n % 2) + res
#    n = n % 2 == 0
#print(res)

#7.1. Символьный тип данных
#1 норм повторим
#simvol = ["*","*","*","*","$","#","#"]
#xewtek = simvol.count("*")
#zvz = simvol.count("#")
#print(xewtek ,"До '$' " )
#print(zvz , " После '$' ")

#2
#massiv1 = ['Ra','Ab','Hg','Bi','Ci','Di','Fi','Li']
#massiv2 = ['А','Б','А','Й','Р','Х','Ы','М']
#massiv3 = ['Ra','Ab','Hg','Bi','Ci','Di','Fi','Li']
#massiv4 = ['Ra','Ab','Hg','Bi','Ci','Di','Fi','Li']
#massiv5 = ['Ra','Ab','Hg','Bi','Ci','Di','Fi','Li']
#ff = sorted(massiv1)
#ff2 = sorted(massiv2)
#print(ff)
#print(ff2)

#3
#sozbmas = 'RA WORLD is best'
#count_lower = 0
#count_upper = 0
#i = 0
#while i < len(sozbmas):
#    if sozbmas[i].islower(): count_lower += 1
#    if sozbmas[i].isupper(): count_upper += 1
#    i +=1
#if count_upper > count_lower:
#    basa = sozbmas.upper()
#    print(basa)
#elif count_lower > count_upper:
#    kiw = sozbmas.lower()
#    print(kiw)
#else:print(sozbmas)

#7.2. Строковый тип данных
#1
#soz25 = str(input("Soz?"))
#print(soz25 + "_")

#2
#sanaik = "№ ксгоу №"
#iamra = sanaik.replace('№','номер один')
#print(iamra)

#3
#ia = "я Рахым Абай"
#iaa = ia.replace('я'," ")
#print(iaa)

#8.1. Текстовые файлы
#1
#zdaanie = open(r"C:\Users\Abair\Desktop\Rakhym\zdanie.txt", 'r')
#for i in zdaanie:
#    print(i)
#zdaanie.close()

#2
#f = open(r"C:\Users\Abair\Desktop\Rakhym\f2.17.txt")
#g = open(r"C:\Users\Abair\Desktop\Rakhym\g2.17.txt","w")
#f_file = f.read()
#f.close()
#f_file = f_file.split()
#mas_f = []
#for i in f_file:
#    if int(i) % 3 == 0  and not int(i) % 7 == 0:
#        mas_f.append(i)
#g.write(str(mas_f))
#g.close()

#3
#n = 2
#k = open(r"C:\Users\Abair\Desktop\Rakhym\pervi.txt")
#vecto = open(r"C:\Users\Abair\Desktop\Rakhym\vektor.txt")
#udalit_dobavit = open(r"C:\Users\Abair\Desktop\Rakhym\udadob.txt",'w+')
#kmatrix = k.read()
#kmatrix = kmatrix.replace('\n','').split()
#vector = vecto.read()
#vect0r = int(kmatrix[1]) * int(kmatrix[5]) - int(kmatrix[2]) * int(kmatrix[4]) #векторлар
#vect1r = - int(kmatrix[0]) * int(kmatrix[5]) - int(kmatrix[2]) * int(kmatrix[3])
#vect2r = + int(kmatrix[0]) * int(kmatrix[4]) - int(kmatrix[1]) * int(kmatrix[3])
#print(vect0r,vect1r,vect2r)
#skal9r = (int(kmatrix[0]) * int(kmatrix[3])) + (int(kmatrix[1]) * int(kmatrix[4])) + (int(kmatrix[2]) * int(kmatrix[5]))
#print(skal9r)
#udalit_dobavit.write('12345')
#udalit_dobavit.seek(1)
#for uddob in udalit_dobavit:
#    print(uddob)
#udalit_dobavit.close()
#k.close()
#vecto.close()
