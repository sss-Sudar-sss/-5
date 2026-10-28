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