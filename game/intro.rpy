label intro:
    show screen gameUI # Shows the stats on the screen. This is a custom made screen which I think you can find in the screens.rpy file!

    stop music

    scene bg university hallway

    "Woman" "[mcname]?"
    
    "..."

    "Woman" "Are you asleep again?"

    "..."

    "Woman" "[mcname]? You're 15 minutes late for our appointment."

    "....."

    "Woman" "[mcname]!!!"

    # show mc embarrassed at mc_emotes

    play music daily_journeys

    "My advisor stands at the entrance of the library, her polished heel tapping on the tile as I jump out of my seat and wipe the drool from my mouth."

    mc "I'm so sorry! I just closed my eyes for a second, Mrs. Roberts. I'll be right there!"

    roberts """
    
    It's alright.

    Just come to my office in ten minutes.

    """ 
    # in theory, the way I did things above means that Mrs. Robert's 2 lines here will need to be clicked through. This is good for monologues. 

    "I stuff my books into my backpack and ignore the curious eyes following my every move."

    "Stay out of the light, Dad says."

    "Don't cause any unnecessary trouble and DEFINITELY don't be caught slacking off—"

    "Or I'll never get a job at Rising Star Financial Group."

    # show mc relieved at mc_emotes

    "Thankfully Mrs. Roberts' office isn't too far away. And Mrs. Roberts has always had a soft spot for me."

    "I lean against the wall outside her office. The door is closed, she must be talking to the student with the appointment slot after mine."

    "In just six more months, I won't see Mrs. Roberts anymore."

    # show mc scared at mc_emotes

    "Six months to get my resume together to apply at Rising Star."

    show bastion concerned

    "Student" "Are you okay? You look like you just saw a ghost."

    # show mc embarrassed at mc_emotes

    "I hadn't even realized Mrs. Roberts' door opened in the midst of my anxiety attack."

    "A guy my age stands in front of me, head tilted as he waits my answer."

    "But my mind goes blank as our eyes meet."

    "And then the rest of his profile comes into view and my jaw nearly falls open."

    "{i}He's... he's so beautiful! Is he really just a student?{/i}"

    "Two students walk past, both giggling to each other as they stare at the new student."

    "Juniper and Zoe, two girls who have made fun of me several times in the past few years."

    show bastion concerned

    "Student" "Maybe not a ghost, after all. Now you look like you just ate a frog."

    # show mc embarrassed at mc_emotes

    mc """
    
    What? A frog? No— no!

    I'm sorry, I was in my head. No ghosts, no frogs.

    Were you in a meeting with Mrs. Roberts?
    
    """

    show bastion default

    "Student" """
    
    Yeah, I just moved here. 
    
    The advisor was just getting me set up with what I should do this semester.

    """

    """
    
    He looks down, hands stuffed into his pockets. Tendrils of curly hair sweep over his face, towards a sharp jaw and full lips.

    Everything about him is almost too perfect.

    """

    mc """
    
    Woah, changing schools? You are braver than me.

    The idea of any credits not being accepted at a new college freaks me out.

    """

    "Student" """
    
    Oh, I'm not worried about that. 
    
    I'm just coasting right now anyway... You know, {i}real{/i}.
    
    """ # using {} {/} is how you do bold and italics and such inside text

    # show mc shocked at mc_emotes

    """

    Who coasts during college??

    If he doesn't have all his credits, he'll be stuck doing more years than necessary.

    That's literally a fate worse than death.

    According to Dad anyway.

    """

    roberts "[mcname]? You can come in now."

    "Mrs. Roberts leans against the door frame, a slight smirk on her face as she glances between me and the new kid before slipping back into her office."

    "Student" "[mcname]? Pretty name."

    "My cheeks start to burn."

    "Student" "I'll see you later maybe?"

    # show mc blush at mc_emotes

    "Just as I open my mouth to respond, the same two students from earlier walk past us again."

    "One points at me and whispers in the ear of her friend, and they both giggle."

    # show juniper and zoe default

    juniper """
    
    Hey, [mcname]!

    First time ever talking to a guy? I didn't know a face could get so red!

    """

    menu:
        "Ugh. I can't stand her."

        "I stand my ground, after all, there's nothing to be embarrassed about!": 
            if (stats["assertive"] >= 15):
                $ mod_stat(-1, "self")
            $ mod_aff(10, "Bastion") # gain points w/ bastion
            $ flags["Learned NK Name"] = True
            call talked_back_rude
        "I'm too embarrassed to face him right now...": # default choice if stats not high enough
            call didnt_talk_back_rude

    jump advisor_scene_1

