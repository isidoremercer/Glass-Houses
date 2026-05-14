## charlotte_ch5.rpy -- Glass Houses
## Chapter 5: "The Weight" -- Charlotte Route
## Act 1: "The Trying"

## === NEW VARIABLES NEEDED (add to variables.rpy) ===
## None — all charlotte_push, charlotte_present, charlotte_eve already defined.

## === AUDIO DEFINITIONS ===
## (Re-defining ones used in ch4 for this file's scope, plus any new ones)
define audio.mus_charlotte = "audio/music/Charlotte Opal ~ Toast Girl.mp3"
define audio.mus_charlotte_sad = "audio/music/Charlotte Opal ~ Of Course.mp3"
define audio.mus_morningafter = "audio/music/The Morning After The Hard Thing.mp3"
define audio.mus_2am = "audio/music/House at 2AM.mp3"
define audio.mus_campus = "audio/music/Campus in Autumn.mp3"
define audio.mus_fivepeople = "audio/music/Five People in a Kitchen.mp3"
define audio.mus_tuesday = "audio/music/A Normal Tuesday.mp3"
define audio.mus_baddecisions = "audio/music/Bad Decisions.mp3"
define audio.mus_shoulders = "audio/music/Shoulders Touching.mp3"
define audio.mus_planned = "audio/music/Planned Evening.mp3"
define audio.mus_mourning = "audio/music/Mourning.mp3"
define audio.mus_glass = "audio/music/Glass Walls.mp3"
define audio.mus_stillhere = "audio/music/Still Here.mp3"

## ===========================
## CHAPTER 5 START
## ===========================

label charlotte_ch5:

    ## ===========================
    ## SCENE 1: THE MORNING AFTER THE CONFESSION (CONDITIONAL)
    ## Three openings based on the porch.
    ## Push-path: performing the morning after openness.
    ## Present-path: NOT making eggs. Mission statement.
    ## Abdication-path: mask at full volume.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    ## CONDITIONAL OPENING
    if charlotte_push > charlotte_present:
        ## === PUSH PATH: The Performance of Morning-After ===
        play music mus_charlotte fadein 3.0

        s_thoughts "The kitchen smells like eggs."

        s_thoughts "Of course it does."

        s_thoughts "I don't know what I expected. That the porch would change something. That Charlotte would come downstairs looking different -- undone, maybe. Like the confession shook something loose."

        s_thoughts "She looks great. She looks BETTER than great. She's wearing a new top and her hair is down and she's humming."

        show charlotte happy at center with dissolve

        c "Morning! I made omelets. The good kind -- with the fold? I watched a video."

        s "Charlotte."

        c "Mushroom and gruyère. You said you liked gruyère once. On the walk. Remember?"

        s "I remember."

        s_thoughts "Charlotte told me the truth last night. And this morning she's performing 'the morning after telling the truth' with the same precision she performs everything."

        c "Coffee's fresh. I used the French press. I know you like the French press better."

        s "How are you?"

        show charlotte smile at center

        c "Great! Really good. I slept well. I feel -- lighter? Is that a thing?"

        s_thoughts "She says 'lighter' like she read it in a self-help book."

        s "That's a thing."

        c "I think telling you was really good. For me. I feel like -- I don't know. Like I can breathe?"

        s_thoughts "She can't breathe. She's running the post-confession playbook."

        s_thoughts "But she's trying. She's TRYING to mean it."

        s_thoughts "That's... something."

        s "The omelet smells good."

        show charlotte laugh at center

        c "It better! I burned the first one learning the fold."

        s_thoughts "I sit down. Charlotte plates the omelet. Garnish. A little something on the side."

        s_thoughts "I eat. She watches me eat."

        s_thoughts "Same as always."

        s_thoughts "But she told me about the stool. The pasta. The extra places. And now she's making me an omelet and watching me eat it and I can see the ten-year-old in the brightness and I don't know what to do with that."

        s_thoughts "I eat the omelet. It's really good."

        s_thoughts "Charlotte smiles. Pours me more coffee without asking."

        show charlotte happy at center

        s_thoughts "The trying is real. The shape of the trying is the same shape as the mask."

        s_thoughts "I don't know if she can tell the difference yet."

        s_thoughts "I don't know if I can either."

        jump charlotte_ch5_scene2

    elif charlotte_present >= charlotte_push and charlotte_present > 0:
        ## === PRESENT PATH: Charlotte Is Not Making Eggs ===
        play music mus_morningafter fadein 3.0

        s_thoughts "The kitchen is quiet."

        s_thoughts "Not Charlotte-quiet. Not 'someone is cooking and the silence has a schedule.' Actual quiet. No sizzle. No humming. No clink of plates being set for five."

        s_thoughts "I come downstairs and the air smells like coffee and nothing else."

        show charlotte neutral at center with dissolve

        s_thoughts "Charlotte is sitting at the kitchen table."

        s_thoughts "Just sitting."

        s_thoughts "She has coffee. One mug. Her hands are wrapped around it. She's looking at the table."

        s "Hey."

        c "Hey."

        s_thoughts "She looks up. Her eyes are a little puffy. Just -- morning eyes. The eyes of someone who didn't sleep well and isn't pretending she did."

        s_thoughts "There are no plates on the table. No forks. No napkins. No little vase of flowers from the secret garden."

        s_thoughts "Just Charlotte and coffee."

        c "I'm not making breakfast."

        s_thoughts "She says it like a mission statement. Like she rehearsed THIS too -- but a different kind of rehearsal. Not the 'how to be perfect' kind. The 'how to be different' kind."

        s "Okay."

        c "I just -- I thought I should try. Not doing the thing."

        s "Okay."

        c "Is that weird?"

        s "It's not weird."

        s_thoughts "It's the bravest thing she's done since the porch."

        s_thoughts "Charlotte is sitting in a kitchen she usually runs. Her hands are on a mug instead of a spatula. She's not doing anything for anyone."

        s_thoughts "She looks terrified."

        s "Do you want me to make something?"

        show charlotte surprised at center

        c "You cook?"

        s "I can make pancakes."

        c "You can make pancakes?"

        s "I can make THINGS that resemble pancakes."

        show charlotte smile at center

        s_thoughts "A small smile. Uncertain. But real."

        c "...Okay."

        s_thoughts "I make pancakes."

        s_thoughts "They are objectively terrible. The first one looks like a map of a country that doesn't exist. The second one is too thick in the middle and raw. The third one is actually fine."

        s_thoughts "I put them on a plate. Not Charlotte's good plates. Just a plate."

        s_thoughts "No garnish. No drizzle. No arrangement."

        s_thoughts "I set them in front of Charlotte."

        s "Two out of three survived."

        show charlotte laugh at center

        s_thoughts "Charlotte looks at the plate. She looks at me."

        s_thoughts "She picks up the terrible first pancake with her fingers and takes a bite."

        c "This is awful."

        s "I know."

        c "The texture is... crunchy? Is it supposed to be crunchy?"

        s "Absolutely not."

        c "It tastes like you didn't mix the batter enough."

        s "I definitely didn't mix the batter enough."

        show charlotte smile at center

        s_thoughts "She takes another bite."

        c "Thank you."

        s "For the bad pancakes?"

        c "For the bad pancakes."

        s_thoughts "She eats them. All of them. Even the raw middle one."

        s_thoughts "Charlotte eats when she's not thinking about eating. When she's distracted by something real."

        s_thoughts "The something real this morning is someone else making breakfast."

        s_thoughts "I don't point it out. I just drink my coffee and let her eat terrible pancakes and it's the best morning we've had."

        jump charlotte_ch5_scene2

    else:
        ## === ABDICATION PATH: The Mask at Full Volume ===
        play music mus_charlotte fadein 2.0

        s_thoughts "6:30 AM."

        s_thoughts "I'm awake because Charlotte is awake. Charlotte is awake because Charlotte is making breakfast."

        s_thoughts "The kitchen sounds like a restaurant. Pans. Running water. The sharp rhythm of a knife on a cutting board."

        show charlotte happy at center with dissolve

        c "Morning! Sit down, sit down. I made everything."

        s_thoughts "She made everything."

        s_thoughts "Eggs. Toast. Fruit salad. There's a FRUIT SALAD. Cut into shapes. The melon is in cubes. The strawberries are halved. There's a mint leaf."

        s "Charlotte, it's 6:30."

        c "Early bird! I couldn't sleep so I thought -- why not? The kitchen was right there."

        s_thoughts "She couldn't sleep because last night she went inside and made muffins in the dark."

        s_thoughts "This morning the muffins are on the counter. Twelve of them. In a pattern."

        c "Coffee? Of course, let me--"

        c "Oh, I reorganized the spice rack. It was bugging me. They were out of order."

        s "They were alphabetical."

        c "They were alphabetical by BRAND. I put them alphabetical by SPICE."

        s_thoughts "Charlotte is moving through the kitchen at full speed."

        s_thoughts "Charlotte Opal is fine. Charlotte Opal is making fruit salad at 6:30 AM and everything is fine."

        c "I was thinking we should do a deep clean this weekend. The bathroom grout is -- well. And Eve's shelf in the fridge is getting a little--"

        s "Charlotte."

        show charlotte smile at center

        c "Hm?"

        s_thoughts "She looks at me. Brightness at full wattage."

        s_thoughts "I open my mouth."

        s_thoughts "I close it."

        s "The eggs are great."

        c "Of course! I added chives."

        s_thoughts "I sit at the table. I eat the eggs. They're perfect."

        s_thoughts "Charlotte watches me eat them."

        s_thoughts "Everything is fine."

        jump charlotte_ch5_scene2

    ## ===========================
    ## SCENE 2: WALKING TO CAMPUS
    ## Charlotte's hand finds Sophia's. The nervous version.
    ## They talk about nothing. Silences exist.
    ## ===========================

label charlotte_ch5_scene2:

    hide charlotte with dissolve
    stop music fadeout 2.0

    scene bg street with Fade(0.8, 0.3, 0.8)
    play music mus_tuesday fadein 2.0

    s_thoughts "Monday. Walking to campus."

    s_thoughts "Charlotte and I are walking. She has her bag over one shoulder. I have mine over both. We look like every other couple on this sidewalk."

    s_thoughts "We are not like every other couple on this sidewalk."

    show charlotte smile at center with dissolve

    c "The weather is nice."

    s "It is."

    c "Like -- genuinely nice. Not the 'I'm filling silence' kind of nice. The actual weather. It's warm."

    s "Charlotte. You just narrated yourself filling the silence."

    show charlotte embarrassed at center

    c "I did NOT. I was making a meteorological observation."

    s "You literally said 'not the filling silence kind.'"

    c "..."

    c "Okay. I was filling the silence."

    s "It's okay. The silence was fine."

    show charlotte neutral at center

    s_thoughts "We walk."

    s_thoughts "Charlotte's hand is at her side. It swings when she walks. It bumps mine."

    s_thoughts "She grabs my hand."

    s_thoughts "I hold on."

    s_thoughts "Her fingers tighten."

    show charlotte smile at center

    s_thoughts "We walk."

    s_thoughts "A dog is barking at a squirrel across the street. Someone is struggling with an umbrella even though it's not raining. A bus stop advertisement for a law firm has been defaced so the lawyer's name says 'BUTT.'"

    show charlotte laugh at center

    c "Oh no. That's vandalism."

    s "Oh yes. That's public service."

    s_thoughts "Her hand is warm. She's holding mine like she's still deciding whether she's allowed to."

    s_thoughts "It's nice."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 3: CHARLOTTE SAYS NO
    ## Something small. Amara asks Charlotte for a favor.
    ## Charlotte says no. The world doesn't end.
    ## CHOICE 1.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_baddecisions fadein 1.5

    s_thoughts "Tuesday evening."

    s_thoughts "I'm at the table doing readings. Charlotte is on the couch with her laptop. Amara is in the kitchen making tea."

    show amara neutral at right with dissolve
    show charlotte smile at left with dissolve

    a "Charlotte."

    c "Yeah?"

    a "I need milk. For tea. Could you grab some from the store?"

    s_thoughts "Normal question. Normal Tuesday. Charlotte has gotten things from the store for everyone in this house more times than I can count."

    s_thoughts "Charlotte opens her mouth."

    s_thoughts "I see it happen."

    s_thoughts "The 'of course' assembling behind her teeth. The reflex."

    show charlotte neutral at left

    c "Actually--"

    s_thoughts "A beat."

    c "I can't today. Sorry."

    s_thoughts "Silence."

    s_thoughts "Two seconds of it."

    s_thoughts "Amara blinks. Not because it's unreasonable. Because Charlotte has never said no to a request in the entire time she's lived here."

    a "Okay."

    s_thoughts "Amara gets her keys. Goes to the store herself."
    
    hide amara with dissolve

    s_thoughts "The world continues to rotate on its axis."

    s_thoughts "Charlotte is staring at the closed door."

    show charlotte surprised at left

    c "I just said no."

    s "You did."

    c "Why does that feel like I committed a crime?"

    s_thoughts "She's not joking. Her hands are doing the hover thing -- reaching for her laptop, pulling back, settling, unsettle."

    c "She needed milk. I could have gone. It's a five minute walk."

    s "You said you couldn't."

    c "I COULD have. I just -- I didn't want to. Is that -- can I just not want to?"

    menu:
        "Charlotte just said no for the first time."

        "\"That was huge. I'm proud of you.\"":
            $ charlotte_push += 1

            s "Charlotte. That was huge. I'm proud of you."

            show charlotte embarrassed at left

            c "It was MILK. It was a trip to the STORE."

            s "It was the first time I've ever heard you say no."

            c "That's not -- I say no. I say no to things."

            s "Name one."

            c "..."

            s "See?"

            show charlotte smile at left

            c "I said no. To the store."

            s "You said no to the store."

            c "...Is it weird that I feel like I should go apologize?"

            s "You don't have to apologize for not buying milk."

            show charlotte embarrassed at left

            c "I KNOW that. I know that logically. But my -- there's a THING in my chest that's saying 'she needed something and you didn't do it and now she thinks you're--'"

            s "Amara doesn't think anything. Amara is buying milk."

            c "Right. Right."

            s_thoughts "Whether she's looking because she wants to or because I told her to -- I don't know."

            jump charlotte_ch5_scene4

        "Say nothing. Let it be normal.":
            $ charlotte_present += 1

            s_thoughts "I go back to my reading."

            s_thoughts "Charlotte is staring at the door. Her hands are hovering. She looks like she might bolt for the store after all."

            s_thoughts "I don't say anything."

            s_thoughts "Charlotte said no. That's normal. People say no. I'm going to treat it like the normal thing it should have been."

            s_thoughts "Charlotte looks at me. Looks at the door. Looks at me again."

            s_thoughts "I turn a page."

            s_thoughts "Charlotte exhales."

            show charlotte smile at left

            s_thoughts "She picks up her laptop. Opens it. Starts typing."

            s_thoughts "Five minutes later she says:"

            c "I said no."

            s "Mm."

            c "And it was fine."

            s "Mm."

            show charlotte happy at left

            s_thoughts "She goes back to typing. Her shoulders drop an inch."

            s_thoughts "She said no and nobody reacted and that's the point."

            jump charlotte_ch5_scene4

        "\"She'll understand. Don't worry about it.\"":
            $ charlotte_present -= 1

            s "She'll understand. Don't worry about it."

            s_thoughts "Charlotte nods. But her eyes are doing something."

            show charlotte neutral at left

            c "Yeah. You're right."

            s_thoughts "She goes back to her laptop."

            s_thoughts "But the typing is different. Slower. She keeps glancing at the door."

            s_thoughts "She smiles."

            show charlotte smile at left

            s_thoughts "Thin."

            jump charlotte_ch5_scene4

    ## ===========================
    ## SCENE 4: THE CHIP
    ## Study session. Charlotte steals a chip without asking.
    ## The biggest deal.
    ## ===========================

