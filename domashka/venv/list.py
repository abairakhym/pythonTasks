#Алдиар есептери
#1.1. Арифметические выражения
import math
#1
# 1.1 (8)

# import math
# y = int(input("y="))
# T = math.sqrt(math.fabs(6*math.pow(y,2))-0.1*y+4)
# print("answer=", T)
#
# # 1.1 (2.8)
import math
# t = int(input("t="))
# y = int(input("y="))
# T = 2.37*math.sin(t+1)/math.sqrt(4*math.pow(y,2)-0.1*y+5)
# print("answer=",T)
#
# # 1.1(3.8)
import math
# a = int(input("a="))
# y = int(input("y="))
# c = int(input("c="))
# x = int(input("x="))
# P = math.pow(a,5) + math.pow(math.sin(y-c),4)*/math.pow(math.sin(x+y),3) + math.fabs(x-y)
# print("value=",P)


# 2.2(1.8)Ввести с клавиатуры значения сторон двух треугольников a1,b1,c1 и
# a2,b2,c2. Определить, площадь какого треугольника – наибольшая. Ответ
# вывести в виде сообщения
#1
# import math
# a1 = int(input("a1="))
# b1 = int(input("b1="))
# c1 = int(input("c1="))
# a2 = int(input("a2="))
# b2 = int(input("b2="))
# c2 = int(input("c2="))
# p = (a1+b1+c1)/2
# S1 = math.sqrt(p*(p-a1)(p-b1)(p-c1))
# p = (a2+b2+c2)/2
# S2 = math.sqrt(p*(p-a2)(p-b2)(p-c2))
# if S1 > S2:
#     print("S1 is bigger than S2=",S1)
# elif S2 > S1:
#     print("S2 bigger than S1=", S2)
# else:
#     print("Values are equal=",S1)

#2
#a = int(input("a = "))
#b = int(input("b = "))
#proiz =  int(input("Напишите произведения двух чисел а * b = "))
#pro = a * b
#if proiz == pro:
#    print("правильно")
#else:print("не правильно ответ =" , pro)

#3
#import math
#alfa=int(input('alfa='))
#v0=int(input('v0='))
#t=int(input('t='))
#h=int(input('h='))
#H=int(input('H='))
#R=int(input('R='))
#x = v0*t*math.cos(alfa)
#y = v0*t*math.sin(alfa)-98*(t**2)/2
#if x==R and H<y<h:
#    print('попадает')
#else:
#    print('не попадает')

