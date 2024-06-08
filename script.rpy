# Wish Academia

define config.menu_include_disabled = True # Makes unavailable choices visible. They are invisible by default.

# This section defines all the characters. Hopefully their other traits like art will go here too.

define mc = Character("[mcname]")
define felix = Character("Felix", who_color="#fd271f")
define teddy = Character("Teddy", who_color="#28a028")
define bastion = Character("Bastion", who_color="#8f2d46")
define wish = Character("Wish", who_color="#FFC000")
define mom = Character("Mom")
define dad = Character("Dad")
define sharp = Character("Professor Sharp")
define roberts = Character("Mrs. Roberts")
define lanie = Character("Lanie")
define Bryce = Character("Bryce")
define prof1 = Character("Professor 1")
define juniper = Character("Juniper")
define zoe = Character("Zoe")
define bea = Character("Bea")
define leah = Character("Leah")
define cash = Character("Cash")

transform mc_emotes: # puts the mc's emotes at a specific location on the screen
    align(0.0,1.0)

# Stats here
default stats = {  # This is the stats dictionary. The names on the left are called keys, and the parts after the : is the data each key holds. 
    "self": 10,
    "attendance": 3,
    "assertive": 0,
    "creative": 0,
    "competitive": 0,
    "compassionate": 0
}

default affection = { # This is another dictionary. This one specifically stores info about the LI and their affection for MC. Seems good to keep these apart.
    "Wish": 10,
    "Bastion": 0,
    "Felix": 5,
    "Teddy": 20
}

default flags = { # This is a flag system, basically just try to remember what flag goes where!
    "Learned NK Name": False, # Did MC learn Bastion's name from him?
    "Sports Visited": False, # Has MC visited Sport Club yet?
    "Music Visited": False, # Has MC visited Music Club yet?
    "Gaming Visited": False, # Has MC visited Gaming Club yet?
    "Visited Any Club": False, # Has the MC visited any of the clubs? Allows repeat players to skip.
}

# When stats change, they can't go over or under certain threshold
init python:
    # Creates the clamp for stat things, basically will make it so nothing is less than 0 and nothing is more than 100.
    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))

    # Handles changing of the stats
    def mod_stat(change, stat_name):
        if stat_name in stats: # Checks to see if the stat being changed is actually in the stats dictionary. 
            stats[stat_name] += change # to break it down, stats[stat_name] means the dictionary[key] so for example if I am changing assertive, the computer reads it as stats[assertive]. += means add to the current exisiting total. Change is the variable for how ever much change is happening in the script. 
            stats[stat_name] = clamp(stats[stat_name], 0, 100) # This is telling the computer to compare the current total of that stat to 0 and 100. If its higher than 100, the number becomes 100. If its less than 0, it becomes 0.
            return stats[stat_name]
        else: # If the stat doesn't exist...
            print("Stat ", stat_name, " does not exist.")

    # handles the affection of LIs the same way as stats
    def mod_aff(change, love_interest):
        if love_interest in affection:
            affection[love_interest] += change
            affection[love_interest] = clamp(affection[love_interest], 0, 100)
            return affection[love_interest]
        else:
            print("Love interest ", love_interest, " does not exist.")

# This isn't the most elegant way to handle this, but it will do for a demo!
label assertive_start: # They jump to this menu when they choose the assertive option from the first menu in the start label. 
    menu:
        "I enjoy music. (Or whatever might suggest creativity lol)": 
            $ mod_stat(15, "creative")
            jump assertive_start_1 # jump signifies moving to a different scene, but in this case since no BG is involved, it doesn't change the BG at all.
        "I enjoy esports.":
            $ mod_stat(15, "competitive")
            jump assertive_start_2
        "... love cats. (lol)":
            $ mod_stat(15, "compassionate")
            jump assertive_start_3

label assertive_start_1:
    menu:
        "I enjoy esports.":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "compassionate")
            jump start_2 # brings player back into narrative
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "competitive")
            jump start_2

