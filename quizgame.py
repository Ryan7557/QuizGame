print('Welcome to the Quiz Game')

play = input("Do you wish to play? ")

if play.lower() != 'yes':
    quit()

count = 0
answer = input('What country begins with "Z" and ends with "e"? ')
if answer.lower() == 'zimbabwe':
    print('Correct')
    count += 1
else:
    print('Wrong!!')

answer = input('What is the most Communist country on Earth? ')
if answer.lower() == 'cuba':
    print('Correct')
    count += 1
else:
    print('Wrong!!')

answer = input('Which Brand is "BMW" from? ')
if answer.lower() == 'germany':
    print('Correct')
    count += 1
else:
    print('Wrong!!')

answer = input('What was the first counrty to do a heart transplant? ')
if answer.lower() == 'south africa':
    print('Correct')
    count += 1
else:
    print('Wrong!!')

print('You got ' + str(count) + ' points')