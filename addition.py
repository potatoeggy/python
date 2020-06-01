# Daniel Chen
# 7 April 2019
# Addition

x = 19
def for_addition(x):
    temp = 0
    for x in range(1, x + 1):
        temp = temp + x
    print(temp)

def if_addition(x):
    temp = 0
    if x % 2 == 0:
        temp = int((1 + x) * (x / 2))
    elif x == 1:
        temp = 1
    else:
        temp = int(1 + x) * (x / 2) + (x / 2 + 0.5)
    print(temp)

# for x in range(x):
for_addition(x)
if_addition(x)