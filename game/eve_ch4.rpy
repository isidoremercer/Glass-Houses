## eve_ch4.rpy -- Glass Houses
## Chapter 4: "The Approach" -- Eve Route
## Act 1: "The Orbiting" (Scenes 1-11)

## === NEW VARIABLES NEEDED (add to variables.rpy) ===
## None yet -- Eve's route has no choices. May need variables for Act 3 / Ch5.

## === AUDIO DEFINITIONS ===
define audio.mus_eve = "audio/music/Eve Morse ~ A Room That Just Emptied.mp3"
define audio.mus_2am = "audio/music/House at 2AM.mp3"
define audio.mus_campus = "audio/music/Campus in Autumn.mp3"
define audio.mus_fivepeople = "audio/music/Five People in a Kitchen.mp3"
define audio.mus_tuesday = "audio/music/A Normal Tuesday.mp3"
define audio.mus_charlotte = "audio/music/Charlotte Opal ~ Toast Girl.mp3"
define audio.mus_time = "audio/music/Moments Across Time.mp3"
define audio.mus_shoulders = "audio/music/Shoulders Touching.mp3"
define audio.mus_morningafter = "audio/music/The Morning After The Hard Thing.mp3"
define audio.mus_glass = "audio/music/Glass Walls.mp3"
define audio.mus_wrong = "audio/music/Something's Wrong in the Kitchen.mp3"
define audio.mus_fragile = "audio/music/Fragile Glass Between.mp3"
define audio.mus_mourning = "audio/music/Mourning.mp3"

## ===========================
## CHAPTER 4 START
## ===========================

label eve_ch4:
    
    pause 1.5
    
    menu:
        "View trigger warning for this route.":
            "TW: This route contains extended discussion of a past sexual assault. Nothing is depicted graphically, but it is a central theme."
            pause 1.5
            jump eve_ch4_start
        "Skip.":
            pause 1.5
            jump eve_ch4_start

    ## ===========================
    ## SCENE 1: THE KITCHEN AT MIDNIGHT
    ## Eve on the kitchen floor. Sophia comes down for water.
    ## Walls: full up. One-word answers.
    ## Smile count: 0.
    ## ===========================
    
