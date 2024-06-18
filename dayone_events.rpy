
label check_sports1:
    mc "What about the sports club?"
    # roberts default
    roberts "That's a great choice! I think you already know the captain pretty well."
    jump counselor_scene_2
label check_music1:
    mc "Music club sounds easy enough."
    # roberts giggle
    roberts "Something tells me you'd really like that one. Cash is in charge of it. You can find them in the music room around lunch time."
    jump counselor_scene_2
label check_gaming1:
    mc "We have a gaming club? I used to play competitively in high school, so that could be fun."
    "That was before Dad blew up about wasting my time on anything not school-related."
    # roberts wincing
    "The counselor winces."
    roberts "That was one of the team-building skills options, but if you think it would bring some fun into your life, then go for it!"
    jump counselor_scene_2

label counselor_scene_2:
    show mc happy at mc_emotes
    "I slip the sheet of paper into my backpack and stand."
    mc "Thank you for the suggestions. If it'll really make my resume look better I'll give the club a shot."
    "And I definitely won't tell Dad."
    
    scene bg hallway
    "I glance at the clock on the wall."
    "It's only lunch time."
    "I have plenty of time to check out each club. Thankfully the sheet the counselor gave me has the room locations and club leader names."

    menu:
        "What should I check out first?"

        "I think I'll go check out the music club.":
            $ flags["Music Visited"] = True
            jump music_club_1
        "Gaming club feels the most right.":
            $ flags["Gaming Visited"] = True
            jump gaming_club_1
        "Maybe sports club would be the best option for me?":
            $ flags["Sports Visited"] = True
            jump sports_club_1

label music_club_1:
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

    menu:

        "Thank you, but I need to go check out the sports club.":
            $ flags["Sports Visited"] = True
            jump sports_club_1
        "I'll let him practice in peace and go find the gaming club.":
            $ flags["Gaming Visited"] = True
            jump gaming_club_1
        "Oh crap! I'm about to miss class!!!":
            jump cat_event_1

label gaming_club_1:
    scene bg gaming

    "Before Dad scolded me over wasting my time on video games, I had spent the first two years of high school playing on a competitive squad."

    return

label sports_club_1:
    "Sports!"
    return

label cat_event_1:
    "Cat event!"