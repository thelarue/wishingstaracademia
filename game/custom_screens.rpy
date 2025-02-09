screen gameUI():
    # Keep this near the "top" of the screen stack
    zorder 100
    # Pull the stat values
    $ a = stats["assertive"]
    $ b = stats["creative"]
    $ c = stats["competitive"]
    $ d = stats["compassionate"]

    frame:
        background None
        xalign 1.0
        yalign 0.0
        xoffset 0
        yoffset 775
        # Build a grid    
        grid 2 5:
            spacing 5
            text "Stat"
            text "Value" 

            text "Assertive" size 33 color "#414141"
            text "[a]" size 33 color "#414141"

            text "Creative" size 33 color "#414141"
            text "[b]" size 33 color "#414141"

            text "Competitive" size 33 color "#414141"
            text "[c]" size 33 color "#414141"

            text "Compassionate" size 33 color "#414141"
            text "[d]" size 33 color "#414141"