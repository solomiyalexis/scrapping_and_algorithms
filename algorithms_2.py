# task_1_alternative for the previously_done task - find similar numbers in different names
phone_book = {'Mike': ['1234', '12345'], 'Dave': ['1234'], 'Ivar': ['050123456789']}
def do_count():
    result = {}
    for name in phone_book.values():
        for phone in name:
            result.setdefault(phone, 0)
            result[phone] += 1
    return result
def left_only_where_count_more_1(counted_duplicates):
    result = []
    for k, v in counted_duplicates.items():
        if v > 1:
            result.append(k)
    return result

count_result = do_count()
left_result = left_only_where_count_more_1(count_result)
print(left_result)

# task_2 - Садик в нем дети (edited)
# Нужно найти имена детей которых возвраст в диапазоне от 7 до 10 лет включительно (edited)
# Игорь - 5
# ваня - 7
# егор - 8
# Инокентий - 30
# Саша - 10
# результат -  [ваня, егор, Саша]
kids = {'igor': 5, 'vanya': 7, 'egor': 8, 'innikentiy': 30, 'sasha': 10}
srch_names = {}
for n, a in kids.items():
    if 7<=a<=10:
        srch_names[n]=a
        print(srch_names)

kids = {'igor': 5, 'vanya': 7, 'egor': 8, 'innikentiy': 30, 'sasha': 10}
srch_names = []
for n, a in kids.items():
    if 7<=a<=10:
        srch_names.append(n)
print(srch_names)

# task_3 - есть числа от 1го до 500та
# нужно:
# сложить все числа которые делятся на 32
# умножить все числа которые делятся на 100
# получить результат умножения и сложения
list = [n for n in range(1, 501)]
pluslist = []
mult = 1
for n in list:
    if n%32 == 0:
        pluslist.append(n)
        result = sum(pluslist)
    elif n % 100 == 0:
        mult*=n
print (result, mult)

# task_4 - Есть словарь 1->2 2->3 3->4…99->100
# его нужно сгенерировать автоматически (edited)
# и потом сделать список в котором будут умноженные ключи на значения
list = [n for n in range(1, 101)]
dict = {}
mult = []
for n in list:
    dict[n] = n+1
print(dict)
for k, v in dict.items():
    mult.append(k*v)
print(mult)

# task_5 - есть словарь 1->10 2->20 3->30 4->50 5->80 6->130 … ряд фибоначи 99 -> ? - узнать,что под закоом вопроса
list = [n for n in range (1, 100)]
list2 = []
a = 0
b = 10

def fib(a, b):
    for n in range (1, 100):
        c = a+b
        a = b
        b = c
        list2.append(c)
    return list2

dict = dict(zip(list, fib(a, b)))
print(dict)
print(dict[99])

# task_6 - есть такой словарь
# {‘a’:[1,2,3], ‘b’:[4,5,6], ‘c’:[7,8,9], ‘d’:[10,11,12]  и т.д. }
# так 10 раз нужно сгенерить автоматически
# потом нужно из массава сделать сумму
# [1,2,3]-> 6
# [4,5,6]->15
# и получить на выходе
# {‘a’:6, ‘b’:15 …}
dict = {}
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'j', 'k', 'l']
size = 1

def sub_list(size):
    return [size, size+1, size+2]

for l in list:
    dict[l] = sub_list(size)
    size+=3

for k, v in dict.items():
    dict[k] = sum(v)
print(dict)


# task_7 - есть числа от 1го до 200т
# нужно:
# сложить все числа которые делятся на 16
# умножить все числа которые делятся на 50
sum = 0
mult = 1
for n in range(1, 200):
    if n%16==0:
        sum +=n
    elif n%50 ==0:
        mult*=n
print(sum, mult)

# task_8 - Есть 2 словаря
# 1:2, 2:3, 3:4 и так до 50:51
# 1:3, 2:6,3 :9 и та4 до 60:61
# Нужно обеденить эти словари и получить 3й словарь где значением будет сумма чисел из 1го и 2го
# Т.е.
# 1:5, 2:9, 3: 13 ....
def create_dict (size, shift=None, mult=None):
    dict = {}
    for n in range(1, size):
        if shift:
            dict[n] = n+shift
        elif mult:
            dict[n] = n*mult
    return dict

dict1 = create_dict(51, shift=1)
dict2 = create_dict(61, mult=3)

