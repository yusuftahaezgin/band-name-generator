rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game_images=[rock,paper,scissors]
user_choose= int(input("What do you choose? Type 0 for rock,1 for Paper or 2 for Scissors.\n"))

if user_choose>2 or user_choose<0:
  print("You entered a number that does not exist, please try again.")
else:
  options_name=["Rock","Paper","Scissors"]

  user_opt_name=options_name[user_choose]

  print("You chose: "+user_opt_name)
  print(game_images[user_choose])


  computer_choose= random.randint(0,2)
  computer_opt_name=options_name[computer_choose]

  print("Computer chose: "+computer_opt_name)
  print(game_images[computer_choose])


  lose="You lose!"
  win = "You win!"
  draw="It's a draw."

  if computer_choose==1 and user_choose==0:
    print(lose)
  elif computer_choose==2 and user_choose==1:
    print(lose)
  elif computer_choose==0 and user_choose==2:
    print(lose)
  elif computer_choose==user_choose:
    print(draw)
  else:
    print(win)
    
# made by yusuf taha ezgin
  

