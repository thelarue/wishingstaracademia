label start:
    # Let the player name the MC.
    python:
        mcname = renpy.input("What is your name?", length=32)
        mcname = mcname.strip()

        if not mcname:
            mcname = "Dahlia"

    # There are a lot of pieces of code commented out because we may or may not actually use them.
    # Initializes the calendar, the month, day, and year should be changed to fit
    # whatever we are using in game for a date.
    # $ calDate = calDate.replace(second=10, hour=12, minute=30, day=20, month=8, year=2024)

    # Causes the calendar to appear on the screen and scroll X to the side to a new date.
    # In this case, its 1 day.
    # call calendar(1)

    # Currently this shows the stats button which when pressed. Can be used to show other things as well.
    show screen gameUI
    scene bg galaxy

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show (outline of mom)

    "It's always the same dream."
    "A wishing star, that's what Mom always called it, shooting across the sky,"
    "And Mom kneeling beneath it, her hands clasped together."

    # move mom center

    "Before she was taken away she used to tell me about her final wish."
    "She said she was saving it for me, and that she couldn't wait to watch it come true together."

    scene bg hospital

    # CG mom being dragged away

    "I wish she would have told me how to use that wishing star."
    "I would have used it back then."

    "My mother wished for me to be brave, to take chances..."

    menu:
        "I would say I'm..."

        "... able to stand my ground.":
            $ mod_stat(20, "assertive")
            jump assertive_start
        "... pretty creative.": 
            $ mod_stat(20, "creative")
            jump creative_start
        "... competitive option":
            $ mod_stat(20, "competitive")
            jump competitive_start
        "... love cats. (lol)":
            $ mod_stat(20, "compassionate")
            jump compassionate_start