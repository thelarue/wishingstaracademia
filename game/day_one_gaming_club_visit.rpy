# #############################
# Day One gaming club visit
# #############################
label gaming_club_day_one:

    stop music

    play music daily_journeys 

    scene bg gaming room

    "Before Dad scolded me over wasting my time on video games, I had spent the first two years of high school playing on a competitive squad."

    "It was the last time I felt like I had actual friends."
    
    "I really liked it."

    mc "Hello?"

    """
    
    I found out the class had gotten cancelled for today, but I banked on some student still showing up.

    Despite what I thought, the room is empty. 
    
    I spotted a computer running on the main menu of a familiar, side-scrolling game.

    No doubt someone was paying {i}very{/i} close attention in the previous class.

    I walked over to the computer.

    This game was one of my favorites growing up.

    I would hide under the covers with a flashlight and play it on my portable into the early hours of the morning.

    """

    menu play_side_scroller:
        "The high score list popped up..."
        
        "I bet I could top it.":
            if (stats["competitive"] >= 15):
                $ mod_stat(-1, "self") # lose some self because you pushed yourself to compete
            $ mod_aff(5, "Felix")
            call day_one_gaming_play_side_scroller

        "I better leave it alone; it's a waste of time.":
            call day_one_gaming_no_side_scroller

    # Return from the side_scroller
    ########################### REWRITE THIS WHOLE THING~!!!!!!!!!!!!!!!###################################################################
    mc "Wait..."

    "I pull out the sheet of paper Mrs. Roberts had given me and read the name of the team captain."

    mc "You're the team captain?"

    felix """
    
    Deja vu, right?"

    Why? You're not thinking of joining, are you?

    """

    # show mc pensive   

    "I wasn't too confident about the idea of joining a gaming club in the first place..."

    "I really liked being a part of the Gaming Club in high school, even if I was distraught when Felix made those accusations."

    "I'd never admit it aloud, but the competitive monster inside me is gnawing it's way out of my skin."

    "And seeing Felix be arrogant and confident really makes me want to knock him down from the pedestal he's put himself upon."

    # show mc defiant at mc_emotes

    mc "Actually, I am here to sign up. Where's the sheet?"

    show felix annoyed

    felix """
    
    First of all, there's no physical sheet. This isn't the 2000s, everything is digital.
    
    Not to mention, there's no way you'd be able to pass the gauntlet anyway.

    """
    
    mc "Gauntlet?"

    "Felix hands me a pamphlet from a pile on one of the desks." 
    
    "Three video game titles are listed on it, each one with a specific criteria to beat."

    felix """
    
    You have to clear in all three challenges before you can be considered one of the elite. And they're not easy.

    Trust me, I'm the one who came up with them.

    """

    # show mc defiant at mc_emotes

    "I scan the challenges."

    mc """
    
    You must have been slacking off since high school if you think these are challenges.

    The first one is beat the current team captain on Armored Power 3, do you have time to play tomorrow?

    """

    "I used to beat him one on one in Armored Power 1, back in high school."

    show felix arrogant

    felix """
    
    This time tomorrow, right here at the Gaming Club Room.
    
    I'll show you how much better I am now.

    """

    # show mc defiant at mc_emotes

    mc "Can't wait."

    """
    
    I can't help but smirk as I leave the room, brushing past his arms.
    
    I didn't realize at first how much he's grown since high school.
    
    But he's much taller, his arms are bulkier, and there's a deep, scratchy tone in his formerly high-pitched voice.
    
    I shake my head as I clench my fist... 
    
    Felix is my arch nemesis!
    
    """
    # End the gaming_club visit
    jump day_one_club_visits

label day_one_gaming_play_side_scroller:
    
    """
    
    I take a seat at the computer and start a new game.
    
    I send a little sprite running across the screen, collecting stars and jumping over traps as I try and beat the high score pinned to the upper right corner of the screen.
    
    It doesn't take long before I'm only a few hundred points away, but there's a tricky jump just ahead of the screen.

    """

    show felix default

    "student" "Good luck, I've been trying to beat the high score for weeks, but I can't get past that jump AND get all the stars."

    """
    
    I hear some guy chiding me, but I ignore it easily enough.

    It comes with being a girl on the internet.

    My character clears the tricky jump with too much momentum, throwing them off screen but then landing onto the next platform, a trail of stars circling the sprite.
    
    The high score on screen flashes as it updates to my score.

    """

    show felix shocked 

    "student" "What?! How did you!?"
    
    "I turn to look behind me, toward the raising and now familiar voice of a student."

    mc "Felix?"

    show felix arrogant

    """
    
    When I was in high school, back when I was allowed to be in clubs, I was in a gaming club.

    I was about to be the captain of our e-sports team, but then {i}someone{/i} ran a smear campaign against me and took that spot from me.

    And he here he is now. Someone I wanted very much to avoid.

    """

    show felix shocked
    
    felix """
    
    You!

    I should have known a {i}cheat{/i} like you would find a way to beat my high score.

    """

    # show mc angry at mc_emotes

    mc """
    
    We haven't spoken in years and that's the first thing you say to me? 
    
    More cheating allegations?

    """

    return


label day_one_gaming_no_side_scroller:

    mc "I shouldn't waste my time on a gaming anyways."

    show felix arrogant

    felix "Hey! Don't you know better than to touch someone else's game?"

    "I yelped before spinning to see a face I loathed."

    show felix default

    """
    
    This guy is the reason I don't like gaming anymore.

    Regardless of how my Dad felt about the habit, Felix is why playing games leaves a bad taste in my mouth.

    My Dad's feelings on the matter just made it easier to give up.

    """

    felix """
    
    Oh, it's you.

    [mcname] [mclast], was it? The notorious cheat.

    """

    # show mc angry at mc_emotes
    
    if stats["assertive"] > 10:
        mc "Oh, just shut up."
    else:
        mc "Lay off, will you?"

    return