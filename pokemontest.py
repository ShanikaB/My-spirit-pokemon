"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""


def main():
    # It is a test that tells you who is your spirit pokemon according to your habits
    # The following is displayed to user
    print("If you are a 90s kid and want to know which pokemon you are, This test is for you")
    print("there are a series of questions that you have to answer as 'y' or 'n', and we will tell you who is your")
    print("spirit pokemon")
    print("Let's begin!")
    ask = input("Do you want to take the test- type y or n: ")
    if ask == "y":
        test_begin()


def test_begin():
    # question asked
    ask1 = input(" Do you love to sleep: ")

    ask2 = input("Do you love dark: ")

    ask3 = input("Are you short tempered: ")

    ask4 = input("Do you hate going out:  ")

    ask5 = input(" Are you a loyal friend: ")

    ask6 = input("Are you a shy person: ")

    ask7 = input("Do you hate when people touch your stuff: ")

    ask8 = input("Do you love singing: ")

    ask10 = input(" Did you enjoy the test: ")

    print("Thanks for being so honest")

    enter = input(" Are you ready to know who is your spirit pokemon. Press any key to continue.  ")

    if ask1 != "y" and ask2 != "y" and ask3 != "y" and ask4 != "y" and ask5 != "y" and ask6 != "y" and ask7 != "y":
        if ask8 != "y":
            print("Oh man!! You are just another boring human.")
    else:
        print(" Oh my my.. You are a mixture ")
        print("")
    # pokemon according to the choices made

    if ask1 == "y":
        print(" You are a Snorlax ")
        print("")
        print(" the Snorlax has endless amounts of food in its reach, which works out because it will not stop")
        print("eating until it’s consumed 900 lbs. of food. This Pokémon is docile when unprovoked, but it’s more ")
        print(" than useful in a duel. He loves to sleep")
        print("")
        print("")

    if ask2 == "y":
        print(" You are a Haunter ")
        print("")
        print("Haunter can be found in dark spots. It stalks its next living victim until it gets close enough to")
        print("attack. It does this by licking the victim in order to steal its life force away. It’s a pretty ")
        print("spooky Pokémon character, especially since it can float through even a solid wall.")
        print("")
        print("")

    if ask3 == "y":
        print(" You are a Gyarados ")
        print("")
        print(" Gyarados is very difficult to tame even for the most experienced Trainer, but that’s exactly why ")
        print("it’s considered pretty awesome.The worse part is this Pokémon likes violence and is attracted to it.")
        print("")
        print("")

    if ask4 == "y":
        print(" You are a Umbreon ")
        print("")
        print("With the combination of its looks and its capabilities, this Pokémon is actually considered an urban")
        print("creature. It’s rare to find an Umbreon living in the wild.")
        print("")
        print("")

    if ask5 == "y":
        print("You are Gengor")
        print("")
        print("This Pokémon is as sinister as it gets. It’s quite stealthy in a way that it can hide in any shadow.")
        print("Gengar is also mischievous and playful, behaving maliciously as it pleases. It plays practical jokes")
        print("on unsuspecting and random victims. However, if you happen to capture yourself a Gengar and train it")
        print("to be your faithful Pokémon, it will stay true and loyal to you to the very end")
        print("")
        print("")

    if ask6 == "y":
        print("You are Kingdra")
        print("")
        print("This Pokémon uses its yawn to create underwater currents that are forceful enough to destroy small ")
        print("ships. On the surface, it can also create large whirlpools and tornadoes. The Kingdra is a powerful")
        print("water creature that awakens during a storm. Make sure not to be in uninhabited sea areas during a ")
        print("storm because a Kingdra will be out looking for you.")
        print("")
        print("")

    if ask7 == "y":
        print("You are Pikachu")
        print("")
        print("Comeon!! it is Pikachu, you don't need a descriptiion. We all love him.")
        print("")
        print("")

    if ask8 == "y":
        print("You are Jigglypuff")
        print("")
        print("You love to sing and make new friends. But when your dear ones ignore you, you get disheartened.")
        print(" You are sensitive in such cases.")
        print("")
        print("")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
