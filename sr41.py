from random import uniform
arr=[]
arrSize=int(input("Введите размерность массива: "))
f=input("Хотите ввести элемента массива? y/n ")
if (f=="y"):
    for i in range (arrSize):
        arr.append (float(input()))
elif (f=="n"):
    for i in range (arrSize):
        arr.append (uniform(0,100))
else:
    print ("Ошибка")
pointermax=arr.index (max(arr))
print ("Входной массив")
print (arr)
for i in range (pointermax +1,arrSize):
    arr[i]=0
print ("Результат")
print (arr)