from random import randrange

def learnIntegerDivision():
    a = randrange(9)
    b = randrange(9)
    c = a*b
    try:
        ans = input("{} / {} = ".format(c, a))
        if int(ans) == (c // a):
            print("CORRECT!")
        else:
            print("INCORRECT!")
    except ValueError:
        print("Please enter Integers Only!")
    except Exception as e:
        print(type(e))
        print(e.args)
        print(e)

print("INTEGER DIVISIONS")

for i in range(8):
    learnIntegerDivision()
