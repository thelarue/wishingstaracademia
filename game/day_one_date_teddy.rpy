label day_one_date_Teddy:
    
    stop music
    
    play music friends_to_the_end
    
    scene bg university hallway

    show teddy default

    teddy """
    
    Oh hey, [mcname]!

    I didn't think you'd still be at school.

    """

    "Teddy spots me as I make my way for the building exit."

    # show mc happy at mc_emotes

    mc "Wow, I feel like I've seen you more today than I have in years!"

    "We naturally gravitate toward the soccer field."

    show teddy happy

    teddy "Is that a bad thing?"

    mc "Of course not! It makes me really happy."

    scene bg sports field with dissolve

    show teddy happy

    teddy """

    Same here, it's been way too long.

    I'm stoked that you are thinking about joining soccer.

    It reminds me about how your mom would watch us when we were kids. She swore we'd both go pro.

    """

    show teddy default

    """

    My and Teddy's mom were close friends. 

    She really wished we were in the same year of school, so us being in the same soccer club as kids made her happy.

    """

    mc "You remember that, huh? She'd probably be thrilled if I did join the team."

    teddy """
    
    I remember a lot of things about the both of you.

    Your house was like my home away from home.

    """

    "Teddy grabs a soccer ball from the side storage cubby off the field."

    teddy "Do you want to practice some kicks?"

    """

    I nod and follow him to the middle of the field after we laid our stuff down.

    He places the ball on the ground 30 feet in front of us and stands besides me.

    """

    teddy "Alright, let's see the first kick!"

    # show mc embarrassed at mc_emotes

    mc "I haven't done this since middle school, so don't make fun of me, got it?"

    show teddy happy

    teddy "Of course."

    """

    I recall what I learned back in our junior club days and try to kick the ball in a straight line.

    It's not very powerful, and the ball doesn't go far.

    """

    show teddy default

    teddy "Not bad, [mcname]."

    "He grabs the ball and puts it back in place."

    if stats["competitive"] >= 5: # He finds competitiveness attractive

        "Teddy stands close enough to me that I can feel the warmth of his body."

    else:

        "Teddy stands besides me again."
    
    teddy "Try and keep your feet facing this way."

    "He positions my non-kicking foot straight and my kicking foot slightly curved."

    teddy "And lock your ankle right before you make contact with the ball."

    # show mc concentrated at mc_emotes

    "I kick the ball again."

    if stats["competitive"] > 10:
        
        "It soars higher and further than before!"
        
        $ mod_aff(5, "Teddy")

    else:
        
        "Despite his instructions, it lands even closer than the last kick."

        call teddy_day_one_bad_kick
    
    # return from the teddy bad kick 

    show teddy default

    mc "This really reminds me of the old days."

    teddy "Same. I've honestly been missing you."

    show teddy happy

    teddy """
    
    It'd be nice if we could get close again, like we used to be.

    Whether you join the team or not.

    """

    # show mc blush at mc_emotes

    "Heat rises to my cheeks."

    if stats["assertive"] < 10:
        "I look down."

        mc "Same..."
    else:
        mc "For sure."
    
    show teddy default

    mc "I've just been so busy with school. Trying to keep my grades high."

    teddy "So the usual?"

    mc "Yeah."

    teddy """
    
    I figured.

    I see you out in the hallways running between a dozen classes.

    """
    show teddy happy

    "He laughs."

    mc "Dad said I should be a top candidate for Rising Star since I've been putting in the work."

    show teddy default

    "He frowns."

    teddy """

    You know, I'm not huge on nepotism or anything but...

    Couldn't he just give you a job? 

    Why is he making you jump through hoops?

    """

    """
    
    My Dad is a swore subject for Teddy.

    Teddy never cared for Dad and I'm pretty sure the feeling is mutual.

    I've always found that surprising since Teddy and Dad shared a sport.

    """

    mc "Because nepotism is bad, of course."

    teddy """
    
    Why work there anyway?

    You'll have to wear one of those stiff suits too!

    """
    
    mc "The financial industry is stable right now, and my dad's company has weathered better than others."

    show teddy happy

    teddy """
    
    But the suits! We used to make fun of your dad for wearing them all the time.

    Weren't you the one who said he looked like a 'sad, dead penguin'?

    I don't think you will fashionably recover if you follow in his footsteps.

    """

    "I laugh."

    mc """

    Hey now! He might look like a sad, dead penguin...

    But he makes a good living.

    I want that for me too.

    """

    show teddy default

    teddy """
    
    But is that really your dream?

    Didn't you always say you wanted to be more like your mom?

    """

    # show mc thoughtful at mc_emotes

    """

    He's right.

    I used to make fun of Dad and say I wanted to be a creative.

    Just like Mom.

    But that was before....

    """

    mc "Well, dreams can change."

    "I say it with a smile on my face that I don't really feel."

    mc """

    I just want a comfortable, stable life.

    Sometimes I wonder if Mom's where she is now because of how unstable her job was.

    Dad makes it sound like it broke her.

    """

    teddy """
    
    I understand, [mcname].

    And I'll support you no matter what.

    You'd be successful in any industry.

    I just want you to be happy in whatever it is that you choose to do.

    """

    mc "Thank you, Teddy."

    "That's the nicest thing I've been told in a long time."

    mc "You've always been my best friend."

    show teddy happy

    "His smile reaches his eyes, and my heart flutters at the sight."

    mc "But what about you?"

    if stats["assertive"] > 10:
        mc "Weren't you supposed to graduate a couple years ago?"

        show teddy default

        teddy "Haa... Still so blunt."
    else:
        show teddy default

        "Teddy was supposed to graduate a couple years ago."
    
    teddy """

    I took two years off to travel.

    And honestly... I learned so much more than I would have just staying here.

    It may have taken me a lot of effort to get back into the swing of academic life, but it was worth it.

    Not that Wishing Star Academia made it easy.

    """

    """

    Wishing Star Academia, or WSA as most people call it, is an ivy league school.

    It couldn't have been easy to get the school to agree to a hiatus since Teddy got in on a soccer scholarship.

    """

    teddy """
    
    I'm planning on spending a few years post graduation going back.

    I mean, doing humanitarian things.

    I'll get my international affairs degree and see how I can help outside of just being muscle.

    You know, being out there, helping people...

    """

    show teddy happy

    teddy "It was rewarding."

    mc """

    That's amazing, Teddy.

    I can't believe I get to call you a friend.

    You're definitely going to change the world one day.

    """

    show teddy default

    teddy "A friend... I'm glad too, [mcname]."

    "He glances at the time on his phone."

    teddy """
    
    Looks like this impromptu soccer practice ran pretty late.

    We should do this again. I've missed you.

    """

    mc "For sure! I'd really like that."

    teddy "I know you live nearby, but I can walk you home if you'd like."

    # show mc no at mc_emotes 

    mc "Thank you, but it's not really that long. I'll be okay!"

    # This would be a perfect place for a cg VVVVVV

    """

    Teddy pulls me into a tight hug.

    My face heats up as I hug him back.

    We used to cling to each other as kids, but this feels different.

    Feeling his muscles under his shirt press against me makes me feel...

    Embarrassed?

    I think that's what this feeling is, right?

    He says goodbye and waves as he walks back towards the university.

    """

    jump day_one_go_home

label teddy_day_one_bad_kick:

    menu:

        "That's okay!":
            "There's no point sweating it."

            teddy """
            
            Don't worry, [mcname].
            
            If you join the team, I promise to whip you up into shape.

            """

            show teddy happy
            
            teddy "Nicely, of course."
            
            return # goes back to the date label

        "No, I CAN do better than that. Be competitive!":
            if stats["competitive"] <= 10:
                $ mod_stat(-1, "Self") # Lose a sense of self, because MC is not competitive in this build of her
                $ mod_stat(1, "competitive") # However gain a competitive stat because she is trying
                
            """
            
            Before Teddy can get the ball for me, I run and reset the ball.

            I give it a kick.

            Though it doesn't go soaring, it is better than last time.

            """

            show teddy happy

            teddy """
            
            Glad to see you aren't willing to give up. We need more of that on the team.

            Just don't push yourself too hard, okay?

            """

            $ mod_aff(5, "Teddy") # He likes the spunk!

            return


            






