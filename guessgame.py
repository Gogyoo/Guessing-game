#Wishlist: add a counter and a message if you get it on the first guess

from sys import exit
from random import randint
 
# Players guess a number and the program tests its validity.
def input_check(rand_n):
    user_guess = raw_input("Enter a number between 1 and 1000.\n>")
    try:
		user_guess = int(user_guess)
		results(user_guess, rand_n)      
    except ValueError:
       print "Remember: only positive numbers from 1 to  1000 included."
            input_check(rand_n)
    if user_guess == 0 or user_guess > 1000:
        print "Between 1 and 1000.\nTake your time.You can do it."
        input_check(rand_n)
     else:
            results(user_guess, rand_n)
 
# Compares input with random number, taking appropriate course of action
# through (more) branching.
def results(guess, rand_n):
    while True:
        if guess == rand_n:
            restart()
        elif guess < rand_n:
            print "Too low!"
            input_check(rand_n)
        elif guess > rand_n:
            print "Too high!"
            input_check(rand_n)
 
# Players can now exit the program or try it again.
def restart():
    again = raw_input("GG! Wanna rematch?\n>")
    yes = ["y", "Y", "Yes", "yes", "Yeah", "yeah"]
    # pdb.set_trace()
    if again in yes:
        print "It's on!"
        start()
    else:
    print "Back to the shell. See you later!"
        exit(0)
 
def start():
    rand_n = randint(1,1000)
    print rand_n
    input_check(rand_n)
 
# Prints an opening statement about the game
print "Hi! How would you like to guess a number that I just thought of?"
start()
