print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))

bill_with_tip= (tip/100)*bill+bill
bill_per_person= bill_with_tip/people

# two_digit_number= round(bill_per_person,2)

two_digit_number = "{:.2f}".format(bill_per_person) # ustteki sekilde yuvarlamada .60 gibi ilk sayıdan sonrası 0 olan sayılarda 0 ı gostermiyordu ornegin 33.60 gostermesi gerekirken 33.6 gosteriyordu, round fonksiyonunda virgulden sonra 2 basamak goster dememize ragmen gostermiyordu bizde 0 olunca da gostermesi icin formatlama islemi yaptık

print(f"Each person should pay: ${two_digit_number}")