label charlotte_ch5_scene4:

    hide amara
    hide charlotte
    with dissolve
    stop music fadeout 1.5

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_morningafter fadein 2.0

    s_thoughts "Wednesday evening."

    s_thoughts "I'm on the floor. Back against the couch. Charlotte is on the couch behind me. She's revising the Vermeer paper on her laptop. My readings are spread across the coffee table."

    s_thoughts "I have chips. The salt and vinegar kind from the convenience store. The bag is on the floor next to me."

    show charlotte smile at center with dissolve

    s_thoughts "Charlotte is typing. She's been typing for forty minutes. The focus face is on -- the one where her lower lip tucks under her front teeth and she doesn't know she's doing it."

    s_thoughts "I like the focus face."

    s_thoughts "I'm reading about Goffman. Backstage behavior. The idea that we all have a private self we only show when nobody's watching."

    s_thoughts "I think about Charlotte on the porch."

    s_thoughts "Charlotte reaches past my shoulder."

    s_thoughts "Her hand goes into the chip bag."

    s_thoughts "She takes a chip."

    s_thoughts "She eats it."

    s_thoughts "She goes back to typing."

    s_thoughts "..."

    s_thoughts "I stare at her."

    show charlotte neutral at center

    c "What?"

    s "You just took a chip."

    c "It was right THERE."

    s "You took something without asking."

    c "It's a chip."

    s "Charlotte. You asked permission to use my phone charger yesterday. The charger I leave in the living room for ANYONE. You asked."

    show charlotte embarrassed at center

    c "That's different. That's an electronic. This is a potato."

    s "You TOOK a chip. Without performing the chip-request ritual. Without the 'oh, do you mind if I--' thing."

    c "I don't have a chip-request ritual."

    s "You have a ritual for EVERYTHING."

    c "I do not have a -- okay. I might have a small system for shared food in common spaces."

    s "You just took a chip."

    show charlotte neutral at center

    c "...Is that a big deal?"

    s "It's the biggest deal."

    s_thoughts "Charlotte looks at me."

    s_thoughts "I look at Charlotte."

    s_thoughts "Something crosses her face. Not the flicker. Not the mask refreshing. Something slower. The realization of what she just did."

    s_thoughts "She just wanted a chip and she took a chip."

    show charlotte smile at center

    c "It was a good chip."

    s "Have another one."

    s_thoughts "She reaches into the bag again. Takes another chip. Slower this time. Aware of herself."

    s_thoughts "She eats it."

    show charlotte happy at center

    c "These are really good."

    s "I know."

    s_thoughts "She takes a third chip."

    s_thoughts "By the fourth, she stops noticing she's doing it."

    s_thoughts "That's the point."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 5: LILA CHECKS IN
    ## Campus. Lila's sister subplot.
    ## "She seems less perfect. Is that weird to say?"
    ## (Scenes 5 and 15 merged per architecture note.)
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)
    play music mus_campus fadein 2.0
    
    s_thoughts "Lila and I are hanging out at the usual spot."

    show lila happy at center with dissolve

    l "So how's the toast girl?"

    s "Don't call her the toast girl."

    l "Egg girl? Chef girl? Girl who wakes up at sunrise to feed your entire household like a benevolent dictator?"

    s "Her name is Charlotte."

    l "I KNOW her name is Charlotte. I'm asking how she's doing."

    s "She's... trying."

    show lila annoyed at center

    l "Trying what?"

    s "To be different. I think."

    l "Different how?"

    s "Less -- I don't know how to say this without it sounding weird."

    l "Soph, everything you say sounds weird. I'm calibrated."

    s "She's not doing the thing. The everything-is-fine thing. Or she's TRYING not to. She said no to something the other day. Like, an actual no."

    show lila shocked at center

    l "CHARLOTTE said no?"

    s "To going to the store."

    l "Charlotte. Pink hair Charlotte. 'Of course!' Charlotte. Said NO?"

    s "She did."

    l "Was there an earthquake?"

    s "There was not."

    show lila happy at center

    l "Huh."

    s "What?"

    l "Nothing. She just seems -- I don't know. Less perfect. Is that weird to say?"

    s "That's the best compliment you could give her."

    l "It's not a COMPLIMENT. It's an observation. She seems like a person instead of a -- what did you call it? A care package with legs?"

    s "I never called her that."

    l "You THOUGHT it. I could tell."

    s_thoughts "I might have thought it."

    l "So she's trying. You're trying. Very romantic. Two people trying."

    s "Shut up."

    show lila laugh at center

    l "Oh -- speaking of trying. My sister."

    s "What happened?"

    l "She told our dad the business club is boring."

    s "Your sister. The one who joined business club because of you."

    l "The very one. She told Dad -- to his FACE -- that she thinks accounting is 'the saddest math.' Sophia. She called accounting the saddest math."

    s "Is she wrong?"

    l "She is objectively correct and I'm TERRIFIED."

    s "Terrified?"

    show lila annoyed at center

    l "Because she's pushing back. She's actually -- she's finding her own thing. She joined the theater club. THEATER. The thing I wanted to do. The thing I didn't do because Dad said it wasn't practical."

    s "Lila."

    l "She's sixteen and she's braver than me. She told Dad to his face and he just -- he blinked. He didn't yell. He didn't do the disappointed thing. He blinked and said 'okay.'"

    s "That's good."

    l "Is it? Because I've spent years in business and she spent MINUTES and she got 'okay.' I got a LECTURE about career viability."

    s "Maybe you got the lecture so she didn't have to."

    show lila shocked at center

    s_thoughts "Lila goes quiet."

    s_thoughts "Lila doesn't go quiet."

    l "..."

    l "That's annoyingly insightful."

    s "I have my moments."

    show lila happy at center

    l "She did the thing I can't do. She just -- said it. Out loud. To the person it mattered to."

    s_thoughts "I think about Charlotte."

    s "She's trying. We both are."

    l "God, we're all a mess."

    s "Speak for yourself."

    l "I'm speaking for EVERYONE."

    s_thoughts "She grins."

    hide lila with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 6: HAPPY GIRLFRIEND MORNING
    ## Charlotte shows Sophia her Vermeer research.
    ## Real nerd energy. Forgets to offer coffee.
    ## That's the point.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Thursday morning."

    s_thoughts "I come downstairs and Charlotte is at the table with her laptop open and three books stacked next to her coffee and she's got that look."

    s_thoughts "The focus face. Bottom lip under teeth."

    show charlotte happy at center with dissolve
    
    play music mus_charlotte fadein 1.5

    c "SOPHIA."

    s "Mm?"

    c "Okay. Okay, listen. I found something."

    s "Good morning to you too."

    c "Good morning, yes, hi -- LISTEN. So you know the Vermeer paper? The one about domestic space and the frame?"

    s "The one you've been writing for three weeks?"

    c "Yes! Okay so I was reading this essay by Svetlana Alpers -- she's a Rembrandt scholar but she wrote about Vermeer too -- and she talks about the MAP."

    s "The map?"

    c "In the paintings! There's a map on the wall in like HALF of Vermeer's domestic interiors. A map of the world. Hanging on the wall of the room where the woman is trapped."

    s "Huh."

    c "Don't you SEE? The world is right there. It's ON THE WALL. But the woman is pouring milk. She's reading a letter. She's making lace. The world is literally hanging on her wall and she never looks at it because her whole world IS the room."

    s_thoughts "Charlotte is talking fast. Her hands are moving. She's gesturing at the laptop like it personally offended her on the day of her daughter's wedding."

    c "And the maps aren't decorative! They're accurate. Cartographic or whatever."
    
    c "They represent exploration and commerce and the Dutch Golden Age and -- and the woman is INSIDE the room that's inside the painting that's inside the museum and the map is the only thing in the room that points OUTSIDE."

    s "Charlotte."

    c "What?"

    s "You haven't offered me coffee."

    show charlotte surprised at center

    c "I -- oh. Oh! Sorry, I--"

    s "Don't apologize."

    s_thoughts "I get up. I make my own coffee."

    s_thoughts "Charlotte watches me do it. Her face -- a flicker. It passes."

    s_thoughts "Charlotte forgot because she was excited about a map in a painting from 1658."
    
    s_thoughts "...I don't mind making my own coffee."

    show charlotte happy at center

    c "So the thesis is -- the thesis is that the frame isn't just the painting. The frame is the room, the wall, the map, the window. Every element is a different kind of frame. And the woman is inside ALL of them."

    s "Like nesting dolls."

    c "Like nesting dolls! Like cages inside cages. And she looks peaceful because she doesn't know she's inside them."

    s_thoughts "Charlotte's eyes are bright. She found something that excites her and she wants to share it."

    c "Morin is going to love this. Or hate it. She has opinions about Alpers."

    s "She'll love it."

    show charlotte smile at center

    c "You always say that."

    s "Because you're always good."

    s_thoughts "She doesn't say 'of course.' She doesn't deflect."

    s_thoughts "She just looks at me. A little surprised. Like a compliment about her brain doesn't have a pre-built response."

    c "...Okay. More coffee?"

    s "I just got coffee."

    c "Right. Right."

    s_thoughts "She goes back to the laptop. Her knee is bouncing under the table."

    s_thoughts "I drink my coffee and read my Goffman and Charlotte mutters about cartographic symbolism and it's the best morning."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 7: PROFESSOR'S FEEDBACK
    ## Charlotte gets notes on the paper.
    ## "You describe the cage beautifully. But you never ask why the women stay."
    ## CHOICE 2.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)
    play music mus_sunlight fadein 2.0

    s_thoughts "Friday. Charlotte comes out of her professor's office looking like someone adjusted her internal thermostat by three degrees."

    show charlotte neutral at center with dissolve

    s "How'd it go?"

    c "Fine."

    s_thoughts "Charlotte saying 'fine' without exclamation marks is an unusual phenomenon."

    s "What did she say?"

    c "She said my argument about the frame is strong. The map section needs more development. The writing is 'clean and precise.'"

    s "That's good."

    c "She also said -- hold on, I wrote it down."

    s_thoughts "Charlotte checks her phone."

    c "'You describe the cage beautifully. But you never ask why the women stay.'"

    s "..."

    s_thoughts "Charlotte puts her phone away."

    s_thoughts "She's quiet."

    s_thoughts "Something hit."

    s_thoughts "I open my mouth."

    menu:
        "\"What do you think she meant?\"":
            $ charlotte_push += 1

            s "What do you think she meant?"

            show charlotte embarrassed at center

            c "I don't -- it's a fair note. Academically. Why DO they stay? In the paintings? They could leave. The door is right there."

            s "Can they leave?"

            c "Of course they can. It's a room. Rooms have doors."

            s "Do they know the doors are there?"

            show charlotte neutral at center

            s_thoughts "Charlotte looks at me."

            s_thoughts "She hears it."

            c "...It's a paper, Sophia. About paintings."

            s "I know."

            c "I'm not -- I don't need to make it about--"

            s "I didn't say anything."

            c "You're making a face."

            s "What face?"

            c "Like you're saying 'I see through you'."

            s_thoughts "Now she's making a face."

            c "Like THAT."

            s_thoughts "She's deflecting. But she's deflecting slower than she used to."

            show charlotte happy at center

            c "I'll think about it. The note. I just need to -- sit with it."

            s "Okay."

            s_thoughts "She doesn't say 'of course.'"

            s_thoughts "She doesn't say anything for a while."

            s_thoughts "We walk."

            jump charlotte_ch5_scene8

        "Don't ask. Let Charlotte process.":
            $ charlotte_present += 1
            $ charlotte_push -= 1

            s_thoughts "I swallow the question."

            s_thoughts "It's right there. 'Do you think she's talking about you?' It's sitting on my tongue. The question is RIGHT THERE."

            s_thoughts "I swallow it."

            s "Want to get coffee?"

            show charlotte surprised at center

            s_thoughts "Charlotte looks at me. She expected the question. I can see her bracing for it."

            s_thoughts "I didn't ask."

            show charlotte smile at center

            c "...Yeah. Coffee sounds good."

            s_thoughts "We walk. Charlotte is quiet. Processing."

            s_thoughts "Halfway to the coffee shop she says:"

            c "I think I need to rethink the whole paper."

            s "Yeah?"

            c "Maybe it's not about the cage. Maybe it's about why you'd build one."

            s_thoughts "She says it like she's talking about Vermeer."

            s_thoughts "She's not talking about Vermeer."

            s_thoughts "I don't say that."

            s "That's a better paper."

            c "Morin will either love it or tell me I'm overreaching."

            s "You're not overreaching."

            show charlotte happy at center

            s_thoughts "She bumps my shoulder. I bump hers back."

            s_thoughts "I didn't ask. Charlotte is thinking anyway."

            s_thoughts "Maybe the question doesn't need to come from me."

            jump charlotte_ch5_scene8

        "Change the subject.":
            $ charlotte_present -= 1

            s "Want to talk about something else?"

            show charlotte smile at center

            c "Yes. God, yes. Tell me something stupid."

            s "The Goffman reading has a typo on page 47. He wrote 'pubic performance' instead of 'public performance.'"

            show charlotte laugh at center

            c "He did NOT."

            s "Page 47. I circled it."

            c "SOPHIA."

            s "It changes the entire argument."

            s_thoughts "Charlotte is laughing. The real one. The brightness is back but it's the kind that covers something."

            s_thoughts "I changed the subject because Charlotte wanted me to. That's the easy thing."

            s_thoughts "But Charlotte's professor just told her 'you never ask why they stay' and Charlotte needed to sit with that and I took it away."

            s_thoughts "Because Charlotte wanted me to."

            s_thoughts "Charlotte always wants people to take the hard things away. That's the whole problem."

            jump charlotte_ch5_scene8

    ## ===========================
    ## SCENE 8: ISABELLA BACKGROUND TRAGEDY
    ## Brief. ONE FRAME face change before the smile.
    ## Apple. Lumi chat. Don't explain.
    ## ===========================

label charlotte_ch5_scene8:

    hide charlotte with dissolve
    stop music fadeout 1.5

    scene bg kitchen with dissolve
    play music mus_shoulders fadein 2.0

    s_thoughts "Saturday afternoon."

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte and I are in the kitchen. She's reading a passage from her Vermeer paper aloud and I'm pretending to understand Dutch art criticism. Our shoulders are touching."

    c "So the argument is that Vermeer's light is ALWAYS from the left. Always from a window we can see but the subject can't reach. It's -- here, listen to this line--"

    s_thoughts "The door opens."

    show isabella smile at right with dissolve

    s_thoughts "Isabella. She notices us."

    show isabella neutral at right

    pause 1.5

    show isabella smile at right

    i "You two are gross."

    c "We're studying!"

    s_thoughts "Isabella opens the fridge. Grabs an apple."

    i "Alright lovebirds. Carry on with your... Dutch romance."

    c "It's not just ROMANCE. It's art criticism."

    show isabella happy at right

    i "Same thing."

    s_thoughts "She leaves. The door swings shut."
    
    hide isabella with dissolve

    s_thoughts "Charlotte laughs."

    show charlotte laugh at left

    c "She's so funny."

    s_thoughts "She is."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 9: CHARLOTTE ASKS ABOUT EVE
    ## Charlotte is genuinely lost. No script for this.
    ## CHOICE 3. (charlotte_eve tracked)
    ## ===========================

    scene bg livingroom night with Fade(0.8, 0.3, 0.8)
    play music mus_2am fadein 2.0

    s_thoughts "Sunday night."

    s_thoughts "Charlotte is on the couch. I'm in the armchair. She's got a mug of tea she's been holding for twenty minutes without drinking."

    show charlotte neutral at center with dissolve

    s_thoughts "The house is quiet. Isabella's music is off. Amara's door was closed when I walked by. Eve's--"

    s_thoughts "Eve's door has been closed for two days."

    c "Can I ask you something?"

    s "Yeah."

    c "I don't know what to do about Eve."

    s_thoughts "She says it plain. No preamble. No brightness."

    c "She barely talks to me anymore. And I know -- I know the chore chart thing was -- I KNOW. But I don't know how to fix it."

    s "What do you think happened?"

    c "I think I did the thing where I -- organized her. Like she was a project. And she felt it."

    s "She did feel it."

    show charlotte sad at center

    c "I know."

    c "But what am I supposed to DO? I tried giving her space. She went further away. I tried talking to her. She said three words and left. I tried not trying and that just felt like ignoring her."

    s_thoughts "Charlotte's hands are tight around the mug."

    c "My whole -- everything I know how to do is the OPPOSITE of what she needs."

    s_thoughts "She's genuinely lost."

    s_thoughts "Charlotte doesn't have a script for when someone experiences her whole thing as control, not comfort."

    menu:
        "Charlotte is asking about Eve."

        "\"Be honest with her. Tell her you know the chore chart was about control.\"":
            $ charlotte_push += 1
            $ charlotte_eve += 1

            s "Be honest with her."

            show charlotte surprised at center

            c "I AM honest with her."

            s "Charlotte. Tell her you know the chore chart wasn't about cleaning. Tell her you know it was about control. That you were organizing the house because you can't not organize things and she felt it and you're sorry."

            c "I can't just SAY that."

            s "Why not?"

            c "Because what if she--"

            s_thoughts "She stops."

            c "What if she agrees."

            s "Then she agrees. And you deal with it."

            show charlotte neutral at center

            c "You make it sound simple."

            s "It's not simple. But it's honest."

            s_thoughts "Charlotte drinks the tea she's been holding for twenty minutes."

            s_thoughts "It must be cold by now."

            c "You think she'd listen?"

            s "I think Eve respects honesty more than effort."

            c "That's terrifying."

            s "Yeah."

            show charlotte sad at center

            c "I don't know how to be honest without a plan."

            s "Maybe that's the plan."

            s_thoughts "Charlotte is quiet for a long time."

            c "...I'll think about it."

            s "Okay."

            s_thoughts "She drinks more cold tea."

            jump charlotte_ch5_scene10

        "\"She'll come around. Just give her space.\"":
            $ charlotte_present += 1
            $ charlotte_eve -= 1

            s "She'll come around. Just give her space."

            show charlotte smile at center

            s_thoughts "Charlotte's face relaxes."

            s_thoughts "That's the wrong reaction."

            c "You think so?"

            s "Eve is -- she's Eve. She pulls away and comes back. That's her pattern."

            c "That IS her pattern."

            s "Just give it time."

            c "Time. I can do time."

            s_thoughts "Charlotte nods. She drinks her tea."

            s_thoughts "I just told Charlotte the comforting thing. The thing that lets her not change. 'She'll come around' is the Charlotte solution -- wait it out and keep being warm and eventually the other person adapts."

            s_thoughts "Eve doesn't adapt. Eve leaves."

            s_thoughts "But Charlotte is smiling and her shoulders are down and she looks less tense and I don't have the heart to take that away from her right now."

            s_thoughts "Maybe Eve will come around."

            s_thoughts "Maybe."

            jump charlotte_ch5_scene10

    ## ===========================
    ## SCENE 10: CHARLOTTE'S ROOM — THE FIRST THING
    ## Charlotte puts something on her wall. A postcard.
    ## Just because she likes it. Sophia sees it. Doesn't mention it.
    ## ===========================

