# Variable initialisation
secret_number=9
guess_count=1
guess_limit=3

#Loop and condition

while guess_count<=guess_limit:
    number = int(input("Guess:"))
    if number==secret_number:
        print("You Win!!!")
        break
    guess_count+=1
else:
    print("You fail")

