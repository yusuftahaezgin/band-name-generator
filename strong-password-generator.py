#Password Generator Project

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# num_letters= int(input("How many letters would you like in your password?\n")) 
# num_symbols = int(input("How many symbols would you like?\n"))
# num_numbers = int(input("How many numbers would you like?\n"))



# for letter in range(1,num_letters+1):
#   rand=random.randint(0,51)
#   rand_letter=letters[rand]
#   print(rand_letter,end="")

# for symbol in range(1,num_symbols+1):
#   rand_for_symbols=random.randint(0,8)
#   rand_symbol=symbols[rand_for_symbols]
#   print(rand_symbol,end="")

# for number in range(1,num_numbers+1):
#   rand_number=random.randint(0,9)
#   print(rand_number,end="")

# bu sekil kolay kodda yazdırırsak sıralı yazdıracaktır yani ilk basta girdigimiz sayı kadar random harf getirecek sonra girdigimiz sayı kadar random sembol getirecek en son ise girdigimiz sayı kadar random sayı getirecek yani sifrenin sırası hep harf/sembol/sayı seklinde olur bu da cok guvenli bir sifre olmaz simdi alttaki kodda bu sırayı da random yaptık

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))


password_list= []
for letter in range(1,num_letters+1):
  rand=random.randint(0,51)
  rand_letter=letters[rand]
  password_list.append(rand_letter)

for symbol in range(1,num_symbols+1):
  rand_for_symbols=random.randint(0,8)
  rand_symbol=symbols[rand_for_symbols]
  password_list.append(rand_symbol)

for number in range(1,num_numbers+1):
  rand_for_number=random.randint(0,9)
  rand_number=numbers[rand_for_number]
  password_list.append(rand_number)

random.shuffle(password_list) #sırası harf/sembol/sayı olan sifreyi password_list diye bir lsiteye attık ve shuffle fonksiyonunu kullanarak bu sırayı da random yaptırdık simdi sifre cok daha guvenli oldu
#print (password_list)

#simdi bu listeyi (string seklinde) son kullanıcıya verilecek cıktı seklinde yazdıralım
password=""
for x in password_list:
  password+=x

print(f"Here is a strong password for you: {password}")