label charlotte_ch5_scene10:

    hide charlotte with dissolve
    stop music fadeout 2.0

    scene bg charlottebedroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "I'm looking for my charger. Charlotte said she might have it."

    s_thoughts "Charlotte's room is Charlotte's room."

    s_thoughts "But there's something new."

    s_thoughts "A postcard. Tacked to the wall above her desk. A Vermeer painting -- not the milk maid. A different one. A woman reading a letter by a window."

    s_thoughts "It's not for anyone."

    s_thoughts "I find my charger on her desk. I leave."

    s_thoughts "I don't mention the postcard."

    ## ===========================
    ## SCENE 11: A BAD DAY THAT'S JUST A BAD DAY
    ## Charlotte is grumpy. Actually grumpy.
    ## Not performed-fine. Not mask-crisis.
    ## Just a bad day.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_baddecisions fadein 1.5

    s_thoughts "Tuesday."

    s_thoughts "Charlotte comes home at 4 PM. She drops her bag in the hallway. She doesn't hang it on the hook. Charlotte ALWAYS hangs it on the hook."

    show charlotte annoyed at center with dissolve

    s_thoughts "She walks into the kitchen. She opens the fridge. Closes the fridge. Opens it again. Takes nothing."

    c "There's nothing to eat."

    s "There's the leftover--"

    c "There's nothing I WANT to eat."

    s_thoughts "Charlotte doesn't say things like 'there's nothing I want to eat.' Charlotte makes do. Charlotte finds the silver lining in an empty fridge and turns it into a teachable moment about meal planning."

    s "Bad day?"

    c "My visual culture lecture was two hours of a man explaining Derrida to a room full of people who already read Derrida. My coffee was cold by the time I got to drink it. I stepped in a puddle. A BIG puddle. My sock is still wet."

    s "That sounds--"

    c "And the bus was late. And someone on the bus was eating a tuna sandwich. A TUNA SANDWICH, Sophia. On PUBLIC TRANSIT."

    s "Criminal behavior."

    c "It should be. It should be ILLEGAL."

    s_thoughts "She's actually grumpy. Wet sock. Cold coffee. Tuna sandwich."

    s_thoughts "I'm watching Charlotte be grumpy like I'm witnessing a solar eclipse."

    c "Stop looking at me like that."

    s "Like what?"

    c "Like me being annoyed is cute."

    s "It IS cute."

    show charlotte annoyed at center

    c "I hate you."

    s_thoughts "She doesn't mean it."

    s_thoughts "That's new too."

    s_thoughts "Charlotte metabolizes annoyance so fast it never reaches her face."

    s_thoughts "But Charlotte just said 'I hate you' and it was the least Charlotte thing she's ever done and I kind of want to frame it."

    s "Do you want tea?"

    c "I don't want tea. I want a TIME MACHINE so I can un-step in the puddle."

    s "I can't help you with the time machine."

    c "Then you're useless."

    s_thoughts "She takes her wet sock off and throws it toward the stairs to the basement where the laundry is. It doesn't make it. It lands on the kitchen floor."

    s_thoughts "Charlotte looks at the sock on the floor."

    show charlotte neutral at center

    s_thoughts "Charlotte leaves the sock on the floor."

    c "I'm going to lie on the couch and hate everything for twenty minutes."

    s "Okay."

    c "Don't talk to me."

    s "Okay."

    s_thoughts "She goes to the living room. I hear the couch creak."
    
    hide charlotte with dissolve

    s_thoughts "I pick up the sock."

    s_thoughts "Charlotte doesn't know I picked up the sock."

    s_thoughts "That's fine."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 12: SOPHIA'S VULNERABILITY — THE RECIPROCITY SCENE
    ## Sophia has a bad moment. Charlotte wants to FIX.
    ## "Can you just sit here and not fix anything?"
    ## CHOICE 4. (Big one — present +2 for genuine vulnerability.)
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Thursday."

    s_thoughts "I bombed the Goffman quiz."

    s_thoughts "Not 'I didn't do great' bombed. BOMBED. The kind where you turn the paper over and the first question doesn't even look like a language you speak."

    s_thoughts "I know this material. I KNOW Goffman. I've been reading about performance theory while dating a girl who is a walking case study. I should be the leading expert on Goffman."

    s_thoughts "I wrote 'frontstage' when the answer was 'backstage.' I reversed the entire framework."

    s_thoughts "I'm sitting on my bed looking at the wall."

    s_thoughts "There's a knock."

    show charlotte smile at center with dissolve

    c "Hey. I noticed you came home early. Are you -- do you want tea? I can make tea. Or food? I think there's--"

    s "Ugh."

    show charlotte surprised at center

    s_thoughts "She's already in care mode. I can see the program running. 'Sophia is upset. Deploy comfort protocol. Tea, food, gentle questions, physical presence.'"
    
    play music mus_charlotte_sad fadein 2.0

    s "Can you just sit here and not fix anything?"

    s_thoughts "Charlotte freezes."

    s_thoughts "Her hand is already reaching for the doorframe. Her body is oriented toward the kitchen. Every part of her is programmed to GO and DO and HELP."

    show charlotte neutral at center

    c "...Okay."

    s_thoughts "She sits on the bed."

    s_thoughts "She doesn't DO anything."

    s_thoughts "She just sits."
    
    s_thoughts "It's the most difficult nothing I've ever seen."

    s_thoughts "Her hands are in her lap. They're twitching. She keeps almost reaching for my shoulder, pulling back. Almost asking 'what's wrong,' swallowing it."

    s_thoughts "She's sitting next to me on a bed doing nothing and it looks like it's costing her oxygen."

    s_thoughts "We sit."

    s_thoughts "One minute. Two."

    s_thoughts "Charlotte's knee is bouncing."

    s_thoughts "Three minutes."

    c "This is awful."

    s "I know. Thank you."

    c "I don't know what to do with my hands."

    s "You don't have to do anything with your hands."

    c "They want to make tea."

    s "Tell them no."

    show charlotte sad at center

    c "I told them no. They're angry about it."

    s_thoughts "I almost laugh."
    
    s_thoughts "I don't."

    s_thoughts "Charlotte is sitting next to me not fixing me and it's the most generous thing anyone has ever done."

    menu:
        "Charlotte is sitting without fixing. Do I meet her?"

        "Tell her what happened. Really tell her.":
            $ charlotte_present += 2

            s "I bombed a quiz."

            c "Okay."

            s_thoughts "That's it. Just 'okay.'"

            s "I know the material. I've been reading Goffman for weeks. I reversed frontstage and backstage."

            c "Reversed them?"

            s "I wrote the opposite of the right answer. For every question. Like I KNOW the answer and my brain said 'do the wrong one.'"

            s_thoughts "I'm looking at the wall."

            s "I do this. I take something I care about and I overthink it until it breaks. Katie used to say -- she said I analyze everything so hard I lose the thing I was analyzing."

            s_thoughts "I don't talk about Katie. I don't bring Katie into this room."

            s_thoughts "But I just did."

            show charlotte neutral at center

            s_thoughts "Charlotte is listening. Not fixing-listening. Just listening."

            s "She was right. Katie. She was right about that."

            c "She doesn't get to be right about you."

            s_thoughts "Charlotte says it quiet. Not the care-package voice. The voice from the porch."

            s "She's right though. I do it. I'm doing it right now. I'm analyzing my analysis of a quiz about performance analysis."

            c "How many layers deep is that?"

            s "At least four."

            show charlotte smile at center

            c "That's impressive."

            s "It's exhausting."

            c "Yeah."

            s_thoughts "She's sitting. Still sitting. Her hands have stopped twitching."

            s_thoughts "I just told Charlotte about the quiz and about Katie and about the thing I do and she didn't fix any of it."

            s_thoughts "She sat there."

            s "Thank you."

            c "For what?"

            s "For not making tea."

            show charlotte happy at center

            c "It was the hardest thing I've ever done."

            s "I know."

            s_thoughts "She leans her head on my shoulder."

            s_thoughts "The new one. Weight."

            s_thoughts "We sit."

            jump charlotte_ch5_scene13

        "Let her sit. Accept the sitting.":
            $ charlotte_push += 1

            s_thoughts "We sit."

            s_thoughts "I don't tell her what happened. I don't mention that I'm thinking about Katie. I don't explain the quiz."

            s_thoughts "I just let Charlotte sit next to me and not fix anything."

            s_thoughts "Five minutes."

            s_thoughts "Charlotte exhales."

            c "I sat."

            s "You sat."

            c "It was terrible."

            s "Thank you for sitting."

            show charlotte smile at center

            c "You're welcome. Never make me do that again."

            s "No promises."

            s_thoughts "She bumps my shoulder. I bump hers."

            s_thoughts "Charlotte sat without fixing. I let her."

            s_thoughts "Neither of us met all the way in the middle. But we were in the room."

            jump charlotte_ch5_scene13

        "Deflect. Make it funny.":
            $ charlotte_push -= 1
            $ charlotte_present -= 1

            s "I'm fine. Goffman hates me personally."

            show charlotte smile at center

            c "Goffman doesn't hate you."

            s "He hates me. It's personal. He wrote 'The Presentation of Self in Everyday Life' specifically to ruin my Thursday."

            c "That book was published in 1956."

            s "Long-term grudge."

            s_thoughts "Charlotte laughs. I laugh."

            s_thoughts "And we both pretend I wasn't just staring at a wall."

            s_thoughts "I did the thing I asked her not to do."

            s_thoughts "Performed."

            jump charlotte_ch5_scene13

    ## ===========================
    ## SCENE 13: THE FIRST REAL FIGHT
    ## "I can FEEL you being careful."
    ## No immediate apology. Separate rooms.
    ## CHOICE 5.
    ## ===========================

label charlotte_ch5_scene13:

    hide charlotte with dissolve
    stop music fadeout 2.0

    scene bg kitchen with Fade(1.5, 0.5, 1.5)

    s_thoughts "Friday."

    s_thoughts "It starts over nothing."

    s_thoughts "Charlotte comes home from class. She looks fine. A normal day."

    s_thoughts "I'm in the kitchen. I ask how her day was. Normal question."

    show charlotte smile at center with dissolve

    c "Good! Class was good. Morin liked the map section."

    s "That's great."

    s_thoughts "I say 'that's great' and I mean it but I also hear it come out and it sounds careful. Like I'm handling a thing that's fragile."

    s_thoughts "Charlotte hears it too."

    show charlotte neutral at center

    c "What?"

    s "Nothing. I said that's great."

    c "You said it weird."

    s "I didn't say it weird."

    c "You said it like you were checking on me."

    s "I wasn't checking on you."

    show charlotte annoyed at center

    c "You were. You had the voice."

    s "What voice?"

    play music mus_glass fadein 1.5

    c "The CAREFUL voice. The voice you use when you're -- when you're monitoring me. Like I'm a -- like I'm a PATIENT."

    s "Charlotte, I asked how your day was."

    c "You asked how my day was in the voice that means 'are you okay or are you about to relapse.'"

    s_thoughts "That stings."

    s_thoughts "Because she's not wrong."

    s "I just--"
    
    c "I told you about the stool."
    
    s_thoughts "I freeze."

    c "And now every time I say I'm fine you look at me like -- like you're CHECKING. Checking for the stupid stool."

    s "I... I'm careful because I care."
    
    s_thoughts "I'm trying to deflect. It's not working."

    show charlotte sad at center

    c "I know you care! That's not -- that's the PROBLEM. Everything I do -- EVERYTHING -- you're watching it to see if it's real or if it's the 'backstage'."
    
    s_thoughts "That hurts."

    s "That's not--"

    c "Yes it IS. I can't -- I can't EXIST without you cataloguing it."

    s_thoughts "The kitchen is quiet."

    s_thoughts "Charlotte is breathing hard. Her eyes are bright -- not the mask-bright. Anger-bright."

    c "I told you because I trusted you. Not so you could watch me better."

    menu:
        "\"I'm sorry. You're right.\"":
            $ charlotte_present += 1

            s "You're right."

            show charlotte surprised at center

            s "I've been doing it. The careful thing. I didn't -- I thought I was being supportive but I was being--"

            c "Careful."

            s "Careful."

            s_thoughts "Charlotte's shoulders drop an inch."

            s_thoughts "The anger isn't gone. But the recognition is there."

            c "I'm sorry I snapped."

            s "Don't be sorry. You were right."

            c "I was right AND I was mean about it."

            s "You weren't mean. You were honest."

            show charlotte neutral at center

            s_thoughts "Charlotte looks at me for a long time."

            c "I'm going to go -- I need to be alone for a bit."

            s "Okay."

            s_thoughts "She goes upstairs. I hear her door close."

            s_thoughts "Not a slam. Just a close."
            
            s_thoughts "She never closes her door."

            s_thoughts "I stand in the kitchen."

            s_thoughts "She was right. I've been handling her. Watching her instead of being WITH her."

            s_thoughts "The file again. Katie again."

            s_thoughts "I do this."

            jump charlotte_ch5_scene14_apologized

        "\"I'm careful because I don't want to lose this.\"":
            $ charlotte_push += 1

            s "I'm careful because I don't want to lose this."

            show charlotte surprised at center

            s_thoughts "Charlotte blinks."

            s "You told me about the stool and the extra places and your mom and -- Charlotte, you gave me the real thing. And now I'm terrified of breaking it."

            c "You're not going to break me."

            s "You don't know that."

            c "I'm not BREAKABLE."

            s "I didn't say you were breakable. I said I was scared."

            show charlotte neutral at center

            s_thoughts "The kitchen is very quiet."

            c "..."

            c "I don't want you to be scared of me."

            s "I'm not scared of you. I'm scared of me. Of the thing I do. Where I notice everything and turn it into--"

            c "A project."

            s "..."

            c "Like Katie."
            
            s_thoughts "..."
            
            c "I don't want to be a project."
            
            c "I don't want to be Katie."

            s_thoughts "That lands."

            s "I don't -- that's not what I--"

            c "I'm going upstairs."

            s "Charlotte--"

            c "I just need -- I need to not be in this kitchen."

            s_thoughts "She leaves."
            
            hide charlotte with dissolve

            s_thoughts "I stand in the kitchen."

            s_thoughts "She said 'Like Katie.' And I wanted to argue. And I couldn't."

            s_thoughts "Because she's right."

            jump charlotte_ch5_scene14_pushed

        "Wait for Charlotte to come to you.":
            $ charlotte_present -= 1

            s_thoughts "I don't say anything."

            s_thoughts "Charlotte is standing in the kitchen breathing hard and I don't say anything because I don't know what to say and also because part of me is thinking 'she'll come back. She always comes back.'"

            show charlotte sad at center

            c "..."

            c "I'm going upstairs."

            s "Okay."

            s_thoughts "She goes."

            s_thoughts "I stand in the kitchen."

            s_thoughts "I didn't apologize. I didn't push back. I didn't do anything."

            s_thoughts "I let her do it again."

            jump charlotte_ch5_scene14_waited

    ## ===========================
    ## SCENE 14: THE REPAIR (CONDITIONAL on Scene 13 choice)
    ## The morning after the fight.
    ## Three versions.
    ## ===========================

    ## ===========================
    ## SCENE 14A: REPAIR — APOLOGIZED THAT NIGHT
    ## Tentative warmth. Coffee but not breakfast.
    ## ===========================

label charlotte_ch5_scene14_apologized:

    stop music fadeout 2.0
    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_morningafter fadein 2.0

    s_thoughts "Saturday morning."

    s_thoughts "Charlotte is at the table."

    s_thoughts "She made coffee. Not breakfast. Coffee."

    s_thoughts "The table has two mugs. No plates. No forks. No flowers."

    s_thoughts "A compromise."

    show charlotte neutral at center with dissolve

    s "Morning."

    c "Morning."

    s_thoughts "We sit."

    s_thoughts "The fight is still in the room. It's lingering like a particularly unpleasant fart."

    c "I'm sorry I said you were handling me."

    s "You weren't wrong."

    c "I know. I'm sorry I said it like that, though."

    s "Like what?"

    show charlotte sad at center

    c "Like you were the problem. You're not the problem. The -- the way I feel about being watched is the problem. You were being kind and I turned it into an attack because--"

    s "Because it felt like one."

    c "Yeah."

    s "That makes sense."

    s_thoughts "Charlotte wraps her hands around her mug."

    show charlotte neutral at center

    c "I don't want you to stop noticing things."

    s "No?"

    c "It's why I -- you SEE things. That's why I trust you. I just need -- sometimes I need you to see things and not DO anything with them."

    s "I can try that."

    c "Can you?"

    s "No. But I can try."

    show charlotte smile at center

    s_thoughts "A small laugh. Almost."

    s_thoughts "The coffee is warm. The kitchen is quiet. Two people who had a fight and are sitting with the aftermath."

    s_thoughts "Nobody is performing."

    s_thoughts "That's new."

    jump charlotte_ch5_scene14_5

    ## ===========================
    ## SCENE 14B: REPAIR — PUSHED BACK
    ## Tense morning. Heavy silence. But Charlotte didn't perform "fine."
    ## ===========================

label charlotte_ch5_scene14_pushed:

    stop music fadeout 2.0
    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_2am fadein 2.0

    s_thoughts "Saturday morning."

    s_thoughts "Charlotte is at the table."

    s_thoughts "She has coffee. She's not reading. She's not on her phone. She's just sitting with coffee."

    show charlotte neutral at center with dissolve

    s_thoughts "I sit down."

    s "Morning."

    c "Morning."

    s_thoughts "Silence."

    s_thoughts "The kind where both people know the other person is right and neither person wants to be the first to say it."

    s_thoughts "Charlotte is not performing 'fine.' She's... performing not performing."

    s_thoughts "That might be progress. Maybe."

    s_thoughts "It doesn't feel like progress."

    s_thoughts "I pour myself coffee. Sit back down."

    s_thoughts "We drink in silence."

    s_thoughts "Charlotte's hands are tight on the mug."

    s_thoughts "Five minutes."

    c "I meant what I said."

    s "I know."

    c "I don't want to be a project."

    s "I know."

    c "Do you?"

    s_thoughts "I look at her."

    s "I'm trying."

    show charlotte sad at center

    c "..."

    s_thoughts "She nods. Not convinced. Not dismissing."

    s_thoughts "Just sitting in it."
    
    c "I shouldn't have said what I said. About Katie. That was too far."
    
    s "Yeah. But it was true."
    
    c "Yeah. I'm sorry. About that. Not the other stuff."
    
    s_thoughts "We both sit with that."

    s_thoughts "The fight isn't resolved. Both of us know it. But Charlotte is sitting in the kitchen not performing recovery and that's something."

    s_thoughts "It's not enough. But it's something."

    jump charlotte_ch5_scene14_5

    ## ===========================
    ## SCENE 14C: REPAIR — WAITED (Charlotte came first. Of course.)
    ## Charlotte apologizes first. The pattern holds.
    ## ===========================

label charlotte_ch5_scene14_waited:

    stop music fadeout 2.0
    scene bg kitchen night with Fade(0.8, 0.3, 0.8)
    play music mus_charlotte fadein 2.0

    s_thoughts "Friday night."

    s_thoughts "10 PM. I'm in my room. Reading. Not reading. Looking at a book."

    s_thoughts "Knock."

    show charlotte sad at center with dissolve

    c "Hey."

    s "Hey."

    c "I shouldn't have snapped at you."

    s_thoughts "There it is."

    s_thoughts "Charlotte came first. Of course Charlotte came first."

    c "I said things I didn't mean and I shouldn't have raised my voice and I'm sorry."

    s "Charlotte--"

    c "I know you were being kind. I know the careful voice comes from caring. I just -- I need to not feel watched sometimes. But that's my thing to manage."

    s_thoughts "'My thing to manage.'"

    s_thoughts "Charlotte Opal. Apologizing for having a feeling."

    s "It's okay."

    c "It's not, but thank you."

    s_thoughts "She smiles. Thin."

    show charlotte smile at center

    c "Goodnight."

    s "Goodnight."

    s_thoughts "She goes back to her room."

    s_thoughts "Charlotte apologized first."

    s_thoughts "Charlotte ALWAYS apologizes first."

    s_thoughts "I let her."

    s_thoughts "The fight changed nothing."

    scene bg kitchen with dissolve

    s_thoughts "Saturday morning. Charlotte made coffee. She's at the table. She smiles when I come down."

    show charlotte smile at center with dissolve

    c "Morning! Sleep well?"

    s "Yeah."

    s_thoughts "The brightness is back. Not full-wattage. But it's there."

    s_thoughts "Last night didn't happen. Charlotte filed it under 'resolved' because she apologized and I accepted and the system works."

    s_thoughts "It works the way it's always worked."

    s_thoughts "It doesn't work."

    jump charlotte_ch5_scene14_5

    ## ===========================
    ## SCENE 14.5: CHARLOTTE FATIGUE
    ## The exhaustion of self-monitoring.
    ## "I'm so tired of paying attention to whether I'm paying attention."
    ## Bridge to Act 2.
    ## ===========================

