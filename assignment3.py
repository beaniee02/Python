#Build even and odd number checker
number = int(input('Enter a number: '))
if number % 2 == 0:
    print('The number you entered is an even number')
else:
    print('The number you entered is an odd number')

# Collect names of students and group them into two different departments
# namesofstuddents = ['Busola', 'Benjamin', 'Quyum', 'Dara', 'Taiwo', 'Favour', 'Tife', 'Ajibola']
name = input('\nEnter your name: ')
if len(name) % 2 == 0:
    print('You are in Group A')
else:
    print('You are in Group B')

#Set 5-10 structured cbt questions and grade the student
score = 0
question1 = input('Which of the following is an input device? ')
ans1 = ['Keyboard', 'Monitor', 'Printer', 'Speaker']
if question1 in ans1[0]:
    score+=10
    print('You answered the question correctly')
else:
    print(f'The correct answer is', ans1[0])
question2 = input('\nWhich of the following is a high-level programming language? ')
ans2 = ['Assembly', 'Python', 'Machine code', 'Binary']
if question2 in ans2[1]:
    score+=10
    print('You answered the question correctly')
else:
    print('The answer is', ans2[1])

question3 = input('\nIn Python, which loop is used to repeat a block of code a specific number of times? ')
ans3 = ['while loop', 'for loop', 'do-while loop' 'if-else loop']
if question3 in ans3[1]:
    score+=10
    print('You answered the question correctly')
else:
    print('The correct answer is', ans3[1])

question4 = input('\nWhich HTML tag is used to create a hyperlink? ')
ans4 = ['<img>', '<a>', '<p>', '<div>']
if question4 in ans4[1]:
    score+=10
    print('You answered the question correctly')
else:
    print('The correct answer is', ans4[1])

question5 = input('\nWhat is the file extension for Python? ')
ans5 = ['.txt', '.java', '.html', '.py']
if question5 in ans5[3]:
    score+=10
    print('You answered the question correctly')
else:
    print('The correct answer is', ans5[3])

question6 = input('\nWhat does the acronym "IP" stand for in networking? ')
ans6 = ['Internet Protocol', 'Internal Pathway', 'Information Packet', 'Instant Program']
if question6 in ans6[0]:
    score+=10
    print('You answered the question correctly')
else:
    print('The correct answer is', ans6[0])

question7 = input('\nWhat does CPU stand for? ')
ans7 = ['Central Processing Unit', 'Central Program Unit', 'Central Print Unit', 'Computer Program Unit']
if question7 in ans7[0]:
    score+=10
    print('You answered the question correctly')
else:
    print('The correct answer is', ans7[0])

question8 = input('\nWhich of the following is an example of an operating system? ')
ans8 = ['Microsoft Word', 'Windows', 'Python', 'Google Chrome']
if question8 in ans8[1]:
    score+=10
    print('You answered the question correctly')
else:
    print('The correct answer is', ans8[1])

question9 = input('\nWhich of the following is used to display information on a computer? ')
ans9 = ['Mouse', 'Hard Drive', 'Monitor', 'Keyboard']
if question9 in ans9[2]:
    score+=10
    print('You answered the question correctly')
else:
    print('The correct answer is', ans9[2])

question10 = input('\nWhich of the following is a web browser? ')
ans10 = ['Android', 'Windows', 'Microsoft Word', 'Google Chrome']
if question10 in ans10[3]:
    score+=10
    print('You answered the question correctly')
else:
    print('The correct answer is', ans10[3])

print('\nYour total score is', score)