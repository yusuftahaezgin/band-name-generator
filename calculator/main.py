#Calculator
from replit import clear  # clear fonk kullanmak icin ekledik
from art import logo


def add(n1, n2):  #toplama
    return n1 + n2


def subtract(n1, n2):  #cıkarma
    return n1 - n2


def multiply(n1, n2):  #carpma
    return n1 * n2


def divide(n1, n2):  #bolme
    return n1 / n2


def exponent(n1, n2):  #üs alma
    return n1**n2


math_signs = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent
}


def calculator():  # ozyinelemeli fonksiyon!
    print(logo)
    num1 = float(input("What's the first number?: "))
    for sign in math_signs:
        print(sign)

    isRepeat = True
    while isRepeat:
        choose_sign = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        cal_function = math_signs[choose_sign]
        answer = cal_function(num1, num2)
        print(f"{num1} {choose_sign} {num2} = {answer}")

        repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. (For exit 'e'):  "
        )
        if repeat == "y":
            num1 = answer

        elif repeat == "n":
            isRepeat = False
            clear()
            calculator()  # burada kullanıcı 'n' derse while dan cıkar ancak program sonlanmasın sıfırdan yeni sayılarla hesaplama yapması icin tekrar fonksiyonu cagırdık ve en bastan baslattık buna ozyineleme(fonksiyonun icinde kendi kendini cagirmasi) denir. burda eger kontrollerle fonksiyonu kendi icinde cagirmazsak sonsuz donguye girer buna dikkat et!!!

        else:  # programdan cıkıs yapma
            isRepeat = False
            print("Goodbye!")


calculator()