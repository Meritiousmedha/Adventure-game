name = input("Enter your name: ")
print("Welcome", name, "to this adventure game")

answer = input("You are on the dirt road, it has come to an end. Which way do you want to go, left or right? ").lower()

if answer == "left":
    answer = input("You came to a river, you can walk around or swim across? ").lower()

    if answer == "walk":
        print("You walk a few miles and run out of thirst. You lost the game.")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator. You lost the game.")
    else:
        print("Invalid option. You lose.")

elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly. Do you want to cross it or head back? ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Do you want to talk to them? (Yes/No) ").lower()

        if answer == "yes":
            print("He killed you! You lost the game.")
        elif answer == "no":
            print("You escaped and won the game!")
        else:
            print("Invalid option. You lose.")
    else:
        print("Invalid option. You lose.")
else:
    print("Invalid option. You lose.")

print("Thanks for playing, " + name + ", for trying this game!")