label eve_ch4_start:
    scene bg kitchen night with Fade(1.0, 0.5, 1.0)

    play music mus_2am fadein 3.0

    s_thoughts "2 AM."

    s_thoughts "I can't sleep because my brain won't stop doing the thing where it replays every conversation from the last twelve hours and adds commentary."

    s_thoughts "Water. That's the mission. Go downstairs, get water, come back, stare at the ceiling like a normal person."

    s_thoughts "The kitchen light is on."

    show eve neutral at center with dissolve

    s_thoughts "Eve."

    s_thoughts "She's at the table. Mug in both hands, book open in front of her. Not the floor this time. She's sitting like a person who expected to be here for a while."

    s_thoughts "She looks up."

    e "Oh. Hi."

    s_thoughts "Same as last time. 'Oh. Hi.' Like she's confirming I exist rather than greeting me."

    s "Hey. Sorry. Just getting water."

    s_thoughts "She nods. Goes back to her book."

    s_thoughts "I fill a glass. The tap sounds enormous in the quiet."

    s_thoughts "I drink it standing at the counter. The fridge hums. Eve turns a page."

    s_thoughts "Her socks don't match. One is grey, one is dark blue. I don't know why I'm looking at her socks."

    s_thoughts "I should go back upstairs."

    s_thoughts "I don't go back upstairs."

    s_thoughts "I sit down across from her. She doesn't look up."

    s_thoughts "We sit."

    s_thoughts "Eve reads. I have no book and no excuse for being here. The mug in her hands is the green one with the chip on the rim. She always uses that one. I don't know when I learned that."

    e "Mm."

    s_thoughts "Not a word. A sound. She hasn't asked me to leave."

    s_thoughts "The house is different at this hour. No Charlotte energy in the walls. No Isabella's music through the floor. Just the fridge and the clock and Eve's page turning."

    e "The house is quieter when Charlotte's asleep."

    s_thoughts "That's a speech, for midnight Eve."

    s "Yeah. It is."

    s_thoughts "She takes a sip of tea. Both hands. She wraps her whole hands around the mug like she's protecting it from something."

    s_thoughts "We sit for a while longer. I don't know how long. Long enough that my glass is empty and I should get more water or go to bed."

    e "Goodnight."

    s "Goodnight, Eve."

    s_thoughts "She doesn't look up from the book."

    s_thoughts "I rinse my glass. I go upstairs."

    hide eve with dissolve

    pause 1.5

    s_thoughts "The kitchen light stays on."

    stop music fadeout 3.0
    
    ## ===========================
    ## SCENE 1.5: "CARRYING THE MIDNIGHT"
    ## Sophia alone the next day. Replaying the physical details.
    ## The before of the crush. Filing that lingers.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    play music mus_tuesday fadein 2.0

    s_thoughts "Wednesday. My room. 7:30 AM."

    s_thoughts "I have class in an hour. I've been awake for twenty minutes. I've been staring at my ceiling for nineteen of them."

    s_thoughts "The other minute I spent looking at the glass of water on my nightstand and thinking about how I filled it from the same tap as Eve last night and that's a stupid thing to think about."

    s_thoughts "Eve was at the kitchen table."

    s_thoughts "This is not new information. Eve is sometimes at the kitchen table. Eve exists in the house. I am aware of this."

    s_thoughts "She held the mug with both hands."

    s_thoughts "Both hands. Wrapped around it. Not the way you hold a mug when you're drinking something -- the way you hold something you're keeping warm. Or keeping safe. Like the mug might leave if she wasn't careful."

    s_thoughts "The green one. The one with the chip on the rim."

    s_thoughts "Her socks didn't match. One grey, one blue. Who wears mismatched socks at 2 AM? Everyone. Everyone wears mismatched socks at 2 AM because nobody's looking at socks at 2 AM."

    s_thoughts "I was looking at her socks at 2 AM."

    s_thoughts "And her hands. And the way she turned a page without the sound going anywhere -- just a small sound in a big silence."

    s_thoughts "'Oh. Hi.'"

    s_thoughts "She said it like she was confirming something. Not 'oh, hi, how nice to see you.' Not 'oh, hi, what are you doing here.' Just: oh. Hi. You exist. Noted."
    
    scene bg bathroom with dissolve

    s_thoughts "I get out of bed. I get dressed. I brush my teeth. Normal things. The things a person does when they're going to class and not replaying a night over and over in their heads."

    s_thoughts "It's not -- it's nothing. It's a girl drinking tea at 2 AM. It's unremarkable."

    s_thoughts "I'm remarking on it."

    s_thoughts "I'm annoyed that I'm remarking on it."

    scene bg campus with Fade(0.8, 0.3, 0.8)

    s_thoughts "Walking to class. The air is cold. My jacket smells like the laundry detergent Charlotte insists we all use because it was on sale."

    s_thoughts "I think about the kitchen light staying on after I left."

    s_thoughts "Was she still reading? Did she go to bed right after? Does she do this every night -- sit in the kitchen at 2 AM with her book and her green mug and her mismatched socks?"

    s_thoughts "I don't know."

    s_thoughts "The filing instinct is running. That's what this is. I met a new variable and my brain wants to put it somewhere. Who is Eve at 2 AM? What does she read? Why the kitchen table and not her room?"

    s_thoughts "File it. Move on."

    s_thoughts "I file it."

    s_thoughts "I don't move on."

    s_thoughts "I'm still thinking about both hands on the mug when I sit down in the lecture hall."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 2: NOVA'S CLASS -- ETHNOGRAPHY INTRODUCTION
    ## Nova introduces the elective. The observer's obligation.
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)

    play music mus_nova fadein 2.0

    s_thoughts "It's time for Dr. Nova's elective."

    s_thoughts "I signed up because the description said 'ethics of observation' and I thought, well, that's basically my autobiography."
    
    s_thoughts "Lila signed up because she thought it would be an easy A. Same difference."
    
    s_thoughts "We've finally gotten past the basics -- communications 101 -- part of the class. Everyone, even non-majors, are caught up to speed. One of our classmates is asking about the course's name from when we signed up."

    show professor neutral at center with dissolve

    nova "Ethnography and the Ethics of Encounter is... a mouthful. You can call it 'the watching class.'"

    s_thoughts "A few laughs. Nova doesn't smile at them."

    nova "Ethnography. The study of people in their natural environments. The researcher enters a community. She watches. She takes notes. She publishes."

    nova "She thinks she's invisible."

    s_thoughts "She looks at the room. Not scanning -- settling."

    nova "She isn't."

    nova "The community changes because she's there. The researcher changes because the community is there. Nothing is observed without being altered."

    s_thoughts "I write that down. I underline it."

    nova "The question for this course isn't whether the observer alters the observed. That's established. Heisenberg figured that out with particles. We're dealing with people."

    nova "The question is: what do you do with the knowledge that you already have?"

    show professor happy at center

    nova "Sit with that. We'll come back to it."

    s_thoughts "I sit with it."

    s_thoughts "I think about Eve's mismatched socks. The green mug. The way she said 'the house is quieter when Charlotte's asleep' like she was giving me something."

    s_thoughts "I think about the file I'm already building."

    s_thoughts "I think about Heisenberg."

    hide professor with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 3: CAMPUS -- WALKING TOGETHER
    ## Eve is different outside the house.
    ## Short sentences but more of them.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_eve fadein 2.0

    s_thoughts "Thursday. I'm heading to the library. Eve is heading somewhere."

    s_thoughts "We leave the house at the same time. Not planned. The porch. The steps. The sidewalk."

    show eve neutral at center with dissolve

    s_thoughts "We fall into step."

    s_thoughts "Eve is different outside the house. Not more talkative -- more present. Like the house has a weight she puts down when she walks through the door."

    s_thoughts "She looks at things. Actually looks."

    e "Dog."

    s "Where?"

    s_thoughts "She points. Across the quad, a corgi in a harness is trying to eat a pinecone while its owner scrolls their phone."

    s "That dog is losing a fight with a pinecone."

    e "The pinecone is winning."

    s_thoughts "A beat. The corners of her mouth do something. Not a smile. The ghost of what a smile would be if it wasn't worried about commitment."

    s_thoughts "We keep walking."

    e "That sign is new."

    s_thoughts "She nods at a bulletin board. Someone has posted a flyer for a 'SILENT DISCO FOR INTROVERTS' with the tagline 'finally, dancing without the part that sucks.'"

    s "I feel personally called out by that."

    e "You dance?"

    s "I have been known to move rhythmically at parties. Under duress."

    e "Hm."

    s_thoughts "We walk."

    s_thoughts "The campus is doing its autumn thing. Orange leaves. People in scarves. A guy with a guitar sitting against a tree, playing something I almost recognize."

    s "You notice things."

    show eve neutral at center

    s_thoughts "Eve looks at me. Direct."

    e "You do too."

    s_thoughts "A beat."

    s_thoughts "We both see each other seeing."

    s_thoughts "It's a small thing. The kind of thing that should be nothing. Two people noticing the same dog, the same sign, the same guitar."

    s_thoughts "But Eve doesn't do this. Eve doesn't walk with people and point at things. Eve is in her room or she's not in the room or she's on the kitchen floor at 2 AM."

    s_thoughts "She's here. Walking. Pointing at dogs."

    s_thoughts "I file it."

    s_thoughts "I catch myself filing it."

    e "This is my turn."

    s "Oh. Yeah."

    e "Bye."

    s "Bye."

    s_thoughts "She goes left. I go straight."
    
    hide eve with dissolve
    
    s_thoughts "Bye. Not goodnight. Not a sound. 'Bye.' Like she was walking with someone and then she wasn't."

    s_thoughts "Like normal people do."

    stop music fadeout 2.0
    
    ## ===========================
    ## SCENE 3.5: "ACROSS THE QUAD"
    ## Sophia spots Eve at a distance. Watches without approaching.
    ## Earns Lila's "you're doing a thing" in Scene 4.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_afternoon fadein 2.0

    s_thoughts "Friday afternoon."

    s_thoughts "I'm between classes. Bench. Coffee. Reading something for Nova that I will retain approximately none of."

    s_thoughts "I look up."

    s_thoughts "Eve is across the quad."

    s_thoughts "She's on a bench. Far enough that she's a shape -- dark hair, red scarf, the grey coat she always wears. She has a book open in her lap."

    s_thoughts "She's not reading."

    s_thoughts "She's looking at something. A tree, maybe. Or the sky past the tree. Or nothing. Her head is tilted at that angle where you can tell someone's not focused on anything in particular -- just existing in a direction."

    s_thoughts "People walk past her. A group of guys with a frisbee. A girl on a skateboard. None of them notice her."

    s_thoughts "Eve sits on a bench the same way Eve sits in a kitchen at 2 AM. Like the space was designed for other people and she's just borrowing it. No elbows on armrests. No spreading out. She takes up exactly the space of one person and not a centimeter more."

    s_thoughts "The scarf is doing the thing where it's half on her shoulder and half not. She reaches up and adjusts it without looking. An automatic gesture. She's done it a thousand times."

    s_thoughts "I watch her adjust her scarf."

    s_thoughts "I watch her turn a page she wasn't reading."

    s_thoughts "I watch her push her glasses up with one finger -- index finger, bridge of the nose, quick."

    s_thoughts "She doesn't know I'm here."

    s_thoughts "I should go over. Say hi. We walked together yesterday. We pointed at dogs. She said 'bye' like a normal person."

    s_thoughts "I don't go over."

    s_thoughts "I just sit here with my cold coffee and my unread reading and I watch Eve Morse exist on a bench across the quad."

    s_thoughts "A leaf falls into her lap. She picks it up. Looks at it. Puts it on the armrest."

    s_thoughts "She didn't throw it away. She put it somewhere."

    s_thoughts "I'm watching a girl look at a leaf."

    s_thoughts "This is what I'm doing with my Friday afternoon."

    s_thoughts "I pack up my bag. I walk the other direction."

    stop music fadeout 2.0

    s_thoughts "I think about the leaf on the armrest all the way to the dining hall."

    ## ===========================
    ## SCENE 4: LILA ON CAMPUS -- "You're doing a thing"
    ## Name the crush. Move on. Seed mental health club.
    ## TIGHT. 8-10 lines of dialogue.
    ## ===========================

    scene bg dininghall with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 1.5

    s_thoughts "I arrive at the dining hall for lunch with Lila."

    show lila happy at center with dissolve

    l "So what's new at the dysfunction house?"

    s "Don't call it that."

    l "You literally named it Bad Decision House."

    s "That's DIFFERENT. That's affectionate."

    l "Uh huh. So who's your current project? Charlotte still doing the thing where she cooks feelings?"

    s "She's fine. Everyone's fine. I've been... I don't know. Hanging out with Eve a bit."

    show lila shocked at center

    s_thoughts "Lila's face does the thing."

    l "You're doing a thing."

    s "What thing?"

    l "The voice. You used the voice."

    s "I don't have a voice."

    l "You do. You have a 'I'm mentioning this person casually because I am SO casual about them' voice. I've heard it about Katie. I've heard it about that girl from Philosophy 201."

    s "I don't--"

    l "The ghost girl. You're crushing on the ghost girl."

    show lila happy at center

    s_thoughts "I open my mouth. I close it."

    s "She's not a ghost girl."

    l "You didn't deny the crushing part."

    s "..."

    l "SOPHIA."

    s "Okay! Maybe. I don't know. We just watch -- we just hang out sometimes. In the kitchen."

    l "At 2 AM? In the kitchen? Romantic."

    s "It's not romantic. It's just... quiet."

    show lila annoyed at center

    l "Babe. You are DOWN BAD."

    s_thoughts "I am maybe a little down bad."

    s "Can we change the subject?"

    l "Fine. I joined a thing."

    s "A thing?"

    l "Mental health club. On campus. I know, I know. Lila Vibe, joining a club that isn't 'being loudly correct in public.'"

    s "I wasn't going to say anything."

    l "You were thinking it. Anyway. It's fine. They have snacks."

    s_thoughts "Lila says 'it's fine' and 'they have snacks' the way someone says 'I'm taking this seriously but I'm not ready to admit that yet.'"

    s "That's cool, Lila."

    l "Whatever. Tell me more about the ghost girl."

    s "I'm not telling you more about the ghost girl."

    l "You just called her the ghost girl."

    s "I hate you."

    show lila laugh at center

    l "You love me. Update me when something happens. WHEN. Not if."

    hide lila with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 5: THE HOUSE -- CHARLOTTE TENSION (Background)
    ## Charlotte's system. Eve doesn't engage.
    ## Brief. Don't spotlight.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Saturday evening."

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte is doing the thing."

    s_thoughts "Dinner for five. The good plates. Something with rosemary that fills the whole downstairs."

    c "Dinner in ten! I made extra because Eve never eats with us and then she's hungry later, so there's a plate in the fridge for whenever."

    s_thoughts "She says this brightly. Like it's not a criticism. Like she's not keeping score."

    show eve neutral at right with dissolve

    s_thoughts "Eve is in the hallway."

    s_thoughts "She heard."

    s_thoughts "Something crosses Eve's face. Not annoyance -- recognition. Like she's seen this script before. A house with a temperature. Someone managing the weather."

    s_thoughts "Eve doesn't say anything. She goes upstairs."

    hide eve with dissolve
    show charlotte smile at left

    c "Is she -- I made her a plate. I always make her a plate."

    s "I know."

    c "Of course she can eat whenever she wants! I just -- it's nicer when everyone's here. That's all."

    s_thoughts "The 'of course' has an edge Charlotte can't hear."

    s_thoughts "I eat Charlotte's dinner. It's excellent. Eve's plate sits in the fridge."

    s_thoughts "At midnight, when I go downstairs for water, the plate is in the sink. Rinsed."

    s_thoughts "She ate alone."

    hide charlotte with dissolve
    stop music fadeout 2.0
    
    ## ===========================
    ## SCENE 5.5: "THE PORCH"
    ## Early morning. Eve through the window. The glass between them.
    ## The yearning is in the restraint.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_morningafter fadein 2.0

    s_thoughts "Sunday. Early. The kind of early where the light is grey and the house hasn't woken up yet."

    s_thoughts "I didn't sleep well. My brain doing the 2 AM thing except it's been doing it since midnight and now it's 6:30 and I've given up."

    s_thoughts "I come downstairs."

    s_thoughts "The kitchen is empty. The counter is clean. Charlotte's chore chart on the fridge. The rosemary from last night's dinner still in the air."

    s_thoughts "I fill the kettle. I'm putting tea in a mug when I see her."

    s_thoughts "Through the window. The kitchen window that looks out onto the porch."

    s_thoughts "Eve."

    s_thoughts "She's sitting on the porch step. The green mug in both hands. The scarf. She's in her pajama pants and the grey coat over them, which is a combination that shouldn't work and does."
    
    s_thoughts "It really does."

    s_thoughts "Her breath is fogging."

    s_thoughts "It's cold out there. Cold enough that you can see her breath in small clouds that appear and disappear. She's not shivering. She's just sitting."

    s_thoughts "She doesn't know I'm here."

    s_thoughts "The window is between us. Glass and a door and three feet of porch and she's right there."

    s_thoughts "She looks up. At what? A bird. A car in the distance. The specific quality of 6:30 AM light. I don't know."

    s_thoughts "This is Eve when nobody's watching."

    s_thoughts "Her hair is unbrushed. She pushes it out of her face with the back of her hand because both hands are full of mug."

    s_thoughts "My kettle clicks off."

    s_thoughts "I could go out there. Open the door. Sit on the other side of the step. Say 'hi' and she'd say 'oh. hi.' and we'd sit with our tea in the cold."

    s_thoughts "I could."

    s_thoughts "I pour water over my tea bag. I sit down at the kitchen table."

    s_thoughts "Inside."

    s_thoughts "I can still see her through the window."

    s_thoughts "The kitchen is warm. The porch is cold. Eve is on the other side of the glass."

    s_thoughts "I drink my tea."

    s_thoughts "She drinks hers."

    s_thoughts "The distance between the kitchen and the porch is a door. I don't open it."

    s_thoughts "The house wakes up around us. Charlotte's alarm upstairs. The pipes doing their thing."

    s_thoughts "Eve stands. She goes inside. Not through the kitchen -- through the front door. I hear it open and close. Her footsteps on the stairs."

    s_thoughts "She never knew I was here."

    s_thoughts "The kitchen is just a kitchen again."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 6: DINING HALL -- EVE SHOWS UP
    ## Eve sits down without announcement.
    ## Brief. The reader clocks it.
    ## ===========================

    scene bg dininghall with Fade(0.8, 0.3, 0.8)

    play music mus_tuesday fadein 1.5

    s_thoughts "Tuesday. Lunch. I'm in the dining hall with my readings and a sandwich that's mostly bread."

    s_thoughts "I'm reading about participant observation. The irony is not lost on me."

    show eve neutral at center with dissolve

    s_thoughts "Eve sits down across from me."

    s_thoughts "No announcement. No 'is this seat taken.' She just puts her tray down and sits."

    e "Hi."

    s "Hi."

    s_thoughts "Eve does not come to the dining hall."

    s_thoughts "Eve eats in her room or she doesn't eat or she appears at midnight to rinse a plate in the dark."

    s_thoughts "Eve is at the dining hall."

    s_thoughts "She has soup. She eats it slowly. She doesn't explain why she's here."

    s_thoughts "I go back to my reading. Or I try. The words keep doing the thing where they're on the page but they're not in my brain because my brain is occupied with: Eve is at the dining hall. Eve sat across from me. Eve is eating soup."

    e "What are you reading?"

    s "Participant observation ethics. For Nova's class."

    e "Is it good?"

    s "It's dense. There's a whole chapter on 'the gaze of the sympathetic outsider' which sounds like a band name."

    s_thoughts "Eve almost does the mouth thing. The not-quite-smile."

    e "Hm."

    s_thoughts "We eat. She finishes her soup. I finish my bread sandwich."

    e "Okay. Bye."

    s "Bye."

    s_thoughts "She picks up her tray. She leaves."

    s_thoughts "Eve came to the dining hall because I was at the dining hall."

    s_thoughts "Don't file it. Don't file it. Don't--"

    s_thoughts "Filed."

    hide eve with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 7: ANOTHER LATE NIGHT -- THE ANIME
    ## The route object is introduced.
    ## Eve: "It's COMPELLINGLY stupid."
    ## Walls down enough to share a screen.
    ## ===========================

    scene bg kitchen night with Fade(0.8, 0.3, 0.8)

    play music mus_2am fadein 3.0

    s_thoughts "Wednesday. 1 AM. The kitchen."

    s_thoughts "This is becoming a thing. I don't want to call it a thing because then it's a thing and things have expectations."

    show eve neutral at center with dissolve

    s_thoughts "Eve is at the table. But she's not reading tonight."

    s_thoughts "She's on her phone. Earbuds in. The screen reflects in her glasses -- bright colors, movement. She doesn't hear me come in."

    s_thoughts "I get water. I sit down."

    s_thoughts "She looks up. Takes one earbud out."

    e "Oh. Hi."

    s "Hi."

    s_thoughts "She pauses whatever she's watching. The screen freezes on what looks like someone mid-punch with hair that defies physics."

    s "What are you watching?"

    s_thoughts "She tilts the phone toward me. Just enough to see."

    s_thoughts "It's an anime. Bright colors, big eyes, a protagonist who appears to be screaming about friendship."

    e "It's stupid."

    s "You've been watching it for an hour."

    s_thoughts "She looks at me. Then at the phone. Then at me."

    e "It's compellingly stupid."

    s_thoughts "Something in her voice. Not defensive. A little embarrassed. A little caught."

    s "What's it about?"

    e "There's a tournament. Everyone has a special move. The protagonist's special move is essentially 'wanting it more.'"

    s "That's the power system? Wanting it?"

    e "Wanting it and screaming. You have to scream."

    s "That's terrible."

    e "That's anime."

    s_thoughts "She says 'anime' with a specific kind of emphasis. The kind that means she's watched a lot of it and she knows exactly what she sounds like and she's doing it anyway."

    s "So why are you watching it at 1 AM in the kitchen?"

    e "Because my room is too quiet and the tournament arc just started and the rival character is about to do the thing."

    s "What thing?"

    e "The thing where the rival character who's been absent for six episodes comes back and is inexplicably stronger and nobody explains how."

    s "That sounds frustrating."

    e "It's the best part."

    s_thoughts "She's sitting up straighter. She's talking faster. Eve, who gives me seven words on a good midnight, is explaining a fictional tournament to me with her hands."

    s_thoughts "I don't think she notices she's doing it."

    s "Can I watch?"

    s_thoughts "She looks at me."

    s_thoughts "Something crosses her face. Not the fear thing from the first night. Something else. Surprise, maybe. That I asked."

    e "It's really stupid."

    s "You've said. Compellingly."

    s_thoughts "She moves her phone so I can see the screen. She puts the earbud back in and offers me the other one."

    s_thoughts "I take it."

    s_thoughts "We're sitting at the kitchen table sharing earbuds and watching an anime about screaming and friendship at 1 AM."

    s_thoughts "Our shoulders don't touch. Almost."
    
    s_thoughts "I think about the almost an almost embarrassing amount."

    s_thoughts "The protagonist is fighting someone. He's losing. He's thinking about his friends. This is apparently how power works."

    s_thoughts "Eve's eyes are on the screen. The light moves across her glasses."

    s_thoughts "I watch the show. I watch Eve watching the show."

    s_thoughts "I stop watching Eve watching the show before she catches me."

    hide eve with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 8: ISABELLA CHECK-IN (Background Thread)
    ## Brief. Isabella is observant. Lumi-phone beat.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)

    play music mus_tuesday fadein 1.5

    s_thoughts "Thursday. The hallway."

    show isabella neutral at center with dissolve

    i "Hey."

    s "Hey."

    i "So you and Eve have been hanging out."

    s_thoughts "Isabella says this the way you say 'the sky is blue.' Conversational. No weight. Lots of weight."

    s "We've just been watching a show."

    show isabella smile at center

    i "Eve doesn't 'just' do anything."

    s "What does that mean?"

    i "It means Eve doesn't 'just.' She decides. She calculates. She shows up somewhere because she decided to show up there."

    i "I've lived with her for a year. She came to the dining hall maybe three times. Total."

    s "..."

    i "I'm not saying anything! I'm just saying she's been -- present. Around you. That's new."

    s_thoughts "Isabella's phone buzzes. She glances at it."

    s_thoughts "That expression. The one where her face softens and she's not performing anything for a second."

    show isabella happy at center

    i "Sorry. One sec."

    s_thoughts "She types something quick. Puts the phone away."

    i "Anyway. Be nice to her."

    s "I'm always nice."

    i "You're always observant. That's different."

    s_thoughts "She says it warmly. Like it's a compliment. Like it might not be."

    hide isabella with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 9: CONVENIENCE STORE
    ## Eve is more relaxed outside the house.
    ## She makes jokes. She doesn't know she's making jokes.
    ## Wall status: Down. The store has no gravity.
    ## ===========================

    scene bg conveniencestore with Fade(0.8, 0.3, 0.8)

    play music mus_eve fadein 2.0

    s_thoughts "Friday. 11 PM."

    s_thoughts "Eve was putting on her jacket in the hallway. I was on the couch. She looked at me."

    s_thoughts "She didn't say 'do you want to come.' She just looked at me. And I stood up."

    show eve neutral at center with dissolve

    s_thoughts "The convenience store at night. Fluorescent lights that make everyone look slightly deceased."

    s_thoughts "Eve picks things up and puts them back. She's been holding the same bag of gummy worms for thirty seconds."

    e "These have gelatin."

    s "You check ingredients on gummy worms?"

    e "I check ingredients on everything."

    s "Even water?"

    e "Water is one ingredient. It's easy to check."

    s_thoughts "She puts the gummy worms back. Picks up a different bag."

    e "These are vegan."

    s "Are you vegan?"

    e "No. I just like knowing."

    s_thoughts "She says that like it explains everything. It kind of does."

    s_thoughts "We wander. The store is small and bright and completely empty except for the cashier, who is reading something on their phone with the intensity of someone who will not be interrupted."

    s_thoughts "Eve stops at the instant noodles."

    e "This brand changed their packaging."

    s "Is that... bad?"

    e "It's wrong. The old one had a drawing of a bowl. This one has a photo. Photos on packaging are a lie. Nobody's noodles look like that."

    s "You have strong opinions about noodle packaging."

    e "Someone has to."

    s_thoughts "I laugh. I actually laugh. Not the polite kind. The kind that comes out before you can organize it."

    s_thoughts "Eve looks at me."

    show eve surprised at center

    s_thoughts "Surprised. Like she said something normal and it turned out to be funny and she's not sure how that happened."

    show eve neutral at center

    s_thoughts "She moves to the next aisle."

    e "Toothpaste."

    s "Is that what you came for?"

    e "I came for toothpaste."

    s "You've been here twenty minutes and you haven't gone near the toothpaste."

    e "I was being thorough."

    s_thoughts "She grabs toothpaste. I grab chips. We stand in front of the cashier, who rings us up without looking away from their phone."

    s_thoughts "Outside. The air is cold. Eve pulls her scarf up."

    s_thoughts "We walk back to the house. The sidewalk is narrow and she walks close."

    s_thoughts "Eve is more relaxed out here. The house has Charlotte's gravity. The store has no gravity. The sidewalk at 11 PM has nothing but cold air and Eve's opinions about noodle packaging."

    s_thoughts "I don't file this one."

    s_thoughts "I just walk."

    hide eve with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 10: THE LIVING ROOM -- EVE GRAVITATES
    ## Ensemble. Eve sits near Sophia.
    ## Everyone notices. Nobody says anything.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)

    play music mus_fivepeople fadein 2.0

    s_thoughts "Sunday."

    s_thoughts "The living room. Everyone is here."

    show charlotte smile at left with dissolve

    s_thoughts "Charlotte on the couch with her laptop, doing something that involves a lot of aggressive typing and occasional sighing."

    show isabella happy at right with dissolve

    s_thoughts "Isabella on the floor with her phone. She's texting someone and doing the thing where she smiles at the screen."

    s_thoughts "Amara in the armchair with a book. She turned a page seven minutes ago. She hasn't turned another one. She's either reading very slowly or thinking very hard."

    s_thoughts "I'm at the table with my Nova readings."

    s_thoughts "Eve comes in."

    show eve neutral at center with dissolve

    s_thoughts "She stands in the doorway for a second. The room full of people. Charlotte's domain."

    s_thoughts "She doesn't usually come in when everyone's here."

    s_thoughts "She sits on the floor. Near my end of the table. Not next to me. Near."

    s_thoughts "She has a book. She opens it."

    s_thoughts "Charlotte looks up from her laptop. Her eyes go from Eve to the floor near my legs to me."

    show charlotte neutral at left

    s_thoughts "She doesn't say anything."

    s_thoughts "Isabella glances over. Her eyes do the same path. Eve. Floor. Me. Her mouth opens. She looks at her phone instead."

    s_thoughts "Amara turns a page."

    s_thoughts "Eve reads. I read. The room is full of people and the smallest distance in it is between Eve's shoulder and my ankle."
    
    s_thoughts "Now I AM thinking about it an embarrassing amount."

    s_thoughts "She sat near me."

    s_thoughts "She could have sat anywhere."

    s_thoughts "She sat near me."

    s_thoughts "I don't say it out loud. I read the same paragraph four times."

    s_thoughts "The sun moves. Someone makes tea."

    s_thoughts "Isabella leaves." 
    
    hide isabella with dissolve   
    
    s_thoughts "Charlotte leaves."

    hide charlotte with dissolve

    s_thoughts "Eve stays."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 11: EVE'S ROOM -- THE FIRST TIME
    ## Act 1 closing beat. Eve invites Sophia in.
    ## The wall is down. Eve is yapping.
    ## The plant on the windowsill.
    ## Eve says something about the rival character
    ## that's accidentally about herself.
    ## Smile: ONCE, maybe. This is the scene.
    ## ===========================

    scene bg kitchen night with Fade(0.8, 0.3, 0.8)

    play music mus_eve fadein 3.0
    
    show eve neutral at center with dissolve

    s_thoughts "Monday night. 12:30 AM."

    s_thoughts "We're two episodes in. My neck is killing me from leaning over Eve's phone on the table."

    s_thoughts "Eve pauses the show."

    s_thoughts "I look up."

    e "This is bad for your neck."

    s "It is bad for my neck."

    e "Posturally, this is a disaster."

    s "Are you an expert on posture now?"

    e "I'm an expert on this table being too low and your neck being at an angle that will cause problems."

    s_thoughts "She's looking at the table. Not at me."

    e "My laptop has a bigger screen."

    s "...Okay?"

    e "It's in my room."

    s_thoughts "A beat."

    s_thoughts "Eve is inviting me to her room."

    s_thoughts "She's framing it as an ergonomic intervention. But she's inviting me to her room."

    e "If you want."

    s_thoughts "If you want. I very much do want. I don't say that out loud."

    s "Yeah. Okay."

    scene bg evebedroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Eve's room."

    s_thoughts "I've been here once. After the party. The open door. The book she wasn't reading."

    s_thoughts "It's the same and it's different."

    s_thoughts "Small. A bed with a dark comforter pulled tight. A desk with a laptop and a stack of books organized by size. The anime posters on the wall -- three of them, framed properly, not just taped up. She framed her anime posters."

    s_thoughts "Books on the shelf. A lot of books. More than a shelf should hold. They're arranged in a way I can't figure out -- not alphabetical, not by size, something else."

    s_thoughts "On the windowsill."

    s_thoughts "A plant."

    s_thoughts "It's small. Some kind of succulent, dark green, in a plain clay pot. It looks healthy. Not thriving -- healthy. Like it's figured out how to exist on whatever attention it gets and it's fine with that."

    s_thoughts "Something living in Eve's room. Something that comes back."

    show eve pj neutral at center with dissolve

    s_thoughts "Eve changes into her pajamas. Oversized pink shirt hanging over the shoulder, plaid pants. It's a cute outfit."

    s_thoughts "She looks smaller in her own space. Not fragile -- contained."

    s_thoughts "There's one chair. She gestures at it."

    e "Chair."

    s_thoughts "She sits on the bed. Opens the laptop. The show picks up where we left off."

    s_thoughts "The screen is bigger. My neck is grateful."

    s_thoughts "The room smells like tea and something else. Laundry. The fabric softener that comes in the purple bottle."

    s_thoughts "We watch."

    s_thoughts "And then Eve starts talking."

    e "See -- that move. That move doesn't make sense. She set it up three episodes ago and then she uses it here and the physics are completely different."

    s "The physics of the special screaming move are inconsistent?"

    e "Yes! The range was established in episode four. She hit someone across a field. Now she can't hit someone standing right there?"
    
    s_thoughts "She scoffs. It's a cute kind of scoff. I file it."

    s "Maybe she's tired?"

    e "She's not tired. She literally just powered up. That was the whole point of the last scene. She did the thing where she remembers her friends and gets stronger."

    s "The friendship power-up."

    e "The friendship power-up! Which is a full restore. The show established this! And now they're just ignoring their own rules because they need the fight to last two more episodes."

    s_thoughts "She's sitting cross-legged on the bed. Her hands are moving. She's gesturing at the laptop screen like she's arguing with it."

    s_thoughts "Eve."

    s_thoughts "Eve who gives me 'oh, hi' and 'mm' and 'goodnight.' Eve who turns pages in silence and wraps her hands around a mug like she's holding something fragile."

    s_thoughts "She's yapping."
    
    s_thoughts "She's actually yapping."

    s_thoughts "I don't think she knows she's doing it."

    s "What about the rival? Where's the rival been?"

    show eve pj flustered at center

    e "Don't get me started on the rival."

    s "I'm getting you started."

    e "The rival is the best character and they keep sidelining her. She disappears for entire arcs." 
    
    e "She comes back and she's clearly gone through something huge and they give her like two lines and then she's in the background again."

    s "That sounds frustrating."

    e "It's criminal. She's carrying the entire thematic weight of the show and they keep putting her in the background because the loud one is easier to write."

    s_thoughts "Eve is leaning forward. Her glasses have slipped down her nose. She pushes them up without stopping."

    e "The rival is the one who actually changes. The protagonist just -- he gets louder. He gets more determined. That's not growth." 
    
    e "But the rival? She starts out alone. She fights alone. She doesn't trust anyone because every time she trusted someone it went wrong."

    s_thoughts "Something."

    s_thoughts "Something in my chest."

    e "And then slowly -- slowly -- she starts letting people in." 
    
    e "Not because she has some big revelation. Because they just kept showing up. They kept being there." 
    
    e "And she ran out of reasons to keep them out."

    show eve pj neutral at center

    s_thoughts "Eve is looking at the screen."

    s_thoughts "She doesn't hear what she just said."

    s_thoughts "I do."

    e "Sorry. I'm -- I talk too much about this."

    s "No. Keep going."

    show eve pj flustered at center

    s_thoughts "She looks at me."

    e "You don't have to humor me."

    s "I'm not humoring you."

    s_thoughts "She searches my face. Whatever she's looking for, she finds it."

    show eve pj smile at center

    s_thoughts "Eve smiles."

    s_thoughts "Not the almost-smile. Not the ghost of a mouth thing. An actual, real, unguarded smile."

    s_thoughts "It's."

    s_thoughts "I don't have a file for this."

    show eve pj neutral at center

    e "Okay. So. Episode seven. The rival comes back and she has a new move and it makes no sense but also it's the coolest thing in the entire show."

    s_thoughts "She starts the next episode."

    s_thoughts "Eve talks through the whole thing. She pauses to explain backstory. She rewinds to show me something I missed. She does voices for the characters -- badly, intentionally badly, committing to the bit."

    s_thoughts "The plant on the windowsill catches the light from the laptop screen."

    s_thoughts "I'm in Eve's room. She invited me in. She's showing me the thing she cares about."

    pause 2.0

    s_thoughts "Something in my chest does a thing."
    
    s_thoughts "An architectural thing."

    s_thoughts "It's not a file. It's not an observation."

    s_thoughts "It's the rival character who fights alone because every time she trusted someone it went wrong."

    s_thoughts "It's Eve in an oversized shirt with her glasses slipping, arguing with a laptop about fictional physics."

    s_thoughts "It's the way she said 'if you want' and meant 'please stay.'"

    s_thoughts "We watch three more episodes. Eve talks about all of them."

    s_thoughts "I don't file any of it."

    s_thoughts "I just stay."

    stop music fadeout 4.0

    ## ===========================
    ## END OF ACT 1: "THE ORBITING"
    ## Eve let Sophia in. The room. The show. The voice.
    ## Act 2 begins with the door opening further --
    ## and the visibility feedback loop starting to run.
    ## ===========================

    jump eve_ch4_act2

