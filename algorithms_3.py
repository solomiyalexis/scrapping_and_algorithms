# task_1 - leap year and list of all leap years from 0 to 2018 and count their amount
def is_leap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    return False

years = [n for n in range(2019)]
leap_years_list = []
for year in years:
    if is_leap(year):
        print( year, 'is leap')

# task_2 - 2 lists: list1 = [0...100000] / 3, list2 = [0...100000] / 7 + find all not douplicated elements which are in both lists
list1 = [n for n in range (100000) if n%3==0]
list2 = [n for n in range (100000) if n%7==0]

list3 = set(list1).union(set(list2))
print(list3)

# task_3 - there is a list with not ordered nums, find second highest num in the list
list = [1, 5, 8, 2, 4, 9, 10, 3, 6, 7]
list.sort(reverse=True)
print('the second highest num in', list, 'is', list[1])

# task_4 - python = {2: 'Ivan', 17: 'Artem', 18: 'Sergey', 21: 'Antuan', 34: 'Anton', 35: 'Sergey', 37: 'Stepan', 43: 'Artem', 44: 'Antuan', 51: 'Sergey', 60: 'Antuan',
# 61: 'Sergey', 62: 'Stepan', 78: 'Artem', 79: 'Stepan', 82: 'Ivan', 90: 'Antuan', 94: 'Antuan', 95: 'Ivan'}
# js = {0: 'Antuan', 7: 'Sergey', 10: 'Anton', 16: 'Ivan', 17: 'Ivan', 23: 'Ivan', 33: 'Ivan',34: 'Antuan', 39: 'Ivan', 45: 'Artem', 47: 'Stepan', 58: 'Stepan',
# 66: 'Stepan', 67: 'Sergey', 71: 'Sergey', 73: 'Antuan', 87: 'Stepan', 94: 'Antuan', 96: 'Stepan'}
# find students who study both lang and one only

python = {2: 'Ivan', 17: 'Artem', 18: 'Sergey', 21: 'Antuan', 34: 'Anton', 35: 'Sergey', 37: 'Stepan', 43: 'Artem', 44: 'Antuan', 51: 'Sergey', 60: 'Antuan',
61: 'Sergey', 62: 'Stepan', 78: 'Artem', 79: 'Stepan', 82: 'Ivan', 90: 'Antuan', 94: 'Antuan', 95: 'Ivan'}
js = {0: 'Antuan', 7: 'Sergey', 10: 'Anton', 16: 'Ivan', 17: 'Ivan', 23: 'Ivan', 33: 'Ivan',34: 'Antuan', 39: 'Ivan', 45: 'Artem', 47: 'Stepan', 58: 'Stepan',
66: 'Stepan', 67: 'Sergey', 71: 'Sergey', 73: 'Antuan', 87: 'Stepan', 94: 'Antuan', 96: 'Stepan'}

#variant_1
both_courses = {x:python[x] for x in python if x in js}
print(both_courses)

#variant_2
intersection = dict(python.items() & js.items())
print(intersection)



# task_5 generators
# variant_1
def square_nums(nums):
    for i in nums:
        yield (i*i)

square_result = square_nums([1, 2, 3, 4, 5])

for n in square_result:
    print (n)

#variant_2
square_result = (i*i for i in [1,2, 3, 4, 5])
print (square_result)

for n in square_result:
    print (n)
