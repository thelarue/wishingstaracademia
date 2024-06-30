label day_one_date_Bastion:
    
    stop music
    
    play music daily_journeys # if a fuller version was made, bastion might have his own song? idk

    scene university hallway 

    """
    
    ... What a long day. 
    
    I'm about to leave when I hear someone call my name.
    
    """

    bastion "Hey, [mcname]."

    show bastion default

    """
    
    I turn to see Bastion wave at me from across the hallway.
    
    Returning his wave, I walk over.
    
    """

    bastion "You're here later than most students."

    mc """

    I had a lot to do today.

    You're here pretty late yourself.

    I saw your practicing earlier, you were incredible!

    """

    show bastion amused

    bastion """

    Oh, you saw that?

    I hadn't done that song in months.

    I was pretty rough sounding, right?

    """

    show bastion concentrated

    "He blushes as he runs a hand through his hair."

    if stats["assertive"] >= 5: # if MC assertiveness is over 5

        # show mc no at mc_emotes

        mc """

        No way!

        It sounded so natural. 

        """

        $ mod_aff(5, "Bastion") # thanks for the compliment
    
    mc "That song sounded familiar, what song was it?"

    show bastion default

    bastion """

    Oh, that was an original.

    Well, based on my mom's story, but I wrote the music.

    """

    mc "Your mom's story?"

    bastion """
    
    My mom's a published author, so for Mother's Day every year I compose a song for her.

    If you have a moment... I could show you?

    """

    mc "Absolutely!"

    stop music

    scene music club with dissolve

    """

    I follow Bastion back into the music room.

    I pull up a chair as he fishes through the backpack he left in the music room.

    He frees a phone and takes a seat besides me.

    """

    show bastion concentrated

    bastion "Here's the song."

    play music violin_practice

    """

    He plays a song from his phone as I sit next to him.

    It's slow and sweet, with moments that make me almost want to cry.

    """

    if stats["creative"] >= 10: # if MC creative is over 10
        
        $ mod_aff(5, "Bastion") # he likes that you noticed

        mc """
        
        This song is bittersweet... It sounds like it could play during a hard truth in a movie.

        Or maybe when two lovers part for the best. That sort of thing.

        """

        show bastion amused # would be shocked IF I HAD ONE lol

        bastion """

        Wow, that's exactly what I was going for.

        The story was about a woman going through a divorce, but ultimately moving on from it.

        Heavy stuff, right?

        """

        mc """

        For sure! 

        You know, I play the violin too.

        Mostly classical stuff.

        """

        "When Dad isn't home anyway..."

    else:
        
        bastion """
        
        This song is based on a pretty heavy story about a woman going through a divorce.

        Near the end, she realizes it was for the best, but it still makes her sad.

        I hope I conveyed that well enough.

        """

        call bastion_day_one_didnt_notice

    show bastion default

    bastion """

    You play as well? 

    Maybe you should join string ensemble if there is still room.

    I'm glad there was still room for me in class.

    """

    mc "How do you like it here so far, by the way?"

    bastion """
    
    It's alright, but I miss home.

    It wasn't my choice to  move here, but my mom's publisher wanted her near them.

    I didn't want her to have to move to a new city by herself.

    """

    "How sweet!"

    mc "That must have been a hard decision."

    bastion """
    
    It would have been, but the perks made it a little easier.

    My old school isn't nearly as impressive as Wishing Star Academia.

    When her publisher said they had connections that could help me get ahead in life, well, it was hard to turn down.

    """

    """
    
    Wishing Star Academia, or WSA as most people call it, is an ivy league school.
    
    You had to have pull with the school, money, or a lot of talent to get accepted.

    """

    mc "Even with their connections, you must have been a top student if you were accepted into our school so late in your coursework."

    bastion "I was in the top 3%, actually."

    "Wow. He's kind, thoughtful, AND smart?"

    mc "You're an impressive guy."

    show bastion amused

    "He covers his mouth as he shyly smiles."

    bastion "Thanks, but I'm not really that special."

    show bastion default

    bastion "What about you though? How'd you get into this prestigious university?"

    mc """

    Oh, I prepared for the application process since graduating elementary school.

    Both of my parents went here, and my dad stayed friends with the Dean and a bunch of professors who work here.

    He stayed friends specifically to give his future kids an edge, he said.

    """

    bastion "Wow, so you were clearly meant to attend this school."

    mc "To be honest, I probably would have been disowned had I been rejected."

    "It was meant as a joke, but the realization of how true that statement is hits me in a sad way."

    mc "Anyways, thank you for showing me the song. It's incredible."

    bastion "It was really nice talking to you, maybe we can hang out again?"

    mc "That would be fun!"

    "We exchanged details."

    show bastion amused

    bastion """
    
    Can't wait. I'll see you later, [mcname].

    Maybe in class, huh?

    """
    jump day_one_go_home

label bastion_day_one_didnt_notice:

    menu:
        "Say something profound. Be creative!":
            if stats["creative"] <= 10: # if this stat is 10 or lower
                $ mod_stat(-1, "Self") # Lose a sense of self, because MC is not that creative in this build of her
                $ mod_stat(1, "creative") # Gain a point for putting yourself out there
            
            mc """

            Now that you mention it, it does feel like a sad song with hope for something better to come.

            Yeah, she's divorced, but life goes on.

            I've never experienced a feeling like that, but it feels like you captured it well.

            I play the violin too, but I've never created anything on my own before.

            I mostly just play classical pieces.

            """
            $ mod_aff(5, "Bastion") # He appreciates the attempt to understand

            return 

        "I mostly just play the classics, myself.":
            mc """
            
            This might sound weird, but I have a hard time noticing stuff like that.

            I actually play the violin as well.

            Mostly, I stick to the classics.

            """

            "And only when Dad isn't home to hear me practice."

            return