#imports
import time
from threading import Thread

score = 0
# Engine Parts
class Characters(object):
    def name(self):
        print('1. Morrissey Wayout')
        print('2. Shawn Rover')
        print('3. Roslin Ringlead')
        print('4. Don Jonas')
        who = input('> ')
        if who == '1':
            print('You chose Morrissey Wayout!')
            Introduction.expo('Morrissey', 'Morrisey loved to make music. His music was always "Deep" and "insightful", at least to him. So much so that he would bash other musicians for not understanding his shitty lyrics. One day, he decided to play his music on a homemade radio tower over all public radio stations. It wasnt long before he was tracked down by the local DJs, and chased into an abandoned record warehouse...')
        elif who == '2':
            print('You chose Shawn Rover!')
            Introduction.expo('Shawn', "Shawn thinks he is a wizard. He's always experimenting with 'magic'. Recently, he's been kidnapping people's cats in an attempt to turn them into his new human friends. The neighborhood cat ladies aren't very happy with his recent behavior, so they called the police. As a brave wizard, Shawn refused to give up, and ran into a 'magic tower' (skyscraper) to escape... ")
        elif who == '3':
            print('You chose Roslin Ringlead')
            Introduction.expo('Roslin', 'Roslin was very charismatic, so when it came to gaining followers, she was a natural. First she gained followers on social media, then with some wise words and hard work, she got people to worship her as a full on goddess. One day she decided to have a "ritual", where her followers would gather, eat, drink and stop breathing. The plan was a simple classic, poisoned punch, steal their wallets then move to maine. If only the arsenic didnt fall out her pocket during the opening speech.... '')
        elif who == '4':
            print('You chose Don Jonas!')
            Introduction.expo('Don', "He liked to fuck shit up.  People don't like that. He ran away")

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
class Roof(Room):
    print("You open a door and arrive on the roof of the building")
    print("You hear footsteps behind you, better find a way out!")
    print("You run to the edge of the building and see a building close by, jump to it!")
    def top():
                time.sleep(5)
                if jump == 'jump':
                    print("He slides face first down the stairs")
                    print("That's gotta hurt!")
                    print("You reach the top of the stairs")
                else:
                    print ("He catches you, and snaps you neck")
                    Game.death('')
    Thread(target = top).start()
    jump = input("Go: ")

# Stuff for running
Introduction.startup('')
