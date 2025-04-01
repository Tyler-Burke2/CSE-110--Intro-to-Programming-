
print("Hello, welcome to the chapel!")

name = input("What is your name? ")

if name == "Satan":
    print("Depart thee hence Satan!")
    exit()
else:
    print("Hello " + name + ", good to see you at church today!")

church = input("What are you most excited for at church today? 1st Hour or 2nd Hour? ")

if church == "1st Hour":
    print("Taking the sacrament IS important!")

elif church == "2nd Hour":
    print("I like seeing all of my friends there too!")

else:
    print("We only have 2 hours of church. Which one do you like more? <<RUN AGAIN>>")
