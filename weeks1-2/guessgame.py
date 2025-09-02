import random
print('Guess Game; Try your luck!!')
secret_number = random.randint(1, 10)
user_number = int(input('Input your lucky number from 1 to 10 here: '))
number_of_tries = 1
while user_number !=secret_number:
    if user_number < secret_number :
        print(user_number, 'Number is too low,')
    if user_number > secret_number:
        print(user_number, 'Number is too high')
    user_number = int(input('Oops, Try Again: '))
print('Yes 👍 !! the Super Secret Number was: '
      , user_number, 'Great, You won!')