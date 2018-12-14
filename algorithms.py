# task_1 - min / max numbers
x = [i for i in range(1, 10)]
min_num = min(x)
max_num = max(x)
print (min_num, max_num)

# task_2 - even / not even numbers
x = [i for i in range(1, 10)]
for i in x:
    if i % 2 == 0:
        print ('number', i, 'is even')
    else:
        print ('number', i, 'is not even')

# task_3 - multiplication table
size = 10
for i in range (1, 11):
    for j in range (1, 11):
        k = i*j
        print (k, ' ', end='')
        if k==i*10:
            print()

# task_4 - '*' steps
for i in range(1, 10):
    s = i*'*'
    print(s)

# task_5 - numbers steps
for i in range (1, 10):
    n = i*str(i)
    print(n)

# task_5 - sum of numbers in a string
raw_input = input('type data:')
if raw_input.isdigit():
    suma = sum(int(n) for n in raw_input)
    print(suma)

# task_6 - delete 5 symboled strings from the list
line = 'there are words with more than five symbols'
new_line = line.split(' ')
for w in new_line:
    if len(w)>5:
        new_line.remove(w)
print(new_line)

# task_7 - show numbers 1-9 in a table 3x3
for n in range(1, 10):
    print(n, ' ', end='')
    if n % 3==0:
        print()