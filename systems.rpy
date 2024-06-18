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
    "assertive": 5,
    "creative": 5,
    "competitive": 5,
    "compassionate": 5
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