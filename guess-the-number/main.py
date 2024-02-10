#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from replit import clear
import random

def attempts(choosen_level):
    if choosen_level=="easy":
        return 10
    elif choosen_level=="hard":
        return 5
    else:
        return -1 # easy veya hard dısında bir deger girerse kullanıcı hata versin ve while dongusune de girmesin diye -1 verdim


def compare(user_guess,number):
    if user_guess==number:
        return 1
    elif user_guess>number:
        return "Too high."
    elif number>user_guess:
        return "Too low."

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer=random.randint(1,100)
    #print(f"The correct answer: {answer}")
    difficulty=input("Choose a difficulty.Type 'easy' or 'hard': ")
    number_of_attempts= attempts(difficulty)
    if number_of_attempts==-1:
        print("Wrong selection!")
    while number_of_attempts>0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_number=int(input("Make a guess: "))
        user_compare=compare(user_number,answer)
        if user_compare==1:
            print(f"Congratulations, you found the number {answer}!")
            number_of_attempts=-5
        else:
            if number_of_attempts==1:
                print(user_compare)
            else:
                print(user_compare)
                print("Guess again.")
            number_of_attempts-=1
            
    if number_of_attempts==0:
        print("Your attempt is over, you lose :(")


game()