def merge_dicts(dict1, dict2):
    dict = {}
    for n in range(1, max(len(dict1), len(dict2))):
        dict[n] = dict1.get(n, 0) + dict2.get(n, 0)
    return dict

dict3 = merge_dicts(dict1, dict2)
print(dict3)

#alternative version
s = set()
s.update(dict1.keys())
s.update(dict2.keys())
print(s)
dict3 = {}

for k in s:
   dict3[k] = dict1.get(k, 0) + dict2.get(k, 0)
print(dict3)

# task_9 - у тебя есть числа
# 1,4,7,9,11,15,30,40,100
# и
# 2,4,4,5,7, 10 , 11, 5O
# тебе нужно напиать такой алгоритм, который сделает слияние этих списков
# и на выходе получится отсортированный массив
# 1,2,4,4,4,5,7,9,10,11,11,15,30,40,50,100
list1 = [1,4,7,9,11,15,30,40,100]
list2 = [2,4,4,5,7,10,11,50]
list1+=list2
list1 = sorted(list1)
print(list1)

# task_10 - 2я задача
# есть словарь
# a = {1:2, 2:3, 3:4 …. 99:100 }   — нужно сгенерировать через цикл
# потому нужно сделать новый словарь в котором будут поменяны местами ключ и значение
# получишь
# b = {2:1, 3:2, 4:3 … 100:99}
dict = {}
dict2 = {}

for n in range(1, 100):
    dict[n] = n+1
    v = dict[n]
    dict2[v] = n
print(dict2)


# task_11 - a = [1,4,7,10 … 1000]
# нужно умножить каждое число на позицию на которой находится
# т.е.
# b = [1 * 1, 4 * 2, 7 * 3, 10 * 4 …. ]
list = []
list2 = []
num = 0
for n in range(1, 1001):
    n = num + 1
    num+=3
    list.append(n)
for i, n in enumerate(list, start=1):
    list2.append(i*n)
print(list2)


#task_12 - два словаря
# dict1 = {1:2, 10:30, 500:1000}
#dic2 = {1:3, 9: 200, 500: 1001}
# соединить и получить третий, в котором ключи будут из первых двух, но без повторений, а занчения будут их первых двух, но сплюсованные
dict1 = {1:2, 10:30, 500:1000}
dict2 = {1:3, 9: 200, 500: 1001}
s = set()
s.update(dict1)
print(s)
s.update(dict2)
print(s)
dict3 = {}
for n in s:
    dict3[n] = dict1.get(n, 0) + dict2.get(n, 0)
print(dict3)

# task_13  - аналог метода сорт (по восходящим числам) вручную
a = [1, 2, 3, 11]
b = [2, 3, 4, 3, 6, 8, 10]

def safe_get_by_index(array, index):
    return array[index] if len(array) > index else None

def merge(array1, array2):
    if len(array1) == 0:
        return array2

    if len(array2) == 0:
        return array1

    result = []
    index1 = 0
    index2 = 0
    while True:
        v1 = safe_get_by_index(array1, index1)
        v2 = safe_get_by_index(array2, index2)

        if v1 is None and v2 is None:
            return result
        elif v1 is None:
            index2 += 1
            result.append(v2)
        elif v2 is None:
            index1 += 1
            result.append(v1)
        else:
            if v1 < v2:
                index1 += 1
                result.append(v1)
            elif v2 < v1:
                index2 += 1
                result.append(v2)
            else:
                index1 += 1
                result.append(v1)


c = merge(a, b)
print(c)

# task_14 -  Find the element that appears once
# ```Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
# Output: 2```
input = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
input1 = {}
for n in input:
    input1.setdefault(n, 0)
    input1[n]+=1
for k, v in input1.items():
    a = input1[k]
    if a == 1:
        print (k)


# task_15 - Write a program to find out duplicate or repeated characters in a
# string, and calculate the count of repeatition.
string = 'hello, world!'
dict = {}
for l in string:
    if string.count(l) > 1:
        dict.setdefault(l, 0)
        dict[l]+=1
print(dict)


# task_16 - Есть список a = [1,2,3,4,5,6,7,8,9, xxx , 1000]
# нужно написать метод который разобъет этот список на список списков по указаному количеству элементов.
#
# пример:
# a = [1,2,3]
#
# result = split_by_partition(a, 1)
# print (result)
# # результат  [ [1], [2], [3] ]
# или
# result = split_by_partition(a, 2)
# print (result)
# # результат  [ [1,2], [3] ]
#
# или
# result = split_by_partition(a, 3)
# print (result)
# # результат  [  [1,2,3]  ]
a = [n for n in range(1, 1000)]
size = 3
list = [a[n:n+size] for n in range(0, len(a), size)]
print(list)


