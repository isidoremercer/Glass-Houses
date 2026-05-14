## eve_ch5.rpy -- Glass Houses
## Chapter 5: "The Telling" -- Eve Route
## Act 1: "The Approach to the Telling" (Scenes 1-6)
## Act 2: "The Telling" (The confession scene + Scenes 7-8)
## Act 3: "The Distance" (Scenes 9-16)

## === NEW VARIABLES NEEDED (add to variables.rpy) ===
## None -- Eve's route has no choices.

## === AUDIO DEFINITIONS ===
define audio.mus_eve = "audio/music/Eve Morse ~ A Room That Just Emptied.mp3"
define audio.mus_eve_confession = "audio/music/Eve Morse ~ The Girl Before The Ghost.mp3"
define audio.mus_2am = "audio/music/House at 2AM.mp3"
define audio.mus_campus = "audio/music/Campus in Autumn.mp3"
define audio.mus_fivepeople = "audio/music/Five People in a Kitchen.mp3"
define audio.mus_tuesday = "audio/music/A Normal Tuesday.mp3"
define audio.mus_charlotte = "audio/music/Charlotte Opal ~ Toast Girl.mp3"
define audio.mus_shoulders = "audio/music/Shoulders Touching.mp3"
define audio.mus_morningafter = "audio/music/The Morning After The Hard Thing.mp3"
define audio.mus_wrong = "audio/music/Something's Wrong in the Kitchen.mp3"
define audio.mus_mourning = "audio/music/Mourning.mp3"
define audio.mus_fragile = "audio/music/Fragile Glass Between.mp3"
define audio.mus_time = "audio/music/Moments Across Time.mp3"
define audio.mus_glass = "audio/music/Glass Walls.mp3"
define audio.mus_afternoon = "audio/music/Afternoon Study Session.mp3"

## ===========================
## CHAPTER 5 START
## ===========================

