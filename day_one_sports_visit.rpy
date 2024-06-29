# #############################
# Day One sports club visit
# #############################
label sports_club:
    scene bg sports field
    "Soccer was admittedly the first one that came to mind."
    "It's the only team Dad said I could consider, but only if I followed in his footsteps and did soccer, since he was the team captain at this same university." 
    "It's the easiest choice if I end up having to tell him about taking on an extra-curricular."

    "A soccer ball flies in front of my face, making me shriek and jump back in surprise."

    student "Sorry about that! I didn't see you!"

    show teddy default

    student "Oh! [mncname]? What are you doing here, neighbor?"

    "Teddy, my childhood friend."
    "We first met on the playground behind his house. I had crawled under our fence to play on it as soon as we moved into the neighborhood."
    "I jumped onto the monkey bars, but my grip was too weak and I fell mid-swing."
    "Teddy found me, splashed water on a cut on my knee and wrapped a bandage around it."
    "Then he asked me to wait until he's was around to play on the swings."
    "We were inseparable until we entered high school when he moved to live with his mom after his parent's divorce."
    "Still, he's one of the very few friends I've been able to keep for so long."
    
    mc "Teddy! You're the only person I'd ever forgive for pelting me in the face with a soccer ball."
    "Is he... blushing?"
    mc "I'm here to ask about signing up for the co-ed soccer team!"

    teddy "Then you're talking to the right guy! I didn't know you were interested in soccer. You only played in middle school, right?"

    mc "Yeah, but we had so much fun!"
    mc "I wasn't that bad, was I?"

    student "Teddy! There you are!"

    "Bea, a bully I've known since high school, shoves me aside."

    bea "Oops, sorry [mcname], I never notice you."

    leah "Remember when [mcname] showed up to graduation and even the principal didn't know who she was? That was so embarrassing!"

    "They both snicker into their hands."

    leah "Oh no, [mcname], you weren't planning on joining the soccer team, were you?"
    leah "Sadly, there aren't any spots left."

    menu sports_club_mean_girls_choice:
        "They're right, unfortunately...":
            call day_one_sports_club_mean_girls_sad_choice
        "Stuck in high school... But why is Bea wearing a leg brace?":
            $ mod_aff(5, "Teddy")
            call day_one_sports_club_mean_girls_brace_choice
    
    # Come back here after the choice

    show teddy default

    teddy  "Oh yeah! You just need to prove yourself first. Score three goals during on obstacle course in front of the team, and then you're in!"

    "My phone pings as he texts me the criteria."

    teddy  "If it were up to me I'd let you on immediately, but a former team captain started this tradition a long time ago." 
    teddy  "I'll still help you through it! Meet me here tomorrow around this time and we can get started."

    mc  "Thank you Teddy! I should get going, but I'll see you tomorrow!"

    teddy "Anytime, [mcname]. I'm always happy to see you."
    "Why am I suddenly blushing?"
    "It can't be because of Teddy, right?"
        
    # Back to the club selection menu
    jump day_one_club_visits

# Mean Girls choice
# Big sad 
label day_one_sports_club_mean_girls_sad_choice:
    mc "..."
    "How could I ever forget how humiliating that was? Especially since it was the day after..."
    show teddy angry
    teddy "It's embarrassing to still be talking about high school as adults."
    teddy "And we actually do have a spot available, Bea. I don't expect coach to let you back on the team for a while."

    leah "We were just joking!"
    bea "We're all friends! Right, MC? It was just a joke."

    "Teddy has always gone a little above and beyond in defense."
    "He enjoyed bullying the bullies a little too much."
    "But he's still generally known as the campus' golden retriever. Just a brown haired-puppy that's admired by everyone."
    "I don't want to make things any more awkward for him."

    mc "Yeah, it's a joke between us. Like, ha-ha I'm so normal and plain."
    mc "It's hilarious if you really think about it."

    show teddy default 
    teddy "If you say so..."

    "Bea and Leah nod frantically before scurrying away."

    teddy "But if they're giving you a hard time you just let me know, okay?"

    mc "I promise I will! Anyway, about the club?" 
    return



# Mean girls choice
# Leg brace
label day_one_sports_club_mean_girls_brace_choice:
    "I couldn't imagine still being so obsessed with high school and popularity. It must be exhausting."
    "I notice Bea limping on her left leg while wearing a leg brace."
    mc "And are you sure there's not a spot available? I heard someone sprained their ankle and got benched. I do hope they're okay..."

    show teddy default
    
    teddy "[mcname] is right, you guys should really move on to caring about something else."

    bea "Whatever. Teddy, I'll find you after you're done talking with [mcname] . We still have that history project to do together."

    leah "Yeah, Teddy, we'll talk to you later."

    "They both leave as Teddy leans towards me."

    # This isn't how college works -_-
    teddy "I'll talk to them later. They're usually nice to me, but if they're that mean to you, I'll totally make sure they flunk the history project."

    mc "Thanks, Teddy. But that's okay. You taught me how to look after myself before you left."

    show teddy happy

    teddy "That's right! Although I'm pretty sure I also taught you how to knock someone out. Don't think you've used that technique yet, right?"

    mc "Not yet, thankfully. I'll let you know when I do. But in the meantime, do you think I'd be able to join the soccer team?"
    "The thought of spending more time with Teddy makes my heart flutter."
    "But why?"

    return