label assertive_start_2:
    menu:
        "I enjoy music. (Or whatever might suggest creativity lol)": 
            $ mod_stat(10, "creative")
            $ mod_stat(5, "compassionate")
            jump start_2
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "creative")
            jump start_2

label assertive_start_3:
    menu:
        "I enjoy music. (Or whatever might suggest creativity lol)": 
            $ mod_stat(10, "creative")
            $ mod_stat(5, "competitive")
            jump start_2
        "I enjoy esports.":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "creative")
            jump start_2  

label creative_start:
    menu:
        "... able to stand my ground.":
            $ mod_stat(15, "assertive")
            jump creative_start_1
        "... competitive option":
            $ mod_stat(15, "competitive")
            jump creative_start_2
        "... love cats. (lol)":
            $ mod_stat(15, "compassionate")
            jump creative_start_3

label creative_start_1:
    menu:
        "... competitive option":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "compassionate")
            jump start_2
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "competitive")
            jump start_2

label creative_start_2:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "compassionate")
            jump start_2
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "assertive")
            jump start_2

label creative_start_3:
    menu:
        "... am creative.":
            $ mod_stat(10, "creative")
            $ mod_stat(5, "competitive")
            jump start_2
        "... competitive option":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "creative")
            jump start_2

label competitive_start:
    menu:
        "... able to stand my ground.":
            $ mod_stat(15, "assertive")
            jump competitive_start_1
        "... pretty creative.": 
            $ mod_stat(15, "creative")
            jump competitive_start_2
        "... love cats. (lol)":
            $ mod_stat(15, "compassionate")
            jump competitive_start_3

label competitive_start_1:
    menu:
        "... pretty creative.": 
            $ mod_stat(10, "creative")
            $ mod_stat(5, "compassionate")
            jump start_2
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "creative")
            jump start_2

label competitive_start_2:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "compassionate")
            jump start_2
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "assertive")
            jump start_2
    
label competitive_start_3:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "creative")
            jump start_2
        "... art.":
            $ mod_stat(10, "creative")
            $ mod_stat(5, "assertive")
            jump start_2

label compassionate_start:
    menu:
        "... able to stand my ground.":
            $ mod_stat(15, "assertive")
            jump compassionate_start_1
        "... pretty creative.": 
            $ mod_stat(15, "creative")
            jump compassionate_start_2
        "... competitive option":
            $ mod_stat(20, "competitive")
            jump compassionate_start_3

label compassionate_start_1:
    menu:
        "... pretty creative.":
            $ mod_stat(10, "creative")
            $ mod_stat(5, "competitive")
            jump start_2
        "... competitive option":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "creative")
            jump start_2

label compassionate_start_2:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "competitive")
            jump start_2
        "... competitive option":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "assertive")
            jump start_2

label compassionate_start_3:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "creative")
            jump start_2
        "... pretty creative.":
            $ mod_stat(10, "creative")
            $ mod_stat(5, "assertive")
            jump start_2

# The game starts here.

label start:
    # Let the player name the MC.
    python:
        mcname = renpy.input("What is your name?", length=32)
        mcname = mcname.strip()

        if not mcname:
            mcname = "Dahlia"

    # There are a lot of pieces of code commented out because we may or may not actually use them.
    # Initializes the calendar, the month, day, and year should be changed to fit
    # whatever we are using in game for a date.
    # $ calDate = calDate.replace(second=10, hour=12, minute=30, day=20, month=8, year=2024)

    # Causes the calendar to appear on the screen and scroll X to the side to a new date.
    # In this case, its 1 day.
    # call calendar(1)

    # Currently this shows the stats button which when pressed. Can be used to show other things as well.
    show screen gameUI
    scene bg galaxy

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show (outline of mom)

    "It's always the same dream."
    "A wishing star, that's what Mom always called it, shooting across the sky,"
    "And Mom kneeling beneath it, her hands clasped together."

    # move mom center

    "Before she was taken away she used to tell me about her final wish."
    "She said she was saving it for me, and that she couldn't wait to watch it come true together."

    scene bg hospital

    # CG mom being dragged away

    "I wish she would have told me how to use that wishing star."
    "I would have used it back then."

    "My mother wished for me to be brave, to take chances..."

    menu:
        "I would say I'm..."

        "... able to stand my ground.":
            $ mod_stat(20, "assertive")
            jump assertive_start
        "... pretty creative.": 
            $ mod_stat(20, "creative")
            jump creative_start
        "... competitive option":
            $ mod_stat(20, "competitive")
            jump competitive_start
        "... love cats. (lol)":
            $ mod_stat(20, "compassionate")
            jump compassionate_start

