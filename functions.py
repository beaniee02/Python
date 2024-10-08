'''
Types of function: inbuilt function and owned fuction
stages of function: declaration, definition and invoking
'''

# def landing_page():
#     print('''
#                 1. login
#                 2. register
#                 3. make enquiries
#                 4. exit
#         ''')
#     user = input('select option>>> ')
#     if user == '1':
#         print("Welcome")
#     elif user == '2':
#         print("Welcome you can now register")
#     elif user == '3':
#         print("What do you want to know!! oloju rangandan")
#     elif user == '4':
#         exit()

# landing_page()

'''
Parameterized functions
Non parametrized functions
Global variable
Local variable
Parameter
Argument
'''
z = 10
def add_num(x, y):
    global b
    b = 25
    q = 10
    sum_all = x + 8 + y + z + q
    print(sum_all)
add_num(4, 2)

def subtract_num(j, k):
    sub_all = b - j - 8 - k - z
    print(sub_all)
subtract_num(15, 2)


'''
types of argument
1. default args
2. keyword args
3. positional args
4. arbitrary args
'''

#default
def add_num(x=4, y=14):
    global b
    b = 25
    q = 10
    sum_all = x + 8 + y + z + q
    print(sum_all)
add_num()

#keyword
def college(name, location):
    print(name, location)

college(name='SQI', location='Yoaco')
college(location='Yoaco', name='SQI')

#positional
def college_class(college, level):
    print(f"My name is Bolu, I study at {college} and My level is {level}")

college_class("SQI", "Level2")
college_class("Level2", "SQI")

#arbitrary
def college_class_(*args):
    print(f"My name is Bolu, I study at {args[0]}, My level is {args[1]} and I'm about to go {args[2]}")

college_class_("SQI", "Level2", "Home", "titi", "tolu")

#kwargs
def collegeclass(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs)
    # print(kwargs.keys)

collegeclass(name="SQI", levl="Level2", address="Home", name2="Titi", name3="Tife")


import sys
val1 = 50
val2 = 20
def subtract():
    a = input('enter first value>>> ')
    b = input('enter second value>>> ')