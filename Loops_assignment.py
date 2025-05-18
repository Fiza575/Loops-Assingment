    # Task no 1 (Using a for Loop)
for number in range(1,11):
    print(number)

 #Task no 2 (While Loop)

    number = 1
    while number <=5:
      print(number)
      number+=1

    # Task no 3 (Loop with Condition)

number =int(input("Enter a number:"))
while number >=1:
    print(number)
    number -=1

# Task no 4 (Nested loop)
count = 1
for a in range(1,4):
   for b in range(1,4):
    print(f"{count},{a}x{b}={a*b}")
    count +=1

# Task no 5 (Using break)

for number in range(0,11):
   if number ==6:
      break
   print(number)

# Task no 6 (Using continue)

for e in range(0,6):
   if e ==3:
      continue
   print(e)

# (Bonus Task: Count the Letters)

word =str(input("Please Enter a word:"))
for letter in word:
   print(letter)