label charlotte_ch5_scene14_5:

    hide charlotte with dissolve
    stop music fadeout 2.0

    scene bg charlottebedroom with Fade(1.0, 0.5, 1.0)

    s_thoughts "Sunday."

    s_thoughts "Charlotte comes home at 5 PM."

    s_thoughts "She doesn't say hello. She doesn't check the kitchen. She doesn't straighten anything on the way to her room."

    s_thoughts "I find her sitting on her bed. Not reading. Not on her phone. Just sitting."

    show charlotte sad at center with dissolve

    s "Hey."

    c "Hey."

    s_thoughts "She's tired."

    s "What's up?"

    c "Nothing. I'm just -- tired."

    s "Like sleep-tired?"

    c "Like..."

    s_thoughts "She leans back. Stares at the ceiling."

    show charlotte neutral at center
    play music mus_charlotte_sad fadein 3.0

    c "I'm so tired of paying attention to whether I'm paying attention."

    s "..."

    c "Every morning I wake up and I think 'am I making eggs because I want to or because I'm performing?' And then I think 'does it matter why I'm making eggs?'"
    
    c "And then I think 'the fact that I'm asking means it matters' and then I'm standing in the kitchen with a spatula having an EXISTENTIAL CRISIS about eggs."

    s "..."

    c "And then I don't make eggs. And not making eggs feels like a statement. And then I think 'is not making eggs also a performance?' And then I want to SCREAM."

    s_thoughts "She sits up."

    c "And saying no. Saying no is supposed to be -- it felt good! For five seconds. And then the rest of the day I'm thinking 'was that a real no? Did I say no because I wanted to or because you want me to say no?'"
    
    c "And I can't -- I can't tell."

    s_thoughts "Her voice is ragged."

    c "I'm performing not-performing. Do you understand how insane that is? I'm standing on the stool checking whether I'm standing on the stool."

    s_thoughts "The postcard is on the wall. The Vermeer woman reading a letter."

    s_thoughts "Charlotte doesn't look at it."

    c "The mask was EASY. The mask was -- I knew what to do. Be warm. Be useful. Say 'of course.' Make sure the table looks right. I could DO that. I was GOOD at that."

    s "You were."

    c "And now I'm trying to -- what? Be different? Be real? And real is EXHAUSTING because real doesn't have a script. Real is just -- me. Standing in a kitchen. Not knowing if I want to make eggs."

    show charlotte sad at center

    s_thoughts "Charlotte puts her hands over her face."

    c "I'm so tired, Sophia."

    s_thoughts "I sit on the bed next to her."

    s_thoughts "She doesn't lean into me. She doesn't perform recovery."

    s_thoughts "She just sits."
    
    c "The porch... That night on the porch. Maybe... What if... What if it was a mistake?"
    
    s_thoughts "She's not looking at me. The question is rhetorical. At least I think so."
    
    s_thoughts "I don't respond."
    
    s_thoughts "She doesn't look at me for a while."

    c "Is it supposed to be this hard?"

    s "I don't know."

    c "Great. Love that. Very helpful."

    s "I know."

    s_thoughts "A beat."

    c "I think I'm going to go to bed early."

    s "Okay."

    c "Not because I'm avoiding you. Because I'm actually tired."

    s "I know."

    c "Do you?"

    s "Yeah."

    show charlotte neutral at center

    s_thoughts "She looks at me."

    c "Thank you for not making this a moment."

    s "You're welcome."

    s_thoughts "I stand up. I go to the door."

    s_thoughts "Charlotte is sitting on her bed. Tired. Small. Empty."

    s_thoughts "She looks... like a kid."

    s_thoughts "Trying to rebuild herself while still living inside the construction site."

    c "Sophia?"

    s "Yeah?"

    c "...Goodnight."

    s "Goodnight."

    s_thoughts "I close the door."

    s_thoughts "Charlotte is trying. Really trying."

    s_thoughts "And the trying is killing her."

    s_thoughts "The mask is always right there."

    stop music fadeout 3.0

    ## ===========================
    ## END OF ACT 1
    ## Charlotte is exhausted from self-monitoring.
    ## The relapse in Act 2 will feel like relief.
    ## The mask is comfortable. When Sophie calls,
    ## Charlotte gets to stop fighting herself.
    ## ===========================

    jump charlotte_ch5_act2

    ## ===========================
    ## ===========================
    ## ACT 2: "THE BREAKING"
    ## The shortest act. The hardest hitting.
    ## Charlotte's old patterns reassert under pressure.
    ## The mask snaps back on and it feels like RELIEF.
    ## ===========================
    ## ===========================

    ## ===========================
    ## SCENE 16: THE TRIGGER
    ## Sophie calls. Mom having a bad week.
    ## Charlotte's mask snaps on IMMEDIATELY.
    ## She looks RELIEVED. That's worse than horror.
    ## ===========================

label charlotte_ch5_act2:

    scene bg charlottebedroom with Fade(1.5, 0.5, 1.5)

    s_thoughts "Monday."

    s_thoughts "I'm in Charlotte's doorway. She said come in. I'm leaning on the frame."

    s_thoughts "She's on her phone. Not scrolling. Listening."

    show charlotte neutral at center with dissolve

    s_thoughts "Her face is still. She's nodding even though the person on the other end can't see her."

    c "Mm-hmm. Yeah. No, I know."

    s_thoughts "Sophie."

    c "How long has she been -- okay. Okay, and she's taking the -- yeah."

    s_thoughts "Charlotte's hand is flat on the desk. Not gripping. Just flat. Like she's checking if the desk is still there."

    c "Sophie. Soph. Hey. It's fine."

    s_thoughts "Her voice changes."

    s_thoughts "Not the crack. Not the wobble."

    s_thoughts "The opposite."

    c "It's not a crisis. The medication adjustment takes time. She's been through this before. Remember the one in -- yeah. And she was fine. She was FINE."

    s_thoughts "Charlotte's shoulders square."

    c "Okay here's what you're going to do. Are you listening? Don't cry. I need you to listen."

    s_thoughts "Her voice is bright."

    s_thoughts "Bright like a fluorescent. Not warm-bright. Clinical-bright. Every syllable is precise and steady and shaped like someone who has done this a hundred times."

    c "Call Dr. Adler. She needs to know about the dosage. Then check the fridge -- if Mom hasn't been eating, there's freezer meals in the bottom drawer. The ones in the green containers. Label says Tuesday and Thursday but ignore that, they're interchangeable."

    s_thoughts "She's not looking at me."

    c "And DON'T let her skip the walk. Even if she says she's tired. Especially if she says she's tired. Twenty minutes. Around the block. You go with her."

    s_thoughts "Charlotte is standing up."

    s_thoughts "She was sitting on the bed. Now she's standing. When did she stand up?"

    play music mus_charlotte fadein 2.0

    c "I can come home this weekend. I'll take the Friday bus. I can be there by--"

    c "Sophie. Sophie, LISTEN. It's going to be fine. I've got this."

    s_thoughts "She's got this."

    s_thoughts "She's got her shoulders back and her voice is steady and her free hand is already smoothing the bedsheet and she's got this."

    s_thoughts "She's got this the way she's always got it. The way her whole life she's 'got it.'"

    c "Okay. Okay, love you. Call me tonight. I mean it."

    s_thoughts "She hangs up."

    show charlotte happy at center

    s_thoughts "She turns to me."

    s_thoughts "She smiles."

    c "Sorry about that! Sophie worries. You know how she is."

    s "Is everything okay?"

    c "Oh, yeah! Mom's adjusting a medication. She's been a little low. It happens. Sophie just panics sometimes because she wasn't -- she didn't grow up with the bad years, so every dip feels like--"

    s_thoughts "She catches herself."

    c "It's not a crisis. It's really not. It's just a bad week."

    s "Charlotte."

    c "I might go home this weekend. Just to check in. I can take the Friday bus and be back Sunday night. I'll meal prep before I go so nobody has to worry about dinner."

    s "Charlotte."

    show charlotte smile at center

    c "I should call Dr. Adler's office actually. Sophie never remembers to leave the right callback number. And I should check if the pharmacy--"

    s "Charlotte."

    c "What?"

    s_thoughts "She looks at me."

    s_thoughts "She's smiling."

    s_thoughts "The old one."

    s_thoughts "Full wattage. Full coverage. Every corner lit."

    s_thoughts "She looks relieved."

    s_thoughts "That's the thing. She doesn't look scared. She doesn't look sad."

    s_thoughts "She looks like someone who just exhaled for the first time in three weeks."

    s_thoughts "The mask is on and Charlotte is breathing again."

    s "You said it's not a crisis."

    c "It's not!"

    s "Then why are you meal-prepping for a house of adults?"

    show charlotte happy at center

    c "Because I like cooking? I'm allowed to like cooking."

    s_thoughts "She's allowed to like cooking."

    s_thoughts "She does like cooking."

    s_thoughts "She also likes it more when she's needed."

    s "Okay."

    c "Okay!"

    s_thoughts "Charlotte picks up her phone again. Starts typing. She's already making a list."

    s_thoughts "I can see it from the door. Bullet points. Color-coded."

    s_thoughts "The Charlotte I've been building with for weeks just walked out of the room and the Charlotte who was here before walked back in."

    s_thoughts "And she looks so relieved I could cry."

    hide charlotte with dissolve

    ## ===========================
    ## SCENE 17: THE MORNING AFTER THE CALL
    ## Charlotte made eggs. For everyone. At 6:45 AM.
    ## The chore chart is back.
    ## Sophia's stomach drops.
    ## ===========================

    stop music fadeout 2.0

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Tuesday. 6:50 AM."

    s_thoughts "I'm awake because something woke me up."

    s_thoughts "The smell."

    s_thoughts "Eggs. Butter. Rosemary."

    show charlotte happy at center with dissolve

    s_thoughts "Charlotte is at the stove. Apron. Humming. The good knife is out. There are julienned vegetables on the cutting board."

    s_thoughts "The table is set for five."

    s_thoughts "Five forks. Five napkins. The little vase of flowers is back."

    s_thoughts "The chore chart is on the fridge."

    s_thoughts "It's new. Color-coded. Laminated."

    s_thoughts "She laminated a chore chart between midnight and 6:45 AM."

    c "Morning! Sit down. I made omelets. The fold kind."

    s_thoughts "My stomach drops."

    s_thoughts "Not because of the eggs. The eggs are beautiful. The fold is perfect."

    s_thoughts "Because the house smells like the day I moved in."

    c "I used the gruyère! We were running low so I went to the store this morning. I also got milk because I noticed we were out. And dish soap. And I picked up some of those cookies Amara likes? The ones with the -- the almond ones."

    s "Charlotte, it's not even seven."

    c "Early bird! Worm!"

    s_thoughts "She plates the omelet. Garnish. Little sprig of something green."

    s_thoughts "The bathroom smells like bleach. I noticed on the way down."

    s_thoughts "She cleaned the bathroom."

    c "Oh, I also reorganized under the sink. The cleaning supplies were a DISASTER. Who puts the sponges with the garbage bags?"

    s "When did you sleep?"

    show charlotte smile at center

    c "I slept! I slept fine. I just woke up early."

    s_thoughts "She didn't sleep."

    s_thoughts "Charlotte is standing in the kitchen at 6:50 AM too busy being Charlotte to worry about anything else."

    s_thoughts "And the worst part is she's HAPPY."

    c "Eat! Before it gets cold."

    s_thoughts "I sit down."

    s_thoughts "I eat the omelet."

    s_thoughts "It's perfect."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 18: CHARLOTTE OVERCORRECTS
    ## The "of course" gets louder.
    ## The postcard. She walks past it without looking.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_charlotte fadein 1.5

    s_thoughts "Wednesday."

    s_thoughts "Charlotte is doing the dishes. Isabella's dishes. Isabella is standing right there."

    show isabella neutral at left with dissolve
    show charlotte happy at right with dissolve

    i "Charlotte, I can do my own--"

    c "It's fine! I'm already here."

    i "I literally just put them down."

    c "Of course! But I'm doing a load anyway so it makes sense."

    hide isabella with dissolve
    scene bg kitchen with dissolve

    s_thoughts "Thursday."

    s_thoughts "Charlotte has reorganized the fridge. Everything is in containers. The containers have labels."

    c "I noticed Eve's leftovers were getting pushed to the back. So I moved them forward. And dated everything."

    s "You dated the fridge."

    c "I dated the CONTENTS of the fridge. The fridge itself is timeless."

    s_thoughts "She laughs at her own joke."

    s_thoughts "The laugh is right. The timing is right."

    s_thoughts "Everything is right."

    hide charlotte with dissolve

    scene bg charlottebedroom with dissolve

    s_thoughts "Friday."

    s_thoughts "I walk past Charlotte's room to get my charger."

    s_thoughts "The postcard is on the wall. The Vermeer woman reading a letter."

    s_thoughts "Charlotte's laptop is open. The Vermeer paper tab is visible."

    s_thoughts "Charlotte walks past both on her way to the bathroom with a bucket and a sponge."

    s_thoughts "She doesn't look at either one."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 19: SOPHIA TRIES TO TALK ABOUT IT
    ## Charlotte deflects with practiced ease.
    ## THE BIG NEGATIVES CHOICE.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Friday evening."

    s_thoughts "Charlotte is on the couch. She's folding laundry. Everyone's laundry."

    show charlotte smile at center with dissolve

    s_thoughts "She's folding Amara's sweater with hospital corners."

    s_thoughts "I don't think sweaters have corners."

    s "Hey."

    c "Hi! I'm almost done with this. Then I was going to start on the--"

    s "Can we talk?"

    show charlotte happy at center

    c "Of course! What's up?"

    s "About this week."

    c "What about it?"

    s "Charlotte."

    c "What?"
    
    play music mus_glass fadein 2.0

    s_thoughts "She's looking at me. Open face. Bright eyes. The 'whatever you need' expression."

    s "Since Sophie called. You've been--"

    c "Oh. That. I told you, it's not a crisis. Sophie just worries. You know how younger sisters are."

    s "I'm not asking about Sophie."

    show charlotte smile at center

    c "I'm FINE. I'm just -- I like being busy. I like taking care of things. Is that a crime?"

    s "Nobody said it was a crime."

    c "You're using the voice."

    s_thoughts "The careful voice."

    s "I'm not--"

    c "You ARE. You're doing the thing where you're about to say something for my own good and I can feel it assembling behind your face."

    s_thoughts "She's right."

    s_thoughts "She's also deflecting so smoothly I almost didn't notice."

    c "Sophie needed help. I helped. That's what sisters do. And while I was up I figured I might as well -- the house was getting a little--"

    s "Charlotte."

    c "WHAT?"

    s_thoughts "The brightness flickers."

    s_thoughts "Half a second."

    show charlotte smile at center

    c "Sorry. Sorry, I didn't mean to -- I'm fine. Really."

    menu:
        "Charlotte is deflecting."

        "\"Charlotte, you're doing the thing again.\"":
            $ charlotte_push += 1

            s "Charlotte. You're doing the thing again."

            show charlotte neutral at center

            s_thoughts "She flinches."

            s_thoughts "The kind that goes through the whole body."

            s_thoughts "Because she knows."

            c "I know."

            s "You--"

            c "I KNOW. I know I'm doing it. You think I don't KNOW?"

            s_thoughts "Her hands stop folding."

            c "I'm doing the thing again. You say that like I don't know. Like you've just had the breakthrough of a century."

            s_thoughts "She picks up another sweater. Folds it."

            show charlotte sad at center
            
            c "You know what the worst part is?"
            
            s "What?"

            c "It feels so GOOD. Not making eggs for a week felt like holding my breath. And then Sophie called and I could just -- exhale."

            s "I know."

            c "So don't tell me I'm doing the thing. I know I'm doing the thing. I just can't -- right now -- I can't--"

            s_thoughts "She folds the sweater with perfect edges."

            show charlotte smile at center

            c "I'm going to finish this laundry. And then I'm going to make dinner. And it's going to be fine."

            s_thoughts "She's smiling."

            s_thoughts "I can see the kid on the stool."

            s_thoughts "I can see her and I can't reach her."

            jump charlotte_ch5_scene20

        "Hold her. Say nothing.":
            $ charlotte_present += 1

            s_thoughts "I sit down next to her on the couch."

            s_thoughts "I take the sweater out of her hands. Put it on the coffee table."

            s_thoughts "I put my arms around her."

            show charlotte surprised at center

            s_thoughts "Charlotte goes rigid."

            s_thoughts "One second. Two."

            show charlotte smile at center

            s_thoughts "She melts."

            s_thoughts "No. She performs melting."

            c "I'm okay. I'm really okay."

            s_thoughts "She says it into my shoulder."

            c "It's just been a weird week. Sophie called and I got a little -- but I'm handling it. I'm handling it."

            s_thoughts "She's always handling it."

            s_thoughts "I can feel it. The muscles in her shoulders arranging into 'comforted.' The breathing evening into 'reassured.'"

            s_thoughts "She pats my back."

            s_thoughts "Charlotte pats MY back."

            s_thoughts "I'm holding her and she's comforting ME."

            c "Thank you. I needed that."

            s_thoughts "She pulls back. Picks up the sweater. Starts folding again."

            show charlotte happy at center

            c "Okay! Where was I?"

            s_thoughts "She was in my arms."

            s_thoughts "She left without leaving."

            jump charlotte_ch5_scene20

        "\"What do you need me to do?\"":
            $ charlotte_push -= 2
            $ charlotte_present -= 2

            s "What do you need me to do?"

            show charlotte happy at center

            s_thoughts "Charlotte's face lights up."

            s_thoughts "Not the flinch. Not the wobble."

            s_thoughts "She LIGHTS UP."

            c "Oh! You don't have to do anything. Really. But if you wanted to -- the pantry could probably use a once-over? And someone should check if we need more dish soap."

            s "I meant for you. What do you need me to do for YOU."

            c "That IS for me! A clean pantry is -- I mean, it helps everyone."

            s_thoughts "She didn't hear me."

            s_thoughts "No. She heard me perfectly."

            c "Oh, and if you could grab the recycling on your way out? I keep forgetting and--"

            s "Yeah. I'll get the recycling."

            show charlotte smile at center

            c "Thank you! You're the best."

            s_thoughts "She goes back to folding."

            s_thoughts "I asked Charlotte what she needed and she gave me a chore list."

            jump charlotte_ch5_scene20

    ## ===========================
    ## SCENE 20: ISABELLA NOTICES
    ## Brief. "She's doing it again." "I know."
    ## Isabella speaking from experience.
    ## Cross-route thread: "when Charlotte was... when we were close"
    ## ===========================

