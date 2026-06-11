define s = Character("Shoni", color="#7a7fc5")
image mov_back = Movie(size=(1920, 1080), play="images/background.ogg")
image city = ("city.jpg")
image airport = ("airport.png")
image backstreet = ("Backstreet_Spring_Day.png")
image convenience_store = ("convenience_store.png")
# The game starts here.

# Define the logo image (optional but recommended for clean code)
image logo_intro = "logo.jpg"

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

    $ m_mouth = "smile"
    $ m_brow = "happy"

    scene mov_back with fade
    show maihi casual sneakers at fullbody_pos

    s "Welcome to my personal project! In this game, I want you to enjoy the
        game and read the story carefully, pick  options that suit you!"

    show maihi notice at fullbody_pos

    $ m_brow = "suspicious"
    s "Now tell me, what is the name of your character?"


$ persistent.playername = renpy.input("Please enter your name.")

$ persistent.playername = persistent.playername.strip()
if persistent.playername == "":
        $ persistent.playername = "Player"
$ player = persistent.playername

show maihi None at fullbody_pos
$ m_brow = "happy"
s "Nice to meet you, [player]!"
s "Let's get this show going, [player]!"

scene backstreet with fade
"You, [player], are dropped off at the exit of Kaerdence National Airport with only your luggage and dreams..
What dreams? Up to you, bud. You're walking across the airport, the rustle of the bag on your back faint against the loud noises of people walking and talking
as you head to find some food."

"Along the way, you come across a convenience store, no name on it but it does have two vending machines on each side of the door,
pretty convenient."

menu:
    "Do you enter?"

    "Yes.":
        scene convenience_store with fade
        "You enter the convenience store, and are greeted by shelves of food, and aisles of snacks along the flooring."

    "No.": 
        show screen custom_popup(title="Ending Found!", message="You discovered the 'Going Home Hungry' ending!", button_text="Close",)
$ renpy.pause(hard=True)
