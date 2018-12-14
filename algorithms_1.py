# task_1 - chose unique (not douplicated) words from the text
line = 'there are some unique words in this set of words'
new_line = line.split(' ')
for w in new_line:
    if new_line.count(w)<2:
        print(w)

# task_2 - number of repeated words in the text
line = 'there are some repeated words in this set of words'
repeated = {}
for w in line.split(' '):
    count = line.count(w)
    repeated[w] = count
print(repeated)

#task_3 - delete forbiden words (substitute into "*")
forbiden = ['forbiden', 'words']
text = 'there are some forbiden words in this line'
for f in forbiden:
    text = text.replace(f, '***')
print(text)

# my first variant
forbiden = ['forbiden', 'words']
text = 'there are some forbiden words in this line'
for w in text.split(' '):
    for f in forbiden:
        if w==f:
            text = text.replace(w, '***')
print(text)

# task_4 - words which appear in both texts
text1 = 'hello, world!'
text2 = 'hi, world!'
for w in text1.split(' '):
    for z in text2.split(' '):
        if w==z:
            print(w)

# task_5 - search of similar numbers among different people
# my variant
phone_book = {'ivan': 12345, 'petr': 23456, 'frank': 12345}
phones = {}
for name, phone in phone_book.items():
    phones.setdefault(phone, [])
    phones[phone] += [name]
print(phones)

# task_6 - divide keys and values in different lists
dict = {1:2, 3:4, 5:6}
list1 = []
list2 = []
for k, v in dict.items():
    list1.append(k)
    list2.append(v)
print (list1, list2)

