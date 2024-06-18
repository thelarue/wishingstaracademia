
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
            jump intro # brings player back into narrative
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "competitive")
            jump intro

label assertive_start_2:
    menu:
        "I enjoy music. (Or whatever might suggest creativity lol)": 
            $ mod_stat(10, "creative")
            $ mod_stat(5, "compassionate")
            jump intro
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "creative")
            jump intro

label assertive_start_3:
    menu:
        "I enjoy music. (Or whatever might suggest creativity lol)": 
            $ mod_stat(10, "creative")
            $ mod_stat(5, "competitive")
            jump intro
        "I enjoy esports.":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "creative")
            jump intro  

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
            jump intro
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "competitive")
            jump intro

label creative_start_2:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "compassionate")
            jump intro
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "assertive")
            jump intro

label creative_start_3:
    menu:
        "... am creative.":
            $ mod_stat(10, "creative")
            $ mod_stat(5, "competitive")
            jump intro
        "... competitive option":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "creative")
            jump intro

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
            jump intro
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "creative")
            jump intro

label competitive_start_2:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "compassionate")
            jump intro
        "... love cats. (lol)":
            $ mod_stat(10, "compassionate")
            $ mod_stat(5, "assertive")
            jump intro
    
label competitive_start_3:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "creative")
            jump intro
        "... art.":
            $ mod_stat(10, "creative")
            $ mod_stat(5, "assertive")
            jump intro

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
            jump intro
        "... competitive option":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "creative")
            jump intro

label compassionate_start_2:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "competitive")
            jump intro
        "... competitive option":
            $ mod_stat(10, "competitive")
            $ mod_stat(5, "assertive")
            jump intro

label compassionate_start_3:
    menu:
        "... able to stand my ground.":
            $ mod_stat(10, "assertive")
            $ mod_stat(5, "creative")
            jump intro
        "... pretty creative.":
            $ mod_stat(10, "creative")
            $ mod_stat(5, "assertive")
            jump intro
