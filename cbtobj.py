# import time
# name_and_matricno_of_registered_students = {'Adesina Busolami' : '202401', 'Ajibade Juliana': '202402', 'Adekunle Kehinde': '202403', 'Ojo Florence' : '202404', 'Ayanlude Boluwatife': '202405'}
# name = input('Enter your name: ')
# matric_no = input('Enter your matric no: ')
# for keys, values in name_and_matricno_of_registered_students.items():
#     if name == keys and matric_no == values: 
#         print('please wait...') 
#         time.sleep(2)
#         print('\nYou can proceed with taking your test\n')
#         score = 0
#         cbt_questions = {
#             '1. Who is the current President of Nigeria? a) Muhammadu Buhari b) Bola Ahmed Tinubu c) Yemi Osibanjo d) Goodluck Johnathan': 'b',
#             '2. In what year did Nigeria gain independence from Britain? a) 1960 b) 1963 c) 1957 d) 1970' : 'a',
#             '3. Which Nigerian state recently became the largest oil producer? a) Akwa Ibom b) Delta c) Rivers d) Lagos' : 'a',
#             '4. Who is the current Governor of the Central Bank of Nigeria (CBN)? a) Godwin Emefiele b) Folashodun Shonubi c) Lamido Sanusi d) Zainab Ahmed' : 'b',
#             '5. Which Nigerian University was recently ranked highest in Africa in Times Higher Education Marketing? a) University of Lagos b) University of Ibadan c) Covenant University d) Obafemi Awolowo University' : 'c',
#             '6. The Nigerian national minimum wage was recently raised to what amount? a) #30,000 b) #50,000 c) #100,000 d) #70,000' : 'd',
#             '7. Which Nigerian artist won the Grammy Award for Best Global Music Album in 2021? a) Burna Boy b) Wizkid c) Davido d) Tiwa Savage' : 'a',
#             '8. The Lekki Toll Gate shooting during the #ENDSARS protests happened in which year? a) 2018 b) 2020 c) 2021 c) 2021 d) 2019' : 'b',
#             '9. What is the capital of Nigeria? a) Lagos b) Port Harcourt c) Abuja d) Kano' : 'c',
#             '10. Which Nigerian footballer recently signed a major deal with a European football club? a) Wilfred Ndidi b) Victor Oshimen c) Kelechi Iheanacho d) Samuel Chukwueze' : 'b',
#             '11. The 2023 Nigerian Presidential election was held on what date? a) Februrary 25, 2023 b) March 10, 2023 c) April 1, 2023 d) January 31, 2023' : 'a',
#             '12. Who is the current Minister of Foreign Affairs in Nigeria? a) Geoffrey Onyeama b) Zainab Ahmed c) Nyesom Wike d) Festus Keyamo' : 'a',
#             '13. The Nigerian national football team is also known as what? a) The Black Stars b) The Desert Warriors c)The Indomitable Lions d) The Super Eagles' : 'd',
#             '14. Which state is the largest by population in Nigeria? a) Lagos b) Kano c) Kaduna d) Rivers' : 'a',
#             '15. Who is the current Chief Justice of Nigeria (CJN)? a) Ibrahim Tanko Muhammad b) Walter Onnoghen c) Olukayode Ariwoola d) Mahmud Mohammed' : 'c'
#             }
        
#         for question, answer in cbt_questions.items():
#             print('\nLoading...\n')
#             time.sleep(1)
#             print(question)
#             ans = input('Answer: ')
#             if ans == answer:
#                 score+=1
#                 percentage = round((score/15)*100)
#         print('please wait while we calculate your score')
#         time.sleep(3)
#         print(f'Dear, {name} you have {percentage}%')
#         break
#     else:   
#         print("You did not register for this course")
#         break



# registered_student = []

# for name in range(1, 6):
#     registered_name = input('Name: ')
#     registered_matricno = int(input('Matric no: '))     
#     student = registered_name, registered_matricno
#     registered_student.append(student)
# print(registered_student)

