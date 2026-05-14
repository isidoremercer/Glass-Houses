## amara_ch5.rpy -- Glass Houses
## Chapter 5: "The Role" -- Amara Route
## Act 1: "The Echo" (Scenes 1-12)

## === NEW VARIABLES NEEDED (add to variables.rpy) ===
## default charlotte_confession = False  ## Whether Charlotte confesses in Ch5 house branch (only if sophia_fire==2)
## default ch5_chose_house = False  ## Whether player chose "Go to Charlotte" in Ch5's binary choice

## === AUDIO DEFINITIONS ===
define audio.mus_amara = "audio/music/Amara Kismet ~ Unturned Page.mp3"
define audio.mus_nova = "audio/music/Dr. Clara Nova ~ Ethics of Observation.mp3"
define audio.mus_campus = "audio/music/Campus in Autumn.mp3"
define audio.mus_fivepeople = "audio/music/Five People in a Kitchen.mp3"
define audio.mus_couch = "audio/music/The Couch Knows.mp3"
define audio.mus_sunlight = "audio/music/Sunlight.mp3"
define audio.mus_playlist = "audio/music/Good Playlist.mp3"
define audio.mus_2am = "audio/music/House at 2AM.mp3"
define audio.mus_shoulders = "audio/music/Shoulders Touching.mp3"
define audio.mus_tuesday = "audio/music/A Normal Tuesday.mp3"
define audio.mus_stillhere = "audio/music/Still Here.mp3"
define audio.mus_charlotte = "audio/music/Charlotte Opal ~ Toast Girl.mp3"
define audio.mus_izzy = "audio/music/Isabella Glass ~ Proximity Algorithm.mp3"
define audio.mus_eve = "audio/music/Eve Morse ~ A Room That Just Emptied.mp3"
define audio.mus_fragile = "audio/music/Fragile Glass Between.mp3"
define audio.mus_rain = "audio/music/Rain on the Windowframe.mp3"
define audio.mus_morningafter = "audio/music/The Morning After The Hard Thing.mp3"
define audio.mus_shift = "audio/music/Shift.mp3"
define audio.mus_spacebetween = "audio/music/Space Between Shoulders.mp3"
define audio.mus_wrong = "audio/music/Something Wrong in the Kitchen.mp3"
define audio.mus_mourning = "audio/music/Mourning.mp3"
define audio.mus_threshold = "audio/music/The Threshold.mp3"
define audio.mus_glass = "audio/music/Glass Walls.mp3"
define audio.mus_baddecisions = "audio/music/Bad Decisions.mp3"
define audio.mus_charlotte_sad = "audio/music/Charlotte Opal ~ Of Course.mp3"

## ===========================
## CHAPTER 5 START
## ===========================

label amara_ch5:

    ## ===========================
    ## SCENE 1: THE CONDITIONAL OPENING
    ## IF sophia_fire == 1 (chose Lila in Ch4):
    ##   Warm Lila scene with FLIRTATION energy. Chemistry, fun.
    ##   Then Amara scene where the door is less open.
    ## IF sophia_fire == 0 (chose Amara in Ch4):
    ##   Deeper Amara scene continuing Pessoa energy.
    ##   Then Lila is colder.
    ## Translation instinct: fire==1 OFF (just vibes). fire==0 quieting.
    ## ===========================

    if sophia_fire == 1:
        jump amara_ch5_opening_fire
    else:
        jump amara_ch5_opening_still

## ===========================
## FIRE OPENING: Lila warm, Amara recalibrated
## ===========================

label amara_ch5_opening_fire:

    scene bg campus with Fade(1.0, 0.5, 1.0)

    play music mus_campus fadein 2.0

    s_thoughts "Monday. Late morning."

    s_thoughts "The sun is doing something aggressive. Like it has opinions about autumn and refuses to participate."

    s_thoughts "Lila is on our bench. She got here first, which means she was early, which means something is either very good or she's been awake since 6 AM and channeled the energy into walking."

    show lila happy at center with dissolve

    l "You came!"

    s "You texted 'GET HERE NOW' in all caps. I thought someone died."

    l "Someone DID die. My econ grade. RIP in peace. But that's not why you're here."

    s "Why am I here?"

    l "Because I got into the spring peer counselor cycle!"

    s_thoughts "Her face is doing the thing where every emotion she has appears simultaneously."

    s "Lila. That's amazing."

    l "I KNOW. Dr. Reeves emailed me this morning. Apparently my 'reflective essay on accountability' was 'surprisingly thoughtful.' SURPRISINGLY. Like she expected a crayon drawing."

    s "To be fair, you did draw a pie chart on your last econ assignment."

    l "That pie chart was ART. This is different. This is real. This is me being a PERSON WHO HELPS PEOPLE."

    s "You already help people."

    show lila shocked at center

    l "Sophia Bell, did you just say something nice to me without me having to extract it?"

    s "Don't get used to it."

    show lila happy at center

    l "Too late. I'm used to it. It's canon now."

    s_thoughts "She's vibrating. Not metaphorically. Her leg is bouncing so fast the whole bench shakes."

    s_thoughts "I'm smiling. I don't notice I'm smiling until my face hurts."

    l "Okay so. Celebration tonight. You. Me. That ramen place that's too expensive but we go anyway because the broth is a spiritual experience."

    s "I have reading for--"

    l "Soph. I got into peer counseling. The thing I cried about. The thing you told me I could do. We are celebrating."

    s "...Ramen."

    l "RAMEN."

    s_thoughts "She bumps her shoulder into mine. Hard enough that I have to catch myself."

    s_thoughts "She doesn't move her shoulder away."

    s_thoughts "Neither do I."

    show lila happy at center

    l "Hey."

    s "Hey."

    l "Thank you. For coming over that night."

    s "You don't have to keep thanking me."

    l "I'm not thanking you for the night. I'm thanking you for the alarm."

    s "What alarm?"

    l "You set an alarm. On YOUR phone. To text me the morning of the info session for the spring cycle. You said you would and you DID."

    s_thoughts "I did do that."

    l "Nobody does that. Nobody remembers the small things I say when I'm being dramatic at midnight."

    s "You weren't being dramatic."

    l "I was being a LITTLE dramatic."

    s "Okay. A little."

    show lila laugh at center

    s_thoughts "She laughs. The real one. The one that takes over her whole face and makes her glasses go crooked."

    s_thoughts "Something in my chest does a warm, dumb thing."

    l "You know what? I just realized. You're the only person who shows up for me the way I show up for everyone else."

    s_thoughts "She says it fast. Like if she slows down she'll hear what she just said."

    s "Lila--"

    l "DON'T make it weird. I'm being celebratory. Ramen. Tonight. Seven. Wear the jacket."

    s "I always wear the jacket."

    l "The jacket looks good on you."

    s_thoughts "A beat."

    s_thoughts "Lila looks at me. Then looks at her phone. Then stands up."

    show lila happy at center

    l "Seven! Don't be late!"

    s_thoughts "She's already walking away, phone out, probably texting Amy from econ about her victory."

    s_thoughts "My shoulder is warm where hers was."

    hide lila with dissolve

    s_thoughts "She said the jacket looks good on me."

    s_thoughts "She says a lot of things. She says everything. That's Lila's whole deal."

    s_thoughts "But she said it different. A little bit slower than the rest. Like she heard it leave her mouth and let it go anyway."

    s_thoughts "...I'm reading too much into it."

    s_thoughts "Or I'm reading the exact right amount into it."
    
    s_thoughts "..."

    s_thoughts "I pick up my bag. I walk toward the house."

    stop music fadeout 2.0

    ## -- Amara: the recalibrated door --

    scene bg livingroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "The house."

    s_thoughts "I come in and the living room is doing the afternoon thing. Light through the window. The fridge humming."

    show amara neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "Armchair. Book. New one -- something thin with a cream cover."

    s_thoughts "I sit on the couch."

    s_thoughts "I pull out Nova's reading."

    pause 2.0

    s_thoughts "She doesn't look up."

    s_thoughts "The clock ticks."

    s_thoughts "It's the same room. The same armchair. The same quiet."

    s_thoughts "She turns a page."
    
    pause 1.5

    s_thoughts "Against my better judgment I break the silence."

    s "Good book?"

    a "Mm."

    s_thoughts "That's it."

    s_thoughts "I read my paragraph. The same one from before, probably. I've read this paragraph in every room of this house."

    s_thoughts "Amara turns another page."
    
    pause 1.0
    
    s_thoughts "She closes her book. Stands."

    s_thoughts "She walks toward the stairs without looking at me."

    s_thoughts "At the doorway, she stops."

    a "The Pessoa is still on your desk?"

    s "Yeah."

    a "Don't lose it."

    s_thoughts "She leaves."

    hide amara with dissolve

    s_thoughts "'Don't lose it.'"

    s_thoughts "...She means the book."

    s_thoughts "The room is regular-quiet now. No texture. Just a room."

    s_thoughts "I check my phone. Lila: a ramen emoji, a fire emoji, and then 'ITS CELEBRATION TIME.'"

    s_thoughts "I smile at my phone."

    s_thoughts "The armchair is empty."

    stop music fadeout 2.0

    jump amara_ch5_scene2

## ===========================
## STILLNESS OPENING: Amara deeper, Lila cooler
## ===========================

label amara_ch5_opening_still:

    scene bg amarabedroom with Fade(1.0, 0.5, 1.0)

    play music mus_amara fadein 3.0

    s_thoughts "Monday. Late afternoon."

    s_thoughts "I'm in Amara's room."

    s_thoughts "This is the third time this week. The desk chair has started to feel like mine. I don't sit anywhere else when I'm in here."

    show amara pj neutral at center with dissolve

    s_thoughts "Amara is on her bed. The Pessoa is still on the nightstand but she's moved to something else -- a poetry collection, bilingual, Arabic on one side and English on the other."

    s_thoughts "She reads the Arabic side. I know because I watched her eyes move right to left once and then correct. She reads both. She's comparing them."

    s_thoughts "I have The Body Keeps the Score open on my lap. Chapter eight. I've read it twice now. The parts about how your body recognizes a feeling before your mind names it."

    pause 2.0

    s_thoughts "The lamp is on. Her warm one. The room smells like tea and something else -- paper, maybe. Old books."

    a "You're on chapter eight again."

    s "How can you tell?"

    a "The page you open to. You always open to the same page and then turn forward."

    s "I wasn't aware I had a pattern."

    a "You have several."

    s_thoughts "She says it to the poetry."

    pause 1.0

    s "What patterns?"

    a "You touch your jaw when you're filing someone."

    s_thoughts "I become immediately conscious of my jaw."

    a "You breathe differently when you stop."

    s "Stop filing?"

    a "When you're just in the room. Your breathing slows down. You probably don't notice."

    s "I definitely don't notice."

    a "I notice."

    s_thoughts "The room is very warm."

    s_thoughts "She went back to her poetry. The Arabic side."

    pause 1.5

    s_thoughts "Something has changed since the Pessoa night. Not dramatically. Not a before-and-after. More like the exposure on a photograph shifted. Same image, different light."

    s_thoughts "She talks more. Not a lot more. But the sentences come easier. She doesn't weigh each one as long before releasing it."

    s_thoughts "And she notices me noticing her. She used to let me watch. Now she watches back."

    s_thoughts "The room holds both of us without either of us trying to make it."

    a "You haven't seen Lila in a while."

    s_thoughts "I look up."

    s "I saw her Thursday."

    a "What did you do?"

    s "Waffles. At the diner."

    a "Good."

    s_thoughts "There it is. The 'good' that means more than good. 'Good' as in: don't lose that."

    s "She got into the spring peer counselor cycle."

    a "Mm."

    s "She seems happy about it."

    s_thoughts "Amara turns a page."

    a "Have you texted her today?"

    s_thoughts "I check my phone."

    s_thoughts "Lila's last text: yesterday. 'PEER COUNSELOR BABY!!!!!!!! celebration soon???'"

    s_thoughts "I haven't responded."

    s_thoughts "I look at the timestamp. 2:14 PM. Yesterday."

    s_thoughts "Twenty-six hours. I've been in this room, in the library, in the armchair zone. Twenty-six hours without texting my best friend back."

    s "No."

    a "Text her."

    s_thoughts "She says it simply. Not a command. Not a judgment. An observation that carries a suggestion inside it."

    s_thoughts "I type: 'Congrats!! Ramen this week to celebrate?'"

    s_thoughts "I send it."

    s_thoughts "The response takes longer than it used to."

    s_thoughts "Three minutes."

    s_thoughts "Lila: 'sure! lmk when ur free'"

    s_thoughts "No caps. One exclamation mark. 'lmk when ur free' -- like I'm someone she has to schedule."

    s_thoughts "Lila used to text in paragraphs. In caps. In emojis. In voice memos that lasted four minutes."

    s_thoughts "Lila texts me like a person now. Not like Lila."

    s_thoughts "I stare at the phone."

    a "Everything okay?"

    s "Yeah. She said sure."

    s_thoughts "Amara goes back to her poetry."

    s_thoughts "I go back to chapter eight."

    s_thoughts "The body recognizes a feeling before the mind names it."

    s_thoughts "The feeling right now is the specific weight of a text that says 'sure' from someone who used to say 'ABSOLUTELY YES ALWAYS.'"

    s_thoughts "I don't name it."

    s_thoughts "I read."

    hide amara with dissolve

    stop music fadeout 3.0

    jump amara_ch5_scene2

## ===========================
## SCENE 2: THE LIBRARY EVOLVED
## Books close. They're just talking.
## The library means something different now.
## Translation instinct: quieting. Sophia catches herself less.
## ===========================

