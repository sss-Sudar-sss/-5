import random
#Задание 1
print("#Задание 1")
while True:
    print("Введите строку:")
    stroka=input()
    e_s= True
    for i in stroka:
        if i !=" " and i !="\t" :
            e_s=False
            break
    if e_s:
        print("Строка не может быть пустой!")
    else:
        break
count = 0
pp= False
for s in stroka:
    if s!="," and s!=";" and s!="." and s!=" " and s !="\t":
        if not pp:
            pp=True
            count +=1
    else:
        pp=False
print("Ваша строка:", stroka)

print("Количество слов в ней:",count)


#Задание 2
print("#Задание 2")
while True:
    print("Введите строку со скобками:")
    stroka=input()
    e_s= True
    for i in stroka:
        if i !=" " and i !="\t" :
            e_s=False
            break
    if e_s:
        print("Строка не может быть пустой!")
    else:
        break
res=""
g= False
for i in stroka:
    if i == "(" or i == "[" or i == "{":
        g=True
    elif i == ")" or i == "]" or i == "}":
        g=False
    else:
        if not g:
            res += i
print("Ваша строка:", stroka)
print("Ваша изменненая строка (без текста в скобках):", res)


#Задание 3
print("#Задание 3")
while True:
    print("Введите размер списка (натуральное число):")
    try:
        n=int(input())
    except ValueError:
        print("Размер списка это натуральное число!")
        continue
    if n<=0:
        print("Размер списка это положительное число и не может быть равно нулю!")
    else:
        break
spisok=[]
for i in range(n):
    s=random.randint(-100,100)
    spisok.append(s)
print("Ваш список со случайными элементами:", spisok)
su=0
for i in range(n):
    if (i+1) % 2 !=0:
        su += spisok[i]
print("Сумма элементов списка с нечетными номерами:",su)



ot1=-1
ot2=-1
for i in range(n):
    if spisok[i]<0:
        ot1=i
        break
for i in range(n-1,-1,-1):
    if spisok[i]<0:
        ot2=i
        break
su_ot = 0
if ot1!=-1:
    if ot1 == ot2:
        print("Отрицательное число единственное в списке!")
    else:
        for i in range(ot1 + 1, ot2):
            su_ot+=spisok[i]
        if su_ot==0:
            print("Сумма чисел между первым и последним отрицательными числами (исключая границы):", su_ot)
            print("(Так как элементы не содержат между собой чисел.)")
        else:
            print("Сумма чисел между первым и последним отрицательными числами (исключая границы):", su_ot)
else:
    print("Недостаточно отрицательных элементов в списке!")