#2.3. Оператор выбора вариантов
#1
#a=int(input('a='))
#b=int(input('b='))
#c=int(input('c='))
#if a==b!=c or a==c!=b or c==b!=a:
#    print('равнобедренный')
#else:
#    print('не равнобедренный')
#2
#import math
#x=int(input('x='))
#k=int(input('k='))
#m=int(input('m='))
#n=int(input('n='))
#if x**2>m+n:
#    y=math.log(math.fabs(m*x+n))
#    print(y)
#if x**2==m+n:
#    y=math.pow(math.e , math.cos(math.fabs(m*x-n)))
#    print(y)
#if x**2<m+n:
#    y=(k*2+(math.cos(x)2))*(1/3)
#    print(y)
#3
#import math
#film=str(input('выберите фильм: '))
#if film=='Хроники Нарнии':
#    print('12:00\n16:00\n20:00')
#    time=int(input('выберите время: '))
#    if time==12:
#        s=25
#        print('1 бил.=25гр\n+5 бил.=-5%\n+10 бил.=-10%')
#        tic = int(input('количество билетов: '))
#        if tic<6:
#            print('цена:',tic*s,'гр')
#        elif 5<tic<11:
#            s=s-(s*5/100)
#            print('цена:',tic*s,'гр')
#        else:
#            s=s-(s*10/100)
#            print('цена:',tic*s,'гр')
#    if time==16:
#        s = 35
#        print('1 бил.=35гр\n+5 бил.=-5%\n+10 бил.=-10%')
#        tic = int(input('количество билетов: '))
#        if tic < 6:
#            print('цена:', tic * s, 'гр')
#        elif 5 < tic < 11:
#            s = s - (s*5/100)
#            print('цена:', tic * s, 'гр')
#        else:
#            s = s - (s*10/100)
#            print('цена:', tic * s, 'гр')
#    if time==20:
#        s = 45
#        print('1 бил.=45гр\n+5 бил.=-5%\n+10 бил.=-10%')
#        tic = int(input('количество билетов: '))
#        if tic < 6:
#            print('цена:', tic * s, 'гр')
#        elif 5 < tic < 11:
#            s = s - (s*5/100)
#            print('цена:', tic * s, 'гр')
#        else:
#            s = s - (s*10/100)
#            print('цена:', tic * s, 'гр')
#if film=='Чужие':
#    print('10:00\n13:00\n16:00')
#    time = int(input('выберите время: '))
#    if time==10:
#        s=25
#        print('1 бил.=25гр\n+5 бил.=-5%\n+10 бил.=-10%')
#        tic = int(input('количество билетов: '))
#        if tic<6:
#            print('цена:',tic*s,'гр')
#        elif 5<tic<11:
#            s=s-(s*5/100)
#            print('цена:',tic*s,'гр')
#        else:
#            s=s-(s*10/100)
#            print('цена:',tic*s,'гр')
#    if time==13:
#        s = 35
#        print('1 бил.=35гр\n+5 бил.=-5%\n+10 бил.=-10%')
#        tic = int(input('количество билетов: '))
#        if tic < 6:
#            print('цена:', tic * s, 'гр')
#        elif 5 < tic < 11:
#            s = s - (s*5/100)
#            print('цена:', tic * s, 'гр')
#        else:
#            s = s - (s*10/100)
#            print('цена:', tic * s, 'гр')
#    if time==16:
#        s = 35
#        print('1 бил.=35гр\n+5 бил.=-5%\n+10 бил.=-10%')
#        tic = int(input('количество билетов: '))
#        if tic < 6:
#            print('цена:', tic * s, 'гр')
#        elif 5 < tic < 11:
#            s = s - (s*5/100)
#            print('цена:', tic * s, 'гр')
#        else:
#            s = s - (s*10/100)
#            print('цена:', tic * s, 'гр')
#if film=='Аватар':
#    print('10:00\n14:00\n18:00')
#    time = int(input('выберите время: '))
#    if time==10:
#        s=35
#        print('1 бил.=35гр\n+5 бил.=-5%\n+10 бил.=-10%')
#        tic = int(input('количество билетов: '))
#        if tic<6:
#            print('цена:',tic*s,'гр')
#        elif 5<tic<11:
#            s=s-(s*5/100)
#            print('цена:',tic*s,'гр')
#        else:
#            s=s-(s*10/100)
#            print('цена:',tic*s,'гр')
#    if time==14:
#        s = 45
#        print('1 бил.=45гр\n+5 бил.=-5%\n+10 бил.=-10%')
#        tic = int(input('количество билетов: '))
#        if tic < 6:
#            print('цена:', tic * s, 'гр')
#        elif 5 < tic < 11:
#            s = s - (s*5/100)
#            print('цена:', tic * s, 'гр')
#        else:
#            s = s - (s*10/100)
#            print('цена:', tic * s, 'гр')
#    if time==18:
#        s = 45
#        print('1 бил.=45гр\n+5 бил.=-5%\n+10 бил.=-10%')
#        tic = int(input('количество билетов: '))
#        if tic < 6:
#            print('цена:', tic * s, 'гр')
#        elif 5 < tic < 11:
#            s = s - (s*5/100)
#            print('цена:', tic * s, 'гр')
#        else:
#            s = s - (s*10/100)
#            print('цена:', tic * s, 'гр')
#else:
#    print('введите правильное название фильма!')

