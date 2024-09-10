import art
print(art.logo)
bids = {}
def find_high_bid():
    max_bid=0
    winner_person=""
    for person in bids:
        if max_bid < bids[person]:
            max_bid =bids[person]
            winner_person=person

    print(f"Max bid is ${max_bid} and winner is {winner_person}")

is_Finish=False
while is_Finish!=True:
    name=input("What is your name?: ")
    bid=input("What is your bid?: $")
    bids[name] =int(bid)
    another_offer=input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if another_offer=="yes":
        print("\n"*300)
    elif another_offer=="no":
        is_Finish= True
        find_high_bid()

