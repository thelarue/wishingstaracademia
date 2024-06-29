# #############################
# Day One gaming club visit
# #############################
label gaming_club:

    scene bg gaming room

    "Before Dad scolded me over wasting my time on video games, I had spent the first two years of high school playing on a competitive squad."
    "It was the last time I felt like I had actual friends."
    "I really liked it"

    mc "Hello?"

    "The room is empty, but there's a computer still running on the main menu of a side-scrolling game."

    menu play_side_scroller:
        "A quick game won't hurt anyone.":
            $ mod_aff(5, "Felix")
            jump day_one_gaming_play_side_scroller
        "I better leave it alone; it's a waste of time.":
            jump day_one_gaming_no_side_scroller

    # Return from the side_scroller
    mc "Wait..."

    "I pull out the sheet of paper Mrs. Roberts had given me and read the name of the team captain."

    mc "You're the team captain?"

    felix "Deja vu, right?"
    felix "Why? You're not thinking of joining, are you?"

    # show mc pensive   
    "I wasn't too confident about the idea of joining a gaming club in the first place..."
    "I really liked being a part of the Gaming Club in high school, even if I was distraught when Felix made those accusations."
    "I'd never admit it aloud, but the competitive monster inside me is gnawing it's way out of my skin."
    "And seeing Felix be arrogant and confident really makes me want to knock him down from the pedestal he's put himself upon."

    # show mc defiant
    mc "Actually, I am here to sign up. Where's the sheet?"

    show felix annoyed
    felix "First of all, there's no physical sheet. This isn't the 2000s, everything is digital."
    felix "Not to mention, there's no way you'd be able to pass the gauntlet anyway."
    
    mc "Gauntlet?"
    "Felix hands me a pamphlet from a pile on one of the desks. Three video game titles are listed on it, each one with a specific criteria to beat."

    felix "You have to clear in all three challenges before you can be considered one of the elite. And they're not easy." 
    felix "Trust me, I'm the one who came up with them."

    # show mc defiant 
    "I scan the challenges."

    mc "You must have been slacking off since high school if you think these are challenges."

    mc "The first one is beat the current team captain on Armored Power 3, do you have time to play tomorrow?"

    "I used to beat him one on one in Armored Power 1, back in high school."

    felix "This time tomorrow, right here at the Gaming Club Room."
    felix "I'll show you how much better I am now."

    # show mc defiant

    mc "Can't wait."

    """
    I can't help but smirk as I leave the room, brushing past his arms.
    I didn't realize at first how much he's grown since high school.
    But he's much taller, his arms are bulkier, and there's a deep, scratchy tone in his formerly high-pitched voice.
    I shake my head, Felix is my arch nemesis!
    """

    ##############
    # Post gaming club.
    # This whole section probably needs to be re-written though
    # So much is not here if you don't go here. And it's kind of a full additional scene.
    ###############

    scene bg university hallway

    "I walk back into the main university's hallway after leaving the gaming club."

    student "[mcname]! There you are! We've been texting you all day!"
    "I turn around and find two of the closest friends I've ever had, Lanie and Bryce, clutching their backpacks and tapping their feet."

    lanie "You skipped lunch, are you okay?"

    mc "Yeah! I had a meeting with Mrs. Richards."
    mc "She said I needed to add an extra-curricular to my resume, so I'm going between them all to see which one I like the most."

    bryce "A club? You?"
    bryce "We begged you to join the Debate Club for years! Why now?"

    mc "I wondered that too, but who am I to argue with a guidance counselor?"
    mc "Plus, if she really thinks it'll help my resume I figured it couldn't hurt to try."
    mc "I know it'll be hard to convince my dad..."

    lanie "He'll understand eventually. Wasn't he in a club too?"
    
    mc "He was in the soccer club, and mom in the string ensemble club."
    mc "I'm interested in both, plus maybe the gaming club."

    lanie "Gaming club? You do know who's the team captain, right?"

    bryce "Wait, we have a gaming club?"

    mc "Yeah, I was surprised too."
    mc "And I know Felix is the team captain, I just talked to him."
    mc "We're battling each other tomorrow."

    lanie "Oh, I bet he's really excited about that."

    "She nudges me with her elbow."

    mc "What's that supposed to mean?"

    # How does this even sort of make sense in light of the "I'm running a smear campaign and making everyone hate the MC"?
    lanie "Just that Felix's had a crush on you for over five years now."
    lanie "Or are you going to keep denying it?"

    mc "Felix definitely doesn't like me like that!"
    mc "If anything, it feels like he hates me."

    lanie "I'm sure."
    lanie "Anyway, we're almost late to our afternoon class."

    bryce "Call us back, okay?"
    bryce "We gotta talk about what we're doing for summer!"

    """
    We say our goodbyes, and I watch as they walk down the hallway together.
    Both Lanie and Bryce have been great friends since Lanie and I met Bryce freshman year of university. 
    They seem to have gotten closer to one another, and I'd be lying if I said I didn't sometimes feel left out.
    Hopefully our summer trip will help strengthen our bond before we all branch out to separate career fields. 
    I can't dwell too much on it, after all there's still a few things left to do today. 
    """
    # End the gaming_club visit
    jump day_one_club_visits

label day_one_gaming_play_side_scroller:
    "I take a seat at the computer and start a new game."
    "I send a little sprite running across the screen, collecting stars and jumping over traps as I try and beat the high score pinned to the upper right corner of the screen."
    "It doesn't take long before I'm only a few hundred points away, but there's a tricky jump just ahead of the screen."

    show felix arrogant

    student "Good luck, I've been trying to beat the high score for weeks, but I can't get past that jump AND get all the stars."

    "My character clears the tricky jump with too much momentum, throwing them off screen but then landing onto the next platform, a trail of stars circling the sprite."
    "The high score on screen flashes as it updates to my score."

    show felix shocked 

    student "What?! How did you!?"
    
    "I turn to look behind me, toward the raising voice of a student. It's a familiar voice, grating against my ears."

    mc "Felix?"

    show felix arrogant

    "I was poised to be the team captain of my squad during my sophomore year, but my arch-nemesis ran a smear campaign against me using completely unsubstantiated allegations of illegal modding."
    "However, their campaign was successful and they were selected as team captain, leaving me shunned by the squad."

    "And here he was, standing right behind me."
    
    felix "I should have known like you would cheat to beat that score."

    # show mc angry at mc_emotes

    mc "We haven't spoken in years and first thing you say to me, more cheating allegations?"

label day_one_gaming_no_side_scroller:

    mc "I shouldn't waste my time on a Gaming Club anyways, not after what happened last time."

    show felix arrogant

    felix "You're still stuck on that?"

    "I jump forward in into the room then turn to see the only student with better grades than me."
    "He's also half of the reason I've not played video games competitively since high school."

    felix "It was years ago, anyone else would have gotten over it by now."
    
    mc "Accusing someone of cheating just to become team captain while ostracizing them from the rest of the club isn't just something to get over."
