
# This is a very hard way to solve this problem. We will use customized responses moving forward.
label select_sports:
    mc "What about the sports club?"
    # roberts default
    roberts "That's a great choice! I think you already know the captain pretty well."
    jump counselor_scene_2
label select_music:
    mc "Music club sounds easy enough."
    # roberts giggle
    roberts "Something tells me you'd really like that one. Cash is in charge of it. You can find them in the music room around lunch time."
    jump counselor_scene_2
label select_gaming:
    mc "We have a gaming club? I used to play competitively in high school, so that could be fun."
    "That was before Dad blew up about wasting my time on anything not school-related."
    # roberts wincing
    "The counselor winces."
    roberts "That was one of the team-building skills options, but if you think it would bring some fun into your life, then go for it!"
    jump counselor_scene_2

# #############################
# All replies land here.
#  Wrap Counselor talk
# #############################

label counselor_scene_2:
    show mc happy at mc_emotes
    "I slip the sheet of paper into my backpack and stand."
    mc "Thank you for the suggestions. If it'll really make my resume look better I'll give the club a shot."
    "And I definitely won't tell Dad."
    
    scene bg university hallway
    "I glance at the clock on the wall."
    "It's only lunch time."
    "I have plenty of time to check out each club. Thankfully the sheet the counselor gave me has the room locations and club leader names."

    # Don't put in the menu loop, You can't reuse it without making it hard.
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
        "I think I'll go check out the music club." if flags['Music Visited'] == False:
            $ flags['Music Visited'] = True
            jump music_club
        "Gaming club feels the most right." if flags['Gaming Visited'] == False:
            $ flags["Gaming Visited"] = True
            jump gaming_club
        "Maybe the sports club would be the best option for me?" if flags['Sports Visited'] == False:
            $ flags["Sports Visited"] = True
            jump sports_club
        # This should only show once we seen one club    
        "Oh crap! I'm about to miss class!!!" if len(day_one_club_visit_set) > 0:
            jump cat_event            

# #############################
# Day One music club visit
# #############################
label music_club:
    scene bg music club
    # cg of bastion playing an instrument
    # play music
    "I gasp."
    "It's Bastion, his head hanging over his instrument as he plays a soft melody with skill and precision."
    sharp "Isn't he amazing? He just transferred here this week and already signed up for music club."
    "Oh, I came here to ask Professor Sharp about signing up. I guess that means there's no room left?"
    sharp "I'm Professor Sharp, and there's exactly two spots open. You both can sign up, if you can pass the trial."
    "A trial?"
    "He hands me a notepad with three items written in red."
    sharp "There's three things we need before we can accept any more students. You and Bastion can work together."
    sharp "If you can bring all three things before the festival, you can officially list music club as your extra-curricular for when you apply for Rising Star Financial."
    # mc react confuse
    mc "How did you know I'm going to apply to Rising Star?"
    sharp "Your name is [mcname], right? I knew your father in school. I'd be really surprised if he wasn't pushing you to follow in his footsteps."
    mc "Is he really that predictable?"
    "I pay closer attention to Professor Sharp."
    "He's the same age as my parents, with kind eyes and an easy smile. I wonder how well he knew Dad?"
    "Does he know Mom?"
    sharp "Your father is, well..."
    sharp "I'm sure he hasn't changed at all."

    "He changes the subject quickly."

    sharp "I'll tell Bastion to meet you at the club room tomorrow around this time so you can discuss the first item together."
    sharp "You can stay awhile and listen, if you'd like."

    # Head back to the menu list
    jump day_one_club_visits


# #############################
# Day One music club visit
# #############################
label sports_club:
    scene bg sports field
    "Sports!"
    
    jump day_one_club_visits

# #############################
# Day One cat event
# #############################
label cat_event:
    "Cat event!"

    jump day_one_cat_event