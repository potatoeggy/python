def user_input():
    global userinput
    userinput = input('Enter an integer: ')
    try:
        global int_input
        int_input = int(userinput)
        odd_even(int_input)
        print('Its divisors are ' + divisors(int_input))

    except ValueError:
        print('\"' + userinput + '\"' + ' is not an integer. Try again.')
        user_input()

def odd_even(var):
    if var % 2 == 0:
        print(userinput + ' is even.')
    else:
        print(userinput + ' is odd.')

def divisors(var):
    x = 1
    temp = '1'
    while x <= var / 2:
        x = x + 1
        if var % x == 0:
            if x != var:
                temp = temp + ', ' + str(x)
            else:
                break
    if temp != 1:
        temp = temp + ', ' + str(var)
    return temp
            

user_input()
