'''
try
except
finally
'''

for i in range(1,3):
    try:
        rand_num = int(input('enter a number>> '))
        print(f'{rand_num} is an integer')
    except:
        print('the num should be an integer')