label charlotte_ch5_scene20:

    hide charlotte with dissolve
    stop music fadeout 1.5

    scene bg hallway with dissolve
    play music mus_2am fadein 2.0

    s_thoughts "Saturday. Charlotte caught the bus after dinner last night."

    s_thoughts "I'm in the hallway. Isabella catches my arm."

    show isabella neutral at center with dissolve

    i "Hey."

    s "Hey."

    i "She's doing it again."

    s_thoughts "No preamble."

    s "I know."

    i "What happened?"

    s "Sophie called. Her mom's adjusting a medication."

    show isabella sad at center

    i "Ah."

    s_thoughts "Isabella leans against the wall. She's got her phone in one hand. The screen is angled away from me."

    i "When Charlotte was -- when we were close--"

    s_thoughts "A pause."

    s_thoughts "It does all the work."

    show isabella neutral at center

    i "She'd do this. Something would happen. And the old Charlotte would just -- click into place. Like a program booting up."

    s "How long does it last?"

    i "A week. Sometimes two. Then she'd come back. Gradually. Like waking up."

    s "What do I do?"

    i "Nothing."

    s "..."

    i "That's the worst part."

    s_thoughts "Isabella crosses her arms. Her phone is still in her hand. The screen lights up. She tilts it further away."

    i "You can't pull her out. If you try, she just performs harder. She'll perform recovery if she thinks you need to see it."

    s "She already did that."

    show isabella sad at center

    i "Yeah."

    s_thoughts "Isabella is quiet for a second."

    i "She'll come back. She always comes back."

    s "What if she doesn't?"

    show isabella neutral at center

    i "Then you sit with that."

    s_thoughts "Isabella's eyes are doing something. Not the almost-perfect smile. Something older. Something that knows this kitchen and these patterns from before I was here."

    i "I should go. I've got a -- thing."

    s "Izzy."

    show isabella smile at center

    i "I'm fine! Go take care of your girlfriend."

    s_thoughts "The smile."

    s_thoughts "It's perfect."

    s_thoughts "Almost."

    hide isabella with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 20.5: THE VERMEER PAPER BEAT
    ## Brief. The paper is untouched.
    ## Charlotte stopped writing when the mask went back on.
    ## ===========================

    stop music fadeout 2.0

    scene bg charlottebedroom with dissolve

    s_thoughts "I pass Charlotte's room on Sunday."

    s_thoughts "The door is open. It's always open now."

    s_thoughts "The Vermeer paper is on the desk. The laptop is closed."

    s_thoughts "Last week she was talking about maps and nesting cages and the light always coming from the left."

    s_thoughts "The postcard is still on the wall. The woman reading a letter."

    s_thoughts "Charlotte hasn't written a word since Sophie called."

    s_thoughts "When the mask went back on, the paper stopped."

    s_thoughts "The paper is Charlotte writing about herself. She can't do both."

    ## ===========================
    ## SCENE 21: EVE ANNOUNCES SHE'S LOOKING ELSEWHERE
    ## Not dramatic. Practical. The "of course" is SO wrong
    ## that even Amara looks up.
    ## CHOICE — every option costs.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Monday morning. Breakfast."

    s_thoughts "Charlotte made pancakes. Nobody asked for pancakes."

    show charlotte happy at left with dissolve
    show eve neutral at right with dissolve

    s_thoughts "Eve is at the table. She's holding her mug. She hasn't touched the pancakes."

    s_thoughts "She puts the mug down."

    e "Charlotte."

    c "Mm?"

    e "I've been looking at other rooms."

    play music mus_glass fadein 2.0

    s_thoughts "The kitchen doesn't stop. Charlotte keeps flipping a pancake."

    c "Oh?"

    e "There's a place on Elm. Single room. Quiet."

    s_thoughts "Charlotte turns around."

    show charlotte smile at left

    c "Of course! Whatever you need."

    s_thoughts "The 'of course' lands like a gunshot."
    
    s_thoughts "Did she even hear Eve? What Eve just said? I'm making a face. Eve sees me make a face."

    c "If that's what's right for you, then -- absolutely! I think that's really mature, actually."

    show eve annoyed at right

    e "Charlotte--"

    c "No, it's GREAT. You should do what's best for you. I mean that. I totally mean that."

    s_thoughts "Even Amara looks up."

    s_thoughts "I can't see her but I hear the book close."

    e "I wasn't asking for permission."

    c "Of course not! I'm just saying -- I support you."

    s_thoughts "Eve looks at Charlotte."

    s_thoughts "Charlotte looks at Eve."

    s_thoughts "The smile doesn't move."

    show eve neutral at right

    s_thoughts "Eve stands up. She leaves the kitchen."

    hide eve with dissolve

    s_thoughts "Charlotte picks up Eve's plate. Eve's untouched pancakes."

    s_thoughts "She washes the plate."

    s_thoughts "The plate was already clean."

    show charlotte smile at left

    menu:
        "Eve just walked out. Charlotte is washing a clean plate."

        "Follow Eve.":
            $ charlotte_eve += 1
            $ charlotte_push += 1

            s_thoughts "I follow Eve."

            hide charlotte with dissolve

            scene bg entry with dissolve

            show eve neutral at center with dissolve

            s "Eve."

            s_thoughts "She's already halfway to the stairs."

            e "Don't."

            s "I'm not going to try to talk you out of it."

            show eve annoyed at center

            s_thoughts "She stops."

            s_thoughts "Turns."

            e "Then what?"

            s "Are you okay?"

            e "I'm fine."

            s "That's Charlotte's line."

            show eve surprised at center

            s_thoughts "Something crosses her face."

            show eve neutral at center

            e "The house is hers. Everything in it is arranged the way she needs it. I'm just a thing that won't go where she puts me."

            s "That's not--"

            e "It is. It IS that. She doesn't mean it to be. I know she doesn't mean it. But I can't live inside someone else's system."

            s_thoughts "Eve is quiet."

            e "She's a good person."

            s "I know."

            e "Tell her I said that. When she can hear it."

            s_thoughts "Eve goes upstairs."

            hide eve with dissolve

            s_thoughts "I sit at the bottom of the stairs between Eve's closed door and the kitchen where Charlotte is washing clean dishes."

            jump charlotte_ch5_scene22

        "Stay with Charlotte.":
            $ charlotte_present += 1
            $ charlotte_eve -= 1

            s_thoughts "I stay."

            s_thoughts "Eve's footsteps go up the stairs."

            s_thoughts "Charlotte washes the plate."

            s "Charlotte."

            c "Hm?"

            s "Put the plate down."

            show charlotte surprised at left

            s_thoughts "She puts the plate down."

            s_thoughts "She picks up a glass."

            s "Charlotte."

            c "I'm just finishing the--"

            s "The glass is clean."

            show charlotte smile at left

            c "...Is it?"

            s "You know it is."

            s_thoughts "Charlotte looks at the glass."

            show charlotte neutral at left

            s_thoughts "She puts it down."

            c "I'm fine."

            s "I know."

            c "She should do what's best for her."

            s "I know."

            c "I MEAN that."

            s "I know you do."

            s_thoughts "Charlotte stands at the sink."

            s_thoughts "Her hands are wet. She's not drying them."

            s_thoughts "I'm here. Eve isn't."

            s_thoughts "That's a side."

            hide charlotte with dissolve

            jump charlotte_ch5_scene22

        "Pretend nothing happened.":
            $ charlotte_present -= 2
            $ charlotte_eve -= 1

            s_thoughts "I pick up my fork."

            s_thoughts "I eat a pancake."

            s "These are really good."

            show charlotte happy at left

            c "Oh! Thank you! I tried a new recipe. Buttermilk."

            s "You can taste the buttermilk."

            c "Right? It makes such a difference."

            s_thoughts "We talk about pancakes."

            s_thoughts "Eve is upstairs looking at listings for a room on Elm Street. Charlotte is telling me about the chemical properties of buttermilk."

            s_thoughts "I'm eating pancakes because I'm a coward."

            hide charlotte with dissolve

            jump charlotte_ch5_scene22

    ## ===========================
    ## SCENE 22: THE SLOW UNRAVELING
    ## NOT a montage. Individual beats.
    ## Charlotte organizing. Charlotte ironing. Charlotte laughing.
    ## The laugh is its own scene and the most unsettling.
    ## ===========================

    ## --- Beat 1: The Pantry at Midnight ---
    
label charlotte_ch5_scene22:
    stop music fadeout 2.0
    scene black with Fade(0.8, 0.3, 0.8)

    s_thoughts "Saturday. 11:47 PM."

    s_thoughts "I get up to get water."

    scene bg kitchen with dissolve

    show charlotte smile at center with dissolve

    play music mus_2am fadein 2.0

    s_thoughts "Charlotte is in the pantry."

    s_thoughts "She has every can out. They're on the counter in rows. She's wiping down the shelves."

    s "Charlotte?"

    c "Hey! Sorry, did I wake you? I just noticed the pantry was getting a little -- you know."

    s "It's almost midnight."

    c "I know! I was going to bed and then I saw the cans and they were all -- the labels were facing different directions."

    s_thoughts "The labels."

    s_thoughts "Charlotte is organizing canned goods by label direction at midnight."

    c "Go back to bed. I'm almost done."

    s "Charlotte."

    c "Five more minutes. I promise."

    s_thoughts "I go back to bed."

    s_thoughts "I hear the cans for another hour."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## --- Beat 2: The Napkins ---

    scene bg laundry with dissolve

    s_thoughts "Sunday. I'm doing laundry."

    show charlotte happy at center with dissolve

    s_thoughts "Charlotte is at the ironing board."

    s_thoughts "She is ironing napkins."

    s_thoughts "We don't own nice napkins. These are paper towels."

    s_thoughts "Charlotte is ironing paper towels."

    c "They fold better if you press them first."

    s_thoughts "They do not."

    s_thoughts "Nobody has ever ironed a paper towel. Nobody in the history of the species has thought 'you know what this disposable paper product needs? A crease.'"

    s_thoughts "Charlotte is pressing them with care."

    hide charlotte with dissolve

    ## --- Beat 3: The Laugh ---

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Monday."

    s_thoughts "I'm at the kitchen table."

    show charlotte smile at center with dissolve

    s_thoughts "Charlotte is putting away groceries. She bought groceries. Again."

    s_thoughts "She's talking about something. I'm half-listening. A story about the cashier."

    c "And she said 'oh, you must be cooking for a big family!' and I said 'just a house of five!' and she said--"

    s_thoughts "Charlotte stops."

    s_thoughts "She laughs."

    s_thoughts "She laughs like it's funny."

    show charlotte laugh at center

    s_thoughts "It's not funny."

    s_thoughts "The cashier story isn't even a story. It's just a cashier saying something about groceries."

    s_thoughts "Charlotte laughed because that's where the laugh goes."
    
    s_thoughts "The script reads 'Charlotte laughs' and she laughs right where it says."
    
    s_thoughts "That's the version of the story Charlotte is telling."

    show charlotte smile at center

    s_thoughts "She looks at me."

    s_thoughts "Waiting."

    s_thoughts "I'm supposed to laugh too."

    s "Ha."

    s_thoughts "I don't laugh."

    s_thoughts "I say 'ha' like it's a word and Charlotte hears it and her smile holds and she goes back to putting away groceries."

    s_thoughts "That's the worst one."

    s_thoughts "The cans. The napkins. The omelets."

    s_thoughts "The laugh."

    s_thoughts "The laugh at nothing."

    hide charlotte with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 23: THE BREAKDOWN + THE REFUSAL
    ## One scene, three phases.
    ## The mask goes blank.
    ## "I can't remember what I was making."
    ## "If you fix this for me, it's just the same thing."
    ## CHOICE: stay or leave.
    ## ===========================

    scene bg kitchen night with Fade(1.5, 0.5, 1.5)

    s_thoughts "Tuesday. Late."

    s_thoughts "The kitchen light is on."

    s_thoughts "I come downstairs because the kitchen light is on and it shouldn't be."

    ## Phase 1: The Mask Goes Blank.

    show charlotte pj neutral at center with dissolve

    s_thoughts "Charlotte is standing at the counter."

    s_thoughts "She has a spatula."

    s_thoughts "She's not moving."

    s_thoughts "Not frozen. Not crying. Not performing. Just... standing."

    s_thoughts "The stove is on. There's a pan. Something was in the pan. It's burned now."

    s_thoughts "Charlotte is looking at the spatula like she's never seen one before."

    s_thoughts "Her mouth opens."

    c "I was making..."

    s_thoughts "She stops."

    c "I was making something for..."

    s_thoughts "She stops."

    s_thoughts "She can't finish the sentence."

    s_thoughts "She can't remember what she was making or who she was making it for."

    s_thoughts "She can't remember if someone asked or if she just started because starting is what she does."

    s_thoughts "The mask doesn't crack."

    s_thoughts "It goes blank."

    s_thoughts "What's underneath isn't the ten-year-old. It isn't the porch confession. It isn't the extra places or the stool."

    s_thoughts "It's nothing."

    s_thoughts "She's nothing."

    ## Phase 2: Sophia Enters.

    s_thoughts "..."
    
    s_thoughts "She sees me."

    play music mus_charlotte_sad fadein 3.0

    c "I can't remember what I was making."

    s "That's okay."

    c "No."

    s_thoughts "She says it quiet."

    c "It's not."

    c "Because I can't remember if I wanted to make it or if I just -- if I'm just--"

    s_thoughts "She looks at the spatula."

    c "I don't know what I'm doing here."

    c "I set my alarm for midnight. Did you know that? I set my alarm because I was going to make -- something. For tomorrow. For the morning. And I came downstairs and I turned on the stove and I got the pan and I--"

    c "I don't know what I was going to make."

    c "I don't know if it was eggs or pancakes or -- I don't know who it was for. Was it for Eve? Because she said she's leaving and maybe if I--"

    s_thoughts "She looks at me."

    c "Was it for you?"

    s "Charlotte--"

    c "Was I making this for you? Because you like the fold omelets? Or was I making it because that's what I DO and I can't--"

    s_thoughts "Her voice cracks."

    s_thoughts "Not the mask cracking. Her."

    c "I can't tell the difference."

    c "I've never been able to tell the difference."

    ## Phase 3: Charlotte Refuses Help.

    s_thoughts "I reach for her."

    s_thoughts "Charlotte steps back."

    s_thoughts "Not angry. Not scared."

    s_thoughts "Clear."

    c "Don't."

    s "..."

    c "If you fix this for me, it's just -- it's the same thing."

    s "I'm not trying to fix--"

    c "You ARE. You're going to hold me and say something kind and I'm going to feel better and then tomorrow I'm going to make omelets again because that's what happens."
    
    c "I let someone take care of me and I am taken care of perfectly because I do everything you're supposed to do when you're taken care of and I do it perfectly."
    
    c "I do it because that's what I'm supposed to do."
    
    c "I do it because that's what Charlotte DOES."
    
    c "I do it because I don't know who Charlotte IS."

    s_thoughts "She puts the spatula down."

    c "I don't know anything about that girl."
    
    c "I look at her every morning in the mirror and I don't recognize her."
    
    s "..."
    
    c "I don't recognize her, Sophia."
    
    c "I stare at her every day and she's like a stranger to me."
    
    c "There are five people in this house and only one of them is a stranger."
    
    s_thoughts "I study her closely, quietly."

    s_thoughts "She's not crying."

    c "I don't know what I like. I don't know what I WANT."

    c "I just... know what everyone else wants."
    
    c "I know their things."
    
    s_thoughts "Her voice gets meek. Like she's afraid to say it."

    c "...I don't have a thing."
    
    s "..."

    c "The postcard."

    s "The postcard?"

    c "I put it up because you thought I should have something that's mine."

    s_thoughts "I don't remember telling her that."
    
    c "I looked at it every day and I thought 'is this mine? Do I like this? Or do I like it because Sophia wants me to like something?'"
    
    c "Do I like it because Sophia didn't like that my bedroom was empty and I wanted Sophia to like my bedroom?"

    s_thoughts "The kitchen is very quiet."

    s_thoughts "The burned pan is smoking slightly."

    c "I can't -- you can't fix this for me. Do you understand?"

    s "Yes."

    c "Because if you fix it, I'll let you."

    c "I'll let you fix Charlotte. I'll be the most perfect Charlotte you need me to be."
    
    s_thoughts "I think of Isabella. For some reason I wonder what she's talking to Lumi about."
    
    c "And then it's just -- it's the same. The same damn thing every damn time."

    c "Someone else figures out who Charlotte is so I don't have to figure out who I am without the spatula."

    s_thoughts "She said 'the spatula' like it means everything."

    s_thoughts "It does."

    stop music fadeout 2.0

    menu:
        "Stay in the kitchen.":
            $ charlotte_present += 1

            s_thoughts "I don't reach for her."

            s_thoughts "I don't fix anything."

            s_thoughts "I turn off the stove."

            s "The pan is burning."

            s_thoughts "Charlotte looks at the stove."

            c "...Oh."

            s_thoughts "I move the pan off the burner."

            s_thoughts "I sit down at the table."

            s_thoughts "Charlotte is standing. I'm sitting."

            s_thoughts "The kitchen is quiet."

            s "I'm not going to fix anything. I'm just going to be in the kitchen."

            show charlotte pj vulnerable at center

            c "..."

            s "Because it's a kitchen. And I'm allowed to be in a kitchen at midnight."

            c "That's a stupid reason."

            s "It's the only one I've got."

            s_thoughts "Charlotte looks at me."

            s_thoughts "She doesn't sit down."

            s_thoughts "But she doesn't leave."

            s_thoughts "We stay in the kitchen."

            s_thoughts "Not fixing anything."

            s_thoughts "Charlotte puts the spatula in the sink."

            s_thoughts "That's all."

            jump charlotte_ch5_scene25

        "Leave. Give her space.":
            $ charlotte_push -= 1
            $ charlotte_present -= 1

            s "Okay."

            s_thoughts "I stand up."

            s "I'll be upstairs."

            show charlotte pj vulnerable at center

            s_thoughts "Charlotte watches me go."

            s_thoughts "She didn't ask me to leave."

            s_thoughts "She asked me not to fix it."
            
            s_thoughts "So I left."

            s_thoughts "I'm on the stairs when I hear the water run."

            s_thoughts "Charlotte washing the burned pan."

            s_thoughts "Alone."

            jump charlotte_ch5_scene25

    ## ===========================
    ## SCENE 25: THE HOUSE HOLDS (CONDITIONAL on Scene 21 choice)
    ## The house without Charlotte's performance.
    ## Charlotte sees the house functioning from the hallway.
    ## It should be a relief. It's terrifying.
    ## ===========================

