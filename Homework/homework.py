# EXERCISE 1
# Q1
x=0
y=0
z=0
if x==5:
    if y<6:
        if z<=11:
            print("nothing")
        else:
            print(2)
    else:
        print(1)
else:
    if y>3:
        print(3)
    else:
        print("nothing")

#Q2
x=0
y=0
if x>4:
    if y>3:
        print("nothing")
    else:
        print(3)
else:
    if y<2:
        print("nothing")
    else:
        print(1)

# EXERCISE 2
nbRepeat=5
for i in range(5):
    print("Hello Word")

# EXERCISE 3
number=int(input("Please enter number: "))
while number>5:
    print(number)
    number=number-2

# EXERCISE 4
user_name=str(input("Please enter your name: "))
age=int(input("Please enter your age: "))
print("My name is",user_name,",I am",age,"years old.")

# EXERCISE 5
userMessage=int(input("Please enter number"))
if userMessage<0:
    print("Negative Number!")
else:
    print("Positive Number!")

# EXERCISE 6
# Q1
number=0
if number < 25:
    print("Dog")
elif number <= 30:
    print("Cat")
else:
    print("Cow")
# To see "Cat" number must be in the range:-infinity,30

# Q2
number=31
if number < 25:
    print("Dog")
elif number <= 30:
    print("Cat")
else:
    print("Cow")
# To see "Cow" number must be in the range:31,+infinity

# EXERCISE 7
# Q1
value=10
if value >= 5:
    print("Apple")
elif value <= 10:
    print("Banana")
# if value equal to 10,will be print: Banana

# Q2
value=10
if value >= 5:
    print("Apple")
elif value <= 10:
    print("Banana")
# Which problem/instruction this code is solving?
# elif value <= 10 :
#     print("Banana")

# EXERCISE 8
# Q1
value=10
if value >10:
    print("Red")
elif value <= 10:
    print("Blue")
#  if value equal to 10,will be print: Blue

# Q2
value=10
if value >10:
    print("Red")
elif value <= 10:
    print("Blue")
# Which problem/instruction this code is solving?
# All code

# EXERCISE 9
text=str(input("Please enter text"))
total=0
for i in range(len(text)):
    total+="x"
print(total)

# EXERCISE 10
word=str(input("Please enter word: "))
number=int(input("Please enter number: "))
if word=="good" and number>=7 or number<=15:
    print("It's good")
elif word=="bed" and number<7 or number>15:
    print("It's bed")








    

    



        