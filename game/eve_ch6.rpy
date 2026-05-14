## eve_ch6.rpy -- Glass Houses
## Chapter 6: "The Return" -- Eve Route
## One Act, Three Movements.
## Movement 1: The Orbiting Again (~2/3)
## Movement 2: The Choice (one menu)
## Movement 3: The Confession Path (~1/3)

## === NEW VARIABLES NEEDED (add to variables.rpy) ===
## default eve_confession = False

## === AUDIO DEFINITIONS ===
define audio.mus_eve = "audio/music/Eve Morse ~ A Room That Just Emptied.mp3"
define audio.mus_mourning = "audio/music/Mourning.mp3"
define audio.mus_fragile = "audio/music/Fragile Glass Between.mp3"
define audio.mus_shoulders = "audio/music/Shoulders Touching.mp3"
define audio.mus_fivepeople = "audio/music/Five People in a Kitchen.mp3"
define audio.mus_tuesday = "audio/music/A Normal Tuesday.mp3"
define audio.mus_campus = "audio/music/Campus in Autumn.mp3"
define audio.mus_2am = "audio/music/House at 2AM.mp3"
define audio.mus_shift = "audio/music/Shift.mp3"
define audio.mus_rain = "audio/music/Rain on the Windowframe.mp3"

## ===========================
## CHAPTER 6 START
## ===========================

