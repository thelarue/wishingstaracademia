# #############################
# Day One sports club visit
# #############################
label sports_club_day_one:
    
    stop music
    
    play music daily_journeys

    scene bg sports field
    
    """
    
    Grant writing was admittedly the first one that came to mind.
    
    A tiny part of me wondered: {i}what if I don't get into Rising Star{/i}?

    Maybe I could find a place at a non-profit, like the one Mom used to work at.
    
    Dad wouldn't be completely opposed, right? It's not private sector, but it's still money-related... {i}ish{/i}.

    ...

    As I made my way out of the building to head to Grant Writing 340, I cut through the soccer field.

    A soccer ball flies in front of my face, making me shriek and jump back in surprise.

    """

    student "Sorry about that! I didn't see you!"

    show teddy default with easeinright

    student "Oh! [mcname]? What are you doing here, neighbor?"

    # This visit seems the most exposition heavy. Could consider editing it or spicing it up with a cg in future builds.

    show teddy happy 

    """
    
    Teddy, my childhood friend.

    We first met on the playground behind his house after our moms arranged a first play date. 
    
    While our moms talked, we played together. 

    My first impression of Teddy was that he was a big softie. I spent most of the time bossing him around.

    Then I jumped onto the monkey bars, but my grip was too weak and I fell mid-swing.

    Teddy, who had begged me not to do that, tried to catch me. 

    After that, I saw Teddy in a different light. Like a protector of sorts.

    We were inseparable until we entered high school when he moved to live with his mom after his parents' divorce.

    Still, he's one of the very few friends I've been able to keep for so long.

    """
    
    # show mc happy at mc_emotes

    mc "Teddy! You're the only person I'd ever forgive for pelting me in the face with a soccer ball."

    "Is he... blushing?"

    mc """
    
    I'm actually on my way to check out a grant writing class.

    It turns out I'm a bit behind on credit hours, and it fits my requirements.

    """

    show teddy default

    teddy """
    
    Then you're talking to the right guy! I've taken that class before. 
    
    I didn't know you were interested in grant writing.

    """

    mc """
    
    Well, I wouldn't say I'm {i}interested{/i} in it, but maybe there's tools from it I could learn.

    You know, apply those skills to something else. 

    Knowing how to ask for money has {i}got{/i} to be a little helpful, right? 

    """

    student "Teddy! There you are!"

    "Bea, a bully I've known since high school, casually shoves me aside."

    "She's followed by her underling, Leah."

    """

    I'm amazed they got into this school, but then again...

    Their parents probably just gave a big donation to get them in.

    And now we're all stuck with these wannabe mean girls.

    """

    bea "Oops, sorry [mcname], I never notice you."

    show teddy angry

    leah "Remember when [mcname] showed up to high school graduation and even the principal didn't know who she was? That was so embarrassing!"

    "They both snicker into their hands."

    "Their words conjured that memory which I tried to keep locked away."

    menu sports_club_mean_girls_choice:
        "...":
            call day_one_sports_club_mean_girls_sad_choice from _call_day_one_sports_club_mean_girls_sad_choice
        "Wait, isn't Bea wearing a leg brace?" if (stats["creative"] >= 15): # Trying to get away with saying MC reverse engineers this trick
            $ mod_aff(5, "Teddy")
            call day_one_sports_club_mean_girls_brace_choice from _call_day_one_sports_club_mean_girls_brace_choice
    
    # Come back here after the choice

    show teddy default

    teddy  "Oh yeah! I'm actually busy right now, but let's exchange contact info."

    show teddy happy

    teddy "You know, uh, so I can text you about class."

    show teddy default

    "We exchange phone numbers."

    teddy  """
    
    I'll send you the syllabus and answer any questions you have, okay?

    Maybe we can meet up tomorrow to discuss it somemore, yeah?

    """

    mc  "Maybe we will. Thank you, Teddy!"

    show teddy happy

    teddy "Anytime, [mcname]. I'm always happy to see you."
    
    "Waving goodbye to Teddy, I feel my heart beat a little quicker."

    show teddy happy with easeoutleft
        
    # Back to the club selection menu
    jump day_one_club_visits

# Mean Girls choice
# Big sad 
label day_one_sports_club_mean_girls_sad_choice:
    
    mc "..."

    "I couldn't think or even process what they just said."
    
    "How could I ever forget how humiliating that was? Especially since it was the day after..."
   
    teddy """
    
    It's embarrassing to still be talking about high school as adults.
    
    [mcname] and I are trying to have a conversation, so I'd appreciate it if you could leave.

    """

    leah "We were just joking."

    "Her friendly tone reminded me of all the times the teachers wrote off my concerns."

    bea "We're all friends! Right, [mcname]? It was just a joke."

    """
    
    These girls could make people's lives hell.

    I didn't want the campus' resident golden retriever to get caught up in whatever mess they could dream up.

    """

    mc """
    
    Yeah, it's an inside joke between us. 
    
    Like... ha-ha I'm so normal and plain.
    
    It's funny if you really think about it.

    """

    "I tried to hold eye contact with Teddy. Willing him to believe me."

    show teddy default 

    teddy "If you say so..."

    "Bea and Leah nod frantically before scurrying away."

    teddy "But if they're giving you a hard time you just let me know, okay?"

    mc "I promise I will! Anyway, about the class?" 

    return


# Mean girls choice
# Leg brace
label day_one_sports_club_mean_girls_brace_choice:
    
    """
    
    I really shouldn't be surprised they are still obsessed with high school.

    That's where they peaked after all.

    I notice Bea limping on her left leg while wearing a leg brace.

    """

    mc """
    
    Oh man, how'd you get that leg brace?

    Don't tell me you tried to show off pole dance moves to boys again?

    """

    show teddy default

    mc "That's another funny story from high school, don't you think?"
    
    teddy """
    
    Oh yeah! I remember hearing about that.

    Bea, your infamy spread to me even though I was already gone by then.

    """

    bea """
    
    Yup... Well, whatever. 
    
    Teddy, I'll find you after you're done talking with [mcname] to talk about our group project.

    """

    leah "Yeah, talk to you later."

    "They both leave as Teddy leans towards me."

    teddy """
    
    Wow, they are still mean to you, huh?
    
    They've been nice to me recently, so I thought they grew up since high school.

    """

    """
    
    Looking over Teddy's physique, there's no question in my mind why they'd be nice to him now.

    He's had a growth spurt since high school.

    """

    teddy "If it's to help a friend, I'll make sure to tank the project."

    mc """
    
    No way! Don't do that.

    I'm fine, promise. You taught me how to stand up for myself before you left for college.

    So I'm fine, really!

    """

    show teddy happy

    teddy """
    
    That's right! 
    
    Although I'm pretty sure I also taught you how to knock someone out. 
    
    Don't think you've used that technique yet, right?

    """

    mc "Not yet, thankfully. Hopefully, I'll never have to. Anyway, about that class..."

    return
