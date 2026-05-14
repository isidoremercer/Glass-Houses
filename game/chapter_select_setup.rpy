## chapter_select_setup.rpy -- Variable Setup Menus for Chapter Select
##
## When players use chapter select to jump to Ch5 or Ch6 of a route,
## they need route-specific variables set. These labels show a quick
## menu to configure the game state, then jump to the real chapter.
##
## Normal game flow never hits these labels -- they're only reached
## from chapter_select.rpy.

## =========================================
## ISABELLA ROUTE SETUP
## =========================================

label izzy_ch5_setup:

    scene black

    "Chapter Select: Isabella Ch5"
    "Which ending path are you building toward?"

    menu:
        "Constellation (presence -- stop observing, just be there)":
            $ constellation = 5
            $ case_study = 2
            $ bridge = 2
        "Case Study (honesty -- see her completely)":
            $ constellation = 2
            $ case_study = 5
            $ bridge = 2
        "Bridge (sacrifice -- give her what she needs)":
            $ constellation = 2
            $ case_study = 2
            $ bridge = 5

    jump izzy_ch5

label izzy_ch6_setup:

    scene black

    "Chapter Select: Isabella Ch6"
    "Which ending path are you building toward?"

    menu:
        "Constellation (presence -- stop observing, just be there)":
            $ constellation = 8
            $ case_study = 3
            $ bridge = 3
        "Case Study (honesty -- see her completely)":
            $ constellation = 3
            $ case_study = 8
            $ bridge = 3
        "Bridge (sacrifice -- give her what she needs)":
            $ constellation = 3
            $ case_study = 3
            $ bridge = 8

    "Did Sophia hear Lumi's exact words?"

    menu:
        "Yes -- Isabella told her the direct quote":
            $ heard_lumi_words = "exact"
        "Partially -- Isabella softened it":
            $ heard_lumi_words = "paraphrase"
        "No -- Sophia chose not to ask":
            $ heard_lumi_words = "none"

    jump izzy_ch6

## =========================================
## CHARLOTTE ROUTE SETUP
## =========================================

label charlotte_ch5_setup:

    scene black

    "Chapter Select: Charlotte Ch5"
    "How has Sophia approached Charlotte so far?"

    menu:
        "Mostly pushed (challenged her, named what she saw)":
            $ charlotte_push = 8
            $ charlotte_present = 4
        "Mostly present (accepted her rhythm, stayed alongside)":
            $ charlotte_push = 4
            $ charlotte_present = 12
        "Balanced (both pushed and stayed present)":
            $ charlotte_push = 6
            $ charlotte_present = 8

    "Has Sophia supported Eve staying in the house?"

    menu:
        "Yes -- Eve is still here":
            $ charlotte_eve = 2
        "No -- Eve has been drifting away":
            $ charlotte_eve = 0

    jump charlotte_ch5

label charlotte_ch6_setup:

    scene black

    "Chapter Select: Charlotte Ch6"
    "How has Sophia approached Charlotte?"

    menu:
        "High push, high present (earned both halves)":
            $ charlotte_push = 8
            $ charlotte_present = 16
        "High push, low present (challenged but didn't stay)":
            $ charlotte_push = 8
            $ charlotte_present = 6
        "Low push, high present (stayed but didn't challenge)":
            $ charlotte_push = 3
            $ charlotte_present = 14
        "Low push, low present":
            $ charlotte_push = 3
            $ charlotte_present = 6

    "Has Eve stayed in the house?"

    menu:
        "Yes -- Eve stayed":
            $ charlotte_eve = 2
        "No -- Eve left":
            $ charlotte_eve = -2

    jump charlotte_ch6

## =========================================
## AMARA ROUTE SETUP
## =========================================

label amara_ch5_setup:

    scene black

    "Chapter Select: Amara Ch5"
    "What choices has Sophia made so far?"

    menu:
        "Chose Amara in Ch4 (stayed with the book)":
            $ sophia_fire = 0
            $ ch4_chose_lila = False
        "Chose Lila in Ch4 (went to help Lila)":
            $ sophia_fire = 1
            $ ch4_chose_lila = True

    jump amara_ch5

label amara_ch6_setup:

    scene black

    "Chapter Select: Amara Ch6"
    "In Ch4, when Lila texted and Amara left a book..."

    menu:
        "Sophia stayed with Amara":
            $ sophia_fire = 0
            $ ch4_chose_lila = False
        "Sophia went to Lila":
            $ sophia_fire = 1
            $ ch4_chose_lila = True

    "In Ch5, when Charlotte texted and Amara was holding Sophia's hand..."

    menu:
        "Sophia stayed with Amara":
            pass
        "Sophia went to Charlotte":
            $ sophia_fire += 1
            $ ch5_chose_house = True

    if sophia_fire == 2:
        $ charlotte_confession = True
    else:
        $ charlotte_confession = False

    jump amara_ch6
