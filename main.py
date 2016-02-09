from random import randint
from Player import Player
from Enemy import Enemy
from time import time


# COOL!
print "Welcome to FlamRPG"
print "This is a text based RPG testing your hacking prowess"
print "Are you the realest haxx0r?"

tmp = raw_input("What's your name, adventurer?\n>>>")
player1 = Player(tmp)

print player1.get_name() + "... Welcome.  The world is depending on you. Anonymous is running rampant on the " \
                           "wild west known as the interwebs and you must save the weakling prince and defend " \
                           "humanitarian things."

print "hack this thing: "


mob1 = Enemy('Wordpress Server', 1, 1, 5)



while mob1.cpu.speed and player1.cpu.speed:
    mob1.cpu.speed -= 1
    player1.cpu.speed -= 1
    print player1.cpu.speed + ', ' + mob1.cpu.speed
    time.sleep(1)
