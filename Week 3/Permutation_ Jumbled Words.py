"""
Player 1 and Player 2 are in the game
Player 1 post a jumbled word and player 2 need to find the answer
and vice-versa

"""
import random


def choose():
    words = ["rainbow", "computer", "science", "programming", "mathematics", "player", "reverse", "water", "board"]
    pick = random.choice(words)
    return pick


def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled


def thank(p1name, p2name, pp1, pp2):
    print(p1name, "Your Score is : ", pp1)
    print(p2name, "Your score is : ", pp2)
    print("Thanks for playing ")
    print("Have a nice day! ")


def play():
    p1name = input("Player 1, Please enter your name ")
    p2name = input("Player 2, Please enter your name ")
    pp1 = 0  # Player 1 initial point
    pp2 = 0
    turn = 0  # Initial turn
    while (1):
        # Computer's task
        picked_word = choose()
        # Create the question
        qn = jumble(picked_word)
        print(qn)

        # Player 1

        if turn % 2 == 0:
            print(p1name, "Your turn. ")
            answer = input("What is on my mind? ")
            if answer == picked_word:
                pp1 = pp1 + 1
                print("Your score is ", pp1)
            else:
                print("Better luck next time. I thought: ", picked_word)

            c = input("Press 1 to continue and 0 to quit ")
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break

        # Player 2
        else:
            print(p2name, "Your turn. ")
            answer = input("What is on my mind? ")
            if answer == picked_word:
                pp2 = pp2 + 1
                print("Your score is", pp2)
            else:
                print("Better luck next time. I thought: ", picked_word)

            c = input("Press 1 to continue and 0 to quit ")
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break
        turn = turn + 1


play()
