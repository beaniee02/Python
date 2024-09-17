'''
list
tuple
set
dictionary
'''

# list_of_student = list(['kiki', 'bolu', 'tope', ['dara', 'titi']])
# list_of_item =  ['1', 3j, 6.8, True, ['Temi', 'Taiwo']]
# list_of_student2 = list(['kiki', 'bolu', 'tope', ['dara', 'titi' 'temi'], 'ayo', 'bayo', 'fola'])
# list_of_student3 = [['kiki', 'bolu', 'tope'], ['fola', 'grace']]


# print(type(list_of_student))
# print(type(list_of_item))

# print(len(list_of_student2))
# print(len(list_of_student))
# print(len(list_of_item))

# print((list_of_student[3][1]))
# print(list_of_student3[0][1], list_of_student3[1][1])
# print(list_of_student3[0][1], list_of_student2[3][1])
# print(list_of_student2[-3:-1])

# list_of_student2.reverse()
# print('reversing all the names: ',list_of_student2)

# list_of_student3.append('Temi')
# print('appending a name: ', list_of_student3)

# empty_list = []
# for each in range(0,2):
#     name = input('Enter your name: ')
#     age = input('Enter your age: ')
#     age_name = name, age
#     empty_list.append(age_name)
# print(empty_list)

# for each in range(0,3):
#     age_name = name = [input('Enter your name: '), input('Enter your age: ')]
#     empty_list.append(age_name)
# print(empty_list)

# list_of_student4 = [['Aliu', 'Habeeb', 'Fathima'], ['Sodiq', 'Toheeb']]
# list_of_student3.extend(list_of_student4)
# print(list_of_student3)
# list_of_student3.insert(2, 'Habeeb')
# print(list_of_student3)

# list_of_student3.remove('Temi')
# list_of_student3.pop(1)
# print(list_of_student3)
# list_of_student3.pop()
# print(list_of_student3)

# list1 = []
# list1 = [int(item) for item in input('Enter the list items: ').split()]
# print(list1)


# name = 'tolu titi'
# print(name.split())


#Tuple - it contains heterogenous elements which can be accessed by indexing. It is immutable, it is faster than list(when it comes to iteration)
fruits = ('mango', 'pawpaw')
fruits2 = tuple(('mango', 'pawpaw', 'orange', 'apple'))
fruits_basket = ('mango', 'pawpaw', 'mango', 'pawpaw', 3j,('temi', 'dara', 'taiwo', 'tk'), ['cucumber', 'banana'], {1, 2, 3})

print(type(fruits2))
print(len(fruits2))
print(fruits2[::-1])
print(len(fruits_basket))
print('findings: ', fruits_basket[::2])
print('\nindex 5:', fruits_basket[5][0], '\n')

for name in fruits_basket[7]:
    print(name)

#unpacking
employee = (('Taiwo', 'taiwo123@gmail.com', 'liegeman', 'male'), ('Dara', 'daradudu@gmail.com', 'doughnutBoy', 'male'), ('Temi', 'iyagbogbo@gmail.com', 'iyagbogbo', 'female'), ('Tkristi', 'tgirl@gmial.com', 'tgirlie', 'female'))

# employee1, employee2, employee3 = employee
# print(employee1[0], employee2[0], employee3[0])

employee1, *others, employee3 = employee
print(others)

# for name, email, username, gender in employee:
    # print('name of employees', name, '\n')
    # print('email of employees', email, '\n')
    # print('username of employees', username, '\n')
    # print('gender of employees', gender, '\n')

x = 0
for name, _, _, _ in employee:
    x += 1
    print(f'name of employees {x} {name} \n')

#concateninating two tuples
fruits4 = fruits + fruits2
print(fruits4)

del fruits


#Set
set1 = {1, 6, 3, 4, 6, 4}
set2 = set({8, 4, 3, 9})

print(type(set1))
print(type(set1))

set1.add(5)
set1.update((12, 14,15))
set1.remove(15)
set3 = set1.copy()
set1.add(10)
print(set3)
print(set1)