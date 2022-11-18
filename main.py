#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for x in range(0, 5):
llist = []
slist = []
nlist = []
for i in range(0, nr_letters):
  pos = random.randint(0, len(letters)-1)
  llist.append(letters[pos])
for i in range(0, nr_symbols):
  pos = random.randint(0, len(symbols)-1)
  slist.append(symbols[pos])
for i in range(0, nr_numbers):
  pos = random.randint(0, len(numbers)-1)
  nlist.append(numbers[pos])
  # print('-------------------------')  
  # print(llist)
  # print(slist)
  # print(nlist)
  # print('-------------------------')  
pwdstr = ''
for i in llist:
  pwdstr += i
for i in slist:
  pwdstr += i
for i in nlist:
  pwdstr += i
print(pwdstr)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
fulllist = llist + slist + nlist
pwdstr = ''
for i in range(0, len(fulllist)):
  pos = random.randint(0, len(fulllist) - 1)
  pwdstr += fulllist[pos]
print(pwdstr)