#3.1. Оператор цикла с параметром
#1
#print(sum(1.0/i for i in range(1, int(input())+1)))
#2
#import cmath
#import math
#k = int(input("k = "))
#j = -1
#i = j
#Q2 = 1.0
#while j <= k:
#    j += 1
#    if j == (j**2):
#        continue
#    if j == 4:
#        continue
#    mult = ((j - (j**2)) * k) / (j - 4)
#    Q2 *= mult
#print('mult', Q2)
#Q1 = 0.0
#while i <= k:
#    i += 1
#    if math.sqrt(math.log1p(i == 5)):
#        continue
#    if math.log1p(i == 7):
#        continue
#    sum = cmath.sqrt(cmath.log(i - 5)) / cmath.log(i - 7)
#    Q1 += sum
#    i += 1
#print('sum',sum)

#3.2. Операторы цикла с предусловием и постусловием
#1
#chislo = int(input("Число? = "))
#for i in range(chislo+1):
#    a = i
#    b = i+1
#    d =+ 1
    #print(a,b)
#    if a * b == chislo:
#        print(a ,"*", b ,"=", chislo )
#        break

#2
#a, b = 7, 5
#i = min(a, b)
#while True:
#    if i%a==0 and i%b==0:
#        break
#    i += 1
#print(i)

#3 
#k = True
#S = 1
#while k:
#    a = int(input(" a = "))
#    if a <= 0 : break
#    S= S * a
#    print(S)

#3.3. Вычисление бесконечных сумм
#1 xz dyrisin
#x = int(input("x = "))
#for i in range(x+1):
#  s = (x ** i) * math.sin(math.pi / 4) + (x ** i) * math.sin(math.pi / 4) + (x ** i) * math.sin(math.pi / 4)
#print(s)


#4.1. Одномерные массивы
#1
#massiv16 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#max_ = max(massiv16)
#min_ = min(massiv16)
#for i in massiv16:
#    if i == max_:
#        print("индекс max =",i-1)
#    if i == min_:
#        print("индекс min =",i-1)
#print(massiv16)

#2
#R = [1,2,3,4,5,6,7,8,9]
#dlinaR = len(R)
#max_ = max(R)
#for i in range(dlinaR):
#    if (R[i] % 2 == 1):
#        if R[i] == max_:
#           print(i," индекс наибольшего из нечетных")
#           break

#3
#massiv9 = [10011,101,1001,1101,101010,1011,10100,10101,10]
#dlinamas = len(massiv9)
#def binaryToDecimal(n):
#    return int(str(n),2)
#for i in range(dlinamas):
#    if __name__ == '__main__':
#        print(binaryToDecimal(massiv9[i]))

#4.2. Двухмерные массивы
#1
#n = 2
#a = [[1,2],[3,4]]
#min_ = min(a[0])
#_min = min(a[1])
#proiz = min_ * _min
#print(min_,"*",_min,"=",proiz)

#2
#def zm(n):
#    dx, dy = 1, 0
#    x, y = 0, 0
#    arr = [[None] * n for _ in range(n)]
#    for i in range(1, n**2+1):
#        arr[x][y] = i
#        nx, ny = x+dx, y+dy
#        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
#            x, y = nx, ny
#        else:
#            dx, dy = -dy, dx
#            x, y = x+dx, y+dy
#    for x in list(zip(*arr)):
#        print(*x)
#zm(int(input()))

#3
#a = [[1,2,3],
#     [4,5,6],
#     [7,8,9]]
#sum1 = sum(a[0])
#sum2 = sum(a[1])
#sum3 = sum(a[2])
#j = 0
#c = 0
#if sum3 > sum1 < sum2:
#    print("sum1  минимальна",sum1)
#    new_list = []
#    for row in a:
#        new_row = []
#        for v in row:
#            new_row.append(v * sum1)
#        new_list.append(new_row)
#    print(new_list)
#elif sum3 > sum2 < sum1:
#    print("sum2  минимальна",sum2)
#    new_list = []
#    for row in a:
#        new_row = []
#        for v in row:
#            new_row.append(v * sum2)
#        new_list.append(new_row)
#    print(new_list)
#elif sum1 > sum3 < sum2:
#    new_list = []
#    for row in a:
#        new_row = []
#        for v in row:
#            new_row.append(v * sum3)
#        new_list.append(new_row)
#    print(new_list)
#    print("sum3  минимальна",sum3)

