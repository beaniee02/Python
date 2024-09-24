val = 4
if val < 6:
    print('correct')
    if val >= 8:
        print('The value is 5')
    if val == 3:
        print('The value is less than 5')
elif val % 2 == 0:
    print('This is an even number')
else:
    print('Incorrect')


#For loop
# list_items = ['mango', 'orange', 'apple', 'pineapple', 'cashew']
# list_items2 = ['basket', 'container', 'bucket']
# turns = 0
# for fruits in list_items:
#     turns+=1
#     for each in list_items2:
#         print(each)
#         print('round {} >>> this is {}'.format(turns, fruits))

#Multiplication table
for numbers in range(1, 6):
    for digits in range(1, 6):
        multiply = digits * numbers
        print(f'\n{numbers} * {digits} = {multiply}', end='')
    print()