label start_2:
    scene bg hallway

    # show robertsselor angry

    roberts "[mcname]?"
    ". . ."
    roberts "Are you asleep again?"
    ". . ."
    roberts "[mcname]? You're 15 minutes late for our appointment."
    ". . . . . ."
    roberts "[mcname]!!!"
    show mc emba at mc_emotes
    # wait 1.5 seconds then
    pause 1 
    hide mc # hide the emote
    mc "I'm so sorry! I just closed my eyes for a second. I'll be right there!"
    # show roberts default
    roberts "It's alright."
    roberts "Just come to my office in ten minutes."

    # show mc default

    "I stuff my books into my backpack and ignore the curious eyes following my every move."
    "Stay out of the light, Dad says."
    "Don't cause any unncessary trouble and DEFINITELY don't be caught slacking off-"
    "Or I'll never get a job at Rising Star Financial Group."
    
    show mc happy at mc_emotes
    pause 1 
    hide mc 
    "Thankfully the counselor's office isn't too far away. And Mrs. Roberts has always had a soft spot for me."
    "I lean against the wall outside her office."
    "The door is closed, she must be talking to the student with the appointment slot after mine."
    "In just six more months, I won't see Mrs. Roberts anymore."

    show mc emba
    pause 1 
    hide mc 
    "Six months to get my resume together to apply at Rising Star Financial Group."

    "Student" "Are you okay? You look like you just saw a ghost."

    "I hadn't even realized Mrs. Roberts's door open in the midst of my anxiety attack."

    "A guy my age stands in front of me, head tilted as he waits for my answer."

    "But my mind goes blank as our eyes meet."

    "And then the rest of his profile comes into view and my jaw nearly falls open."

    show bastion default # cg ? lmao

    "He's... he's beautiful! Is he really just a student?"

    "Two students talk past, both giggling to each other as they stare at the new student."

    show bastion #concern

    "Student" "Maybe not a ghost, after all. Now you look like you just ate a frog."

    show mc emba at mc_emotes
    pause 1 
    hide mc 
    mc "What? A frog? No- no!"

    mc "I'm sorry, I was in my head. No ghosts, no frogs."
    mc "Were you in a meeting with Mrs. Roberts?"

    show bastion default

    "Student" "Yeah, I just transferred. Mrs. Roberts was helping me with my schedule."
    "He looks down, hands stuffed into the pockets of fashionably ripped jeans. Tendrils of curly hair sweep over his face, toward a sharp jaw and full lips."
    "Everything about him is almost too perfect."

    mc "Woah, transferring this late in the semester is scary. You're a lot braver than I am."
    "Did I really just say that?"

    # bastion react

    mc "Not that you won't be able to get a good job afterward! I'm sure it's not too late for you!"

    # bastion default

    "Student" "Oh, I'm not too worried about that. I'm just trying to enjoy my last year before the world becomes, you know, real."

    "What does he mean???"

    "There's no way that he doesn't have five prospective employers lined up after graduation?"

    # roberts default

    roberts "[mcname]? You can come in now."

    "Roberts leans against the door frame, a slight smirk on her face as she glances between us before slipping back into her office."

    # bastion default

    "Student" "[mcname]? That's a pretty name."

    "My cheeks start to burn."

    "Student" "I'll see you later maybe?"

    # mc react

    "Just as I open my mouth to respond, the same two students from eafelixier walk past us again."
    "One points at me and whispers in the ear of her friend, and they both giggle."

    # rude girl1

    juniper "Hey, [mcname]!"
    juniper "First time ever talking to a boy? I didn't know a face could get so red."

    menu:
        "Ugh. I can't stand her."

        "I stand my ground, after all there's nothing to be embarrassed about! Available if Assertive is at least 10" if (
            stats["assertive"] >= 10): 
            $ mod_aff(10, "bastion")
            $ flags["Learned NK Name"] = True
            jump talked_back_rude
        "I'm too embarrassed to face him right now...":
            jump didnt_talk_back_rude