# for items in range(1, 6):
#     name = input('\nWhat is your name? ')
#     matric_no = int(input('What is your matric no? '))
#     student_details = name, matric_no
#     if student_details in registered_student:
#         ask_student = input('\nAre you ready to take this test (Yes or No)? ')
#         if ask_student == "Yes":
            # score = 0
            # cbt_questions = {
            #     '1. Who is the current President of Nigeria? a) Muhammadu Buhari b) Bola Ahmed Tinubu c) Yemi Osibanjo d) Goodluck Johnathan': 'b',
            #     '2. In what year did Nigeria gain independence from Britain? a) 1960 b) 1963 c) 1957 d) 1970' : 'a',
            #     '3. Which Nigerian state recently became the largest oil producer? a) Akwa Ibom b) Delta c) Rivers d) Lagos' : 'a',
            #     '4. Who is the current Governor of the Central Bank of Nigeria (CBN)? a) Godwin Emefiele b) Folashodun Shonubi c) Lamido Sanusi d) Zainab Ahmed' : 'b',
            #     '5. Which Nigerian University was recently ranked highest in Africa in Times Higher Education Marketing? a) University of Lagos b)University of Ibadan c) Covenant University d) Obafemi Awolowo University' : 'c',
            #     '6. The Nigerian national minimum wage was recently raised to what amount? a) #30,000 b) #50,000 c) #100,000 d) #70,000' : 'd',
            #     '7. Which Nigerian artist won the Grammy Award for Best Global Music Album in 2021? a) Burna Boy b) Wizkid c) Davido d) Tiwa Savage' :'a',
            #     '8. The Lekki Toll Gate shooting during the #ENDSARS protests happened in which year? a) 2018 b) 2020 c) 2021 c) 2021 d) 2019' : 'b',
            #     '9. What is the capital of Nigeria? a) Lagos b) Port Harcourt c) Abuja d) Kano' : 'c',
            #     '10. Which Nigerian footballer recently signed a major deal with a European football club? a) Wilfred Ndidi b) Victor Oshimen c)Kelechi Iheanacho d) Samuel Chukwueze' : 'b',
            #     '11. The 2023 Nigerian Presidential election was held on what date? a) Februrary 25, 2023 b) March 10, 2023 c) April 1, 2023 d)January 31, 2023' : 'a',
            #     '12. Who is the current Minister of Foreign Affairs in Nigeria? a) Geoffrey Onyeama b) Zainab Ahmed c) Nyesom Wike d) Festus Keyamo' :'a',
            #     '13. The Nigerian national football team is also known as what? a) The Black Stars b) The Desert Warriors c)The Indomitable Lions d)The Super Eagles' : 'd',
            #     '14. Which state is the largest by population in Nigeria? a) Lagos b) Kano c) Kaduna d) Rivers' : 'a',
            #     '15. Who is the current Chief Justice of Nigeria (CJN)? a) Ibrahim Tanko Muhammad b) Walter Onnoghen c) Olukayode Ariwoola d) Mahmud Mohammed' : 'c'
            #     }
            # for question, answer in cbt_questions.items():
            #     print(question)
            #     ans = input('Answer: ')
            #     if ans == answer:
            #         score+=1
            #         percentage = round((score/15)*100)
            # print(f'Dear, {name} you have {percentage}%')
#         else:
#             print('Cancel')
#     else:
#         print('You were not registered for this course')
#     if items < 4:
#         ask_user = input('Is the next person available for the test (Yes or No)? ')
#         if ask_user != 'Yes':
#             print('Test Terminated')

# user = []