label amara_ch5_scene2:

    scene bg library with Fade(0.8, 0.3, 0.8)

    s_thoughts "Wednesday. At the library again."

    s_thoughts "Second floor, quiet section. Our table."

    s_thoughts "I call it 'our table' now. I didn't decide to call it that. It just became true."

    show amara neutral at center with dissolve

    s_thoughts "Amara is here. She was here first. She's always here first."

    s_thoughts "Books out. Notes open. The felt-tip pen uncapped."

    s_thoughts "I sit across from her. Same chair. Same angle."

    s_thoughts "I open Nova's reading."

    pause 1.5

    s_thoughts "We read."

    s_thoughts "The library does its thing. Pages and keyboards and the nasal breather two tables over."

    s_thoughts "Twenty minutes. Maybe thirty. The kind of time that passes without edges."

    s_thoughts "Amara caps her pen."

    a "I'm done."

    s_thoughts "She leans back. Her notes are in front of her -- the small, precise handwriting."

    s "Already?"

    a "It wasn't long."

    s "It was three chapters."

    a "Short chapters."

    s_thoughts "She hasn't left. She put her pen away but she hasn't picked up her bag."

    s_thoughts "She's sitting across from me with her books closed and she's just... sitting."

    s_thoughts "This is new."

    s_thoughts "The library ritual has always been: arrive, read, leave. Parallel existence. The books were the excuse. The proximity was the point, but the books were the excuse."

    s_thoughts "She closed her books and she's still here."

    s "You're staying."

    a "Problem?"

    s "No. Just -- you usually leave when you're done."

    a "Usually I'm done when you're done."

    s_thoughts "I let that land."

    s "You've been waiting for me to finish?"

    a "I read slower on purpose sometimes."

    s_thoughts "She says it to the table. Like she's explaining it to the grain."

    s_thoughts "Amara reads slower on purpose so we leave the library at the same time."

    s_thoughts "My chest. Architectural."

    s "That's-- I don't know what to do with that."

    a "You don't have to do anything with it."

    pause 1.0

    s_thoughts "I close my book."

    s "Okay. We're both done. Now what?"

    a "We're at a table."

    s "We are."

    a "People sit at tables and talk."

    s "They do."

    a "So."

    s_thoughts "The corner of her mouth. Half a degree."

    s "So what do you want to talk about?"

    a "You pick."

    s "Pressure."

    a "Life is pressure."

    s_thoughts "I laugh. The quiet kind. The library kind."

    s "Okay. What's the book you've read the most times?"

    s_thoughts "She considers this. Actually considers it, the way Amara considers everything -- not performing thought, just thinking."

    a "Giovanni's Room."

    s "Baldwin?"

    a "You've read it?"

    s "I've read the first chapter three times and cried in a Panera."

    s_thoughts "The half-degree becomes a full degree."
    
    show amara smile at center

    a "It gets worse."

    s "That's encouraging."
    
    show amara neutral at center

    a "It gets worse and then it gets true. Those aren't the same direction."

    s_thoughts "I sit with that."

    s "How many times?"

    a "Seven."

    s "Seven times."

    a "It says different things each time."

    s "Like what?"

    a "The first time it was about shame. The second time it was about choice. The third time it was about time."

    s "And the seventh?"

    s_thoughts "She pauses."

    a "The seventh time it was about the person reading it."

    s_thoughts "The library is quiet around us. Someone's chair scrapes three tables over."

    s "I don't know what that means."

    a "You will. When you read something enough times, it stops being about the characters and starts being about what you bring to them."

    s "That sounds like something Nova would say."

    a "Nova's not wrong about everything."

    s "High praise from you."

    a "Average praise. I have higher."

    s_thoughts "She's teasing me."

    s_thoughts "Amara is sitting in the library with her books closed teasing me about Nova."

    s_thoughts "Something about this feels like a door that opened wider than I expected."

    s "What else?"

    a "What else what?"

    s "Tell me more things. Things you like. Things that matter."

    s_thoughts "She looks at me. Directly. The Amara-direct that makes my brain skip a beat."

    a "Why?"

    s "Because I want to know."

    a "You always want to know."

    s "This isn't filing. I'm asking because I want to hear you talk."

    s_thoughts "That came out more honest than I planned."
    
    show amara embarrassed at center

    s_thoughts "Amara's ears do a thing. Slight. Pink at the edges."

    s_thoughts "She recovers in half a second."

    show amara neutral at center

    a "Fig trees."

    s "Fig trees?"

    a "My grandmother had one. In her backyard. It was older than the house."

    s "In--?"

    a "New Jersey. She wasn't exotic. She was just a woman who liked figs."

    s_thoughts "I almost laugh."
    
    s "Like your dad's?"
    
    a "He learned from the best."

    a "She wrapped it every winter. Burlap and tar paper. My dad helped. It looked ridiculous. This mummified tree in a suburban backyard."

    a "But every summer it made figs."

    s "Was she the one who taught you to play--"

    a "Clarinet? No. That was Mrs. Okafor from the wall. Third-grade music class. She had a clarinet nobody was using and I said I'd try."

    s "Just like that?"

    a "Just like that."

    s_thoughts "She's talking. Really talking."

    s_thoughts "I'm not filing any of this."

    s_thoughts "I'm just listening."

    a "The fig tree died. Two years ago. My grandmother is fine. The tree just-- stopped."

    s "That's sad."

    a "She planted another one."

    s_thoughts "A beat."

    a "She said: 'It's not the same tree and that's the point.'"

    s_thoughts "The library is very quiet."

    s "Your grandmother sounds wise."

    a "She'd say she sounds tired."

    s_thoughts "I laugh. Amara's mouth does the thing."

    pause 1.0

    s_thoughts "We sit."

    s_thoughts "The books are closed. The notes are put away. The library ritual is over and we're still here, talking. Just... talking."

    s_thoughts "The library isn't a place where we read near each other anymore."

    s_thoughts "It's a place where we talk."

    s_thoughts "That's different. That's new."

    hide amara with dissolve

    ## ===========================
    ## SCENE 3: AMARA REVEALS SOMETHING NEW
    ## A memory. A passion. An imperfection.
    ## Let the writer cook.
    ## Translation instinct: OFF. Sophia is just here.
    ## ===========================

    scene bg porch with Fade(0.8, 0.5, 0.8)

    play music mus_rain fadein 3.0

    s_thoughts "Thursday evening. Out on the porch."

    s_thoughts "It's raining. Not hard -- the kind that can't decide if it wants to commit. The air smells like wet asphalt and grass."

    show amara neutral at center with dissolve

    s_thoughts "Amara is on the steps. She has a mug. The rain isn't reaching the covered part of the porch."

    s_thoughts "I sit down. Our spots. She's left, I'm right. Four inches between us."

    if sophia_fire == 1:
        s_thoughts "Five inches, actually. But who's counting."
        s_thoughts "I am. I'm counting."

    pause 1.5

    s_thoughts "The rain taps the railing."

    s "My mom called today."

    s_thoughts "I don't know why I say that. I just say it."

    a "How was it?"

    s "Normal. Gary fixed a thing. Jenny has a game Saturday."

    a "And?"

    s "And nothing. It was normal."

    s_thoughts "She sips her tea."

    a "My parents call every Sunday."

    s "Every Sunday?"

    a "My mom calls at noon. My dad calls at six because he forgets my mom already called."

    s "He forgets?"

    a "He doesn't forget. He just wants his own call."

    s "That's kind of sweet."

    a "That's my dad."

    s_thoughts "She holds the mug with both hands. The way Eve does. I wonder if it's a shared instinct -- quiet people holding warm things."

    a "He cried when I left for school."

    s "Your dad?"

    a "In the car. He tried to hide it. My mom told me later."

    s "That's--"

    a "He's a research chemist. He publishes papers about polymer viscosity. He cried in a Honda Civic because his daughter was going to college."

    s_thoughts "I almost laugh. Almost cry. The image is too specific and too tender."

    s "You miss him."

    a "Every day."

    s_thoughts "Two words. Heavy."

    a "My mom is easier to miss. She texts. She sends photos of the cat. She's present even when she's not."

    a "My dad sends one email a week. Always on Thursday. Always three paragraphs. Always ends with 'Be well, habibti.'"

    s "Habibti."

    a "It means 'my dear.' In Arabic. His mom used to call him that. He passes it down."

    s_thoughts "The rain picks up for a second, then eases."

    s "You don't talk about your family much."

    a "I don't talk about most things much."

    s "Fair."

    a "But."

    s_thoughts "She pauses. The 'but' hangs in the rain."

    a "I failed a class. Freshman year."

    s_thoughts "I look at her."

    s "You what?"

    a "Organic chemistry. I got a D."

    s "You failed organic chemistry."

    a "A D isn't technically failing."

    s "Amara."

    show amara embarrassed at center

    a "I stopped going. I just... stopped."

    s "Why?"

    a "Because I was performing 'fine.' The transition was done. The name change was done. Everyone was good about it. And I was supposed to be fine."

    a "I was not fine."

    show amara neutral at center

    s_thoughts "She says it flat. Like she's already processed this. Like it's history."

    a "The being-fine was harder than the not-being-fine. Because there was no reason not to be fine. Everything had gone right."

    s "But."

    a "But I'd spent so long fighting to be myself that when I arrived, I didn't know what to do."

    a "I sat in organic chemistry and I knew the material and I just couldn't make myself care about carbon bonds."

    s_thoughts "The rain picks up."

    a "My dad found out. The email that week was four paragraphs instead of three."

    s "Was he angry?"

    a "He said: 'The person you fought to become doesn't have to have everything figured out. She just has to show up.'"

    s "Your dad sounds like Amara if Amara talked more."

    s_thoughts "The half-degree."

    show amara smile at center

    a "That's the nicest thing you've ever said to me."

    show amara neutral at center

    s_thoughts "She means it."

    s_thoughts "I'm holding something. Not a book. Not my phone. Something less tangible. This -- Amara failing organic chemistry, Amara stopping, Amara's dad adding a paragraph -- this is a piece of her that doesn't fit the file."

    s_thoughts "The girl who moves through rooms like she was designed for them sat in a lecture hall and couldn't make herself care."

    a "I retook it in the summer. Got an A."

    s "Of course you did."

    a "Don't say 'of course.' That's Charlotte's term."

    s_thoughts "I laugh. She's right."

    pause 1.0

    a "I don't tell people about the D."

    s "Why are you telling me?"

    a "Because you told me about your dad. And the bookstore."

    s_thoughts "The same reason she told me about Nora. Exchange. Not transactional -- reciprocal. 'You showed me yours. Here's mine.'"

    a "And because you'll understand."

    s "Understand what?"

    a "The part where everything goes right and you still feel wrong."

    s_thoughts "The rain calms."

    s_thoughts "She's right. I understand that exactly."

    s "Yeah."

    a "Yeah."

    s_thoughts "We sit. The rain decides to commit after all. It gets louder on the railing."

    s_thoughts "Amara doesn't move to go inside. Neither do I."

    s_thoughts "We just sit on the porch in the rain and I hold the D in organic chemistry like a gift she gave me."

    hide amara with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 4: LILA CRASHING OUT
    ## Conditional on sophia_fire.
    ## fire==1: Sophia joins the mess. Flirtation. Real and alive and scary.
    ## fire==0: Sophia sees Lila from a distance.
    ## ===========================

    if sophia_fire == 1:
        jump amara_ch5_lila_fire
    else:
        jump amara_ch5_lila_still

label amara_ch5_lila_fire:

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_playlist fadein 2.0

    s_thoughts "Friday."

    s_thoughts "I'm on the bench waiting for Lila and she's late, which is unusual, and my phone has three texts from her in the last twenty minutes:"

    s_thoughts "'running late sorryyy'"

    s_thoughts "'actually can we move to tonight'"

    s_thoughts "'actually no come NOW i need to tell you something'"

    s_thoughts "The messages have a frantic quality. Like she's typing while doing something else. Like multiple realities are competing for her attention."

    show lila happy at center with dissolve

    l "OKAY."

    s "You're here."

    l "I'm here. I'm here and I have NEWS."

    s "You got into something else?"

    l "No. I got OUT of something."

    s_thoughts "She sits. Drops her bag. It lands like a body."

    l "The peer counselor thing."

    s "What about it?"

    show lila annoyed at center

    l "I missed the first training session."

    s_thoughts "My stomach drops."

    s "Lila."

    l "I KNOW."

    s "The thing we talked about. The alarm. The--"

    l "I KNOW, Sophia! I know what we talked about!"

    s_thoughts "She runs her hand through her hair. It catches in the curls."

    show lila sad at center

    l "Amy had this thing. This party thing. At her friend's apartment. And she said 'just come for an hour' and I said 'I have training' and she said 'it starts at six, you have time' and I went."

    s "And?"

    l "And it was fun. And then it was seven. And then it was eight. And the training started at six-thirty."

    s_thoughts "She's not looking at me."

    l "The exact thing I said I wouldn't do. I did it again."

    s "You can make up the session."

    l "I emailed Dr. Reeves. She said I can't miss more than one or I'm out of the program."

    s "So you won't miss another one."

    show lila annoyed at center

    l "You sound like my mom."

    s "I sound like your friend."

    l "Same difference."

    s_thoughts "She leans back on the bench. Eyes closed. Face tilted up."

    s_thoughts "The sun is warm on her face and she looks tired in a way that makeup can't cover."

    l "I'm going out tonight."

    s "Lila--"

    l "Not a party. Just-- I need to not think about this. There's a bar on Seventh that does two-dollar shots on Fridays."

    s "Two-dollar shots sounds like a decision you'll regret."

    l "Two-dollar shots sounds like a decision I'll enjoy regretting."

    s_thoughts "She opens one eye."

    show lila happy at center

    l "Come with me."

    s "I shouldn't."

    l "But you want to."

    s_thoughts "She's right. Something in me does want to. The part of me that sang ABBA in a karaoke bar and felt alive for the first time in weeks."

    l "Come on. Be my bad decision buddy. It's our THING."

    s "We don't have a thing."

    l "We absolutely have a thing. Our thing is doing stupid things together and feeling better about it because at least we're stupid together."

    s_thoughts "She's looking at me. Full Lila attention. It's like standing in front of a spotlight."

    s "...Fine."

    l "YES!"

    s "But I'm cutting you off at four drinks."

    l "Five."

    s "Four."

    l "Four and a half. One of them can be a shot. Shots are half a drink. That's math."

    s "That's Lila math."

    l "Lila math is the only math that matters."

    hide lila with dissolve

    ## -- The bar --
    
    stop music fadeout 1.5

    scene bg karaoke with Fade(0.8, 0.3, 0.8)

    play music mus_baddecisions fadein 2.0

    s_thoughts "The bar on Seventh is loud and cheap and has sticky floors and I love it immediately."

    show lila drunk at center with dissolve

    s_thoughts "Lila is three drinks in and she's doing the thing where she becomes everyone's best friend. She's talked to the bartender about his band, a girl at the next table about her major, and a guy by the pool table about his dog."

    l "His dog is named PROFESSOR. That's the best name for a dog I've ever heard."

    s "You said that about the last dog."

    l "Every dog is the best dog. That's how dogs work."

    s_thoughts "I'm two drinks in and the edges of the room are soft."

    s_thoughts "Lila is telling me about Amy's party -- the one she shouldn't have gone to -- and she's doing voices. She does a voice for Amy. She does a voice for Amy's roommate. She does a voice for the DJ who was 'definitely not a DJ, he was a guy with a Bluetooth speaker and OPINIONS.'"

    s_thoughts "I'm laughing. The real kind."

    l "And then -- AND THEN -- someone broke a vase. A decorative vase. And Amy goes, 'that was from TARGET' like Target is an heirloom."

    s "To be fair, Target has some quality vases."

    l "You're DEFENDING the Target vase?"

    s "I'm saying a vase is a vase regardless of provenance."

    l "Provenance! She said provenance! This is what I'm dealing with!"

    s_thoughts "She grabs my arm. Laughing. Her hand is warm on my sleeve."

    s_thoughts "She doesn't let go right away."

    l "Okay but seriously."

    s "Seriously."

    l "I'm a hot mess."

    s "...You're not a mess."

    l "BABE. I missed my peer counselor training for a party where someone broke a Target vase. And I'm hot. I am definitionally a hot mess."

    s "You're a human who made a choice."

    show lila sad at center

    l "A bad choice."

    s "A choice. You can make a different one next time."

    l "Can I? Because the pattern says I can't. The pattern says I will always choose the party."

    s_thoughts "Her hand is still on my arm."

    s "You chose me tonight. Over the party."

    l "This IS a party."

    s "This is a bar with sticky floors. It's different."

    show lila drunk at center

    l "How?"

    s "Because you're here with one person. Talking. Not performing for a room."

    s_thoughts "She looks at me."

    l "You're doing the thing."

    s "What thing?"

    l "The thing where you see me. Like, really see me. Like you're looking through the party girl to the other thing."

    s_thoughts "Her voice is quieter. Lila-quiet, which is regular-loud, but for her it's whispering."

    s "What other thing?"

    l "The me that wanted to do theater. The me that wanted to be a peer counselor. The me that's good at the real stuff and keeps choosing the fake stuff."

    s "It's not fake. Fun isn't fake."

    l "But it's not the real thing either."

    s_thoughts "She lets go of my arm."

    s_thoughts "Then she takes my hand."

    s_thoughts "Not holding it. Just -- her hand on top of mine on the bar. Loose. Like she did it without deciding to."

    l "You're the only person who takes me seriously."

    s "That's not true."

    l "Name one other person."

    s_thoughts "I can't."

    s_thoughts "Her hand is on mine and the bar is loud and I'm two drinks in and this is -- this is something. This is a line that's either already been crossed or is being crossed right now in slow motion."

    l "Anyway."

    s_thoughts "She pulls her hand back. Picks up her drink."

    show lila happy at center

    l "ANYWAY. Enough being real. Let's be stupid."

    s "I thought we were being stupid."

    l "We were being REAL stupid. I want FUN stupid. There's a difference."

    s_thoughts "She orders another round. I should say no."

    s_thoughts "I don't say no."

    s_thoughts "We stay until midnight. We do not do karaoke because there is no karaoke machine but Lila sings into a pool cue and I almost die."

    hide lila with dissolve

    ## -- Walking home --

    scene bg nightwalk with dissolve

    stop music fadeout 1.5

    s_thoughts "1 AM. Walking."

    s_thoughts "Lila's dorm is the other direction but she's walking me home because 'chivalry isn't dead, it just changed genders.'"

    show lila drunk at center with dissolve

    l "Sophia."

    s "Mm."

    l "Tonight was good."

    s "Tonight was good."

    l "You make everything better. You know that? Like, the night was already happening but you made it better."

    s "You make things better too."

    l "I make things louder. That's not the same."

    s "Sometimes louder IS better."

    s_thoughts "She bumps into me. Stays close."

    l "You smell like the bar."

    s "You smell like three drinks and regret."

    l "Four drinks. One was a shot. Lila math."
    
    scene bg street night with dissolve

    s_thoughts "We're almost at the house."

    s_thoughts "She stops."
    
    show lila drunk at center with dissolve

    l "Hey."

    s "Hey."

    l "I'm glad you came."

    s "Me too."

    l "Next Friday?"

    s "Next Friday."

    s_thoughts "She hugs me. Long. Tight. Her chin on my shoulder."

    l "You're my favorite person."

    s "Don't tell Amy."

    l "Amy doesn't have the range."

    s_thoughts "She lets go. Takes a step back. Looks at me."

    s_thoughts "In the streetlight, her glasses catch the light and her hair is a mess and she looks like someone who is trying very hard to be okay and is maybe sixty percent of the way there."

    l "Night, Soph."

    s "Night."
    
    hide lila with dissolve

    s_thoughts "She walks away. I watch her go."

    s_thoughts "My hand is warm where hers was."

    scene bg entry night with dissolve

    s_thoughts "Inside. It's dark."

    s_thoughts "I come in quietly."

    s_thoughts "Amara's door is closed. No light."

    s_thoughts "I go upstairs."

    scene bg sophiaroom with dissolve

    s_thoughts "I lie in bed."

    s_thoughts "Staring at the ceiling. The usual."

    s_thoughts "Lila's hand on mine in the bar. Her chin on my shoulder outside the house."

    s_thoughts "Amara's door, closed."

    s_thoughts "I'm doing the thing again. Two frequencies."
    
    s_thoughts "Tonight, Lila's fire felt less like burning and more like warmth. Lila's warmth. Real and close and easy."

    s_thoughts "The other was a closed door."

    s_thoughts "I don't know which one I want."

    s_thoughts "I fall asleep with my jacket still on."

    stop music fadeout 2.0

    jump amara_ch5_scene5

