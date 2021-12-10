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
a = int(input("a = "))
x = int(input("x = "))
y = int(input("y = "))
if(a / 2):
    print("он " + a)
else:print("он емес" + a)
if(x / 2):
    print("он " + x)
else:print("он емес" + x)
if(y / 2):
    print("он " + y)
else:print("он емес " + y)

















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
#    mi = sum(massiv10[i])
#    print(mi)

#2
#massiv5 = [[1,2,3,4,5]
#          ,[1,2,3,4,5]
#          ,[1,2,3,4,5]
#          ,[1,2,3,4,5]
#          ,[1,2,3,4,5]]
#masi = [[5,5,5,5,5]
#       ,[4,4,4,4,4]
#       ,[3,3,3,3,3]
#       ,[2,2,2,2,2]
#       ,[1,1,1,1,1]]
#for i in range(1):
#    print(massiv5)
#    print(masi)

#3
#n, m = map(int, input().split())
#pascal = [[1] * n for i in range(m)]
#for i in range(1, m):
#    for j in range(1, n):
#        pascal[i][j] = pascal[i - 1][j] + pascal[i][j - 1]
#for i in range(len(pascal)):
#    print(*pascal[i])


