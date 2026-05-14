## endings_gallery.rpy — Endings Gallery
##
## Accessible from the main menu. Shows all 20 endings grouped by route.
## Locked endings show "???" with progressive hints (click to reveal more).
## Unlocked endings show their name and a short description.

init offset = -1

init python:

    endings_data = [

        ## === ISABELLA ROUTE ===
        {
            "route": "Isabella",
            "route_color": "#d4a5c9",
            "name": "Constellation",
            "flag": "ending_izzy_constellation",
            "gh": False,
            "hints": [
                "An ending on Isabella's route.",
                "Sophia chose love over knowledge.",
                "Don't observe. Don't ask. Just be there."
            ],
            "description": "They're together. She stopped observing. But stopping isn't growth."
        },
        {
            "route": "Isabella",
            "route_color": "#d4a5c9",
            "name": "Case Study",
            "flag": "ending_izzy_casestudy",
            "gh": False,
            "hints": [
                "An ending on Isabella's route.",
                "The most intimate ending. Being seen completely.",
                "Write what you actually see. Not what you want to see."
            ],
            "description": "'You SAW me.' They're not together. Being seen and being loved aren't the same thing."
        },
        {
            "route": "Isabella",
            "route_color": "#d4a5c9",
            "name": "Bridge",
            "flag": "ending_izzy_bridge",
            "gh": False,
            "hints": [
                "An ending on Isabella's route.",
                "Sophia builds something she can't walk across.",
                "Translate what Lumi really meant."
            ],
            "description": "'I built the bridge. She walked across it. That's what bridges are for.'"
        },
        {
            "route": "Isabella",
            "route_color": "#d4a5c9",
            "name": "Seen",
            "flag": "gh_seen_izzy",
            "gh": True,
            "hints": [
                "A hidden ending on Isabella's route.",
                "Requires all four routes completed, plus a specific choice in Charlotte's route.",
                "In Charlotte's route Ch4, push Isabella to name her feelings. Then replay Isabella's route."
            ],
            "description": "The file shared. Both watching. Both terrified. The laptop stays open."
        },

        ## === CHARLOTTE ROUTE ===
        {
            "route": "Charlotte",
            "route_color": "#f2c57c",
            "name": "Of Course",
            "flag": "ending_charlotte_of_course",
            "gh": False,
            "hints": [
                "An ending on Charlotte's route.",
                "The comfortable lie.",
                "Neither push nor be present enough, but make sure Eve stays. Let the mask win."
            ],
            "description": "Monday morning. Omelets. Chore chart. 'Of course!' said to nobody."
        },
        {
            "route": "Charlotte",
            "route_color": "#f2c57c",
            "name": "The Crack",
            "flag": "ending_charlotte_the_crack",
            "gh": False,
            "hints": [
                "An ending on Charlotte's route.",
                "Seen but shattered.",
                "Push Charlotte hard enough to confront her mother. The truth exists in the room now."
            ],
            "description": "'Do you still love me?' 'Yes.' The most intimate moment she's ever had."
        },
        {
            "route": "Charlotte",
            "route_color": "#f2c57c",
            "name": "Something New",
            "flag": "ending_charlotte_something_new",
            "gh": False,
            "hints": [
                "An ending on Charlotte's route.",
                "Charlotte finds the door.",
                "Low push, high present. Charlotte uses the Vermeer paper to reconcile -- then leaves."
            ],
            "description": "'Thanks, Sophia. For the map.' Charlotte is looking out the window."
        },
        {
            "route": "Charlotte",
            "route_color": "#f2c57c",
            "name": "Five Places",
            "flag": "ending_charlotte_five_places",
            "gh": False,
            "hints": [
                "The darkest ending on Charlotte's route.",
                "Make the worst choices possible.",
                "Low push, low present, and Eve has left. Charlotte counts the forks."
            ],
            "description": "Five forks for four people. Her lips move while she counts."
        },
        {
            "route": "Charlotte",
            "route_color": "#f2c57c",
            "name": "Stool",
            "flag": "gh_seen_charlotte",
            "gh": True,
            "hints": [
                "A hidden ending on Charlotte's route.",
                "Requires all four routes completed, plus a specific choice in Amara's route.",
                "In Amara's route, Charlotte must confess (select Lila in Ch4, then Charlotte in Ch5). Then replay Charlotte with high push, high present, and Eve staying."
            ],
            "description": "Both of them on the stool. 'I'm Charlotte. I just figured that out.'"
        },

        ## === EVE ROUTE ===
        {
            "route": "Eve",
            "route_color": "#a8b5a2",
            "name": "Friends",
            "flag": "ending_eve_friends",
            "gh": False,
            "hints": [
                "An ending on Eve's route.",
                "The safest true thing she can say.",
                "Tell Eve you have feelings for her. Watch what happens."
            ],
            "description": "'Friends?' 'Friends.' She writes it in the notebook. The notebook stays open."
        },
        {
            "route": "Eve",
            "route_color": "#a8b5a2",
            "name": "Confession",
            "flag": "gh_seen_eve",
            "gh": True,
            "hints": [
                "A hidden ending on Eve's route.",
                "Requires all four routes completed, plus specific choices in Charlotte's route.",
                "In Charlotte's route, ensure Eve stays in the house. Then replay Eve's route."
            ],
            "description": "Eve initiates. The notebook closes. No thorn."
        },

        ## === AMARA ROUTE ===
        {
            "route": "Amara",
            "route_color": "#7ba7bc",
            "name": "Babe",
            "flag": "ending_amara_babe",
            "gh": False,
            "hints": [
                "An ending on Amara's route.",
                "Two forest fires.",
                "Choose Lila at every turn. The fire consumes everything."
            ],
            "description": "Lila and Sophia. Loud in every way a kiss can be loud."
        },
        {
            "route": "Amara",
            "route_color": "#7ba7bc",
            "name": "Muffin Girl",
            "flag": "ending_amara_muffin_girl",
            "gh": False,
            "hints": [
                "An ending on Amara's route.",
                "Charlotte's ending, hidden in Amara's route.",
                "Choose Lila in Ch4, Charlotte in Ch5, then go to library and get rejected."
            ],
            "description": "'You couldn't fix me. So you found someone else you could fix instead.'"
        },
        {
            "route": "Amara",
            "route_color": "#7ba7bc",
            "name": "Two Inches",
            "flag": "ending_amara_two_inches",
            "gh": False,
            "hints": [
                "An ending on Amara's route.",
                "The fling that wasn't.",
                "Amara Ch4, Charlotte Ch5 OR Lila Ch4, Amara Ch5. Stay with Lila and see what could've been."
            ],
            "description": "Two inches of porch step. She didn't close the gap."
        },
        {
            "route": "Amara",
            "route_color": "#7ba7bc",
            "name": "One Mississippi",
            "flag": "ending_amara_one_mississippi",
            "gh": False,
            "hints": [
                "An ending on Amara's route.",
                "Sophia hedged once.",
                "Lila Ch4, Amara Ch5 OR Amara Ch4, Charlotte Ch5. Go to library and still count one mississppi."
            ],
            "description": "One Mississippi, two Mississippi. Counting thunder. Still watching for the leaving."
        },
        {
            "route": "Amara",
            "route_color": "#7ba7bc",
            "name": "Still",
            "flag": "ending_amara_still",
            "gh": False,
            "hints": [
                "An ending on Amara's route.",
                "Pure devotion.",
                "Choose Amara at every turn. Stillness."
            ],
            "description": "The library. Their table. She's not slowing down. Neither is Sophia."
        },
        {
            "route": "Amara",
            "route_color": "#7ba7bc",
            "name": "Parking Lot",
            "flag": "ending_amara_parking_lot",
            "gh": False,
            "hints": [
                "An ending on Amara's route.",
                "Alone.",
                "Push everyone away. Choose Amara twice, then stay with Lila. Katie was right."
            ],
            "description": "A Denny's parking lot. Again. Different city. Same girl."
        },
        {
            "route": "Amara",
            "route_color": "#7ba7bc",
            "name": "Burn",
            "flag": "ending_amara_burn",
            "gh": True,
            "hints": [
                "A hidden ending on Amara's route.",
                "Requires all four routes completed, plus a specific choice in Isabella's route.",
                "In Isabella's route Ch5, choose 'Leave it' when Amara mentions Isabella. Then replay Amara with two Lila choices."
            ],
            "description": "'I'm not slowing down for you anymore.' 'Wouldn't dream of it.'"
        },
        {
            "route": "Amara",
            "route_color": "#7ba7bc",
            "name": "Extinguish",
            "flag": "ending_amara_extinguish",
            "gh": True,
            "hints": [
                "A hidden ending on Amara's route.",
                "Requires all four routes completed, plus a specific choice in Isabella's route.",
                "In Isabella's route Ch5, choose 'Leave it' when Amara mentions Isabella. Then replay Amara with two Amara choices."
            ],
            "description": "Amara reaches. A library kiss. The best kind."
        },

        ## === TRUE ENDING ===
        {
            "route": "True",
            "route_color": "#ffffff",
            "name": "Glass Houses",
            "flag": "gh_true_ending_seen",
            "gh": True,
            "hints": [
                "The true ending.",
                "Requires all four Glass Houses endings to be seen first.",
                "Complete Seen, Stool, Confession, and Burn or Extinguish. Then replay from Chapter 3. Select '...' when prompted."
            ],
            "description": "The letter. The file made love. The keeping, let go."
        },
    ]

    ## Route display order and colors
    route_order = [
        ("Isabella", "#d4a5c9"),
        ("Charlotte", "#f2c57c"),
        ("Eve", "#a8b5a2"),
        ("Amara", "#7ba7bc"),
        ("True", "#ffffff"),
    ]