label talked_back_rude:
    show mc mad at mc_emotes
    pause 1 
    hide mc 
    mc "You've been stalking the new student while giggling behind your hands thinking no one else is watching you, but it's really obvious to everyone else."
    mc "Do you even know his name? Or are you guys too obsessed with just creeping on a good looking guy?"

    # Rudes shocked

    juniper "You'll regret this!"

    "They both turn heel and speed away, practically leaving dust in their wake."

    show bastion default

    # bastion amused # swap to this.

    "Student" "That was impressive. The name's Bastion, by the way."

    "I blush, just now realizing that I also was too enamored by his looks to ask his name."
    
    show mc happy at mc_emotes
    pause 1 
    hide mc 

    mc "That's also a pretty name."

    roberts "[mcname]?"

    "Roberts's head peeks out of her room."

    roberts "I don't have all day."

    # bastion default
    bastion "Thanks, hopefully I'll catch you around."

    "He turns and walks off as Roberts raises an eyebrow at us."

    jump counselor_scene_1

label didnt_talk_back_rude:
    "They burst out laughing and walk away."

    show mc sad at mc_emotes
    pause 1 
    hide mc 

    "I hurry into the counselor's office, too embarrassed to face his reaction to such public humiliation."

    # roberts default

    roberts "I'll see you later, Bastion. Good luck on your first week."

    "Roberts says goodbye to the new student, and I make a mental note to remember his name."

    "Bastion, it's a pretty name as well."

    "I wish I had the courage to tell him that."

label counselor_scene_1:
    # scene bg counselors office

    roberts "Do you want to talk about what just happened out there?"

    "Absolutely not!"

    "I can't get Bastion's mysterious eyes out of my mind..."

    "But that's definitely not something to tell my counselor."

    show mc sad at mc_emotes
    pause 1 
    hide mc 

    mc "You said there was a problem with my resume."

    "She sighs deeply."

    roberts "Yes, of course. I wanted to talk to you about your extracurricular activities."

    "She sets down my resume on her desk, and I skim through the short but sweet resume."

    roberts "Or lack thereof."

    show mc emba at mc_emotes
    pause 1 
    hide mc 

    mc "My dad told me to focus on grades first, and that clubs aren't important in university. I know I'm not valedictorian but there's not many students with better grades than mine."

    "There's two students, to be precise." 
    
    "The top student is a sweet gifelix who invites me to a study session twice a year for the past three years."

    "And the second is... well..."
    
    "I won't mention him if I don't have to."

    # roberts default

    roberts "I understand that, but when your resume looks identical to thousands of others that are submitted at the same time each year you really need something else to stand out."

    roberts "A club would look really good on this."

    "I kick back in my seat."

    "A club?"

    "I barely even have time to listen to music, and finals are coming up soon."

    "Plus..."

    "Dad would be so pissed."

    roberts "I can tell that you're hesitant, but it wouldn't hurt to check some clubs out."

    "She sets another sheet of paper on top of my resume."

    roberts "Here's a list of clubs with at least one opening that need help with the end of the year festival. Most would look great on your resume."
    
    roberts "There's a few that- well, is just for the team-building experience."

    show mc emba at mc_emotes
    pause 1 
    hide mc

    menu:
        "Out of the clubs listed on the sheeet, I'm most interested in..."

        "Sports Club": 
            $ mod_aff(5, "teddy")
            jump check_sports1
        "Music Club": 
            $ mod_aff(5, "bastion")
            jump check_music1
        "Gaming Club": 
            $ mod_aff(10, "felix")
            jump check_gaming1