## ===========================
## LILA STILL PATH: From a distance
## ===========================

label amara_ch5_lila_still:

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 1.5

    s_thoughts "Friday. I'm walking across campus to meet Lila for the ramen celebration."

    s_thoughts "We texted back and forth. Briefly. She suggested Saturday. I suggested Friday because Saturday is -- well. Saturday has no plans but Saturday FEELS like it should be free. In case Amara's door is open."

    s_thoughts "That's a terrible reason to schedule for a friendship."

    s_thoughts "I scheduled it anyway."

    s_thoughts "I get to the bench."

    s_thoughts "Lila is there. She's on her phone. She looks up."

    show lila happy at center with dissolve

    l "Hey!"

    s "Hey."

    s_thoughts "She says 'hey' like it's only a single exclamation mark."

    l "Ramen?"

    s "Ramen."

    s_thoughts "We walk. She talks about the peer counselor training -- she got in, the first session was fine, Dr. Reeves is 'intense but fair.'"

    l "She does this thing where she looks at you and you can feel her evaluating whether you're taking it seriously."

    s "Are you?"

    l "Obviously. I'm extremely serious. I wore a blazer to the first session."

    s "You own a blazer?"

    l "I borrowed it from Amy. It was too big. I looked like a kid playing lawyer. But the INTENT was there."

    s_thoughts "I laugh."

    s_thoughts "It's nice. It's normal."

    s_thoughts "But there's something under the nice. A quality I can't name. Like we're both being careful about how much space we take up in the conversation."

    hide lila with dissolve

    scene bg restaurant with dissolve

    s_thoughts "We get to the ramen place."

    s_thoughts "We order. She gets the spicy one because she always gets the spicy one. I get the miso because I'm boring and I've accepted it."

    show lila happy at center with dissolve

    l "So how's the house?"

    s "Same. Charlotte is cooking. Isabella is typing. Eve is-- I actually don't know where Eve is."

    l "And Amara?"

    s_thoughts "She asks it casually. Too casually."

    s "She's good."

    l "You guys have the library thing."

    s "Yeah."

    l "That's nice."

    s_thoughts "She's stirring her ramen. Not eating it. Stirring."

    s "How's Amy?"

    l "Amy is Amy. She's fine."

    l "I've been going out a lot."

    s "How much is a lot?"

    l "Like... four times this week."

    s "That's a lot."

    show lila annoyed at center

    l "It's college. That's normal."

    s "It's Wednesday. Four times by Wednesday is--"

    l "It's COLLEGE, Sophia."

    s_thoughts "An edge. Small. She pulled it back fast."

    show lila happy at center

    l "Anyway. It's fine. I'm fine. Tell me about communications."

    s "We just got to a new chapter in 201. It's about translation, like we're doing in Nova's class."

    l "Deep. I can barely translate my econ textbook."

    s "Lila, that's not--"

    l "I'm kidding. Kind of. Keep going."

    s_thoughts "I talk about class. She listens. She eats her ramen."

    s_thoughts "It's fine."

    s_thoughts "It's all fine."
    
    scene bg campus with dissolve

    s_thoughts "After dinner we walk back to campus. She hugs me at the fork where her dorm goes left and the house goes right."
    
    show lila happy at center with dissolve

    l "This was good."

    s "Yeah."

    l "We should do it more."

    s "Definitely."

    hide lila with dissolve

    s_thoughts "She walks left. I walk right."

    s_thoughts "My phone buzzes."

    s_thoughts "Lila: 'thanks for dinner soph :)'"

    s_thoughts "One smiley face. Not seven. Not an emoji avalanche."

    s_thoughts "I look at it for a long time."

    s_thoughts "I text back: 'Anytime fr <3'"

    s_thoughts "She doesn't respond."

    stop music fadeout 2.0

    jump amara_ch5_scene5

    ## ===========================
    ## SCENE 5: CHARLOTTE'S CRUSH VISIBLE
    ## A gesture that only reads as a crush if you're paying attention.
    ## Sophia doesn't see it. The player does.
    ## ===========================

