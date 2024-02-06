alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(entry_text, entry_shift, entry_direction):
    new_word = ""
    if entry_direction == "decode":
      entry_shift *= -1
    for char in entry_text:
        if char in alphabet:
            index= alphabet.index(char)
            new_index= index+entry_shift
            new_letter=alphabet[new_index]
            new_word+=new_letter
        else:
            new_word+=char
        
    
    print(f"Here's the {entry_direction}d result: {new_word}")

from art import logo
print(logo)

is_Repeat=True
while is_Repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift= shift%26 #kaydırmak icin kullanıcı cok buyuk sayı girerse dye 26 ya modunu aldık aynı sekil sorunsuz calısır cunku alfabe sayısına modunu aldık buyuk sayıyla islem yapacagımıza kalanla yapıyoruz aynı kaydırma islemine denk gelir
    caesar(text, shift, direction)

    result=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result=="no":
        is_Repeat=False
        print("Goodbye!")