screen endings_gallery():

    tag menu

    ## Track which ending is expanded and hint depth
    default expanded = None
    default hint_depth = 0

    use game_menu(_("Endings"), scroll="viewport"):

        style_prefix "endings"

        ## Counter
        text "[endings_seen_count()] / 20":
            xalign 0.5
            color "#ffffff"
            size 52
            bold True
            font "IMPRISHA.TTF"

        null height 10

        ## Grouped by route
        for route_name, route_color in route_order:

            null height 20

            ## Route header
            text route_name:
                color route_color
                size 36
                bold True

            null height 10

            for ending in endings_data:
                if ending["route"] == route_name:

                    ## Each ending is a button (clickable to expand hints)
                    button:
                        style "endings_entry"
                        xfill True

                        if not getattr(persistent, ending["flag"], False):
                            if expanded == ending["flag"]:
                                action [SetScreenVariable("expanded", None), SetScreenVariable("hint_depth", 0)]
                            else:
                                action [SetScreenVariable("expanded", ending["flag"]), SetScreenVariable("hint_depth", 0)]

                        vbox:
                            spacing 6

                            hbox:
                                spacing 15

                                ## Status indicator
                                if getattr(persistent, ending["flag"], False):
                                    text "\u2713":
                                        color "#1a3355"
                                        size 28
                                        yalign 0.5
                                else:
                                    text "\u2022":
                                        color "#888888"
                                        size 28
                                        yalign 0.5

                                vbox:
                                    ## Name or ???
                                    if getattr(persistent, ending["flag"], False):
                                        hbox:
                                            spacing 12
                                            text ending["name"]:
                                                color "#222222"
                                                size 28
                                                bold True
                                            if ending["gh"]:
                                                text "Glass Houses":
                                                    color "#3a1166"
                                                    size 20
                                                    yalign 0.5
                                    else:
                                        text "???":
                                            color "#777777"
                                            size 28

                                    ## Description or hint
                                    if getattr(persistent, ending["flag"], False):
                                        text ending["description"]:
                                            color "#333333"
                                            size 22
                                            italic True
                                    elif expanded == ending["flag"]:
                                        text ending["hints"][hint_depth]:
                                            color "#555555"
                                            size 22
                                            italic True

                            ## Hint controls (only for locked + expanded)
                            if not getattr(persistent, ending["flag"], False) and expanded == ending["flag"]:
                                hbox:
                                    xalign 1.0
                                    spacing 15
                                    if hint_depth < 2:
                                        textbutton "Reveal more...":
                                            action SetScreenVariable("hint_depth", hint_depth + 1)
                                            text_color "#1a3355"
                                            text_size 20
                                    else:
                                        text "No further hints.":
                                            color "#555555"
                                            size 20
                                            italic True

        null height 40


## === STYLES ===

style endings_entry is button:
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    hover_background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    padding (20, 12, 20, 12)
    xmargin 5
    ymargin 3