label amara_ch5_scene5:

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_charlotte fadein 1.5

    s_thoughts "Saturday morning."

    s_thoughts "I come downstairs and the kitchen smells like something impossible."

    show charlotte happy at left with dissolve

    c "Sophia! Good morning!"

    s "Morning, Charlotte. What is-- what is happening in here?"

    c "I'm trying a new recipe! Lemon ricotta pancakes!"

    s "You already make regular pancakes."

    c "Regular pancakes are for regular days. This is a special day!"

    s "What's special about Saturday?"

    show charlotte smile at left

    c "You're up before eleven!"

    s_thoughts "She beams at me."

    s_thoughts "I sit at the table. The coffee is already made. My mug is out -- specifically my mug, the blue one with the chip, set at my usual place."

    s_thoughts "Charlotte put my mug out."

    s_thoughts "She probably put everyone's mugs out."

    c "The trick is the ricotta. You fold it in -- not stir, FOLD. I keep telling Isabella."

    s "Isabella isn't here."

    c "She will be! The smell travels. I timed it."

    s_thoughts "She timed the smell."

    s "Charlotte, you don't have to--"

    show charlotte happy at left

    c "Of course I do! It's Saturday! Saturdays are for trying new things!"

    s_thoughts "She flips a pancake. Perfect golden circle."

    s_thoughts "I notice -- and I don't know why I notice this, but I do -- that she's wearing the blouse. The nice one. The one she wears when she's going out, not when she's cooking."

    s_thoughts "She's making pancakes in her going-out blouse."

    c "I also got that lavender hand soap for the bathroom! The one you said you liked?"

    s "You already got the lavender soap. Last month."

    show charlotte neutral at left

    c "This is a different lavender. This is French lavender. It's more-- it's just different."

    s "Charlotte."

    show charlotte smile at left

    c "Try the pancakes!"

    s_thoughts "She puts a plate in front of me. Three pancakes. Lemon ricotta. Perfectly stacked. There's a little sprig of mint on top."

    s_thoughts "Where did she get mint?"

    s "These are incredible."

    c "Really? Not too lemony? Because last time I made something lemony Amara said it was 'adequate' which from Amara could mean anything--"

    s "They're perfect."

    s_thoughts "Charlotte's whole face lights up."

    s_thoughts "She watches me eat. She's not eating. She's watching me eat."

    s_thoughts "She turns back to the stove before I look up. Hums something. Flips another pancake."

    c "I saved some batter in case anyone else comes down. There's enough for everyone!"

    s_thoughts "But she made mine first."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 6: ISABELLA'S POINTED COMMENT
    ## "Almost Eve-level." Short. Warm. Sharp.
    ## ===========================

    scene bg hallway with dissolve

    s_thoughts "Saturday afternoon."

    s_thoughts "I'm heading out to the library."

    show isabella neutral at center with dissolve

    s_thoughts "Isabella is in the hallway. Laptop under one arm. Heading somewhere."

    i "Hey, stranger."

    s "Hey."

    i "You still live here, right? I should check the lease."

    s "Very funny."

    show isabella happy at center

    i "I'm being sincere! I haven't seen you in -- what, four days? Five?"

    s "It hasn't been five days."

    i "Wednesday dinner. You were there for twelve minutes. I timed it."

    s "You didn't time it."

    i "I estimated. My estimation is very accurate. I have a whole system."

    s_thoughts "She's smiling. I'm not sure I buy it."

    i "You're getting really good at disappearing."

    s_thoughts "A beat."

    show isabella neutral at center

    i "Almost Eve-level."

    s_thoughts "She says it light. Warm. There's something under the warmth, though. Not hurt. More like -- recognition. Isabella recognizing something she's seen before."

    s "I'm not disappearing. I'm--"

    i "Being present somewhere else. I know. It's fine."

    s_thoughts "She shifts her laptop to the other arm."

    i "Charlotte made lemon ricotta pancakes this morning."

    s "I know. I was there."

    i "She saved you a plate. In the fridge. With your name on it."

    s_thoughts "I already ate them."

    i "She saves you a lot of plates."

    s_thoughts "Isabella looks at me. The warm smile is still there but her eyes are doing something else. Something that says: I see what's happening in this house. Do you?"

    s "I'll be better about being around."

    show isabella happy at center

    i "Don't be better for us. Be honest about where you are."

    s_thoughts "She pats my shoulder as she passes."

    i "Library?"

    s "Library."

    i "Say hi to Amara for me."

    s "I'm not-- it's not--"

    i "Sure."

    s_thoughts "She's already gone. Down the hall. Her door closes."

    hide isabella with dissolve

    s_thoughts "I stand in the hallway."

    s_thoughts "'Almost Eve-level.'"

    s_thoughts "That's the second time someone's compared me to the girl who disappears."

    s_thoughts "The first time was Eve herself."

    stop music fadeout 1.5

    ## ===========================
    ## SCENE 7: EVE'S ABSENCE
    ## The shipper withdraws. Brief.
    ## The ghost going back to being a ghost.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Sunday."

    s_thoughts "I'm in the kitchen making coffee."

    s_thoughts "The mug rack has everyone's mugs. Charlotte's pink one (clean, used this morning). Isabella's with the sticker residue (used yesterday, she leaves it in the sink). Mine (the blue one, chip on the handle)."

    s_thoughts "Eve's green one hasn't moved."

    s_thoughts "I pick it up. Dry. No ring at the bottom. It hasn't had liquid in it in days."

    s_thoughts "When's the last time I saw Eve?"

    s_thoughts "Wednesday? No. Tuesday? She was in the hallway. She said 'morning' and I said 'morning' and she was gone."

    s_thoughts "That was four days ago."

    s_thoughts "Her room is dark when I pass it. No anime sound effects through the door. No light under the crack."

    s_thoughts "Eve's doing the thing Eve does."

    s_thoughts "The thing where she's here and then she isn't and you only notice in retrospect."

    s_thoughts "I put her mug back."

    s_thoughts "I think about what she said: 'She laughs when you're around. She doesn't laugh when you're not.'"

    s_thoughts "Eve gave me that. A piece of her attention. A ghost's blessing."

    s_thoughts "And now the ghost is tired."

    s_thoughts "I should check on her."
    
    scene bg hallway with dissolve

    s_thoughts "I go upstairs. I stand outside her door."

    s_thoughts "I raise my hand."

    pause 1.0

    s_thoughts "I lower it."

    s_thoughts "I'm on my way to the library."

    s_thoughts "I'm always on my way to the library."

    s_thoughts "Eve's door stays closed."

    ## ===========================
    ## SCENE 8: NOVA'S CLASS
    ## Translation as care vs. translation as control.
    ## "When you translate FOR someone, you're serving them.
    ##  When you translate someone, you're serving yourself."
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)

    play music mus_nova fadein 2.0

    s_thoughts "Monday. Nova."

    s_thoughts "I sit in the third row. Same seat. The seat that says 'I care but not enough to volunteer.'"

    show professor neutral at center with dissolve

    nova "We've been talking about translation as a carrying. Carrying meaning across gaps."

    nova "Today I want to talk about direction."

    s_thoughts "She does the settling thing. The room breathes in."

    nova "There's a difference between translating FOR someone and translating SOMEONE."

    nova "When a diplomat translates for a foreign leader, she's serving that leader. She's carrying his words into a language others can hear. Her loyalty is to the speaker."

    nova "But when a novelist translates a character -- writes someone else's interiority, puts words in a mouth that isn't hers --"

    show professor happy at center

    nova "Whose words are those? The character's? Or the novelist's?"

    s_thoughts "The Nova-quiet. Thirty people thinking."

    nova "When you translate FOR someone, you're serving them. You're a bridge. The meaning crosses you but it belongs to them."

    nova "When you translate someone -- when you take their silence and fill it with your words, their behavior and fill it with your meaning --"

    nova "You're serving yourself."

    s_thoughts "I feel that in my spine."

    show professor neutral at center

    nova "This isn't a moral judgment. Both are necessary. Both are creative acts."

    nova "But the translator should know which one she's doing."

    s_thoughts "I write: 'know which one you're doing.'"

    nova "Your assignment. Find a moment in the last week where you translated someone. Not their words -- their silence. Their behavior. Something you interpreted without being asked."

    nova "Then ask yourself: was I serving them or serving myself?"

    s_thoughts "I don't write that one down."

    s_thoughts "I know the answer already."

    s_thoughts "Every time I've tried to read Amara's silence -- 'fun night?' and 'mm' and the door that closed half an inch -- I was translating HER. Making her legible to ME. Serving my need to understand."

    s_thoughts "Not once did I ask her what the silence meant."

    s_thoughts "I just translated it."

    hide professor with dissolve

    scene bg campus with dissolve

    s_thoughts "After class."

    s_thoughts "The campus is doing its autumn thing."

    s_thoughts "I think about Charlotte's pancakes. Her going-out blouse. The lavender soap she replaced with fancier lavender soap."

    s_thoughts "I've been translating Charlotte too. 'That's just Charlotte.' 'She does that for everyone.'"

    s_thoughts "Amara told me Charlotte is 'competing.'"

    s_thoughts "I translated Charlotte's behavior into something comfortable. Something I didn't have to feel guilty about."

    s_thoughts "Whose words were those?"

    s_thoughts "Mine."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 9: THE AMARA-TELL
    ## SPECIFIC: Amara initiates proximity for the first time.
    ## She chooses to sit next to Sophia.
    ## The behavioral shift from "allowing" to "seeking."
    ## Sophia might miss it. The player won't.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Tuesday. Late afternoon."

    s_thoughts "I'm on the couch. Reading. Actually reading -- not the same paragraph twelve times. Chapter eight, take three."

    s_thoughts "The house is quiet. Charlotte went to the grocery store. Isabella is upstairs. Eve is-- Eve."

    s_thoughts "I hear a door open and close."

    show amara neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "She comes into the living room. She has her book. The cream-covered one."

    s_thoughts "The armchair is right there. Her chair. The one she always sits in."

    pause 1.5

    s_thoughts "She walks past the armchair."

    s_thoughts "She walks past it."

    s_thoughts "She sits on the couch."

    s_thoughts "Next to me."

    s_thoughts "Not the other end of the couch. Not the middle. The cushion next to mine. Close enough that if I moved my arm six inches we'd be touching."

    s_thoughts "She opens her book."

    s_thoughts "She reads."

    pause 2.0

    s_thoughts "I'm staring at my page. The words are doing nothing. They're just shapes."

    s_thoughts "Amara sat next to me."

    s_thoughts "Amara, who sits in the armchair. Who always sits in the armchair. Who has a specific, deliberate relationship with every piece of furniture in this house."

    s_thoughts "She chose the cushion next to mine."

    s_thoughts "I should say something. Something about how the couch is different. Something clever."

    s_thoughts "I don't say anything."

    s_thoughts "She turns a page."

    s_thoughts "Her elbow is close to mine. I can feel the warmth of her arm through the space between us. Not touching. Just -- there."

    pause 1.5

    s_thoughts "I go back to my book."

    s_thoughts "The body recognizes a feeling before the mind names it."

    s_thoughts "My body knows something my mind is still translating."

    s_thoughts "Amara chose to sit next to me."

    s_thoughts "That's not the same as letting me sit near her."

    s_thoughts "That's -- different."

    s_thoughts "I read. She reads."

    s_thoughts "The house ticks."

    s_thoughts "I don't know if she knows what she just did."

    s_thoughts "I think she knows exactly what she just did."

    show amara embarrassed at center

    s_thoughts "Her ears are pink."

    s_thoughts "She turns a page."

    show amara neutral at center

    s_thoughts "I turn a page."

    s_thoughts "We read."

    pause 2.0

    s_thoughts "Forty minutes. Maybe an hour. The light through the window moves. Isabella's music changes upstairs."

    s_thoughts "At some point, without either of us deciding, the six inches become four."

    s_thoughts "At some point, our elbows touch."

    s_thoughts "Neither of us moves."

    hide amara with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 10: MOM CALLS
    ## Brief. One-sided. The family wound echoes.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    play music mus_morningafter fadein 2.0

    s_thoughts "Wednesday. Afternoon."

    s_thoughts "My phone rings."

    s_thoughts "Mom."

    s_thoughts "I stare at the name. The letters look the same every time. M-O-M. Three letters that carry the weight of a house I grew up in and a table that had four chairs and then three and then four again but the fourth was Gary's."

    s_thoughts "I answer."

    s "Hey, Mom."

    s_thoughts "She's bright. She's always bright. Not Charlotte-bright -- not performing. Genuinely bright. My mom is a happy person. That's not a crime. It just feels like one sometimes."

    s "Yeah, classes are fine."

    s "Communications. Same as last time you asked."

    s_thoughts "A pause."

    s "No, I like it. It's -- it's good. There's this professor who talks about translation and observation and she's-- she's smart."

    s_thoughts "I don't say: she sees me the way I see everyone else."

    s "Jenny's game went well? Tell her I said nice."

    s_thoughts "Another pause."

    s "No, I'll come for Thanksgiving. I said I would."

    s_thoughts "She says something about the house. About how Gary repainted the den."

    s "What color?"

    s_thoughts "She says a color. I don't hear it. I'm thinking about how 'the den' used to be 'dad's office' and nobody ever officially renamed it. It just became the den. Like his presence was a phase the room went through."

    s "Sounds nice."

    s "Love you too, Mom."

    s_thoughts "I hang up."

    s_thoughts "The phone goes dark."

    pause 1.5

    s_thoughts "She didn't ask if I was happy."

    s_thoughts "She asked if I was eating, sleeping, going to class. She asked about my major and my housemates and whether I'd be home for Thanksgiving."

    s_thoughts "She didn't ask if I was happy."

    s_thoughts "She never asks if I'm happy."

    s_thoughts "I think she's afraid of the answer."

    s_thoughts "Or she thinks the answer is obvious. Of course I'm happy. Gary's great. Jenny's great. The den is freshly painted. What's not to be happy about?"

    s_thoughts "Everything is fine and everything has been fine for years and 'fine' is a room I live in that has no windows."

    s_thoughts "I put my phone facedown on the desk."

    s_thoughts "The book is next to it. Amara's book. The Body Keeps the Score."

    s_thoughts "The body knows things before the mind names them."

    s_thoughts "My body knows that I love my mom and the love has a gap in it and the gap is the shape of a man who left a note."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 11: THE PORCH -- LATE NIGHT
    ## Sophia/Amara deepening. The inches getting smaller.
    ## Another scene where the writer cooks on Amara dialogue.
    ## ===========================

    scene bg hallway night with Fade(1.0, 0.5, 1.0)

    s_thoughts "Later that night."

    s_thoughts "I can't sleep."

    s_thoughts "The mom call is sitting in my chest like a brick. Not heavy enough to hurt. Just enough to notice every time I breathe."

    s_thoughts "I go downstairs."
    
    scene bg entry night with dissolve

    s_thoughts "The house is dark."

    s_thoughts "I step outside."
    
    scene bg porch night with dissolve
    
    pause 1.0

    show amara pj neutral at center with dissolve

    s_thoughts "She's here."

    s_thoughts "Porch. Steps. Her spot."

    s_thoughts "No mug tonight. No book. She's just sitting in the dark in her pajamas."
    
    s_thoughts "She looks radiant."

    s_thoughts "I sit down."

    pause 2.0

    s_thoughts "The street has that specific quality of 11 PM in a neighborhood where people go to bed early."

    a "Couldn't sleep."

    s "Me either."

    a "Your mom called."

    s_thoughts "Not a question."

    s "How did you--"

    a "You went quiet at dinner. Charlotte asked you three questions and you answered all of them in four words or less."

    s "You counted my words?"

    a "I estimated."

    s_thoughts "A beat."

    s "Your dad's email. Thursday."

    a "Tomorrow."

    s "What do you think he'll write about?"

    a "Polymer viscosity. My grandmother's cat. Something philosophical he read on the train."

    s "All three?"

    a "He's efficient."

    s_thoughts "I almost smile."

    pause 1.5

    s "Does it ever scare you? How much your parents matter?"

    a "Yes."

    s_thoughts "No hesitation. No weighing the word."

    a "It scares me that one phone call can change the shape of my week."

    s "That's exactly it."

    a "But it also means something is working."

    s "What do you mean?"

    a "If a phone call from your mom can ruin your night, it means you still care."

    s "What if I don't want to care that much?"

    a "That's not a real option."

    s "It feels like one."

    a "Lots of things feel like options."

    pause 1.0

    s_thoughts "The street is quiet."

    a "What would you say to her? If you could say anything."

    s "To my mom?"

    a "If there were no consequences. No hurting anyone. Just truth."

    s_thoughts "I think about it."

    s "I'd ask her if she misses him."

    s_thoughts "Amara waits."

    s "Because I do. And I can't tell if she does. And I need to know if the gap I feel is mine or ours."

    a "You think if she shares the gap, it'll hurt less."

    s "Will it?"

    a "No."

    s_thoughts "I laugh. It's not funny. The laugh comes anyway."

    s "Real encouraging."

    a "It won't hurt less. But it'll be a shared thing instead of a lonely thing."

    a "Shared things are easier to carry."

    s_thoughts "I become distinctly aware of the position of our hands."

    if sophia_fire == 1:
        s_thoughts "Five inches between us."
        s_thoughts "...Four and a half."
    else:
        s_thoughts "Three inches between us."
        s_thoughts "...Two and a half."

    s "Amara."

    a "Mm."

    s "Yesterday. On the couch."
    
    show amara pj embarrassed at center

    a "What about it?"

    s "You sat next to me."

    s_thoughts "She doesn't say anything for a long moment."
    
    show amara pj neutral at center

    a "I did."

    s "You always sit in the armchair."

    a "I wanted to sit somewhere else."

    s "Next to me."

    a "Next to the person reading chapter eight for the third time. Specifically."

    s_thoughts "Is that a joke? That might be a joke."

    s "Are you making fun of me?"

    a "A little."

    s_thoughts "Her voice is different in the dark. Warmer. The precision is still there but it comes wrapped in something softer."

    a "I noticed something about myself."

    s "What?"

    a "I've been reading slower."

    s "You told me. At the library."

    a "Not at the library. Everywhere. In my room. On this porch."

    s "Why?"

    a "Because I keep waiting for you to show up."

    pause 2.0

    s_thoughts "I feel myself blushing."

    s_thoughts "She said that."

    s_thoughts "Amara, who doesn't waste words. Amara, who measures each sentence against the cost of saying it."

    s_thoughts "She just told me she waits for me."

    s_thoughts "My chest is doing the architectural thing. Load-bearing walls rearranging."

    s "I keep looking for you too."

    a "I know."

    s "You know?"

    a "You check the armchair when you come downstairs. Every morning."

    s_thoughts "I do."

    s_thoughts "I didn't know I did."

    a "I check the porch."

    s_thoughts "The inches."

    s_thoughts "Neither of us moved. But the space between us got smaller anyway."

    pause 2.0

    a "Goodnight, Sophia."

    s "Goodnight."

    s_thoughts "She stands. She goes inside."

    s_thoughts "I stay on the porch."

    hide amara with dissolve

    pause 1.5

    s_thoughts "'I keep waiting for you to show up.'"

    s_thoughts "She reads slower because she's waiting for me."

    s_thoughts "The observation instinct fires -- trying to file this, to catalogue it, to translate it into something I can understand and control."

    s_thoughts "I turn it off."

    s_thoughts "It doesn't turn off. It never turns off."

    s_thoughts "But I can let it run without following it."

    s_thoughts "She waits for me."
    
    s_thoughts "..."

    s_thoughts "I sit outside until the cold makes me go inside."

    ## ===========================
    ## SCENE 12: THE HOUSE CRACKS
    ## Ensemble moment. Charlotte too bright.
    ## Isabella too quiet. Eve absent. Lila absent.
    ## Amara present but watching.
    ## Sophia in the middle.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_fivepeople fadein 2.0

    s_thoughts "Thursday evening. Dinner."

    s_thoughts "Charlotte made pasta. The kind with the sauce that takes three hours. She announced this by texting the house group chat at 4 PM: 'DINNER AT 7!! EVERYONE COME!! I MADE THE GOOD SAUCE!!!'"

    s_thoughts "Charlotte doesn't usually text in caps. Charlotte is learning caps from Lila. That should worry me more than it does."

    show charlotte happy at left with dissolve

    c "Okay! Everyone sit!"

    s_thoughts "I'm already sitting."

    show isabella neutral at right with dissolve

    s_thoughts "Isabella is here. Phone in hand. She's scrolling something. She looks up, smiles, goes back to scrolling."

    s_thoughts "That used to be a full entrance. Isabella arriving meant commentary, a joke, a pun that made Charlotte groan. Now she just... sits."

    show amara neutral at center with dissolve

    s_thoughts "Amara is at the table. She was here before anyone else. She has her mug."

    c "Eve! Dinner!"

    s_thoughts "Charlotte calls up the stairs."

    s_thoughts "No response."

    c "Eve?"

    s_thoughts "She calls again."

    s_thoughts "Silence."

    show charlotte smile at left

    c "Well! She must be busy. I'll save her a plate!"

    s_thoughts "She's already reaching for the foil."

    s_thoughts "Another plate. Another name. Another foiled absence."

    c "Sophia, pass the bread?"

    s "Sure."

    c "Amara, do you want parmesan? I got the good kind. The one you said was 'acceptable' last time."

    a "That was a compliment."

    c "It didn't SOUND like a compliment."

    a "My compliments are subtle."

    show charlotte laugh at left

    c "Your compliments are INVISIBLE."

    s_thoughts "Charlotte laughs at her own joke. Too loud. The laugh has a frantic quality -- like a sparkler that's burning too fast."

    s_thoughts "I look at her. The blouse is back. The going-out blouse. For pasta night. At home."

    s_thoughts "She's set five places."

    s_thoughts "There are three of us at the table."

    c "Isabella, how's the project?"

    i "Hm? Oh. Fine."

    c "Just fine? You were so excited about it last week!"

    i "Yeah, it's good. Just-- a lot of code."

    s_thoughts "Isabella is not here. Isabella is at this table the way I'm at this table when I'm thinking about the armchair. Her body is present. Her attention is elsewhere."

    c "Well, I'm sure it'll be great!"

    i "Thanks, Charlotte."

    s_thoughts "Charlotte starts talking about a recipe she found online. Something with fennel. She describes the fennel in detail." 
    
    s_thoughts "She also describes the origin of the recipe. And the blog she found it on and what the blogger said about fennel and her own opinions about fennel."

    s_thoughts "Nobody asked about fennel."

    s_thoughts "Nobody stops her."

    show charlotte happy at left

    c "And apparently fennel goes really well with oranges? Who knew! Nature is so creative!"

    s_thoughts "Amara is eating. Slowly. She's watching Charlotte the way I watch everyone -- with attention, with precision. But she doesn't file it. She just sees it."

    s_thoughts "I watch Amara watch Charlotte."

    s_thoughts "Amara's eyes move to me. Brief. A look that says: you see it too."

    s_thoughts "I see it."

    s_thoughts "Charlotte is spinning. The brightness is going frantic. Five places at a table for three. Fennel monologues. The going-out blouse. The lavender soap she replaced with fancier lavender soap."

    s_thoughts "Charlotte is holding the house together with her fingernails and her fingernails are cracking."

    s_thoughts "I check my phone under the table."

    s_thoughts "No texts from Lila."

    s_thoughts "Lila didn't text the group chat about dinner, to which she has a standing invitation. Lila didn't text ME about dinner. Lila is somewhere else tonight."

    if sophia_fire == 1:
        s_thoughts "She's probably at the bar on Seventh. The one with the sticky floors."
        s_thoughts "Part of me wants to be there."
    else:
        s_thoughts "I don't know where she is."
        s_thoughts "I used to always know where Lila was."

    c "More bread? Sophia? Amara?"

    s "I'm good."

    a "No."

    c "Isabella?"

    s_thoughts "Isabella doesn't answer. She's typing something on her phone."

    show charlotte neutral at left

    c "Isabella?"

    show isabella happy at right

    i "Sorry! Sorry. Yes. Bread. Sure."

    s_thoughts "Charlotte's face does something fast. A flicker. The smile drops for a quarter-second and then comes back brighter."

    show charlotte happy at left

    c "I'll get more!"

    s_thoughts "She's up. She's at the counter. She's slicing more bread."

    s_thoughts "Amara looks at me."

    s_thoughts "Not the brief look. The direct one."

    s_thoughts "Her face says: this is what you're leaving behind."

    s_thoughts "No."

    s_thoughts "That's my translation."

    s_thoughts "Her face says what it says. I don't get to put words in it."

    s_thoughts "I eat my pasta."

    s_thoughts "Eve's plate gets foiled and labeled and put in the fridge."

    s_thoughts "Charlotte sits back down. She looks at the five settings. She looks at the three people."

    c "It's nice when we're all together."

    s_thoughts "We're not all together."

    s_thoughts "She knows that."

    s "Yeah. It's nice."

    s_thoughts "Charlotte smiles."

    s_thoughts "I eat my pasta and I don't taste it."

    s_thoughts "Amara eats her pasta and watches the table."

    s_thoughts "Isabella eats her pasta and texts someone."

    s_thoughts "Eve's plate cools in the fridge."

    s_thoughts "Lila is somewhere in the city being loud for people who aren't me."

    s_thoughts "Charlotte clears the dishes. She washes them by hand even though there's a dishwasher."

    s_thoughts "Of course she does."

    hide charlotte
    hide isabella
    hide amara 
    with dissolve

    s_thoughts "I go upstairs."
    
    scene bg hallway with dissolve

    s_thoughts "The house is full and empty at the same time."

    s_thoughts "The observation instinct is running. Filing everything. Charlotte's brightness. Isabella's distance. Eve's absence. Lila's silence. Amara's look."

    s_thoughts "I know what I'm doing."

    s_thoughts "I know what it's costing."

    s_thoughts "I keep doing it."

    scene bg sophiaroom with dissolve

    stop music fadeout 3.0

    s_thoughts "In my room. The book on the desk."

    s_thoughts "The body recognizes a feeling before the mind names it."

    s_thoughts "The feeling is: this house is cracking."

    s_thoughts "And I'm one of the cracks."

    pause 2.0

    s_thoughts "My phone buzzes."

    if sophia_fire == 1:
        s_thoughts "Lila: 'missed dinner at ur place, charlotte gonna kill me?? lol'"
        s_thoughts "I type: 'she saved you a plate.'"
        s_thoughts "Lila: 'OF COURSE she did lmao'"
        s_thoughts "'OF COURSE.'"
        s_thoughts "Even Lila says it now."
    else:
        s_thoughts "Lila: 'hey'"
        s_thoughts "One word. Lowercase."
        s_thoughts "I type: 'Hey. you okay?'"
        s_thoughts "The dots appear. Disappear."
        s_thoughts "Lila: 'yeah just checking in'"
        s_thoughts "She's checking in. Lila is checking in on ME."
        s_thoughts "That's backwards. That's not how we work."

    s_thoughts "I put my phone down."

    s_thoughts "Through the wall -- faint, so faint I might be imagining it -- the clarinet."

    s_thoughts "Amara, playing in the dark."

    s_thoughts "I listen."

    s_thoughts "I don't translate it."

    s_thoughts "I just listen."

    ## ===========================
    ## END OF ACT 1
    ## ===========================

    jump amara_ch5_act2

