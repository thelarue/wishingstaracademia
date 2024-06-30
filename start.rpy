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

    "My mother wished for me to be brave, to take chances, to..."

    # Start by creating a list that will capture what options are picked in order
    $ stat_set = []
    # This maps the selections in the upcoming menu to the stats they modify
    $ stat_mapping = {"... stand my ground.": "assertive","... be creative." : "creative", "... be the best.": "competitive", "... care deeply.": "compassionate"}
    menu stat_select:
        set stat_set 
        "... stand my ground.":
            jump stat_select 
        "... be creative.":
            jump stat_select
        "... be the best.":
            jump stat_select
        "... care deeply.":
            jump stat_select            
        "No matter what." if len(stat_set) >= 4:
            # We add different values to the stats based on the selections:
            # 
            # Option 1: 15 points
            # Option 2: 10 Points
            # Option 3: 5 Points
            # Option 4: 0 Points
            #
            # We walk through the stat_set array to get the option tied to the stat, which we can make into a dictionary:
            #
            # "... stand my ground.": assertive
            # "... be creative." : creative
            # "... be the best.": competitive
            # "... care deeply.": compassionate

            # Start with a new Python block
            python:
                # We know the value we need to add starts at 15, and drops by 5 each time. 
                stat_value = 15

                # We also know that the last option we picked (No Matter What), which we're using to move to the next section
                # Needs to be removed from our list, since there aren't any stats for it.
                stat_set.remove("No matter what.")

                # Create a for loop. 
                # "In order from 1 to 4, show me the value that picked for stat_set"
                for count, selection in enumerate(stat_set):

                    # Use the mod_stat function to add a value to the stat, based on the option chosen
                    # This means we need to take the value we have stored in selection, and give that to stat_mapping dictionary
                    mod_stat(stat_value, stat_mapping[stat_set[count]])

                    # Now that we added the current stat value, let's reduce it for the next loop iteration
                    stat_value = stat_value - 5

                    # From here, we repeat and loop back to the top until we run out of values in stat_set

            # Now that stats are set, let's go to the intro!
            jump intro