label charlotte_ch5_scene25:

    hide charlotte with dissolve
    stop music fadeout 2.0

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_shift fadein 2.0

    s_thoughts "It's been about a week since our conversation."

    s_thoughts "We haven't talked much since then. Mostly just hanging out quietly when we do."
    
    s_thoughts "I'm okay with that."

    s_thoughts "Dishes in the sink. Several days' worth."

    s_thoughts "Nobody made eggs."

    s_thoughts "The chore chart is still on the fridge. Nobody is following it."

    show amara neutral at right with dissolve

    s_thoughts "Amara puts rice in the rice cooker. She doesn't announce it. She just does it."
    
    a "Dinner." 

    hide amara with dissolve

    show isabella smile at left with dissolve

    s_thoughts "Isabella orders pizza."

    i "I got half pepperoni, half cheese. If anyone wants pineapple they can order their own pizza and try to explain themselves when Judgment Day arrives. There will be no mercy from me."

    hide isabella with dissolve

    s_thoughts "I do the dishes."

    s_thoughts "Badly."

    s_thoughts "There's a glass that might be permanently stained."

    ## Conditional Eve beat
    if charlotte_eve > 0:
        s_thoughts "Eve comes downstairs."

        s_thoughts "She doesn't say anything. She opens the fridge. Takes out the milk. Puts it back."

        s_thoughts "Then she picks up a sponge and wipes the counter."

        s_thoughts "She's still here."

        s_thoughts "The house adjusts."
        
    elif charlotte_eve == 0:
        scene bg hallway with dissolve
        
        s_thoughts "I knock on Eve's door to bring her some pizza."
        
        s_thoughts "At first she doesn't reply."
        
        s_thoughts "As I start to walk away, she opens the door to grab it. I look back."
        
        s_thoughts "A quiet 'thank you' and the door closes."
        
    else:
        scene bg hallway with dissolve
        
        s_thoughts "Eve's door is closed."

        s_thoughts "It's been closed for two days."

        s_thoughts "Her presence is a question mark. The house adjusts around the shape of it."

    scene bg entry with dissolve

    s_thoughts "Charlotte is at the bottom of the stairs."

    s_thoughts "She's staring at the kitchen."

    s_thoughts "The house is functioning."

    s_thoughts "Not well. Not gracefully. The dishes are done wrong and the pizza is lukewarm and the rice is slightly too wet."

    s_thoughts "But the house is functioning."

    s_thoughts "Without her."

    s_thoughts "That should be a relief."
    
    s_thoughts "I'm not sure if it is."

    stop music fadeout 3.0

    ## ===========================
    ## END OF ACT 2
    ## Charlotte is raw.
    ## The mask went blank.
    ## The house held without her.
    ## Now: the slow rebuild.
    ## ===========================

    jump charlotte_ch5_act3

    ## ===========================
    ## ===========================
    ## ACT 3: "THE AFTERMATH"
    ## The slow rebuild.
    ## Charlotte is raw. Not performing, not "better."
    ## Just present in a way she's never been.
    ## Sophia has to learn that loving Charlotte
    ## doesn't mean fixing Charlotte.
    ## ===========================
    ## ===========================

    ## ===========================
    ## SCENE 26: CHARLOTTE'S ROOM — EXTENDED
    ## Charlotte is spending time in HER room.
    ## Not hiding — being.
    ## On the bed. Like it's hers.
    ## ===========================

label charlotte_ch5_act3:

    scene bg charlottebedroom with Fade(1.5, 0.5, 1.5)

    s_thoughts "Three days."

    s_thoughts "Charlotte has been in her room for three days."

    s_thoughts "Not hiding. Not spiraling. I checked -- not because I was monitoring, but because the silence scared me."

    s_thoughts "She's reading."

    s_thoughts "On the bed."

    s_thoughts "This matters because Charlotte doesn't use her bed like a bed. She uses it like a shelf. Her bed is where clean laundry goes to die. She studies at the desk. She eats in the kitchen. She sleeps on the bed, technically, in the six inches between folded towels."

    s_thoughts "But she's sitting on her bed. Legs crossed. Book in her lap. The towels are -- somewhere else."

    s_thoughts "I knock on the open door."

    show charlotte pj neutral at center with dissolve

    play music mus_morningafter fadein 3.0

    s "Hey."

    c "Hey."

    s "Whatcha reading?"

    c "Um."

    s_thoughts "She holds up the book."

    s_thoughts "It's a novel. Not an academic text. A novel."

    c "It's -- I found it in the living room. Someone left it."

    s "Amara's. She leaves books everywhere."

    c "It's about a woman who runs a bakery."

    s "Is it good?"

    c "It's... fine. She keeps describing bread in a way that makes me hungry."

    s "That's a compliment for a bakery book."

    s_thoughts "Charlotte almost smiles."

    s_thoughts "Not the full Charlotte smile. The kind where one corner of her mouth moves and the other one is still deciding."

    c "I've been reading for three hours."

    s "Yeah?"

    c "I haven't done that since -- I don't know. High school?"

    s_thoughts "She looks at the book like it's a weird thing she found in the road."

    c "I don't even know if I like it. The bread woman is kind of annoying. She keeps making sourdough for her ex-husband."

    s "Sounds familiar."

    show charlotte pj sad at center

    c "..."

    s "Sorry. That was--"

    c "No. That was funny."

    s_thoughts "A beat."

    c "The bread woman should stop making sourdough for her ex-husband."

    s "She really should."

    show charlotte pj neutral at center

    s_thoughts "Charlotte goes back to reading."

    s_thoughts "I lean on the doorframe."

    s_thoughts "The postcard is still on the wall. The Vermeer woman reading a letter."

    s_thoughts "There's a second one now. I can see it from here. It's smaller. A different painting -- I can't tell which. Something with blue."

    s_thoughts "Charlotte didn't mention it."

    s_thoughts "I don't either."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 27: A MORNING WITHOUT PERFORMING
    ## Nobody makes breakfast for anyone.
    ## Coffee. Cereal. Silence.
    ## Uncomfortable and okay.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Friday morning."

    s_thoughts "I come downstairs."

    s_thoughts "The kitchen smells like coffee and nothing else."

    s_thoughts "Charlotte is at the table. She has coffee. One mug. She's looking at her phone."

    show charlotte neutral at center with dissolve

    s_thoughts "The table has one mug on it. Just the one."

    s_thoughts "I open the cabinet. Get cereal. Get a bowl."

    s_thoughts "Charlotte doesn't look up."

    s_thoughts "I pour cereal. I pour milk. I sit down."

    s_thoughts "We're at the same table."

    s_thoughts "Nobody says anything."

    s_thoughts "The cereal is loud. Crunching in silence is an act of aggression."

    s_thoughts "I crunch."

    s_thoughts "Charlotte scrolls."

    s_thoughts "The fridge hums."

    s_thoughts "A full minute passes."

    s_thoughts "Charlotte puts her phone down."

    c "This is weird."

    s "Little bit."

    c "I keep wanting to offer you something."

    s "I have cereal."

    c "I KNOW you have cereal. I can hear the cereal. The cereal is deafening."

    s "It's Cheerios."

    c "Cheerios are the loudest cereal."

    s "That's factually incorrect. Grape-Nuts are the loudest cereal."

    show charlotte neutral at center

    c "..."

    s "..."

    s_thoughts "We sit."

    s_thoughts "Charlotte drinks her coffee. I eat my cereal."

    s_thoughts "Nobody fills the silence."

    s_thoughts "It's uncomfortable."

    s_thoughts "It's okay."

    s_thoughts "Charlotte finishes her coffee. She puts the mug in the sink. Not washed. Just in the sink."

    s_thoughts "Charlotte Opal put an unwashed mug in the sink."

    s_thoughts "I don't mention it."

    hide charlotte with dissolve

    ## ===========================
    ## SCENE 28: SOPHIA MESSES UP
    ## The careful voice. Charlotte catches it.
    ## Callback to Act 1: "I can FEEL you being careful."
    ## CHOICE 7.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_2am fadein 2.0

    s_thoughts "Saturday afternoon."

    s_thoughts "Charlotte is on the couch. She's staring at her laptop. The Vermeer paper is open again. She's been staring at the same paragraph for twenty minutes."

    show charlotte neutral at center with dissolve

    s_thoughts "I'm in the armchair. I'm pretending to read."

    s_thoughts "I'm watching her."

    s_thoughts "I know I'm watching her. I know I'm doing the thing."

    s_thoughts "I can't stop."

    s "How's the paper going?"

    c "Hm?"

    s "The Vermeer paper. How's it--"

    s_thoughts "I hear myself."

    s_thoughts "The voice."

    s_thoughts "The careful voice."

    s_thoughts "'How's the paper going' except every syllable is calibrated to sound casual and it's not casual at all. It's the voice of someone checking a wound."

    show charlotte annoyed at center

    c "You're doing it."

    s "Doing what?"

    c "The voice. The careful voice."

    s_thoughts "My chest does something unpleasantly architectural."

    c "You just asked me about the paper in the same voice you used to ask me about my day when I was--"

    s_thoughts "She doesn't finish. She doesn't have to."

    c "I can hear it, Sophia."

    menu:
        "She caught me."

        "\"You're right. I was checking on you.\"":
            $ charlotte_present += 1
            $ charlotte_push -= 1

            s "You're right."

            show charlotte surprised at center

            s "I was checking on you. I was watching you stare at the paper and I got scared and I used the voice."

            c "..."

            s "I'm sorry."

            s_thoughts "Charlotte looks at me."

            s_thoughts "Something tired. Resigned."

            show charlotte neutral at center

            c "Thank you."

            s "For what?"

            c "Not pretending you weren't."

            s_thoughts "She goes back to the laptop."

            s_thoughts "I go back to pretending to read."

            s_thoughts "The voice is still there. The impulse is still there."

            s_thoughts "But I named it. And Charlotte heard me name it."

            s_thoughts "It's not fixed. But it's named."

            jump charlotte_ch5_scene28_5

        "\"I wasn't -- I was just asking about the paper.\"":
            $ charlotte_push += 1
            $ charlotte_present -= 1

            s "I wasn't doing the voice. I was just asking about the paper."

            show charlotte annoyed at center

            c "Sophia."

            s "I'm allowed to ask about the paper."

            c "You're allowed to ask about the paper. You're not allowed to ask about the paper in the voice that means 'I'm worried you're about to stand in the kitchen with a spatula again.'"

            s_thoughts "That stings."

            s "That's not fair."

            c "Probably not."

            s_thoughts "She closes the laptop."

            show charlotte neutral at center

            c "I'm going to my room."

            s "Charlotte--"

            c "I'm not mad. I'm just -- I can't do the thing where we pretend you weren't checking."

            s_thoughts "She goes upstairs."

            s_thoughts "I sit in the living room."

            s_thoughts "She's right. I was checking."

            s_thoughts "I lied about it because the truth would have meant admitting I'm still doing the thing she asked me to stop."

            s_thoughts "Which is worse than doing the thing."

            jump charlotte_ch5_scene28_5

        "\"I don't have a careful voice.\"":
            $ charlotte_present -= 2
            $ charlotte_push -= 1

            s "I don't have a careful voice."

            show charlotte sad at center

            c "..."

            s "I was asking about your paper. That's it."

            c "Okay."

            s_thoughts "She says 'okay' the way she used to say 'of course.'"

            s_thoughts "Flat. Accepting. Done."

            show charlotte neutral at center

            c "The paper's fine."

            s "Good."

            s_thoughts "She goes back to staring at the paragraph."

            s_thoughts "I go back to pretending to read."

            s_thoughts "The room is quiet."

            s_thoughts "We both know I'm lying."

            s_thoughts "Charlotte just chose not to fight about it."

            s_thoughts "That's not the same as it being okay."

            jump charlotte_ch5_scene28_5

    ## ===========================
    ## SCENE 28.5: CHARLOTTE'S WOBBLE
    ## Recovery is not linear.
    ## "Of course!" in the OLD voice. They both freeze.
    ## Brief. No choice. Just the proof.
    ## ===========================