#5.1. Функции
#1
#import math
#def abc (a,b,c):
#    amed = int(0.5 * math.sqrt(2*(math.pow(c,2)) + 2*(math.pow(b,2)) - (math.pow(a,2))))
#    bmed = int(0.5 * math.sqrt(2*(math.pow(a,2)) + 2*(math.pow(c,2)) - (math.pow(b,2))))
#    cmed = int(0.5 * math.sqrt(2*(math.pow(a,2)) + 2*(math.pow(b,2)) - (math.pow(c,2))))
#    print("a = ",amed,", b = ",bmed,", c = ",cmed)
#abc(10,20,30)

#2тут не понятное задача


#3
#def sum_digits(num = int(input())):
#    return num%10 + sum_digits(num//10) if num > 9 else num
#print(sum_digits())

#5.2. Библиотеки
#1
#matrix = [[1,2,3,4,5],[6,7,8,9,10],[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
#dlina = len(matrix)
#summ = sum(matrix[0] + matrix[1] + matrix[2] + matrix[3] +matrix[4])
#koop = summ / dlina
#print(koop)

#2
#import math
#e = int(input("e = "))
#i = int(input("i = "))
#j = int(input("j = "))
#nM = [[1,1,1,1,1,1,1],[2,2,2,2,2,2,2],[3,3,3,3,3,3,3],[4,4,4,4,4,4,4],[5,5,5,5,5,5,5],[6,6,6,6,6,6,6]]
#a = (math.pow(math.pow(math.log(i+j),4),4)-(e**e))
#print(a)
#nm0 = sum(nM[0]) / len(nM[0])
#nm1 = sum(nM[1]) / len(nM[1])
#nm2 = sum(nM[2]) / len(nM[2])
#nm3 = sum(nM[3]) / len(nM[3])
#nm4 = sum(nM[4]) / len(nM[4])
#nm5 = sum(nM[5]) / len(nM[5])
#print(nm0,nm1,nm2,nm3,nm4,nm5)
#summa = nm0 + nm1 + nm2 + nm3 + nm4 + nm5
#print(summa)

#6.1. Динамические массивы
#1
#n = 5
#nn = [1,2,6,4,9,3,6,9,12]
#su = []
#d = len(nn)
#for i in range(d):
#    if nn[i] % 3 == 0:
#        su.append(nn[i])
#        #print(su) прикин бурыш шыгат нан койсан
#summm = sum(su)
#print(summm)

#2 + #3 вместе
#mas9 = [1,2,3,4,5,6,7,8,9]
#mas10 = []
#mas10.append(mas9)
#summ = sum(mas9)
#dl = len(mas9)
#sreee = summ / dl
#print(sreee)

#6.2. Динамические структуры: стеки и очереди
#1
#svedenie = []
#mon = int(input("цена "))
#svedenie.append(mon)
#mo = int,str(input("сведения "))
#svedenie.append(mo)
#print(svedenie)
#svedenie.pop(0)
#print(svedenie)

#2
#stec = []
#stec.append("«sdf")
#stec.append(2)
#stec.append("ssd4")
#stec.append("«hello")
#print(stec)
#stec.pop(0)
#stec.pop(1)
#print(stec)

#3 кор уйрен
#import random
#from collections import deque
#N = random.randrange(1,10)
#q = deque([random.randrange(1,11) for i in range(0,N)])
#print("Queue: ", q)
#while len(q) > 0 and q[0]%2 == 1:
#    q.popleft()
#print()
#print("Queue: ", q)
#try:
#    print("id of the first item: ",id(q[0]))
#except IndexError as err:
#    print("NIL: {0}".format(err))
#try:
#    print("id of the last item: ",id(q[-1]))
#except IndexError as err:
#    print("NIL: {0}".format(err))

#6.3.Динамические структуры: списки

#1
#numbers = [1, 22, 3, 4, 5]
#numbers[0] = 0.99
#print(numbers)

#2
#num = [1,-2,3,-4,5,6]
#for i in range(len(num)):
#    print(i)
#    if num[i] < 0:
#       num[i + 1] = 66
#print(num)

