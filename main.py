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
    def play(speed):
        score = 0
        yourroom = random.randint(1, 8)
        time.sleep(2)
        print('\n')
        print('\n')
        print('\n')
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
                time.sleep(3)
                print("Things are about to get crazy, you can feel it")
                print("You hear chanting in the next room over")
                input("> Press enter when you've prepared yourself")
                print("You enter a room full of figures in white hoods")
                print("All eyes are immediately set on you")
                print("Run, or fight?")
                calt = None
                def cult():
                            time.sleep(speed)
                            if calt == 'run':
                                print("In total panic, run past them and tword the exit")
                                print("You feel a strange force push you out the door")
                                print("You're back at the entrance to the building that started all this'")
                                print("You hear screaming in the distance, directed at you.'")
                                print("Here we go again!'")
                                time.sleep(5)
                                Game.play(speed)
                            elif calt == 'fight':
                                print("There's about 10, you're sure you can take them")
                                print("As you throw your first punch, you notice a pentagram in the center of the room")
                                print("It's beginning to glow")
                                input("> Press enter to begin boss fight!")
                                Bosses.cult_boss(3)
                            else:
                                print ("A cult member approches you, and stabs you in the chest")
                                Game.death(1)
                Thread(target = cult).start()
                calt = input("?: ")
            elif paint == '2D':
                pygame.mixer.music.load('slew.mp3')
                print("You paint a scrawny man with blue hair and black eyes on the wall")
                print('How relaxing')
                pygame.mixer.music.play(1)
                time.sleep(5)
                print("You no longer feel any rush to do anything. Take it easy")
                Game.play(10)
            elif paint == 'fire':
                pygame.mixer.music.load('burn.mp3')
                print("You paint a scrawny man with blue hair and black eyes on the wall")
                print("Is it me, or is this room getting really hot?")
                pygame.mixer.music.play(1)
                time.sleep(5)
                print("You walk out of the room, and nearly trip over a flamethrower")
                Bosses.flames(4)
            else:
                print(f'You paint {paint} on the wall')
                print("You hear footsteps, time to run!")
                Game.play(speed)
        elif yourroom == 2:
                print("You open a door and arrive on the roof of the building")
                print("You hear footsteps behind you, better find a way out!")
                print("You run to the edge of the building and see a building close by, jump to it!")
                jump = None
                def top():
                            time.sleep(speed)
                            if jump == 'jump':
                                print("You jump to the next roof")
                                print("You land safely!")
                                print("You run through the first door you see")
                                Game.play(speed)
                            else:
                                print ("Some catches you, and throws you off the building")
                                Game.death(1)
                Thread(target = top).start()
                jump = input("Go: ")
        elif yourroom == 3:
                 print("You open a door and see a large man blocking you path")
                 print("Punch him!")
                 punch = None
                 def pawnch():
                             time.sleep(speed)
                             if punch == 'punch':
                                 print("He drops to the floor")
                                 print("Back to running!")
                                 Game.play(speed)
                             else:
                                 print ("He knocks you out with one punch")
                                 Game.death('')
                 Thread(target = pawnch).start()
                 punch = input("Go: ")
        elif yourroom == 4:
                 print("You run through an open doorway, and the roof starts caving in!")
                 print("Run away!")
                 run = None
                 def ran():
                             time.sleep(speed)
                             if run == 'run':
                                 print("You run through another open and escape the room")
                                 Game.play(speed)
                             else:
                                 print ("The roof falls on your head")
                                 Game.death('')
                 Thread(target = ran).start()
                 run = input("Go: ")
        elif yourroom == 5:
                 print("You kick down a door, and someone immeditly jumps at you")
                 print("Duck!")
                 duck = None
                 def dawk():
                             time.sleep(speed)
                             if duck == 'duck':
                                 print("Their punch misses!")
                                 print("Back to running!")
                                 Game.play(speed)
                             else:
                                 print ("Everything fades to black as you pass out, and never wake up")
                                 Game.death('')
                 Thread(target = dawk).start()
                 duck = input("Duck: ")
        elif yourroom == 6:
            print('\n')
            print("You run past a man with in a white robe")
            print("He's got a large red 'X' painted on his hand")
            print('Stange....')
            time.sleep(10)
            Game.play(speed)
        elif yourroom == 7:
            print("You run into a room and a man charges you")
            print("He's wearing headphones, steal them, or keep running?")
            ah = None
            def phones():
                        time.sleep(5)
                        if ah == 'steal':
                            print('\n')
                            print("You attempt to steal his headphones, but drop them")
                            print("As you keep running, you can quietly hear that he was listening to 'Clint Eastwood' by Gorillaz")
                            print("That's cool I guess")
                            time.sleep(3)
                            Game.play(speed)
                        elif ah == 'run':
                            print('\n')
                            print("You keep running, and run right past him")
                            print('Smart move')
                            Game.play(speed)
                        else:
                            print ("He tackles you and beast you to death")
                            Game.death('')
            Thread(target = phones).start()
            ah = input("Run?: ")
        elif yourroom == 8:
            print("You enter a room with a large dog in the middle")
            print("The dog is sleeping, sneak around him")
            def sneak():
                time.sleep(speed)
                if sneak == 'sneak':
                    print('\n')
                    print("You tiptoe around the dog and leave the room")
                    print("Back to running!")
                    Game.play(speed)
                else:
                    print ("The dog wakes up and quickly rips you to shreds")
                    Game.death('')
                Thread(target = sneak).start()
                punch = input("Sneak: ")

    def death(score):
        print(f"You died, better luck next time!")