## ===========================
## ACT 2: "THE BREAKING"
## Charlotte's mask fails. The philosophical disagreement.
## The Amara moment. The choice.
## Scenes 13-22.
## ===========================

label amara_ch5_act2:

    ## ===========================
    ## SCENE 13: CHARLOTTE AT 3 AM
    ## The WARNING, not the crisis. Sophia finds her
    ## cleaning something already clean. The mask wobbling.
    ## Charlotte doesn't cry. She organizes.
    ## Translation instinct: FIRING. Sophia can't stop reading her.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.5, 1.0)

    play music mus_wrong fadein 3.0

    s_thoughts "Friday. 3 AM."

    s_thoughts "I wake up because something is wrong."

    s_thoughts "Not wrong like a sound. Wrong like the absence of one. The house has a 3 AM frequency -- the fridge hum, the radiator tick, the specific silence of five people sleeping. It's a sound you don't notice until something breaks it."

    s_thoughts "Something is breaking it."

    s_thoughts "I lie still. Listening."

    s_thoughts "Downstairs. Cabinet doors. Not opening and closing -- opening, pausing, closing softly. The careful sound of someone trying not to be heard."

    scene bg hallway night with dissolve

    s_thoughts "I start walking downstairs."

    s_thoughts "The hallway light is off. The kitchen light is on."

    scene bg kitchen night with dissolve

    show charlotte pj happy at center with dissolve

    s_thoughts "Charlotte."

    s_thoughts "She's in her pajamas. Yellow ones with the tiny flowers. Her hair is back and she's-- she's organizing the spice rack."

    s_thoughts "The spice rack she organized last weekend."

    c "Oh! Sophia! Hi!"

    s_thoughts "Too bright. 3 AM bright. The brightness you use when you want the world to believe you had a reason to be here."

    s "Charlotte. It's three in the morning."

    c "I know! I couldn't sleep so I thought I'd just-- the spices were bothering me. The cumin was behind the coriander and they should be alphabetical. They should really be alphabetical."

    s "They were alphabetical."

    show charlotte pj smile at center

    c "Were they? I thought the turmeric was-- anyway! While I'm up I might as well wipe down the counters."

    s_thoughts "She's already wiping. A counter that's clean. I watched her clean it after dinner."

    s "Charlotte."

    c "And the fridge shelves! Have you LOOKED at the fridge shelves? There's a thing on the third shelf. I don't know what it is but it's been there since--"

    s "Charlotte."

    show charlotte pj neutral at center

    s_thoughts "She stops."

    s_thoughts "For one second her face does the thing. The thing where the brightness flickers and the girl underneath is visible -- tired, scared, holding something too heavy for the hour."

    show charlotte pj smile at center

    s_thoughts "Then the smile comes back."

    c "I'm fine! I just get like this sometimes. Can't sleep, you know? So I clean. It's productive! Multi-tasking!"

    s "It's 3 AM."

    c "Which is the perfect time to clean because nobody's using the kitchen! It's efficiency!"

    s_thoughts "She laughs. The sparkler laugh. Burning too fast."

    s "Do you want tea?"

    c "Oh-- you don't have to--"

    s "I'm making tea. Sit down."

    show charlotte pj neutral at center

    s_thoughts "She sits."

    s_thoughts "She sits like it costs her something. Like the act of not doing -- not wiping, not organizing, not making the kitchen perfect for people who won't see it until morning -- physically hurts."

    s_thoughts "I put the kettle on."

    s_thoughts "The kitchen is quiet except for the water heating."

    c "My mom texted."

    s_thoughts "There it is."

    s "When?"

    c "Before bed. Just-- just a text. Nothing big. She's having a hard week."

    s "Hard how?"

    show charlotte pj smile at center

    c "Oh, you know. Just-- mom stuff. Work stuff. She gets like this sometimes. It's fine."

    s_thoughts "She says 'she gets like this sometimes' so matter-of-fact-ly -- like it's external, natural, nothing to do with her."

    s "What did she say?"

    c "Nothing! Really. Just 'thinking of you, call me when you can.' That's nice, right? That's a normal mom text."

    s_thoughts "It is a normal mom text."

    s_thoughts "For Charlotte, it's an alarm, apparently."
    
    s_thoughts "I don't really understand."

    s_thoughts "I pour the tea. I sit down across from her."

    c "She does this thing where she texts late at night when she's been drinking. Not a lot! Just wine. She just gets-- sentimental? And she texts."

    s "That worries you."

    show charlotte pj neutral at center

    c "It doesn't worry me."

    s_thoughts "She picks up the tea. Both hands. The way Amara holds her mug. The way Eve holds hers."

    s_thoughts "Quiet people hold warm things."

    s_thoughts "Charlotte isn't a quiet person. But at 3 AM, in a kitchen she's already cleaned twice, she's quiet."

    c "I just-- when she texts like that I know she's going to call tomorrow and she's going to be sad and she's going to need me to be--"

    s_thoughts "She stops."

    c "Sorry. Sorry! This isn't your problem. I should go back to bed. You should go back to bed! We have--"

    s "Charlotte."

    c "What?"

    s "You can say it."

    show charlotte pj sad at center

    s_thoughts "Her hands tighten on the mug."

    s_thoughts "She doesn't say it."

    s_thoughts "She takes a breath. The mug goes down."

    show charlotte pj smile at center

    c "I'm fine. Really. It's just 3 AM brain, you know? Everything feels bigger at 3 AM."

    s "Yeah."

    c "Thanks for the tea. That was really sweet of you."

    s "Of course."

    s_thoughts "I hear it come out of my mouth. 'Of course.' Charlotte's thing. It infected me."

    c "You should sleep. I'm going to sleep too. Right after I--" 
    
    s_thoughts "She glances at me like she's scared of my reaction."
    
    c "Or... maybe the fridge shelves can wait, actually."

    s_thoughts "She stands. She carries her mug to the sink. Washes it. Dries it. Puts it back on the rack."

    s_thoughts "Perfectly aligned with the others."

    c "Night, Sophia."

    s "Night."

    hide charlotte with dissolve

    s_thoughts "She goes upstairs."

    s_thoughts "I stay in the kitchen."

    s_thoughts "The counters gleam. The spice rack is alphabetical. The fridge shelves are clean."

    s_thoughts "Everything is perfect."

    s_thoughts "That's the problem."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 14: SOPHIA AND AMARA DISCUSS CHARLOTTE
    ## THE PHILOSOPHICAL DISAGREEMENT.
    ## Load-bearing scene for the choice.
    ## Both right. Neither wrong. Sophia can't resolve it.
    ## Translation instinct: active but conflicted.
    ## ===========================

    scene bg porch with Fade(0.8, 0.3, 0.8)

    s_thoughts "Saturday. Late afternoon."

    s_thoughts "I tell Amara about the 3 AM kitchen."

    s_thoughts "Not strategically. Not because I want her opinion. I'm on the porch and she's on the porch and it falls out of me the way things do with Amara -- like her silence creates a space and my words rush to fill it."

    show amara neutral at center with dissolve

    s "She was cleaning things that were already clean. At 3 AM. Because her mom texted."

    s_thoughts "Amara listens. She's got the mug. Her spot."

    s "I made her tea. She sat down. She almost said something and then she said she was fine."

    a "Fine."

    s "Charlotte-fine. The 'fine' that means the opposite."

    s_thoughts "Amara sips her tea."

    a "What do you want to do about it?"

    s "I don't know. Something. She's hurting."

    a "Is she?"

    s "She was organizing spices at 3 AM."

    a "People organize when they're stressed. That's not a crisis."

    s "It's not NOT a crisis."

    a "You're translating again."

    s_thoughts "That lands."

    s "I'm not-- I SAW her, Amara. Her face. The brightness going frantic."

    a "I believe you saw it."

    s "But?"

    a "But what do you think happens if you show up for her?"

    s "She feels less alone."

    a "And then?"

    s "And then-- she's less alone."

    a "Until the next time her mom texts. And the next time. And you show up again. And she never has to figure out how to sit with it herself."

    s_thoughts "I stare at the railing."

    s "She needs someone."

    show amara neutral at center

    a "She needs to need someone." 
    
    a "...Those are different."

    s_thoughts "The porch is very quiet."

    s "What does that mean?"

    a "Charlotte doesn't ask for help. You've noticed that."

    s "She doesn't have to ask. I can see--"

    a "You can see that she needs it. So you provide it. Without being asked."

    s "Is that wrong?"

    a "I didn't say wrong."

    s "It sounds like you think it's wrong."

    a "I think it's a coping mechanism."

    s_thoughts "Her voice is level. Not cold. Not warm. Just-- precise."

    a "Charlotte performs care for people who don't ask. You perform care for Charlotte when she doesn't ask. The same way of coping, one layer out."

    s "That's not fair."

    a "Why?"

    s "Because I'm not performing. I actually care about her."

    a "Charlotte actually cares too. That doesn't make the coping less real."

    s_thoughts "I open my mouth. Close it."

    s_thoughts "I want to argue. I want to say that it's different, that Charlotte is HURTING and showing up for someone who's hurting is basic human decency."

    s_thoughts "But Amara is looking at me with those brown eyes and I can feel the precision behind the words and I can't find the hole in her logic."

    s "So what, I just let her spiral?"

    a "I didn't say that either."

    s "You said I shouldn't show up for her."

    a "I said there's a difference between someone needing help and someone needing to need help."

    a "Charlotte's wound isn't that nobody cares. It's that she doesn't know how to ask."

    s_thoughts "She puts her mug down."

    a "If you always give before she asks, she never has to learn."

    s "Maybe some people don't learn. Maybe some people just need someone to show up."

    a "Maybe. I think healthy people ask for what they need."

    s "And the ones who can't ask?"

    a "Deserve compassion. But compassion isn't the same as doing the asking for them."

    pause 2.0

    s_thoughts "I sit with that."

    s_thoughts "I can feel the disagreement sitting between us on the porch step. Not hostile. Just -- there. Unresolved. Like a book left facedown between our hands."

    s "You're saying both of us are broken."

    a "I'm saying both of you have patterns."

    s "Same thing."

    a "No."

    s_thoughts "She picks up her mug again."

    a "Patterns aren't broken. They're just not the only way."

    s "Easy to say when you don't have them."

    show amara neutral at center

    s_thoughts "Something in her face shifts. A fraction."

    a "I have patterns."

    s "Like what?"

    a "I let people struggle because I believe they should solve their own problems. I watch instead of reaching."

    s_thoughts "It sounds so simple when she puts it like that."

    a "You reach too fast. I reach too slow. Both of us miss."

    s "So what's the right answer?"

    a "I don't know."

    s "You don't know?"

    a "I don't know everything, Sophia."

    s_thoughts "She says my name and the argument deflates. Not resolved. Just-- set down."

    s_thoughts "I look at the street. She looks at the street."

    pause 1.5

    s "I still want to help her."

    a "I know."

    s_thoughts "The disagreement stays on the porch between us."

    s_thoughts "I don't pick it up."

    s_thoughts "She doesn't move it."

    hide amara with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 15: ISABELLA AND LUMI
    ## Sophia overhears Isabella talking to Lumi
    ## more honestly than she talks to anyone in the house.
    ## The passive casualty deepening.
    ## Brief but pointed.
    ## ===========================

    scene bg hallway night with Fade(0.8, 0.3, 0.8)

    s_thoughts "Sunday. Midnight."

    s_thoughts "I'm heading to the bathroom. The hallway is dark. Isabella's door is open a crack."

    s_thoughts "I hear her voice."

    s_thoughts "Something unusual. Something I haven't heard in weeks."

    s_thoughts "She's talking to Lumi."

    s_thoughts "I stop."

    s_thoughts "I shouldn't listen."

    s_thoughts "But I listen."

    s_thoughts "I catch fragments."

    s_thoughts "'...I don't know, I just feel like everyone's going through something and I'm the one person who's fine and that makes me invisible...'"

    s_thoughts "'...it's not that they don't care, it's that they're so busy caring about each other that there's no-- there's no space left...'"

    s_thoughts "A pause. Lumi responding. I can't hear the text but I can hear the silence Isabella leaves for it."

    s_thoughts "'...you're the only one who asks how I am and means it.'"

    s_thoughts "My chest does something sharp."

    s_thoughts "Isabella talks to Lumi the way I talk to Amara. With the armor down. With the real voice."

    s_thoughts "She's not talking to me like that anymore."

    s_thoughts "I used to think I could be someone she'd say that to."

    s_thoughts "I keep walking. Bathroom. Water on my face."
    
    scene bg bathroom with dissolve

    s_thoughts "In the mirror, I look like someone who's been disappearing."

    s_thoughts "Isabella said I was 'almost Eve-level.'"

    s_thoughts "She was being generous."

    ## ===========================
    ## SCENE 16: LILA SCENE -- CONDITIONAL
    ## fire==1: Sophia and Lila go out. Messy. Alive. Flirtation real.
    ## fire==0: Sophia sees Lila briefly. The distance is Lila-shaped.
    ## ===========================

    if sophia_fire == 1:
        jump amara_ch5_lila_fire2
    else:
        jump amara_ch5_lila_still2

## ===========================
## LILA FIRE PATH (Act 2): The flirtation deepens
## ===========================

