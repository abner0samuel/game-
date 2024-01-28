
a = 68
b = 3
print(f"{0:b}{a}")
print(int(1000100))
print(a|b)




from random import randint
number = int(input('enter a number : '))
answer = randint(0,number)
guess1 = []
while True:
    guess = int(input ('guess  the random number : '))
    guess1.append(guess)
    for value in guess1:
        if guess1.count(value) == 2:
            print('you have already try this number')     
    if guess == answer:
        print('you are correct...')
        break
    elif guess < answer:
        print('you failed guess higher...')
    elif guess > answer:
        print('you failed guess lower...')
    else:
        continue