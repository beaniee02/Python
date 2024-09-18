#single line comment
#Below is a multi-line comment
'''won ni won wa mi won ni won wa mi i'm in sanfrancisco jamming'''

#escape characters: \n- means a new line

print('I am now a certified python developer')


'''
variable definition
variable declaration
variable rules
'''
#definition and declaration
student_name = 'Temi', 'Dara', 'Tkristi', 'Taiwo'
print(student_name)

#rules
'''
Your name must be well descriptive
You should not start naming with numbers
You should not use reserve words i.e. function names for naming
No spacing in between names
You cant use special characters to start naming
'''
_name = "temi"
print(_name)

fruits = 'agbalumo', 'mango'
fruit2 = 'agbalumo'

#naming convention
'''
pascal naming convention
camel  casing
snake casing
'''
#camelcasing
nameOfStudent = 'Grace'
#snakecasing
name_of_student = 'Grace'
#pascalcasing
nameOfstudent = 'Grace'

val1 = (2, 4, 5)
result = sum(val1)
print(result)
#inbuilt python function
print(type(fruits))
print(type(fruit2))
print(len(fruit2))

# Patient = input('Is this person a new patient? : ')
# Name = input('What is your name? : ')
# Age = input('How old are you? : ')
# Address = input('Where do you live? : ')
# # print('The'+ ' ' + Age + ' ' + 'year' + ' ' + 'old' + ' ' + Name + ' ' + 'staying' + ' ' + 'at' + ' ' + Address + ' ' + 'is' + ' ' + 'a' + ' ' + 'new' + ' ' + 'patient')
# # print('The', Age, 'year old', Name, 'staying at', Address, 'is a new patient')
# print(f'The {Age} year old {Name} staying at {Address} is a new patient')

#Operators
'''
Arithmetic operators

+  Addition: adds two operands x + y
-  Subtraction:  subtracts two operands x - y
*  Multiplication: multiplies two operands x * y
/  Division(float): divides the first operand by the second x / y
// Division(floor): divides the first operand by the second x // y
%  Modulus: returns the remainder when the first operand is divided by the second x % y
** Power: returns first raised to power second operand x ** y 
'''

# operators






# Types of operators in python
# Arithmetic operators
# Identity operators
# Membership operators
# Assignment operators
# Bitwise operators
# Logical operators
# Comparison or relational operators

'''
Comparison operators in python

>  Greater than: True if the left operand is greater than the right operand x > y
<  Less than: True if the left operand is less than the right operand x < y
==  Equal to:  True if both operands are equal x == y
!=  Not equal to: True if operands are not equal x != y
>=  Greater than or equal to: True if the left operand is greater than or equal to the right operand x >= y
<=  Less than or equal to: True if the left operand is less than or equal to the right operand x <= y
'''

'''
Logical operators in python

and - true if both the operands are true x and y
or - true if either of the operand is true x or y
not - true if the operand is false not x
'''


# a = 'mango'
# b = 'orange'
# if len(a) and len(b) == 5:
#     print('both are of the same length')
# else:
#     print('na lie, both are not of the same length')

# a = 5
# b = 3
# b += a
# print(b)

# score = 0
# question = input('What is your name: ')
# ans = ['Tkristi', 'bukunmi']
# if question in ans:
#     score+=5
#     print('you just scored', score)
# else:
#     print('you just scored', score)


#strings and methods
name = '    fukunmi olanrewaju'
# print(len(name))
# print(name.strip().capitalize())
print(name.replace('f', 'b', 1))

#indexing
student_Name = 'Darasimiamaladudu'
# new_name = student_Name[0:13] + 'lafun'
# new_name = [student_Name]
print(student_Name[0:8:2])
print(student_Name[::3])