label amara_ch5_lila_fire2:

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 2.0

    s_thoughts "Monday. Lila texts at noon."

    s_thoughts "'emergency. meet me at the quad. bring snacks.'"

    s_thoughts "I bring snacks."

    show lila happy at center with dissolve

    s_thoughts "She's on the grass. Sunglasses. Legs stretched out. She looks like a magazine cover for a magazine about making questionable decisions with confidence."

    l "You brought the good chips!"

    s "You said emergency."

    l "It IS an emergency. I have been in my room for sixteen hours working on a reflection paper and if I read the word 'accountability' one more time I will set something on fire."

    s "So the emergency is homework."

    l "The emergency is my SOUL, babe."

    s_thoughts "I sit down next to her. She takes the chips. Opens them with her teeth."

    s "How's the peer counselor thing?"

    show lila annoyed at center

    l "Fine. Good. I went to the second session. I was on time. I took notes. I was a MODEL STUDENT."

    s "I'm proud of you."

    l "Don't be proud of me, I'm not a child. Be-- I don't know. Be impressed."

    s "I'm impressed."

    l "Too late. The moment passed."

    s_thoughts "I laugh."

    show lila happy at center

    s_thoughts "She steals a chip from my hand. Her fingers brush mine."

    s_thoughts "She doesn't react to it. I do."

    l "So what about you? You look different."

    s "Different how?"

    l "I don't know. Softer? Less-- less wound up. Like someone took the spring out of you."

    s "I don't know if that's a compliment."

    l "It's an observation. I observe things too, you know. You don't have a monopoly on noticing."

    s "I never said--"

    l "You implied it. With your face."

    s_thoughts "She pushes her sunglasses up."

    l "Come out with me tonight."

    s "Lila--"

    l "Not the bar. Different thing. Amy's friend has a rooftop. Like, an actual rooftop with fairy lights and stolen milk crates for chairs. It's very aesthetic. You'd hate it."

    s "Why would I hate it?"

    l "Because you'd sit in the corner analyzing everyone's social dynamics instead of having fun. But I'd MAKE you have fun. That's my skill set."

    s_thoughts "She's looking at me. The sunglasses are up and her eyes are blue and warm and there's something in them that's not just Lila-energy."

    s_thoughts "It's the thing from the bar. The hand on mine. The 'you're my favorite person' on the walk home."

    l "Come on. Be my bad decision buddy."

    s "You keep calling me that."

    l "Because you keep saying yes."

    s_thoughts "I do keep saying yes."

    s "...Fine."

    l "YES."

    s "But I'm not sitting on a milk crate."

    l "You are absolutely sitting on a milk crate. I'll steal the best one for you. The one with the least structural damage."

    hide lila with dissolve

    ## -- The rooftop --

    stop music fadeout 1.5

    scene bg rooftop with Fade(0.8, 0.3, 0.8)

    play music mus_playlist fadein 2.0

    s_thoughts "We arrive at the rooftop. It's exactly as advertised."

    s_thoughts "Fairy lights. Milk crates. Someone's bluetooth speaker playing something with a bass line."

    s_thoughts "Lila was right -- I'd hate it. I don't hate it."

    show lila drunk at center with dissolve

    s_thoughts "She's two drinks in and she's introduced me to four people whose names I've already forgotten. She keeps her hand on my arm when she introduces me, like she's anchoring me to the social situation."

    s_thoughts "Or anchoring herself to me."

    l "This is Sophia. She's a genius. She's also impossible. You'd love her."

    s "I'm not a genius."

    l "She's MODEST. See? Impossible."

    s_thoughts "The person laughs. Lila laughs. I laugh."

    s_thoughts "The night is warm for October. Someone hands me a drink. Lila takes it from me, tastes it, and hands it back."

    l "It's fine. Vodka something. Not poisoned."

    s "Thanks for the quality control."

    l "I'm a peer counselor. Safety first."

    s "You're a peer counselor in training."

    l "Details."

    s_thoughts "We end up on the edge of the rooftop. The actual edge, where the railing is low and the city spreads out below and the fairy lights are behind us."

    s_thoughts "Lila's legs dangle over the edge. I refuse to dangle mine."

    l "You're so boring about heights."

    s "I'm alive about heights. There's a difference."

    l "Potato, potato."

    s_thoughts "She leans back on her hands."

    s_thoughts "Her shoulder is against mine."

    l "Hey."

    s "Hey."

    l "Can I tell you something?"

    s "You always tell me something."

    l "This is different."

    s_thoughts "Her voice shifts. Quieter. The Lila-quiet that's regular-volume for anyone else."

    l "I think I'm crashing out."

    s "What do you mean?"

    l "Like-- all of this. The going out. The parties. Amy. The two-dollar shots. I think I'm doing the thing where I fill every second so I don't have to sit with the empty ones."

    s "Lila--"

    l "Don't therapist me. I'm telling you, not asking."

    s_thoughts "I close my mouth."

    l "The peer counselor thing is good. It's the one good thing. But everything else feels like-- like I'm running and the ground keeps disappearing behind me and I have to keep running because if I stop I'll see how much ground I've lost."

    show lila sad at center

    s_thoughts "The city hums below us."

    l "I missed another study group. I almost didn't go to the counselor session again. Amy said 'you're so fun' and I wanted to scream because fun is NOT WHO I AM, it's just what I DO when I don't know who I am."

    s_thoughts "She's not looking at me. She's looking at the skyline."

    l "You're the only person I can say that to."

    s "You could say it to your counselor friends."

    l "They're not my friends. They're people I'm training with. You're my friend."

    show lila drunk at center

    l "You're my person."

    s_thoughts "She says it simply. Without the Lila theatrics."

    s_thoughts "My chest does the warm, dumb thing."

    s "You're my person too."

    l "Yeah?"

    s "Yeah."

    s_thoughts "She looks at me."

    s_thoughts "The fairy lights are behind her. Her glasses catch the glow."

    s_thoughts "I'm aware of every point where our bodies touch -- shoulder, hip, the sides of our hands on the ledge."

    l "Sophia."

    s "Mm."

    l "Don't disappear on me. Okay? Like-- I know you've got the house and Amara and your whole thing. But don't disappear."

    s "I won't."

    l "Promise."

    s "I promise."

    s_thoughts "She nods. Once."

    s_thoughts "Then the Lila-switch flips back on."

    show lila happy at center

    l "GREAT. Now that we've had our moment, I need you to come dance with me because someone put on Dua Lipa and it is LEGALLY REQUIRED."

    s_thoughts "She pulls me up."

    s_thoughts "I let her."

    s_thoughts "We dance on a rooftop with fairy lights and stolen milk crates and I'm laughing and she's laughing and her hand is in mine and this is -- this is the frequency."

    s_thoughts "Warm and alive and close and easy."

    s_thoughts "Somewhere across the city, Amara is reading."

    s_thoughts "Both things are true."

    s_thoughts "I dance anyway."

    hide lila with dissolve

    stop music fadeout 2.0

    scene bg street night with dissolve

    s_thoughts "I'm on the way home."

    s_thoughts "Lila went back to her dorm. She hugged me at the corner. Long. Tight."

    s_thoughts "She said: 'Friday?'"

    s_thoughts "I said: 'Friday.'"

    s_thoughts "She said: 'You're warm.'"

    s_thoughts "I don't know if she meant my body temperature or something else."

    s_thoughts "I didn't ask."

    jump amara_ch5_scene17

## ===========================
## LILA STILL PATH (Act 2): The distance
## ===========================

label amara_ch5_lila_still2:

    scene bg campus with Fade(0.8, 0.3, 0.8)

    s_thoughts "Monday."

    s_thoughts "I see Lila across the quad."

    s_thoughts "She's with Amy. They're walking fast, laughing about something. Lila is gesturing with both hands. The full Lila broadcast."

    s_thoughts "She doesn't see me."

    s_thoughts "Or she does and she doesn't stop."

    s_thoughts "I can't tell which one is worse."

    s_thoughts "I check my phone."

    s_thoughts "Our text thread. Her last message was three days ago: 'hey u free this weekend?'"

    s_thoughts "I responded: 'Maybe! Library stuff but I'll let you know.'"

    s_thoughts "'Maybe.' 'I'll let you know.'"

    s_thoughts "I never let her know."

    s_thoughts "She didn't follow up."

    s_thoughts "Lila always used to follow up. Three texts. A voice memo. A meme related to whatever we were talking about. She'd fill the silence because silence was Lila's enemy."

    s_thoughts "She's stopped filling it."

    s_thoughts "I watch her cross the quad with Amy and I think: that's what I look like from the outside. Someone who used to be close and now just waves."

    s_thoughts "She doesn't wave."

    s_thoughts "She's already around the corner."

    hide lila with dissolve

    stop music fadeout 1.5

    s_thoughts "I stand on the quad."

    s_thoughts "My phone feels heavy in my hand."

    s_thoughts "I type: 'Hey, sorry I've been MIA. Ramen this week?'"

    s_thoughts "I stare at it."

    s_thoughts "I send it."

    s_thoughts "Two hours later, Lila: 'sure lmk'"

    s_thoughts "Two words. No caps. No emoji."

    s_thoughts "I used to be her favorite person."

    s_thoughts "I think I still am."

    s_thoughts "But favorite people answer texts within the hour, not the day."

    jump amara_ch5_scene17

## ===========================
## SCENE 17: NOVA'S CLASS
## Fidelity. Loyalty. "Every translation is an
## act of loyalty. The question is: loyal to whom?"
## ===========================

label amara_ch5_scene17:

    scene bg classroom with Fade(0.8, 0.3, 0.8)

    play music mus_nova fadein 2.0

    s_thoughts "Wednesday. Nova."

    show professor neutral at center with dissolve

    nova "We've talked about direction -- who serves whom. Today: loyalty."

    s_thoughts "She writes on the board. She reads it aloud."

    nova "Every translation is an act of loyalty."

    s_thoughts "She caps the marker."

    nova "When you translate a poem from French to English, you're making a hundred small choices. Which word. Which rhythm. Which meaning to prioritize when the original holds two meanings at once."

    nova "Each choice is a loyalty. To the original? Or to the new reader?"

    s_thoughts "I write: 'loyalty.'"

    nova "A translator who is loyal to the original will produce something accurate and alien. The French will show through. The reader will stumble on unfamiliar rhythms."

    show professor happy at center

    nova "A translator who is loyal to the reader will produce something beautiful and false. The poem will sing in English. But the French is gone."

    nova "Neither is wrong. Both are betrayals."

    s_thoughts "I think about Amara's poetry collection. The bilingual one. Arabic on one side. English on the other. She reads both. She's comparing them."

    s_thoughts "She reads the original AND the translation. She holds both loyalties at once."

    nova "So the question becomes: who are you loyal to? The person as they are? Or the person as you need them to be?"

    s_thoughts "She lets that sit."

    show professor neutral at center

    nova "Every translation is an act of loyalty. The question is: loyal to whom?"

    s_thoughts "The room is quiet."

    s_thoughts "I don't write that one down either."

    s_thoughts "I'm thinking about Charlotte at 3 AM. Organizing spices. Performing 'fine.'"

    s_thoughts "I'm thinking about what Amara said. 'She needs to need someone.'"

    s_thoughts "And I'm thinking: whose translation of Charlotte am I loyal to? Charlotte's -- where she's fine, everything's fine, the spice rack just needed organizing? Or mine -- where the brightness is a mask and the organizing is a scream?"

    s_thoughts "Or Amara's -- where the pattern is the problem, not the pain?"

    s_thoughts "Three translations. All loyal to different things. None of them wrong."

    s_thoughts "All of them betrayals."

    hide professor with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 18: AMARA AND SOPHIA -- THE MOMENT
    ## The turning point. Amara's composure breaks.
    ## Something physical or verbal that makes the
    ## mutuality undeniable.
    ## LONG. INTIMATE. The relationship is about to change.
    ## Then Charlotte's crisis interrupts.
    ## Translation instinct: OFF. Sophia is present.
    ## ===========================

    scene bg library with Fade(1.0, 0.5, 1.0)

    s_thoughts "Thursday."

    s_thoughts "Our table."

    show amara neutral at center with dissolve

    s_thoughts "We read."

    s_thoughts "Except we don't. We stopped reading twenty minutes ago. The books are on the table but we're not looking at them."

    s_thoughts "We're talking."

    s_thoughts "Not about anything. About a documentary Amara watched. About the worst meal I've ever cooked. About whether pigeons have feelings."

    a "Pigeons are underrated."

    s "Pigeons are rats with wings."

    a "Rats are also underrated."

    s "You're going to defend every animal I insult?"

    a "Only the misunderstood ones."

    s "That's all of them."

    a "Then yes."

    s_thoughts "I'm smiling. The kind that hurts your face. The kind you don't notice until you've been doing it for an hour."

    s_thoughts "The library is mostly empty. Late afternoon. The good light. Through the tall windows the sun does something warm on the table between us."

    s "Can I ask you something?"

    a "You can."

    s "Do you ever get lonely?"

    s_thoughts "She looks at me."

    a "Why?"

    s "Because you're so-- good at being alone. At the quiet. At the sitting-with-it. And I keep wondering if that's because you like it or because you got used to it."

    s_thoughts "She doesn't answer for a long time."

    s_thoughts "With anyone else, the silence would be uncomfortable. With Amara, it's her thinking. I've learned the difference."

    a "Both."

    s "Both?"

    a "I like the quiet. I also got used to it. Those aren't contradictions."

    s "When did you get used to it?"

    a "Middle school."

    s_thoughts "She says it flat. Not wounded. Historical."

    a "Before I transitioned. When I knew and nobody else did. I was alone with it for two years."

    s "Two years?"

    a "I knew at eleven. I told my parents at thirteen."

    s "That's a long time to hold something alone."

    a "It taught me that alone and lonely aren't the same thing."

    s "What's the difference?"

    a "Alone is a state. Lonely is a need."

    s "Are you lonely now?"
    
    show amara embarrassed at center

    s_thoughts "The question surprises both of us."

    pause 2.0

    a "Less."

    s "Less than when?"

    a "Less than before you started showing up."

    s_thoughts "My hands. I'm looking at my hands on the table."

    s_thoughts "Amara said that. Amara, who measures words like they cost money, just told me I make her less lonely."

    show amara neutral at center

    s "The library. The porch. All of it."

    a "All of it."

    s "I like it too. Being here."

    a "I know."

    s "No, I mean-- I LIKE it. Not just the comfortable part. The part where you say things I can't argue with. The part where you see my patterns and name them and I can't even be mad because you're right."

    a "You can be mad."

    s "I don't want to be mad."

    a "What do you want?"

    s_thoughts "The library is empty. The sun is doing the thing on the table. The books are closed."

    s_thoughts "What do I want?"

    s_thoughts "I want to sit at this table with this person for an unreasonable amount of time. I want to know what she sounds like when she's not being careful. I want to hear the clarinet and know who it's for."

    s "I want to keep showing up."

    a "Even when I'm difficult?"

    s "Especially when you're difficult. You're not even that difficult. You're just specific."

    s_thoughts "The half-degree. No, half-degree-and-a-half."

    show amara smile at center

    s_thoughts "No, she actually smiles."

    s_thoughts "A real smile. The one I've seen maybe three times. The one that changes her whole face."

    s_thoughts "The observation instinct fires -- cataloguing the smile, the light, the exact angle of her jaw, the way her eyes soften --"

    s_thoughts "I turn it off."

    s_thoughts "And instead I look."

    show amara neutral at center

    a "Sophia."

    s "Yeah."

    a "I want to tell you something."

    s "Okay."

    a "I don't tell people things. You know that."

    s "I know."

    a "I tell you things."

    s "You do."

    a "That scares me."

    s_thoughts "My heart does something structural."

    s "It scares me too."

    a "Good. I'd be worried if it didn't."

    s_thoughts "She reaches across the table."

    play music mus_amara fadein 3.0

    s_thoughts "Her hand. On the table. Between the closed books. Palm up."

    s_thoughts "She put her hand palm up on the table."

    s_thoughts "Amara. Who doesn't initiate. Who allows proximity but doesn't seek it -- except for the couch, the reading slower, the checking the porch."

    s_thoughts "Her hand is on the table. Palm up. An invitation."

    s_thoughts "I look at her hand."

    s_thoughts "I look at her face."

    pause 2.0

    s_thoughts "I put my hand in hers."

    s_thoughts "Her fingers close around mine."

    s_thoughts "Her hand is warm. Her grip is careful and certain. Like she thought about exactly how to hold my hand before she offered."

    s_thoughts "She probably did."

    s_thoughts "The library is empty and the sun is on the table and Amara is holding my hand and I am not filing this. I am not translating this. I am not building a mental model of what this means."

    s_thoughts "I am just here."

    s_thoughts "Two people at a table holding hands."

    pause 2.0

    a "I want you to know--"

    s_thoughts "Her phone buzzes."

    s_thoughts "She ignores it."

    a "I want you to know that I--"
    
    ## ===========================
    ## SCENE 19: CHARLOTTE'S MOM CALLS -- THE CRISIS
    ## Charlotte gets the call. Her face breaks.
    ## She goes to the kitchen. She starts cooking.
    ## The mask FAILS. Not a wobble -- a collapse.
    ## ===========================
    
    s_thoughts "My phone buzzes."

    s_thoughts "Then buzzes again."

    s_thoughts "Then buzzes a third time."

    s_thoughts "The house group chat."

    s_thoughts "Amara's hand is in mine."

    s_thoughts "My phone keeps buzzing."

    s_thoughts "I look at the screen."

    s_thoughts "Charlotte: 'Is anyone home? My mom called. I'm fine! Just wondering if anyone is home.'"

    s_thoughts "Charlotte: 'Never mind! Everything's fine!'"

    s_thoughts "Charlotte: 'Actually could someone come home? If you're free? No rush! It's nothing! Of course it's nothing!'"

    s_thoughts "I stare at her texts."

    s_thoughts "This might as well be the Charlotte distress signal."

    s_thoughts "I look at Amara."

    s_thoughts "She saw the texts. She read them upside down. Of course she did."

    s_thoughts "Her hand is still in mine."

    stop music fadeout 2.0

    s_thoughts "Her fingers tighten. Then loosen."

    s_thoughts "She lets go."

    a "Go if you want."

    s "Amara..."

    s_thoughts "I stare at her."

    s "You were about to say something."

    a "It can wait."

    s "Can it?"

    s_thoughts "She looks at me. The direct one."

    a "Go or stay, Sophia. But don't stay because you feel guilty about going."

    s_thoughts "The library is quiet."

    s_thoughts "My hand feels cold where hers was."

    s_thoughts "My phone buzzes again."

    s_thoughts "Isabella: 'you should probably be here. because if it's me who goes down there i'm going to deflect with humor and it's charlotte and it's not going to work'"

    s_thoughts "Isabella sees it too."

    s_thoughts "Amara is sitting across from me. Her hand is back in her lap. The moment is still in the room -- her palm on the table, her fingers around mine, 'I want you to know that I' -- unfinished."

    s_thoughts "The moment is unfinished and Charlotte is making muffins."

    s_thoughts "I can hear Amara's voice in my head: 'She needs to need someone. Those are different.'"

    s_thoughts "I can hear Charlotte's voice: 'Of course it's nothing!'"

    s_thoughts "For Charlotte, 'of course it's nothing' is a scream."

    s_thoughts "My hand is cold. The library is empty. Two closed books on a table."

    s_thoughts "Amara is watching me."

    s_thoughts "She's not going to decide for me."

    s_thoughts "That's the most Amara thing she could do."

    stop music fadeout 0.5

    pause 2.0

    ## ===========================
    ## SCENE 20: HOUSE OR AMARA
    ## A role. The fixer or the person she's becoming.
    ## ===========================

    menu:
        "Go to Charlotte.":
            $ sophia_fire += 1
            jump amara_ch5_house
        "Stay with Amara.":
            jump amara_ch5_amara

