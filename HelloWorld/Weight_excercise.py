Weight=int(input("Enter your weight: "))
unit=input("Enter the unit you want to choose in (L)bs or (K)gs: 1")

if unit.upper()=="L":
    print(f'You have choosen Lbs your weight is {Weight}')
else:
    print(f"You have choosen Kg your weight is {Weight}")