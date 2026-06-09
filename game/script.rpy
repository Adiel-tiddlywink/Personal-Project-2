define s = Character("Shoni", color="#7a7fc5")
image mov_back = Movie(size=(1920, 1080), play="images/background.ogg")
image city = ("city.jpg")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene mov_back with fade
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

s "Welcome to my personal project! In this game, I want you to enjoy the
    game and read the story carefully, pick  options that suit you!"

s "Now tell me, what is the name of your character?"

$ persistent.playername = renpy.input("Please enter your name.")

$ persistent.playername = persistent.playername.strip()
if persistent.playername == "":
        $ persistent.playername = "Player"
$ player = persistent.playername

s "Nice to meet you, [player]!"
s "Let's get this show going, [player]!"

scene city with fade
"You, [player], are dropped off at.. Where are you actually dropped off at?"







$ renpy.pause(hard=True)