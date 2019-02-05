# Rooms
class Roof(Room):
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
                else:
                    print ("He catches you, and snaps you neck")
                    Game.death('')
    Thread(target = top).start()
    jump = input("Go: ")
    Room.points()



#Insert next room here
class Roof(Room):
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
                else:
                    print ("He catches you, and snaps you neck")
                    Game.death('')
    Thread(target = top).start()
    jump = input("Go: ")
    Game.play(score)

class Door(Room):
    def open():
        pass