#3
#class Node:
#    def __init__(self, data=None):
#        self.data = data
#        self.prev = self.next = None
#def append(lst, data):
#    while lst.next:
#        lst = lst.next
#    lst.next = Node(data)
#    lst.next.prev = lst
#def print_list(lst):
#    while lst:
#        print(lst.data, end=(' ', '\n')[lst.next == None])
#        lst = lst.next
#def func(lst):
#    curr = lst
#    while curr:
#        if curr.data % 2 != 0:
#            n = Node(curr.data)
#            n.next = curr
#            n.prev = curr.prev
#            if curr == lst:
#                lst = n
#            else:
#                curr.prev.next = n
#        curr = curr.next
#    return lst
#if __name__ == '__main__':
#    head = Node(-2)
#    [append(head, i) for i in range(1, 6)]
#    [append(head, i) for i in range(2, 7)]
#    [append(head, i) for i in (3, 3, 3, 7, 5, 3, 3)]
#    print_list(head)
#    head = func(head)
#    print_list(head)
#    print(head)

#7.1. Символьный тип данных
#1
#masiv = [1,2,3,4,":"]
#for i in range(len(masiv)):
#    if masiv[i] == ":":
#        print(i)

#2
#masiv = ["*","$","#","*"]
#for i in range(3):
#    if masiv[i] == "*":
#        masiv.pop(i)
#print(masiv)

#3
#mas1 = ["аба","лол"]
#mas2 = ["баа","пир"]
#smas1 = sorted(mas1)
#smas2 = sorted(mas2)
#for i in range(2):
#    if smas1[0] == smas2[i]:
#        print("Да  они анаграмни")
#    if smas2[1] == smas2[i]:
#        print("Да  они анаграмни")

#7.2. Строковый тип данных
#1
#stroka = [" ","lol"]
#stroka = [item.replace(" ","«»") for item in stroka]
#print(stroka)

#2
#s= input()
#a= ""
#b= ""
#for i in range (0, len(s), 2):
#   a += s[i]
#for i in range (1, len(s), 2):
#   b += s[i]
#print(a ,b)

#3
#reverseds = "hey"
#stroka = reverseds[::-1]
#print(stroka)

#7.3. Структуры
#1
#max_price = -1
#prodannieIvanom = 0
#samidorogoitovar = ''
#tovar = ["Смартфон","Компьютер"]
#prodov = "Иванов"
#for i in tovar:
#   if prodov == "Иванов":
#      print("Смартфон")
#      prodannieIvanom =+ 1
#      chena = int(input("цена"))
#      if chena > max_price:
#         max_price = chena
#         samidorogoitovar = "Компьютер"
#         print(samidorogoitovar)

#2
#for i in range(3):
#   famila = [str(input("Famila "))]
#   ima = [str(input("Ima "))]
#   otch = [str(input("Otchet "))]
#   dolzhnost = [str(input("Dolzhnost "))]
#   zarplata = [int(input("Zarplata "))]
#   denrojdenie = [float,int(input("Den rozhdenie "))]
#molodoi = min(denrojdenie)
#print(molodoi)

#3
#for i in range(10):
#    name = [str(input("name = "))]
#    zod  = [str(input("zodiak = "))]
#    date = [int, float(input("den rojdenie = "))]
#    needd = name, zod, date
#    zodii = input("zodiak vibori")
#    if zodii == zod[i]:
#       print(name[i])
#    if zodii != zod[i]:
#       print("Нет такого")

#8.1. Текстовые файлы
#1
###################################3#for i in range(2):
#print("Ввод чисел через пробел)
#    familyimaotchestva = [str(l) for l in input("Famila Ima Otchetvo").split()]
#    adres = [int,str((e) for e in input("Adres").split())]
#    natcia = [str((elu) for elu in input("Natcia").split())]
#    datarojdenie = [int,str((uel) for uel in input("data rojdenie").split())]
#    obrozovanieuniver = [str((hel) for hel in input("obrozavanie").split())]
#    godpostuplenienaJOB = [int(el) for el in input("god postuplenie na raboty").split()]
#for i in range(2):
#    if 2015 == godpostuplenienaJOB[i]:
#        print(familyimaotchestva[i])
#        print(adres[i])
#        print(natcia[i])
#        print(datarojdenie[i])
#        print(obrozovanieuniver[i])