label eve_ch6:

    ## ===========================
    ## MOVEMENT 1: "THE ORBITING AGAIN"
    ## Seven scenes. The return. The careful re-approach.
    ## Sophia carries "I'm in love with you"
    ## through every single one.
    ## ===========================

    ## ===========================
    ## SCENE 1: THE KITCHEN AGAIN
    ## Midnight. Green mug. "Oh. Hi."
    ## Callback to the very first scene of Ch4.
    ## Everything is different now.
    ## ===========================

    scene bg kitchen night with Fade(1.0, 0.5, 1.0)

    play music mus_eve fadein 4.0

    s_thoughts "Wednesday."

    s_thoughts "I know it's Wednesday because I've been counting days since 'hey'."

    s_thoughts "Since the open door."

    s_thoughts "My brain has been doing this thing where it replays that moment and tries to extract more information from it than a three-letter word can hold." 
    
    s_thoughts "'Hey.' What kind of hey. An I'm-here hey or an I'm-tolerating-your-presence hey or a hey-I-missed-you hey or just -- hey."

    s_thoughts "It was just hey."

    s_thoughts "I need water."

    s_thoughts "The kitchen light is on."

    show eve neutral at center with dissolve

    s_thoughts "Eve."

    s_thoughts "Green mug. Both hands. A book open in front of her. It's past midnight."

    s_thoughts "She looks up."

    e "Oh. Hi."

    s_thoughts "My chest does something stupid."

    s_thoughts "Same words. Same inflection. Same Eve at the same table with the same mug. As if everything -- the anime and the telling and the distance and all of it -- could fold down into 'oh, hi' and the kitchen would just accept it."

    s "Hey. Water."

    s_thoughts "She nods."

    s_thoughts "I fill a glass."

    s_thoughts "The tap sounds exactly as enormous as it did the first time."

    s_thoughts "I drink it standing at the counter. The fridge hums. Eve turns a page."

    s_thoughts "Her socks don't match. One is grey, one is dark blue."

    s_thoughts "Same socks."

    s_thoughts "Or different mismatched socks that happen to be the same colors. Or she has a drawer of unmatched socks and this is just what comes out. I don't know. I know I'm looking at her socks again at 2 AM and I know that means the same thing it meant last time."

    s_thoughts "I sit down across from her."

    s_thoughts "She doesn't look up."

    s_thoughts "We sit."

    pause 2.0

    s_thoughts "The house is different at this hour. No Charlotte energy in the walls. No Isabella's music through the floor. Just the fridge and the clock and Eve's page turning."

    s_thoughts "It's the same and it's completely different."

    s_thoughts "I know things now. All the things she's told me. About her family. About why she came here. About... Cadence."

    s_thoughts "And she knows I know."

    s_thoughts "And I might know she knows I have feelings for her because I basically screamed it with my eyes every night since the convenience store and I'm not subtle."

    s_thoughts "She's reading."

    s_thoughts "I'm sitting."

    s_thoughts "Both of us are pretending this is normal."

    s_thoughts "Both of us know it's not."

    pause 2.0

    e "The house is quieter when Charlotte's asleep."

    s_thoughts "Same thing she said that first night."

    s "Yeah. It is."

    s_thoughts "We sit for a while. I don't know how long. Long enough that my glass is empty."

    e "Goodnight."

    s "Goodnight, Eve."

    s_thoughts "She doesn't look up from the book."

    s_thoughts "I rinse my glass. I go upstairs."

    hide eve with dissolve
    
    scene bg hallway night with dissolve

    pause 1.5

    s_thoughts "The kitchen light stays on."
    
    s_thoughts "She left her room open. I glance inside."
    
    s_thoughts "Something is different about her bookshelf. I can see it from here."
    
    s_thoughts "The chronological order is the same, left to right. But there's a new book at the end."

    s_thoughts "Right end. Recent. A small paperback, the kind you'd buy at a train station."

    s_thoughts "Eve added to the timeline while she was gone."

    s_thoughts "She was reading while she was behind the closed door. She was building her shelf."

    s_thoughts "I notice it. I don't file it."

    s_thoughts "I sit with it."

    s_thoughts "Everything is the same. Nothing is the same."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 2: ANIME NIGHT RESUMES
    ## Eve's room. The laptop. But the blanket
    ## isn't shared. The inches are deliberate.
    ## Eve's guard drops -- once.
    ## ===========================

    scene bg hallway with Fade(1.0, 0.5, 1.0)

    s_thoughts "Saturday."

    s_thoughts "I'm in the hallway. Coming back from the bathroom."

    s_thoughts "Eve's door is open."

    s_thoughts "She's on her bed. Laptop open. The show paused on the title card."

    s_thoughts "She looks at me."

    show eve pj neutral at center with dissolve
    
    play music mus_spacebetween fadein 3.0
    
    e "Are you coming in?"
    
    s_thoughts "I nod with some hesitation."
    
    scene bg evebedroom with dissolve
    
    pause 2.0
    
    show eve pj neutral at center with dissolve

    e "I'm on episode thirty-four."

    s_thoughts "We were on twenty-six."

    s_thoughts "She watched eight episodes without me."

    s_thoughts "During the distance. While her door was closed and I was on my floor listening to her playlist. She was watching our show."

    s_thoughts "She needed it and she couldn't wait."

    s_thoughts "I'm hurt but weirdly glad. She's seen it before. But if she needed to rewatch those episodes without me, then that's what she needed. But it still hurts a little."

    s_thoughts "I don't say any of this."

    s "Thirty-four. That's -- you skipped ahead."

    e "Yeah."

    s_thoughts "No explanation. No apology."

    s "Do I need to catch up or--"

    e "You can. Or I can just tell you what happened."

    s "Tell me."

    s_thoughts "She sits up a little. The laptop screen lights her face."

    e "The rival came back."

    s_thoughts "Of course she did."

    e "After the loss. After the bench scene. She disappears for three episodes. Nobody knows where she went."

    s "Classic."

    e "When she comes back she has a new technique. It doesn't make sense. The power scaling is completely wrong. But it's -- it works narratively, even if it's nonsense mechanically."

    s "What's the technique?"

    e "She stops fighting alone. The whole point of her character was fighting alone. Solo battles. Never asking for help. And then she comes back and her new move requires another person."

    s_thoughts "Something."

    e "A partner technique. She can't use it by herself. She has to trust someone to cover her back."

    s_thoughts "Eve says this like she's talking about anime."

    s_thoughts "She is talking about anime."

    s_thoughts "She's also not."

    e "It's good writing. They earned it."

    s "Yeah."

    s_thoughts "I sit in the chair. She's on the bed. The blanket is just on her side. Not shared. The two feet between the bed and the chair feel like a decision."

    s_thoughts "She hits play on episode thirty-four."

    s_thoughts "We watch."

    s_thoughts "Eve doesn't yap. Not like before. She makes small comments -- the animation in this scene, the pacing of that fight. But the long passionate rants about the rival character's thematic weight are gone."

    s_thoughts "She's being careful."

    s_thoughts "The episodes play. One. Then another. The autoplay countdown starts and neither of us stops it."

    s_thoughts "The rival character is on screen. She's fighting alongside the protagonist for the first time. The partner technique. They're clumsy with it. They keep getting the timing wrong."

    e "See? The timing. They have to sync their attacks. She's too fast and he's too reckless."

    s "They'll figure it out."

    e "Obviously they'll figure it out. That's not the point. The point is they're bad at it first."

    s_thoughts "I notice something in voice. This isn't the measured Eve. Not the careful Eve, either."

    s_thoughts "The Eve who cares about fictional people."

    s_thoughts "The rival takes a hit meant for the protagonist. She falls. He catches her. It's corny. It's so corny."

    s_thoughts "Eve laughs."

    show eve pj smile at center

    s_thoughts "A real laugh. Short and surprised, like it escaped before she could catch it."

    s_thoughts "She catches herself."

    show eve pj neutral at center

    s_thoughts "The guard goes back up. Physically, visibly -- her shoulders tighten, her spine straightens, her face resets."

    s_thoughts "But for half a second."

    s_thoughts "The old Eve was there."

    s_thoughts "The one from the anime nights. The one who yapped about the rival character. The one who forgot she was wearing the wall."

    pause 1.5

    s_thoughts "Eve is looking at the screen. Not at me."

    e "She's fighting again."

    s_thoughts "The rival. On screen. Fighting alongside someone."

    e "She's fighting again."

    s_thoughts "She says it twice. Quiet. Like she's confirming something to herself."

    s_thoughts "The episode ends."

    s_thoughts "She closes the laptop."

    e "Same time Wednesday?"

    s "Yeah."

    s_thoughts "I stand up. I go to the door."

    e "Sophia."

    s_thoughts "I turn."

    show eve pj flustered at center

    s_thoughts "She's looking at the closed laptop. Not at me."

    e "Thanks for catching up."

    s "You did the hard part."

    s_thoughts "She doesn't respond."

    s_thoughts "I go to my room."

    hide eve with dissolve
    
    scene bg sophiaroom with dissolve

    s_thoughts "I lie on my bed and stare at the ceiling and think about Eve laughing at a corny anime scene and how she caught herself doing it and how the catching was worse than anything."

    s_thoughts "Because catching yourself means you know. You know you were open for a second and now you have to close it back up."

    s_thoughts "She's fighting again."

    s_thoughts "I press my face into my pillow and make a sound that is not a word."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 3: THE HOUSE SCENE
    ## Ensemble. Eve is present -- really present.
    ## Sophia almost says it. To the room. To nobody.
    ## Cross-route threads: Charlotte's wobble, Isabella's phone.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_fivepeople fadein 2.0

    s_thoughts "Thursday evening."

    s_thoughts "Something miraculous is happening."

    s_thoughts "All five of us are in the kitchen."

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte made pasta. Because Charlotte makes pasta when the house feels fragile -- it's her version of a structural repair."

    show isabella happy at right with dissolve

    s_thoughts "Isabella is at the counter, telling a story about a vending machine that ate her last three coins. She's doing the voices."

    show eve neutral at center with dissolve

    s_thoughts "Eve is here."

    s_thoughts "She's not lurking or only here for a single task. She's just -- Eve. In the kitchen. During dinner. With people."

    s_thoughts "She's leaning against the counter near the fridge. She has a glass of water. She's listening to Isabella's vending machine story with something that's almost a smile."

    c "I made garlic bread! There's extra. Eve, do you want some? There's a plate for you."

    s_thoughts "Charlotte holds out the plate. The brightness wobbles once -- her hand pauses, her face goes somewhere for half a second, then the smile reassembles."

    s_thoughts "I see it. I don't follow up."

    e "Thanks."

    s_thoughts "Eve takes a piece of garlic bread."

    s_thoughts "She takes garlic bread from Charlotte's plate. Charlotte's whole face lights up."

    c "Of course! I always make extra. It's nothing."

    s_thoughts "It is not nothing. Charlotte made garlic bread and Eve took a piece and Charlotte is glowing like she won something."

    i "So the vending machine, right? I'm standing there and I'm like, okay, the universe hates me specifically--"

    s_thoughts "Isabella's phone buzzes. She glances at it. Something crosses her face -- softer, private, gone -- and she puts it away."

    i "--and then the guy behind me goes 'have you tried hitting it?' And I said 'sir, I was raised by the internet, violence is always my second option.'"

    s_thoughts "Charlotte laughs. Eve makes a sound that might be a laugh."

    s_thoughts "Amara is reading at the table. She hasn't looked up."

    s_thoughts "Five people in a kitchen."

    s_thoughts "I'm watching Eve take a bite of garlic bread and I'm watching her be a person in a room full of people. A room where she's not performing and she's not hiding and she's just standing near a fridge eating bread that Charlotte made."

    s_thoughts "And the love is so loud in my chest I can't--"

    s_thoughts "I can barely--"

    pause 1.5

    s_thoughts "I open my mouth."

    s_thoughts "I don't know what I'm going to say. Not to Eve. To the room. To nobody."

    s_thoughts "I close it."

    s_thoughts "I take a breath."

    s_thoughts "I drink my tea."

    i "Sophia, you okay? You look like you swallowed wrong."

    s "Fine. Just -- garlic bread."

    c "Is it too much garlic? I can never tell. Isabella says I overdo it."

    i "I said it was AGGRESSIVE garlic. That's different from too much."

    c "Is it?"

    i "Aggressive is a compliment!"

    s_thoughts "The kitchen is warm. The conversation keeps going. Normal."

    s_thoughts "Eve catches my eye across the room."

    s_thoughts "She doesn't smile. She doesn't look away."

    s_thoughts "She just looks at me. For a second."

    show eve flustered at center

    s_thoughts "Then she takes another bite of garlic bread."

    show eve neutral at center

    s_thoughts "Amara turns a page."

    hide charlotte
    hide isabella
    hide eve
    with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 4: LILA CHECK-IN
    ## Campus. "So she's back?" "And you still
    ## haven't told her." "Because the last
    ## person who told her destroyed her."
    ## For ONCE, Lila has no advice.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 2.0

    s_thoughts "Friday. The bench."

    show lila happy at center with dissolve

    l "So she's back."

    s "She's back."

    l "And you're doing a face."

    s "What face?"

    l "The face where you look like someone told you good news and bad news at the same time and you're still deciding which one to react to."

    s "I don't have that face."

    show lila annoyed at center

    l "You have so many faces, babe. You have a face for everything. You have a face for 'I'm pretending I don't have a face.' I've been taking careful notes."

    s "..."
    
    show lila neutral at center

    l "So. She came back. Door's open. Anime nights. Late evenings in the kitchen together. The whole shebang."

    s "The whole thing."

    l "And you still haven't told her."

    s_thoughts "I look at the ground."

    s "I can't."

    l "Why?"

    s "Because the last person who told her destroyed her."

    pause 2.0

    s_thoughts "Lila is quiet."

    s_thoughts "Lila is never quiet."

    show lila happy at center

    s_thoughts "She's looking at her iced coffee. Condensation running down the side."

    l "That's really hard."

    s_thoughts "No follow-up. No 'but you should anyway.' No 'the worst that can happen is she says no.' No Lila-branded advice that's 60 percent confidence and 40 percent guesswork."

    l "That's really hard."

    s_thoughts "She says it again. Like she's confirming it to herself."

    s "Yeah."

    l "You love her?"

    s_thoughts "I look at Lila."

    s "I think so."

    s_thoughts "Lila nods. She drinks her iced coffee. It's forty degrees outside and she's drinking iced coffee because that's who Lila is."

    l "I don't have a thing for this."

    s "A thing?"

    l "Advice. A bit. The Lila take. I usually have a take."

    s "Yeah."

    l "I don't have one. I just know it sounds really hard."

    s_thoughts "She squeezes my arm. Once."

    l "You'll figure it out. Or you won't. Either way I'm here."

    s "Thanks, Lila."

    l "Don't thank me, I'm useless. Update me, though."

    hide lila with dissolve

    s_thoughts "She leaves."

    s_thoughts "I sit on the bench."

    s_thoughts "Lila didn't have advice. Lila always has advice. The fact that she doesn't have advice is its own kind of answer."

    s_thoughts "There's no good version of this."

    s_thoughts "I tell her and I become Cadence's shape."

    s_thoughts "I don't tell her and I carry it until it poisons everything."

    s_thoughts "Those are the options."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 5: NOVA'S CLASS -- THE FINAL ONE
    ## The paper. "Put the notebook down."
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)

    play music mus_nova fadein 2.0

    s_thoughts "Monday."

    s_thoughts "Last class of the semester."

    show professor neutral at center with dissolve

    s_thoughts "Nova is returning papers. She moves through the rows with that specific calm that means she's about to say something that matters."

    nova "Before I hand these back. I want to say something."

    s_thoughts "The room goes quiet. Not because Nova commands it. Because she pauses and the silence fills the space and we all wait."

    nova "You came to this class to study observation. The ethics of the gaze. The ethnographer's dilemma."

    nova "Most of your papers were analysis. Good analysis."

    s_thoughts "She pauses."

    nova "Some of your papers were testimony."

    s_thoughts "She looks at me."

    s_thoughts "Not for long. Just a flicker. But I know."

    s_thoughts "She puts the paper on my desk face-down."

    nova "Here's what I want you to think about for your final projects."

    nova "What's the difference between observation and attention?"

    s_thoughts "Nobody answers."

    nova "Observation requires a subject. Something you're watching. Something separate from you. You observe from outside."

    nova "Attention requires presence. You're not outside. You're in the room. You're not studying the room. You're in it."

    pause 1.5

    show professor happy at center

    nova "Some of you wrote beautiful observations. Detailed. Precise. You could be excellent ethnographers."

    nova "But ethnography has a cost. The notebook is always between you and the subject."

    s_thoughts "She's looking at me again."

    nova "Sometimes the most ethical thing the ethnographer can do is put the notebook down."

    pause 2.0

    s_thoughts "I turn the paper over."

    s_thoughts "B+."

    s_thoughts "In the margin, in Nova's small handwriting: 'This is testimony. I want you to think about what that means.'"

    s_thoughts "Below that: 'The glass house metaphor works. But you're still standing outside it.'"

    show professor neutral at center

    nova "That's it. Good luck with your final projects and have a good winter break."

    hide professor with dissolve

    s_thoughts "People are packing up. Chairs scraping. Someone asking someone else about lunch."

    s_thoughts "I sit with the paper."

    s_thoughts "'Put the notebook down.'"

    s_thoughts "The notebook is the file. The file is the observation instinct. The thing I do with everyone."

    s_thoughts "With Eve."

    s_thoughts "Nova is telling me to stop watching and start being."

    s_thoughts "I don't know how."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 6: THE FLOOR PLAYLIST -- REALLY LISTENING
    ## Sophia on the floor. Eve's listening position.
    ## The Cadence song. The decision.
    ## She can't carry it anymore.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.5, 1.0)

    s_thoughts "Tuesday night. Late."

    s_thoughts "I'm on the floor."

    s_thoughts "Not the bed. Not the chair. The floor."

    s_thoughts "Eve's listening position."

    s_thoughts "I didn't plan it. I came in from class and dropped my bag and sat down on the floor and I just -- stayed."

    s_thoughts "This is what Eve does."

    s_thoughts "When things are bad she sits on the floor and listens to her playlist. 'Floor.' Just the word floor."

    s_thoughts "I open my phone."

    play music mus_eve fadein 3.0

    s_thoughts "I hit play."

    s_thoughts "Pop. Folk. The songs I know now. The ones that aren't Eve's private language anymore because she gave them to me."

    s_thoughts "I'm not analyzing the choices. I'm not filing the genres."

    s_thoughts "'Put the notebook down' is what Nova said."

    s_thoughts "I'm trying."

    pause 2.0

    s_thoughts "A song plays and I think about the convenience store and the noodle packaging. 'Someone has to.' Eve's face when she didn't know she was funny."

    s_thoughts "Another song and I think about the mug. Both hands. The chip on the rim."

    s_thoughts "Another and it's the hallway. Twenty minutes on the floor outside her door. 'Thank you for sitting in the hallway instead of coming in.'"

    s_thoughts "Another and it's the shoulder. Her shoulder against mine. She didn't move."

    s_thoughts "The playlist is a map. Every song is a room I've been in with Eve."

    pause 2.0

    s_thoughts "A song ends."

    s_thoughts "The next one starts."

    s_thoughts "Country."

    s_thoughts "Cadence's song."

    s_thoughts "The one Eve blushed at. The one she trailed off about. 'It was...' Her favorite."

    s_thoughts "I let it play."

    s_thoughts "I used to hear it as evidence. As part of the file. The country song: filed under 'things that matter to Eve,' subcategory 'things she can't talk about.'"

    s_thoughts "Now I hear it as part of her life."

    s_thoughts "Cadence liked this song. Eve kept it on the playlist. The playlist she listens to on bad days. On the floor."

    s_thoughts "She couldn't take it off."

    pause 2.0

    s_thoughts "I think about what confessing means."

    s_thoughts "Cadence told Eve too."

    s_thoughts "'I have feelings for you.' That was the shape of it. Someone who was Eve's closest person saying: I want more than this."

    s_thoughts "And then."

    s_thoughts "I know what happened after."

    s_thoughts "If I say it, I become that shape. Not the same person. Not the same act. But the same shape. The shape of someone who took the friendship and asked for more."

    s_thoughts "I know this."

    s_thoughts "I'm going to do it anyway."

    s_thoughts "Not because I think it'll go differently. Not because I'm noble or selfless or any of the things a better person would be."

    s_thoughts "Because I can't carry it anymore."

    s_thoughts "It's been in my chest since the convenience store and it got heavier after the floor playlist and it got heavier after 'she was like you' and it got heavier after 'hey' and the open door and the laugh she caught and the garlic bread and every single moment in between."

    s_thoughts "I'm full."

    s_thoughts "That's not brave. It's not romantic. It's just honest."

    s_thoughts "I'm full and I can't hold it and I'm going to tell her."

    pause 2.0

    s_thoughts "The song ends."

    s_thoughts "I stay on the floor for a while."

    s_thoughts "Sitting the way Eve sits. Listening the way Eve listens."

    s_thoughts "Sitting on your floor listening to someone else's bad-day playlist because you're in love with them is a thing. It's a specific, nameable thing. And I'm doing it."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 7: CHARLOTTE AND ISABELLA
    ## The cross-route scene. BRIEF. WARM.
    ## The background tragedy is deafening
    ## for players who've done the other routes.
    ## First-time players see a sweet friendship scene.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_tuesday fadein 2.0

    s_thoughts "Wednesday afternoon."

    s_thoughts "I need to talk to someone. Not Lila -- Lila doesn't have advice for this. I need someone who lives in this house. Someone who knows Eve."

    show charlotte smile at left
    show isabella happy at right
    with dissolve

    s_thoughts "Charlotte and Isabella are at the kitchen table. Charlotte's doing something on her laptop. Isabella has a textbook and a bag of chips."

    s "Can I ask you guys something?"

    c "Of course!"

    i "Is it about Eve?"

    s "How did you--"

    i "Because duh."

    s "...Right."

    i "C'mon. Sit."

    s_thoughts "I sit down."

    s "I'm going to tell her how I feel."

    show charlotte happy at left

    c "Oh! Sophia. That's -- that's wonderful."

    s_thoughts "Charlotte straightens up. She reaches across the table and tucks a strand of hair behind my ear. A small thing. A Charlotte thing."

    c "Of course you should tell her! She deserves to know."

    s "I'm scared."

    c "Of course you are. That's normal. But Eve -- she came back, right? She opened the door. She wouldn't have done that if she didn't want you there."

    s_thoughts "Charlotte says this with absolute warmth. Not a crack in it."

    i "Just say it."

    s "Just say it?"

    i "What's the worst that could happen?"

    s_thoughts "I stare at her."

    s "A lot of things."

    show isabella smile at right

    i "Yeah, but also -- you're already dying. You've been dying for weeks. Just say the thing."

    s "That's your advice? 'Just say the thing'?"

    i "I'm a CS major, not humanities. My relationship advice is literally 'have you tried turning it off and on again.'"

    s_thoughts "Charlotte laughs."
    
    show isabella happy at right

    c "What Isabella means is -- trying to hold something in forever just protects yourself."

    s_thoughts "'Protects yourself.' Charlotte says it and it's... offhand. Easy."

    i "Also, Eve's smart. She probably already knows."

    s "That's what scares me."

    c "Then you're not telling her anything new. You're just saying it out loud."

    s_thoughts "Isabella's phone buzzes. She glances at it. Her face does a thing and she puts it away."

    i "Anyway. You got this."

    c "You do! We're here. Whatever happens."

    s_thoughts "Charlotte squeezes my hand. Isabella gives me a thumbs up."

    s_thoughts "Two friends helping."

    s_thoughts "I feel better. Resolved. Ready."

    s "Thanks."

    c "Of course."

    hide charlotte
    hide isabella
    with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## END OF MOVEMENT 1
    ## ===========================

    ## ===========================
    ## MOVEMENT 2: THE CHOICE
    ## Eve's room. The anime was playing.
    ## Eve paused it. The laptop screen frozen.
    ## One option. One button.
    ## The ONLY menu in three chapters.
    ## ===========================

    scene bg evebedroom with Fade(1.0, 0.5, 1.0)

    play music mus_shoulders fadein 2.0

    s_thoughts "Wednesday night."

    show eve pj neutral at center with dissolve

    s_thoughts "We're three episodes in. The rival character is fighting alongside the protagonist again. They're getting better at the partner technique. The timing is starting to sync."

    s_thoughts "Eve is on the bed. I'm in the chair. The blanket is still just on her side."

    s_thoughts "She's been commenting on the fights. Not yapping -- commenting. Small observations. She's still careful."

    s_thoughts "The plant on the windowsill catches the light from the laptop screen."

    s_thoughts "The green mug on the nightstand."

    s_thoughts "Everything is in this room. The bookshelf with its chronological timeline. The framed anime posters. The plant that comes back."

    s_thoughts "The girl on the bed who told me the worst thing that ever happened to her and ran and came back."

    s_thoughts "Eve pauses the show."

    s_thoughts "The laptop screen freezes on the rival character mid-strike. Her arm extended. Her face determined."

    e "Do you want tea? I was going to--"

    s "Eve."

    s_thoughts "I say her name and I don't know what's coming after it."

    s_thoughts "She looks at me."

    s_thoughts "I know what's coming after it."

    pause 2.0

    stop music fadeout 3.0

    pause 2.0

    s_thoughts "The room is silent."

    s_thoughts "The laptop fan hums."

    s_thoughts "The plant."

    s_thoughts "The mug."

    s_thoughts "Her face."

    pause 2.0

    menu:
        "\"I have feelings for you.\"":
            jump eve_ch6_confession

        "Confess." if eve_gh_unlocked():
            jump eve_ch6_glass_houses

    ## ===========================
    ## MOVEMENT 3: THE CONFESSION PATH
    ## "Friends"
    ## ===========================

