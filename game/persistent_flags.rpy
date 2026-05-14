## persistent_flags.rpy — Cross-route gates for Glass Houses true endings
##
## Persistent variables survive across new games. They live in the player's
## Ren'Py persistent file, not in any save slot. This is the mechanism that
## lets a choice in one playthrough unlock content in a later playthrough.
##
## The four Glass Houses true endings are each gated by a flag set in a
## DIFFERENT route, plus completion of that route. The fiction: Sophia can
## only love each girl the way she actually needs to be loved if she has
## already practiced it on her in a life where she wasn't trying to win her.
##
## Each gate is the act that proves Sophia gave each girl what she needs.
## The girls don't need to be fixed — they need to be met:
##   Izzy      — needs to be made the subject, asked the invasive question
##   Eve       — needs presence that doesn't become the shape of the wound
##   Amara     — needs to be heard across rooms and chosen explicitly
##   Charlotte — needs a room where her own wanting can be recognized

init python:

    ## === CHAPTER COMPLETION FLAGS ===
    ## Set at the end of each common route chapter. Used by chapter select.
    if persistent.completed_chapter1 is None:
        persistent.completed_chapter1 = False
    if persistent.completed_chapter2 is None:
        persistent.completed_chapter2 = False
    if persistent.completed_chapter3 is None:
        persistent.completed_chapter3 = False

    ## === ROUTE COMPLETION FLAGS ===
    ## Set at the end of each route's Ch6. Required for the all-routes
    ## gate that unlocks the "..." option in the Ch3 cruel observation
    ## scene, and required (alongside the cross-route flags below) for
    ## each route's true ending.
    if persistent.completed_izzy_route is None:
        persistent.completed_izzy_route = False
    if persistent.completed_charlotte_route is None:
        persistent.completed_charlotte_route = False
    if persistent.completed_amara_route is None:
        persistent.completed_amara_route = False
    if persistent.completed_eve_route is None:
        persistent.completed_eve_route = False

    ## === CROSS-ROUTE GATE FLAGS ===

    ## IZZY GATE — set in Charlotte route, ch4 scene 14 (Isabella seed scene).
    ## Sophia pushes Isabella to name her past crush on Charlotte. Izzy gets
    ## to be the subject for once instead of the wise background friend.
    ## The "speaking from experience" branch sets this. The "Let it go"
    ## branch does not.
    if persistent.pushed_izzy_visible is None:
        persistent.pushed_izzy_visible = False

    ## EVE GATE — set in Charlotte route. Sophia ensures Eve stays in the
    ## house instead of being absorbed/displaced by Charlotte's caretaking
    ## orbit. Tracks the charlotte_eve handling.
    if persistent.eve_stayed_in_charlotte_route is None:
        persistent.eve_stayed_in_charlotte_route = False

    ## AMARA GATE — set in Izzy route, ch5 (new choice at line ~2651,
    ## "She came to my room yesterday" scene). Sophia chooses NOT to
    ## extract Isabella-data from Amara, sees Amara back instead.
    if persistent.left_it_with_amara is None:
        persistent.left_it_with_amara = False

    ## CHARLOTTE GATE — set in Amara route, ch5. The charlotte_confession
    ## scene fires only when sophia_fire == 2 (Lila + House).
    ## Charlotte gets to want something out loud, near someone outside
    ## her usual register.
    if persistent.charlotte_confessed_in_amara_route is None:
        persistent.charlotte_confessed_in_amara_route = False

    ## === GH ENDINGS SEEN ===
    ## Set when each per-route Glass Houses ending fires. Used to gate
    ## the "..." option in Ch3 (the Glass Houses Chapter unlock) — the
    ## player must have actually witnessed all four pieces of wisdom
    ## before the meta-end opens.
    if persistent.gh_seen_izzy is None:
        persistent.gh_seen_izzy = False
    if persistent.gh_seen_charlotte is None:
        persistent.gh_seen_charlotte = False
    if persistent.gh_seen_eve is None:
        persistent.gh_seen_eve = False
    if persistent.gh_seen_amara is None:
        persistent.gh_seen_amara = False

    ## === INDIVIDUAL ENDING FLAGS ===
    ## Used by the endings gallery to track which of the 20 endings
    ## the player has seen. GH endings reuse the gh_seen_* flags above.

    ## Isabella route (3 normal — GH "Seen" uses gh_seen_izzy)
    if persistent.ending_izzy_constellation is None:
        persistent.ending_izzy_constellation = False
    if persistent.ending_izzy_casestudy is None:
        persistent.ending_izzy_casestudy = False
    if persistent.ending_izzy_bridge is None:
        persistent.ending_izzy_bridge = False

    ## Charlotte route (4 normal — GH "Stool" uses gh_seen_charlotte)
    if persistent.ending_charlotte_of_course is None:
        persistent.ending_charlotte_of_course = False
    if persistent.ending_charlotte_the_crack is None:
        persistent.ending_charlotte_the_crack = False
    if persistent.ending_charlotte_something_new is None:
        persistent.ending_charlotte_something_new = False
    if persistent.ending_charlotte_five_places is None:
        persistent.ending_charlotte_five_places = False

    ## Eve route (1 normal — GH "Confession" uses gh_seen_eve)
    if persistent.ending_eve_friends is None:
        persistent.ending_eve_friends = False

    ## Amara route (6 normal + 2 GH tracked individually for gallery)
    ## gh_seen_amara is still used for the GH gate (set by either Burn or Extinguish)
    ## but these individual flags track which specific endings the player has seen.
    if persistent.ending_amara_burn is None:
        persistent.ending_amara_burn = False
    if persistent.ending_amara_extinguish is None:
        persistent.ending_amara_extinguish = False
    if persistent.ending_amara_babe is None:
        persistent.ending_amara_babe = False
    if persistent.ending_amara_muffin_girl is None:
        persistent.ending_amara_muffin_girl = False
    if persistent.ending_amara_two_inches is None:
        persistent.ending_amara_two_inches = False
    if persistent.ending_amara_one_mississippi is None:
        persistent.ending_amara_one_mississippi = False
    if persistent.ending_amara_still is None:
        persistent.ending_amara_still = False
    if persistent.ending_amara_parking_lot is None:
        persistent.ending_amara_parking_lot = False

    ## === TRUE ENDING SEEN ===
    if persistent.gh_true_ending_seen is None:
        persistent.gh_true_ending_seen = False