#2 Kor yiren
#f = open("f.txt")
#x=f.read()
#f.close()
#x=x.split()
#y=0
#g=[]
#for i in x:
#    z=int(i)%2
#    if z==0:
#        g.append(i)
#g_file = open("g.txt", "w")
#g_file.write(str(g))
#g_file.close()

#3
#_1fail = open(r"C:\Users\Abair\Desktop\perfail.txt")
#_2fail = open(r"C:\Users\Abair\Desktop\vtofail.txt")
#k = _1fail.read()
#l = _2fail.read()
#k = k.replace('\n',' ').split()
#l = l.replace('\n',' ').split()
#dlina_k = len(k)
#dlina_l = len(l)
#k_l = dlina_k - dlina_l
#l_k = dlina_l - dlina_k
#for i in range(2):
#  if dlina_k == dlina_l:
#     print(dlina_l,dlina_k)
#  elif dlina_k > dlina_l:
#       dlina_l =+ k_l
#  elif dlina_l > dlina_k:
#      dlina_k =+ l_k
#_1fail.close()
#_2fail.close()

#8.2. Бинарные файлы
#1
#import pickle
#print("Ввод чисел через пробел только 3 компа")
#namecom = [str((l)  for l in input("firma компьютера ").split())]
#prozesor = [tuple(str((g) for g in input("Частота процессора ").split()))]
#obemoper = [tuple(str((h) for h in input("Объем оперативной памяти ").split()))]
#obemzhdisk = [tuple(str((j) for j in input("Объем жесткого диска ").split()))]
#money = [int(el) for el in input("Цена ").split()]
#allmoney =  sum(money)
#print("Oбщия стоимость предложенных: ",allmoney)
#for i in range(3):
#    if prozesor[i] == "2 ГГц/сек" or "2ГГц/сек" or "2ггц/сек":
#        if namecom[i] == "asus" or "Asus":
#            print(namecom[i])
#            print("частота процессора",prozesor[i])
#            print("объем оперативной памяти;",obemoper[i])
#            print("объем жесткого диска",obemzhdisk[i])
#            print("цена",money[i])
#with open(r"C:\Users\Abair\Desktop\bfail.txt","ab") as asus:
#    pickle.dump(namecom, asus)
#    pickle.dump(prozesor, asus)
#    pickle.dump(obemoper, asus)
#    pickle.dump(obemzhdisk, asus)
#    pickle.dump(money, asus)

#2
#import pickle
#memo = input("?").split()
#stringgrid = input("?").split()
#print(memo,stringgrid)
#memo = [item.replace("*","+") for item in memo]
#memo = [ite.replace("/","+") for ite in memo]
#stringgrid = [it.replace("*","+") for it in stringgrid]
#stringgrid = [i.replace("/","+") for i in stringgrid]
#print(memo,stringgrid)
#with open(r"C:\Users\Abair\Desktop\simfail.txt","ab") as simbol:
#    pickle.dump(memo,simbol)
#    pickle.dump(stringgrid,simbol)

#3
#import pickle
#rang = int(input("ckolko l9dei?"))
#for i in range(rang):
#    famila = [int(input("Фамилия и инициалы клиентов кабельной сети"))]
#    money = [int(input("Стоимость оплаты услуг кабельной сети за месяц"))]
#    mesa = [int(input("Количество месяцев, за которые заплатил клиент"))]
#    selectmesa = [int(input(" Количество месяцев, за которые заплатил клиент вперед"))]
#    if 3 >= selectmesa:
#        ac3sia = money / 10
#        with open(r"C:\Users\Abair\Desktop\simfail.txt") as cabel:
#            pickle.dump(famila,cabel)
#            pickle.dump(ac3sia,cabel)
#            pickle.dump(mesa,cabel)
#            pickle.dump(selectmesa,cabel)

#Тип данных – дата и время
#1.1
#import datetime
#d = datetime.date(2020, 06, 14)
#print(d.year)  # 2020
#print(d.day)  # 14
#print(d.month)  # 06

#1.2