# def student():
#     for registration in range(1, 12):
#         print('''
#                 1. Register
#                 2. Login
#     ''')
#         ask_user = input('Select an option>>> ')
#         if ask_user == '1':
#             name = input('What is your name? ')
#             password = input("Create your password: ")
#             # if len(password) > 8:
#             #     print('You have exceeded the maximum limit of characters to create a password!')
#             user_details = name, password
#             user.append(user_details)
#             print('You have successfully registered your name for the test')
#         if ask_user == '2':
#             # for students in range(1, 6):
#                 user_name = input('Enter your name: ')
#                 user_password = input('Enter your password: ')
#                 correct_details = user_name, user_password
#                 if correct_details in user:
#                     prompt_user = input('Are you ready to attempt the test? (Yes/No) ')
#                     if prompt_user.lower() == "yes":
                        # score = 0
                        # cbt_questions = {
                        #     ' Who is the current President of Nigeria? a) Muhammadu Buhari b) Bola Ahmed Tinubu c) Yemi Osibanjo d) Goodluck Johnathan': 'b',
                        #     ' In what year did Nigeria gain independence from Britain? a) 1960 b) 1963 c) 1957 d) 1970' : 'a',
                        #     ' Which Nigerian state recently became the largest oil producer? a) Akwa Ibom b) Delta c) Rivers d) Lagos' : 'a',
                        #     ' Who is the current Governor of the Central Bank of Nigeria (CBN)? a) Godwin Emefiele b) Folashodun Shonubi c) Lamido Sanusi d) Zainab Ahmed' : 'b',
                        #     ' Which Nigerian University was recently ranked highest in Africa in Times Higher Education Marketing? a) University of Lagos b)University of Ibadan c) Covenant University d) Obafemi Awolowo University' : 'c',
                        #     ' The Nigerian national minimum wage was recently raised to what amount? a) #30,000 b) #50,000 c) #100,000 d) #70,000' : 'd',
                        #     ' Which Nigerian artist won the Grammy Award for Best Global Music Album in 2021? a) Burna Boy b) Wizkid c) Davido d) Tiwa Savage' :'a',
                        #     ' The Lekki Toll Gate shooting during the #ENDSARS protests happened in which year? a) 2018 b) 2020 c) 2021 c) 2021 d) 2019' : 'b',
                        #     ' What is the capital of Nigeria? a) Lagos b) Port Harcourt c) Abuja d) Kano' : 'c',
                        #     ' Which Nigerian footballer recently signed a major deal with a European football club? a) Wilfred Ndidi b) Victor Oshimen c)Kelechi Iheanacho d) Samuel Chukwueze' : 'b',
                        #     ' The 2023 Nigerian Presidential election was held on what date? a) Februrary 25, 2023 b) March 10, 2023 c) April 1, 2023 d)January 31, 2023' : 'a',
                        #     ' Who is the current Minister of Foreign Affairs in Nigeria? a) Geoffrey Onyeama b) Zainab Ahmed c) Nyesom Wike d) Festus Keyamo' :'a',
                        #     ' The Nigerian national football team is also known as what? a) The Black Stars b) The Desert Warriors c)The Indomitable Lions d)The Super Eagles' : 'd',
                        #     ' Which state is the largest by population in Nigeria? a) Lagos b) Kano c) Kaduna d) Rivers' : 'a',
                        #     ' Who is the current Chief Justice of Nigeria (CJN)? a) Ibrahim Tanko Muhammad b) Walter Onnoghen c) Olukayode Ariwoola d) Mahmud Mohammed' : 'c'
                        #     }
                        # numbering = 0
                        # import random
                        # for question, answer in cbt_questions.items():
                        #     numbering+=1
                        #     quest = random.choice(list(cbt_questions.keys()))
                        #     print(f"{numbering} {quest}")
                        #     ans = input('Answer: ')
                        #     if ans == answer:
                        #         score+=1
                        #         percentage = round((score/15)*100)
                        # print(f'Dear, {name} you have {percentage}%')
#                     elif prompt_user.lower() == "no":
#                         print('You have terminated your test')
#                     else:
#                         print('You have not answered the question correctly')
#                 else:
#                     print('You have entered an invalid name or password!')
#                 # if registration < 10:
#                 #     # for students in user:
#                         # next_person = input('Is the next candidate ready to take the test? (Yes/No) ')
#                         # if next_person.lower() != "yes":
#                         #     print('You have terminated your test')


# student()