# Intro
class Introduction(object):
    def __init__(self):
        pass
    def startup(self):
        print("Welcome to Runner's fury!")
        print("To start the game, please choose your character")
        Characters.name('')
    def expo(name, backstory):
        print(f'We begin with the story of {name}')
        print(f'{backstory}')
        print('And now their adventure begins...')
        print('\n Have you played before? \n Y/N')
        tut = input('> ')
        if tut == 'Y':
            Game.play(5)
        else:
            Introduction.tutorial('')
    def tutorial(Room):
        print('The premise of this game is pretty simple')
        print("You're running away, but you're path isn't all too clear")
        print('You have limited lime to type the action you need to take to continue running')
        print("For example, if you're told that there is a low hanging object ahead, you may want to type 'duck'")
        print("In case you can't tell, your also not a pacafist, so you may have to fight too, with words like 'kick', 'punch', and 'jab'")
        print("Press enter after every action, don't press it more than once. Please.")
        print("Don't type if you aren't prompted to do so, or you'll break everything")
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
                        Game.play(5)
                    else:
                        print ("Man you suck at this, try again")
                        Introduction.tutorial('')
        Thread(target = train).start()
        punch = input("Try it: ")


class Bosses(object):
    def cult_boss(speed):
        print("A large creature of fire springs from the center of the pentagram")
        print("He's about 30 feet tall, and made of red and orange flames")
        print("He shoots a fireball in you direction!")
        print("Jump or duck?")
        ah = None
        def satan():
                    time.sleep(4)
                    if ah == 'jump':
                        print("You jump as high as you can, but your clothes catch fire")
                        print("The fire consumes you, but you aren't dead")
                        print("You're back at the entrance to the building that started all this")
                        print("You hear screaming in the distance, directed at you.")
                        print("Here we go again!")
                        time.sleep(10)
                        Game.play(4)
                    elif ah == 'duck':
                        print("You lost a little hair, but you're relatively ok")
                        print("The fireball seems to have killed a few cult members")
                        Bosses.cult_defeat(3)
                    else:
                        print ("Burning hurts a lot more than you thought it would")
                        Game.death('')
        Thread(target = satan).start()
        ah = input("Oh shit: ")

    def cult_defeat(speed):
        print("You see a fire alarm on the other side of the room!")
        print("Dash to it!")
        woter = None
        def water():
                    time.sleep(3)
                    if woter == 'dash':
                        print("You pull the alarm")
                        print("The beast screaches as the fire begins to go out")
                        print("It then begins to grow agin")
                        print("You exit the building, and the entire building is consumed by flames")
                        print("At least you're not being chased anymore!")
                        print('You win!')
                        input('> Press enter to end game')
                    else:
                        print ("The moster catches you, and you feel pain not just on your flesh, but in your soul")
                        Game.death('')
        Thread(target = water).start()
        woter = input("QUICKLY: ")

    def flames(speed):
        input('Press enter to pick it up')
        print("You've arrived at an incomplete section of the game, sorry!")
# Stuff for running
pygame.mixer.init()
Introduction.startup('')
