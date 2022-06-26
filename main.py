#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

sınır1=0
harf=""
for letter in letters:
  if nr_letters>sınır1:
    sınır1+=1
    harf+=random.choice(letters)

sınır2=0
sembol=""
for symbol in symbols:
  if nr_symbols>sınır2:
    sınır2+=1
    sembol+=random.choice(symbols)

sınır3=0
sayı=""
for number in numbers:
  if nr_numbers>sınır3:
    sınır3+=1
    sayı+=random.choice(numbers)
password=harf+sembol+sayı
char_list=list(password)

shuffled_list=random.sample(char_list,len(char_list))
shuffled_password="".join(shuffled_list)
print(shuffled_password)
