started=False
stopped=False
while True:
    command=input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            print("Car has started....Ready to go!")
            started= True
            stopped=False
    elif command== "stop":
        if stopped:
            print("car has aleady stopped")
        else:
            print("Car stopped")
            stopped=True
            started=False
    elif command=="quit":
        print("programm ended")
        break
    else:
        print("I don't understand that....")