## ===========================
## ACT 2: "THE OPENING"
## Scenes 12-23
## The door is open. The feedback loop runs.
## The trust deepens. Then cracks. Then holds.
## ===========================

label eve_ch4_act2:

    ## ===========================
    ## SCENE 12: NOVA'S CLASS -- OBSERVER AND OBSERVED
    ## "What does it mean to see someone who doesn't want to be seen?"
    ## The question stays.
    ## ===========================

    scene bg classroom with Fade(1.0, 2.0, 1.0)

    play music mus_nova fadein 2.0

    s_thoughts "Wednesday. Nova's class."

    s_thoughts "I'm early. I'm never early. I just -- I left the house before Charlotte could ask if I wanted eggs and before I could check if Eve's door was open and before my brain could do the thing it's been doing where every decision involves a girl in mismatched socks."

    show professor neutral at center with dissolve

    nova "Last week we talked about informed consent in fieldwork. Today I want to pull that thread."

    s_thoughts "She writes on the board. One word: GAZE."

    nova "The ethnographer writes about what she sees. But the act of writing changes what she sees. The subject becomes the version of themselves that's being watched."

    nova "This is not abstract."

    s_thoughts "She looks at the room. The way she does -- like she's already seeing more than she's saying."

    nova "You do this to each other. Every day. You walk into a room and someone is there and you become the version of yourself that person expects. You perform for each other constantly."

    nova "The ethnographer's sin isn't that she watches. It's that she pretends she doesn't change anything by watching."

    s_thoughts "I write that down."

    s_thoughts "I think about Eve's room. The anime posters she framed properly. The plant. The way she said 'if you want' and meant something else."

    s_thoughts "I think about the file I'm building. The one I told myself I stopped building."

    show professor happy at center

    nova "So. A question for you."

    nova "What does it mean to see someone who doesn't want to be seen?"

    s_thoughts "The room is quiet."

    nova "Is that care?"

    s_thoughts "A longer pause."

    nova "Or is it invasion?"

    s_thoughts "She's not looking at me. She's looking at the room. But my hands are doing the thing where they grip the pen too hard."

    s_thoughts "I don't answer."

    s_thoughts "Nobody answers."

    nova "Sit with that. Don't resolve it. Resolution is lazy."

    s_thoughts "I sit with it."

    s_thoughts "I sit with it on the walk home. I sit with it on the porch. I sit with it while I'm making tea and while I'm pretending to read and while I'm not-checking if Eve's door is open."

    s_thoughts "It's open."

    s_thoughts "I keep walking."

    hide professor with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 13: THE DOOR
    ## Open. A pattern starts.
    ## Not an invitation. Not a refusal.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)

    play music mus_eve fadein 2.5

    s_thoughts "Thursday."

    s_thoughts "Eve's door is open."

    s_thoughts "I notice it on my way to the bathroom. It's usually closed. Eve's door is always closed the way Amara's is always closed and Charlotte's is always open and Isabella's has stickers on it. The door tells you who lives there."

    s_thoughts "Eve's door is open."

    show eve neutral at center with dissolve

    s_thoughts "She's inside. On her bed. Reading. The laptop is closed. The plant on the windowsill is catching afternoon light."

    s_thoughts "She looks up."

    e "Hey."

    s "Hey."

    s_thoughts "That's it. She goes back to reading. I go to the bathroom."

    s_thoughts "I come back. The door is still open."

    s_thoughts "I go downstairs. I make tea. I come back upstairs."

    s_thoughts "The door is still open."

    hide eve with dissolve
    
    s_thoughts "..."

    s_thoughts "Friday. Eve's door is open."
    
    s_thoughts "..."

    s_thoughts "Saturday. Eve's door is open."

    s_thoughts "She's not always in there. Sometimes the room is empty and the door is open anyway. Just -- open."

    s_thoughts "She said it once, weeks ago. 'I left the door open. I don't usually do that.'"

    s_thoughts "She's doing it on purpose."

    s_thoughts "I don't go in unless she looks up. I don't knock on an open door. I walk past and she's there or she isn't and the door is a door."

    s_thoughts "But I notice."

    s_thoughts "She notices me noticing."

    s_thoughts "Neither of us says anything about it."

    stop music fadeout 3.0
    
    ## ===========================
    ## SCENE 13.5: "TWO MUGS"
    ## Anime session. The mug Eve brings without asking.
    ## Sophia catching feelings in real time.
    ## ===========================

    scene bg evebedroom with Fade(0.8, 0.3, 0.8)

    play music mus_shoulders fadein 2.5

    s_thoughts "Wednesday. Eve's room. Anime night."

    s_thoughts "This is the third time I've been in here. I know the room now. The bed, the desk, the shelf with its secret chronology. The posters. The plant."

    s_thoughts "The plant looks good. A little taller than last week, maybe. Or I'm imagining it. Can succulents grow that fast? I'm not going to google 'succulent growth rate' while sitting in Eve's room."

    show eve pj neutral at center with dissolve

    s_thoughts "Eve is on the bed. Cross-legged, blanket over her knees. The laptop between us."

    s_thoughts "I'm in the chair. The one chair. My chair, I guess. It's become my chair. I don't think about that."

    s_thoughts "The show is on. Training arc. The characters are running up a mountain for reasons that have been explained and are still absurd."

    s_thoughts "Eve leans forward."

    s_thoughts "Her glasses catch the screen light. She's gone from casual lean-back to full analysis mode. I can always tell -- the posture shifts, the shoulders come forward, her eyes get sharper behind the glasses."

    e "See that? The animation changed."

    s "What?"

    e "The running. Look at the frame rate. The first half of the episode was standard. This sequence is hand-drawn. You can tell from the weight."

    s "The weight?"

    e "The way the body moves. Standard animation cheats the physics. Hand-drawn gets the momentum right. Watch her feet."

    s_thoughts "I watch the character's feet. I cannot tell the difference. But Eve's hands are moving -- she's drawing invisible frames in the air between us, tracing the difference in motion."

    s_thoughts "Eve's hands."

    s_thoughts "When she talks about the show, her hands come alive. The rest of her is still -- minimal motion, contained, the Eve I know from the kitchen and the hallway. But her hands do this thing where they're suddenly the loudest part of her."

    s_thoughts "She's tracing an arc. The trajectory of a punch. She's explaining why the impact frames are arranged wrong."

    s_thoughts "I am not following the animation analysis."

    s_thoughts "I am watching Eve's hands."

    e "And there -- see? The after-image. That's the signature of the guest animator. She only does two episodes a season but they're always the best ones."

    s_thoughts "She says 'always the best ones' with the kind of conviction other people reserve for religion."

    s_thoughts "She laughs."

    s_thoughts "Not a big laugh. A small one. Surprised out of her. Like she didn't know it was there."

    s_thoughts "My brain does something."

    s_thoughts "A skip in the track. Eve laughed and my brain went somewhere it wasn't supposed to go and came back and is now pretending that didn't happen."

    s_thoughts "I look at the screen."

    e "I'm going to get tea. Pause?"

    s "Yeah."

    s_thoughts "She gets up. She leaves the room."
    
    hide eve with dissolve

    s_thoughts "I sit in the chair in Eve's room alone."

    s_thoughts "I look at the blanket where she was sitting, still holding the shape of her."

    s_thoughts "I hear her in the kitchen. The kettle. A cabinet."

    s_thoughts "I hear her come back up the stairs."

    s_thoughts "She comes in."

    s_thoughts "She's holding two mugs."

    show eve pj neutral at center with dissolve

    s_thoughts "The green one in her left hand. A blue one in her right."

    s_thoughts "She puts the blue mug on the edge of the desk near my chair."

    e "It's the peppermint tea. I didn't know what you wanted tonight so I guessed."

    s_thoughts "She sits back down. Opens the laptop. Unpauses."

    s_thoughts "She brought me a mug."

    s_thoughts "She went downstairs to get tea and she brought me a mug without asking. She just brought one."

    s_thoughts "She thought about me while she was in the kitchen."

    s_thoughts "She was standing at the counter waiting for the kettle and she reached for a second mug."

    s_thoughts "I pick it up. Peppermint. It's good."

    s "Thanks."

    e "Mm."

    s_thoughts "She's already watching the show. The scene is back. The mountain. The running. The hand-drawn frames she cares about."

    s_thoughts "I hold the mug."

    s_thoughts "The warmth of it."

    s_thoughts "Eve brought me tea."

    s_thoughts "I take a sip and I watch the show and I don't look at her because if I look at her right now my face is going to do something I can't explain."

    hide eve with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 14: AMARA AND EVE -- THE QUIET SCENE
    ## Sophia sees them from the hallway.
    ## Shared silence. No dialogue.
    ## Establishes why Amara has standing later.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Sunday morning."

    s_thoughts "I'm coming downstairs and I stop."

    show amara neutral at left with dissolve
    show eve neutral at right with dissolve

    s_thoughts "Amara is in the armchair. Eve is on the floor near the couch."

    s_thoughts "They're not talking. They're not doing the same thing. Amara has a book. Eve has her phone, screen dark, just -- holding it."

    s_thoughts "They look comfortable."

    s_thoughts "More comfortable than Eve looks with anyone else in this house. More comfortable than Eve looks with me, and I'm the one who gets the anime rants and the gummy worm opinions."

    s_thoughts "Amara turns a page. Eve shifts. Their silence has a texture to it. Like they've been doing this long enough that the silence doesn't need filling."

    s_thoughts "I watch for a second from the hallway."

    s_thoughts "Something about the way Eve's shoulders sit. She's not calculating proximity. She's not managing the distance between herself and another person. She's just -- there."

    s_thoughts "I don't go in."

    s_thoughts "This isn't for me."

    hide amara with dissolve
    hide eve with dissolve

    pause 1.0

    s_thoughts "I go back upstairs."

    ## ===========================
    ## SCENE 15: EVE'S BAD DAY #1
    ## Eve isn't at dinner. Door is closed.
    ## Sophia doesn't knock. Passes the test.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_wrong fadein 2.0

    s_thoughts "Monday."

    s_thoughts "Eve isn't at dinner. This isn't unusual. Eve isn't at dinner the way the sun sets -- it happens. You don't remark on it."

    s_thoughts "But she wasn't in the kitchen at midnight last night either. And she wasn't in the hallway this morning. And her door was closed."

    show charlotte happy at left with dissolve

    c "Has anyone seen Eve?"

    s_thoughts "Charlotte says this while plating pasta. She says it brightly. Like a census question."

    show amara neutral at right with dissolve

    a "Leave her."

    s_thoughts "Two words. Charlotte's hands pause over the plate."

    show charlotte neutral at left

    c "I just -- I made extra--"

    a "Leave her."

    s_thoughts "Charlotte puts the extra plate in the fridge. She doesn't say 'of course.' She doesn't say anything."

    s_thoughts "Amara goes back to her food."

    s_thoughts "I eat dinner. I clear my plate. I go upstairs."

    hide charlotte with dissolve
    hide amara with dissolve

    scene bg hallway with dissolve

    s_thoughts "Eve's door is closed."

    s_thoughts "I stand in front of it."

    s_thoughts "I want to knock. I want to say 'hey, are you okay?' I want to sit on her floor and not say anything and just be in the room because being in the room is what we do now."

    s_thoughts "My hand comes up."

    s_thoughts "I put it back down."

    s_thoughts "Amara said 'leave her.' Amara said it twice. Amara says things once, maybe, if you're lucky. She said it twice."

    s_thoughts "I go to my room."

    s_thoughts "I don't sleep well."

    stop music fadeout 3.0

    ## The next morning.

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Tuesday morning."

    show eve neutral at center with dissolve

    s_thoughts "Eve is in the kitchen. Making tea. The green mug."

    s_thoughts "She looks tired in a way that isn't about sleep. Something under the skin. A weight that settled somewhere in the night and hasn't left."
    
    play music mus_morningafter fadein 2.0

    e "Hey."

    s "Hey."

    s_thoughts "She pours hot water. The kettle clicks off."

    s_thoughts "I don't ask. I don't ask if she's okay. I don't ask where she was. I don't say 'I noticed your door was closed' because that's the kind of sentence that sounds like care and feels like surveillance."

    s_thoughts "I get my own mug. I pour my own water."

    s_thoughts "We stand in the kitchen."

    s_thoughts "Eve drinks her tea. Both hands around the mug."

    s_thoughts "I drink mine."

    e "Thanks."

    s "For?"

    s_thoughts "She looks at the tea. At the counter. At nothing."

    e "Nothing."
    
    e "..."
    
    s "..."
    
    e "Tomorrow?"
    
    s_thoughts "I don't ask what she means."
    
    s "Yeah."
    
    e "...Okay."

    s_thoughts "She takes her tea upstairs."

    hide eve with dissolve

    s_thoughts "I stand in the kitchen."

    s_thoughts "I passed something. I don't know what it was. But I passed it by doing nothing."

    s_thoughts "Filing instinct: Eve has bad days. Eve goes quiet. Eve's door closes. Do not knock."

    s_thoughts "I let the file sit. I don't add to it."
    
    s_thoughts "I'm thinking about tomorrow."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 16: THE ANIME -- TOURNAMENT ARC GETS REAL
    ## The protagonist just sits with the rival.
    ## Deliberate pause. Neither speaks.
    ## ===========================

    scene bg evebedroom with Fade(0.8, 0.3, 0.8)

    play music mus_eve fadein 3.0

    s_thoughts "Tomorrow. Night. Eve's room."

    s_thoughts "This is -- I guess this is a thing now. Wednesday and Saturday nights. Her room. The laptop. The show."

    s_thoughts "She didn't say 'let's make it a schedule.' But it's Wednesday and I'm sitting in Eve's chair and she's on the bed and the anime is playing."

    show eve pj neutral at center with dissolve

    s_thoughts "We're deep into the tournament arc. The silly fights stopped being silly about three episodes ago. The stakes got real. Someone lost badly. Someone else is missing."

    s_thoughts "The rival character -- Eve's favorite, the one who disappears for arcs and comes back stronger, the one Eve won't shut up about -- lost a fight."

    s_thoughts "Not a dramatic loss. Not a power-of-friendship-will-save-me loss. A real one. Outmatched. Outclassed. The kind of fight where you know it's over before it ends and you watch anyway because looking away feels worse."

    s_thoughts "The episode after."

    s_thoughts "The rival is sitting alone. A bench. Night. The city lights behind her."

    s_thoughts "The protagonist finds her."

    s_thoughts "He doesn't give a speech."

    s_thoughts "He doesn't offer to train together."

    s_thoughts "He doesn't say 'we'll get stronger' or 'I believe in you' or any of the things the show has been teaching us to expect."

    s_thoughts "He just sits down."

    s_thoughts "The rival says: 'Why are you here?'"

    s_thoughts "The protagonist says: 'Because you are.'"

    s_thoughts "The camera holds on them. Sitting. The city behind them. Nobody talking."

    s_thoughts "Eve's hand tightens on the blanket."

    s_thoughts "She doesn't know I can see."

    s_thoughts "The episode ends."

    stop music fadeout 2.0

    pause 3.0

    s_thoughts "Silence."

    s_thoughts "The autoplay countdown starts. 5... 4... 3..."

    s_thoughts "Eve reaches over and pauses it."

    pause 2.0

    s_thoughts "The room is quiet. The laptop fan hums. The plant on the windowsill is a dark shape against the window."

    show eve pj neutral at center

    e "That one was good."

    s "Yeah."

    s_thoughts "Her voice is different. Thinner. She's not doing the analysis thing. She's not going to explain the animation choices or the pacing or why the rival's arc is thematically essential."

    e "The part where he just sat there."

    s "Yeah."

    e "He didn't try to fix it."

    s "He just stayed."

    e "Yeah."

    pause 2.0

    s_thoughts "Something in the room."

    s_thoughts "Not heavy. Not light. Present."

    s_thoughts "Eve is looking at the paused screen. The countdown frozen. The rival's face in the last frame, streetlight catching her eyes."

    s_thoughts "I think about the hallway. Monday night. The closed door. My hand coming up and going back down."

    s_thoughts "I think about the tea yesterday. 'Thanks.' 'For?' 'Nothing.'"

    s_thoughts "I think about a protagonist who didn't give a speech. Who just sat in the dirt."

    s_thoughts "I don't say any of this."

    e "Next episode?"

    s "Yeah."

    s_thoughts "She unpauses."

    s_thoughts "We watch the next one. It's lighter. A training montage. Eve makes fun of the physics."

    s_thoughts "But neither of us has forgotten the sitting."

    show eve pj neutral at center
    hide eve with dissolve

    stop music fadeout 3.0
    
    ## ===========================
    ## SCENE 16.5: "THROUGH THE WALL"
    ## No music. Sophia hears Eve through the wall.
    ## Auditory intimacy. Brief.
    ## ===========================

    stop music fadeout 2.0

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Thursday night. My room."

    s_thoughts "I'm on my bed. Book open. Not reading."

    s_thoughts "Through the wall."

    s_thoughts "Eve's room is on the other side of this wall. I didn't think about this when I moved in. Why would I? It's a wall. Walls are walls."

    s_thoughts "I can hear her chair creak."

    s_thoughts "That specific creak. The desk chair. It makes that sound when she leans back -- a small complaint from the mechanism, barely audible. But I know it."

    s_thoughts "I know it."

    s_thoughts "I hear a mug being set down. Two-handed. Gentle. Not the way Charlotte puts a mug down -- decisive, a little loud, already reaching for the next thing. Eve sets a mug down like she's placing it. Like the surface matters."

    s_thoughts "Pages turning. Real pages. A book, not the laptop. I can tell the difference now. Pages have a specific rustle. The laptop has the click-scroll-pause of someone reading on a screen."

    s_thoughts "She's reading."

    s_thoughts "I'm lying on my bed listening to Eve read through a wall."

    s_thoughts "I know the sounds of her room. The chair creak. The mug placement. The pages. The specific silence that means she's thinking versus the silence that means she's just still."

    s_thoughts "When did this happen?"

    s_thoughts "When did the sounds from the next room become something I track? When did Eve's chair creak become a sound I recognize the way I recognize Charlotte's laugh or Isabella's music?"

    s_thoughts "A sound I'd miss."

    s_thoughts "The chair creaks again. She's shifting. Getting up, maybe. Footsteps -- soft, bare feet on the floor. She's walking to the window."

    s_thoughts "I picture her. At the windowsill. Checking the plant. Or just looking out."

    s_thoughts "The wall between us is drywall and plaster. A few inches. I could put my hand on it and she'd be right there on the other side."

    s_thoughts "I don't put my hand on the wall. That would be insane."

    s_thoughts "I want to knock on the wall. The way you knock on a door but smaller. Just: I'm here. You're there. Goodnight."

    s_thoughts "I don't."

    s_thoughts "I turn over. I close my book."

    s_thoughts "Through the wall, the chair creaks one more time."

    s_thoughts "I fall asleep to the sound of Eve existing in the next room."

    ## ===========================
    ## SCENE 17: SOPHIA NOTICES / EVE OFFERS
    ## The visibility feedback loop starts.
    ## Notice -> like -> offer -> receive -> offer more.
    ## The playlist.
    ## ===========================

    scene bg evebedroom with Fade(0.8, 0.3, 0.8)

    play music mus_spacebetween fadein 2.5

    s_thoughts "Saturday."

    s_thoughts "Eve's room. We're not watching the show tonight. We just ended up here."

    s_thoughts "I came upstairs to return a book I borrowed from the shelf."
    
    s_thoughts "Something about ethnographic methods that Eve had, because of course Eve has an ethnography book she never mentioned, filed between a manga volume and a poetry collection in whatever system her shelf uses."

    s_thoughts "I handed it back. She said 'what did you think?' and I said 'the chapter on reciprocal observation was interesting' and she said 'which part?' and now it's an hour later and I'm in the chair and she's on the bed and we're just talking."

    show eve pj neutral at center with dissolve

    s_thoughts "Her room at night. The lamplight makes everything warmer. The anime posters look different in soft light -- less like decor and more like things someone chose because they meant something."

    s_thoughts "I notice her books."

    s "Your shelf. I've been trying to figure out the system."

    show eve pj flustered at center

    s_thoughts "Eve goes still."

    e "What?"

    s "Your books. They're not alphabetical. Not by size. Not by genre -- you've got manga next to theory next to fiction. But there's a pattern."

    s_thoughts "She's looking at me the way she looked at me when I laughed at the noodle packaging thing. Surprised that someone is paying attention to a thing she didn't put on display."

    e "You noticed that?"

    s "Is that okay?"

    s_thoughts "A beat."

    show eve pj neutral at center

    e "...Yeah."

    s_thoughts "She looks at the shelf."

    e "It's chronological. In order of when I read them."

    s "When you read them. Not when you got them."

    e "When I read them. The shelf is -- it's like a timeline. This end is when I was fourteen. That end is last week."

    s_thoughts "She points from left to right. The shelf is a history. Her reading life arranged in the order she lived it."

    s "The manga at the beginning."

    e "I was fourteen."

    s "The poetry in the middle."

    e "I was sixteen. Bad year. Good poems."

    s_thoughts "She says 'bad year, good poems' like it's one thing. Like those always go together."

    s "The ethnography book near the end."

    e "Last month. I found it at a used bookstore. It had someone's notes in the margins."
    
    s_thoughts "Last month. She bought an ethnography book. I'm in an ethnography class. I try really hard not to file it."
    
    s_thoughts "I, of course, fail."

    s "You kept the notes?"

    e "Someone else's thoughts in a book I'm reading. It's like -- I don't know. Company."

    s_thoughts "Something."

    s_thoughts "The way she said 'company.' Not lonely. Not sad. Just -- honest."

    e "Nobody notices the shelf."

    s_thoughts "She says it quietly."

    e "Isabella noticed the posters. Charlotte noticed the plant -- she offered to water it, I said no. Amara noticed the books but she didn't ask."

    e "Nobody noticed the order."

    s_thoughts "I don't know what to do with that."

    s_thoughts "I don't file it. I hold it."

    show eve pj flustered at center

    s_thoughts "Eve looks at me. Then at the shelf. Then at her hands."

    e "Do you want to hear something?"

    s "Yeah."

    s_thoughts "She picks up her phone. Opens something. Holds it out."

    e "This is -- it's a playlist. For bad days."

    s_thoughts "I take her phone. The screen shows a list. Songs I don't recognize. The playlist is called 'floor.' Just the word 'floor.'"

    s "Floor?"

    e "Because I listen to it on the floor. When things are bad I sit on the floor and I listen to this."

    s_thoughts "She's not looking at me. She's looking at the plant."

    e "I've never shown anyone that."

    s_thoughts "My chest does something. Not the architectural thing from before. Something quieter. Like a door opening that I didn't know was a door."

    s_thoughts "I scroll through the playlist. I don't analyze the song choices. I don't file the genres. I just look at it."

    s "Thank you."

    show eve pj neutral at center

    s_thoughts "Eve nods. Takes the phone back."

    e "We can listen to it. If you want."
    
    s_thoughts "I do want."

    s "Okay."
    
    s_thoughts "She gestures to the floor. I pause for a moment as my brain processes. Oh. The floor."
    
    s_thoughts "I stand up, walk to the middle of the room, and sit down on my knees."
    
    s_thoughts "She follows, carefully, like she's considering every step."
    
    s_thoughts "She sits cross-legged across from me, a couple feet away. I find myself wishing she was closer."
    
    e "Ready?"
    
    s "Ready."
    
    s_thoughts "She places the phone in the middle between us. Turns up the volume to max."
    
    s_thoughts "Hits play."
    
    s_thoughts "It's not what I expected. I thought it would be something edgy or emo. Maybe that's me judging a litle too quick."
    
    s_thoughts "Instead it's a wide range. Some pop, some folk. Even a little country. She blushes when it comes on. I smile."
    
    e "It was..."
    
    s_thoughts "She doesn't finish the thought. She looks almost sad as she trails off. I file it."
    
    s "You can learn a lot about people from the music they listen to."
    
    e "What have you learned about me?"
    
    s "That you're not who I thought you were at first."
    
    e "Yeah."
    
    e "..."
    
    e "Neither are you."
    
    s_thoughts "We both sit with that as more songs play. She scooches a little closer to me. Not far, but closer."
    
    s_thoughts "After a while she hits pause."
    
    e "I can send it to you. If you want."
    
    s "I do."
    
    e "Okay."

    s_thoughts "She sends it. My phone buzzes in my pocket."

    s_thoughts "Eve gave me her floor playlist."

    s_thoughts "I noticed her shelf and we listened to her music and she gave me her floor playlist."

    s_thoughts "The loop."

    s_thoughts "I know what's happening. I can see the pattern. I'm watching myself be in a pattern and I can't stop and I don't want to stop."
    
    s_thoughts "I look over at Eve."

    s_thoughts "She moved to the bed with her phone, scrolling through the playlist like she's double-checking all the songs we just listened to."

    s "Maybe we can listen to one of mine sometime."
    
    s "...If you want."
    
    e "..."
    
    e "I do."

    hide eve with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 18: LILA -- "SHE'S DOING IT ON PURPOSE"
    ## Lila names the reciprocity.
    ## Isabella intel. Mental health club drop.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 1.5

    s_thoughts "Monday. The bench with Lila."

    show lila happy at center with dissolve

    l "Status update on the ghost situation."

    s "Please stop calling it that."

    l "I will when you stop looking like that every time I bring her up."

    s "Looking like what?"

    l "Like your face is trying to be casual and your face is BAD at being casual."

    s_thoughts "I am bad at being casual."

    l "So. I have intel."

    s "From who?"

    l "Isabella."

    s "You're getting updates from Isabella?"

    l "Isabella texts me! We're friends! I have friends other than you, Soph. Because I'm a delight."

    s "What did she say?"

    show lila shocked at center

    l "Oh, so NOW you want to know. A second ago it was 'please stop calling it that.'"

    s "Lila."

    l "Okay. So. Isabella says Eve sits near you in a room full of people."

    s "She sat on the floor."

    l "Near YOUR end of a table. In a room with a couch and an armchair and a whole other end of a table. She sat on the FLOOR near YOU."

    s "Maybe she likes that part of the floor."

    show lila annoyed at center

    l "Sophia."

    s "..."

    l "Isabella also says Eve went to the dining hall."

    s "People eat at the dining hall. That's what it's for."

    l "Eve doesn't eat at the dining hall. Eve eats in her room like a Victorian ghost. Isabella said she's gone there maybe three times in a year."

    s_thoughts "I know this. I know all of this. Hearing Lila say it out loud makes it real in a way that my internal monologue doesn't."

    l "And she walks with you. And she watches anime with you in her room. And she does not do these things with other people."

    s "How much has Isabella told you?"

    l "Enough. Here's my thing."

    show lila happy at center

    l "Last time we talked, I said you were crushing on the ghost girl."

    s "Which I still haven't confirmed."

    l "Your face confirmed it three minutes ago. But here's what's new."

    l "She's doing it on PURPOSE."

    s "...What?"

    l "The sitting near you. The dining hall. The walking. The room. She's not accidentally being around you, Soph. She's choosing it. Repeatedly. With intention."

    l "YOU'RE doing it on purpose. SHE'S doing it on purpose. The two of you are doing it on purpose at each other."

    s "That's not how grammar works."

    l "That's not a denial."

    s_thoughts "It's not a denial."

    s "I don't know what she's -- I don't know what any of it means."

    l "It means she likes you."

    s "It means she's comfortable around me. That's different."

    show lila annoyed at center

    l "Is it?"

    s_thoughts "I don't know."

    l "You're the worst. Okay. I gotta go. Club meeting."

    s "The mental health thing?"

    l "Yeah. My advisor said something last week that stuck with me."

    s "What?"

    l "She said sometimes the people who disappear are the ones who need the most space to come back. That you can't chase someone back into a room. You just leave the door open."

    s_thoughts "Lila says this while packing up her bag. She doesn't know she's talking about Eve. She's probably talking about herself, or someone from the club, or nobody specific."

    s_thoughts "Leave the door open."

    s_thoughts "Eve's door is open."

    l "Anyway. Text me when you two stop being stupid."

    show lila laugh at center

    s "We're not being--"

    l "STUPID. Both of you. Aggressively stupid."

    s_thoughts "She waves. She leaves."
    
    hide lila with dissolve

    s_thoughts "I sit on the bench alone."

    s_thoughts "She's doing it on purpose."

    s_thoughts "I'm doing it on purpose."

    s_thoughts "The two of us are doing it on purpose at each other."

    s_thoughts "That's not how grammar works. It might be how this works."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 19: SOPHIA FAILS
    ## She pushes. Eve's walls go up.
    ## The filing instinct costs her something.
    ## The repair is not free.
    ## ===========================

    scene bg evebedroom with Fade(0.8, 0.3, 0.8)

    play music mus_eve fadein 2.0

    s_thoughts "Wednesday. Eve's room."

    s_thoughts "We finished an episode. The credits are rolling. Eve is talking about the side character's arc -- the one whose parents sent her to the academy because they didn't know what else to do with her."

    show eve pj neutral at center with dissolve

    e "It's interesting because they don't play it as tragic. She talks about her parents like they're an event. 'They did what they did.' No anger."

    s "Is that realistic?"

    e "For her? Yeah. Some people don't get angry about it. They just leave."

    s_thoughts "Something in how she says it. Not the anime voice. Not the analysis voice. Something flatter."

    s "Is that--"

    s_thoughts "I stop. I hear myself. I hear the question I'm about to ask."

    s_thoughts "But I don't stop fast enough."

    s "Did you -- is that what it was like?"

    show eve pj neutral at center

    s_thoughts "The room changes."

    s_thoughts "Not dramatically. Not a door slamming. The temperature drops two degrees. Eve's posture shifts. Shoulders up. Jaw set. The openness from thirty seconds ago is gone like it was never there."

    show eve pj annoyed at center

    e "What?"

    s "I didn't mean-- I wasn't trying to--"

    e "You're comparing me to an anime character."

    s "No. That's not what I--"

    e "You heard me say something about the show and you turned it into a question about me."

    s_thoughts "She's right."

    s_thoughts "She's exactly right."

    s "Eve, I'm sorry."

    show eve pj neutral at center

    e "I know."

    s_thoughts "She says 'I know' the way she says 'goodnight.' Closed. Complete. No follow-up invited."

    s_thoughts "The laptop screen shows the credit roll. The music is tinny through the speakers."

    s_thoughts "Eve picks up her phone. Unlocks it. Starts scrolling. She's not scrolling anything. She's putting a wall between us."

    s "Should I go?"

    e "I don't know."

    s_thoughts "That's worse than 'yes.'"

    s_thoughts "I stay in the chair. She stays on the bed. We're three feet apart and the distance is enormous."

    s_thoughts "A minute. Two. The credit music ends. Silence."

    s "I won't do that again."

    e "..."

    s "I mean it. I don't get to -- I don't get to take something you're saying about a show and make it about you. That's not mine to do."

    show eve pj neutral at center

    s_thoughts "Eve is looking at her phone. Not at me."

    e "You do it with everyone."

    s_thoughts "That lands."

    s "I know."

    e "Charlotte. Isabella. You watch people and you find the pattern and you follow it."

    s "I know."

    e "I'm not a pattern."

    s "I know."

    s_thoughts "She puts the phone down."

    show eve pj sad at center

    e "I'm not angry."

    s "Okay."

    e "I just -- I can't do the thing where someone takes something I said and turns it into something about me. I can't -- that's not--"

    s_thoughts "She stops. Her hands are in her lap. She's looking at them."

    e "You should go."

    s "Okay."

    s_thoughts "I stand up. I don't say 'goodnight.' I don't say 'are you okay.' I don't say anything."

    s_thoughts "I walk to the door."

    e "Sophia."

    s_thoughts "I turn."

    show eve pj neutral at center

    e "It's not about you."

    s_thoughts "She says it quietly. Like she's reminding herself as much as telling me."

    s "I know."

    s_thoughts "I close the door behind me."

    stop music fadeout 2.0

    scene bg hallway with dissolve
    
    pause 4.0

    play music mus_wrong fadein 2.0

    s_thoughts "I stand in the hallway."

    s_thoughts "My hands are shaking. Not from fear. From the thing where you just watched yourself do the exact thing you told yourself you wouldn't do."

    s_thoughts "I pushed. I didn't mean to. She was talking about a character and I heard her voice change and the filing instinct fired and I followed it like a hound on a scent and I--"

    s_thoughts "I asked her if the anime character's parents were like hers."

    s_thoughts "I asked Eve Morse if the anime character who was sent away by parents who didn't know what else to do was like her."

    s_thoughts "Stupid."

    s_thoughts "I go to my room. I sit on my bed."

    s_thoughts "Nova's voice: 'What does it mean to see someone who doesn't want to be seen?'"

    s_thoughts "It means you find the thing they were showing you through fiction and you yank it into the real and the fiction was the point. The fiction was safe. The fiction was the room she could talk about it in, and I broke the room."

    s_thoughts "I don't sleep."

    stop music fadeout 3.0

    ## The next day.

    scene bg hallway with Fade(0.8, 0.3, 0.8)

    s_thoughts "Thursday."

    s_thoughts "Eve's door is closed."

    pause 1.5

    s_thoughts "I walk past it. I don't knock."
    
    s_thoughts "..."

    s_thoughts "Friday."
    
    pause 1.5

    s_thoughts "Eve's door is closed."

    s_thoughts "I see her in the kitchen once. She makes tea. She doesn't look at me. She doesn't look away from me. She just -- makes tea."

    s_thoughts "I say 'hey.' She says 'hey.' That's it."
    
    s_thoughts "..."

    s_thoughts "Saturday morning."
    
    pause 2.0

    s_thoughts "Eve's door is open."

    s_thoughts "I walk past. She's at her desk. She looks up."

    show eve neutral at center with dissolve

    e "Hey."

    s "Hey."

    s_thoughts "A beat."

    e "Wednesday?"

    s_thoughts "She's asking about the show. She's asking if we're still watching on Wednesday."

    s_thoughts "The door is open. The question is an open door."

    s "Yeah. Wednesday."

    e "Okay."

    s_thoughts "She goes back to her desk."

    s_thoughts "I go downstairs."

    s_thoughts "Something was tested. Something held. Barely."

    s_thoughts "The repair isn't a conversation. There's no 'I forgive you.' There's no processing. There's just: the door was closed and now it's open and she said 'Wednesday?'"

    s_thoughts "I'll take it."

    hide eve with dissolve

    ## ===========================
    ## SCENE 20: EVE TEXTS SOPHIA
    ## The wall is thinnest through a screen.
    ## Brief. Light. The text that means everything.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Sunday afternoon. My room. I'm reading. Or I'm holding a book and thinking about Eve."

    s_thoughts "My phone buzzes."

    s_thoughts "A screenshot. From the anime. The rival character is standing in the background of a scene with her arms crossed, looking profoundly annoyed."

    s_thoughts "No caption."

    s_thoughts "Then:"

    s_thoughts "'this is you when the coffee maker is broken'"

    s_thoughts "I stare at my phone."

    s_thoughts "Eve texted me."

    s_thoughts "I snap my own face in the front camera -- deliberately choosing the most annoyed expression I can make -- and send it back."

    s_thoughts "'No this is me when the coffee maker is broken.'"

    s_thoughts "Three dots."

    s_thoughts "'worse. you look worse than a cartoon.'"

    s_thoughts "I laugh. I actually laugh alone in my room at a text from Eve Morse."

    s_thoughts "'You're mean.'"

    s_thoughts "'you walked into it'"

    s_thoughts "'I walked into a COMPARISON with an anime character?'"

    s_thoughts "'you should be flattered. she's the best character.'"

    s_thoughts "I read that three times."

    s_thoughts "We text for twenty minutes. Eve texting is different from Eve talking. She uses full sentences. She uses exclamation points. She sends a string of screenshots from the show captioned with increasingly specific observations about the side characters."

    s_thoughts "At one point she sends three consecutive texts about why the tournament bracket is rigged against the rival and it reads like a thesis abstract."

    s_thoughts "'Same time on Wednesday?'"

    s_thoughts "'obviously.'"

    s_thoughts "Eve sent me something. Eve was thinking about me and sent me something."

    s_thoughts "This is what it feels like, isn't it."

    s_thoughts "This is what it is."

    stop music fadeout 2.0
    
    ## ===========================
    ## SCENE 20.5: "THE BED"
    ## THE CHAIR-TO-BED TRANSITION. This is a Moment.
    ## Sophia's hyperawareness of proximity.
    ## Eve's shoulder lean -- half a second, then gone.
    ## ===========================

    scene bg evebedroom with Fade(0.8, 0.3, 0.8)

    play music mus_eve fadein 3.0

    s_thoughts "Wednesday. Eve's room."

    show eve pj neutral at center with dissolve

    s_thoughts "I'm in the chair. Eve's on the bed. The laptop is open between us."

    s_thoughts "The new arc started. The characters are older. Something about the animation changed -- the lines are thinner, the colors more muted. Eve explained the production shift for ten minutes. I understood about forty percent of it and enjoyed a hundred."

    s_thoughts "The problem is the angle."

    s_thoughts "The laptop is on the bed, propped against a pillow. From the chair, I'm watching at an angle that makes the left third of the screen a smear of color."

    s_thoughts "I've been leaning. My neck has an opinion."

    s_thoughts "Eve pauses the show."

    e "You can't see from there."

    s "I can mostly see."

    e "You've been leaning for twenty minutes."

    s "I'm an adaptable person."

    e "You're going to pull something."

    s "My neck is fine."

    e "Your neck is at thirty degrees."

    s_thoughts "She says 'thirty degrees' like she measured it."

    s_thoughts "She shifts the laptop. It doesn't help. The angle is the angle. The chair is where the chair is."

    e "Just -- sit here."

    s_thoughts "She gestures at the bed."

    s_thoughts "Casual. Practical. A furniture rearrangement, not an invitation."

    s_thoughts "Okay."

    s_thoughts "Okay okay okay."

    s "Okay."

    s_thoughts "I get up. I sit on the bed."

    s_thoughts "The mattress dips under me. I'm aware of the physics of this. Two bodies on a surface. The way the springs adjust. The way the blanket shifts."

    s_thoughts "Eve repositions the laptop between us. The screen is straight-on now. Perfect angle."

    e "Better?"

    s "Better."

    s_thoughts "She unpauses."

    s_thoughts "The show plays."

    s_thoughts "I am not watching the show."

    s_thoughts "I'm cataloging."

    s_thoughts "The distance between her knee and mine is -- I don't know. Four inches. Five. Close enough that if either of us shifted, we'd touch. Far enough that we're not touching. The exact distance of plausible deniability."

    s_thoughts "The blanket is big enough for two. She hasn't offered to share it. It's draped over her legs and pooled in the space between us like a border."

    s_thoughts "She's in her pajamas. The oversized shirt. The plaid pants."

    s_thoughts "Her hair is down. It falls down to her shoulder on the side closest to me."

    s_thoughts "I can smell her shampoo."

    s_thoughts "Or her fabric softener. Or her. Some combination of clean laundry and something else. Something warm. I hate that I'm noticing this. I hate that my brain is doing the thing where it catalogs sensory input like a --"

    s_thoughts "Like a --"

    s_thoughts "Her hair is right there."

    e "This fight choreography is better than the first arc."

    s "Mm?"
    
    s_thoughts "I realize we're still watching anime together."

    e "The camera work. They're using longer takes. Less cutting."

    s "Right. Yeah. Totally. Longer takes."

    s_thoughts "I have not been watching the camera work."

    s_thoughts "I have been thinking about the fact that there is warmth coming from her body. Not in a -- it's just. Physics. Bodies are warm. When you sit next to someone on a bed you can feel the warmth of them. That's just how it works."

    s_thoughts "I am trying to make my crush into a science problem."
    
    s_thoughts "...Science has never been my strong suit."

    s_thoughts "The episode continues. A fight. An aftermath. Characters sitting in a field."

    s_thoughts "Eve's analyzing the color theory. Her hands are moving. She's leaning toward the screen."

    s_thoughts "Something happens in the show. Something funny. The loud protagonist does the face."

    s_thoughts "Eve laughs."

    s_thoughts "And she leans."

    s_thoughts "Her hand brushes against mine."

    s_thoughts "For half a second."

    s_thoughts "The weight of her. The warmth of her through two layers of fabric. Her hand against my hand."

    s_thoughts "Half a second."

    show eve pj flustered at center

    s_thoughts "She straightens."

    s_thoughts "She didn't pull away. She just... came back to center. Like a pendulum returning."

    e "Sorry -- the protagonist's face, it's--"

    s "No, it was funny."

    s_thoughts "It was not about the protagonist's face."

    show eve pj neutral at center

    s_thoughts "Eve is looking at the screen."

    s_thoughts "I am looking at the screen."

    s_thoughts "We are both looking at the screen."

    s_thoughts "Neither of us is talking about the hand thing."

    s_thoughts "The episode plays."

    s_thoughts "The plant on the windowsill catches the lamplight."

    s_thoughts "My hand has a memory now. The exact weight. The exact warmth. Half a second that my body is going to store indefinitely, apparently, because my hand won't stop being aware of the inches of air where Eve was."

    s_thoughts "The blanket has crept. It's on my leg now too. The edge of it. She didn't put it there. Gravity did. Or the dip of the mattress. Or the universe, which is apparently conspiring."

    s_thoughts "We watch two more episodes."

    s_thoughts "Our hands don't touch again."

    s_thoughts "Every time she shifts, I know."

    s_thoughts "Every time I shift, she knows."

    s_thoughts "We both know we both know."

    s_thoughts "Nobody says anything."

    s_thoughts "It's the best Wednesday of my life."

    hide eve with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 21: AMARA'S WARNING
    ## "People never mean to."
    ## Short. Sharp. A knife.
    ## ===========================

    scene bg kitchen night with Fade(0.8, 0.3, 0.8)

    s_thoughts "Monday. Late."

    s_thoughts "Everyone else has gone upstairs. I'm in the kitchen cleaning my mug because I'm a responsible adult who cleans her mug sometimes."

    show amara neutral at center with dissolve

    s_thoughts "Amara is at the table. I didn't hear her come in. She does that."

    a "Sophia."

    s_thoughts "I look up."

    s_thoughts "Amara is looking at me. Direct. She's always direct, but this is different. This has weight behind it."

    a "Watch yourself with her."

    s "What?"

    a "Eve. Watch yourself."

    s "I'm not -- we're just--"

    a "Don't."

    s_thoughts "The word lands like a hand on my chest."

    s "What are you--"

    a "Unless you want a problem with me."

    s_thoughts "The kitchen is quiet. Uncomfortably so."

    s_thoughts "Amara doesn't do threats. Amara doesn't do drama. Amara does minimum viable words that carry maximum weight. And she just said 'unless you want a problem with me.'"

    s "I'm not going to hurt her."

    s_thoughts "Amara looks at me."

    s_thoughts "She looks at me the way you look at a weather forecast that says 'sunny' when you can see the clouds."

    a "People never mean to."

    s_thoughts "She picks up her book. She leaves."

    hide amara with dissolve

    s_thoughts "I stand in the kitchen with a clean mug and my hands wet and something cold in my stomach."

    s_thoughts "Amara knows something about Eve. Amara knows something I don't know."

    s_thoughts "Amara sat in a room with Eve and the silence was comfortable because they share something. Something that predates me."

    s_thoughts "And she just told me: if you hurt her, I'm not the quiet one."

    s_thoughts "People never mean to."

    s_thoughts "I dry my hands."

    s_thoughts "I go upstairs."
    
    scene bg hallway night with dissolve

    s_thoughts "Eve's door is open. The light is on. I can hear the faint sound of her music through the gap."

    s_thoughts "I go to my room."
    
    scene bg sophiaroom with dissolve

    s_thoughts "I think about the anime character's parents and the question I asked and Eve's voice when she said 'I'm not a pattern.'"

    s_thoughts "People never mean to."

    s_thoughts "The file I'm building on Eve. The one I told myself I stopped building."

    s_thoughts "I haven't stopped building it."

    pause 1.5

    s_thoughts "I think about whether I can."

    ## ===========================
    ## SCENE 22: THE ALMOST-TOUCH
    ## Eve's room. Anime. Late.
    ## Hands almost touch. She doesn't flinch.
    ## Brief. Embodied. The reader holds their breath.
    ## ===========================

    scene bg evebedroom with Fade(0.8, 0.3, 0.8)

    play music mus_spacebetween fadein 3.0

    s_thoughts "Wednesday."

    s_thoughts "Eve's room. The show. Our ritual."

    show eve pj neutral at center with dissolve

    s_thoughts "We're three episodes in. A good night. Eve is talking again -- not at the level of the first yap session, but close. She paused the show twice to explain a callback I missed. She did the bad voice for the villain. She's relaxed."

    s_thoughts "The repair held. We're here. The door is open."

    s_thoughts "Episode ends. She leans over to the laptop to queue the next one."

    s_thoughts "I reach for the chips at the same time."

    s_thoughts "The bag is between us. On the bed. Where we're both sitting."

    s_thoughts "Our hands."

    pause 1.0

    s_thoughts "Her fingers brush mine."

    s_thoughts "Not a full touch. The edge of her hand against the edge of mine. Knuckle to knuckle."

    s_thoughts "The room stops."

    show eve pj flooshed at center

    s_thoughts "Eve's hand is right there."

    s_thoughts "She doesn't pull away."

    s_thoughts "She doesn't flinch."

    pause 1.5

    s_thoughts "That's the thing. She doesn't flinch."

    s_thoughts "Something about the way she doesn't flinch tells me that flinching was the expected thing. That her body had a plan and the plan was to flinch and she didn't follow the plan."

    s_thoughts "One second. Two."

    s_thoughts "She moves her hand. Slowly. Not snatching it away. Withdrawing. Deliberate."

    show eve pj flustered at center

    s_thoughts "She queues the next episode."

    e "This one is filler."

    s "Okay."

    e "The filler episodes are the good ones."

    s "Okay."

    s_thoughts "We watch filler."

    s_thoughts "I'm not watching filler."

    s_thoughts "I'm thinking about the place where her hand was."

    s_thoughts "The place on my hand where Eve's fingers were for two seconds."

    s_thoughts "She didn't flinch."

    show eve pj neutral at center

    s_thoughts "The episode plays. A beach episode. The characters are being silly. Eve makes a comment about the animation quality."

    s_thoughts "We're pretending the hand thing didn't happen."

    s_thoughts "I'm going to be thinking about the hand thing for the rest of my life."

    hide eve with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 23: EVE'S BAD DAY #2 -- THE HALLWAY
    ## The strongest trust moment in the chapter.
    ## Twenty minutes of sitting.
    ## "For sitting in the hallway instead of coming in."
    ## ===========================

    scene bg hallway with Fade(1.0, 0.5, 1.0)

    play music mus_wrong fadein 3.0

    s_thoughts "A week later."

    s_thoughts "Eve wasn't at the next anime night. Saturday came and she texted 'not tonight.' Two words."
    
    s_thoughts "Then Wednesday. No text. Just a closed door. I didn't knock."

    s_thoughts "...Thursday her door was closed." 
    
    s_thoughts "...Friday her door was closed."

    s_thoughts "Saturday morning I see Charlotte putting a plate of toast outside Eve's door, and Charlotte's face when she puts it down is the face of someone who has done this before and knows it won't be eaten but does it anyway."

    s_thoughts "By Saturday afternoon I am sitting in my room not reading a book."

    s_thoughts "I could text her. I don't."

    s_thoughts "I could knock. I don't."

    s_thoughts "I go downstairs. I come back upstairs. I pass her door."

    scene bg evebedroom with dissolve

    s_thoughts "Open."

    s_thoughts "The door is open."

    show eve pj sad at center with dissolve

    s_thoughts "Eve is in bed. Not sleeping. Not sitting up. Somewhere between. The covers are pulled up. She's on her side, facing the wall."

    s_thoughts "The plant on the windowsill. The posters. The shelf with its chronological history of everything Eve has ever read. The room is the same room I've been in for weeks."

    s_thoughts "Eve is not the same Eve."

    s_thoughts "She's awake. I can tell because her breathing isn't sleep-breathing. It's the kind of breathing where you're aware of the door being open and someone standing in it."

    s "Hey."

    s_thoughts "A long pause."

    e "Hey."

    s_thoughts "Her voice is small. Not small like quiet. Small like far away."

    s "Do you want company?"

    s_thoughts "Another pause. The house is quiet around us. Charlotte is downstairs. Someone is running the tap."

    e "I don't know."

    s_thoughts "I look at her. At the bed. At the room."

    s_thoughts "I think about the sitting. At the bench. The rival and the protagonist. 'Why are you here?' 'Because you are.'"

    s_thoughts "I think about what Lila's advisor said. Leave the door open."

    s_thoughts "I think about the anime character's parents and the question I shouldn't have asked and Eve's voice when she said 'I'm not a pattern' and Amara's voice when she said 'people never mean to.'"

    stop music fadeout 2.0

    s_thoughts "I sit down."

    s_thoughts "On the floor. In the hallway. Outside the door."

    s_thoughts "Not in the room. Not away. In the doorway."

    scene bg hallway with dissolve

    show eve pj sad at center with dissolve

    s_thoughts "I can see Eve's back from here. The shape of her under the blanket. The edge of the bed."

    s_thoughts "I sit."

    pause 2.0

    s_thoughts "A minute."

    s_thoughts "The house moves. Charlotte's footsteps downstairs. A cabinet opening. Closing."

    pause 1.5

    s_thoughts "Five minutes."

    s_thoughts "I lean my head against the doorframe. The floor is hard. My tailbone is going to complain about this."

    s_thoughts "I stay."

    pause 2.0

    s_thoughts "Eve shifts."

    e "Can you just... be here? And not ask me anything?"

    s "Yeah."

    play music mus_fragile fadein 4.0

    s_thoughts "I'm here."

    s_thoughts "I'm not asking anything."

    pause 2.0

    s_thoughts "Ten minutes."

    s_thoughts "The light changes. Afternoon shifting. The hallway gets dimmer."

    s_thoughts "I hear Isabella's door open somewhere. Footsteps. She walks past the end of the hall. She sees me on the floor. She stops."

    s_thoughts "I shake my head. Very slightly."

    s_thoughts "Isabella looks at me. Looks at the open door. She nods once and goes downstairs."
    
    pause 3.0

    s_thoughts "Fifteen minutes."

    s_thoughts "My phone is in my pocket. I don't touch it." 
    
    s_thoughts "The hallway floor has a pattern in the wood I've never noticed. Three knots in a row." 
    
    s_thoughts "Someone carved initials into one of the boards a long time ago. J.K. or J.R. -- I can't tell."

    s_thoughts "The house breathes."

    pause 4.0

    s_thoughts "Twenty minutes."

    s_thoughts "Eve's voice."

    e "Sophia."

    s "Yeah."

    e "Thank you."

    s "I didn't do anything."

    s_thoughts "A pause."

    e "You sat in the hallway instead of coming in."

    pause 2.5

    s_thoughts "That's the distinction."

    s_thoughts "The hallway. Not the room."

    s_thoughts "Present without intrusion. Close without entering."

    s_thoughts "I didn't plan it. I didn't think 'the hallway is the right distance.' I just sat down where my body stopped and my body stopped at the threshold."

    s_thoughts "But Eve felt the distinction. Eve, who calculates proximity like other people calculate tips, who knows exactly where every person in a room is at all times, who has spent her entire life mapping the distance between herself and everyone else... "
    
    s_thoughts "Eve felt me choose the hallway."

    s_thoughts "And it was the right choice."

    s_thoughts "Not because I figured her out. Not because I filed the right data and produced the right behavior."

    s_thoughts "Because I'm learning."

    s_thoughts "I think."

    s_thoughts "I sit in the hallway. Eve is in the bed. The door is open between us."

    s_thoughts "The house moves. People come and go downstairs. The light changes."

    s_thoughts "I don't ask anything."

    s_thoughts "I just stay."

    hide eve with dissolve

    stop music fadeout 4.0

    pause 2.0

    ## ===========================
    ## END OF ACT 2: "THE OPENING"
    ## The door has been open. The loop ran.
    ## Sophia failed and repaired. Eve texted.
    ## Amara drew a line. Hands almost touched.
    ## And Sophia sat in a hallway for twenty minutes
    ## because that's where her body stopped.
    ##
    ## Act 3: "The Edge"
    ## Eve shares layers 1 and 2.
    ## Nova's ethics class recontextualizes everything.
    ## The chapter ends on the threshold.
    ## ===========================

    jump eve_ch4_act3

