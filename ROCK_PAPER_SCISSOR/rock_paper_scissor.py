import random


# rock, paper and scissors
def gameWin(comp, you):
# computer and user choose same
    if comp == you:
        return None

# computer choose rock
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

# computer choose paper
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return  True

# computer choose scissors
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True


print("computer choose between: rock(r), paper(p) and scissors(s)")
print("")
ranNo = random.randrange(1, 3)
if ranNo == 1:
    comp = 'r'
elif ranNo == 2:
    comp = 'p'
elif ranNo == 3:
    comp = 's'

you = input("User choose between: rock(r), paper(p) and scissors(s)")
print("")
a = gameWin(comp , you)




print("computer choose {}".format(comp))
print("you choose {}".format(you))

if a == None:
    print('game is tie')
elif a:
    print('you won!')
else:
    print('you lose!')