## === HELPER: have all four routes been completed? ===
## Required precondition for any per-route GH ending — these are
## replay-only content. The player must have lived through every
## route at least once before any GH ending can fire.
init python:
    def all_routes_complete():
        return (
            persistent.completed_izzy_route
            and persistent.completed_charlotte_route
            and persistent.completed_amara_route
            and persistent.completed_eve_route
        )


## === HELPER: have all four per-route GH endings been seen? ===
## Used to gate the "..." option in Ch3 cruel observation scene.
## The player must have actually witnessed all four pieces of wisdom
## (one per route GH ending) before the Glass Houses Chapter unlocks.
init python:
    def all_gh_endings_seen():
        return (
            persistent.gh_seen_izzy
            and persistent.gh_seen_charlotte
            and persistent.gh_seen_eve
            and persistent.gh_seen_amara
        )


## === HELPER: is each per-route GH ending available? ===
## Each function returns True only if (a) all four routes are complete
## AND (b) the cross-route flag for THIS route is set. Per-route GH
## endings are replay-only — they cannot fire on a first playthrough.
##
## Note: Izzy, Charlotte, and Amara also have additional in-route conditions
## that must be checked at the menu site (not in this helper, because in-route
## variables aren't part of the persistent layer):
##   Izzy      — balanced state across constellation/case_study/bridge (TBD)
##   Charlotte — charlotte_push >= 6 AND charlotte_present >= 10 AND charlotte_eve > 0
##   Amara     — sophia_fire == 0 OR sophia_fire == 2
init python:
    def izzy_gh_unlocked():
        return all_routes_complete() and persistent.pushed_izzy_visible

    def charlotte_gh_unlocked():
        return all_routes_complete() and persistent.charlotte_confessed_in_amara_route

    def eve_gh_unlocked():
        return all_routes_complete() and persistent.eve_stayed_in_charlotte_route

    def amara_gh_unlocked():
        return all_routes_complete() and persistent.left_it_with_amara


## === HELPER: count how many endings have been seen ===
## Used by the endings gallery to display "X / 20 Endings Discovered"
init python:
    def endings_seen_count():
        flags = [
            persistent.ending_izzy_constellation,
            persistent.ending_izzy_casestudy,
            persistent.ending_izzy_bridge,
            persistent.gh_seen_izzy,
            persistent.ending_charlotte_of_course,
            persistent.ending_charlotte_the_crack,
            persistent.ending_charlotte_something_new,
            persistent.ending_charlotte_five_places,
            persistent.gh_seen_charlotte,
            persistent.ending_eve_friends,
            persistent.gh_seen_eve,
            persistent.ending_amara_babe,
            persistent.ending_amara_muffin_girl,
            persistent.ending_amara_two_inches,
            persistent.ending_amara_one_mississippi,
            persistent.ending_amara_still,
            persistent.ending_amara_parking_lot,
            persistent.ending_amara_burn,
            persistent.ending_amara_extinguish,
            persistent.gh_true_ending_seen,
        ]
        return sum(1 for f in flags if f)


## === HELPER: is the Glass Houses Chapter (the new Ch4) unlocked? ===
## The "..." option in Ch3's cruel observation scene reads this.
## Requires all four per-route GH endings to have been seen — meaning
## the player has collected all four pieces of wisdom about Sophia's
## wound and is now ready for the dad chapter.
init python:
    def glass_houses_chapter_unlocked():
        return all_gh_endings_seen()