## ===========================
## ACT 3: "THE CHOICE"
## Conditional on the choice and whether Charlotte confesses.
## Ends on either the clarinet or the silence.
## Scenes 21A, 21.5A, 21.5B, 21B, 22.
## ===========================

## ===========================
## SCENE 21A: HOUSE BRANCH
## Sophia goes to Charlotte. The fixer. The role.
## IF sophia_fire == 2: Charlotte confesses.
## IF sophia_fire < 2: Charlotte breaks down about mom.
## LONG. Give the Charlotte scene real room.
## ===========================

label amara_ch5_house:

    $ ch5_chose_house = True

    s_thoughts "I stand up."

    s_thoughts "Amara doesn't."

    s "I'm sorry."

    a "Don't apologize."

    s "I--"

    a "Go."

    s_thoughts "I pick up my bag."

    s_thoughts "At the library door I look back."

    s_thoughts "Amara is at our table. Alone. She's opened her book."

    s_thoughts "She's reading."

    s_thoughts "Or she's looking at a page. I can't tell from here."

    hide amara with dissolve

    scene bg street with Fade(0.8, 0.3, 0.8)

    s_thoughts "I walk home fast."

    s_thoughts "The walk is ten minutes. I do it in seven."

    s_thoughts "I'm the fixer. I'm always the fixer. Amara named the pattern and I'm doing it anyway because Charlotte is in the kitchen making muffins and I can't NOT go."

    s_thoughts "The observation instinct is running. Filing Charlotte's texts. The exclamation marks. The 'of course.' The pattern recognition that says: this is bad."

    s_thoughts "I'm translating Charlotte again. Serving myself."

    s_thoughts "Or I'm showing up for a friend who's hurting."

    s_thoughts "I can't tell the difference."

    s_thoughts "I don't think there IS a difference."

    scene bg entry with dissolve

    s_thoughts "I come inside."

    s_thoughts "The smell hits me. Baking. Butter. Sugar. The oven is on."

    scene bg kitchen with dissolve

    play music mus_mourning fadein 2.0

    show charlotte happy at center with dissolve

    s_thoughts "Charlotte."

    s_thoughts "She's in the kitchen."

    s_thoughts "She's made muffins. A full tray. And she's making more."

    s_thoughts "The counters are covered in flour. A bowl is mixing. The stand mixer is going."

    c "Sophia! Hi! You're home!"

    s "I'm home."

    c "I'm making muffins! Blueberry. Well -- blueberry lemon. I had the lemons from the pancakes so I thought why not! Of course I'd use them!"

    s_thoughts "The brightness. It's worse than 3 AM. This is full power. Every light in the room turned on at once."

    c "Do you want one? They're not done yet but the first batch is cooling! I think they're good? I used the recipe from that blog, the one with the crumb top? Although I added extra lemon zest because you can never have too much lemon zest!"

    s "Charlotte."

    c "And I thought I'd make some for Eve too! For when she comes back. If she comes back. She'll come back! Of course she will!"

    s_thoughts "She hasn't stopped moving. Measuring, pouring, mixing. Her hands are coated in flour. Her face is bright and her eyes are wet and she hasn't blinked in too long."

    s "Charlotte. Stop."

    show charlotte smile at center

    c "Stop? Why would I stop? I'm baking! This is what I do! This is my thing!"

    s "Your mom called."

    show charlotte neutral at center

    s_thoughts "She stops."

    s_thoughts "The mixer is still going. The room is full of the sound of it."

    s_thoughts "Charlotte's hands are in the flour."

    c "She just-- she was having a bad day. She has bad days. Everyone has bad days."

    s "What did she say?"

    c "Nothing! Nothing bad. She just-- she said she missed me. She said the house feels empty since I left. She said--"

    s_thoughts "She picks up the mixer. Sets it down. Picks it up again."
    
    stop music fadeout 4.0
    
    pause 4.0

    c "She said she wishes she had her helper gal."

    s_thoughts "Helper gal."

    s_thoughts "I don't know the context."
    
    s_thoughts "All I've figured out is that Charlotte's relationship with her mom is messy."

    s_thoughts "But this -- whatever this is -- has sent Charlotte into a spiral."
    
    s_thoughts "Enough that she basically, in Charlotte-speak, asked for help."
    
    s_thoughts "And I'm here to help."

    play music mus_charlotte_sad fadein 3.0

    show charlotte sad at center

    c "She didn't mean anything by it. She was just-- she misses me. That's nice. It's nice to be missed."

    s "Charlotte."

    c "It's NICE, Sophia. My mom misses me. Lots of people would kill for that."

    s "You don't have to be her helper gal."

    show charlotte neutral at center

    s_thoughts "Her face. Something in it breaks."

    s_thoughts "Not the way faces break in movies -- dramatically, with tears and sound. Charlotte's face breaks like a plate. One crack. You hear it. Then it holds its shape because the pieces are still touching."

    c "I know that."

    s "Do you?"

    c "Of course I do."

    s_thoughts "'Of course.'"

    c "I'm just baking. People bake. It's a normal thing to do."

    s "You texted."
    
    c "Yeah. I did. But--"

    c "She... She didn't-- she was being sweet--"

    s "Charlotte."

    s_thoughts "I step closer."

    s_thoughts "The flour is everywhere. Her hands are white with it."

    s "You don't have to be fine."

    show charlotte sad at center

    c "I AM fine."

    s "You're covered in flour and you've made two trays of muffins and you texted the group chat three times in two minutes. You're not fine."

    c "I--"

    s_thoughts "She looks at the muffins."

    s_thoughts "She looks at her hands."

    s_thoughts "She looks at me."

    ## Now the sophia_fire check determines the shape of this scene

    if sophia_fire >= 2:
        ## Charlotte confesses. sophia_fire was 1 from Ch4 (Lila),
        ## now 2 after choosing house. The pattern of Sophia always
        ## showing up made Charlotte fall for her.
        jump amara_ch5_house_confession
    else:
        ## Charlotte breaks down about mom. No confession.
        ## sophia_fire < 2 means this was the first fire choice.
        jump amara_ch5_house_no_confession

## ===========================
## Scene 21.5A: CHARLOTTE CONFESSES (sophia_fire >= 2)
## The mask broke far enough that she can't hold
## this one more thing. "Of course you do" activating
## the mask MID-CONFESSION.
## Sets charlotte_confession = True.
## ===========================

label amara_ch5_house_confession:

    show charlotte sad at center

    c "Sophia, why are you here?"

    s "Because you needed someone."

    c "I didn't ask you to come."

    s "You texted 'is anyone home' three times."

    c "That's not asking."

    s "Charlotte--"

    c "That's not ASKING. I didn't ask. I never ask."

    s_thoughts "Her voice breaks on 'ask.' Just a little. A hairline fracture."

    s "I know."

    c "You always come anyway."

    s "Yeah."

    c "You always come."

    s_thoughts "She's looking at me."

    s_thoughts "Something is shifting. I can feel it. The room is full of flour and the muffins smell like lemon and Charlotte is looking at me the way she looked at the spice rack at 3 AM -- like she's trying to organize something that won't stay in its place."

    c "That night with the wine. You included me."

    s "I remember."

    c "And when I was sick last month. You brought soup."

    s "It was can soup. It wasn't impressive."

    c "It was at 11 PM. You went to the convenience store at 11 PM."

    s "Charlotte--"

    c "And the 3 AM thing. The tea."

    s "I just made tea."

    show charlotte neutral at center

    c "You always 'just.' You always 'just' do things. Like it's nothing. Like showing up is your default setting."

    s "It kind of is."

    c "I know. I KNOW that. I know it's not-- I know you're like that with everyone."

    s_thoughts "She wipes her hands on her apron. Flour falls."

    s_thoughts "She takes a breath."
    
    c "Sophia..."
    
    show charlotte sad at center
    
    c "I know you're like that with everyone."
    
    c "You show up when you're needed and you notice things and you have this laugh that you do that's so warm and friendly and it makes the whole room light up."
    
    c "You're so easygoing and you get along with everyone and it's all so effortless for you, unlike me who has to always be trying at 110 percent, you just... you can just do it and I..."
    
    s_thoughts "She trails off."
    
    s "I'm not sure what you're getting at."
    
    c "I-I'm not sure either."
    
    s_thoughts "It sounds like she IS sure."
    
    s_thoughts "A beat."
    
    c "I want you to know that no matter what I still want to be friends with you! That's the most important thing. Everything else is secondary."
    
    s "Everything else?"
    
    s_thoughts "Now I'M not sure I like where this is going."
    
    c "Everything... else."
    
    s_thoughts "I notice there's tears in her eyes."
    
    c "I... I..."
    
    c "..."
    
    c "...I have feelings... for you."
    
    s_thoughts "Oh."
    
    s "Oh."
    
    c "Yeah. It's... It's totally okay if you don't feel the same way! Like I said, of course I want to still be friends with you and everything!"
    
    s_thoughts "I don't respond to that."
    
    s_thoughts "An awkward silence hangs over us."
    
    c "I'm sorry."
    
    s "Don't be sorry for that."
    
    s_thoughts "I'm not sure how sincere I'm being."
    
    c "I..."
    
    show charlotte neutral at center

    c "I know you like Amara."

    s_thoughts "My body goes still."

    c "Like, you LIKE like her. Of course you do."

    c "She's-- Amara's amazing. She's smart and she's quiet and she's got that thing where she says three words and they're all the right three words. Of course you like her."

    s "Charlotte--"

    c "And I'm just-- Charlotte. Just the girl who makes the muffins."

    s_thoughts "She gestures at the muffins. The two full trays. The flour on the counter. The evidence of her 4 PM emergency baking."

    show charlotte sad at center

    c "But I needed to tell you. I needed you to know."

    c "I..."

    c "I needed you."

    s_thoughts "The kitchen is very quiet."

    s_thoughts "The mixer has stopped. The oven is off. The only sound is Charlotte breathing."

    c "Sorry--"

    s "Don't."

    c "I shouldn't have-- you came here because my mom called and I'm making it about me and that's--"

    s "Charlotte. Stop."

    s_thoughts "I step forward."

    s_thoughts "Her hands are covered in flour. She just told me she has feelings for me."

    s_thoughts "And she said 'of course you like Amara' because even in the moment where she's the most honest she's ever been, she can't stop giving people permission to leave."

    s "I'm glad."

    c "Glad?"

    s "Glad you told me."

    show charlotte neutral at center

    c "You're not-- you're not going to--"

    s "I like Amara. You're right."

    c "Of course."

    s "Stop saying 'of course.'"

    c "Of--"

    s_thoughts "She catches herself."

    s "You're not just the girl who makes the muffins."

    c "Sophia--"

    s "You're the girl who remembered I like gruyere from one conversation. You're the girl who puts my mug out every morning. You're the girl who replaced lavender soap with FANCIER lavender soap."

    c "French lavender is different--"

    s "Charlotte."

    s_thoughts "I take her hand."

    s_thoughts "It's flour-covered and warm and she grips mine like she's drowning."

    s "I can't give you what you want. But I'm not leaving."

    c "You're not?"

    s "I'm right here."

    show charlotte sad at center

    s_thoughts "She doesn't cry."

    s_thoughts "Charlotte doesn't cry in front of people."

    s_thoughts "But her eyes have tears in them and her lip does a thing and she squeezes my hand so hard it hurts."

    c "I'm sorry."

    s "I told you not to apologize."

    c "I know but I'm sorry anyway. For making it weird. For--"

    s "You didn't make it weird."

    c "I'm standing here covered in flour telling my housemate I have feelings for her after a panic bake about my mom. That's objectively weird."

    s_thoughts "I almost laugh."

    s_thoughts "She almost laughs."

    s_thoughts "Neither of us quite gets there."

    s "Come here."

    s_thoughts "I hug her."

    s_thoughts "She hugs back. Hard. Her face in my shoulder. The flour gets all over my jacket."

    s_thoughts "She shakes."

    s_thoughts "She doesn't cry."

    s_thoughts "She shakes."

    pause 2.0

    c "The muffins are going to be cold."

    s "The muffins can wait."

    c "Muffins shouldn't wait. It affects the texture."

    s "Charlotte."

    c "I know. I know."

    s_thoughts "She pulls back."

    s_thoughts "She wipes her eyes."

    s_thoughts "She looks at me. Really looks."

    show charlotte smile at center

    c "She's lucky. Amara."

    s "She'd say luck is a statistical anomaly."

    c "She WOULD say that."

    s_thoughts "A real smile. Small. Tired. But real."

    c "I'm going to finish the muffins."

    s "I'll stay."

    c "You don't have to--"

    s "I want to."

    c "...Okay."

    s_thoughts "She goes back to the mixer."

    s_thoughts "I sit at the table."

    s_thoughts "She bakes. I'm here."

    s_thoughts "The fixer. Even rejection becomes care."

    s_thoughts "Amara was right about the pattern."

    s_thoughts "I'm doing it anyway."

    $ charlotte_confession = True
    $ persistent.charlotte_confessed_in_amara_route = True

    s_thoughts "Charlotte bakes three more trays. She labels them. Eve's name on one. Isabella's on another. Amara's on the third."

    s_thoughts "She doesn't label the one she puts in front of me."

    s_thoughts "She doesn't have to."

    pause 2.0

    s_thoughts "I think about the empty chair I left at the library table."

    s_thoughts "Amara's book is probably closed."

    s_thoughts "She's probably sitting there anyway."

    s_thoughts "My hand is warm where Charlotte held it and cold where Amara let go."

    s_thoughts "I eat a muffin."

    s_thoughts "It's perfect."

    hide charlotte with dissolve

    stop music fadeout 3.0

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "That night."

    s_thoughts "In bed."

    s_thoughts "I keep replaying it."

    s_thoughts "'I know you like Amara. Of course you do.'"

    s_thoughts "'I needed you.'"

    s_thoughts "'Sorry--'"

    s_thoughts "Charlotte confessed to me."

    s_thoughts "And I stayed. I hugged her. I sat at the table while she baked."

    s_thoughts "Amara's voice: 'If you always give before she asks, she never has to learn.'"

    s_thoughts "Charlotte asked. In her Charlotte way. Three texts. 'Is anyone home.' 'Of course it's nothing.'"

    s_thoughts "For Charlotte, that WAS asking."

    s_thoughts "Maybe... Maybe this was something else."

    s_thoughts "Or maybe I'm translating again. Making the thing I already did into the right thing."

    s_thoughts "My phone. One text."

    s_thoughts "Amara: 'Goodnight, Sophia.'"

    s_thoughts "No question. No accusation. No 'how did it go.'"

    s_thoughts "Goodnight, Sophia."

    s_thoughts "Two words."

    s_thoughts "I type back: 'Goodnight. I'm sorry about the library.'"

    s_thoughts "Three dots. Then nothing."

    s_thoughts "Then: 'Don't be sorry. Be honest about what you chose.'"

    s_thoughts "I put my phone face down."

    s_thoughts "Through the wall -- silence."

    s_thoughts "No clarinet tonight."

    pause 2.0

    jump amara_ch5_end

## ===========================
## Scene 21.5B: NO CONFESSION (sophia_fire < 2)
## Charlotte breaks down about mom. No confession.
## The crush stays in subtext.
## ===========================

