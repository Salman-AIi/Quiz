
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

question_1 = input('Which is the largest ocean in the world?' + '\n')

if question_1 =='pacific' or 'Pacific' or 'pacific ocean' or 'Pacific ocean':
    print('correct!') 
else:
    print('Wrong!')
    print('Press enter for the next question.')


