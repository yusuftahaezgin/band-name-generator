from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
bids={}

def find_high_bid(bidders): # en yuksek teklifi bulan fonksiyon
    max_bid=0
    winner_person=""
    for person in bidders:
        if bidders[person]>max_bid:
            max_bid=bidders[person]
            winner_person=person
    print(f"The winner is {winner_person} with a bid of ${max_bid}")


print(logo)
print("Welcome to the secret auction program.")

is_Finish=True
while is_Finish==True:
    name= input("What is your name?: ")
    bid= int(input("What's your bid?: $"))
    bids[name]= bid
    another_offer=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if another_offer=="yes":
        clear()
    else:
        is_Finish=False
        clear()
        find_high_bid(bids)

