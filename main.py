#imports
import time
import random
import pygame
from threading import Thread



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
            Introduction.expo('Roslin', 'Roslin was very charismatic, so when it came to gaining followers, she was a natural. First she gained followers on social media, then with some wise words and hard work, she got people to worship her as a full on goddess. One day she decided to have a "ritual", where her followers would gather, eat, drink and stop breathing. The plan was a simple classic, poisoned punch, steal their wallets then move to maine. If only the arsenic didnt fall out her pocket during the opening speech.... ')
        elif who == '4':
            print('You chose Don Jonas!')
            Introduction.expo('Don', "He liked to fuck shit up.  People don't like that. He ran away")

class Game(object):
    def play(score):
        score = 0
        yourroom = random.randint(1, 3)
        print(yourroom)
        print(f'{score}')
        time.sleep(1)
        if yourroom == 1:
            print("You run through a door and enter a room with all white walls")
            print("There's multiple cans of spraypaint on the ground, and the room is silent")
            print("Anything you want to draw while you catch your breath?")
            paint = input("Paint: ")
            if paint == 'X':
                pygame.mixer.music.load('X.mp3')
                print("You paint a large red 'X' on the wall")
                print('You feel stronger than ever before')
                pygame.mixer.music.play(1)
                time.sleep(5)
                print("You're now egar to continue your run")
                Game.play(0)
            elif paint == '2D':
                pygame.mixer.music.load('slew.mp3')
                print("You paint a scrawny man with blue hair and black eyes on the wall")
                print('How relaxing')
                pygame.mixer.music.play(1)
                time.sleep(5)
                print("You no longer feel any rush to do anything. Take it easy")
                Game.play(0)
            else:
                print(f'You paint {paint} on the wall')
                print("You hear footsteps, time to run!")
                Game.play(1)
        elif yourroom == 2:
                print("You open a door and arrive on the roof of the building")
                print("You hear footsteps behind you, better find a way out!")
                print("You run to the edge of the building and see a building close by, jump to it!")
                jump = None
                def top():
                            time.sleep(5)
                            if jump == 'jump':
                                print("You jump to the next roof")
                                print("You land safely!")
                                print("You run through the first door you see")
                                Game.play(1)
                            else:
                                print ("He catches you, and snaps you neck")
                                Game.death(1)
                Thread(target = top).start()
                jump = input("Go: ")
        elif yourroom == 3:
                 print("You open a door and see a large man blocking you path")
                 print("Punch him!")
                 jump = None
                 def pawnch():
                             time.sleep(5)
                             if punch == 'punch':
                                 print("He drops to the floor")
                                 print("Back to running!")
                                 Game.play(1)
                             else:
                                 print ("He knocks you out with one punch")
                                 Game.death('')
                 Thread(target = pawnch).start()
                 punch = input("Go: ")
        elif yourroom == 4:
                 print("You open a door and see a large man blocking you path")
                 print("Punch him!")
                 jump = None
                 def punch():
                             time.sleep(5)
                             if punch == 'punch':
                                 print("He drops to the floor")
                                 print("Back to running!")
                                 Game.play(1)
                             else:
                                 print ("He knocks you out with one punch")
                                 Game.death('')
                 Thread(target = top).start()
                 jump = input("Go: ")

#Insert random room selection here
    def death(score):
        print(f"Nice, you scored {score} points!")
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
            Game.play(0)
        else:
            Introduction.tutorial('')
    def tutorial(Room):
        print('The premise of this game is pretty simple')
        print("You're running away, but you're path isn't all too clear")
        print('You have limited lime to type the action you need to take to continue running')
        print("For example, if you're told that there is a low hanging object ahead, you may want to type 'duck'")
        print("Incase you can't tell, your also not a pacafist, so you may have to fight too, with words like 'kick', 'punch', and 'jab'")
        print("Press enter after every action, don't press it more than once. Please.")
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
                        Game.play(0)
                    else:
                        print ("Man you suck at this, try again")
                        Introduction.tutorial('')
        Thread(target = train).start()
        punch = input("Try it: ")



#Insert next room here


# Stuff for running
pygame.mixer.init()
Introduction.startup('')
