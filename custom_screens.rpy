screen gameUI: 
    imagebutton: # adds a button
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "GUI/stats_idle.png" 
        action ShowMenu("StatsUI")

screen StatsUI:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox: # Horizontal Container Box. This will help keep the two boxes contained inside side-by-side.
            spacing 40

            vbox: # Vertical Container Box. This contains the names of the stats.
                spacing 10
                text "Assertive" size 40
                text "Creative" size 40
                text "Competitive" size 40
                text "Compassionate" size 40
            
            vbox: # This will contain the value of the stats.
                spacing 10
                $ a = stats["assertive"]
                $ b = stats["creative"]
                $ c = stats["competitive"]
                $ d = stats["compassionate"]
                text "[a]" size 40
                text "[b]" size 40
                text "[c]" size 40
                text "[d]" size 40
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "GUI/stats_idle.png" 
        action Return()