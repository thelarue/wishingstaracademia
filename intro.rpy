label intro:
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
