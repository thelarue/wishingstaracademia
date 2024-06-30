label day_one_go_home:

    stop music

    scene bg mc room

    """

    I get home just in time to make myself look busy.

    At my desk, I quickly pull out my books from my bag and get to work.

    After some time, I hear Dad's car pull up to the house.

    Dad loudly opens the front door downstairs as if to announce his agitation as well.

    I can hear the sound of Dad's loud footsteps as he makes his way upstairs.

    My heart starts to beat loudly.

    """

    play music broken_constellation

    """

    I didn't do anything wrong.

    He's not going to lecture me today.

    My grades are great. I'm about to graduate.

    Everything... is fine.

    """

    dad "[mcname]."

    """
    
    He calls my name from outside the door, his voice ominous.

    My bedroom door creaks open as I sense his presence first.

    I turn to see my Dad's statue-like figure.

    """

    mc "Hey, dad! Sorry, I didn't know you were home."

    dad "I heard that you were seen talking to a boy today."

    "{i}What?{/i}"

    mc "A boy? Oh, I was just asking for information about classes."

    dad """
    
    I heard you were alone with that boy for quite some time.

    What could you have to talk about with anyone for so long?

    """

    if stats["self"] < 9:
        call day_one_dad_argument
    else:
        call day_one_dad_no_argument

    # Return from that

    dad "So you say."

    """
    
    I could tell I was safe from his wrath.

    For now, at least.

    How did he find out? Who told him?

    """

    dad """
    
    You best do well in class. 

    If you need anything, you come to your father.

    Understand?

    """

    mc "Yes, sir."

    dad """
    
    Good. Now get back to studying.

    """

    jump day_one_ending

    
label day_one_dad_argument:

    mc """
    
    My advisor said I needed to take another course this semester to graduate on time.

    So I just wanted to see what other students thought about my options.

    """

    dad """
    
    You couldn't talk to the instructors? 

    You couldn't talk to me?

    """

    mc "You don't exactly make it easy."

    "No. I didn't just say that outloud."

    dad """

    When I decided to support you and co-sign your loans, I gave you very simple rules.

    Maintain a 4.0. Take school seriously.

    And no boys.

    If you're so determined to make a fool of me, then perhaps I should rescind your opportunity to join my company.

    """
    mc "Please, don't, Dad."

    "I fought to maintain my composure."

    mc "I'm sorry. I won't disobey you again."

    return

label day_one_dad_no_argument:
    stop music

    mc """

    Sorry, Dad. 

    It was a small group project, and those are hard to do online.

    """
    return

label day_one_ending:

    stop music
    play music starlight serenade
    scene bg galaxy

    """
    It's dark now, the sky so clear that I can see every bright star flickering in the distance.
    
    This was Mom's favorite type of night. She'd point at each star and give it an entire name and back-story.
    
    She also somehow always knew when a wishing star was about to come shooting across the sky.
    
    But she'd tell me to wait to wish until I saw the right one.

    I spot a star falling across the sky.
    
    I lift my head, but there was nothing special about that star.

    The star flashes brightly like a diamond.

    As I stared at it, I had a feeling that it was... important.

    """

    menu:
        "Maybe I should make a wish...?"

        "I wish to have a close group of friends before I graduate.":
            $ mod_aff(5, "Teddy")
        "I wish to have a better social life before I graduate.":
            $ mod_aff(5, "Bastion")
        "I wish for good grades and high scores on my finals.":
            $ mod_aff(5, "Felix")
        "I wish Mom was home.":
            $ mod_aff(5, "Wish")
    
    return
