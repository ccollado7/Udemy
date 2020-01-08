#This program says hello and ask for my name

print("Hello world")

#Part pf the program that ask for you Name

print("What is your name?") #Ask for your name
myName = input()
print("It is good to meet you, " + myName)
print("The lenght of your name is:")
print(len(myName))


#Part of the program that ask for your Age

print("What is yor age?") #Ask for your age
myAge = input()
print("You will be "+ str(int(myAge) + 1)+ " in a year")
