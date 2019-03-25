
print('This is a quiz!')
print('See how well you score!')
name = input("Enter Your Name:")
print("\t")
print("Hello and welcome to the quiz!:" + "--" + name + "!" + "--")
print("\t")
print("The quiz will have 3 questions!")
print("\t")
print('You will have three guesses to each question!')
print("\t")
print("DO NOT CHEAT" + "\t" + "press enter to start")
input()



#Question 1

question_1 = input('Which is the largest ocean in the world?' + '\n')

if question_1 =='pacific' or question_1 =='Pacific' or question_1 =='pacific ocean' or question_1 =='Pacific ocean':
    grading_1 = '1_1'

    print('\n')
    print('Brilliant!')
    print('Press Enter For The Next Question!') 
    input()
else:
    grading_1 = '1_0'

    print('Wrong!,That Was A Hard One!')
    print('Press enter for the next question.')
    input()

#Question 2

question_2 = input('Where is the worlds largest house located?' + '\n')

if question_2 =='mumbai' or question_2 =='Mumbai' or question_2 =='Bombay' or question_2 =='bombay':
    grading_2 = '2_1'
 
    print('Thats Right,Keep it up!')
    print('Press Enter For The Last Question!')
    input()
else:
    grading_2 = '2_0'
 
    print('Wrong!Do Better Next Time!.')
    print('Press enter fo your last question.')
    input()

#Question 3

question_3 = input('What is the smallest country in the world?' + '\n')

if question_3 == 'vatican' or question_3 == 'vatican city' or question_3 == 'Vatican' or question_3 == 'Vatican city' or question_3 == 'Vatican City':
    grading_3 = '3_1'
 
    print('Thats Right!,Good Job!')
    print('Press Enter To Get Your Grades!')
    input()
else:
    grading_3 = '3_0'
 
    print('The Answer Was: Vatican City')
    print('Press Enter To Get Your Grades!')
    input()
#####################################################################
if grading_1 == '1_1' and grading_2 == '2_1' and grading_3 == '3_1':
    print ('U Got Full Marks!')
    print('3/3!' + '\n')
    print('You Are A Genius!')

######################################################################

if grading_1 == '1_0' and grading_2 == '2_1' and grading_3 == '3_1':
    print ('U Got A 2/3!' + '\n')
    print('You Are Good!')    

if grading_1 == '1_1' and grading_2 == '2_0' and grading_3 == '3_1':
    print ('U Got A 2/3!' + '\n')
    print('You Are Good!')    

if grading_1 == '1_1' and grading_2 == '2_1' and grading_3 == '3_0':
    print ('U Got A 2/3!' + '\n')
    print('You Are Good!')  

######################################################################

if grading_1 == '1_0' and grading_2 == '2_0' and grading_3 == '3_1':
    print ('U Got A 1/3!' + '\n')
    print(':(' + '\n')
    print('You Need Practice!')
    
if grading_1 == '1_0' and grading_2 == '2_1' and grading_3 == '3_0':
    print ('U Got A 1/3!' + '\n')
    print(':(' + '\n')
    print('You Need Practice!')  

if grading_1 == '1_1' and grading_2 == '2_0' and grading_3 == '3_0':
    print ('U Got A 1/3!' + '\n')
    print(':(' + '\n')
    print('You Need Practice!')   

#####################################################################

if grading_1 == '1_0' and grading_2 == '2_0' and grading_3 == '3_0':
    print ('U Got A 0/3!' + '\n')
    print(':(' + '\n')
    print('Do Better Next Time!')


