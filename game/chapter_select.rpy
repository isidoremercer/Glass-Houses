## chapter_select.rpy -- Chapter Select
##
## Accessible from the main menu. Lets players replay chapters they've
## already completed. Route chapters set sensible default variables.
## Gated behind persistent completion flags.

init offset = -1

screen chapter_select():

    tag menu

    use game_menu(_("Chapters"), scroll="viewport"):

        style_prefix "chapters"

        vbox:
            spacing 8

            ## --- COMMON ROUTE ---

            text "Common Route":
                color "#2d5a8a"
                size 36
                bold True

            null height 5

            ## Chapter 1 -- always available
            textbutton "Chapter 1: Move-In Day":
                action Start()
                style "chapter_entry"

            ## Chapter 2 -- requires Ch1 complete
            if persistent.completed_chapter1:
                textbutton "Chapter 2: Settling":
                    action Start("chapter2")
                    style "chapter_entry"
            else:
                textbutton "Chapter 2: Settling {size=-6}(locked){/size}":
                    style "chapter_entry_locked"

            ## Chapter 3 -- requires Ch2 complete
            if persistent.completed_chapter2:
                textbutton "Chapter 3: Cracks":
                    action Start("chapter3")
                    style "chapter_entry"
            else:
                textbutton "Chapter 3: Cracks {size=-6}(locked){/size}":
                    style "chapter_entry_locked"

            null height 25

            ## --- ROUTE CHAPTERS ---
            ## Only show routes that have been completed at least once.
            ## Each route sets sensible defaults for the affinity variables.

            if persistent.completed_izzy_route or persistent.completed_charlotte_route or persistent.completed_eve_route or persistent.completed_amara_route:

                text "Routes":
                    color "#2d5a8a"
                    size 36
                    bold True

                null height 5

            if persistent.completed_izzy_route:
                textbutton "Isabella: Ch4 -- Closer":
                    action [SetVariable("cruel_target", "Isabella"),
                            SetVariable("charlotte_points", 2),
                            SetVariable("isabella_points", 5),
                            SetVariable("amara_points", 1),
                            SetVariable("eve_points", 1),
                            SetVariable("route", "isabella"),
                            Start("izzy_ch4")]
                    style "chapter_entry"

                textbutton "Isabella: Ch5 -- Break":
                    action [SetVariable("cruel_target", "Isabella"),
                            SetVariable("charlotte_points", 2),
                            SetVariable("isabella_points", 5),
                            SetVariable("amara_points", 1),
                            SetVariable("eve_points", 1),
                            SetVariable("route", "isabella"),
                            Start("izzy_ch5_setup")]
                    style "chapter_entry"

                textbutton "Isabella: Ch6 -- Me Too":
                    action [SetVariable("cruel_target", "Isabella"),
                            SetVariable("charlotte_points", 2),
                            SetVariable("isabella_points", 5),
                            SetVariable("amara_points", 1),
                            SetVariable("eve_points", 1),
                            SetVariable("route", "isabella"),
                            Start("izzy_ch6_setup")]
                    style "chapter_entry"

                null height 10

            if persistent.completed_charlotte_route:
                textbutton "Charlotte: Ch4 -- Honeymoon":
                    action [SetVariable("cruel_target", "Charlotte"),
                            SetVariable("charlotte_points", 5),
                            SetVariable("isabella_points", 2),
                            SetVariable("amara_points", 1),
                            SetVariable("eve_points", 1),
                            SetVariable("route", "charlotte"),
                            Start("charlotte_ch4")]
                    style "chapter_entry"

                textbutton "Charlotte: Ch5 -- Weight":
                    action [SetVariable("cruel_target", "Charlotte"),
                            SetVariable("charlotte_points", 5),
                            SetVariable("isabella_points", 2),
                            SetVariable("amara_points", 1),
                            SetVariable("eve_points", 1),
                            SetVariable("route", "charlotte"),
                            Start("charlotte_ch5_setup")]
                    style "chapter_entry"

                textbutton "Charlotte: Ch6 -- Visit":
                    action [SetVariable("cruel_target", "Charlotte"),
                            SetVariable("charlotte_points", 5),
                            SetVariable("isabella_points", 2),
                            SetVariable("amara_points", 1),
                            SetVariable("eve_points", 1),
                            SetVariable("route", "charlotte"),
                            Start("charlotte_ch6_setup")]
                    style "chapter_entry"

                null height 10

            if persistent.completed_eve_route:
                textbutton "Eve: Ch4 -- Approach":
                    action [SetVariable("cruel_target", "Eve"),
                            SetVariable("charlotte_points", 1),
                            SetVariable("isabella_points", 1),
                            SetVariable("amara_points", 2),
                            SetVariable("eve_points", 5),
                            SetVariable("route", "eve"),
                            Start("eve_ch4")]
                    style "chapter_entry"

                textbutton "Eve: Ch5 -- Telling":
                    action [SetVariable("cruel_target", "Eve"),
                            SetVariable("charlotte_points", 1),
                            SetVariable("isabella_points", 1),
                            SetVariable("amara_points", 2),
                            SetVariable("eve_points", 5),
                            SetVariable("route", "eve"),
                            Start("eve_ch5")]
                    style "chapter_entry"

                textbutton "Eve: Ch6 -- Return":
                    action [SetVariable("cruel_target", "Eve"),
                            SetVariable("charlotte_points", 1),
                            SetVariable("isabella_points", 1),
                            SetVariable("amara_points", 2),
                            SetVariable("eve_points", 5),
                            SetVariable("route", "eve"),
                            Start("eve_ch6")]
                    style "chapter_entry"

                null height 10

            if persistent.completed_amara_route:
                textbutton "Amara: Ch4 -- Gravity":
                    action [SetVariable("cruel_target", "Amara"),
                            SetVariable("charlotte_points", 1),
                            SetVariable("isabella_points", 1),
                            SetVariable("amara_points", 5),
                            SetVariable("eve_points", 2),
                            SetVariable("route", "amara"),
                            Start("amara_ch4")]
                    style "chapter_entry"

                textbutton "Amara: Ch5 -- Role":
                    action [SetVariable("cruel_target", "Amara"),
                            SetVariable("charlotte_points", 1),
                            SetVariable("isabella_points", 1),
                            SetVariable("amara_points", 5),
                            SetVariable("eve_points", 2),
                            SetVariable("route", "amara"),
                            Start("amara_ch5_setup")]
                    style "chapter_entry"

                textbutton "Amara: Ch6 -- Identity":
                    action [SetVariable("cruel_target", "Amara"),
                            SetVariable("charlotte_points", 1),
                            SetVariable("isabella_points", 1),
                            SetVariable("amara_points", 5),
                            SetVariable("eve_points", 2),
                            SetVariable("route", "amara"),
                            Start("amara_ch6_setup")]
                    style "chapter_entry"

                null height 10

            ## --- GLASS HOUSES ---
            if persistent.gh_true_ending_seen:

                null height 15

                text "True Ending":
                    color "#2d5a8a"
                    size 36
                    bold True

                null height 5

                textbutton "Glass Houses":
                    action Start("glass_houses_chapter")
                    style "chapter_entry"

            ## --- COMPLETIONIST LETTER ---
            null height 25

            if endings_seen_count() >= 20:
                text "From the Authors":
                    color "#2d5a8a"
                    size 36
                    bold True

                null height 5

                textbutton "Letter to the Completionist":
                    action Start("completionist_letter")
                    style "chapter_entry"
            else:
                text "???":
                    color "#777777"
                    size 28

        null height 40


## === STYLES ===

style chapter_entry is button:
    background Frame("gui/button/idle_background.png", Borders(12, 8, 12, 8))
    hover_background Frame("gui/button/hover_background.png", Borders(12, 8, 12, 8))
    xfill True
    xpadding 20
    ypadding 10
    ymargin 2

style chapter_entry_text:
    color "#333333"
    hover_color "#1a3355"
    size 26
    bold True

style chapter_entry_locked is button:
    background Frame("gui/button/idle_background.png", Borders(12, 8, 12, 8))
    xfill True
    xpadding 20
    ypadding 10
    ymargin 2

style chapter_entry_locked_text:
    color "#999999"
    size 26
