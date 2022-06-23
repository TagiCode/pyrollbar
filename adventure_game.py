from optparse import Option
import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(1)


def intro(weapon, option):
    print_pause("You find yourself standing in an open field,",
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + option + " ",
                "fairie is somewhere around here,\n"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave")
    print_pause("In your hand you hold your trusty",
                "(but not very efective) dagger")


def house(weapon, option):  # fight or run to field
    print_pause("You approach the door of the house")
    print_pause("You are about to knock when the door opens",
                "and out steps a " + option + ".")
    print_pause("Eep! This the " + option + "'s house!")
    fight(weapon, option)


def fight(weapon, option):  # fight
    print_pause("The " + option + " attacks you")
    if weapon != []:
        fight_run = input("Would you like to 1 fight or 2 run away?")
        if fight_run == '1':  # fight with new sword
            print_pause("As the " + option + " moves to attack,",
                        "you unsheath your new sword.")
            print_pause("The Sword of Oporoth shine brightly in your had",
                        "as you brace yourself for attack.")
            print_pause("But the " + option + " takes the look",
                        "at your shiny new toy and runs away!")
            print_pause("you have rid the town of the " + option + ".",
                        "You are victorious!")
            play_again(weapon, option)  # paly again or not
        else:
            print_pause("You run back into the field. Luckily,",
                        "you don't seem to have been followed")
            field(weapon, option)   # main
    else:
        print_pause("You feel a bit unde-prepared for this,",
                    "with only having a tiny dagger")
        while True:
            fight_run = input("Would you like to (1) fight or (2) run away?")
            if fight_run == '1':  # fight
                print_pause("You do your best ...")
                print_pause("but your dagger is no match for " + option + "")
                print_pause("You have been defeated!")
                play_again()  # play again or not
            elif fight_run == '2':  # run
                print_pause("You run back into the field. Luckily,",
                            "you don't seem to have been followed")
                field(weapon, option)  # main


def cave(weapon, option):  # dagger
    print_pause("You peer cautiosly into the cave")
    if weapon == []:
        print_pause("It turns out to be only very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found a magical Sword of Ogoroth!")
        print_pause("You discad your silly old dagger and",
                    "take the sword with you")
        print_pause("You walk back out to the field")
        weapon.append('Ogoroth')
        field(weapon, option)
    else:
        print_pause("You have been here before,",
                    "and gotten all the good stuff.",
                    "It's just an empty cave now.")
        print_pause("you walk back out to the field.")
        field(weapon, option)  # main


def play_again(weapon, option):
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game(weapon, option)
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again(weapon, option)


def field(weapon, option):
    print_pause("Enter 1 to knock on the door of house")
    print_pause("Enter 2 to peer into cave")
    house_or_cave = input("please enter 1 or 2 ")
    if house_or_cave == '1':
        house(weapon, option)
    elif house_or_cave == '2':
        cave(weapon, option)


def play_game():
    item = []
    option = random.choice(["wicked fairie", "pirate",
                            "dragon", "troll", "gorgon"])
    intro(item, option)
    field(item, option)


play_game()