# task_17 - 1. Написать сортировку пузырьком
# variant_1
def get_min(a):
    if len(a) == 0:
        return None

    cached_min = a[0]
    cached_i = 0

    for i, n in enumerate(a):
        if n < cached_min:
            cached_min = n
            cached_i = i

    return cached_i


def swap(array, from_index, to_index):
    v = array[to_index]  # remember value
    array[to_index] = array[from_index]  # move from_index to to_index
    array[from_index] = v  # restore old


to_sort_array = [5, 3, 1, 5, 1, 2, 6, 8, 9]

for v, n in enumerate(to_sort_array):
    min_index = get_min(to_sort_array[v:])
    swap(to_sort_array, min_index + v, v)

print(to_sort_array)

# variant_2

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i] # темр = 55
                alist[i] = alist[i+1] # лист_ай = 20
                alist[i+1] = temp # лист_ай+1 = 55

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


# task_18 - есть 2 списка
# нужно найти пересечения их (т.е. все элементы которые повторяются и другом)
a = {5,6,7,8,9,10}
b = {1,2,3,4,5,6}
print(b.intersection(a))


# task_19 - есть список со строками
# нужно найти строку с максимальной длинной
a = ['hello', 'world', 'hello world']
#variant_1
b = max(a, key=len)
print (b)
#variant_2
def longestr(a):
    count = 0
    for w in a:
        if len(w) > count:
            count = len(w)
            word = w
            print('the longest string is ' + word + '. it\'s length is', count)
print(longestr(a))



# task_20 - есть массив со строками
# [“add”,“pop”,“pop”,“pop”,“add”]
# и соответствующий по длинне массив с числами
# [1,2,3,4,5]
# нужно получить результат программы если для каждого слова “add” элемента будет добавляться, а при кадом “pop” убираться из списка результата
# т.е. для этой программы ответ будет [5]
# в случае если список пустой “pop” не останавливает программу
a = ['add','pop','pop','pop','add']
b = [1,2,3,4,5]

def add_pop_num(a, b):
    c = []
    for x, y in zip(a, b):
        if x == 'add':
            c.append(y)
        elif x == 'pop':
            if c:
                c.pop()
    return c

print(add_pop_num(a, b))

# task_21 - еcть список цифр, если в этом списке есть число `100`, то вернуть True, а иначе False
list = [n for n in range (1, 101)]
def true_false(list):
    for n in list:
        if n == 100:
            return True
    return False
print(true_false(list))


# task_22 - у тебя есть данные:
# [1, 2, 3, 4, 5, 3]
# [1, 2, 3, 4, 5, 7]
# тебе нужно получить результаты умноножения всех чисел 3 на симметричное ему число из другого списка
# т.е. в этой задаче [ 9,  21]
a = [1, 2, 3, 4, 5, 3]
b = [1, 2, 3, 4, 5, 7]
c = []
def mult (a, b):
    for x, y in list(zip(a, b)):
        if x == 3:
            n = x*y
            c.append(n)
    return c
mult_nums = mult(a, b)
print(mult_nums)


# task_23 - Дано  [[1,2,3],[4,5,6], [7,8,9] …  ] так до 1000
#
# найти все  тройки где есть простые числа и вывести их. Наример:
#
# [[1,2,3],[7,8,9],[10,11,12],[13,14,15],[16,17,18] … ]
#
# сделать метод is_prime и contains_prime

a = [n for n in range(1, 1000)]
size = 3
list = [a[n:n+size] for n in range(0, len(a), size)]
print(list)

def is_prime(n):
    if n>1:
        for num in range(2, n):
            if n%num==0:
                return False
    return True
print(is_prime(4))

def contains_prime(list):
    for x in list:
        if is_prime(x):
            return True
    return False

new_list = []
for l in list:
    if contains_prime(l):
        new_list.append(l)
print(new_list)


# task_24 - find if the year is leap / find a number of days in a month for a certain year - use days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    return False

print(is_leap(1988))

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(year, month):
    if not month >=1 and month <=12:
        print ('enter the correct months')
    if month == 2 and is_leap(year):
        return 29
    return days[month]

print(days_in_month(1987, 9))
