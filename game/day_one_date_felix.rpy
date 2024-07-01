label day_one_date_Felix:
    # The BG scene isn't changed at all. 
    # Open with the Felix showing up and asking her what she is doing

    stop music

    play music daily_journeys

    show felix default

    felix "You're still here?"
    
    felix "Aren't you like an hour late for your bedtime?"

    mc "I actually still have a few hours before curfew."

    show felix shocked

    """
    
    Felix gives me a bewildered look.

    Was it something I said?

    """
    
    mc "What about you? You don't live on campus but you're literally always here."

    show felix default

    felix  "The PCs here can run the newest Kingdom Archives game."

    "His shrug is nonchalant."

    felix "My laptop at home can barely handle a single online game without dying to the lag."

    mc "There's a new KA game?"

    """
    
    Felix and I played the last release of Kingdom Archives together when we were still on talking terms.

    Kingdom Archives is probably one of the most niche MOBAs on the market...

    But we both couldn't help but get suckered in by the colorful characters.

    And awful lore.

    """

    felix "Yeah! It's really good."

    show felix arrogant # would be tsundere if I had that image

    felix "If you want, I can show you a quick game."

    "Even King Felix has no one else to talk to about this game."

    if stats["compassion"] >= 10: # Poor Felix, you asshole
        "I give a resigned sigh."

        mc """
        
        Okay, but it has to be really quick.

        I won't be able to play it myself anytime soon, anyway.

        """

        $ mod_aff(5, "Felix") # He likes that you gave in, the prick
    
    else:
        mc "I'm actually really busy right now."

        show felix shocked # or begging lol

        felix "Oh, come on, [mcname]!"

        "He looks at the ground with a pouty face."

        felix "You know barely anyone else plays this game."

        """
        
        Ugh. I can't take the guilt.

        What a low blow to deal to a fellow fan.

        """

        mc "Fine... Let's go."

    hide felix default with Dissolve(1)

    # move to gaming room with a dissolve
    scene bg gaming room with Dissolve(2)
    
    "I follow him into the gaming room."

    "He pulls out a chair in front of a PC already logged into Kingdom Archives and gestures at me to sit."

    show felix default

    felix "I assume your card's locked until after mid-terms, right?"

    mc "How'd you know?"

    felix "Your dad locked it every year around this time in school."

    felix "Not surprising that he still does it."

    "He leans over me, and I try to remember the last time we were this close to each other physically."
    "He navigates through several menus and an online match-making screen shows."
    "After a few moments, a match is found and battle screen fades in." 
    "Two assassins face off from each other."
    "The controls feel familiar, but Felix still gives me helpful instructions as the match begins and I take control."

    mc "Hopefully it's the last year he locks it."

    "Felix sits next to me and watches as my match progress."

    mc "Next year, we'll both be at Rising Star Financial and managing our own finances."

    felix "Why does it sound like you're excited to be stuck with me in our post-grad career?"

    felix "Obsess much?"

    "I blush and wince a bit."

    mc "You know that's not what I meant."

    mc "I could care less if you get a job at the same company as me."

    show felix arrogant

    felix "First, it's {i}couldn't{/i} care less, so I guess you care quite a lot."

    felix "Second, well, I guess I wouldn't mind it."

    "Despite my familiarity, I lose the first round miserably after hearing that."

    felix "Wow, you still suck."

    mc "It would be easier if you weren't throwing off my groove."

    """
    
    He chuckles, and I playfully shove his shoulder with my own.

    Then it gets awkward.

    """

    show felix default

    """

    We used to be closer friends in high school until he started making things up about me.

    Looking at him, I can't read if he regrets it or not.

    """

    felix "Hey, a new round is starting!"

    "The next round starts, and both assassins are staring each other down."

    "Felix wasn't always this confusing."

    "It feels like we could be friends again..."

    "I manage to win the battle."

    felix "I haven't really made any friends since university started."

    felix "So it's been kind of boring."

    mc "But I always see you walking with a group of people. I thought they were your friends?"

    felix "I don't even know half of their names."

    felix "And they definitely don't know mine."

    "I grin just as I win the second round."

    mc "You mean Eugene?"

    show felix angry

    felix "Don't say it so loud!"

    felix "Someone else might hear you!"

    "Before long, I've started a new match, my assassin is standing across from a warrior."

    mc "Sorry, sorry."

    mc "I didn't mean to say it like that."

    mc "But if they really don't know your name is Felix, why don't you tell just tell them?"

    "The round begins and there's a silence between us hanging in the air."
    "The match ends in another loss, and I've still not heard a peep from Felix."
    "I can feel time starting pass faster, and I keep playing more matches."

    show felix default with Dissolve(.5)
    "Felix breaks the silence suddenly."

    felix "Making friends just seems worthless these days."
    felix "None of them have any advantages for me."
    felix "And they don't even play games, so there's almost nothing for us to even talk about."

    mc "Well, I know in school we have to be competitive."
    mc "But maybe after school we can play some co-op games together again."
    mc "I kinda miss it."

    "For the first time, I finally see a small blush creep over Felix's cheeks."

    felix "Sure!"
    felix "I mean, I guess..."
    felix "If you really wanted to."
    felix "I am really busy these days but I can probably make some time for you."

    mc "Lucky me."
    "He can be such a tsundere sometimes."
    "I glance at the time on my phone, realizing how late it is."

    felix "You should get home before your dad gets mad like he alway does."
    "Back then, I'd stay at Felix's house late into the night, playing games."

    "I raise my eyes away from the screen and tilt my head, making a show of thinking."

    mc "I can probably stay a bit longer."

    "I shoot my eyes in his direction with a smile for a moment, before focusing back on the game."

    "I guess he still doesn't have anyone at home waiting up for him."
    "His mom passed away when we were in high school, and his dad was always absent on some work trip in a distant city."
    
    felix "Thanks, but I'm fine."
    felix "Almost done with the latest Tech-Mech 6 game."

    mc "Oh, I heard that was a good one."
    mc "You should tell me about it next time."

    felix "On our next date?"

    "Whoa. Wait."

    mc "That's not what I meant."

    felix "Sure, [mcname]."
    felix "Keep telling yourself that."

    """
    But we both laugh at the same time.

    It's a comfortable feeling, teasing each other and talking about games.

    I'm almost sad when we say goodbye and I leave him to head back home for the night.

    """
    scene bg university hallway with Dissolve (0.9)

    """
    The gaming room door closes slowly behind me with a click.

    It takes everything in me to not turn around and glance back at him through the window as I walk away from the door.

    Before long, I make my way off campus.    
    """
    jump day_one_go_home
    