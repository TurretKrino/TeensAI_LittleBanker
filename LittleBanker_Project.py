userPoints = 650
budget = 20
moneySpent = 120


def menu():
    choice = int(input("Choose Save, Budget, Or Points (1,2 or 3): "))
    if choice == 1:
        save()

    elif choice == 2:
        budget()

    else:
        print("Number of points:",userPoints)
        menu()



def save():
    choice = int(input("Choose Story Mode or How to Play (1 or 2): "))
    if choice == 1:
        storyMode()
    elif choice ==2:
        userGuide()


def budget():

    choice = int(input("Choose Current Budget or Money Spent (1 or 2): "))
    if choice == 1:
        print("Current Budget:",budget,"dollars")
    elif choice == 2:
        print("Money Spent:",moneySpent,"dollars")
    menu()

def storyMode():
    userPoints = 650
    choice=int(input("You need a new pen for class. But there are some candies in the shop next door. Will you buy the pen, the candies, or save your money? (1,2,3): "))
    if choice == 1:
       userPoints += 100
    elif choice == 2:
        userPoints-= 50
    elif choice ==3:
        userPoints+=25
    print("You now have",userPoints,"points")



def userGuide():
    print("Welcome to LittleBanker! LittleBanker teaches you how to save and spend money the right way! Choose decisions and earn points. Remember - spend responsibly! Have fun!")
    menu()


menu()
