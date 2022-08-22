import random


def sys(scoreS, scoreU):
    # system
    li = ["Rock", "Paper","Scissor"]
    ran_lis = random.choice(li)
    print(ran_lis)

    # user
    user = input("Choose and type: Rock , Paper , Scissor: ")

    if ran_lis == user:
        print("system win count:", scoreS)
        print("user win count :", scoreU)
        print("==")
        sys(scoreS, scoreU)
    else:
        cap = user.capitalize()
        if (ran_lis == "Rock" and cap == "Paper") or (ran_lis == "Paper" and cap == "Scissor") or (ran_lis == "Scissor" and cap == "Rock"):
            # print("ScoreU")
            scoreU += 1

        elif (ran_lis == "Rock" and cap == "Scissor") or (ran_lis == "Paper" and cap == "Rock") or (ran_lis == "Scissor" and cap == "Paper"):
            # print("scoreS")
            scoreS += 1

        else:
            print("invalid Choice")

        occurS = int(scoreS)
        U_occur = int(scoreU)
        while occurS < 2 and U_occur < 2:
            print("system win count:", scoreS)
            print("user win count :", scoreU)
            print("")
            sys(scoreS, scoreU)

        if scoreS == 2:
            print("sys winner")

        elif scoreU == 2:
            print("user is winner")
            print("")
    cont = input("do you want to play again?[y/n]:  ")
    if cont == 'y' or cont == 'Y':
        sys(0, 0)

    elif cont == 'n' or cont == 'N':
        print("exit")
        exit()
    else:
        print("invalid choice")

sys(0,0)