label eve_ch6_confession:

    ## ===========================
    ## THE CONFESSION
    ## Eve's face. "Cadence told me too."
    ## "But you just did what she did."
    ## ===========================

    $ eve_confession = True

    s "I have feelings for you."

    pause 2.0

    s_thoughts "Eve looks at me."

    s_thoughts "Her face doesn't change."

    s_thoughts "That's the thing. Her face doesn't change."

    s_thoughts "She looks at me the way you look at something you expected. Not surprised. Not angry. Not hurt."

    s_thoughts "Just watching it arrive."

    show eve pj neutral at center

    s_thoughts "Her eyes are steady. Her hands are still in her lap. She doesn't pull the blanket tighter or lean away or do any of the things I've been bracing for."

    s_thoughts "She just looks at me."

    s_thoughts "She's been expecting this."

    pause 3.0

    e "I know."

    pause 1.5

    s "You know?"

    e "I've known for a while."

    pause 2.0

    play music mus_mourning fadein 3.0

    s_thoughts "I look around the room."

    s_thoughts "At the laptop frozen on the rival's face."

    s_thoughts "At the plant."

    s_thoughts "At..."
    
    s_thoughts "Her."

    e "Cadence told me too."

    pause 3.0

    s_thoughts "That sentence."

    s_thoughts "In the room."

    s_thoughts "Between us."

    s_thoughts "Four words that contain an entire history and I'm standing inside it."

    s "I'm not Cadence."

    e "I know you're not."

    pause 2.0

    e "But you just did what she did."

    s_thoughts "Not an accusation."

    s_thoughts "A fact."

    s_thoughts "Said the way she described her parents. The way she described the empty house. Weather-flat. The voice from the very first time she told me about her family."

    s_thoughts "'The house where nobody looked.'"

    s_thoughts "That voice."

    s_thoughts "She's telling me what I did the way she tells anyone what happened to her. Carefully. Precisely. Without accusation."

    s_thoughts "Because accusation would mean she's surprised. And she's not."

    pause 2.0

    show eve pj sad at center

    s_thoughts "Eve stands up."

    s_thoughts "She doesn't slam anything. She doesn't cry. She's not angry."

    s_thoughts "She just leaves."

    s_thoughts "She walks past me to the door and opens it and walks through it."

    hide eve with dissolve

    s_thoughts "The door closes."

    s_thoughts "Not slammed. Closed. The way you close a door when you're the kind of person who closes doors carefully because you grew up in a house where doors got slammed."

    pause 3.0

    s_thoughts "The laptop screen is still frozen."

    s_thoughts "The rival character. Mid-strike. Her arm extended."

    s_thoughts "I'm alone in Eve's room."

    s_thoughts "I did the thing."

    s_thoughts "I became the shape."
    
    stop music fadeout 1.5

    ## ===========================
    ## SOPHIA BREAKS DOWN
    ## The hallway. Same hallway.
    ## Same floor. Different everything.
    ## ===========================

    scene bg hallway night with Fade(0.8, 0.3, 0.8)

    s_thoughts "Somehow I end up in the hallway."

    s_thoughts "I don't know when I left her room. I don't remember standing up. I'm just here."

    s_thoughts "Same hallway."

    s_thoughts "Same floor."

    s_thoughts "The one where I sat for twenty minutes. The one that meant 'present without intrusion.' The one she thanked me for."

    s_thoughts "I sit down."

    play music mus_fragile fadein 2.0

    s_thoughts "Not because it's the right thing to do. Because my legs stopped working."

    pause 2.0

    s_thoughts "I think about every moment I've spent with Eve these last months."

    s_thoughts "The kitchen. The mug. 'Oh. Hi.' The anime. The convenience store. The noodle packaging. The floor playlist. The shoulder touch. The hallway. The telling. The distance. The open door."

    s_thoughts "All of it."

    s_thoughts "Gone."

    s_thoughts "Because I couldn't hold it anymore."

    pause 2.0

    s_thoughts "I'm crying."

    s_thoughts "It's not graceful. The kind where your face does things you can't control and you can't breathe right and you keep making sounds that aren't words."

    s_thoughts "The hallway is empty."

    s_thoughts "The hallway where I sat for twenty minutes and Eve said 'thank you.'"

    s_thoughts "Now it means something else."

    s_thoughts "Now it means 'alone with what I did.'"

    s_thoughts "I can't stop crying."

    s_thoughts "I tried to be different from Cadence. I sat in the hallway. I didn't push. I waited. I learned. I put the notebook down."

    s_thoughts "And then I picked it back up and wrote 'I have feelings for you' on the last page and handed it to her and she read it and left."
    
    s_thoughts "She left."

    s_thoughts "Because it doesn't matter how I said it."

    s_thoughts "It matters that I said it."

    pause 3.0

    ## ===========================
    ## AMARA APPEARS
    ## The most she's ever spoken.
    ## Costly sentences. Silences. Precision.
    ## ===========================

    show amara neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "I don't know when she got here. I don't know how long she's been standing there."

    s_thoughts "She's looking at me."

    s_thoughts "Amara is always where the hallway needs her."

    s_thoughts "She sits down."

    s_thoughts "Not next to me. Across. Her back against the opposite wall. Like she's establishing: I'm here. I'm not touching you."

    pause 2.0

    a "You told her."

    pause 1.5

    a "She left."

    s_thoughts "Not a question. Two facts."

    s_thoughts "I nod. I can't talk. I'm still doing the thing where I can't breathe right."

    pause 2.0

    a "She knew."

    pause 1.5

    a "She's known for weeks."

    pause 1.5

    a "She came back knowing."

    s_thoughts "Amara says each sentence and then stops. Like she's placing them. One at a time."

    s_thoughts "Costly sentences."

    s_thoughts "I'm watching Amara spend words the way I've never seen her spend them."

    pause 2.0

    a "She didn't run because you're the person who hurt her."

    s_thoughts "I look up."

    pause 1.5

    a "She ran because the pattern is the pattern."

    pause 1.0

    a "Her body doesn't know the difference yet."

    s_thoughts "Each sentence lands. Sits. Breathes."

    s_thoughts "Amara is talking more than I've ever heard her talk. The room feels different. The hallway feels different. Amara is talking."

    pause 2.0
    
    a "She knew you'd say it. She came back anyway. That means she's choosing." 
    
    pause 1.5
    
    a "...Let her choose."
    
    s "Okay."
    
    s_thoughts "I try to say it in a normal voice. I can't. It comes out as a half-sob."

    pause 2.0

    s_thoughts "I'm still crying."

    a "I've been watching both of you."

    pause 1.0

    a "For months."

    a "That's what I do."

    s_thoughts "Not a boast. Credentials. She's establishing why what she's about to say matters."

    s_thoughts "Amara has been doing what I do. Watching. But Amara watches without filing. Without the notebook."
    
    s_thoughts "She doesn't need it like I need it."
    
    pause 2.0

    a "You won't hurt her."

    pause 1.5

    a "Not on my watch."

    s_thoughts "I look up at her when she says it. Her expression is indiscernible."
    
    s_thoughts "But she means it. I can tell she means it."
    
    pause 1.0

    a "Let me go talk to her."

    s_thoughts "Amara stands up."

    s_thoughts "She looks at me."

    s_thoughts "I look at her."

    s_thoughts "She nods. Once."

    s_thoughts "She goes inside."

    hide amara with dissolve

    s_thoughts "Eve's door opens. Closes."

    s_thoughts "Amara is with Eve."

    s_thoughts "I'm in the hallway."

    stop music fadeout 3.0

    ## ===========================
    ## THE WAIT
    ## Same evening. Hours, not days.
    ## Sophia on the floor. The house around her.
    ## The distance is shorter this time.
    ## ===========================

    pause 3.0

    s_thoughts "I wait."

    pause 2.0

    s_thoughts "Not the active waiting from before. Not 'I'm giving you space with an agenda.'"

    s_thoughts "I'm sitting on the floor in the hallway because I can't stand up and I don't know what else to do."

    pause 2.0

    s_thoughts "The house moves around me."

    s_thoughts "Charlotte's footsteps downstairs. Something in the kitchen. A cupboard opening. She's making tea. She doesn't know."

    s_thoughts "Someone's music through a wall. Isabella. Something lo-fi."

    s_thoughts "The sounds of a house that doesn't know what just happened."

    pause 3.0

    s_thoughts "I don't know what's happening inside Eve's room."

    s_thoughts "Amara is in there. With Eve."

    s_thoughts "I think about Amara and Eve in the living room. Both of them in the same space, not talking. The most comfortable either of them had ever been that I'd seen."

    s_thoughts "Amara is the right person for this. Not me."

    s_thoughts "Amara doesn't hover. Amara doesn't observe. Amara doesn't perform warmth."

    s_thoughts "Amara just exists in the room."

    pause 3.0

    s_thoughts "Time passes."

    s_thoughts "I don't know how much."

    s_thoughts "The house gets quieter. Charlotte's footsteps go upstairs. She passes me quietly. She doesn't want to interrupt."

    s_thoughts "Isabella's music stops. She passes me to go to the bathroom. 'Sorry,' she whispers like confession."

    s_thoughts "I'm still on the floor."

    pause 2.0

    s_thoughts "My phone says it's been two hours."

    s_thoughts "It feels like seven."

    s_thoughts "It feels like four seconds."

    s_thoughts "I don't know if Eve will come back."

    s_thoughts "Last time -- after the telling -- she disappeared for days. A week. Her door closed. The ghost went back to being a ghost."

    s_thoughts "This could be that again."

    s_thoughts "I could be sitting in this hallway when the sun comes up."

    pause 3.0

    s_thoughts "But."

    s_thoughts "Last time it took a week."

    s_thoughts "Last time the open door was a Tuesday with no catalyst. Just a Tuesday."

    s_thoughts "This is the same night."

    s_thoughts "The distance is shorter."

    s_thoughts "A shorter retreat."

    pause 2.0

    s_thoughts "Eve's door opens."
    
    s_thoughts "Amara walks past."
    
    s_thoughts "A moment passes. Then another. And another."
    
    s_thoughts "Eventually, after what feels like eons..."

    ## ===========================
    ## EVE COMES BACK
    ## "Friends?" / "Friends."
    ## ===========================

    play music mus_eve fadein 4.0
    
    pause 2.5

    show eve neutral at center with dissolve

    s_thoughts "Eve."
    
    s_thoughts "Standing in front of me in the hallway. Our hallway."

    s_thoughts "She doesn't look angry. She doesn't look scared."

    s_thoughts "She looks tired."

    s_thoughts "The kind of tired that comes from running and then stopping."

    s_thoughts "Her eyes are red. Her hair is pushed back with one hand. She's still in her pajamas."

    s_thoughts "She's looking at me on the floor."

    s_thoughts "I'm looking at her."

    pause 3.0

    e "Friends?"

    pause 2.0

    s_thoughts "Not a question."

    s_thoughts "An offering."

    s_thoughts "The safest true thing she can say."

    pause 1.5

    s "Friends."

    pause 2.0

    s_thoughts "I mean it."

    s_thoughts "And I carry the weight."

    s_thoughts "Both at the same time."

    pause 2.0

    s_thoughts "Eve sits down."

    s_thoughts "Not across from me. Next to me. Her back against the same wall."

    s_thoughts "A foot between us."
    
    s_thoughts "I don't look at her. I don't want her to see how much I've been crying."
    
    s_thoughts "But she can obviously see. She doesn't say anything about it."
    
    s_thoughts "We just... sit."

    s_thoughts "We just sit in the hallway."

    s_thoughts "Neither of us talks."

    pause 3.0

    hide eve with dissolve

    ## ===========================
    ## THE ENDING: ANIME FADE-OUT
    ## Eve's room. The show playing.
    ## The rival is fighting again.
    ## Neither of them watching.
    ## ===========================

    scene bg evebedroom with Fade(1.0, 0.5, 1.0)

    show eve pj neutral at center with dissolve

    s_thoughts "Later."

    s_thoughts "Eve's room."

    s_thoughts "I don't know who suggested it. Maybe nobody did. Maybe we just migrated. From the hallway to the room."

    s_thoughts "The laptop is open. The show is playing."

    s_thoughts "I'm in the chair. She's on the bed. The blanket is on her side."

    s_thoughts "The green mug is on the nightstand."

    s_thoughts "The plant on the windowsill catches the screen light."

    s_thoughts "On screen, the rival character is fighting. The partner technique again. She and the protagonist are in sync now. The timing is right."

    s_thoughts "She's fighting again."

    pause 2.0

    s_thoughts "Neither of us is really watching."

    s_thoughts "The anime plays. The room is warm. The fan hums."

    s_thoughts "Eve reaches for the mug and wraps her hands around it."

    s_thoughts "She's here."

    s_thoughts "She ran and she came back. Again. For the second time."

    s_thoughts "The pattern holds: Eve runs and Eve returns."

    s_thoughts "And the distance was shorter this time."

    pause 3.0

    s_thoughts "It's not what I wanted with Eve."

    s_thoughts "But it's not not what I wanted with Eve, either."

    s_thoughts "She's okay."

    s_thoughts "I'm okay."

    s_thoughts "We're..."

    pause 1.5

    s_thoughts "We're okay."

    s_thoughts "Friends."

    pause 3.0
    
    s_thoughts "I think I'm still in love with her."
    
    s_thoughts "I write it down in the notebook."
    
    s_thoughts "And we watch anime together quietly."
    
    stop music fadeout 4.0

    pause 3.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Friends{/size}"

    $ persistent.ending_eve_friends = True
    $ persistent.completed_eve_route = True
    return


    ## ===========================
    ## MOVEMENT 3 (GH PATH): CONFESSION
    ## The ending with no thorn.
    ## Sophia says the true thing.
    ## Eve says the true thing back.
    ## ===========================