label eve_ch5:

    ## ===========================
    ## ACT 1: "THE APPROACH TO THE TELLING"
    ## The days between "soon" and "now."
    ## Eve has decided. The approach is terrifying.
    ## ===========================

    ## ===========================
    ## SCENE 1: THE MORNING AFTER "SOON"
    ## The promise changed the air.
    ## Both performing normal. Neither buying it.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    play music mus_morningafter fadein 3.0

    s_thoughts "I didn't sleep."

    s_thoughts "I mean, I slept. Some. The kind of sleep where your body gives up arguing with your brain and just lies there while your brain runs the same three sentences in a loop."

    s_thoughts "'There's more.'"

    s_thoughts "'I think I want to tell you.'"

    s_thoughts "'Soon.'"

    s_thoughts "My shoulder still has the ghost of hers against it. That's not how physics works. I don't care."
    
    s_thoughts "I laid in bed all last night thinking about what she said and about her shoulder and about all the other parts of us I'd like to touch just like our shoulders did."
    
    s_thoughts "It's a bit embarrassing but I don't care."

    s_thoughts "It's morning."

    show eve neutral at center with dissolve

    s_thoughts "Eve is eating cereal."

    s_thoughts "Not at midnight. Not on the floor. Not in the liminal space between awake and asleep where the house belongs to us. Actual morning. Daylight. Cereal."
    
    s_thoughts "She's stunning."

    s_thoughts "She looks up when I come in."

    e "Hey."

    s "Hey."

    s_thoughts "Normal."

    s_thoughts "Aggressively normal."

    s_thoughts "Two people who said enormous things in a dark room twelve hours ago and are now standing in a kitchen with cereal and sunlight and the fridge humming."

    s_thoughts "I get a mug. I make coffee. The machine gurgles."

    s_thoughts "Eve eats cereal. She's using the green mug for the milk. I don't know why that's the detail I notice. The green mug with the chip on the rim. Cereal milk in it."

    s_thoughts "The promise is in the room. Neither of us looks at it."

    s "Sleep okay?"

    s_thoughts "I ask this like I don't already know the answer from the way she's holding the mug -- both hands, tight, the way she does when she's not okay."

    e "Mm."

    s_thoughts "Not yes. Not no. Mm."
    
    s "Yeah, me either."

    s_thoughts "I sit down across from her. The table between us. The table that used to be where we shared earbuds and watched anime and I was worried about my neck."

    s_thoughts "That was before."

    s_thoughts "Eve finishes her cereal. She rinses the bowl. She puts it in the drying rack."

    e "Class?"

    s "In an hour."

    e "Okay."

    s_thoughts "She goes upstairs."

    hide eve with dissolve

    s_thoughts "I drink my coffee."

    s_thoughts "The kitchen is very bright."

    s_thoughts "I keep thinking about the preview she skipped. The rival character and the new character sitting next to each other. The way Eve's eyes darted to mine and she hit skip like a reflex."

    s_thoughts "Spoilers, she said."

    s_thoughts "It wasn't about spoilers."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 2: LILA CHECK-IN
    ## Sophia talks AROUND it. Doesn't share secrets.
    ## Lila seeds "the hardest part isn't hearing it."
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 2.0

    s_thoughts "Thursday. The bench."

    show lila happy at center with dissolve

    l "You look like garbage."

    s "Thanks."

    l "No, like, specifically garbage. Like someone put you in a bin and then took you out and said 'this isn't recyclable.'"

    s "That's really specific."

    l "I workshopped it on the walk over. So. What's wrong."

    s_thoughts "Lila sits down. She has an iced coffee the size of her forearm. It's forty degrees out."

    s "Nothing's wrong."

    show lila annoyed at center

    l "Sophia."

    s "..."

    l "You texted me at 7 AM. You never text at 7 AM. You text at 2 AM or noon. 7 AM is a cry for help."

    s_thoughts "She's not wrong."

    s "Something is going to happen."

    show lila shocked at center

    l "What kind of something?"

    s "Eve is going to tell me something."

    s_thoughts "Lila's face does a whole journey. She starts at 'ooh gossip' and arrives at 'oh, this is real.'"

    show lila happy at center

    l "What kind of something? I'm guessing not that she's madly in love with you?"
    
    s "Probably not, no."
    
    l "Bummer."
    
    s "Yeah."
    
    l "So what is it, then?"

    s "I don't know. She said -- she said there's more. To the stuff she told me about. Her family. She said there's another layer and she wants to tell me."

    l "And you're scared."

    s "I'm scared."

    l "Of what she's going to say?"

    s_thoughts "I think about that."

    s "Of what happens after."
    
    s "To... to us. To what we have."

    s_thoughts "Lila takes a long drink of her iced coffee. She's quiet for a second. This is unusual. Lila is never quiet for a second."

    show lila happy at center

    l "Okay. So. My club advisor said something last week."

    s "The mental health club."

    l "Don't say it like that. She said -- okay, she said the hardest part of hearing someone's pain isn't the hearing part."

    s "What is it?"

    l "The not-fixing part."

    s_thoughts "I look at her."

    l "She said people tell you something terrible and your whole body goes 'FIX IT' and you have to just -- not. You have to sit there with the terrible thing and not make it about what YOU can do for them."

    s "That sounds awful."

    l "Yeah. She said it's the thing most people fail at. They hear the pain and they leap to 'what can I do' because 'what can I do' is about THEM. It puts them in the center. They become the helper instead of the listener."

    s_thoughts "Something about that."

    s_thoughts "Something about the way Lila says 'the helper' and I think about Charlotte's toast at Eve's door."

    l "So whatever she tells you -- just, like. Hear it."

    s "Just hear it."

    l "Don't fix it. Don't explain it. Don't make it about you."

    s_thoughts "She says this while slurping an enormous iced coffee through a neon straw."

    s "Since when are you the wise one?"

    show lila laugh at center

    l "I've ALWAYS been wise. The world is just catching up."

    s "The world is terrified."

    l "As it should be."

    s_thoughts "She bumps my shoulder with hers."

    l "You'll be okay. Whatever it is. You're good at sitting with things. Even when you think you're not."

    s "Am I?"

    l "Sophia. You sat on a floor in a hallway for twenty minutes because the girl you're crushing on didn't want you in her room. You're okay at sitting with things."

    s_thoughts "I didn't tell Lila about the hallway."

    s "How do you know about the hallway?"

    l "Isabella."

    s "Isabella saw that for two seconds."

    l "Isabella texted me about it for fifteen minutes."

    s_thoughts "I file that and then unfile it. Isabella texted Lila about it. For fifteen minutes."

    s_thoughts "Isabella is paying attention."

    l "Go to class. Stop spiraling. Text me after."

    s "After what?"

    show lila happy at center

    l "After whatever happens. You know what I mean."

    s_thoughts "She stands up. Iced coffee in hand. She's already walking."

    l "And Soph?"

    s "Yeah?"

    l "If it's really bad -- like, the kind of bad where you don't know what to say -- you don't have to say anything. Just stay."

    s_thoughts "She waves without turning around."

    hide lila with dissolve

    s_thoughts "I sit on the bench."

    s_thoughts "The not-fixing part."

    s_thoughts "I think about every instinct I have. Observe. Analyze. Understand. Build a file. Find the pattern. Solve it."

    s_thoughts "Every single one of those is fixing."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 3: THE ANIME -- THE BACKSTORY EPISODE
    ## The fuse. NOT decodable yet.
    ## Heavy, personal, but the reader only understands
    ## AFTER the confession. Replay value.
    ## ===========================

    scene bg evebedroom with Fade(1.0, 0.5, 1.0)

    play music mus_eve fadein 3.0

    s_thoughts "Saturday night. Eve's room."

    s_thoughts "Watching the anime has become a ritual at this point. So has my heartrate reaching concerning levels when we sit on the bed together."

    show eve pj neutral at center with dissolve

    s_thoughts "We're into the new arc. Different energy -- quieter, slower. The fights are over and the characters are dealing with the aftermath of winning."

    s_thoughts "Eve hasn't been yapping tonight. She's been watching. Really watching. Her eyes haven't left the screen."

    s_thoughts "The new arc introduced a character. A girl from the rival's past. Someone the rival knew before the academy -- before the tournament, before any of it."

    s_thoughts "They were close. The show makes that clear in small ways. Shared glances. Inside jokes the protagonist doesn't understand. A scene where the new character finishes the rival's sentence and the rival lets her."

    e "She's important."

    s "The new character?"

    e "Yeah. To -- to the rival."

    s "I can tell."

    s_thoughts "Eve nods. She doesn't elaborate."

    s_thoughts "We watch."

    s_thoughts "The episode builds. Something happened between them. Before. The new character did something, or something happened when they were together, or -- the show isn't clear." 
    
    s_thoughts "It's told in fragments. A flashback that cuts away before the important part. The rival alone in a room afterward. The new character's face in a doorway."

    s_thoughts "It's impressionistic. Abstract. The colors go wrong. The music drops out. There's a sequence where the rival is alone and the screen goes dark and you can hear breathing and then it's morning and she's sitting on a bench staring at nothing."

    s_thoughts "I don't fully understand what the show is saying."

    s_thoughts "Eve is very still. I'm watching her as much as I'm watching the show. She doesn't notice."

    s_thoughts "Her hand is on the blanket. The one that tightened during the bench scene weeks ago. It's tight again."

    s_thoughts "The episode continues. The rival talks to the protagonist. She says something like: 'Some people see you and it's warm. And some people see you and they use it.' The subtitles flash and disappear."

    s_thoughts "The protagonist says: 'What happened?'"

    s_thoughts "The rival says: 'I don't know how to explain it in a way that makes sense.'"

    s_thoughts "The protagonist says: 'You don't have to make sense.'"

    s_thoughts "The rival doesn't answer."

    s_thoughts "The episode ends."

    stop music fadeout 3.0

    pause 3.0

    s_thoughts "Silence."

    s_thoughts "The autoplay countdown starts."

    s_thoughts "Eve reaches over and pauses it."

    pause 2.0

    s_thoughts "The room is dark except for the laptop. The plant on the windowsill is a shadow."

    e "That's the episode I was skipping the preview for."

    s_thoughts "I stop breathing."

    s_thoughts "The preview. Eve's eyes darting to mine. Skip. 'I don't do previews. Spoilers.'"

    s_thoughts "It wasn't about spoilers."

    s "..."

    e "I've seen it before."

    pause 1.5

    s "You've..."

    e "Watched the whole show. A while ago. I started over with you."

    s_thoughts "She started over with me. She rewatched the entire show from the beginning because --"

    s_thoughts "Because she wanted me to see it."
    
    s_thoughts "Be calm my beating heart."

    e "I wasn't ready for you to see it."

    pause 2.0

    s_thoughts "She says this to the laptop screen. Not to me."

    s_thoughts "I don't know what the episode means. I know it was heavy. I know the rival was hurt by someone she trusted. I know Eve's hand is tight on the blanket."

    s "Are you okay?"

    show eve pj sad at center

    e "Mm."

    s_thoughts "Mm. The morning sound. The sound that means everything and nothing."

    pause 1.5

    e "Can we stop for tonight?"

    s "Of course."

    s_thoughts "I almost say 'do you want to talk about it' and I catch myself. Lila's voice. The not-fixing part."

    s "Goodnight, Eve."

    show eve pj neutral at center

    e "Goodnight."

    s_thoughts "Her voice is thin. Like something was stretched and hasn't come back yet."

    s_thoughts "I go to the door."

    e "Sophia."

    s "Yeah?"

    pause 1.5

    e "Soon."

    pause 2.0

    s_thoughts "I nod."

    s_thoughts "I close the door."

    hide eve with dissolve
    
    scene bg hallway with dissolve

    s_thoughts "In the hallway I lean against the wall."

    s_thoughts "The rival was hurt by someone she trusted. The new character. The one who finished her sentences."

    s_thoughts "Eve rewatched the whole show from the beginning so I'd see that episode."

    s_thoughts "She wasn't ready for me to see it."

    s_thoughts "She is now."

    s_thoughts "Soon."

    ## ===========================
    ## SCENE 4: NOVA'S CLASS -- TESTIMONY
    ## Brief. The ethnographer's obligation.
    ## "What do you do with it?"
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)

    play music mus_nova fadein 2.0

    s_thoughts "Monday. Nova's class."

    show professor neutral at center with dissolve

    nova "Last week we talked about what happens when the subject of a study speaks. Today I want to reverse it."

    s_thoughts "She writes on the board: TESTIMONY."

    nova "Sometimes the subject doesn't just passively exist for the ethnographer to observe. Sometimes the subject turns to the ethnographer and says: 'I want to tell you something.'"

    s_thoughts "My pen stops."

    nova "Testimony. From the Latin testis. 'Witness.' The subject asks the observer to bear witness. Not to publish. Not to analyze. To witness."

    nova "What does the ethnographer owe the testimony?"

    s_thoughts "The room is quiet. Someone shifts in their chair."

    show professor happy at center

    nova "This is not abstract. You will encounter this. Someone will trust you with something that was not given for your benefit. And you will have to decide what you do with it."

    s_thoughts "I think about Eve. Obviously."
    
    s_thoughts "I think about how horrendously unethical it probably is to receive testimony as an ethnographer for someone you're head over heels for and who probably doesn't reciprocate at all."
    
    s_thoughts "Oh, Eve."

    s_thoughts "She's about to give me something. What do I do with it?"

    nova "The subject gave you something. What do you do with it?"

    s_thoughts "Nova looks at the room. The slow scan."

    nova "Hold that question. We're going to need it for the paper."

    s_thoughts "She moves on. Readings. Citations. Someone asks about the word count."

    s_thoughts "I sit in my chair."

    s_thoughts "What do you do with it."
    
    scene bg officehours with dissolve

    s_thoughts "I stay behind after class and peek my head in Nova's office."
    
    show professor neutral at center with dissolve
    
    nova "Ms. Bell? Office hours are Thursday."
    
    s "I... I know. I just... I, um..."
    
    nova "You have a question that couldn't wait."
    
    s "I have a question that couldn't wait."
    
    s_thoughts "She leans back in her chair, the kind of lean that's as much resignation as it is curiosity."
    
    nova "Speak."
    
    s "We've been talking a lot about the ethics of receiving testimony."
    
    nova "A+ on summarizing today's lecture."
    
    s "Right. Sorry. I just mean... what if there are other intervening circumstances?"
    
    s_thoughts "She raises her eyebrow at that."
    
    nova "Go on."
    
    s "What if... what if there's a relationship between the ethnographer and the subject giving testimony?"
    
    nova "A relationship? Like, sex?"
    
    s_thoughts "The blush that crosses my face is something like the color of a particularly crisp apple."
    
    s "NO. No. Um. Not that. Well, uh, no. Not that."
    
    nova "Okay then. Something romantic?"
    
    s "Maybe? I mean, like."
    
    nova "You're saying a lot of words without really saying anything."
    
    s "Sorry. I just... there's someone who's going to tell me something soon. Testimony."
    
    nova "And you have feelings for this person?"
    
    s_thoughts "My voice is a squeak."
    
    s "Yeah."
    
    nova "I see."
    
    s_thoughts "She sits with that for a moment."
    
    nova "Does this person reciprocate your feelings?"
    
    s "I'm... not sure."
    
    nova "Ah."
    
    s_thoughts "A beat."
    
    nova "If a subject wants to testify to you, it's up to you to determine how to respond."
    
    nova "All I can do is talk to you about the ethical considerations. I can't do the considering for you."
    
    s "Right."
    
    nova "These things happen when we're observing people, you know."
    
    s "They do?"
    
    nova "All the time. The question is, why are you doing it?"
    
    s "Why...?"
    
    nova "Are you hearing the testimony because it needs to be heard? Or because you think it'll give you a shot with them?"
    
    s_thoughts "I sit with that for a while. It lingers in the room."
    
    nova "Ponder that, Sophia. There may not be a right answer to this one."

    s_thoughts "I nod. I leave. She watches me leave."

    hide professor with dissolve
    scene bg classroom with dissolve
    
    s_thoughts "I don't think my motives with Eve are quite so... below board, I guess."
    
    s_thoughts "But I do have a hell of a crush on her."
    
    s_thoughts "Every day we watch anime I'm thinking about how close we are and I'm imagining and I'm--"
    
    s_thoughts "I cough a particularly unpleasant cough."
    
    s_thoughts "Eve needs to be heard."
    
    s_thoughts "Can I hear her without letting my own feelings get in the way of that?"
    
    s_thoughts "I... don't know."
    
    pause 2.0
    
    s_thoughts "...Welcome to Ethnography."
    
    stop music fadeout 2.0    

    ## ===========================
    ## SCENE 5: THE DAYS BEFORE
    ## Small beats. Not a scene -- a montage.
    ## Eve is preparing. The reader can feel it building.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    play music mus_time fadein 2.0

    s_thoughts "Tuesday."

    s_thoughts "My phone. The typing indicator."

    s_thoughts "Three dots appear. Disappear. Appear. Disappear."

    s_thoughts "Then a meme. A screenshot from the anime. The rival character looking exhausted with the caption 'me at 9am.'"

    s_thoughts "I type back: 'You? Up at 9am?'"

    s_thoughts "Three dots."

    s_thoughts "'sometimes.'"

    s_thoughts "Three dots again. Appear. Disappear. Appear."

    s_thoughts "Nothing."

    s_thoughts "She was going to say something else. She deleted it."

    scene bg kitchen with dissolve

    s_thoughts "Wednesday."

    s_thoughts "Eve is at the kitchen table. She's not eating. She's not reading. She's sitting with her hands around the green mug, staring at a point somewhere between the table and the wall."

    show eve neutral at center with dissolve

    s_thoughts "Her lips are moving. Very slightly. Like she's rehearsing."

    s_thoughts "I come in. She sees me."

    s_thoughts "She stops."

    e "Oh. Hey."

    s "Hey."

    s_thoughts "She takes a sip of tea. Normal. Performing normal."

    s_thoughts "I get water. I sit down."

    s_thoughts "She drinks her tea. I drink my water."

    s_thoughts "Neither of us says it."

    hide eve with dissolve

    scene bg hallway with dissolve

    s_thoughts "Thursday."

    s_thoughts "I'm coming out of the bathroom."

    show amara neutral at left with dissolve
    show eve neutral at right with dissolve

    s_thoughts "Eve and Amara are in the hallway. They're talking. Low. I can't hear the words."

    s_thoughts "Eve says something. Amara nods. Once."

    s_thoughts "Eve goes to her room."

    hide eve with dissolve
    show amara neutral at center with move

    s_thoughts "Amara turns and sees me."

    s_thoughts "She looks at me."

    s_thoughts "I wait for her to say something. 'Watch yourself.' 'People never mean to.'"

    s_thoughts "She doesn't say anything."

    s_thoughts "She goes downstairs."

    hide amara with dissolve

    s_thoughts "Eve's door closes."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 6: THE CALM BEFORE
    ## Sophia alone. The house is quiet.
    ## The last moment of not-knowing.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.5, 1.0)

    s_thoughts "Friday evening."

    s_thoughts "My room. The house is quiet."

    s_thoughts "Too quiet."

    s_thoughts "Charlotte's not in the kitchen. No garlic, no humming. Isabella's not on the couch. Amara's door was closed."

    s_thoughts "The house feels empty the way a theater feels empty before the lights go down."

    pause 1.5

    s_thoughts "I'm on my bed. I have my laptop open. I have readings for Nova's class pulled up."

    s_thoughts "I've been staring at the same paragraph for twenty minutes."

    s_thoughts "'The ethnographer who bears witness enters into a contract with the testimony-giver. The contract is not written. The contract is: I will hold this.'"

    s_thoughts "I close the laptop."

    s_thoughts "I lie back."

    s_thoughts "I think about my conversation with Nova."
    
    s_thoughts "About the contract I'm about to form."
    
    s_thoughts "I think about Eve."
    
    s_thoughts "I've been crushing on her for a while now."
    
    s_thoughts "Does she know?"
    
    s_thoughts "Is the reason she's going to tell me all this BECAUSE she knows?"
    
    s_thoughts "I catch myself. That's exactly what Nova was warning about."
    
    s_thoughts "Making it about me. About my feelings. Instead of the testimony."
    
    s_thoughts "But I can't help but wonder if she knows either way."

    pause 2.0

    s_thoughts "My phone is in my hand. I'm not looking at it. I'm looking at the ceiling."

    s_thoughts "The house is very still."

    s_thoughts "I don't know what she's going to tell me. I know the shape of it. But not the details."

    s_thoughts "Something happened. Because nobody was watching. That's what she said."

    s_thoughts "And she's going to tell me."

    s_thoughts "And I'm going to have to just -- hear it."

    s_thoughts "Don't fix it. Don't file it. Don't make it about you. About my feelings for her."

    s_thoughts "Just stay."

    pause 2.0

    s_thoughts "The rain starts."

    s_thoughts "I can hear it on the window. Soft at first, then steady."

    s_thoughts "Of course it's raining."

    s_thoughts "My phone buzzes."

    pause 1.5

    s_thoughts "Eve."

    s_thoughts "'please come to my room'"

    pause 2.0

    s_thoughts "My chest does something that isn't architectural. It's tectonic. Plates shifting. The ground changing."

    s_thoughts "I stand up."

    stop music fadeout 2.0

    ## ===========================
    ## END OF ACT 1: "THE APPROACH TO THE TELLING"
    ## She asked. Now Sophia walks to the door.
    ## ===========================

    ## ===========================
    ## ACT 2: "THE TELLING"
    ## THE CONFESSION SCENE -- written by Isidore.
    ## FIXED. SACRED. Inserted verbatim with
    ## Ren'Py syntax fixes only.
    ## ===========================

    ## ===========================
    ## THE CONFESSION SCENE
    ## (from scratch/the scene.rpy -- Isidore's writing)
    ## Three syntax fixes applied:
    ## 1. Fade ((1.5, 1.0, 1.5) -> Fade(1.5, 1.0, 1.5)
    ## 2. mus_ghost -> mus_eve_confession
    ## 3. play music line fixed to proper Ren'Py syntax
    ## ===========================

    scene bg hallway night with Fade(1.5, 1.0, 1.5)

    s_thoughts "It's raining outside."

    s_thoughts "Of course it's raining outside."

    s_thoughts "Eve texted me and just said 'please come to my room' and I have a feeling."

    s_thoughts "Maybe she chose today because it's raining. If it wasn't inappropriate I might laugh at the absurdity."

    s_thoughts "Her door is closed."

    s_thoughts "I think about knocking. But before I can, it cracks open, like someone gently pulled it."

    s_thoughts "But she doesn't pull it open."

    s_thoughts "I push it gently. It swings."
    
    scene bg evebedroom with dissolve

    s_thoughts "If she got up to crack it, she already got back in bed."

    show eve neutral at center with dissolve

    s_thoughts "She's fully clothed. Lying in bed. Partly covered in a blanket."

    s_thoughts "Staring at the wall. Like she's not even in the room."

    e "Close the door. Please."

    s_thoughts "I oblige. I approach, carefully, methodically, like I'm a scared planet orbiting a fragile star."

    e "I... I asked Amara to take everyone out to dinner."

    s_thoughts "So that's why it's so quiet around here today."

    s_thoughts "The rain patters on the roof and the window. I look at the plant. I've been giving it a lot of attention lately."

    s_thoughts "I get a few feet away from the bed. Suddenly I freeze."

    s_thoughts "Like my body is telling me."

    e "That's... that's close enough. S... Sophia."

    s_thoughts "She quivers on my name, like she's not sure she's allowed to say it."

    s "Okay."

    s_thoughts "I sit on the floor."

    e "The thing. The thing I didn't tell you about."

    s_thoughts "She turns toward me. Her eyes have this hollowness. A kind of exhaustion that looks existential."

    play music mus_eve_confession fadein 4.0

    pause 5.5

    show eve pain at center

    e "I was raped."

    s_thoughts "Oh."

    pause 1.5

    s_thoughts "The word hangs in the air like it wasn't allowed to be said."

    show eve smile at center

    e "I'm--I'm sorry."

    s_thoughts "It takes me a second to respond."

    s "Why are you apologizing?"

    s_thoughts "She laughs. It's not a laugh."

    show eve neutral at center

    e "Because that's not how you're supposed to do it."

    e "You're supposed to have a lead-up where you dance around it all pretty-like."

    e "It's supposed to be raw and vulnerable and sad and then you finally say it."

    e "It's not how you're supposed to start."

    s "I'm not sure there's a 'supposed to' anything here. Not with me, anyway."

    e "Yeah."

    s_thoughts "A quiet, heavy, settles in the room for a while. I can hear every inch of it."
    
    s_thoughts "I try hard not to think about my feelings for Eve. Not now. Not at this moment. Not when she needs me to just be... a friend."
    
    s_thoughts "I do not succeed. I try to say the right thing anyway."

    s "What happened?"

    e "She..."

    s_thoughts "The word is thick. Like it's stuck to her tongue."

    e "Do you remember that song?"

    s "The country one?"

    s_thoughts "Oh."

    e "It was her favorite."

    s "...You kept it on the playlist."

    e "Yeah. I did."

    e "I... I couldn't... I couldn't bring myself to take it off."

    s_thoughts "I think about that moment. I think about my file. I think about how wrong it was."

    s "Who was she to you?"

    e "My best friend."

    e "She was... like you."

    s_thoughts "I freeze."
    
    s_thoughts "Oh... oh fuck."

    e "Sorry, that was--"

    s "N...No. It's okay."

    s_thoughts "A lot of things start to make sense now."

    e "I was sixteen, I think?"

    e "We went to high school together."

    e "..."

    e "I didn't have a lot of friends in high school."

    s "Me either. Turns out being the 'notices things girl' isn't exactly popular in most cliques."

    s_thoughts "She does the laugh-that's-not-a-laugh at that. She turns over on her back, staring at the roof. Listening to the rain. To the quiet underneath it."

    e "Yeah."

    s_thoughts "Her arms are locked by her sides."

    e "I told you how the silence is loud."

    e "How you hear things in it."

    e "How you learn to."

    s "I've started to notice it."

    s_thoughts "Her response is immediate."

    e "Not like me."

    s_thoughts "She says it like it's a fact. It is. I don't dispute it."

    e "It was my fault. And don't say the thing about how I'm blaming myself. Just... let me talk."

    s_thoughts "I want more than anything to say the thing but I don't. As requested."

    e "We got high together. That night. The night it... the night it happened."

    s_thoughts "She says high like it's a curse word. And 'it' too."

    e "I shouldn't have. I knew she had a bad reaction to it before."

    e "..."

    e "But I did."

    s "Eve--"

    e "Don't. I know."

    s "Yeah."

    s "..."

    show eve pain at center

    e "Her name was Cadence. Like... like music."

    e "I... I don't know why I didn't tell you that earlier."

    s_thoughts "Tears are rolling down her face but she's not crying. Her breathing is the same as before. It's like her eyes are watering but there's nothing behind it."

    e "She was my best friend."

    s "I know."

    e "No. You don't."

    s_thoughts "She's right. Reflex."

    e "All those memories. Good memories. Bad memories. Neutral memories. It's like..."

    e "It's like when you spend your life seeing color and then you lose the ability to see it and everything is grey and you don't know how you can see color for so long and then stop seeing it but it's just how your eyes work."

    e "All those memories were in color. Now they're... they're grey, Sophia. My memories of her are grey."

    s_thoughts "She makes a guttural sound at that. Somewhere between a sob and a snort and a cough."

    s_thoughts "I wish I knew what to say."

    s_thoughts "There's an anger boiling in me. I consider telling her but I'm afraid it'll just be the obvious thing to do and that's not what she needs from me."

    s_thoughts "Instead I sit in the silence. Loud."

    e "I don't remember any of it."

    e "That's the strange thing."

    e "After it happened and I realized what it was, I thought it... I thought that it was ME who did it. To her."

    s "What?"

    e "I--I know. It doesn't make any sense. But I was standing in the bathroom and I got so afraid that I hurt HER somehow."

    e "Because I was high or something or-- I don't know. I... I don't know."

    e "I still can't remember any of it."

    e "I remember what happened before and I remember what happened after but everything in between is like... you know when a tape recorder gets shut off?"

    s "Yeah?"

    e "Then you restart it. There's like... a sound, that it makes. When it cuts from the before to the after."

    s "Right."

    e "There's a sound."

    e "..."

    e "That's all there is. A sound. From when the tape recorder cut off."

    s_thoughts "There's an ache that I can't quite place in my body."

    e "I've thought about all the things I could've done different."

    s "Eve, you--"

    e "I KNOW."

    s_thoughts "I flinch. She's never raised her voice once in all the time I've known her."

    show eve sad at center

    e "Sorry."

    s "Don't be."

    e "Okay."

    s_thoughts "She goes quiet."

    s_thoughts "I listen to the rain. Every drop is like a gunshot."

    s_thoughts "I wonder if that's what it's like for her but always."

    s_thoughts "I shudder just imagining it."

    show eve pain at center

    e "I think about all the things I could've done. Different."

    s_thoughts "This time I don't speak up."

    e "She told me a few weeks before. That she had feelings for me."
    
    s_thoughts "Feelings. I hope Eve doesn't notice the face I make at that word."

    s "What did you say?"

    e "Nothing. I said... nothing."

    e "I didn't know what to say."

    e "She was my best friend. I wanted her to be my best friend. I wanted her to--"

    s_thoughts "She chokes on the word, then goes very still."

    show eve neutral at center

    s_thoughts "Her body starts to shake. So subtly that I might have missed it if she wasn't the only thing I can pay attention to right now."

    s_thoughts "Suddenly she gasps for air, like she hasn't taken a breath in what feels like forever. Then she goes... still."

    s_thoughts "Very still."

    s_thoughts "Painfully still."

    s_thoughts "Still."

    s_thoughts "I sit across the room from her. I fight every urge in my body that says go to her."

    s_thoughts "The hallway replays in my memory. 'Thank you' she said."

    s_thoughts "For not getting too close."

    s_thoughts "Now I understand why."

    s_thoughts "There's a noise from downstairs. Charlotte's voice. She and the other girls just got home."

    s_thoughts "Eve jumps at that, startles. I catch her eyes. Terrified."

    show eve surprised at center

    e "Leave."

    s "Okay."

    s_thoughts "I stand up and walk out of the room."

    s_thoughts "I look back at her for a moment."

    s_thoughts "She's staring at me."

    s_thoughts "Quivering. She looks small."

    s_thoughts "Small like she learned to be."

    s_thoughts "I turn and exit."

    hide eve with dissolve
    
    scene bg sophiaroom with dissolve

    s_thoughts "I hope I did the right thing."

    s_thoughts "But I don't know. There's no rulebook for any of it."

    s_thoughts "I wonder if she's thought the same thing, too."

    s_thoughts "The rain continues."

    s_thoughts "I don't sleep that night."

    s_thoughts "I don't think she does either."

    stop music fadeout 5.0

    ## ===========================
    ## END OF THE CONFESSION SCENE
    ## ===========================

    ## ===========================
    ## SCENE 7: THE MORNING AFTER "LEAVE"
    ## Sophia didn't sleep. Eve's door is closed.
    ## She doesn't knock. But the meaning is different.
    ## ===========================

    scene bg hallway with Fade(1.5, 1.0, 1.5)

    pause 2.0

    s_thoughts "Morning."

    s_thoughts "The house is waking up. Charlotte is downstairs. The coffee machine is doing its thing. Somewhere a door opens and closes."

    s_thoughts "Normal sounds."

    s_thoughts "I've been awake since last night. There's a specific quality to a sleepless morning -- everything is too sharp. The light. The floorboard under my foot. The sound of my own breathing."

    s_thoughts "Eve's door."

    pause 1.5

    s_thoughts "Closed."

    s_thoughts "Not like in the past."

    s_thoughts "This is different."

    s_thoughts "This is the closed of someone who can't take it back."

    s_thoughts "I'm standing outside her door."

    pause 2.0

    s_thoughts "I look around the hallway."

    s_thoughts "I know this hallway. I sat on this floor. I leaned against this doorframe for twenty minutes and she said 'thank you for sitting in the hallway instead of coming in.'"

    s_thoughts "That was before. Before I knew why the hallway mattered. Before I knew what 'too close' meant for Eve."

    s_thoughts "I raise my hand."

    pause 1.5

    s_thoughts "I don't knock."

    s_thoughts "But this time it doesn't feel right."

    s_thoughts "Last time, not-knocking was respect. The hallway. The boundary. The thing I got right without knowing why."

    s_thoughts "This time not-knocking feels like obeying."

    s_thoughts "'Leave.' She said leave. And I left. And now I'm not-knocking and I don't know if that's the hallway thing or the leaving thing."

    s_thoughts "The same action means different things in different moments."

    s_thoughts "I'm learning that too."

    pause 1.5

    s_thoughts "I put my hand down."

    s_thoughts "I go downstairs."

    scene bg kitchen with dissolve

    play music mus_wrong fadein 2.0

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte is making eggs."

    c "Morning! Scrambled or fried? I'm doing both because Amara likes fried and Isabella likes scrambled and you're a wild card."

    s "Scrambled."

    c "Scrambled! Perfect. Eve? Should I -- I'll make extra."

    s_thoughts "Charlotte reaches for another plate."

    s_thoughts "I watch her. The brightness. The 'of course' in her body language. She's already putting food on a plate for someone who won't come down."

    s_thoughts "She doesn't know."

    s_thoughts "None of them know."

    s_thoughts "Amara might. Amara took everyone to dinner last night. Amara nodded once in the hallway."

    s_thoughts "But Charlotte doesn't know. Charlotte is making eggs."

    s "Charlotte."

    c "Hmm?"

    s "The eggs are burning."

    show charlotte surprised at left

    c "Oh! Oh no. Sorry. I was -- sorry."

    s_thoughts "She rescues the eggs."

    s_thoughts "I eat burnt eggs at the kitchen table."

    s_thoughts "Eve doesn't come down."
    
    s_thoughts "I'm turning it all over in my head. Over and over again."
    
    s_thoughts "Charlotte tries to make small talk but quickly desists when it becomes obvious I'm not listening."
    
    s_thoughts "Cadence. Cadence. Cadence."
    
    s_thoughts "The name won't stop echoing in my head."
    
    s_thoughts "A friend. Her best friend. Someone she trusted."
    
    s_thoughts "Someone who betrayed her."
    
    s_thoughts "I just received Eve's testimony. And I'm already mulling over how it relates to ME."
    
    s_thoughts "I'm ashamed. I can't help it. I don't know how to NOT connect this to my feelings for her."
    
    s_thoughts "I'm her friend. That's what I am to her."
    
    s_thoughts "And her last friend... confessed her feelings... and when Eve didn't reciprocate..."
    
    s_thoughts "I would never. But I can't make Eve believe that. And if Eve finds out how I feel..."
    
    s_thoughts "I shudder. It's the kind that reaches into every crevice of my body."
    
    s_thoughts "Charlotte sits down and she's beaming. I'm not beaming."
    
    s_thoughts "Eve needs a friend."
    
    s_thoughts "I don't know how to be that for her without... all the other stuff."
    
    s_thoughts "I don't know."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 8: EVE DISAPPEARS
    ## The ghost goes back to being a ghost.
    ## But worse. Because now Sophia knows.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)

    pause 1.5

    s_thoughts "Saturday."

    s_thoughts "Eve's door is closed."
    
    s_thoughts "..."

    pause 1.0

    s_thoughts "Sunday."

    s_thoughts "Eve's door is closed."
    
    pause 1.0

    scene bg kitchen night with dissolve

    s_thoughts "Monday."

    s_thoughts "I come downstairs at midnight. The kitchen is dark. The green mug is in the drying rack. She was here."

    s_thoughts "I missed her."

    s_thoughts "Not -- not 'I missed seeing her.' I missed HER. The way she holds the mug with both hands. The way she'd look up and say 'oh, hi' like she was confirming I existed."

    s_thoughts "I miss the sound of her voice when she's yapping about anime." 
    
    s_thoughts "I miss the way she checks ingredients on everything." 
    
    s_thoughts "I miss the way she grips the blanket in a particular way when she gets enthralled by the show."

    s_thoughts "I miss her and the missing isn't about what she told me." 
    
    s_thoughts "It's about who she is when she's not telling me anything."
    
    s_thoughts "It's about who I am to her and who I'm not."

    scene bg hallway night with dissolve

    s_thoughts "Tuesday."

    s_thoughts "3 AM. Footsteps in the hallway. Light. Careful. Eve's footsteps."

    s_thoughts "The bathroom door opens. Closes. Water runs."

    s_thoughts "I lie in bed and listen."

    s_thoughts "The bathroom door opens. Footsteps. Her door. Click."

    s_thoughts "She's moving through the house like a ghost. The original ghost. The one from before, the one who was here and not here and you'd realize you hadn't seen her in three days."

    s_thoughts "But it's worse now."

    s_thoughts "Before, the ghost was a stranger. A girl I was building a file on. A quiet presence with mismatched socks and a green mug."

    s_thoughts "Now the ghost is someone I'm close to. Who told me about herself. About the things she doesn't tell anyone."
    
    s_thoughts "Now the ghost is someone I've fallen head over heels for and I don't know if she feels even remotely the same way and now I'm too scared to tell her how I feel."

    s_thoughts "Because now the ghost is someone who said 'she was like you.'"

    s_thoughts "The knowing makes the absence heavier. It fills the empty space with everything she told me and everything she couldn't finish telling me before Charlotte's voice from downstairs interrupted."
    
    scene bg sophiaroom with dissolve

    s_thoughts "Wednesday."

    s_thoughts "Anime night. Our night. The ritual."

    s_thoughts "I sit in my room at the time we'd normally meet."

    s_thoughts "My phone is dark."

    s_thoughts "No text."

    s_thoughts "No meme. No screenshot. No typing indicator appearing and disappearing."

    s_thoughts "Nothing."

    pause 2.0

    s_thoughts "..."

    s_thoughts "Wait."

    s_thoughts "The typing indicator. Three dots. They appear."

    s_thoughts "My heart does something stupid."

    s_thoughts "The dots disappear."

    s_thoughts "They don't come back."

    pause 2.0

    s_thoughts "She tried. She started to reach and then she stopped."

    s_thoughts "That's something, at least."

    s_thoughts "The ghost went back to being a ghost."

    s_thoughts "And I'm standing outside a closed door in every room of my life."

    stop music fadeout 3.0

    ## ===========================
    ## END OF ACT 2: "THE TELLING"
    ## Eve told. Eve said "Leave." Eve disappeared.
    ## Act 3: "The Distance"
    ## ===========================

    jump eve_ch5_act3