label check_sports1:
    mc "What about the sports club?"
    # roberts default
    roberts "That's a great choice! I think you already know the captain pretty well."
    jump counselor_scene_2
label check_music1:
    mc "Music club sounds easy enough."
    # roberts giggle
    roberts "Something tells me you'd really like that one. Cash is in charge of it. You can find them in the music room around lunch time."
    jump counselor_scene_2
label check_gaming1:
    mc "We have a gaming club? I used to play competitively in high school, so that could be fun."
    "That was before Dad blew up about wasting my time on anything not school-related."
    # roberts wincing
    "The counselor winces."
    roberts "That was one of the team-building skills options, but if you think it would bring some fun into your life, then go for it!"
    jump counselor_scene_2

label counselor_scene_2:
    show mc happy at mc_emotes
    "I slip the sheet of paper into my backpack and stand."
    mc "Thank you for the suggestions. If it'll really make my resume look better I'll give the club a shot."
    "And I definitely won't tell Dad."
    
    scene bg hallway
    "I glance at the clock on the wall."
    "It's only lunch time."
    "I have plenty of time to check out each club. Thankfully the sheet the counselor gave me has the room locations and club leader names."

    menu:
        "What should I check out first?"

        "I think I'll go check out the music club.":
            $ flags["Music Visited"] = True
            jump music_club_1
        "Gaming club feels the most right.":
            $ flags["Gaming Visited"] = True
            jump gaming_club_1
        "Maybe sports club would be the best option for me?":
            $ flags["Sports Visited"] = True
            jump sports_club_1

label music_club_1:
    scene bg music club
    # cg of bastion playing an instrument
    # play music
    "I gasp."
    "It's Bastion, his head hanging over his instrument as he plays a soft melody with skill and precision."
    sharp "Isn't he amazing? He just transferred here this week and already signed up for music club."
    "Oh, I came here to ask Professor Sharp about signing up. I guess that means there's no room left?"
    sharp "I'm Professor Sharp, and there's exactly two spots open. You both can sign up, if you can pass the trial."
    "A trial?"
    "He hands me a notepad with three items written in red."
    sharp "There's three things we need before we can accept any more students. You and Bastion can work together."
    sharp "If you can bring all three things before the festival, you can officially list music club as your extra-curricular for when you apply for Rising Star Financial."
    # mc react confuse
    mc "How did you know I'm going to apply to Rising Star?"
    sharp "Your name is [mcname], right? I knew your father in school. I'd be really surprised if he wasn't pushing you to follow in his footsteps."
    mc "Is he really that predictable?"
    "I pay closer attention to Professor Sharp."
    "He's the same age as my parents, with kind eyes and an easy smile. I wonder how well he knew Dad?"
    "Does he know Mom?"
    sharp "Your father is, well..."
    sharp "I'm sure he hasn't changed at all."

    "He changes the subject quickly."

    sharp "I'll tell Bastion to meet you at the club room tomorrow around this time so you can discuss the first item together."
    sharp "You can stay awhile and listen, if you'd like."

    menu:

        "Thank you, but I need to go check out the sports club.":
            $ flags["Sports Visited"] = True
            jump sports_club_1
        "I'll let him practice in peace and go find the gaming club.":
            $ flags["Gaming Visited"] = True
            jump gaming_club_1
        "Oh crap! I'm about to miss class!!!":
            jump cat_event_1

label gaming_club_1:
    scene bg gaming

    "Before Dad scolded me over wasting my time on video games, I had spent the first two years of high school playing on a competitive squad."

    return

label sports_club_1:
    "Sports!"
    return

label cat_event_1:
    "Cat event!"