label eve_ch6_glass_houses:

    scene bg evebedroom with Fade(1.0, 0.5, 1.0)
    show eve pj neutral at center with dissolve

    s "I have to confess something."

    pause 1.5

    s_thoughts "That's not what I meant to say."
    
    s_thoughts "I was going to tell her I had feelings for her."
    
    s_thoughts "I wasn't going to lead-up to it like it's a big confession. I was just going to say it. Lay it out there."

    pause 1.0

    e "...what?"

    s_thoughts "Her face doesn't change. It almost never does. But her fingers move on the edge of the blanket."

    pause 1.5

    s "Sorry. I meant -- I have something to tell you. And I don't know how to start it so I said the wrong word."

    pause 1.0

    s "I meant -- I have something I need to get off my chest."

    s_thoughts "That's worse."

    s_thoughts "Eve is very still."

    pause 2.0

    e "About what."

    s_thoughts "Not a question. A place for me to put it."

    pause 1.5

    s "About..."
    
    s_thoughts "Suddenly my brain is doing a thing."
    
    s "About me."

    pause 2.0

    s_thoughts "The laptop is still frozen on the rival's face. Her arm extended. Mid-strike."

    s_thoughts "I should sit down. I am sitting down. I'm already sitting down. Am I sitting down?"

    s_thoughts "Hands. What do I do with my hands."

    pause 1.5

    s "Can I -- can I just talk for a minute. And you don't have to do anything."

    e "Okay."

    pause 2.0
    
    s_thoughts "I don't know how it happens."
    
    s_thoughts "It just... does."

    play music mus_mourning fadein 4.0

    s "My dad left when I was twelve."

    pause 2.5

    s_thoughts "Her face."

    s_thoughts "Nothing changes on it. But something opens in the middle of the room."

    pause 1.5

    s "I have a little sister. Jenny. She was six."

    s "My mom's fine. My stepdad's -- Gary's great. I mean that. I say it in a way that sounds like I don't mean it, but I do. Gary's great."

    pause 1.5

    s "My dad was -- we were close."

    s_thoughts "My voice is doing the thing. Going flat. Like I'm reading."

    s "There was a bookstore we'd go to on Saturdays."
    
    s "He'd pick out a book for me."

    pause 1.5

    s "Sometimes he'd read it out loud."
    
    s "To me."

    pause 2.0

    e "..."
    
    e "What was the last book."

    s_thoughts "Oh."

    s_thoughts "Nobody has ever asked me that."

    pause 2.0

    s "I... I don't remember."

    s_thoughts "I'm not crying. My eyes are doing something. But I'm not crying."

    s "I remember the hot chocolate was too hot that day and I let it sit. I remember the table we sat at. But... I... I don't remember the book."

    pause 2.0

    e "Okay."

    s_thoughts "She lets the gap sit. She doesn't fill it."

    pause 1.5

    s "He didn't fight with my mom. He didn't yell. Nothing." 
    
    s "He just wasn't there one day."
    
    s "His stuff was gone."
    
    s "..."

    s "...He left a note."
    
    e "Oh."

    pause 1.0

    s "'I need to figure some things out. I love you both. I'll call.'"

    pause 2.0

    s "He called. For a while. Then less. Then even less. And eventually... I stopped picking up."

    pause 2.5

    e "How old were you? When you stopped."

    s "Sixteen."
    
    s_thoughts "She looks at me. I can't read her."

    pause 3.0

    s "I used to think... if..."

    s "I used to think if I'd paid more attention I would have seen it coming."

    pause 2.5

    s "I know that's not how it works. I know."

    s "But somewhere in my head there's still a version of me who thinks -- if I pay enough attention, nobody can surprise me by disappearing."

    pause 3.0

    s_thoughts "The laptop fan spins."

    s_thoughts "The plant sits."

    s_thoughts "Her face... is there."

    pause 2.0

    s "That's what I do. With people. I watch them." 
    
    s "I -- I take notes." 
    
    s "I had a whole thing about you, you know. In my head. A file about Eve Morse." 
    
    s "A version of Eve I was building out of details. What you ate. When you came home. Which books you touched. Your mug. Your socks."

    pause 1.5

    s "I thought I was being careful."
    
    s "I thought... I was looking for the signs."

    pause 2.5

    s "And I know it's not as bad as what you--"

    e "Don't."

    s_thoughts "Fast. The only thing she's said fast all night."

    pause 2.0

    e "It's yours. It counts."

    pause 3.0

    s_thoughts "The room is very quiet."

    s_thoughts "Now. I have to say it now or I won't."

    pause 2.0

    s "The reason I'm telling you this--"

    s_thoughts "My hands."

    s "The reason I'm telling you this is because I'm afraid you'll... you'll leave. Like he did. Like I think they all do, eventually."

    pause 1.5

    s "And I didn't want you to find out about the watching from somewhere else. I didn't want you to figure it out and think I was --"

    s_thoughts "Don't say her name."

    s "-- I didn't want you to figure it out from the outside."

    pause 2.0

    s "So. That's the thing. That's what I wanted to tell you."
    
    s_thoughts "Is it?"

    s "I don't need you to do anything with it. I just -- needed it to be in the room."
    
    s_thoughts "..."
    
    s_thoughts "I wait."

    pause 4.0

    s_thoughts "Nothing."

    s_thoughts "She's looking at the blanket. Her hands are folded on top of it. The mug is near her knee."

    s_thoughts "She hasn't moved."

    s_thoughts "Okay. Okay. This is the part where -- okay."

    pause 3.0

    s_thoughts "Say something. Please say something."

    pause 3.0

    s_thoughts "Don't rush her. You don't get to rush her."
    
    stop music fadeout 2.5

    pause 3.0

    show eve pj smile at center

    e "You're not like her after all."
    
    play music mus_eve fadein 2.5

    pause 3.0

    s_thoughts "Oh."

    pause 2.0

    s "...what?"

    pause 2.0

    e "I've been trying to decide for a while."

    s_thoughts "Her voice is very level."

    e "Not whether you were -- not whether you were going to hurt me. I knew you weren't going to hurt me. I knew that pretty early."

    pause 1.5

    e "Whether you were the same shape."

    pause 2.0

    s_thoughts "I don't breathe."

    pause 2.0
    
    show eve pj pain at center

    e "When she told me about her -- about what her parents did. To her. She told me early. Pretty early."

    pause 1.5

    e "It was blame."

    e "Blame, blame, blame. About her parents. About what they did to her." 
    
    e "Like the blaming was the point."

    pause 2.0

    e "I didn't see it then. I thought she was brave. For telling me."
    
    e "I thought we were the same."

    pause 2.5

    e "I've wondered since -- since everything -- if she used it."

    pause 1.5

    e "To justify--"

    s_thoughts "She stops."

    s_thoughts "She can't say it."

    s_thoughts "She's staring at the screen."

    pause 2.0

    s "...what she did to you?"

    pause 2.0

    e "Yeah."

    pause 3.0
    
    show eve pj neutral at center

    e "I've never said that out loud."

    pause 2.5

    s_thoughts "She looks up."

    e "You just did the opposite."

    pause 1.0
    
    show eve pj smile at center

    e "You just... acknowledged it." 
    
    e "You didn't blame anyone."

    pause 1.5

    e "Not your dad. Not your mom. Not Jenny. Not Gary."

    pause 1.0

    e "Not me."

    pause 2.0

    e "She... she couldn't have done that. I don't think."

    pause 3.0

    s_thoughts "I don't know what to do with my face."

    s_thoughts "Eyes are doing something. Still not crying."

    pause 2.0

    e "You had an Eve file."

    s "...yeah."

    e "I knew."

    pause 1.5

    e "I could feel it. Not in a bad way. It was careful. It was -- it was the opposite of being ignored."

    pause 2.0

    e "I think I liked it. A little."

    s_thoughts "Oh."

    pause 2.0

    e "Which scared me."

    pause 3.0

    e "I've been waiting to see what you'd do with it."
    
    e "When you'd eventually say the thing."
    
    s "The thing?"

    pause 1.5
    
    show eve pj neutral at center
    
    e "That you have feelings for me."
    
    s_thoughts "I freeze."
    
    s "Eve--"
    
    e "But you didn't say it."
    
    e "You just..."

    e "You just opened the file. In front of me."

    pause 2.5

    e "And it wasn't about me."

    pause 1.5

    e "It was about you."

    pause 3.0

    s_thoughts "The fan."

    s_thoughts "The plant."

    s_thoughts "Her."

    pause 2.5

    e "Sophia."

    s "Yeah."

    pause 1.5

    e "I... I need to see something."

    pause 2.0

    s_thoughts "I don't move. I can't tell if I can't move or if I'm waiting."

    s_thoughts "She moves."

    pause 1.5
    
    show eve pj flustered at center

    s_thoughts "She slides off the bed. Two steps. The blanket stays where it was."
    
    s_thoughts "I notice her socks. They don't match."
    
    s_thoughts "I'm still sitting on the bed."

    s_thoughts "Her hand comes up to the side of my face."

    s_thoughts "Careful. Like she's checking the weight of something."

    pause 2.0

    s_thoughts "She kisses me."

    pause 3.0

    s_thoughts "Quiet."

    s_thoughts "Her other hand finds my wrist. Not holding it. Just there."

    pause 2.0

    s_thoughts "When she pulls back she doesn't go far."

    pause 2.0

    e "Okay."

    pause 1.5

    s "Okay."

    pause 3.0

    s_thoughts "She doesn't move her hand from my face."

    pause 2.0
    
    e "...Yeah."
    
    s "Yeah?"
    
    e "Yeah."
    
    s "Are we..."
    
    e "I don't know yet."
    
    s "Okay."
    
    e "I think that's the point."
    
    s "Can we..."
    
    e "Yeah."
    
    s_thoughts "She kisses me. Again. Longer this time."
    
    s_thoughts "She holds my face as she does it. Her hand caresses my wrist."
    
    s_thoughts "Then she pulls back."
    
    e "Sophia?"
    
    s "Yeah?"
    
    e "Thanks."
    
    s "Why are you thanking me?"
    
    e "You let me make the first move."
    
    e "I... didn't think you were going to do that."
    
    e "I didn't think you were going to show me the file."
    
    s "Oh."
    
    s "You're... welcome."
    
    show eve pj smile at center
    
    s_thoughts "She smiles."
    
    e "Friends kiss each other, sometimes."
    
    s "Sometimes."
    
    e "Friends can cuddle and watch anime together."
    
    s "They can."
    
    e "Maybe... that's the kind of friends we can be."
    
    e "If... if you want."
    
    s "I do. I do want."
    
    e "I know you do."
    
    s_thoughts "She's teasing me."
    
    s "Yeah. I'm pretty easy to read, huh?"
    
    e "I like reading you."
    
    s "I like reading you too."
    
    s_thoughts "She kisses me again."

    s_thoughts "The laptop is still paused. The rival is still mid-strike. The plant is still catching the screen light."

    s_thoughts "The notebook -- my notebook --"
    
    s_thoughts "It's closed."

    pause 3.0

    stop music fadeout 5.0

    pause 2.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Confession{/size}"

    $ persistent.gh_seen_eve = True
    $ persistent.completed_eve_route = True
    return