## ===========================
## ACT 3: "THE EDGE"
## Scenes 24-29
## The intimacy is real and it's scaring both of them.
## Eve shares Layers 1 and 2.
## Nova's class recontextualizes everything.
## The chapter ends on the threshold of something neither of them can name.
## ===========================

label eve_ch4_act3:

    ## ===========================
    ## SCENE 24: EVE TALKS ABOUT HOME -- LAYER 1
    ## The anime triggers it. A character going home.
    ## Eve talks like she's describing weather.
    ## LONG. Let it breathe.
    ## ===========================

    scene bg evebedroom with Fade(2.0, 1.0, 2.0)

    play music mus_eve fadein 3.0

    s_thoughts "Wednesday night. Eve's room."
    
    s_thoughts "Things returned to normal after Saturday. Mostly normal, anyway."

    s_thoughts "We're several episodes in. The tournament is winding down. The fights are over. The aftermath episodes."

    show eve pj neutral at center with dissolve

    s_thoughts "This one is quiet. The protagonist won something but the show doesn't feel like winning. Characters are going home. Visiting families. Getting on trains."

    s_thoughts "The rival character is standing on a platform. She has a bag. She's looking at a ticket."

    s_thoughts "She doesn't get on the train."

    s_thoughts "She stands there while the doors close and the train leaves and the platform is empty and the camera holds on her standing alone with her bag and her ticket to a place she doesn't want to go."

    s_thoughts "The scene ends."

    s_thoughts "Eve pauses the show."

    s_thoughts "She doesn't do the analysis thing. She doesn't say anything about the animation or the pacing or the rival's arc."

    s_thoughts "She's looking at the paused screen."

    pause 2.0

    e "My house was like that."

    s_thoughts "Her voice is flat. The voice you use when you've said something in your head so many times it lost its edges."

    s "Like what?"

    e "Quiet."

    s_thoughts "She pulls the blanket tighter around her shoulders."

    e "The kind where you can hear the clock. The kind where you know what room everyone's in by how the floor sounds."

    s_thoughts "I don't say anything."

    e "My dad had a thing about noise. Not -- he didn't hit. I want to say that first. He didn't hit."

    s_thoughts "The fact that she has to say that first."

    e "He was just loud. And then quiet. And the quiet was worse."

    s_thoughts "She's looking at the laptop screen. At the rival character frozen on the platform."

    e "Cabinets. He'd slam cabinets. The kitchen ones. You'd hear it from upstairs and you'd know."

    s "Know what?"

    e "What kind of night it was going to be."

    s_thoughts "She says this the way you'd say 'it's going to rain.' Just information. Just the forecast."

    pause 1.5

    e "The loud kind. The kind where you flinch at cabinets."

    s_thoughts "She looks at her hands."

    e "I still flinch at cabinets."

    pause 1.0

    s_thoughts "The room is quiet. The laptop fan hums. The plant on the windowsill is a dark shape."

    s_thoughts "I don't say anything. I don't reach for her. I don't say 'I'm sorry' because 'I'm sorry' is a thing you say to make yourself feel better and this isn't about me feeling better."

    e "My mom..."

    s_thoughts "She trails off. Starts again."

    e "She was there. She was in the house. She made dinner. She drove me to school."

    e "She just wasn't..."

    pause 2.0

    e "There."

    s_thoughts "She says both parts like they're the same sentence. 'She was there. She just wasn't there.' It says everything it needs to."

    e "You know those dolls. The ones with the painted-on smile."

    s "..."

    e "She had this thing where she'd ask how my day was and I'd start talking and I could see her eyes go somewhere else."

    e "After a while you stop answering the question."

    s_thoughts "My chest."

    e "You say 'fine' because 'fine' is the right length. Long enough to count as an answer. Short enough that she doesn't have to pretend to listen."

    s_thoughts "I am being very careful not to move."

    pause 1.5

    e "It wasn't -- I had food. I had a bed. I had a school. Nobody was going to call anyone."

    s "Eve."

    e "I'm just saying. From the outside it was fine."

    s "You don't have to justify it."

    show eve pj sad at center

    s_thoughts "She looks at me. Quick. Direct. Then away."

    e "I know."

    s_thoughts "A long pause."

    e "I know I don't have to justify it. I just -- I always do. Every time I talk about it I hear myself explaining why it was bad and the explaining makes it sound like I need permission for it to be bad."

    s_thoughts "That."

    s_thoughts "That sentence."
    
    s_thoughts "It lingers."

    e "The house wasn't bad the way people think when you say 'bad house.' Nobody was screaming all the time. Nobody was drunk. It was just -- always a little wrong."

    e "And you learn to read it. You learn to hear the car pull up and know from the sound of the door. You learn the different silences. Which are good and which are bad. Mom's silence. Dad's silence. They're different. You learn that."

    e "And you get very good at being quiet."
    
    e "...Less noise. Less attention. You know?"

    pause 0.5
    
    s "..."
    
    pause 2.0
    
    s "Yeah." 
    
    pause 2.0
    
    s "I do."
    
    pause 1.5

    s_thoughts "She pulls her knees up. Arms around them. She's smaller."

    e "That's why."

    s_thoughts "She says it flatly. She doesn't explain 'why what' and she doesn't need to."

    e "People think I'm shy. Or mysterious. Or whatever."

    e "I learned... I learned to not be in the room."
    
    s "Eve..."
    
    e "You can be in a room and not be in a room, right?" 
    
    e "You just make yourself smaller and smaller until..." 
    
    s_thoughts "She takes a breath. Gently. Like the air is thin but it's not."
    
    e "Until the room forgets you're there."
    
    s "I don't forget."
    
    e "I know."

    show eve pj neutral at center

    s_thoughts "The laptop screen has gone dark. Sleep mode. The room is just lamplight now."

    s_thoughts "Eve is looking at the wall."

    e "I came here to put space between us. Between me and them." 
    
    e "I told my mom I'd come home when I'm ready, but..."

    e "I don't know what ready means."

    s "What did she say?"

    e "She said 'of course, sweetie.'"

    s_thoughts "I can hear it in her voice. It's neither of course nor sweet."

    e "She was relieved, I think." 
    
    e "One less person in the house."
    
    e "She... was relieved."
    
    s_thoughts "Her voice cracks so subtly that if I wasn't paying laser attention I'd miss it."
    
    s_thoughts "I'm not sure what to say."

    pause 2.0

    s_thoughts "The room holds it."

    s_thoughts "I don't file any of this. I don't add it to the pattern. I don't think about what it means for the things Eve does or doesn't do."

    pause 1.5

    e "I don't -- I don't know why I'm telling you this."

    s "You don't have to know why."

    s_thoughts "She looks at me."

    show eve pj flustered at center

    e "You're not doing the thing."

    s "What thing?"

    e "The face. The one where someone tells you something sad and they do the face. The head tilt. The 'oh no, I'm so sorry.'"

    s_thoughts "Am I not doing the face?"

    e "You're just sitting there."

    s "Yeah."

    e "That's -- yeah."

    show eve pj neutral at center

    s_thoughts "She unfolds a little. Not fully. But the knees come down."

    e "The calls are short now. I call every other Sunday. We talk about weather and classes. She asks if I'm eating. I say yes. She says 'that's good, sweetie.'"
    
    s_thoughts "Neither good nor sweet."

    e "We hang up and it's like I just talked to a stranger."
    
    s "A stranger who knows your birthday."
    
    e "...Yeah. That's right."

    s_thoughts "I sit with it."

    s_thoughts "I sit with Eve describing her family the way a geologist describes a rock formation. Here is the fault line. Here is where the pressure built. Here is where nothing happened, which was the worst part."

    pause 2.0

    e "I don't want you to feel sorry for me."

    s "I don't."

    e "..."

    s "I mean -- I feel a lot of things. But sorry isn't the main one."

    e "What's the main one?"

    s_thoughts "I think about it."

    s "Gladness."

    e "What?"
    
    s_thoughts "I recognize the strangeness of what I just said. But it feels right nonetheless."

    s "You're... here."
    
    e "I'm here."
    
    s "In this house."
    
    e "Yeah."
    
    s "With us. With... me."
    
    s_thoughts "I waver on the 'me.'"
    
    show eve pj flooshed at center
    
    e "With you."
    
    s "With me."
    
    pause 2.0
    
    s "So no. I don't feel sorry."

    s "Because I'm not sorry you're here."

    s_thoughts "Eve looks at me."

    s_thoughts "For a long time."

    show eve pj neutral at center

    s_thoughts "Finally she reaches over and wakes the laptop up. The anime is still paused on the rival character standing on the platform."

    e "She doesn't go home."

    s "No."

    e "Good."

    s_thoughts "She closes the laptop."

    e "I'm tired."

    s "Okay."

    s_thoughts "I stand up. I go to the door."

    e "Sophia."

    s "Yeah?"

    e "Same thing as the hallway."

    s_thoughts "I look at her."

    s "What?"

    e "You just sat there. You didn't -- you just sat there."

    s "Yeah."

    e "...Goodnight."

    s "Goodnight, Eve."

    hide eve with dissolve

    stop music fadeout 4.0

    pause 2.0

    s_thoughts "I close the door softly."

    s_thoughts "I go to my room."
    
    scene bg sophiaroom with dissolve
    
    pause 1.5

    s_thoughts "I sit on my bed with everything she told me."

    s_thoughts "I just held it."

    s_thoughts "I am holding it."

    pause 1.5

    s_thoughts "This isn't a file."

    s_thoughts "This is Eve."

    ## ===========================
    ## SCENE 25: CHARLOTTE DOES THE THING
    ## Charlotte brings something to Eve's door.
    ## Eve's walls go up at Charlotte-level.
    ## Brief. No resolution. The tension just exists.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)

    play music mus_tuesday fadein 2.0

    s_thoughts "Thursday morning."

    s_thoughts "I'm coming out of the bathroom and Charlotte is in the hallway. She has a plate. Toast with jam. Cut diagonally."

    show charlotte happy at center with dissolve

    s_thoughts "She knocks on Eve's door. Light. Musical. The Charlotte knock."

    c "Eve? I made toast. There's extra. I just thought -- in case you didn't eat yet."

    s_thoughts "I hear movement inside. The bed shifting."

    s_thoughts "The door opens."

    hide charlotte

    show charlotte happy at left with move
    show eve pj neutral at right with dissolve

    s_thoughts "Eve is in her pajamas. Her hair is pushed to one side. She looks at Charlotte."

    s_thoughts "She looks at the toast."

    s_thoughts "Something crosses Eve's face."

    show eve pj annoyed at right

    s_thoughts "Not at Charlotte. At the toast. At the brightness of the offer. At the specific quality of someone showing up at your door with food and a smile and the unspoken message that they noticed you didn't come down."

    s_thoughts "Eve told me about everything last night. About her house."

    s_thoughts "This morning Charlotte brought her toast and Eve is looking at the toast like it's a grenade."

    s_thoughts "Charlotte doesn't know any of it. Charlotte is being Charlotte."

    show eve pj neutral at right

    e "Thanks."

    s_thoughts "She takes the plate. One word. She steps back."

    c "Of course! I just -- I know you don't always eat in the mornings, so--"

    e "Thanks, Charlotte."

    s_thoughts "She closes the door."

    hide eve with dissolve

    show charlotte neutral at left

    s_thoughts "Charlotte stands in the hallway with her hands empty."

    s_thoughts "Her face does this thing. A flicker. Confusion, hurt, recovery -- all in a second. The brightness reassembles."

    show charlotte smile at left

    c "Okay! Well. There's more downstairs if anyone wants."

    s_thoughts "She turns and sees me."

    c "Oh! Sophia. Toast?"

    s "I'm good. Thanks, Charlotte."

    c "Of course!"

    s_thoughts "She goes downstairs."

    hide charlotte with dissolve

    s_thoughts "I stand in the hallway."

    s_thoughts "Eve's door. Closed."

    s_thoughts "Eve's trust in me is not Eve 'getting better.' It's not Eve opening up to the world. It's Eve choosing one person to be visible to. To me." 
    
    s_thoughts "And Charlotte's warmth, it's -- genuine, loving, and the exact thing Eve won't, or can't, receive."

    s_thoughts "That's not Charlotte's fault."

    s_thoughts "It's just..."
    
    s_thoughts "..."

    stop music fadeout 2.0
    
    ## ===========================
    ## SCENE 25.5: "THE KITCHEN WITHOUT HER"
    ## The gap between Layers 1 and 2.
    ## Eve's door is closed. The absence is heavy.
    ## Yearning without a category.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)

    s_thoughts "A few days pass."

    s_thoughts "Eve's door isn't closed the bad-day way. It's just closed. She's in class. She's studying. She's doing whatever Eve does when Eve isn't with me."

    s_thoughts "I should be fine with this. I am a person who has a life outside of Eve Morse's proximity."

    s_thoughts "I go to class. I take notes. I write things down that I will later read and not recognize."

    s_thoughts "I eat lunch in the dining hall. The seat across from me is empty."

    s_thoughts "It's just a seat."

    s_thoughts "I go to the library. I study. I read three pages of Nova's reading and retain two sentences."

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "I go home."

    s_thoughts "The house is the house. Charlotte made something. Isabella's music from upstairs."

    s_thoughts "I eat dinner."

    s_thoughts "I go to my room."
    
    scene bg sophiaroom with dissolve

    s_thoughts "I look at the floor playlist on my phone. My thumb hovers over the play button."

    s_thoughts "I don't press it."

    s_thoughts "It's hers. It's the thing she gave me. Listening to it without her feels like reading someone's journal when they're not in the room."

    s_thoughts "..."

    s_thoughts "Midnight."

    s_thoughts "I go downstairs."

    s_thoughts "The kitchen light is off."

    s_thoughts "I turn it on."
    
    scene bg kitchen night with dissolve
    
    play music mus_morningafter fadein 2.0

    s_thoughts "The table. The counter. The tap. The fridge humming. Everything in its place."

    s_thoughts "I fill a glass of water."

    s_thoughts "The green mug is not in the drying rack."

    s_thoughts "It's a mug. Its presence or absence in the drying rack means exactly nothing. It means Eve washed it and put it away. Or it means she's using it. Or it means it's in her room waiting to be cleaned."

    s_thoughts "It's a mug."

    s_thoughts "The kitchen at midnight without Eve in it is just a kitchen."

    s_thoughts "That's the problem."

    s_thoughts "I know what this kitchen is with her in it. I know the quality of the silence when she's here. The specific way the fridge sounds when there's someone else hearing it. The way the space between two people at 2 AM is different from any other space."

    s_thoughts "The kitchen is a kitchen and I want it to be more than a kitchen and it's only more than a kitchen when she's here."

    s_thoughts "I drink my water. I rinse the glass."

    s_thoughts "I think about her hands. On the blanket. On the mug. In the air, tracing invisible animation frames."

    s_thoughts "I think about the lean. Hands brushing for half a second. The feeling of her."

    s_thoughts "I don't know what I want."

    s_thoughts "Not -- I mean. I know what I want in the general sense. In the Lila-would-say-you're-down-bad sense."

    s_thoughts "But the specific want. The thing I'd ask for if I could ask for anything."

    s_thoughts "I want Eve to be in the room."

    s_thoughts "Not doing anything. Not talking. Not watching the show. Just -- in the room. I want the weight of her in the next chair."

    s_thoughts "I go back upstairs."

    scene bg hallway night with dissolve

    s_thoughts "Eve's door is closed."

    s_thoughts "No light underneath."

    s_thoughts "I go to bed."

    s_thoughts "..."

    s_thoughts "Friday morning."

    s_thoughts "Eve's door is open."

    s_thoughts "Just open. The way it's been. The way it means what it means."

    s_thoughts "I keep walking. I go to the kitchen."
    
    scene bg kitchen with dissolve

    s_thoughts "The green mug is in the drying rack."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 26: EVE TALKS ABOUT HOME -- LAYER 2
    ## "Something happened because nobody was watching."
    ## The sentences get shorter. She starts things
    ## and doesn't finish them.
    ## LONG. Let it sit.
    ## ===========================

    scene bg evebedroom with Fade(1.0, 0.5, 1.0)

    play music mus_2am fadein 3.0

    s_thoughts "It's Saturday. Anime night."

    s_thoughts "Eve's room. But the anime is off. She didn't open it tonight."

    s_thoughts "We're just sitting. She's on the bed. I'm in the chair. The lamp is on. Her face is bathed in warm light."
    
    s_thoughts "She's really pretty like this. I don't say so."

    show eve pj neutral at center with dissolve

    s_thoughts "We've been talking about nothing. A class she's in. A paper that's due. She mentioned the convenience store changed the noodle packaging again and I laughed and she almost smiled."

    s_thoughts "Then she goes quiet."

    s_thoughts "Not the comfortable quiet. Not the Eve-is-done-talking quiet."

    s_thoughts "A different quiet."

    pause 2.0

    e "The house wasn't just quiet."

    s_thoughts "I don't move."

    e "I told you about... About my parents."

    s "Yeah."

    e "That's not -- that's the frame. That's the shape, I guess." 
    
    e "But inside the frame..."

    s_thoughts "She stops."

    pause 1.5

    e "Nobody was watching."

    s_thoughts "She says it simply. Like a fact."

    e "That's what I mean when I say the house was quiet. Not just the sound. The -- nobody was watching."
    
    s "Watching what?"
    
    e "Watching... caring. Caring enough to watch. What was happening. With me."
    
    e "...Me."
    
    s "I see."

    e "Sophia."
    
    s "Mm?"

    e "When nobody's watching..."

    s_thoughts "She pulls the blanket tighter."

    e "Things... happen."

    pause 2.0

    stop music fadeout 3.0

    s_thoughts "The room is very quiet."

    e "Not the things people think when I say that."

    s_thoughts "She looks at me. Quick. Then away."

    e "Not -- it's not -- I need you to not make a face."

    s "I'm not making a face."

    e "You're going to want to."

    s "Okay."

    s_thoughts "My hands are in my lap. I press them against my knees."

    e "It was more like..."

    s_thoughts "She starts. Stops."

    show eve pj sad at center

    e "The house... it... I left for more reasons than just my parents."
    
    s "Oh? But I thought--"
    
    e "I know. But."
    
    s_thoughts "I notice tears in her eyes."

    e "Nobody was watching, you know?"
    
    e "..."
    
    e "Nobody saw."
    
    e "Nobody but me."

    pause 2.5

    s_thoughts "She's not looking at me. She's looking at the plant."

    e "I... can't tell you what."
    
    s "That's okay--"
    
    e "Not yet. Maybe not ever. I... I don't know."

    e "I hate that house."
    
    s "That's--"
    
    e "That's why I had to leave."
    
    e "That's why I'm here."

    s_thoughts "I'm feeling... something heavy and very still. Like a stone dropped into water but the water doesn't move."

    play music mus_mourning fadein 3.0

    e "You learn things after something happens."
    
    s "..."

    s_thoughts "Her voice is thinner now. The sentences are shorter."

    e "How to hear sounds. All sounds."

    s "R-Right."

    e "You know how some people are afraid of the dark?"

    s "Yeah."

    e "I'm..." 
    
    s_thoughts "She wipes her eyes."
    
    e "I'm afraid of certain rooms."

    pause 1.5

    s_thoughts "I don't move. The stillness is loud."

    e "Not this room. This room is mine." 
    
    e "But -- rooms at night." 
    
    e "Rooms where the door doesn't lock." 
    
    e "Rooms where the light switch is on the wrong side."
    
    s "...Bad rooms."
    
    e "Yeah. Bad."
    
    s_thoughts "She doesn't elaborate. I don't ask her to."

    e "I learned to be small."

    s_thoughts "She says it the way she said 'fine' earlier. Like a fact about the world."

    e "I learned to read silence."
    
    s "To read it?"
    
    e "Silence is loud. It's so loud. Most people don't get that."
    
    s "But you hear it."
    
    e "I do."
    
    e "I listen to every silence and it's so loud, Sophia."
    
    e "There's so much to hear when it's quiet."

    e "You learn to be small and you learn to hear quiet and you learn that being seen is just--"

    s_thoughts "She stops, abruptly. She doesn't finish."

    pause 2.0

    s_thoughts "The room holds it."

    e "...I don't talk about this."

    s "I know."

    e "I'm talking about it."

    s "I know."

    pause 1.5

    e "I don't know why."

    s_thoughts "I do. I think I do. I think it's the hallway and the not-asking and the bench scene and the floor playlist and  weeks of Wednesday and Saturday nights."

    s_thoughts "But I don't say that."

    s "You don't have to know why."

    e "You said that last time."

    s "It's still true."

    show eve pj neutral at center

    s_thoughts "She puts her chin on her knees."

    s_thoughts "We sit."

    s_thoughts "The music from someone's room bleeds through the wall. Tinny. Far away. Isabella, probably."

    s_thoughts "Eve breathes."

    e "You know... You've, you've noticed... how I disappear."

    s "I have."

    e "It's not -- I didn't decide to be like this. I didn't wake up one day and think 'I'm going to be mysterious.' I just..."

    e "You learn. You learn how to be safe when nothing feels safe."

    s_thoughts "I am holding this very carefully."

    e "Charlotte keeps trying to make me bigger."  
    
    s "Charlotte doesn't understand any of this."
    
    e "No."
    
    e "She wants me to fill a space."

    e "I don't know how to fill a space. I don't want to."

    s_thoughts "I think about the other morning with Charlotte."

    e "It's not her fault."

    s "I know."

    e "I know she's trying. I know it's love. Or whatever it is with Charlotte. I just -- her warmth feels like..."

    s_thoughts "She searches for the word."

    e "A test. It feels like a test." 
    
    e "Like if I accept it I'm agreeing that everything is okay and I don't know if everything is okay."
    
    e "..."
    
    e "I don't."

    pause 1.5

    s_thoughts "I watch Eve closely. Her eyes are dry again. I think mine are a little wet."

    s_thoughts "I'm sure she notices."

    s_thoughts "The music through the wall stops. Isabella's gone to bed."

    e "Are you okay?"

    s_thoughts "I blink."

    s "What?"

    e "I just -- I dumped a lot on you. Are you okay?"

    s_thoughts "She's the one asking if I'M okay."

    s "I'm okay."

    e "You don't have to be."

    s "I'm okay, Eve."

    show eve pj neutral at center

    e "Okay."

    s_thoughts "A beat."

    e "I don't want to watch anything tonight."

    s "That's fine."

    e "Can you just -- can we just sit here for a bit?"

    s "Yeah."

    pause 2.0

    s_thoughts "We sit."

    s_thoughts "It's very still."

    s_thoughts "Eve's breathing evens out. Not sleeping. Just... settling."

    s_thoughts "I don't leave until she tells me to."

    s_thoughts "She doesn't tell me to."

    s_thoughts "I stay until she falls asleep."

    s_thoughts "I close the door very quietly."
    
    s_thoughts "For the first time in my life, I hear the silence."

    hide eve with dissolve

    stop music fadeout 4.0
    
    scene bg sophiaroom with dissolve

    pause 2.0

    s_thoughts "In my room, I sit on the floor."

    s_thoughts "Eve's floor playlist is still on my phone."

    s_thoughts "I don't play it."

    s_thoughts "I just sit."

    ## ===========================
    ## SCENE 27: NOVA'S CLASS -- THE ETHICS QUESTION
    ## Sophia speaks up. The question lands.
    ## Nova recognizes something.
    ## A real classroom scene.
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)

    play music mus_nova fadein 2.0

    s_thoughts "Friday. Nova's class."

    s_thoughts "I'm not early this time. I'm not late. I'm just here."

    s_thoughts "The room smells like coffee and dry-erase markers. Someone near the window has a smoothie that's too loud."

    show professor neutral at center with dissolve

    nova "Today I want to talk about what happens when the ethnographer sees something the village didn't want seen."

    s_thoughts "I sit up."

    nova "The scenario. You're embedded in a community. You've been there for months. You eat with them. You laugh with them. They trust you."

    nova "And in the course of that trust, you see something. Not something they showed you. Something that exists in the gaps between what they show you."

    s_thoughts "She's pacing. The slow Nova pace. Three steps, turn, three steps."

    nova "The question isn't whether you saw it. You did. The question is what you do with it."

    nova "Option one. You write about it. You publish. The village reads the book and sees themselves through your eyes -- including the thing they weren't looking at."

    nova "Option two. You don't write about it. You keep it. You know something about them that they didn't choose to share."

    nova "Which is worse?"

    s_thoughts "The room murmurs. Someone says 'the first one, obviously.' Someone else disagrees."

    nova "Arguments. Go."

    s_thoughts "A guy in the second row talks about informed consent. A girl near the back talks about the violence of representation. Lila makes a joke that falls flat. Someone uses the word 'epistemic' and Nova's mouth does a thing."

    nova "Good. More. What if the thing the ethnographer saw was something the village had decided not to look at?"

    s_thoughts "The room gets quieter."

    nova "Not a secret. Not something hidden. Something known and unexamined. A pattern everyone can see and nobody discusses."

    s_thoughts "Eve is on my mind. Obviously."

    s_thoughts "My hand goes up."

    s_thoughts "I don't decide to raise my hand. My hand goes up."

    nova "Ms. Bell."

    s_thoughts "The room is looking at me."

    s "It's like -- the village knows. On some level, everyone knows. But they've built their life around not looking at it directly. And the ethnographer walks in and she's an outsider so she doesn't know the rules about where you don't look."

    s_thoughts "I hear my own voice and I'm not sure if I'm talking about ethnography."

    show professor happy at center

    s_thoughts "Nova is looking at me."

    s "And she writes it down. Because that's what ethnographers do. She writes it down and suddenly the thing that everyone was not-looking-at is on a page. In words. Named."

    s "Is that always violence?"

    s_thoughts "The room is quiet."

    nova "Say more."

    s "Because -- naming something makes it real in a different way. The village was surviving by not naming it. Maybe the not-naming was the only way they could live there." 
    
    s "Then the ethnographer comes in and names it and now it's real in the room and everyone has to look at it."

    s "And maybe -- maybe the ethnographer thinks she's helping." 
    
    s "She thinks naming it is the first step to fixing it. But what if the village didn't ask to be fixed?" 
    
    s "What if the not-looking was the thing keeping them alive?"

    pause 1.5

    s_thoughts "Nova is looking at me for a long time."

    s_thoughts "The look of someone who heard a student ask a question they didn't learn from a textbook."

    show professor neutral at center

    nova "That's the question this course exists to not answer."

    s_thoughts "A pause."

    nova "But I want to push on it. Because there's a third option nobody has named."

    nova "The ethnographer sees the thing. She doesn't write about it. She doesn't name it. But she stays."

    nova "She stays in the village knowing what she knows, and she lets that knowledge change how she moves through the space. She's more careful. She's more present." 
    
    nova "She doesn't demand that anyone look at the thing."

    nova "She just stops pretending she can't see it."

    s_thoughts "I write that down."

    s_thoughts "I underline it."

    s_thoughts "I underline it again."

    nova "Is that better? Is that worse? Is that its own kind of violence -- holding someone's truth without their knowledge?"

    nova "I don't know. That's not a pedagogical dodge. I genuinely don't know."

    s_thoughts "The class moves on. Someone asks about the reading. The smoothie person asks about the midterm."

    s_thoughts "I sit in my chair."

    s_thoughts "'She lets that knowledge change how she moves through a space.'"

    hide professor with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 28: AN ENSEMBLE EVENING -- EVE IS PRESENT
    ## Warm. Brief. The calm before the edge.
    ## Eve exists in the room without performing.
    ## Eve smile: once. Earned. Brief.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)

    play music mus_fivepeople fadein 2.0

    s_thoughts "The evening after class."

    s_thoughts "The living room. The house doing the thing where it's just a house."

    s_thoughts "Charlotte is in the kitchen -- the sounds drift in. Something with garlic. She's humming."

    show isabella happy at left with dissolve

    s_thoughts "Isabella on the couch with her laptop. She's got one earbud in and she's doing the thing where she talks to herself while she types."
    
    show amara neutral at right with dissolve

    s_thoughts "Amara is in the armchair. Reading. She turned one page in the last twenty minutes."

    s_thoughts "I'm at the table pretending to study."

    s_thoughts "Keyword: pretending."

    show eve neutral at center with dissolve

    s_thoughts "Eve is here."

    s_thoughts "Not near me this time. She's on the other end of the couch from Isabella. She has a book. She's actually reading it -- I can tell because her eyes are moving, which is more than I can say for Amara."

    s_thoughts "She's just here."

    i "Does anyone want tea? I'm making tea."

    s_thoughts "Isabella unfolds herself from the couch."

    s "Sure."

    e "The green one."

    i "The green one. Eve has a favorite. The world is changing."

    show eve neutral at center

    s_thoughts "Eve doesn't look up from her book."

    e "I've always had a favorite. You just never asked."

    show isabella sad at left

    i "..."

    i "That's... weirdly devastating."

    e "It's just tea."

    show isabella happy at left

    i "It's not 'just tea.' You just told me you've had an inner life about tea this whole time and I missed it."

    s_thoughts "From the kitchen:"

    c "The green one is on the second shelf! Behind the chamomile!"

    s_thoughts "Charlotte, of course, knows where every tea is."
    
    hide isabella with dissolve

    s_thoughts "Isabella goes to the kitchen. I hear her and Charlotte talking. Something about whether honey counts as sugar."

    s_thoughts "Eve reads."

    s_thoughts "I watch Eve read."

    s_thoughts "Her shoulders are down. Her jaw is loose. She turns a page."

    s_thoughts "She looks like a person."

    s_thoughts "That sounds like nothing. But it's everything."
    
    show isabella happy at left with dissolve

    s_thoughts "Isabella comes back with mugs. Eve takes the green one without looking up. Says:"

    show eve smile at center

    e "Thanks."

    s_thoughts "Isabella puts a mug in front of me. One by the armchair for Amara, who takes it without comment."

    s_thoughts "Charlotte comes in with a plate of something -- crackers, cheese, the little tomatoes she always buys."

    s_thoughts "She puts it on the coffee table."

    c "Snack plate! Because we're civilized."

    s_thoughts "Eve reaches over and takes a tomato."

    s_thoughts "Charlotte sees this. Her whole face lights up. She doesn't say anything. She just -- lights up."

    show eve neutral at center

    s_thoughts "Eve eats the tomato. Goes back to her book."

    s_thoughts "The room settles. Music from Isabella's earbuds, soft. Charlotte by the coffee table, scrolling her phone. Amara reading. Eve reading."

    s_thoughts "I'm not studying."

    s_thoughts "I'm in a room with five people and the ghost is here."
    
    s_thoughts "She's here."

    s_thoughts "I don't file it."

    s_thoughts "I just drink my tea."

    hide amara with dissolve
    hide isabella with dissolve
    hide eve with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 29: THE EDGE
    ## Eve's room. Anime. PJ variants. Late.
    ## "There's more."
    ## Deliberate pauses between every line.
    ## The chapter ends on the threshold.
    ## Use eve vulnerable ONCE -- when she says "there's more."
    ## ===========================

    scene bg evebedroom with Fade(1.0, 0.5, 1.0)

    play music mus_eve fadein 4.0

    s_thoughts "Wednesday."

    s_thoughts "Eve's room. Late."

    s_thoughts "The anime is playing. We're past the tournament now. The show has shifted into something else -- the characters are older, the fights are different, the stakes aren't about winning."

    show eve pj neutral at center with dissolve

    s_thoughts "Eve is on the bed. I'm on the bed. The chair stopped mattering two weeks ago."

    s_thoughts "She's cute in her pajamas. I'm a hot mess in sweats and a hoodie that used to be clean."

    s_thoughts "We've been watching for an hour. Eve's been talking -- not quite yapping, but close. She paused the show to explain a callback. She did the villain voice. She's comfortable."

    s_thoughts "The plant on the windowsill catches the screen light."

    s_thoughts "An episode ends. The autoplay countdown starts."

    s_thoughts "Eve reaches over and pauses it."

    s_thoughts "Her hand stays on the laptop for a second."

    pause 2.0

    s_thoughts "She closes the laptop."

    s_thoughts "The room goes dim. Just the lamp. The plant. The posters."

    stop music fadeout 3.0

    pause 1.5

    e "Sophia."

    s "Yeah?"

    pause 2.0

    s_thoughts "She's not looking at me. She's looking at the closed laptop. Her hands are in her lap."

    e "There's more."

    pause 1.5

    s "More what?"

    e "More than what I told you."

    pause 2.0

    s_thoughts "My chest."

    s_thoughts "I know. Some part of me already knows. The way she said 'something happened.' The way she started but couldn't quite finish."

    s_thoughts "There's another layer."

    play music mus_fragile fadein 3.0

    s "You don't have to--"

    e "I know I don't have to."

    pause 1.5

    s_thoughts "Her voice is quiet. Not small-quiet like the bad day. Deciding-quiet."

    show eve pj sad at center

    s_thoughts "She's looking at the laptop. At the dark screen."

    e "I've never told anyone. What happened."

    pause 1.5

    e "Amara knows." 
    
    s "Oh?"    
    
    e "She didn't -- I didn't tell her. She just..."

    s "She sees things."

    e "Yeah."

    pause 2.0

    s_thoughts "The room."

    s_thoughts "The lamp. The plant. The shelf with its chronological history. Manga at fourteen. Poetry at sixteen. Bad year, good poems."

    s_thoughts "Eve's hands in her lap."

    show eve pj vulnerable at center

    e "There's more."

    e "And I think I want to tell you."

    pause 2.5

    s_thoughts "I am being very careful."

    s_thoughts "Sitting in the dirt."

    s_thoughts "I am not filing this."

    s "Okay."

    pause 1.5

    e "Not tonight."

    s "Whenever is best."

    pause 2.0

    show eve pj sad at center

    s_thoughts "She looks at me."

    s_thoughts "Full eye contact. The kind Eve almost never does. The kind where I can see the dark circles and the way her glasses sit slightly crooked and the thing in her eyes that isn't sadness, exactly."

    e "But... soon."

    pause 1.5

    s "Okay."

    pause 2.0

    s_thoughts "She looks at me for one more second."

    s_thoughts "Then she opens the laptop. The anime starts up where it left off. The autoplay counter resets."

    show eve pj neutral at center

    s_thoughts "The episode plays."

    s_thoughts "Neither of us is watching."

    pause 2.0

    s_thoughts "The characters are talking. Something about a promise. Something about coming back."

    s_thoughts "The screen casts light across Eve's face. She's not watching. She's looking at the space between the laptop and the wall. Her eyes look... empty."
    
    s_thoughts "Like she's not really in the room with me."

    s_thoughts "I'm not watching either. I'm looking at the plant on the windowsill."

    s_thoughts "Eve said 'I think I want to tell you.'"

    s_thoughts "Not 'I have to.' Not 'I should.' 'I want to.'"

    s_thoughts "I don't know what it is."

    s_thoughts "But I know it's the thing underneath. The quiet part. The one that solidified the ghost."

    s_thoughts "And she's going to tell me."

    s_thoughts "Because she wants to."

    pause 2.0

    s_thoughts "The episode ends."
    
    s_thoughts "A next-episode preview starts to play. A new arc must be starting." 

    s_thoughts "It pans to the rival character. Eve's favorite -- she's sitting next to a character who hasn't been introduced yet." 
    
    s_thoughts "Eve's eyes dart to mine and she reaches forward and hits the skip button. It's like a reflex."
    
    e "I don't do previews. Spoilers."
    
    s "Right."

    s_thoughts "Eve shifts. Gets comfortable again as the next episode begins." 
    
    s_thoughts "Her shoulder touches mine."

    s_thoughts "She doesn't move away."

    s_thoughts "Neither do I."

    s_thoughts "The anime plays."

    stop music fadeout 4.0
    
    pause 3.0

    hide eve with dissolve

    scene black with Fade(2.0, 1.0, 2.0)
    
    "Chapter 4: Approach -- End"

    jump eve_ch5
