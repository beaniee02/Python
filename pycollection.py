'''
list
tuple
set
dictionary
'''

list_of_student = list(['kiki', 'bolu', 'tope', ['dara', 'titi']])
list_of_item =  ['1', 3j, 6.8, True, ['Temi', 'Taiwo']]
list_of_student2 = list(['kiki', 'bolu', 'tope', ['dara', 'titi' 'temi'], 'ayo', 'bayo', 'fola'])
list_of_student3 = [['kiki', 'bolu', 'tope'], ['fola', 'grace']]


print(type(list_of_student))
print(type(list_of_item))

print(len(list_of_student2))
print(len(list_of_student))
print(len(list_of_item))

print((list_of_student[3][1]))
print(list_of_student3[0][1], list_of_student3[1][1])
print(list_of_student3[0][1], list_of_student2[3][1])
print(list_of_student2[-3:-1])

list_of_student2.reverse()
print('reversing all the names: ',list_of_student2)

list_of_student3.append('Temi')
print('appending a name: ', list_of_student3)

empty_list = []
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

list_of_student4 = [['Aliu', 'Habeeb', 'Fathima'], ['Sodiq', 'Toheeb']]
list_of_student3.extend(list_of_student4)
# print(list_of_student3)
list_of_student3.insert(2, 'Habeeb')
# print(list_of_student3)

list_of_student3.remove('Temi')
list_of_student3.pop(1)
print(list_of_student3)
list_of_student3.pop()
print(list_of_student3)

list1 = []
list1 = [int(item) for item in input('Enter the list items: ').split()]
print(list1)


name = 'tolu titi'
print(name.split())