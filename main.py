#imports
import time
from threading import Thread

score = 0
# Engine Parts
class Characters(object):
    def name(self):
        print('1. Morrissey Wayout')
        print('2. Calven Helviett')
        print('3. Arthur J. Tullis')
        print('4. Don Jonas')
        who = input('> ')
        if who == '1':
            print('You chose Morrissey Wayout!')
            Introduction.expo('Morrissey', 'He like to fuck shit up')
        elif who == '2':
            print('You chose Calven Helviett!')
            Introduction.expo('Calven', 'He like to fuck shit up')
        elif who == '3':
            print('You chose Arthur J. Tullis!')
            Introduction.expo('Arthur', 'He like to fuck shit up')
        elif who == '4':
            print('You chose Don Jonas!')
            Introduction.expo('Don', 'He like to fuck shit up')

class Game(object):
    def play(self):
#Insert random room selection here
    def death(self):
        print(f"Nice, you scored {score}")
# Intro
class Introduction(object):
    def __init__(self):
        pass
    def startup(self):
        print("Welcome to Snake Cave!")
        print("To start the game, please choose your character")
        Characters.name('')
    def expo(name, backstory):
        print(f'We begin with the story of {name}')
        print(f'{backstory}')
        print('And now their adventure begins...')
        print('\n Have you played before? \n Y/N')
        tut = input('> ')
        if tut == 'Y':
            Game.play('')
        else:
            Introduction.tutorial('')
    def tutorial(self):
        print('The premise of this game is pretty simple')
        print("You're running away, but you're path isn't all too clear")
        print('You have limited lime to type the action you need to take to continue running')
        print("For example, if you're told that there is a low hanging object ahead, you may want to type 'duck'")
        print("Incase you can't tell, your also not a pacafist, so you may have to fight too, with words like 'kick', 'punch', and 'jab'")
        print("When you stop running, you stop living, so stay on the run!")
        print("\n We set up a fake room for you to test you skills in. All rooms will go something like this...")
        input('> Press enter to being training')
        print("You enter a room with a test dummy, he's incapable of fighting back, but if you don't punch him we'll all laugh at you")
        punch = None
        def train():
                    time.sleep(5)
                    if punch == 'punch':
                        print("The test dummy's head falls off")
                        print("Nice work!")
                        input('> Press enter to end training, and start the game')
                    else:
                        print ("Man you suck at this, try again")
                        Introduction.tutorial('')
        Thread(target = train).start()
        punch = input("Try it: ")



# Rooms
class Room(object):
    def points(self):
        score = score + 1

class Stairs(Room):
    print("You see a flight of stairs and begin to run up them")
    print("A large man in standing in your way, but there seems to be space to pass him")
    print("Dodge him!")
    def step():
                time.sleep(5)
                if dodge == 'dodge':
                    print("You jump to the side and pass him!")
                    print("Nice!")
                else:
                    print ("He catches you, and snaps you neck")
                    Game.death('')
    Thread(target = step).start()
    dodge = input("Go: ")
    print("Now kick him down the stairs!")
    def steps():
                time.sleep(5)
                if kick == 'kick':
                    print("He slides face first down the stairs")
                    print("That's gotta hurt!")
                    print("You reach the top of the stairs")
                else:
                    print ("He catches you, and snaps you neck")
                    Game.death('')
    Thread(target = steps).start()
    kick = input("Go: ")
#Insert next room here



# Stuff for running
Introduction.startup('')