label charlotte_ch5_scene28_5:

    hide charlotte with dissolve
    stop music fadeout 1.5

    scene bg kitchen with Fade(0.8, 0.4, 0.8)

    s_thoughts "Sunday."

    s_thoughts "I'm in the kitchen. Charlotte is at the table with her laptop. Isabella comes in."

    show charlotte neutral at left with dissolve
    show isabella neutral at right with dissolve

    i "Hey Charlotte, can I borrow the big pan? The cast iron one?"

    show charlotte happy at left

    c "Of course!"

    s_thoughts "The room stops."

    s_thoughts "Not literally. Isabella is still standing there. The fridge is still humming. Somewhere outside a car goes by."

    s_thoughts "But Charlotte heard herself."

    show charlotte surprised at left

    s_thoughts "The brightness. The exclamation mark. The full-wattage, arms-open, whatever-you-need 'of course.'"

    s_thoughts "It came out like a reflex."

    s_thoughts "Because it is one."

    show isabella neutral at right

    i "...Thanks?"

    s_thoughts "Isabella takes the pan. She doesn't know what just happened. She leaves."

    hide isabella with dissolve

    s_thoughts "Charlotte is staring at the table."

    c "I didn't mean--"

    s "I know."

    c "It just came OUT. Like a -- like a--"

    s_thoughts "She can't finish."

    c "Like a reflex."

    show charlotte sad at left

    s_thoughts "Her hands are flat on the table."

    c "One breakdown doesn't kill a reflex. It just makes you hear it."

    s_thoughts "She said that like she's been thinking it for days."

    s_thoughts "She probably has."

    c "I heard it. The whole -- the brightness. The -- everything."

    s "Yeah."

    c "It sounded like my mom's kitchen."

    s_thoughts "I don't say anything."

    s_thoughts "Charlotte closes her laptop."

    s_thoughts "She sits with it."

    s_thoughts "The silence is awful. Not angry-awful. The awful of someone who knows the thing they're trying to stop is older than the trying."

    s_thoughts "Charlotte opens her laptop again."

    s_thoughts "She starts typing."

    s_thoughts "I don't know if it's the paper or an email or nothing."

    s_thoughts "I let her type."

    hide charlotte with dissolve

    ## ===========================
    ## SCENE 29: CHARLOTTE TRIES SOMETHING NEW
    ## Museum. Alone. For herself.
    ## "Is that weird?" "That's not weird."
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_shift fadein 2.0

    s_thoughts "Wednesday."

    s_thoughts "I'm on the couch when Charlotte comes home."

    s_thoughts "She's got her bag and her jacket and she's holding something -- a folded piece of paper."

    show charlotte embarrassed at center with dissolve

    s_thoughts "She stands in the living room doorway."

    s_thoughts "She's fidgeting."

    c "Hey."

    s "Hey."

    c "So I did a thing."

    s "What kind of thing?"

    c "I went to the art museum."

    s "Yeah?"

    c "By myself."

    s "..."

    c "Is that weird?"

    s "That's not weird."

    show charlotte neutral at center

    c "I just -- I was walking past it. On the way back from class. And I thought -- I've been writing about Vermeer for weeks and I've never just... looked at paintings. In person. Without it being for the paper."

    s "How was it?"

    c "Weird."

    s "Weird how?"

    c "Quiet. Like, really quiet. And nobody was -- there was nobody checking if I was okay. Nobody asking if I needed anything."

    s_thoughts "She sits down on the other end of the couch."

    show charlotte smile at center

    c "There was a painting. Not a Vermeer. Some other Dutch guy. A woman peeling apples."

    s "Okay."

    c "And she's just -- peeling apples. That's it. That's the whole painting. She's looking down at the apple and the peel is in this long spiral and she's alone and she's not doing it for anyone. She's just peeling an apple."

    s "Did you like it?"

    show charlotte surprised at center

    s_thoughts "Charlotte blinks."

    s_thoughts "Like the question caught her off guard."

    c "I..."

    c "Yeah. I liked it. I actually liked it."

    s_thoughts "She says 'I actually liked it' like she's confessing to a minor crime."

    show charlotte smile at center

    c "I stood there for like twenty minutes. A security guard asked if I was okay."

    s "Were you?"

    c "I think so? I was just -- looking. At a woman peeling an apple."

    s_thoughts "She unfolds the paper she's been holding."

    s_thoughts "It's a postcard from the museum gift shop."

    s_thoughts "The woman peeling the apple."

    c "I bought this."

    s "For your wall?"

    show charlotte embarrassed at center

    c "Is that -- I keep putting things on my wall and I don't know if I'm doing it because I want to or because--"

    s "Charlotte."

    c "What?"

    s "It's yours."

    show charlotte neutral at center

    s_thoughts "She looks at the postcard."

    c "The apple peel is really long. Like, unrealistically long. She'd have been peeling that apple for an hour."

    s "Maybe she wasn't in a rush."

    c "Yeah."

    s_thoughts "Charlotte holds the postcard carefully."

    s_thoughts "She goes upstairs."

    s_thoughts "I don't follow her."

    s_thoughts "Later I walk past her room. The door is open."

    s_thoughts "Three postcards on the wall now."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 30: CHARLOTTE'S PAPER FEEDBACK
    ## "You finally asked why they stay."
    ## Charlotte reads it to Sophia.
    ## The paper isn't about Vermeer anymore.
    ## ===========================

    scene bg charlottebedroom with Fade(0.8, 0.3, 0.8)
    play music mus_charlotte fadein 3.0

    s_thoughts "Thursday evening."

    s_thoughts "We're both sitting on Charlotte's bed, cuddling. It's nice."

    s_thoughts "She's been reading something for ten minutes. Not typing. Reading."

    show charlotte neutral at center with dissolve

    c "Sophia."

    s "Mm?"

    c "Can I read you something?"

    s "Yeah."

    c "Professor Morin emailed me. About the paper."

    s "Okay."

    s_thoughts "Charlotte takes a breath."

    s_thoughts "She reads."

    c "'Charlotte -- this draft is a significant departure from your previous work. The argument about the frame is tighter now, and the section on the maps has developed beautifully.'"

    s_thoughts "She pauses."

    c "'But the real shift is in Section 3. You finally asked why they stay. Not structurally -- emotionally. The Vermeer women aren't trapped by the room. They're trapped by the way the room became the whole world.'" 
    
    c "'You wrote that the cage isn't the frame -- it's the moment when the frame stops being visible.'"

    s_thoughts "Charlotte's voice is steady."

    c "'That's the paper I've been waiting for you to write.'"

    s_thoughts "She stops reading."

    s_thoughts "The laptop screen glows."

    s_thoughts "Charlotte is very quiet."

    s "Charlotte?"

    c "She says it's the paper she's been waiting for me to write."

    s "Yeah."

    show charlotte sad at center

    c "The cage isn't the frame. It's the moment when the frame stops being visible."

    s_thoughts "She's not looking at me."

    c "I wrote that."

    s "You did."

    c "About Vermeer."

    s "...Yeah."

    show charlotte neutral at center

    s_thoughts "She closes the laptop."

    s_thoughts "Slowly."

    c "It's not about Vermeer."

    s_thoughts "I don't say anything."

    c "I mean, it IS. Technically. Academically. The argument works for the paintings."

    s "But."

    c "But I wrote 'the cage becomes invisible because the woman has decided the room is enough' and I wasn't thinking about the painting."

    s_thoughts "Her room is quiet. She presses her head against my shoulder and kisses my neck softly."

    c "...I was thinking about the kitchen."

    s_thoughts "She looks up at me."

    show charlotte smile at center

    s_thoughts "She smiles. It's tired and lopsided and gorgeous. I don't tell her that. She's only just started to wear it more lately."

    c "Morin is going to love the final revision."

    s "She already does."

    c "She loves the paper."

    s "She loves what you found."

    show charlotte embarrassed at center

    c "..."

    c "Is it weird that I feel proud? Like, actually proud?"

    s "It's not weird."

    c "Huh."
    
    show charlotte smile at center

    s_thoughts "She opens the laptop again. Reads the email again."

    s_thoughts "I go back to holding her."

    s_thoughts "Charlotte reads her professor's words to herself and the room is warm in a way that has nothing to do with the heater."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 31: LILA CHECKS IN
    ## Brief. Sophia doesn't perform "everything's great."
    ## "That's the first time you haven't used the word 'fine.'"
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)
    play music mus_campus fadein 1.5

    show lila happy at center with dissolve

    l "Okay. Status report."

    s "What?"

    l "Charlotte. You. The whole -- situation. Give me a status report."

    s "Since when do you say 'status report?'"

    l "Since I took a management class. We learned about synergies. Don't change the subject."

    s "It's hard."

    show lila shocked at center

    s_thoughts "Lila stops walking."

    l "What?"

    s "It's hard. But it's real."

    show lila annoyed at center

    l "..."

    l "That's the first time you haven't used the word 'fine.'"

    s "...Huh."

    l "Every time I ask about Charlotte you say 'fine.' Or 'she's fine.' Or 'we're fine.' Or some arrangement of the word 'fine' that means absolutely nothing."

    s "I didn't realize I was doing that."

    l "You were. Constantly."

    s_thoughts "I think about that."

    l "So it's hard but it's real."

    s "Yeah."

    l "Is she okay?"

    s "I don't know. She went to a museum by herself."

    show lila shocked at center

    l "Charlotte went to a museum. ALONE?"

    s "She bought a postcard."

    l "Charlotte bought a postcard for HERSELF?"

    s "She liked a painting of a woman peeling an apple."

    show lila happy at center

    l "SHE LIKED A-- Oh my god. She's becoming a person."

    s "Lila."

    l "I mean that as a COMPLIMENT. She's becoming a person instead of a service."

    s_thoughts "That lands harder than Lila probably intended."

    s "Yeah. She is."

    l "Good."

    s_thoughts "Lila bumps my shoulder."

    l "You sound different too."

    s "Different how?"

    l "Less like you're managing a project. More like you're just... in it."

    s_thoughts "Huh."

    hide lila with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 32: AMARA'S GIFT
    ## THE EMOTIONAL PEAK OF ACT 3.
    ## Rice and eggs. Slightly burned.
    ## Charlotte cries because someone did
    ## the Charlotte thing for Charlotte.
    ## Protect this scene.
    ## ===========================

    scene bg kitchen with Fade(1.5, 0.5, 1.5)

    s_thoughts "Saturday morning."

    s_thoughts "I come downstairs."

    s_thoughts "The kitchen smells like rice and eggs."

    s_thoughts "My first thought is Charlotte. My stomach drops."

    s_thoughts "But the kitchen is empty."

    s_thoughts "No. Not empty."

    s_thoughts "There's a plate on the table."

    s_thoughts "One plate."

    s_thoughts "Rice. Eggs -- scrambled, not the fold kind. A little burned on the edges."

    s_thoughts "Next to the plate: chopsticks. A napkin. A cup of tea that's still steaming."

    s_thoughts "The rice cooker is on the counter. It's still warm."

    s_thoughts "I hear footsteps. Going up."
    
    show amara neutral with dissolve

    s_thoughts "Amara."

    s_thoughts "She made breakfast and put it on the table."

    s_thoughts "She didn't announce it. She didn't wait. She didn't set five places."

    s_thoughts "One plate. One set of chopsticks. One cup of tea."
    
    s_thoughts "Amara walks out without saying a word to me. I'm not even sure she notices me. She goes up the stairs. Her room is downstairs."
    
    hide amara with dissolve

    s_thoughts "I stand in the kitchen."

    s_thoughts "The plate is sitting on the table and I know who it's for because Amara put it at Charlotte's chair."

    s_thoughts "I back out. Go to the stairs. Sit on the bottom step."
    
    show amara neutral with dissolve

    s_thoughts "I wait. A moment later, Amara passes me and returns to her room."
    
    hide amara with dissolve

    s_thoughts "A few minutes. Maybe ten, fifteen."

    s_thoughts "Charlotte's door opens."

    s_thoughts "Footsteps on the stairs."

    show charlotte pj neutral at center with dissolve

    s_thoughts "Charlotte comes down. She's in pajamas. Hair messy. Eyes still morning-small."

    s_thoughts "She sees me on the stairs."

    c "Hey."

    s "There's breakfast."

    s_thoughts "She nods."

    c "I didn't--"

    s "I know."

    s_thoughts "Charlotte walks into the kitchen."

    s_thoughts "I stay on the stairs."

    s_thoughts "I can see her from here."

    s_thoughts "She sees the plate."

    show charlotte pj surprised at center

    s_thoughts "She stops."
    
    play music mus_charlotte_sad fadein 3.0

    s_thoughts "She's standing in the kitchen looking at a plate of rice and burned eggs and a cup of tea that someone made for her."

    s_thoughts "She looks at the stairs."

    s_thoughts "Not at me. Past me. Amara's bedroom."

    s_thoughts "She sits down."

    s_thoughts "She picks up the chopsticks."

    show charlotte pj sad at center

    s_thoughts "She eats."

    s_thoughts "She takes one bite."

    s_thoughts "Two."

    s_thoughts "The eggs are a little burned. The rice is slightly too wet. The tea is genmaicha, not the fancy Earl Grey Charlotte keeps in the cabinet."

    s_thoughts "It's not good."

    s_thoughts "It's not the fold omelet. It's not the garnish. It's not the sprig of something green."

    s_thoughts "Charlotte puts the chopsticks down."

    show charlotte pj vulnerable at center

    s_thoughts "She cries."

    s_thoughts "She cries and she's small and she's ten years old again and someone made her breakfast."

    s_thoughts "Just... crying."
    
    s_thoughts "I watch. I don't file. I can't. Not now."

    s_thoughts "Tears stream down her face. But she's quiet. Her shoulders shaking. One hand over her mouth."

    s_thoughts "She's crying because someone made breakfast and put it on the table and told her and went back to her room and not a single 'of course' was exchanged."

    s_thoughts "Someone did the Charlotte thing."

    s_thoughts "For Charlotte."

    s_thoughts "And Amara didn't need her to say thank you. Amara didn't need her to be grateful. Amara didn't need her to do anything."

    s_thoughts "She just put a plate on the table without a word."

    s_thoughts "Charlotte picks up the chopsticks again."

    s_thoughts "She eats."

    s_thoughts "She eats the burned eggs and the wet rice and she cries and she eats."

    s_thoughts "I sit on the stairs."

    s_thoughts "I don't go in."

    s_thoughts "Some things aren't for me."

    s_thoughts "Charlotte finishes the plate."

    s_thoughts "She drinks the tea."

    s_thoughts "She washes the plate."

    s_thoughts "She washes it slowly. Not the frantic clean-everything way. Just... washing a plate."

    s_thoughts "She puts it on the rack."

    s_thoughts "She stands at the sink for a long time."

    s_thoughts "Then she goes to the stairs."
    
    scene bg entry with dissolve

    s_thoughts "She looks at me."

    show charlotte pj sad at center with dissolve

    s_thoughts "Her eyes are red. She doesn't try to hide it."

    c "The eggs were terrible."

    s "Yeah?"

    c "Amara can't cook."

    s "No."

    c "She made them anyway."

    s "She did."

    s_thoughts "Charlotte sits on the step above me."

    s_thoughts "We sit on the stairs."

    s_thoughts "It's quiet. I half-expect her to cry again, but she doesn't."

    s_thoughts "She just sits. I rest my head on her leg."

    s_thoughts "After a while she stands up and walks back down."

    s_thoughts "I hear her knock on Amara's door."

    s_thoughts "I can't hear what she says."

    s_thoughts "I don't need to."

    hide charlotte with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 33: ISABELLA BACKGROUND THREAD
    ## Brief. The real smile.
    ## The player who did Isabella's route knows.
    ## ===========================

    scene bg kitchen with Fade(1.5, 0.5, 1.5)

    s_thoughts "Later that afternoon."

    show isabella smile at center with dissolve

    s_thoughts "Isabella is in the kitchen. She's on her phone. She's smiling at it."

    s_thoughts "Her glasses slide down because her cheeks push up."

    s_thoughts "She sees me and doesn't hide the phone."

    i "Hey."

    s "Hey."

    s_thoughts "She looks... lighter."

    s_thoughts "Something shifted. I don't know what."

    i "Good day?"

    s "Getting there."

    show isabella happy at center

    i "Yeah."

    s_thoughts "She goes back to her phone."

    s_thoughts "I go to the fridge."

    s_thoughts "I hear her clear her throat."
    
    show isabella neutral at center
    
    i "Sophia?"
    
    s "What's up?"
    
    s_thoughts "She hesitates."
    
    i "Charlotte seems to be doing better."
    
    s_thoughts "I nod."
    
    s "Yeah. She's doing okay."
    
    s_thoughts "Amara echoes in my mind. 'She's always okay.' I wonder if this time is any different."
    
    s_thoughts "Isabella looks down at her phone and back at me."
    
    i "You're a good girlfriend."
    
    s "I am."
    
    i "You... I..."
    
    show isabella vulnerable at center
    
    i "It's just, well... You and Charlotte... I-I kinda wish..."
    
    s_thoughts "I give her a look. I'm not sure what this is about. This doesn't fit in my Isabella file. I watch her closely. She can tell what I'm doing. I know she can."
    
    i "..."
    
    pause 1.5
    
    show isabella sad at center
    
    pause 1.5
    
    show isabella neutral at center
    
    i "N-Never mind."
    
    s "Okay, weirdo."
    
    show isabella laugh at center
    
    s_thoughts "She laughs."

    s_thoughts "It's fine."
    
    s_thoughts "I file it."
    
    s_thoughts "She's fine."

    hide isabella with dissolve

    ## ===========================
    ## SCENE 34: THE SISTER CALL
    ## Charlotte calls Sophie. Not because Sophie needs her.
    ## Because Charlotte wants to talk.
    ## "Since when are you the smart one?"
    ## The snort.
    ## ===========================

    scene bg charlottebedroom with Fade(0.8, 0.3, 0.8)
    play music mus_stillhere fadein 2.0

    s_thoughts "Monday evening."

    s_thoughts "I'm in Charlotte's doorway. She waved me in."

    s_thoughts "She's on the phone. But different."

    show charlotte smile at center with dissolve

    s_thoughts "She's on the bed. Legs crossed. Leaning against the wall. The three postcards are above her."

    s_thoughts "She's not standing. She's not pacing. She's not making a list."

    c "No, I KNOW, Sophie. I know. But that's what I'm saying -- it doesn't have to be a PLAN."

    s_thoughts "She's talking to Sophie."

    s_thoughts "She called Sophie."

    s_thoughts "Not because Sophie called crying. Not because mom had a bad day. Charlotte picked up the phone because she wanted to talk to her sister."

    c "I don't know. I genuinely don't know. That's the whole point."

    s_thoughts "She laughs."
    
    show charlotte laugh at center

    c "Because I used to know everything! I had the answers. Now I'm not so sure anymore."

    c "Now I'm just -- I'm a girl who's figuring herself out."
    
    s_thoughts "She looks at me and smiles."
    
    show charlotte smile at center

    c "Plus I have a beautiful girlfriend."
    
    s_thoughts "I blush. She says it all the time and every time I blush."
    
    s_thoughts "She listens for a bit."

    c "I KNOW it sounds weird. It IS weird."

    s_thoughts "She listens again."

    show charlotte surprised at center

    c "Since when are you the smart one?"

    s_thoughts "Sophie said something. I can't hear it."

    show charlotte laugh at center

    c "Oh SHUT UP."

    s_thoughts "Charlotte laughs."

    s_thoughts "The real one."

    s_thoughts "The snort."

    s_thoughts "The one she hates because it's not pretty. Not the musical Charlotte laugh. The one that sounds like a surprised pig who just got spanked but kind of likes it."

    s_thoughts "She covers her mouth."

    s_thoughts "She sees me seeing her."

    show charlotte embarrassed at center

    c "I have to go. Sophie. I have to GO. Because you're being MEAN. And my BEAUTIFUL girlfriend is at my door and I'm going to KISS her a lot after this. ...EW YOURSELF."

    s_thoughts "She's smiling."

    s_thoughts "The snort smile."

    c "Love you too. Call me -- whenever. Not because you need something. Just because."

    s_thoughts "She hangs up."
    
    show charlotte smile at center

    c "Sophie says hi."

    s "She doesn't know me."

    c "She knows you exist. Obviously. She knows how good you've been for me."

    s "I haven't been THAT good."

    show charlotte smile at center

    c "I... told her about the museum."

    s "What did she say?"

    c "She said 'since when are you the smart one.'"

    s "That's a good sister."

    c "She's a terrible sister. She's sixteen and she's smarter than me."

    s "She had a good teacher."

    show charlotte neutral at center

    s_thoughts "Charlotte looks at me."

    s_thoughts "Not the way she used to look at me."

    s_thoughts "Just looking. Like I'm a painting. I like it."

    c "Yeah."

    s_thoughts "She picks up the bakery novel from the bed."

    c "The bread woman left her ex-husband."

    s "Good for her."

    c "She opened her own bakery."

    s "Was the sourdough good?"

    c "The sourdough was INCREDIBLE. Apparently."

    s_thoughts "I sit on the bed."

    s_thoughts "Charlotte sits beside me. She puts the book down."

    s_thoughts "I give her a look."

    s_thoughts "The postcards are above us."

    s_thoughts "Three women. Different paintings. Different centuries."

    s_thoughts "All of them doing something alone."
    
    s "So you're going to kiss your beautiful girlfriend a lot, huh?"
    
    show charlotte flooshed at center 
    
    c "...Maybe just a little."
    
    s_thoughts "It's not just a little. Time dissolves for a while. It's beautiful."
    
    s_thoughts "Like a painting."

    hide charlotte with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 35: "MAKE YOUR OWN DAMN TOAST"
    ## The exhale.
    ## The first real laugh in weeks.
    ## ===========================

    scene bg kitchen with Fade(1.5, 0.5, 1.5)

    s_thoughts "Wednesday morning."

    s_thoughts "I come downstairs."

    s_thoughts "No eggs. No humming. No Charlotte at the stove."

    s_thoughts "Charlotte is at the table with coffee and the bakery novel."

    show charlotte neutral at center with dissolve

    s_thoughts "I open the bread box."

    s "We have bread."

    c "Mm."

    s "I'm going to make toast."

    c "Okay."

    s_thoughts "I put the bread in the toaster."

    s_thoughts "I stand at the counter."

    s_thoughts "The toaster clicks and hums."

    s "I miss your toast."

    show charlotte neutral at center

    s_thoughts "Charlotte looks up from the novel."

    s "Your toast was better than my toast. I don't know what you did to it."

    c "Butter on both sides before toasting."

    s "That's cheating."

    c "It's TECHNIQUE."

    s_thoughts "The toaster pops. My toast is fine. Regular toast. One-sided-butter toast."

    s "Seriously though. Your toast was really good."

    play music mus_charlotte fadein 2.0

    show charlotte smile at center

    c "Make your own damn toast."

    s_thoughts "I stare at her."

    s_thoughts "Charlotte is looking at me over the bakery novel."

    s_thoughts "She said it flat. Deadpan. Like she's been saving it."

    s_thoughts "I laugh."

    s_thoughts "I don't mean to. It catches me by surprise. It's the surprised kind -- the kind that comes out before you can decide if something is funny."

    s_thoughts "Charlotte's mouth twitches."

    show charlotte laugh at center

    s_thoughts "She laughs."

    s_thoughts "The snort."

    s_thoughts "And then I'm laughing harder because the snort is the funniest sound any human being has ever made and Charlotte is covering her mouth and saying 'STOP' which makes me laugh more."

    s "Make your own damn toast!"

    c "STOP LAUGHING."

    s "I CAN'T."

    s_thoughts "We're both laughing in a kitchen with dishes in the sink and no chore chart on the fridge and my toast is getting cold and Charlotte's coffee is next to a bakery novel and it's the most beautiful mess either of us has ever seen."

    s_thoughts "Charlotte wipes her eyes."

    show charlotte happy at center

    c "I meant it. Make your own toast."

    s "I did. It's bad."

    c "Good."

    s_thoughts "She goes back to the novel."

    s_thoughts "I eat my bad toast."

    s_thoughts "Charlotte's coffee gets cold because she forgot about it."

    s_thoughts "She forgot about her coffee because she's reading about bread."

    s_thoughts "That's enough."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 36: EVE'S DECISION (CONDITIONAL on charlotte_eve)
    ## Three paths:
    ## Positive: Eve comes to dinner. "Hey." "Hey."
    ## Negative: Eve's room is empty. A note.
    ## Zero: The player gets a direct choice.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    s_thoughts "Friday."

    if charlotte_eve > 0:
        ## === EVE STAYED (charlotte_eve positive) ===

        play music mus_morningafter fadein 2.0

        s_thoughts "Dinner."

        s_thoughts "Isabella made pasta. It's overcooked. Nobody cares."

        show charlotte smile at left with dissolve
        show isabella happy at right with dissolve

        s_thoughts "Charlotte is at the table. Isabella is talking about something on her phone. I'm opening a jar of sauce."

        s_thoughts "The front door opens."

        hide isabella with dissolve

        show eve neutral at right with dissolve

        s_thoughts "Eve walks in."

        s_thoughts "She doesn't explain. She doesn't announce. She just comes into the kitchen and pulls out a chair."

        s_thoughts "Charlotte sees her."

        show charlotte neutral at left

        s_thoughts "Charlotte doesn't say 'of course.' Doesn't say 'welcome back.' Doesn't say 'oh, you're joining us!'"

        c "Hey."

        e "Hey."

        s_thoughts "Eve sits down."

        s_thoughts "Charlotte passes her a plate."

        s_thoughts "Not the Charlotte plate-pass. Not the garnished, arranged, made-for-you plate. Just a plate."

        s_thoughts "Eve takes it."

        s_thoughts "We eat overcooked pasta."

        s_thoughts "The chore chart stays off the fridge."

        hide eve with dissolve
        hide charlotte with dissolve
        stop music fadeout 2.0

        jump charlotte_ch5_porch_eve_stayed

    elif charlotte_eve < 0:
        ## === EVE LEFT (charlotte_eve negative) ===

        s_thoughts "I come downstairs."

        s_thoughts "Charlotte is in the kitchen. She's holding a piece of paper."

        show charlotte neutral at center with dissolve
        
        play music mus_wrong fadein 2.0

        s_thoughts "Eve's door was open when I walked past. Not closed-open. Open-open."

        s_thoughts "Empty."

        s_thoughts "The books are gone. The desk lamp is gone. The single plant she kept on the windowsill."

        s_thoughts "Gone."

        s "Charlotte?"

        c "She left a note."

        s_thoughts "Charlotte's voice is flat."

        c "'Found a room. It's quieter.'"

        s "..."

        c "That's the whole note."

        s_thoughts "Charlotte reads it one more time."

        s_thoughts "She puts it in the recycling bin."

        s_thoughts "She doesn't say anything."

        s_thoughts "She doesn't cry."

        s_thoughts "She stands at the counter."

        s_thoughts "Her hand reaches toward the cabinet -- the one with the cleaning supplies."

        s_thoughts "She catches herself."

        s_thoughts "She puts her hand down."

        s_thoughts "She goes upstairs."

        hide charlotte with dissolve
        stop music fadeout 2.0

        jump charlotte_ch5_porch_eve_left

    else:
        ## === charlotte_eve EXACTLY ZERO ===
        ## The torn player gets a direct choice.

        s_thoughts "I come downstairs."

        s_thoughts "Charlotte is in the kitchen."

        show charlotte happy at left with dissolve

        s_thoughts "She's smiling."
        
        play music mus_glass fadein 2.0

        c "I was thinking -- Eve's room. We could turn it into a study! There's good light in there."

        s "Charlotte--"

        c "Or a reading nook! She had those bookshelves, right? We could keep them and--"

        s_thoughts "Movement in the hallway."

        show eve neutral at right with dissolve

        s_thoughts "Eve. Standing in the hallway. Holding a box."

        s_thoughts "Charlotte hasn't seen her."

        s_thoughts "Eve has very much seen her, though."

        s_thoughts "Eve is watching Charlotte perform brightness about the room Eve is leaving."

        s_thoughts "I'm standing between them."

        s_thoughts "Literally between them."

        show charlotte smile at left

        c "The light is really good in the afternoons, actually. I was thinking a DESK, one of those nice--"

        s_thoughts "Eve shifts the box to her other hip."

        s_thoughts "She's waiting."

        s_thoughts "Not for Charlotte to notice her. For me."

        menu:
            "\"Charlotte, stop.\"":
                $ charlotte_eve += 2

                s "Charlotte, stop."

                show charlotte surprised at left

                s_thoughts "Charlotte stops."

                s_thoughts "She looks at me."

                s_thoughts "I look at the hallway."

                s_thoughts "Charlotte follows my eyes."

                show charlotte neutral at left

                s_thoughts "She sees Eve."

                s_thoughts "Eve with the box."

                s_thoughts "The brightness drains."

                c "..."

                show eve neutral at right

                s_thoughts "The kitchen is very quiet."

                s_thoughts "Charlotte's face does something I haven't seen before. Not the mask cracking. Not the blank. Something... crumbling. Like a wall deciding to come down on its own."

                show charlotte sad at left

                c "I was doing it again."

                s_thoughts "She says it to the floor."

                c "I was -- you're leaving and I was turning your room into a project."

                show eve neutral at right

                e "..."

                c "I'm sorry."

                s_thoughts "Eve looks at Charlotte."

                s_thoughts "She puts the box down."

                s_thoughts "Not on the floor like she's staying. On the hall table. Like she's deciding."

                show eve neutral at right

                e "The room on Elm is quieter."

                c "I know."

                e "This house is loud."

                c "I know."

                s_thoughts "A beat."

                e "But quiet gets old."

                s_thoughts "Eve picks up the box."

                s_thoughts "She takes it upstairs."

                s_thoughts "To her room."

                hide eve with dissolve

                s_thoughts "Charlotte is standing in the kitchen."

                show charlotte sad at left

                s_thoughts "Her hands are shaking."

                c "I was doing it. I was RIGHT THERE doing the thing."

                s "You were."

                c "If you hadn't said--"

                s "I know."

                s_thoughts "She sits down at the table."

                s_thoughts "She puts her head in her hands."

                s_thoughts "She doesn't cry."

                s_thoughts "She just sits."

                hide charlotte with dissolve
                stop music fadeout 2.0

                jump charlotte_ch5_porch_eve_zero_stayed

            "\"It's okay. We'll figure out the room.\"":
                $ charlotte_eve -= 2

                s "It's okay. We'll figure out the room."

                show charlotte happy at left

                c "Right! It's a great space. Really. Good bones."

                s_thoughts "Charlotte is smiling."

                s_thoughts "In the hallway, Eve picks the box back up."

                s_thoughts "She watches Charlotte talk about bookshelves and afternoon light."

                show eve sad at right

                s_thoughts "Eve looks at me."

                s_thoughts "I look at Eve."

                s_thoughts "She nods. Once. Like something has been confirmed."

                s_thoughts "She goes upstairs."

                hide eve with dissolve

                s_thoughts "I hear the front door twenty minutes later."

                s_thoughts "Charlotte is still talking about the room."

                show charlotte smile at left

                c "We could do plants! Charlotte's room has plants and it's so -- it would be so nice with plants."

                s_thoughts "Charlotte doesn't have plants."

                s_thoughts "Charlotte is talking about a room that belongs to someone who just walked out the front door and she hasn't noticed."

                s_thoughts "I smoothed it over."

                s_thoughts "Eve picked up the box."

                hide charlotte with dissolve
                stop music fadeout 2.0

                jump charlotte_ch5_porch_eve_zero_left

    ## ===========================
    ## SCENE 37: THE PORCH — END OF CHAPTER
    ## Four endings based on Eve's outcome.
    ## Each should feel complete on its own.
    ## ===========================

    ## ===========================
    ## PORCH A: Eve Stayed (charlotte_eve positive)
    ## The mask is thin. Charlotte lets it be thin.
    ## "I don't know who I am without it."
    ## "I'm here anyway."
    ## ===========================