## ===========================
## ACT 3: "THE DISTANCE"
## Scenes 9-16
## Eve is gone. Sophia learns to wait.
## The longest act. Write it SLOW.
## ===========================

label eve_ch5_act3:

    ## ===========================
    ## SCENE 9: SOPHIA SPIRALS
    ## She thinks she did something wrong.
    ## "She was like you" is the hook in her chest.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.5, 1.0)

    play music mus_mourning fadein 3.0

    s_thoughts "I think I did something wrong."

    s_thoughts "I keep replaying it. Every second. Every breath. Every pause."

    s_thoughts "Did I make a face? When she said 'I was raped' -- did something cross my expression before I could catch it? Did she see me react?"

    s_thoughts "When she said 'she was like you' -- did I react in a way that made it about me?"

    s_thoughts "When she said 'I KNOW' and I flinched -- did the flinch hurt her? Did she see me afraid of her voice and decide that was the thing she was afraid of?"

    s_thoughts "The tape recorder. The click. The sound between before and after."

    s_thoughts "I keep hearing it. Not hers. Mine."

    s_thoughts "Before: Eve on the bed, talking. After: Eve saying 'leave.' The click in between -- Charlotte's voice downstairs, and Eve's face going from raw to terrified in a single frame."

    s_thoughts "I didn't cause that. Charlotte's voice caused that. The interruption caused that."

    s_thoughts "But I keep thinking: what if I was already doing something wrong before the interruption? What if she was already pulling away and Charlotte just gave her the excuse?"

    pause 2.0

    s_thoughts "And underneath all of it."

    s_thoughts "'She was like you.'"

    s_thoughts "Eve's best friend was like me. A noticer. Someone who saw her."

    s_thoughts "And that person used the seeing to destroy her."

    s_thoughts "I am the same kind of person."

    s_thoughts "The observation instinct. The filing. The way I watched Eve before she invited me to watch. The way I noticed the bookshelf and the mug and the socks and the door."

    s_thoughts "That's not just my flaw anymore."

    s_thoughts "That's the shape of the thing that happened to Eve."

    s_thoughts "Someone saw her. Someone was like me. And then."

    pause 1.5

    s_thoughts "But there's the other side of it. The side I keep pushing away."

    s_thoughts "'She was like you' doesn't just mean 'you're dangerous.'"

    s_thoughts "It means I mattered. The way Cadence mattered. Eve let me in the way she let Cadence in. Not because I'm a threat -- because I'm the kind of person Eve lets in."

    s_thoughts "And I can't do anything with that. I can't hold 'she might have feelings for me' and 'the last person who had feelings for her destroyed her' in the same hand. They don't fit. But they're both there."

    pause 1.5

    s_thoughts "And the other thing."

    s_thoughts "'I thought it was ME who did it. To her.'"

    s_thoughts "Eve's first instinct was to think she was the one who hurt Cadence."

    s_thoughts "That's not just self-blame. That's -- the event is fractured. In Eve's telling, there's no clean victim and no clean villain. The categories don't fit. The drugs blur it. The memory is gone -- just a sound, a click, a tape recorder shutting off."

    s_thoughts "I'm sitting with 'Eve was hurt' and also 'Eve's own reality about the event is broken' and the second thing makes the first thing heavier, not lighter."

    s_thoughts "Because I can't just be angry at Cadence."

    s_thoughts "Eve can't just be angry at Cadence."

    s_thoughts "That's the wound. Not what happened. What it did to Eve's ability to know what happened."

    pause 2.0

    s_thoughts "I don't know that Eve's retreat isn't about me."

    s_thoughts "I don't know that she's not behind that closed door thinking about every time I noticed something and wondering if I'm building a file on her with the intent of hurting her."

    s_thoughts "I don't know anything."

    s_thoughts "I'm lying on my bed staring at the ceiling and I don't know anything."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 10: CHARLOTTE AND ISABELLA -- THE HOUSE CONTINUES
    ## SHORT. Two paragraphs. Don't steal Eve's air.
    ## Cross-route threads: Charlotte's wobble, Isabella's phone.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "The house continues."
    
    show charlotte happy at left with dissolve

    s_thoughts "Charlotte cooks dinner. The brightness wobbles once -- her hand pauses over the pan, her face goes somewhere for a second, then the smile reassembles. 'Of course! Seconds, anyone?' Nobody sees it but me. I see it and I don't follow up because I'm thinking about Eve."

    show isabella neutral at right with dissolve

    s_thoughts "Isabella is on the phone. She's texting someone. Lumi, probably."

    s_thoughts "Amara reads."

    s_thoughts "The house is the same house. Four people in a kitchen, one empty chair. The empty chair used to be background. Now it's the loudest thing in the room."
    
    s_thoughts "God, I miss her."

    hide isabella 
    hide charlotte
    with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 11: LILA -- THE ROCK
    ## Lila comes to the house. She doesn't usually.
    ## She plants the seed: "it's not about you."
    ## Partial reframe. Not fully landed.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Thursday."

    s_thoughts "Lila is at the house."

    s_thoughts "She doesn't come to the house that often. Lila exists on campus and at restaurants and on benches. She's the outside. The house is the inside."

    s_thoughts "She's sitting on the couch."
    
    play music mus_eve fadein 2.0

    show lila happy at center with dissolve

    l "Okay. Talk."

    s "Hi to you too."

    l "I don't do preamble. You've been dodging my texts for a week. You look like you haven't slept. And I'm sitting on a couch in a house I've been to exactly twice."

    show lila annoyed at center

    l "So. Talk."

    s_thoughts "I sit on the other end of the couch."

    s_thoughts "I can't tell Lila what Eve said. I wouldn't. That's not mine to share."

    s "She told me something."

    l "Eve?"

    s "Yeah. She told me something big. Something about -- about what happened to her. And then she told me to leave. And then she disappeared."

    l "Disappeared like..."

    s "Like Eve disappears. Door closed. Not at meals. Moving through the house at 3 AM."

    show lila neutral at center

    l "And you think you did something wrong."

    s "How do you know that's what I think?"

    l "Because you're Sophia and that's what you always think."

    s_thoughts "That lands."

    l "Did you do something wrong?"

    s "I don't know."

    l "What did you do?"

    s "I sat on the floor. I listened. I didn't try to fix it."

    l "That sounds right."

    s "Then she told me to leave."

    l "Because something interrupted?"

    s "How did you -- yeah. The other girls came home."

    l "And she got scared."

    s "She got scared."

    s_thoughts "Lila is quiet for a moment. She's looking at her hands. She does this sometimes -- goes still in a way that's so unlike Lila that it always startles me."

    show lila happy at center

    l "Okay. My advisor -- the club advisor -- she said something once. She said sometimes people share something huge and then they need to go be alone with the fact that they shared it."

    s "..."

    l "Like, the sharing isn't the hard part. Living in the world afterward is the hard part. Waking up and knowing someone else knows."

    s_thoughts "I think about Eve. Waking up. Knowing I know."

    l "It's not about you, Sophia."

    s "How do you know that?"

    l "Because you sat on a floor and listened. That's not wrong. That's what she asked for."

    s "She asked me to leave."

    l "She asked you to leave because she got scared. Not because you did something."

    s_thoughts "I want to believe that."

    s_thoughts "I'm not there yet."
    
    show lila neutral at center

    l "Look. I don't know what she told you. I'm not asking. But the girl who watches anime with you and texts you memes and let you sit in her hallway for twenty minutes -- that girl didn't disappear because you sat on her floor wrong."
    
    s "Lila..."
    
    l "Don't Lila me."
    
    s "Lila."
    
    l "Okay. You clearly need to Lila me."
    
    s "What if... it's because... she knows?"
    
    l "She knows what?"
    
    s "About... about how I feel."
    
    s_thoughts "I'm whispering, as if Eve is listening to what we're saying. She could be. The walls are thin."
    
    l "I don't think she does."
    
    s "How do you know?"
    
    l "Because if she knew she might not have told you."
    
    s_thoughts "That takes a second to sink in. It makes it worse."
    
    s "Oh god."
    
    l "It's okay. It's not your fault."
    
    l "But it sounds like what she needs you to be right now is a friend."
    
    s "I'm scared I can't be that."
    
    s "I'm scared I can't... I can't separate how I feel about her."
    
    l "That's okay." 
    
    l "You just have to try."
    
    s_thoughts "'You just have to try.'"

    s_thoughts "Lila stays on the couch for an hour. We don't talk about Eve for most of it. She tells me about her club. She tells me about a guy in her econ class who sneezed so hard his glasses flew off. She shows me a video of a cat falling off a table."

    s_thoughts "She doesn't fix anything."

    s_thoughts "She just stays on the couch."

    l "I gotta go. Text me back this time."

    s "I'll text you back."

    l "Promise."

    s "Promise."

    show lila happy at center

    s_thoughts "She hugs me. Lila gives aggressive hugs. The kind where your ribs complain."

    l "She'll come back. People come back."

    s_thoughts "She leaves."

    hide lila with dissolve

    s_thoughts "'It's not about you.'"

    s_thoughts "I hear it."

    s_thoughts "I'm not convinced."

    ## ===========================
    ## SCENE 11.5: SOPHIA SITS WITH IT
    ## Brief. Time passes. The seed hasn't landed yet.
    ## Breathing room between Lila and Amara.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Days."

    s_thoughts "Friday. Saturday. Sunday."

    s_thoughts "I carry Lila's words around like a stone in my pocket. 'It's not about you.' I take it out, look at it, put it back."

    s_thoughts "I test it against my memory of 'leave.'"

    s_thoughts "Against the sound of Eve's voice when she said it. Not angry. Terrified."

    s_thoughts "It's not about you."

    s_thoughts "But she said 'she was like you.' She SAID that. The person who hurt her was like me. How is that not about me?"
    
    s_thoughts "About how I feel about her?"

    s_thoughts "I go to class. I eat meals. I answer Lila's texts. I don't look at Eve's door when I walk past it."

    s_thoughts "That's a lie. I always look."

    s_thoughts "It's always closed."

    stop music fadeout 2.0
    pause 1.5

    ## ===========================
    ## SCENE 12: AMARA
    ## Short. Sharp. The reframe that lands.
    ## "Because she's the closest she's gotten
    ## in a very long time."
    ## ===========================

    scene bg hallway night with Fade(0.8, 0.3, 0.8)

    play music mus_fragile fadein 2.0

    s_thoughts "Monday."

    s_thoughts "The hallway. I'm coming out of my room."

    show amara neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "She's just there. Like she was waiting. Like she's always there at the exact moment the hallway needs her."

    a "She's okay."

    s_thoughts "That's it. No transition. Amara dropped the sentence into the air like it was nothing."

    s "Is she?"

    a "She told you."

    s "How do you--"

    a "She told me she was going to."

    s_thoughts "The hallway. Thursday before the confession. Eve and Amara. The low conversation I couldn't hear. The nod."

    s "She told you she was going to tell me."

    a "Mm."

    s "But she already told you. Before."

    a "She didn't tell me. I knew."

    s_thoughts "Amara doesn't elaborate. She doesn't need to. Amara sees without demanding to be shown. That's the whole thing."

    s "Then why is she--"

    pause 1.0

    a "You're the closest she's gotten in a very long time."

    s_thoughts "That sentence."

    s "Then why is she--"

    a "Because she's the closest she's gotten in a very long time."

    pause 2.0

    s_thoughts "Oh."

    s_thoughts "...Oh."

    a "Don't chase her."

    s "I'm not."

    a "Good."

    s_thoughts "She starts to walk away."

    s "Amara."

    s_thoughts "She stops."

    s "How long?"

    a "As long as she needs."

    s_thoughts "She goes downstairs."

    hide amara with dissolve

    s_thoughts "I stand in the hallway."

    s_thoughts "The closest she's gotten in a very long time."

    s_thoughts "The closest she's gotten is the most dangerous place for Eve to be."

    s_thoughts "I'm not a threat."

    s_thoughts "But I'm the shape of one."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 13: NOVA'S CLASS -- THE PAPER
    ## Sophia STRUGGLES. 2 AM. Cursor blinking.
    ## Three false starts. The one she hands in
    ## is the one she wrote because she gave up.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    play music mus_2am fadein 3.0

    s_thoughts "2 AM."

    s_thoughts "The cursor blinks."

    s_thoughts "Nova's paper. Due Friday. 'The ethnographer's obligation to testimony: a reflection on the ethics of witness.'"

    s_thoughts "I've been staring at this document for three hours."

    s_thoughts "Attempt one."

    s_thoughts "'The ethnographer, upon receiving testimony from the subject, enters into a relationship defined by the asymmetry of--'"

    s_thoughts "Delete."

    s_thoughts "Too academic. I sound like I'm writing about someone else's life from a safe distance. I'm describing Eve's pain in the passive voice."

    s_thoughts "Attempt two."

    s_thoughts "'When someone tells you the worst thing that ever happened to them, you have two choices: hold it or drop it. Most people--'"

    s_thoughts "Delete."

    s_thoughts "Too clever. I'm performing insight. I'm turning her into an essay question."

    s_thoughts "Attempt three."

    s_thoughts "'I sat on the floor of someone's room and she told me--'"

    s_thoughts "Delete."

    s_thoughts "That's hers. That's not mine to write about."

    pause 2.0

    s_thoughts "The cursor blinks."

    s_thoughts "It's 2:30 AM. The house is quiet. Eve's kind of quiet."

    s_thoughts "I think about what Nova said. 'The subject gave you something. What do you do with it?'"

    s_thoughts "I think about the village. The ethnographer who sees the thing nobody's looking at. Option one: write about it. Option two: keep it. Option three: stay, and let the knowing change how you move."

    s_thoughts "I start typing."

    s_thoughts "Not an essay. Not an argument. Not a thesis with supporting evidence and a clean conclusion."

    s_thoughts "I write about glass houses."

    s_thoughts "About what it means to see inside one. About the difference between looking and witnessing." 
    
    s_thoughts "About the fact that stones are the obvious danger but the real one is your own reflection in the glass -- the moment you see yourself looking and have to decide if you're a visitor or a threat."

    s_thoughts "I write about pillows."

    s_thoughts "The document is messy. It meanders. It contradicts itself. At one point I write 'I don't know what I'm saying' and leave it in because I don't."

    s_thoughts "It has one line that I don't delete."

    s_thoughts "'If you're visiting a glass house, don't throw stones at the occupants. But don't be afraid to offer a pillow.'"

    s_thoughts "I stare at that line."

    s_thoughts "It's not academic writing."

    s_thoughts "I hand it in because it's 3 AM and I've given up trying to make it good."

    stop music fadeout 2.0

    scene bg officehours with Fade(0.8, 0.3, 0.8)

    play music mus_afternoon fadein 2.0

    s_thoughts "Thursday. Nova's office hours."

    show professor neutral at center with dissolve

    s_thoughts "She has my paper on her desk. She's looking at it the way she looks at the room -- the settling thing."

    nova "This isn't academic writing."

    s "I know. I'm sorry. I can redo it."

    nova "I didn't say redo it."

    s_thoughts "She looks at me."

    show professor happy at center

    nova "This is testimony."

    s_thoughts "I don't say anything."

    nova "You wrote a paper about visiting a glass house. Most of the class wrote about theoretical scenarios and cited readings they half-understood. You wrote about standing outside someone's door and choosing not to knock."

    s "I didn't say that."

    nova "You said 'the ethnographer who arrives at the threshold has to decide whether crossing it is care or invasion.' That's not a thesis statement. That's someone who's been standing at a threshold."

    s_thoughts "My hands are in my lap."

    nova "It's the best thing you've written."

    pause 1.5

    s_thoughts "I sit with that."

    s_thoughts "I wrote testimony because I couldn't write analysis."

    s_thoughts "That doesn't feel like growth. It feels like giving up on understanding."

    s_thoughts "Maybe those are the same thing."

    s "Thank you, Dr. Nova."

    nova "You're welcome. And Sophia?"

    s "Yeah?"

    show professor neutral at center

    nova "The pillow line. Keep that."

    hide professor with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 14: AMARA AND EVE -- THE QUIET MOMENT
    ## Sophia passes a room. They're together.
    ## Not talking. Eve is with someone.
    ## Not Sophia. Amara.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)

    s_thoughts "Saturday morning."

    s_thoughts "I'm walking through the hallway. Heading downstairs."
    
    scene bg livingroom with dissolve

    show amara neutral at left
    show eve neutral at right
    with dissolve

    s_thoughts "The living room."

    s_thoughts "Amara is in the armchair. Eve is on the floor near the couch."

    s_thoughts "They're not talking."

    s_thoughts "Amara has a book. Eve has her phone, screen dark, just holding it."

    s_thoughts "The same position as before. The same room. The same two people in the same comfortable silence."

    s_thoughts "Eve is there."

    s_thoughts "Eve is in a room with another person."

    s_thoughts "Not me. Amara."

    pause 1.5

    s_thoughts "Because Amara is the one who doesn't demand. Amara didn't earn this the way I did -- the anime nights, the hallway, the floor playlist, the weeks of Wednesday and Saturday. Amara just is this. Stillness that doesn't ask anything of the person next to it."

    s_thoughts "Eve's shoulders are down. Her jaw is loose. She's not calculating proximity."

    s_thoughts "She's just there."

    s_thoughts "I feel -- I check what I feel."

    s_thoughts "Somewhere between jealousy and relief."
    
    s_thoughts "On the one hand I'm glad Eve is out and spending time with someone."
    
    s_thoughts "On the other--and I'm embarrassed that it's true--I'm jealous that it's someone other than me."

    s_thoughts "Eve is somewhere. Eve is with someone. Eve isn't behind the closed door."
    
    s_thoughts "But she's not with me."

    s_thoughts "I don't go in."

    s_thoughts "This isn't for me."

    s_thoughts "But I stay near the doorway for a moment."

    s_thoughts "The hallway. Again. Presence without intrusion."

    s_thoughts "I go upstairs."

    hide amara with dissolve
    hide eve with dissolve

    pause 1.0

    ## ===========================
    ## SCENE 15: THE WAIT
    ## Time passes. Days. A week.
    ## The floor playlist callback.
    ## Sophia is learning to wait.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.5, 1.0)

    play music mus_eve fadein 3.0

    s_thoughts "Days."

    s_thoughts "A week. Maybe more. I've stopped counting."

    s_thoughts "Eve's door opens and closes. She appears at meals sometimes. A ghost at the edge of the kitchen. She makes tea and takes it upstairs. She doesn't seek me out."

    s_thoughts "She doesn't avoid me either."

    s_thoughts "Avoidance would require acknowledging what happened. She just... exists at a distance."

    s_thoughts "I'm learning to wait."

    s_thoughts "Not the active waiting of someone who's expecting something. Not the 'I'm giving you space so you'll come back' waiting that's really just patience with an agenda."

    s_thoughts "The waiting of someone who is simply not leaving."

    s_thoughts "I go to class. I eat meals. I text Lila back. I don't check Eve's door. I don't not-check Eve's door."

    s_thoughts "I just live in the house."

    pause 2.0

    s_thoughts "One night."

    s_thoughts "Alone in my room. Late."

    s_thoughts "I open the playlist."

    s_thoughts "Eve's floor playlist. 'floor.' The one she gave me in her room. The one I held like a gift."

    s_thoughts "I haven't listened to it since before."

    s_thoughts "I put my earbuds in."

    stop music fadeout 2.0

    pause 1.5

    s_thoughts "I press play."

    pause 1.0

    s_thoughts "Pop. Folk. The songs I don't recognize. The songs that are Eve's private language for bad days."

    s_thoughts "I'm not analyzing the choices. I'm not filing the genres. I'm just listening."

    s_thoughts "I think about her hands when she was showing me the shelf. The way she touched the spines like they were old friends."

    s_thoughts "I think about the convenience store. 'Someone has to.' The way she didn't know she was funny."

    s_thoughts "I think about the almost-touch. Her knuckle against mine. Two seconds. She didn't flinch."
    
    s_thoughts "About the shoulders. The moment I've been replaying in my head over and over again."

    s_thoughts "I think... I think I might be in love with her."

    s_thoughts "Oh god. I can't believe I just admitted that to myself."
    
    s_thoughts "After everything, THAT is where I land?"
    
    s_thoughts "And now after all that's happened, the confession, the telling, the ghost, it didn't go away."

    s_thoughts "It just made it impossible to say."

    s_thoughts "A song ends. Another starts."

    pause 1.5

    s_thoughts "Country."

    play music mus_mourning fadein 3.0

    s_thoughts "The song."

    s_thoughts "The one that came on and Eve blushed and said 'it was...' and didn't finish."

    s_thoughts "It was her favorite."

    s_thoughts "Cadence's favorite."

    s_thoughts "Eve kept it on the playlist. Couldn't bring herself to take it off."

    pause 2.0

    s_thoughts "I hear it differently now."

    s_thoughts "I know what the song meant. I know why Eve trailed off. I know what 'it was...' was going to be before the words stopped."

    s_thoughts "It was her favorite."

    s_thoughts "Cadence."

    s_thoughts "Like music."

    pause 2.0

    s_thoughts "I don't skip it."

    s_thoughts "I let it play."

    s_thoughts "The song fills my room. The room fills with everything Eve told me and everything she couldn't finish and everything that lives in the space between a tape recorder's click."

    s_thoughts "I sit on the floor."

    s_thoughts "Eve's listening position."

    s_thoughts "The song finishes."

    s_thoughts "The next one starts. Something else. Something lighter."

    s_thoughts "I stay on the floor."

    pause 2.0

    s_thoughts "I'm not waiting for Eve to come back."

    s_thoughts "I'm waiting with Eve. Even though she's in her room and I'm in mine. Even though the hallway is between us and neither of us is crossing it."

    s_thoughts "I'm on the floor. She's wherever she is."

    s_thoughts "Same playlist."
    
    s_thoughts "I wonder if I have a song, now."
    
    s_thoughts "I don't know whether that's good or bad."
    
    s_thoughts "Those lines are blurring more and more as of late."

    stop music fadeout 4.0

    pause 2.0

    ## ===========================
    ## SCENE 16: THE DOOR OPENS
    ## SHORT. Resist giving the reader
    ## more than the door.
    ## "Hey." / "Hey."
    ## ===========================

    scene bg hallway with Fade(1.0, 0.5, 1.0)

    play music mus_eve fadein 3.0

    s_thoughts "Tuesday."

    s_thoughts "Not a special day. No catalyst. Just a Tuesday."

    pause 1.5

    s_thoughts "I'm walking to the bathroom."

    s_thoughts "Eve's door."

    pause 2.0

    s_thoughts "Open."

    show eve neutral at center with dissolve

    s_thoughts "She's inside. On her bed. Reading."

    s_thoughts "She looks up."

    pause 1.5

    e "Hey."

    pause 1.5

    s "Hey."

    pause 2.0

    s_thoughts "Not an invitation."

    s_thoughts "Not a refusal."

    s_thoughts "An open door."

    s_thoughts "I keep walking."

    hide eve with dissolve

    pause 2.0

    s_thoughts "The last time I saw Eve in that room."

    s_thoughts "Quivering. Small. 'Leave.'"

    pause 1.0

    s_thoughts "And now."

    s_thoughts "'Hey.'"

    pause 1.5

    s_thoughts "I think about how far those two images are from each other."

    s_thoughts "'Leave' and 'Hey.'"

    s_thoughts "How far she walked to get from one to the other."

    s_thoughts "How far we both walked."

    pause 2.0

    s_thoughts "The door is open."

    s_thoughts "I could go back. I could stand in the doorway and say the thing I've been carrying since the floor playlist. Since the convenience store. Since the earbuds in the kitchen."

    s_thoughts "I could say all the things I've been feeling." 
    
    s_thoughts "The love and the fear and the jealousy and the worry that the shape of my feelings is the shape of what hurt her and I don't know what to do with that because I think I'm falling in love with her and I'm so scared to tell her but I'm not sure how to not."

    s_thoughts "I don't say it."

    s_thoughts "Saying it now would be for me, not for her."
    
    s_thoughts "'She was like you.'"
    
    s_thoughts "That's the thing I have to avoid. Even if it hurts."

    s_thoughts "So I hold it."

    s_thoughts "The door is open. I have something I'm not offering."

    s_thoughts "That's enough."

    stop music fadeout 4.0

    pause 3.0

    scene black with Fade(2.0, 1.0, 2.0)

    "Chapter 5: Telling -- End"

    jump eve_ch6
