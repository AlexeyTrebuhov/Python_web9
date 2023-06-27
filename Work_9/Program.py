

#  1.   Напишите следующие функции:
#  Нахождение корней квадратного уравнения
#  Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
#  Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
#  Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# 2.   Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса


import random
import csv
import os
from math import sqrt
import json
import math

def obxodFile(path):

    for i in range (30):  # количество строк списков, содержащих три цифры
        z1 = random.randint(1,19)
        z2 = random.randint(1,29)
        z3 = random.randint(1,19)
        tree_digit = [z1,z2,z3]        # создали одиночный список с тремя цифрами

        with (
            open('new_csv_file.csv', 'a', newline='', encoding='utf-8')   # записываем в формате csv
            as f_write
        ):
            csv_write = csv.writer(f_write, dialect='excel-tab', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
            all_data = []
            all_data.append(tree_digit)
            print("Записано построчно в файл csv =" ,all_data)
            csv_write.writerows(all_data)

    print("_"*70)

    with open('new_csv_file.csv', newline='') as f:              # чтение из csv
        csv_file = csv.reader(f,dialect="excel-tab",quotechar=',', quoting=csv.QUOTE_NONNUMERIC )

        for line in csv_file:
            a = int(line[0])
            b = int(line[1])
            c = int(line[2])

            data = {}  # Создали словарь для записи итоговых параметров
            data ['meta'] = []



            def decorator_with_args(func): # декоратор для вычисления дискриминанта
                def decorated(a, b, c):
                    ret = func(a, b, c)
                    return ret
                return decorated

            @decorator_with_args
            def add(a, b, c):
                return (b*b)-(4*a*c)
            Discr = add(a,b,c)     # тут вычислили дискриминант и переменные
            #print('Discr:', Discr)



            def decorator_with_args(func): # декоратор для вычисления X для случая если Discr равен ноль
                def decorated(a, b):
                    frt = func(a, b)
                    return frt
                return decorated

            @decorator_with_args
            def sub(a, b):
                return int(-b/(2*a))
            x = sub(a,b)     # тут вычисляем X для случая если Discr равен ноль


            if (Discr >= 0):
                x1 = float((-b + sqrt(Discr))/(2*a))
                x2 = float((-b - sqrt(Discr))/(2*a))

            if (Discr < 0):
                sum_string = str ("корней нет")
                print("При а = ",a," b = ",b,"c = ",c, "Discr =",Discr, sum_string)

            if (Discr == 0):
                sum_string = str (x)
                print("При а = ",a," b = ",b,"c = ",c,"Discr =",Discr, " X1 = ", sum_string)

            if (Discr > 0):
                sum_string = "X1 = " + str (x1) , " X2 = " +  str (x2)
                print("При а = ",a," b = ",b,"c = ",c, "Discr =",Discr," Значения X: ", sum_string)


            def decorator_with_args(func): # декоратор для сохранения в json файл
                def decorated(a, b,c):
                    rur = func(a, b,c)
                    return rur
                return decorated

            @decorator_with_args
            def rur(a, b,c):
                return { "a":a,"b":b,"c":c, "X": sum_string }
            woth_iz_it = rur(a,b,c)


            data ['meta'].append(woth_iz_it)

            with open ('new_json_file','a',encoding= "utf-8") as outfile:     # записываем в формате json
                json.dump (data,outfile)


    f.close()
    os.remove('new_csv_file.csv')   # удаляем файл csv в конце работы программы

obxodFile(os.path)

if __name__ == "__main__":
    print()



