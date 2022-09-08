import random
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random = random.choice(list1)

#guessing mechanism
while True:
    user_input = input('guess the number>')
    if int(user_input) == random:
        print('right')
        break
    if int(user_input) != random:
        print('guess again')