user = []
def register():
    for details in range(1, 11):
        print('''
                    1. Register
                    2. Login
        ''')
        ask_user = input("Select an option>>> ")
        if ask_user == "1":
            print("Enter your details in the form below to register yourself for the test")
            name = input("Enter your name: ")
            password = input("Create a password ")
            user_details = name, password
            user.append(user_details)
            print("You have successfully registered for the test")
        if ask_user == "2":
            print("Enter your details into the form below to login")
            registered_name = input('Enter your name: ')
            registered_password = input('Enter your password: ')
            registered_details = registered_name, registered_password
            if registered_details in user:
                prompt_user = input(f'{registered_name}, are you ready to take this test? (Yes or No) ')
                if prompt_user.capitalize() == 'Yes':
                    score = 0
                    cbt_questions = {
                        ' Who is the current President of Nigeria? a) Muhammadu Buhari b) Bola Ahmed Tinubu c) Yemi Osibanjo d) Goodluck Johnathan': 'b',
                        ' In what year did Nigeria gain independence from Britain? a) 1960 b) 1963 c) 1957 d) 1970' : 'a',
                        ' Which Nigerian state recently became the largest oil producer? a) Akwa Ibom b) Delta c) Rivers d) Lagos' : 'a',
                        ' Who is the current Governor of the Central Bank of Nigeria (CBN)? a) Godwin Emefiele b) Folashodun Shonubi c) Lamido Sanusi d) Zainab Ahmed' : 'b',
                        ' Which Nigerian University was recently ranked highest in Africa in Times Higher Education Marketing? a) University of Lagos b)University of Ibadan c) Covenant University d) Obafemi Awolowo University' : 'c',
                        ' The Nigerian national minimum wage was recently raised to what amount? a) #30,000 b) #50,000 c) #100,000 d) #70,000' : 'd',
                        ' Which Nigerian artist won the Grammy Award for Best Global Music Album in 2021? a) Burna Boy b) Wizkid c) Davido d) Tiwa Savage' :'a',
                        ' The Lekki Toll Gate shooting during the #ENDSARS protests happened in which year? a) 2018 b) 2020 c) 2021 c) 2021 d) 2019' : 'b',
                        ' What is the capital of Nigeria? a) Lagos b) Port Harcourt c) Abuja d) Kano' : 'c',
                        ' Which Nigerian footballer recently signed a major deal with a European football club? a) Wilfred Ndidi b) Victor Oshimen c)Kelechi Iheanacho d) Samuel Chukwueze' : 'b',
                        ' The 2023 Nigerian Presidential election was held on what date? a) Februrary 25, 2023 b) March 10, 2023 c) April 1, 2023 d)January 31, 2023' : 'a',
                        ' Who is the current Minister of Foreign Affairs in Nigeria? a) Geoffrey Onyeama b) Zainab Ahmed c) Nyesom Wike d) Festus Keyamo' :'a',
                        ' The Nigerian national football team is also known as what? a) The Black Stars b) The Desert Warriors c)The Indomitable Lions d)The Super Eagles' : 'd',
                        ' Which state is the largest by population in Nigeria? a) Lagos b) Kano c) Kaduna d) Rivers' : 'a',
                        ' Who is the current Chief Justice of Nigeria (CJN)? a) Ibrahim Tanko Muhammad b) Walter Onnoghen c) Olukayode Ariwoola d) Mahmud Mohammed' : 'c'
                        }
                    numbering = 0
                    import random
                    for question, answer in cbt_questions.items():
                        numbering+=1
                        quest = random.choice(list(cbt_questions.keys()))
                        print(f"{numbering} {quest}")
                        ans = input('Answer: ')
                        if ans == answer:
                            score+=1
                            percentage = round((score/15)*100)
                    print(f'Dear, {registered_name} you have {percentage}%'.center())
                    for person in user:
                        if details < 8:
                            next_person = input('Is the next student available for the test? (Yes/No) ')
                            if next_person.capitalize() == "Yes":
                                if registered_details:
                                    user.remove(registered_details)
                            else:
                                print('Test terminated')
                else:
                    print("You have canceled this test")
            else:
                print("You need to register to attempt the test")

register()