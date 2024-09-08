# import
from random import randint
import time

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
class tic():
    def __init__(self):
        self.move=0

    def board(a="_", b="_", c="_", d="_", e="_", f="_", g="_", h="_", i="_", j="", win=False, lose=False, dub=False):

        print("\n/-----------\\\n|", a, "|", b, "|", c, "|\n|", d, "|", e, "|", f, "|    ", j, "\n|", g, "|", h, "|", i,
              "|\n\\-----------/") # board

        move = input("Pick a spot: ")  # Move is selected by user

        if move == "1":  # If the move is one
            if a == "_":
                a = "O"
                return wincheck(a, b, c, d, e, f, g, h, i, j)
            # continue
        elif a == "O" or "X":
            print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)

        elif move == "2":  # If the move is two
            if b == "_":
                b = "O"
                return wincheck(a, b, c, d, e, f, g, h, i, j)
            elif b == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)

        elif move == "3":  # If the move is three
            if c == "_":
                c = "O"
                return wincheck(a, b, c, d, e, f, g, h, i, j)
            elif c == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)

        elif move == "4":  # If the move is four
            if d == "_":
                d = "O"
                return wincheck(a, b, c, d, e, f, g, h, i, j)
            elif d == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)

        elif move == "5":  # If the move is five
            if e == "_":
                e = "O"
                print("Oh oh oh, I got this one!")
                return wincheck(a, b, c, d, e, f, g, h, i, j)
            elif e == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)

        elif move == "6":  # If the move is six
            if f == "_":
                f = "O"
                return wincheck(a, b, c, d, e, f, g, h, i, j)
            elif f == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)

        elif move == "7":  # If the move is one
            if g == "_":
                g = "O"
                return wincheck(a, b, c, d, e, f, g, h, i, j)
            elif g == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)


        elif move == "8":  # If the move is eight
            if h == "_":
                h = "O"
                return wincheck(a, b, c, d, e, f, g, h, i, j)
            elif h == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)

        elif move == "9":  # If the move is nine
            if i == "_":
                i = "O"
                wincheck(a, b, c, d, e, f, g, h, i, j)
            elif i == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)

        elif move == "10":  # now if the move is 10 and they want to really see an easter egg
            if j == "":
                j = "O"
                print("Uhh, did you mean to do that? Haha, okay. One less move for you I guess...")
                return wincheck(a, b, c, d, e, f, g, h, i, j)
            elif i == "O" or "X":
                print("Pick another spot... Stop cheating!!!!! >:("), board(a,b,c,d,e,f,g,h,i,j)

            else:
                print("Can you stop talking gibber jabber and play the game???"), board(a,b,c,d,e,f,g,h,i,j)


def botmoves(k="_", l="_", m="_", n="_", o="_", p="_", q="_", r="_", s="_", t=""):
    if o == "_":
        o = "X"
        return print("Hmmmmm......"), board(k, l, m, n, o, p, q, r, s, t)
    elif l == "_":
        l = "X"
        return print("Hold on, hold on, I need to make a very high iq play..."), board(k, l, m, n, o, p, q, r, s, t)
    elif s == "_":
        s = "X"
        return print("I'm still thinking--- nevermind..."), board(k, l, m, n, o, p, q, r, s, t)
    elif k == "_":
        k = "X"
        return print("Interesting... Uhh, how about here?"), board(k, l, m, n, o, p, q, r, s, t)
    elif t == "":
        t = "X"
        return print("Oh my, this game is hard"), board(k, l, m, n, o, p, q, r, s, t)
    elif m == "_":
        m = "X"
        return print("What are you doing?"), board(k, l, m, n, o, p, q, r, s, t)
    elif n == "_":
        n = "X"
        return print("Oh my..."), board(k, l, m, n, o, p, q, r, s, t)
    elif r == "_":
        r = "X"
        return board(k, l, m, n, o, p, q, r, s, t)
    elif q == "_":
        q = "X"
        return board(k, l, m, n, o, p, q, r, s, t)
    elif p == "_":
        p = "X"
        return print("Uh huh..."), board(k, l, m, n, o, p, q, r, s, t)
    else:
        return print("I'm all out of moves...")


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
        return winorlose(win,lose,dub)
    elif (a == "O" and d == "O" and g == "O") or \
            (b == "O" and e == "O" and h == "O") or \
            (c == "O" and f == "O" and i == "O") or \
            (a == "O" and b == "O" and c == "O") or \
            (d == "O" and e == "O" and f == "O") or \
            (g == "O" and h == "O" and i == "O") or \
            (a == "O" and e == "O" and i == "O") or \
            (c == "O" and e == "O" and g == "O"):
        win = True
        return winorlose(win,lose,dub)
    # checks all four corners and outside for the easter egg
    elif a == "O" and c == "O" and g == "O" and i == "O" and j == "O":
        dub = True
        return winorlose(win,lose,dub)
    else:
        return botmoves(a,b,c,d,e,f,g,h,i,j)


def winorlose(win=False, lose=False, dub=False):
    if win is True:
        return print("Ugh. That game was a tough one. GG"), message(win,lose,dub)
    elif lose is True:
        return print("You lost? Haha!"), message(win,lose,dub)
    elif dub is True:
        return print(
            "You won. WAIT, YOU WON? How? Like is that even part of the rules?",
            "\n\n How you won: Four corners and one on the outside.",
            "\nCongrats. You have won!"), message(win,lose,dub)

def message(win, lose, dub, w1=0, l1=0, d1=0):
    if win == True:
        w1+=1
        win = False

    elif lose == True:
        l1+=1
        lose = False

    elif dub == True:
        d1+=1
        dub = False

    inp = input(print("\nYour current status is:\nWins: ",w1,"\nLoses: ",l1,"\nSecret Wins:",d1,
      "\n\nWant to play again?:"))

    if "y" in inp:
        return board()
    elif "n" in inp:
        return print('\nThanks for playing!')
    else:
        print("\nsorry, what was that?"), message(win,lose,dub)


# play code

print(
    "Hi, I'm Gage Ward. I want to play you in this game I would like to call...",
    "\nTIC TAC TOE!\nNow let me tell you the rules.",
    "To put your marker on the board, you must simply say a number 1 - 9",
    "\n1 being the top left, and 9 being the bottom right.\n",
    "\n/-----------\\\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n\\-----------/",  # Example gameboard
    "\n\nLet's begin! You are O, and you go first!")  # Intro message

# game time code

board = tic()
board()
