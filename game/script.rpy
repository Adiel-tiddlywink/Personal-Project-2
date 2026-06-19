image logo_intro = "logo.jpg"

label splashscreen:
    
    # Start with a clean black screen
    scene black
    with fade
    
    # Pause on the black screen for 0.5 seconds
    $ renpy.pause(0.5)
    
    # Show custom logo with a smooth 1-second dissolve transition
    show logo_intro with dissolve
    
    # Keep the logo on screen for # seconds
    $ renpy.pause(6.5)
    
    # Hide the logo and return the screen to black
    scene black
    with dissolve
    
    # Small pause before entering the main menu
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
What dreams? Up to you, bud."

"You're walking across the airport, the rustle of the bag on your back faint against the loud noises of people walking 
and talking as you head to find some food."

"Along the way, you come across a convenience store, no name on it but it does have two vending machines on each side of the door,
pretty convenient."

menu:
    "Do you enter?"

    "Yes.":
        jump convenience_store 

    "No.":
        show screen custom_popup(title="Ending Found!", message="You discovered the 'Going Home Hungry' ending!", button_text="Close")
$renpy.pause(hard=True)
        
label convenience_store:
    scene convenience_store with fade
    "You enter the convenience store, and are greeted by shelves of food, and aisles of snacks along the flooring and a few things catch your eye.
    You come to realize that.. there's no one else in here. No customers, no cashiers.. In fact, there's no image at all!"

    show maihi exclaim casual sneakers at fullbody_pos
    $ m_mouth = "o"
    s "Oh, hey! Uhhh.. theres no image here right now!"

    show maihi question casual sneakers at fullbody_pos

    $ m_brow = "sad"
    $ m_mouth ="biggrin"
    s "Oops.. not sure what happened here.. {w=1.5}{nw}"
    show maihi exclaim casual sneakers at fullbody_pos
    extend "Why not come back at a later update to see if I've an image to show, hm?"

    hide maihi exclaim casual sneakers
    jump busstop

label busstop:
    scene busstop with fade
    "After that.. unexpected moment with Shoni, you exit out the convenience store, and keep on walking, having stolen a floating chocolate bar on the way out."
    "Along the way, you spy a nearby bus stop and after a while, you decided 'Why not?' and decide to go and wait for the next bus."

    $ renpy.pause(hard=True)
