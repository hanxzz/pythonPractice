print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("youth tickets are $7.")
        bill = 7
    else:
        print("adults tickets are $12.")
        bill = 12
    wantPhoto = input("do you want photo. y for yes n for no")
    if wantPhoto == 'y':
        bill+=3
    print(f"Your bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
