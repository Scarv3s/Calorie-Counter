print("Welcome to the wonderful daily point tracker!")

def meals():
    total = 0
    print("Did you eat a home-cooked meal?")
    answer = input("Type 1 for Yes; Type 2 for No: ")
    if answer == "1":
        print("Great choice!")
        print("Was it a balanced meal?")
        answer2 = input("Type 1 for Yes; Type 2 for No: ")
        if answer2 == "1":
            total = total + 10
            print("There we go!")
        else:
            total = total + 7
    else:
        print("Was it a healthy choice?")
        answer3 = input("Type 1 for Yes; Type 2 for No: ")
        if answer3 == "1":
            print("Good Job!")
            total = total + 5
        else:
            total = total - 5
    return total

meals()
print('Your total balance for today is ' + str(total))
end = input("")