label charlotte_ch5_porch_eve_stayed:

    scene bg porch with Fade(1.0, 0.5, 1.0)
    play music mus_charlotte fadein 3.0

    s_thoughts "The porch."

    s_thoughts "Same place where the chemistry began to spark."

    s_thoughts "But different Charlotte. And different Sophia."

    s_thoughts "It's cold. Charlotte has a blanket around her shoulders."

    show charlotte neutral at center with dissolve

    s_thoughts "She's not performing warmth. She's not performing cold."

    c "Eve stayed."

    s "She did."

    c "I keep waiting for the -- I don't know. The relief? The 'everything is okay now' feeling?"

    s "Is it coming?"

    c "No."

    s_thoughts "She pulls the blanket tighter."

    c "I thought -- if she stayed, it would mean something. Like proof. 'You stopped performing and nobody left.'"

    s "But?"

    c "But I didn't stop. I just -- changed what I was performing. I performed 'trying.' I performed 'not performing.' And Eve stayed but I don't know if she stayed because I changed or because you kept showing up for her."

    s "Does it matter?"

    show charlotte sad at center

    c "Yeah. It matters."

    s_thoughts "The porch is quiet."

    c "I don't know who I am without it."

    s "The mask?"

    c "All of it. The eggs. The 'of course.' The -- the way I scan a room and know what everyone needs before they know they need it. That's not just a mask. That's -- that's me. Or it was me. Or it's the thing I built instead of me."

    s_thoughts "She looks at the yard."

    c "I don't know what's underneath."

    s "Maybe there's nothing underneath."

    show charlotte surprised at center

    c "That's terrifying."

    s "I mean maybe there's not a secret Charlotte under the mask Charlotte. Maybe you just... build from here."

    show charlotte neutral at center

    c "From here."

    s "From a woman who went to a museum and liked an apple painting and reads bakery novels and tells her sister 'I don't know.'"

    c "That's not very impressive."

    s "It's real."

    s_thoughts "Charlotte pulls the blanket around herself."

    s_thoughts "She looks at me."

    c "I'm going to say 'of course' again. You know that."

    s "I know."

    c "It's going to come out. In the old voice. At the wrong time. And I'm going to hate it."

    s "I know."

    c "And you're going to use the careful voice."

    s "Probably."

    c "And I'm going to snap at you about it."

    s "Looking forward to it."

    show charlotte smile at center

    s_thoughts "Almost a laugh."

    c "I don't know who I am."

    s "No."

    c "And you're here anyway."

    s "I'm here anyway."

    c "Of course."

    s_thoughts "She catches it."

    show charlotte embarrassed at center

    s_thoughts "She heard it."

    c "...Habit."

    s_thoughts "The porch."

    $ charlotte_present -= 1
    
    $ charlotte_push -= 1

    s_thoughts "The same porch. The same two people."

    s_thoughts "Less polish. More blanket."

    s_thoughts "Charlotte Opal is sitting on a porch not knowing who she is and she didn't perform the not-knowing."

    s_thoughts "She just didn't know."

    s_thoughts "The mask is thin."

    s_thoughts "She's letting it be thin."

    stop music fadeout 3.0

    jump charlotte_ch5_end

    ## ===========================
    ## PORCH B: Eve Left (charlotte_eve negative)
    ## Charlotte is performing HARD.
    ## "We could turn it into a study!"
    ## Sophia can't reach her.
    ## ===========================

label charlotte_ch5_porch_eve_left:

    scene bg porch with Fade(1.0, 0.5, 1.0)
    play music mus_charlotte fadein 3.0

    s_thoughts "The porch."

    s_thoughts "Same place."

    show charlotte happy at center with dissolve

    c "It's nice out!"

    s "It's cold."

    c "Cold-nice. Brisk. Invigorating."

    s_thoughts "Charlotte is smiling."

    s_thoughts "The full one. The bright one. Wattage at maximum."

    c "I was thinking about the room. Eve's room. Former Eve's room."

    s "Charlotte."

    c "A study would be really nice. With a desk and one of those lamps -- the ones with the green shade? Very library. Very academic."

    s "Charlotte."

    show charlotte smile at center

    c "Or a guest room! For when Sophie visits. She could take the bus up and we could -- she's never been to campus. I could show her around."

    s "Charlotte, she left."

    show charlotte happy at center

    c "I KNOW she left. And that's fine! People leave. It's fine."

    s "It's not fine."

    c "Of course it is! People move. It happens. She wanted something quieter. That's a valid choice."

    s_thoughts "The 'of course' is at full volume."

    s "She didn't leave because she wanted something quieter."

    show charlotte smile at center

    c "She said it was quieter. On the note. 'It's quieter.' That's what she said."

    s_thoughts "Charlotte is looking at me."

    s_thoughts "The smile is perfect."

    s_thoughts "I can't get in."

    s_thoughts "The door to Charlotte is closed and she locked it from the inside and she's standing behind it saying 'I'm fine' in the brightest voice she has."

    c "Anyway! I was thinking -- this weekend we could clear out the room. Make it nice. Fresh start."

    s "Okay."

    s_thoughts "I say 'okay.'"

    s_thoughts "Because there's nothing else to say."

    s_thoughts "Charlotte is disappearing in real time."

    $ charlotte_present -= 2

    s_thoughts "Eve leaving proved what Charlotte always feared."

    s_thoughts "She stopped performing and someone left."

    s_thoughts "Except that's not what happened."

    s_thoughts "Eve left because Charlotte DIDN'T stop performing. Because the 'of course' was so loud it pushed Eve out the door."

    s_thoughts "And Charlotte can't see that."

    s_thoughts "And I'm sitting on the porch with a smile that won't crack."

    c "I'm fine."

    s_thoughts "She means nothing by it."

    stop music fadeout 3.0

    jump charlotte_ch5_end

    ## ===========================
    ## PORCH C: Eve Zero — Stayed ("Charlotte, stop")
    ## Charlotte is shaken. The mask was ripped off by someone else.
    ## "...Sorry." Not "habit." Just "sorry."
    ## ===========================

label charlotte_ch5_porch_eve_zero_stayed:

    scene bg porch with Fade(1.0, 0.5, 1.0)
    play music mus_charlotte_sad fadein 3.0

    s_thoughts "The porch."

    show charlotte neutral at center with dissolve

    s_thoughts "Charlotte is sitting on the steps. Not on the bench. On the steps. Like she doesn't have the energy to make it all the way to a proper seat."

    s_thoughts "I sit next to her."

    c "You stopped me."

    s "Yeah."

    c "In the kitchen. I was doing it and you stopped me."

    s "Yeah."

    c "If you hadn't said anything--"

    s "I know."

    show charlotte sad at center

    c "Eve would have left."

    s "Probably."

    c "Because I was doing the thing. The room. The study. The -- I was already decorating her absence."

    s "You were."

    s_thoughts "Charlotte's hands are in her lap."

    c "I didn't even see her."

    s "..."

    c "She was standing right there. With a box. And I didn't see her."

    s_thoughts "Her voice cracks."

    c "I was making her leaving into a project and I was doing it so automatically I didn't see she was leaving."

    s "Charlotte."

    c "What?"

    s "She stayed."

    show charlotte neutral at center

    c "Because of you."

    s "Because the house changed."

    c "Because YOU changed it. In that moment. You said stop."

    s "And you stopped."

    show charlotte sad at center

    c "Because you told me to."

    s_thoughts "She's right."

    s_thoughts "I told Charlotte to stop performing and she stopped. Because I asked."

    s_thoughts "That's the thing about Charlotte. She does what you need."

    $ charlotte_push -= 1
    
    $ charlotte_present -= 1

    c "Of course."

    s_thoughts "She catches it."

    s_thoughts "Her face tightens."

    c "...Sorry."

    s_thoughts "Not 'habit.'"

    s_thoughts "Just 'sorry.'"

    s_thoughts "She doesn't know if the apology is for the word or for everything it represents."

    s_thoughts "Neither do I."

    s_thoughts "We sit on the steps."

    s_thoughts "Eve is upstairs. The box is on the hall table."

    s_thoughts "The growth was real."

    s_thoughts "It just wasn't Charlotte's."

    stop music fadeout 3.0

    jump charlotte_ch5_end

    ## ===========================
    ## PORCH D: Eve Zero — Left ("We'll figure out the room")
    ## Charlotte performing. But fragile.
    ## Voice wavers on "fine."
    ## Sophia's fault.
    ## ===========================

label charlotte_ch5_porch_eve_zero_left:

    scene bg porch with Fade(1.0, 0.5, 1.0)
    play music mus_charlotte fadein 3.0

    s_thoughts "The porch."

    show charlotte smile at center with dissolve

    s_thoughts "Charlotte is sitting on the bench."

    s_thoughts "She has a mug. She's holding it the way she holds things when she needs her hands to be busy."

    c "Nice night."

    s "Yeah."

    c "I called Sophie again. She's doing good. Mom's doing good."

    s "That's good."

    c "Everything's good."

    s_thoughts "She smiles."

    s_thoughts "It's thin."

    s_thoughts "Something underneath is showing."

    c "The room will be nice."

    s "Charlotte."

    c "As a study. With the green lamp."

    s "Charlotte."

    show charlotte neutral at center

    c "What?"

    s "Eve left."

    c "I know Eve left."

    s "Because I let you--"

    c "I'm fine."

    s_thoughts "Her voice wavers on 'fine.'"

    s_thoughts "Just slightly. A tremor. Like 'fine' is a plate she's balancing and someone bumped the table."

    $ charlotte_push -= 2

    c "I'm fine. She wanted quieter. She got quieter."

    s_thoughts "Charlotte knows."

    s_thoughts "I know she knows."

    s_thoughts "She was SO CLOSE."

    s_thoughts "But Eve left."

    c "Maybe we could get a rug. For the room. Something nice."

    s "Sure."

    s_thoughts "Charlotte's voice is bright."

    s_thoughts "The 'fine' wavered. Everything else is steady."

    s_thoughts "She almost had it."

    s_thoughts "I took it from her."

    stop music fadeout 3.0

    jump charlotte_ch5_end

    ## ===========================
    ## CHAPTER 5 END
    ## ===========================

label charlotte_ch5_end:

    scene black with Fade(2.0, 1.0, 2.0)
    
    "Chapter 5: Weight -- End"

    jump charlotte_ch6