label talked_back_rude:
    
    # show mc mad at mc_emotes

    mc """
    
    You've been stalking the new student while giggling behind your hands thinking no one else is watching you.

    But you are being so obvious.

    Do you even know his name? Or are you guys fine just creeping on a good looking guy?

    """

    # show juniper and zoe shocked

    zoe "You'll regret this!"

    juniper "Y-Yeah!"

    "They both turn heel and speed away, practically leaving dust in their wake."

    show bastion amused

    "Student" "That was impressive. The name's Bastion, by the way."

    "I blush, just now realizing that I also was too enamored by his looks to ask his name."

    # show mc blush at mc_emotes

    mc "That's also a pretty name."

    roberts "[mcname]?"

    "Mrs. Roberts' head peeks out of her room."

    show bastion default

    bastion "Hopefully, I'll catch you around."

    hide bastion with dissolve

    "He turns and walks off. Mrs. Roberts coughs loudly."

    "I turn to see a raised eyebrow on her face."

    roberts "I don't have all day."

    return

label didnt_talk_back_rude:

    "They burst out laughing and walk away."

    # show mc sad at mc_emotes

    "I hurry into the advisor's office, too embarrassed to face his reaction to such public humiliation."

    roberts "I'll see you later, Bastion. Good luck on your first week."

    "Mrs. Roberts says goodbye to the new student, and I make a mental note to remember his name."

    "{i}Bastion{/i}, it's a pretty name as well."

    "I wish I had the courage to tell him that."

    return

label advisor_scene_1:

    roberts "Do you want to talk about what just happened out there?"

    "{i}Absolutely not!{/i}"

    "I can't get Bastion's mysterious eyes out of my mind..."

    "But that's {i}definitely{/i} not something to tell Mrs. Roberts."

    mc "You said there was a problem with my resume?"

    "She sighs deeply."

    roberts "Yes, of course. I wanted to talk to you about your credit hours."

    "She sets down a list outlining all the classes I've taken and what requirements they fill."

    roberts """
    
    I know you prefer to handle your own affairs, but I couldn't help but notice something.

    You are still lacking some higher level credits.

    """

    # show mc annoyed at mc_emotes

    mc "Me? Missing credits???"

    roberts "Yes, you. I have a feeling you got confused somewhere along the way."

    "She puts out two nearly identical handbooks."

    roberts "This is the course catalog I believe you've been using..."

    "Mrs. Roberts points to the one of them."

    roberts "And this is the one you {b}should{/b} have been using."

    """

    I stare blankly.

    I've been using the wrong course catalog?

    Me???

    """

    roberts """
    
    You are lucky I caught this for you before you found out the worst possible time.

    Really, it's on me too for just allowing you to pick and choose your own courses.

    You might be diligent, but you are still young.

    """

    """
    
    I kick back in my seat.

    I have to take another class this semester.

    Leafing through the pages of the {i}correct{/i} course catalog, I see that if I don't fix this mistake now...

    I'll be here longer than 4 years.

    Dad will be so mad...

    If he finds out.
    
    """

    roberts "Now, I've pulled together a list of courses that I think you could take based on my notes of our first meeting."

    "She sets another sheet of paper on top of my resume."

    roberts """
    
    Here's a list of classes with at least one opening which fit the requirements.

    """

    menu day_one_club_select:
        "Grant Writing 340":
            $ mod_aff(5, "teddy")
            
            mc "What about grant writing?"
    
            # roberts default
            
            roberts """
            
            That's a great choice! I thought you'd like it.

            """

        "String Ensemble 300": 
            $ mod_aff(5, "bastion")
            
            mc "String Ensemble sounds easy enough, I did violin in middle school and was pretty good at it."
    
            # roberts giggle
            
            roberts "Something tells me you'd {i}really{/i} like that one."

        "Gaming Culture and Engagement 302": 
            $ mod_aff(5, "felix")
            
            mc "We have a gaming classes? That sounds sort of fun."
    
            """
            If I'm going to get in trouble... 
            
            Maybe I should have a bit of fun before it all comes crashing down.

            """
    
    jump advisor_scene_2
        