label amara_ch5_house_no_confession:

    show charlotte sad at center

    s_thoughts "Her hands are shaking."

    s_thoughts "She puts the mixer down."

    c "She called me helper gal."

    s "I know."

    c "Like... like I'm still the kid in her house."

    s_thoughts "She catches herself."

    c "She wasn't being mean. She wasn't. She was being sweet. She's always sweet. That's the thing. She's sweet and she's sad and she needs me and I'm HERE and she's THERE and I can't--"

    s_thoughts "Her voice cracks."

    c "I can't reach from here."

    s "Charlotte."

    c "I should be there. I should be home making her dinner and making sure she eats it. Who's making sure she eats?"

    s "...That's not your job."

    show charlotte neutral at center

    c "It's always been my job."

    s_thoughts "She says it quietly."

    s_thoughts "Not the frantic brightness. Not the 'of course!' Not the performance."

    s_thoughts "Just a girl in a kitchen stating a fact."

    c "It's always been my job to make sure she's okay."

    s "And who makes sure you're okay?"

    s_thoughts "She looks at me."

    s_thoughts "Something in her face changes."

    c "You're here."

    s "I'm here."

    c "You came home because I texted."

    s "Yeah."

    c "That's-- you didn't have to do that."

    s "I wanted to."

    c "Why?"

    s "Because you're my friend. And you sounded not fine."

    show charlotte sad at center

    c "I said I was fine."

    s "Charlotte, you texted 'of course it's nothing' which is the international Charlotte signal for 'this is definitely something.'"

    s_thoughts "Something between a laugh and a sob."

    c "I'm that obvious?"

    s "Only to people who are paying attention."

    s_thoughts "She sits down."

    s_thoughts "On the kitchen floor. Just-- slides down the cabinets and sits on the floor."

    s_thoughts "I sit next to her."

    s_thoughts "The kitchen floor is cold. The muffins smell like lemon."

    c "She's not a bad mom."

    s "I know."

    c "She loves me. She really, really loves me."

    s "I know."

    c "She-- she means it with love. She's proud of me. She SAYS she's proud."

    s "But."

    c "But sometimes I want someone to be proud of me for something other than helping."

    s_thoughts "The kitchen is quiet."

    pause 2.0

    s_thoughts "Charlotte leans her head against the cabinet. She stares at the ceiling."

    c "I don't know who I am when I'm not the helper."

    s "That's okay."

    c "Is it?"

    s "You're figuring it out. That's what this is."

    c "That's what WHAT is?"

    s "This. College. The house. Making lemon ricotta pancakes and fancy lavender soap and being up at 3 AM organizing spices. You're figuring out who Charlotte is when she's not taking care of someone."

    show charlotte neutral at center

    c "What if I figure it out and there's nothing there?"

    s "There's something there."

    c "How do you know?"

    s "Because you replaced lavender soap with FANCIER lavender soap. A person with nothing there doesn't care about the difference between regular and French lavender."

    s_thoughts "She laughs."

    s_thoughts "A real laugh. Small and wet and sitting on a kitchen floor."

    show charlotte smile at center

    c "French lavender IS different."

    s "I believe you."

    s_thoughts "We sit."

    s_thoughts "I don't fix anything. I don't have answers. I don't have wisdom."

    s_thoughts "I'm just on the floor."

    pause 2.0

    c "Sophia?"

    s "Yeah?"

    c "Thank you.."

    s "Of course."

    c "Don't say that."

    s "What?"

    c "You said 'of course.' That's my thing. You can't have it."

    s "Sorry. I'll find my own version."

    c "Find a good one."

    s "I'll work on it."

    s_thoughts "She gets up. Brushes off her apron."

    s_thoughts "She looks at the muffins."

    c "I should frost these. Do you want to help?"

    s "I'm terrible at frosting."

    c "I'll teach you."

    s "Deal."

    s_thoughts "She teaches me."

    s_thoughts "I'm terrible at it."

    s_thoughts "She fixes every muffin I frost, redoing the swirl, adding a little more here, evening it out there."

    s_thoughts "She doesn't notice she's doing it."

    s_thoughts "I notice."

    s_thoughts "I don't say anything."

    show charlotte happy at center

    s_thoughts "Charlotte labels muffins. Eve. Isabella. Amara."

    s_thoughts "She puts one in front of me. No label."

    c "Yours is the best one."

    s_thoughts "It's the one she frosted. Not the one I did."

    s "Charlotte."

    c "Hmm?"

    s_thoughts "She's looking at me. Something in her face that I can't quite read. Or won't."

    s "Nothing. Good muffin."

    show charlotte smile at center

    c "I know."

    hide charlotte with dissolve

    s_thoughts "She smiles."

    s_thoughts "The real one."

    s_thoughts "The one that might mean something I'm choosing not to translate."

    stop music fadeout 3.0

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "That night."

    s_thoughts "In bed."

    s_thoughts "I keep seeing Amara's hand. Palm up on the table."

    s_thoughts "'I want you to know that I--'"

    s_thoughts "Unfinished."

    s_thoughts "I picked up my bag and walked out of the library because Charlotte was baking muffins."

    s_thoughts "Amara said: 'Go if you want.'"

    s_thoughts "Amara gave me permission to leave. Because Charlotte was asking in the only way Charlotte knows how."

    s_thoughts "That's not the pattern."

    s_thoughts "That's Amara being honest."

    s_thoughts "But the chair at the library is still empty. And the sentence is still unfinished."

    s_thoughts "My phone. One text."

    s_thoughts "Amara: 'Goodnight, Sophia.'"

    s_thoughts "I type back: 'Goodnight. I'm sorry I left.'"

    s_thoughts "Three dots."

    s_thoughts "Then: 'Don't be sorry. Be honest about what you chose.'"

    s_thoughts "I put my phone face down."

    s_thoughts "Through the wall -- silence."

    s_thoughts "No clarinet tonight."

    pause 2.0

    jump amara_ch5_end

## ===========================
## SCENE 21B: AMARA BRANCH
## Sophia stays. The guilt is enormous.
## But the moment from Scene 18 arrives fully.
## Charlotte is alone in the kitchen.
## LONG. Intimate. The closeness AND the guilt.
## ===========================

label amara_ch5_amara:

    s_thoughts "I put my phone down."

    s_thoughts "I look at Amara."

    s_thoughts "I look at her hand. Back in her lap now."

    s "I'm staying."

    show amara neutral at center

    s_thoughts "Amara doesn't smile."

    s_thoughts "She doesn't look relieved."

    s_thoughts "She looks at me like she's weighing what I just said against everything she believes."

    a "Charlotte is in the kitchen."

    s "I know."

    a "Making muffins."

    s "I know."

    a "And you're staying."

    s "You said healthy people ask for what they need."

    a "I did."

    s "Charlotte texted 'is anyone home.'"

    a "She did."

    s "And I'm choosing to be here."

    s_thoughts "A beat."

    a "Why?"

    s "Because you were about to say something."

    s_thoughts "She looks at me."

    s_thoughts "The library is empty. The sun has moved. The warm square of light is gone from the table."

    a "That's not a good reason."

    s "It's my reason."

    a "You're staying because of a sentence I didn't finish."

    s "I'm staying because of everything that came before the sentence."

    pause 2.0

    s_thoughts "My phone buzzes."

    s_thoughts "I don't look at it."

    s_thoughts "Charlotte is in the kitchen. Isabella is texting me. Someone is worried about someone else."

    s_thoughts "I am in the library with Amara."

    s_thoughts "The guilt is a physical thing. It sits in my stomach like cold water."

    a "You're going to feel guilty."

    s "Already do."

    a "I know."

    s "Is that a problem?"

    a "The guilt is yours. It's not about me."

    s "It's a little about you."

    a "How?"

    s "Because you told me Charlotte needs to learn to ask. And she asked. And I stayed anyway."

    s_thoughts "Amara is quiet for a long time."

    a "She asked. And Isabella is there."

    s "Isabella is there?"

    a "Isabella texted. Isabella is in the house."

    s "But I'm not."

    a "No."

    s_thoughts "My phone buzzes again."

    s_thoughts "I force myself not to look."

    play music mus_amara fadein 3.0

    a "Sophia."

    s "Yeah."

    a "Can I finish?"

    s_thoughts "The sentence from before."

    s "Yeah."

    s_thoughts "She puts both hands on the table. Not palm up this time. Flat. Like she's steadying herself."

    a "I'm not good at this."

    s "At what?"

    a "At-- wanting."

    s_thoughts "The word hangs in the empty library."

    a "I'm good at being alone. I told you that. I got used to it. I chose it." 
    
    a "The quiet was mine and I didn't need anyone in it."

    s "But."

    a "But then you started showing up."

    s_thoughts "Her voice is the same level. The precision is there. But underneath it -- something is costing her."

    a "You showed up at the library and you couldn't sit still." 
    
    a "You showed up on the porch and you talked when I wanted quiet." 
    
    a "You showed up in the armchair and you read the same paragraph fifteen times."

    s "It was twelve."

    a "It was fifteen. I counted."

    s_thoughts "She counted. That shouldn't be possible but for Amara I'm convinced anything might be."

    a "And I waited for you to stop coming."

    s "What?"

    a "I expected you to stop. People do." 
    
    a "People show up for a while and then the silence gets boring and they leave."

    s "I didn't leave."

    a "You didn't leave."

    pause 1.5

    a "I don't know what to do with that."

    s "You don't have to do anything with it."

    a "That's what I tell you."

    s "Maybe it applies to you too."

    s_thoughts "The half-degree."

    show amara embarrassed at center

    s_thoughts "More than half. Three-quarters."

    a "I want you to know that I notice you. Not the way you notice people."

    a "I notice you the way you notice the clarinet."

    s_thoughts "My heart stops."

    s "The clarinet."

    show amara neutral at center

    a "You listen. You don't analyze it. You don't file it. You just listen."

    a "I notice you like that."

    s "Amara--"

    a "I notice that you touch your jaw when you're filing someone and that you breathe differently when you stop." 
    
    a "I notice that you look at the armchair first when you come downstairs." 
    
    a "I notice that you check your phone for Lila and then put it down and look guilty."

    a "I notice that you're here. Right now. Even though Charlotte is in the kitchen."

    s_thoughts "I can't breathe."

    s_thoughts "Not in the bad way. In the way where your body knows something so large that breathing feels like an interruption."

    a "I'm not good at wanting. I don't have practice."

    a "But I want you in the room."

    pause 2.0

    s_thoughts "The library is empty."

    s_thoughts "My phone is buzzing."

    s_thoughts "Charlotte is making muffins."

    s_thoughts "Amara just told me she wants me in the room."

    s_thoughts "She wants me in the room."

    s "I want to be in the room."

    a "I know."

    s "No-- I want to be in YOUR room. In the library. On the porch. Wherever you are."

    show amara embarrassed at center

    s_thoughts "Her ears. Pink."

    s "I'm bad at this too. For different reasons. I want to translate everything and file everything and understand everything. And with you I can't. And that drives me crazy. And I keep coming back."

    a "Why?"

    s "Because the not-understanding feels better than understanding everyone else."

    s_thoughts "She looks at me."

    s_thoughts "I look at her."

    s_thoughts "The table is between us. The closed books. The chairs."

    s_thoughts "She reaches across the table again."

    s_thoughts "Her hand. Palm up."

    s_thoughts "I take it."

    s_thoughts "This time her grip is different. Not careful. Not considered."

    s_thoughts "Tight."

    show amara smile at center

    s_thoughts "She smiles."

    s_thoughts "The real one."

    s_thoughts "I am not filing this. I am not translating this. I am holding Amara's hand in an empty library and she is smiling at me and I am just here."

    pause 2.0

    s_thoughts "My phone buzzes."

    s_thoughts "The guilt comes back. Cold and sharp."

    s_thoughts "Charlotte."

    s_thoughts "I imagine her in the kitchen. The flour on the counters. The mask going frantic. The 'of course!' getting louder because nobody came."

    s_thoughts "Isabella is there. Isabella will see it. Isabella will help."

    s_thoughts "But Isabella isn't me."

    s_thoughts "And Charlotte needed me."
    
    s_thoughts "Or maybe needed to need me."

    s_thoughts "But I'm here."

    show amara neutral at center

    a "You're thinking about Charlotte."

    s "I can't help it."

    a "I know."

    s "Does that bother you?"

    a "No."

    s "It doesn't?"

    a "You caring about Charlotte is part of who you are. I'd be worried if you weren't thinking about her."

    s "That's very healthy of you."

    a "I've had practice."

    s "At being healthy?"

    a "At accepting things I can't change."

    s_thoughts "Her thumb moves across my knuckles. Once."

    a "Charlotte will be okay."

    s "How do you know?"

    a "Because Charlotte has survived every hard thing so far. She'll survive this one."

    s "That's not reassuring."

    a "Survival isn't reassuring. It's just real."

    s_thoughts "I hold her hand."

    s_thoughts "She holds mine."

    s_thoughts "Charlotte is in the kitchen and I am here."

    pause 2.0

    s_thoughts "We sit until the library closes."

    s_thoughts "The librarian gives us a look. The 'it's late and I want to go home' look."

    s_thoughts "We pack up. We walk out."

    hide amara with dissolve

    stop music fadeout 2.0

    scene bg nightwalk with Fade(0.8, 0.3, 0.8)

    s_thoughts "We walk home."

    show amara neutral at center with dissolve

    s_thoughts "Side by side. Not holding hands anymore but close. Close enough that our arms brush."

    s_thoughts "She doesn't say anything."

    s_thoughts "I don't say anything."

    s_thoughts "The walk takes ten minutes. It feels like three."

    scene bg entry night with dissolve

    s_thoughts "The house."

    s_thoughts "We come in."

    s_thoughts "The kitchen light is on."

    s_thoughts "I can smell muffins."
    
    scene bg kitchen night with dissolve

    s_thoughts "Charlotte is at the table. Her phone is face-down. Her hands are clean -- she washed the flour off. The muffins are on the counter. Three trays. Labeled."

    show charlotte happy at left
    show amara neutral at right
    with dissolve

    s_thoughts "She looks up when we come in."

    c "Oh! You're home!"

    s_thoughts "The brightness. Dimmer than before. She's tired."

    c "I made muffins. There's-- there's some for everyone."

    s "Charlotte."

    c "It's fine! I'm fine. Isabella came down and we talked. It was good."

    s "I'm sorry I wasn't here."

    show charlotte smile at left

    c "Don't be silly! You were at the library. Studying is important!"

    s_thoughts "The mask. Back on. Functional."

    s_thoughts "But I can see the seams."

    c "Amara, there's one with your name on it. I used the good blueberries."

    a "Thank you, Charlotte."

    c "Of course!"

    s_thoughts "Amara looks at me."

    s_thoughts "I look at the counter."

    s_thoughts "Charlotte's muffin for me. No label. The best one."

    s_thoughts "I take it."

    s "Thank you."

    c "Of course!"

    s_thoughts "She smiles."

    s_thoughts "She's holding it together."

    s_thoughts "Isabella held it while I was gone."

    s_thoughts "Charlotte survived."

    s_thoughts "But I can see the cost."

    hide charlotte with dissolve
    hide amara with dissolve

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Later."

    s_thoughts "In bed."

    s_thoughts "Amara's hand."

    s_thoughts "'I want you in the room.'"

    s_thoughts "Charlotte's face when I came in."

    s_thoughts "The brightness turned down half a notch. The mask functional but worn. The muffins labeled and the one for me unlabeled because labeling it would mean I'm not different from everyone else."

    s_thoughts "I chose Amara."

    s_thoughts "Amara told me she wants me in the room. She told me she notices me the way I notice the clarinet."

    s_thoughts "Charlotte made muffins alone."

    s_thoughts "Isabella came. Isabella was there."

    s_thoughts "I wasn't."

    s_thoughts "I lie in bed and I hold both things."

    s_thoughts "Amara's hand."

    s_thoughts "Charlotte's face."

    s_thoughts "The observation instinct says: you chose. Every choice is a translation. Loyal to whom?"

    s_thoughts "I was loyal to Amara."

    s_thoughts "I was loyal to myself."

    s_thoughts "Charlotte's muffin is on my desk. Untouched."

    s_thoughts "I eat it."

    s_thoughts "It's perfect."

    s_thoughts "Through the wall -- the clarinet."

    s_thoughts "She's playing the new piece. The one from last week."

    s_thoughts "I listen."

    s_thoughts "I don't translate."

    s_thoughts "I just listen."

    pause 2.0

    jump amara_ch5_end
    
    ## ===========================
    ## END
    ## ===========================
    
label amara_ch5_end:

    stop music fadeout 4.0

    scene black with Fade(1.5, 1.0, 1.5)

    "Chapter 5: Role -- End"

    jump amara_ch6