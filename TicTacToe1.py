# what each letter is in the functions
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# f = 6
# g = 7
# h = 8
# i = 9
# j = off of board, just to be funny

# functions
def board(a="_", b="_", c="_", d="_", e="_", f="_", g="_", h="_", i="_", j=""):
    # There's four endings
    win = False # beat the computer
    lose = False # get beat by the computer
    dub = False # take 3 corners and the number 10 spot
    rage = False # make the computer mad, by saying either X or O when it's your turn

    # Advanced Tracking, feature is being made later
    # how = "Unfortunately, I'm new and I don't know what happened. (._.) sorry..."
    patience = 0
    while win or lose or dub or rage is False:
        # board and plays
        print("\n/-----------\\\n|", a, "|", b, "|", c, "|\n|", d, "|", e, "|", f, "|    ", j, "\n|", g, "|", h, "|", i,
              "|\n\\-----------/")

        # win check
        if (a == "X" and d == "X" and g == "X") or \
                (b == "X" and e == "X" and h == "X") or \
                (c == "X" and f == "X" and i == "X") or \
                (a == "X" and b == "X" and c == "X") or \
                (d == "X" and e == "X" and f == "X") or \
                (g == "X" and h == "X" and i == "X") or \
                (a == "X" and e == "X" and i == "X") or \
                (c == "X" and e == "X" and g == "X"):
            lose = True
            break
        elif (a == "O" and d == "O" and g == "O") or \
                (b == "O" and e == "O" and h == "O") or \
                (c == "O" and f == "O" and i == "O") or \
                (a == "O" and b == "O" and c == "O") or \
                (d == "O" and e == "O" and f == "O") or \
                (g == "O" and h == "O" and i == "O") or \
                (a == "O" and e == "O" and i == "O") or \
                (c == "O" and e == "O" and g == "O"):
            win = True
            break
        # checks all four corners and outside for the easter egg
        elif a == "O" and c == "O" and (g == "O" or i == "O") and j == "O":
            dub = True
            break

        move = input("Pick a spot: ")  # Move is selected by user
        if move == "1":  # If the move is one
            if a == "_":
                a = "O"
                print("Okay, okay, lets see...")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif a == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:(")
                continue

        if move == "2":  # If the move is two
            if b == "_":
                b = "O"
                print("Hold on, hold on, I need to make a very high iq play...")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif b == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:(")
                continue

        if move == "3":  # If the move is three
            if c == "_":
                c = "O"
                print("Interesting... Uhh, how about here?")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif c == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:(")
                continue

        if move == "4":  # If the move is four
            if d == "_":
                d = "O"
                print("Uh huh...")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif d == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:(")
                continue

        if move == "5":  # If the move is five
            if e == "_":
                e = "O"
                print("Oh oh oh, I got this one!")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif c == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:(")
                continue

        if move == "6":  # If the move is six
            if f == "_":
                f = "O"
                print("Hmmmmm......")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif c == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:(")
                continue

        if move == "7":  # If the move is one
            if g == "_":
                g = "O"
                print("What!? Oh no, my plan is ruined.")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif c == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:(")
                continue

        if move == "8":  # If the move is eight
            if h == "_":
                h = "O"
                print("I'm still thinking--- nevermind...")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif c == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:(")
                continue

        if move == "9":  # If the move is nine
            if i == "_":
                i = "O"
                print("What are you doing?")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif c == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:(")
                continue

        if move == "10":  # now if the move is 10 and they want to really see an easter egg
            if j == "":
                j = "O"
                print("Uhh, did you mean to do that? Haha, okay. One less move for you I guess...")
                if d == "_":
                    d = "X"
                    continue
                elif b == "_":
                    b = "X"
                    continue
                elif i == "_":
                    i = "X"
                    continue
                elif a == "_":
                    a = "X"
                    continue
                elif j == "":
                    j = "X"
                    print("Dang, this game is really hard.")
                    continue
                elif c == "_":
                    c = "X"
                    continue
                elif e == "_":
                    e = "X"
                    continue
                elif h == "_":
                    h = "X"
                    continue
                elif f == "_":
                    f = "X"
                    continue
                elif g == "_":
                    g = "X"
                    continue
                else:
                    print("I'm all out of moves...")
                    continue
            elif j == "O" or j == "X":
                print("What are you doing? There's clearly a symbol there!")
                continue

        if move == "O":  # If move is O (Oh) or 0 (Zero)
            if patience == 0:
                print("Uh, so, uh, that's your token on the tic tac toe board.\n"
                      "There's no such thing as a Oh or Zero on the board.\n\n"
                      "You're lucky that I'm giving you another chance >:[")
                patience += 1
                continue
            elif patience == 1:
                print("Okay, let me explain again. Your OH or ZERO is you dang marker? "
                      "Are you getting what I am saying???")
                patience += 1
                continue
            elif patience == 2:
                print("*Sign*\n\nJust play the dang game.")
                patience += 1
                continue
            elif patience == 3:
                print("One more time and I ain't playing anymore...")
                patience += 1
                continue
            elif patience == 4:
                print("Last chance......")
                patience += 1
                continue
            elif patience >= 5:
                print("Okay, that's it... I'm done.")
                rage = True
                break

        if move == "X":  # If the move is his marker
            if patience == 0:
                print("That's my marker? Yours is the O. Now play please...")
                patience += 1
                continue
            elif patience == 1:
                print("Okay, X is my marker. Yours is the O. PLEASE PLAY")
                patience += 1
                continue
            elif patience == 2:
                print("Okay, look person I just want to play this game.\nplease play\n\npretty please. >:]")
                patience += 1
                continue
            elif patience == 3:
                print(">:( What the heck don't you understand about my marker and your marker?!\n"
                      "it's very simple, X's and O's\nit's not rocket science!!!")
                patience += 1
                continue
            elif patience == 4:
                print("Just put in a number between 1 through 9, PLEASE I BEG OF YOU")
                patience += 1
                continue
            elif patience == 5:
                print("PLEASE")
                patience += 1
                continue
            elif patience == 6:
                print("I BEG")
                patience += 1
                continue
            elif patience == 7:
                print(">:(\nI had enough, I am leaving...")
                rage = True
                break

        else:
            print("Can you stop talking gibber jabber and play the game???")

    if win is True:
        return print("Ugh. That game was a tough one. GG")
    elif lose is True:
        return print("You lost? Haha!")
    elif dub is True:
        return print(
            "You won. WAIT, YOU WON? How? Like is that even part of the rules?",
            "\n\nHow you won: Four corners and one on the outside.",
            "\nCongrats. You have won!")
    elif rage is True:
        return print("\n\nWell, it looks like you won by default...\nBut, I hope you feel bad!!! You made him mad! >:(")

    else:
        return print("What happened? An error occurred")

def wincheck(a="_", b="_", c="_", d="_", e="_", f="_", g="_", h="_", i="_", j="",
             win=False, lose=False, dub=False):
    if (a == "X" and d == "X" and g == "X") or \
            (b == "X" and e == "X" and h == "X") or \
            (c == "X" and f == "X" and i == "X") or \
            (a == "X" and b == "X" and c == "X") or \
            (d == "X" and e == "X" and f == "X") or \
            (g == "X" and h == "X" and i == "X") or \
            (a == "X" and e == "X" and i == "X") or \
            (c == "X" and e == "X" and g == "X"):
        lose = True
        return win, lose, dub
    elif (a == "O" and d == "O" and g == "O") or \
            (b == "O" and e == "O" and h == "O") or \
            (c == "O" and f == "O" and i == "O") or \
            (a == "O" and b == "O" and c == "O") or \
            (d == "O" and e == "O" and f == "O") or \
            (g == "O" and h == "O" and i == "O") or \
            (a == "O" and e == "O" and i == "O") or \
            (c == "O" and e == "O" and g == "O"):
        win = True
        return win, lose, dub
    # checks all four corners and outside for the easter egg
    elif a == "O" and c == "O" and (g == "O" or i == "O") and j == "O":
        dub = True
        return win, lose, dub


def winorlose(win=False, lose=False, dub=False):
    if win is True:
        return print("Ugh. That game was a tough one. GG")
    elif lose is True:
        return print("You lost? Haha!")
    elif dub is True:
        return print(
            "You won. WAIT, YOU WON? How? Like is that even part of the rules?",
            "\n\n How you won: Four corners and one on the outside.",
            "\nCongrats. You have won!")


# play code

# intro code

print(
    "Hi, I'm Bobby. I want to play you in this game I would like to call...",
    "\nTIC TAC TOE!\nNow let me tell you the rules.",
    "To put your marker on the board, you must simply say a number 1 - 9",
    "\n1 being the top left, and 9 being the bottom right.\n",
    "\n/-----------\\\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n\\-----------/",  # Example gameboard
    "\n\nLet's begin! You are O, and you go first!")  # Intro message

# game time code

board()
