
age = int(input('Enter your age: \n'))
nights = int(input('Enter nights: \n'))
rate = 0
cost = 0

if age < 18:
    print('You are too young to rent a room.')
else:
    if age <= 25:
        rate = 200
    elif age <= 64:
        rate = 150
    else:
        rate = 120

    cost = nights * rate

    print('Your nightly rate is: ${:.2f}'.format(rate))
    print('Your total cost is: ${:.2f}'.format(cost))