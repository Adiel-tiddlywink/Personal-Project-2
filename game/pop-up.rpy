screen custom_popup(title="Notice", message="Something happened!", button_text="Close"):
    # modal True prevents players from clicking anything behind the pop-up
    modal True
    
    # Use a zorder higher than 0 to make sure it appears on top of dialogue boxes
    zorder 100

    # Semi-transparent background overlay to dim the game screen
    drag:
        align (0.5, 0.5)
        
        frame:
            background "#222222dd" # Dark grey with opacity. Replace with an image using: background "gui/my_popup_bg.png"
            padding (30, 30)
            xsize 500
            ysize 300
            
            vbox:
                align (0.5, 0.5)
                spacing 20
                
                # Pop-up Title
                text title:
                    size 28
                    bold True
                    xalign 0.5
                    color "#ffffff"
                
                # Pop-up Message Body
                text message:
                    size 20
                    xalign 0.5
                    text_align 0.5 # Centers paragraph text block
                    color "#cccccc"
                
                # Action Button to close the pop-up
                textbutton button_text:
                    xalign 0.5
                    padding (15, 10)
                    background "#444444"
                    hover_background "#555555"
                    action Hide("custom_popup")
