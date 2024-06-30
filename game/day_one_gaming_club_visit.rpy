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

    mc "What are you doing here, anyway?"

    felix "My class got cancelled, but I have permission to hang out in the computer lab since I'm captain of the esports team here."

    mc "{i}You're{/i} the team captain?"

    show felix arrogant

    felix """

    Deja vu, right?

    Why? You're not thinking of trying out, are you?

    """
    
    mc "I wasn't. And I definitely wouldn't now."

    felix """
    
    {i}Tch.{/i} You aren't any fun.

    So...

    """

    show felix default

    felix "Why are YOU here?"

    mc "I was thinking of joining the class that was supposed to be on today."

    felix "But why? What do you want to do with gaming?"

    mc "I just need the credit hours. That's all."

    felix """
    
    Well, it's not an easy class.

    This professor is one of the hardest ones to take. Having a poor attendance can cost you over half your grade.

    A lot of people think esports management is peak laziness, but it requires hardwork.

    If you just need credit hours, I doubt you have what it takes. 

    Take something easier.
    
    """

    show felix arrogant

    felix "I'd hate to see you sink to third place."

    mc "You are {i}not{/i} bringing up our grades, are you?"

    felix "Oh I am, and we both know you can't beat me in grades or games."

    """
    
    My eye twitches.

    How dare he continue to accuse me of petty cheating when he lost fair and square back then.

    """

    felix "Now leave, I really can't stand the sight of you."

    "I might join this class just to annoy him." # Please see the vision...

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