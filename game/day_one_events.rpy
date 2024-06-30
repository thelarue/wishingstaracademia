# #############################
# All replies land here.
#  Wrap advisor talk
# #############################

label advisor_scene_2:
    
    #show mc happy at mc_emotes
    
    "I slip the sheet of paper into my backpack and stand."
    
    mc "Thank you for the suggestions. Maybe I'll scope them out before I decide."

    roberts "Don't take too long. You have until tomorrow to decide before registration closes."
    
    scene bg university hallway
    
    "I glance at the clock on the wall."
    
    "I'll scope out the classes and see if anyone I know takes these classes."

    "What should I check out first?"
    
    # Prep for the next section
    # We need to call this now to track the length and know when to show the "I'm late" choice
    $ day_one_club_visit_set = []

# #############################
# Visit a club on Day One
#  We can loop to all, but miss class if we do more than one.
# #############################
label day_one_club_visits:

    scene bg university hallway
    # Leave the option to go to class in, but not selectable at first
    menu day_one_club_visit_picked:
        set day_one_club_visit_set
        "I think I'll go check out string ensemble." if flags['Music Visited'] == False:
            $ flags['Music Visited'] = True
            jump music_club_day_one
        "Gaming Culture and Engagement sounds like fun." if flags['Gaming Visited'] == False:
            $ flags["Gaming Visited"] = True
            jump gaming_club_day_one
        "Maybe the grant writing class would be the best option for me?" if flags['Grants Visited'] == False:
            $ flags["Grants Visited"] = True
            jump sports_club_day_one
        # This should only show once we seen one club    
        "Oh crap! I'm about to miss my own class!!!" if len(day_one_club_visit_set) > 0:
            jump quiz_event            

# These visits are located in their own .rpy files named day_one_CLUB_visit

# #############################
# Day One Quiz
# #############################
label quiz_event:
    
    scene bg university hallway

    """
    Whew, I managed to get to my seat right before the professor took attendance.

    But I groan as he starts to pass out some sort of quiz.

    I hope I can pass it...

    The top of the quiz reads: \"Constellations and Stars\"

    """

    # Catch the user's answers for later
    $ day_one_quiz_answers_set = {}

    menu quiz_one_question_one:
        "1. What is the name of a bright star in Orion?"
        "A. Belinda":
            $ day_one_quiz_answers_set['1'] = "a"
        "B. Behemoth":
            $ day_one_quiz_answers_set['1'] = "b"
        "C. Betelgeuse":
            $ day_one_quiz_answers_set['1'] = "c"
        "D. Beetle":
            $ day_one_quiz_answers_set['1'] = "d"

    menu quiz_one_question_two:
        "2. What is the zodiacal symbol for the constellation Leo?"
        "A. Tiger":
            $ day_one_quiz_answers_set['2'] = "a"
        "B. Elephant":
            $ day_one_quiz_answers_set['2'] = "b"
        "C. Turkey":
            $ day_one_quiz_answers_set['2'] = "c"
        "D. Lion":
            $ day_one_quiz_answers_set['2'] = "d"    

    menu quiz_one_question_three:
        "3. Which is the closest galaxy to Earth outside the Milky Way?"
        "A. Sombrero":
            $ day_one_quiz_answers_set['3'] = "a"
        "B. Antennae":
            $ day_one_quiz_answers_set['3'] = "b"
        "C. Andromeda":
            $ day_one_quiz_answers_set['3'] = "c"
        "D. NCG 2770":
            $ day_one_quiz_answers_set['3'] = "d" 

    menu quiz_one_question_four:
        "4.  In what constellation is Sirius found?"
        "A. Ursa Minor":
            $ day_one_quiz_answers_set['4'] = "a"
        "B. Andromeda":
            $ day_one_quiz_answers_set['4'] = "b"
        "C. Canis Major":
            $ day_one_quiz_answers_set['4'] = "c"
        "D. Ursa Major":
            $ day_one_quiz_answers_set['4'] = "d" 

    menu quiz_one_question_five:
        "5. Which of these constellations is not part of the zodiac?"
        "A. Alpha Centauri":
            $ day_one_quiz_answers_set['5'] = "a"
        "B. Leo":
            $ day_one_quiz_answers_set['5'] = "b"
        "C. Aries":
            $ day_one_quiz_answers_set['5'] = "c"
        "D. Capricornus":
            $ day_one_quiz_answers_set['5'] = "d" 

    menu quiz_one_question_six:
        "6. How many light-years across is the Milky Way?"
        "A. 1,000,000 ":
            $ day_one_quiz_answers_set['6'] = "a"
        "B. 100,000":
            $ day_one_quiz_answers_set['6'] = "b"
        "C. 1,000":
            $ day_one_quiz_answers_set['6'] = "c"
        "D. 10,000":
            $ day_one_quiz_answers_set['6'] = "d" 

    menu quiz_one_question_seven:
        "7. Which of these is a galaxy?"
        "A. Large Magellanic Cloud":
            $ day_one_quiz_answers_set['7'] = "a"
        "B. Ceres":
            $ day_one_quiz_answers_set['7'] = "b"
        "C. Pluto":
            $ day_one_quiz_answers_set['7'] = "c"
        "D. Jupiter":
            $ day_one_quiz_answers_set['7'] = "d" 

    menu quiz_one_question_eight:
        "8. What is a star?"
        "A. A very handsome person":
            $ day_one_quiz_answers_set['8'] = "a"
        "B. Giant ball of hot gas":
            $ day_one_quiz_answers_set['8'] = "b"
        "C. The power to grant a wish":
            $ day_one_quiz_answers_set['8'] = "c"
        "D. A celestial body that orbits the sun":
            $ day_one_quiz_answers_set['8'] = "d" 
    
    "I turn in my test at the end of class."

    "I'll find out tomorrow if I passed or not."
    
    $ highest_affection = max(affection, key=affection.get) # Look at the affection dictionary and return the key with the highest value, 
    # basically whoever has most points should be stored in this variable.
    
    $ day_one_end_date_label = "day_one_date_" + highest_affection # This contructs a label and w/ the naming scheme I am using, will automatically add the correct name.

    # "[highest_affection]" # this is how you can debugg variables to see what ends up showing up. can reveal that you expected X but it showed Y so you can follow up w/ how it got to Y.

    jump expression day_one_end_date_label # when you jump using a variable, it has to be jump expression variable.
    
    # Wish should NOT be the highest unless the player edits that in or something.