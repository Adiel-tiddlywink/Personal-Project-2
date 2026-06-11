define s = Character("Shoni", color="#7a7fc5")
image mov_back = Movie(size=(1920, 1080), play="images/background.ogg")
image city = ("city.jpg")

# The game starts here.

# Define the logo image (optional but recommended for clean code)
image logo_intro = "images/studio_logo.png"

# This special label tells Ren'Py to run this block before loading the main menu
label splashscreen:
    
    # 1. Start with a clean black screen
    scene black
    with fade
    
    # 2. Pause on the black screen for 0.5 seconds
    $ renpy.pause(0.5)
    
    # 3. Show your custom logo with a smooth 1-second dissolve transition
    show logo_intro with dissolve
    
    # 4. Keep the logo on screen for 2.5 seconds
    $ renpy.pause(10.0)
    
    # 5. Hide the logo and return the screen to black
    scene black
    with dissolve
    
    # 6. Small pause before entering the main menu
    $ renpy.pause(2.5)
    
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
menu:
    "What are you dropped off at?"

    "Emora Unitary Airport.":
        "I drink the coffee, and it's good to the last drop."

    "Navonodrea National airport."
        "I drink the tea, trying not to make a political statement as I do."







$ renpy.pause(hard=True)
