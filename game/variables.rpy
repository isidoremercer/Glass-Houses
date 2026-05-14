## variables.rpy — Affinity tracking and game state

## === ROUTE AFFINITY ===
## These accumulate through choices in the common route (Ch1-3)
## At the end of Ch3, the highest score determines the route
default charlotte_points = 0
default isabella_points = 0
default amara_points = 0
default eve_points = 0

## === CHAPTER 3 VARIABLES ===
## Who Sophia said the cruel thing about at the party
## Always targets the route girl (whoever she was watching closest)
## Set after route lock in Ch3, used in morning-after dialogue
default cruel_target = ""

## Route lock — set at end of Ch3
default route = ""

## === ISABELLA ROUTE VARIABLES (Ch4-6) ===
## Three approach variables — determine ending
default constellation = 0
default case_study = 0
default bridge = 0

## How much Sophia knows about Lumi's rejection
## "exact" = case_study path (heard the direct quote)
## "paraphrase" = bridge path (heard Isabella's softened version)
## "none" = constellation path (chose not to ask)
default heard_lumi_words = "none"

## Session-local mirror of persistent.left_it_with_amara.
## Set in ch5 hallway scene if Sophia chooses "Leave it." in this run.
## Used for in-scene callbacks that should only fire if THIS playthrough
## took the Leave it branch (the persistent flag would fire on any past run).
default left_it_with_amara = False

## === CHARLOTTE ROUTE VARIABLES (Ch4-6) ===
## Tracks whether Sophia pushes Charlotte to confront herself
default charlotte_push = 0
## Tracks whether Sophia is simply present with Charlotte
default charlotte_present = 0
## Tracks Sophia's handling of the Eve/Charlotte tension
default charlotte_eve = 0
## Whether the porch kiss happened in Act 1
default charlotte_kissed_porch = False

## === AMARA ROUTE VARIABLES (Ch4-6) ===
## Tracks whether you chose Lila/house or Amara
default sophia_fire = 0
default ch4_chose_lila = False
default ch5_chose_house = False
## Tracks whether Charlotte confesses in Ch 5
default charlotte_confession = False