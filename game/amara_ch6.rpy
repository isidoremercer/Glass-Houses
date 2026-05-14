## amara_ch5.rpy -- Glass Houses
## Chapter 5: "The Identity" -- Amara Route
## Act 1: "Aftermath" 

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
## CHAPTER 6 START
## ===========================

label amara_ch6:

    ## ===========================
    ## SCENE 1: CHOICE AFTERMATH
    ## Different per path. The morning after.
    ## House path: Charlotte is different.
    ## Amara path: Charlotte's muffins. The guilt.
    ## ===========================

    if ch5_chose_house:
        ## Player chose "Go to Charlotte" in Scene 20
        jump amara_ch6_house_aftermath
    else:
        ## Player chose "Stay with Amara" in Scene 20
        jump amara_ch6_amara_aftermath

label amara_ch6_house_aftermath:

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    play music mus_morningafter fadein 3.0

    s_thoughts "Friday morning."

    s_thoughts "I come downstairs because I can smell coffee. Not Charlotte's usual coffee -- the good one. The one she saves for company."

    s_thoughts "She's in the kitchen."

    if charlotte_confession == True:
        show charlotte smile at center with dissolve

        s_thoughts "She sees me and does a thing with her face. Not the brightness. Something more deliberate -- a smile that's been practiced in a bathroom mirror."

        c "Morning!"

        s "Morning."

        c "Coffee's ready. I used the good beans."

        s "I noticed."

        s_thoughts "We look at each other."

        s_thoughts "The confession is in the room. It's not going anywhere. It's just there, like a piece of furniture we both have to walk around."

        c "So."

        s "So."

        c "This is weird, right?"

        s "A little."

        show charlotte happy at center

        c "Good. I thought it was just me."

        s_thoughts "She pours my coffee. She adds the right amount of milk without asking."

        s_thoughts "She knows how I take my coffee."

        s_thoughts "Of course she does."

        c "I want you to know that I'm not going to be weird about it."

        s "Charlotte--"

        c "I SAID I'm not going to be weird about it. That's different from not BEING weird about it. I'll probably be weird about it. But I'm trying."

        s "You don't have to try."

        show charlotte neutral at center

        c "I always try."

        s_thoughts "That lands differently now."

        c "Anyway. Muffins on the counter. Amara's is labeled."

        s_thoughts "She turns back to the stove."

        s_thoughts "Her shoulders are tight."

        s_thoughts "But she's here. She's standing in the kitchen the morning after confessing to someone who doesn't feel the same way, and she's making coffee."

        s_thoughts "That's either incredibly brave or incredibly Charlotte."

        s_thoughts "Same thing."

        s_thoughts "The muffin with Amara's name on it is on the counter. Charlotte wrote it in her neat handwriting. A little heart after the A."

        s_thoughts "She puts hearts on everyone's. I checked."

        s_thoughts "But I checked."

        hide charlotte with dissolve

    else:
        ## No confession path
        show charlotte happy at center with dissolve

        s_thoughts "She's humming. Something I don't recognize."

        c "Sophia! Good morning!"

        s "Morning."

        s_thoughts "She looks different. Something soft. Like the mask got washed and put on slightly crooked and she hasn't noticed."

        c "I saved you coffee. And there's muffins. Obviously."

        s "Obviously."

        c "Last night was--"

        s_thoughts "She pauses."

        c "Thank you. For coming home."

        s "You don't have to thank me."

        show charlotte smile at center

        c "I know. I'm doing it anyway."

        s_thoughts "She hands me coffee. Blue mug."

        s_thoughts "Her hand brushes mine on the handle."

        s_thoughts "She doesn't pull away."

        s_thoughts "I do."

        s_thoughts "She doesn't notice. Or she does and the mask absorbs it."

        c "I called my mom back this morning."

        s "Yeah?"

        c "It was-- it was a conversation. A real one. I told her I can't be her helper gal from two hundred miles away."

        s "What did she say?"

        show charlotte neutral at center

        c "She said 'of course, sweetheart.' Which is-- it's my mom's version of 'of course.' It means the same thing mine does."

        s "Which is?"

        c "I'll process that later. Here, have a muffin."

        s_thoughts "She changes the subject like she's changing a channel."

        s_thoughts "But something is different. The kitchen-floor conversation did something. Moved a wall. Just an inch."

        hide charlotte with dissolve

    s_thoughts "I take my coffee to the living room."

    scene bg livingroom with dissolve

    s_thoughts "The armchair is empty."

    s_thoughts "Amara's book isn't on the side table."

    s_thoughts "She's usually here by now."

    s_thoughts "She's not here."

    s_thoughts "I sit on the couch."

    s_thoughts "The cushion next to mine is empty."

    s_thoughts "I drink my coffee."

    s_thoughts "The house ticks."

    s_thoughts "'Be honest about what you chose.'"

    s_thoughts "I chose Charlotte."

    s_thoughts "The armchair is empty."

    stop music fadeout 3.0

    jump amara_ch6_scene2

label amara_ch6_amara_aftermath:

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    play music mus_morningafter fadein 3.0

    s_thoughts "Friday morning."

    s_thoughts "I come downstairs."

    s_thoughts "The muffins are on the counter."

    s_thoughts "Three trays. Labeled. Eve. Isabella. Amara."

    s_thoughts "Mine is separate. No label. I can tell it's the best."

    s_thoughts "Charlotte made these while I was at the library holding Amara's hand."

    s_thoughts "The guilt sits in my stomach like a stone I swallowed whole."

    s_thoughts "Charlotte's not in the kitchen."

    show isabella neutral at center with dissolve

    s_thoughts "Isabella is."

    i "Morning."

    s "Morning."

    i "Coffee's there. Charlotte made it before she left."

    s "Left?"

    i "Class. She said she had an early thing."

    s_thoughts "Charlotte doesn't have early things on Fridays."

    i "She seemed fine."

    s_thoughts "Isabella says 'fine' like she knows it's a loaded word in this house."

    s "How was last night?"

    show isabella happy at center

    i "She baked. We talked. I made poorly timed jokes. She was upset about her mom. The usual Charlotte thing."

    s_thoughts "'The usual Charlotte thing.' Usual."

    i "She asked where you were. I said the library."

    s "What did she say?"

    show isabella neutral at center

    i "She said 'of course.' And then she frosted a muffin so aggressively the top came off."

    s_thoughts "My chest does a thing."

    i "Anyway. She's fine. You're fine. Everyone's fine."

    s_thoughts "Isabella picks up her mug."

    i "Lumi says hi, by the way."

    s "Lumi says hi?"

    i "She says 'tell Sophia the muffins are a data point.' I don't know what that means."

    s_thoughts "I do."

    hide isabella with dissolve

    s_thoughts "I take my muffin. I sit at the table."

    s_thoughts "Charlotte's handwriting on Amara's label. Small. Precise. A heart after the A."

    s_thoughts "She puts hearts on everyone's."

    s_thoughts "I know because I checked last time."

    s_thoughts "The muffin is perfect."

    s_thoughts "They're always perfect."

    s_thoughts "That's the problem."

    stop music fadeout 3.0
    
    pause 2.5

    s_thoughts "Later. The porch."

    scene bg porch with dissolve

    s_thoughts "Amara is in her spot."
    
    show amara neutral at center with dissolve

    s_thoughts "I sit in mine."

    s_thoughts "Three inches."

    s_thoughts "Maybe two."

    a "You're carrying something."

    s "Charlotte's muffin."

    a "That's not what I mean."

    s "I know."

    s_thoughts "The porch is quiet."

    s "I stayed. And she made muffins alone."

    a "Isabella was there."

    s "Isabella isn't me."

    a "No."

    s_thoughts "She doesn't tell me it's okay. She doesn't tell me I made the right choice."

    a "You're feeling guilty."

    s "Very."

    a "The guilt is information."

    s "Information about what?"

    a "About what you value."

    s_thoughts "I look at her."

    a "You chose to stay. The guilt means you care about what you left."

    a "Both things are real."

    s "That doesn't make it easier."

    a "It's not supposed to."

    s_thoughts "She reaches over."

    s_thoughts "Her hand on mine. Brief. Warm."

    s_thoughts "She pulls it back."

    a "Thank you for staying."

    s "You don't have to--"

    a "I don't HAVE to. I want to."

    s_thoughts "The half-degree."

    s_thoughts "Two and a half inches."

    hide amara with dissolve

    stop music fadeout 2.0
    
    jump amara_ch6_scene2

    ## ===========================
    ## SCENE 2: KATIE ARRIVES
    ## Campus. She's back. She's sharp.
    ## Brief setup -- appearance, recognition, tension.
    ## ===========================

label amara_ch6_scene2:

    scene bg campus with Fade(0.8, 0.3, 0.8)

    stop music fadeout 0.5

    s_thoughts "Monday."

    s_thoughts "I'm walking between buildings. The usual route. Library to lecture hall. I have Nova in forty minutes and I'm early, which means I'm anxious, because I'm only early when something is buzzing."

    s_thoughts "The campus is doing autumn hard now. Orange leaves. Students in scarves. Someone's playing guitar badly near the fountain."

    s_thoughts "I round the corner by the humanities building."

    s_thoughts "And I stop."

    show ex neutral at center with dissolve

    s_thoughts "Red jacket."

    s_thoughts "Brown bob."

    s_thoughts "She's standing outside the humanities building looking at her phone. One hand in her jacket pocket. The posture of someone who knows how to wait."
    
    play music mus_tension fadein 1.5

    s_thoughts "Katie."

    s_thoughts "My body recognizes her before my brain catches up. Something in my chest does the old thing -- the thing I thought I'd uninstalled. A quick, hot pulse. Not attraction. Recognition."

    s_thoughts "Katie Ecks is on my campus."

    s_thoughts "She looks up."

    k "Sophia."

    s_thoughts "She says my name like a fact. Not warm. Not cold. Just: information."

    s "Katie."

    s_thoughts "She puts her phone away. Looks at me. The look I remember -- the one that made me feel like I was being read in real time."

    s_thoughts "I used to love that look."

    s_thoughts "I used to hate that look."

    k "You look different."

    s "It's been months."

    k "You look softer."

    s_thoughts "She doesn't mean it as a compliment."

    s "What are you doing here?"

    k "Visiting a friend at the law school. She's in class."

    s_thoughts "She gestures vaguely at the buildings."

    k "I was going to text you. But here you are."

    s "Here I am."

    k "Can we talk?"

    s_thoughts "Every alarm in my body fires at once."

    s "I have class in--"

    k "I know you're early. You're always early when you're anxious. You show up thirty minutes before things because the waiting gives you something to do with your hands."

    s_thoughts "She's right."

    s_thoughts "She was always right about the mechanics."

    s "...Okay. Talk."

    k "Not here. Coffee?"

    s_thoughts "I should say no."

    s "Sure."

    hide ex with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 3: THE KATIE SCENE -- THE SET PIECE
    ## SHARED SCAFFOLDING. Same Katie lines regardless
    ## of path. Different defender.
    ## fire >= 2: LILA defends.
    ## fire <= 1: AMARA defends.
    ## Both versions: LONG. Painful. True.
    ## ===========================

    scene bg restaurant with Fade(0.8, 0.3, 0.8)

    s_thoughts "The coffee place near the humanities building. Small. Two floors. We sit upstairs because Katie always sat upstairs."

    s_thoughts "Some things you don't unlearn."

    show ex neutral at center with dissolve

    play music mus_glass fadein 2.0

    s_thoughts "She orders black coffee. I order a latte. She raises an eyebrow at the latte. I don't explain it."

    s_thoughts "We sit."

    k "So."

    s "So."

    k "How's the house?"

    s "It's good."

    k "That's not what I hear."

    s_thoughts "My stomach drops."

    s "What do you hear?"

    k "Jess knows Amy. Amy knows your friend Lila. Lila talks."

    s_thoughts "Of course she does."

    k "Lila talks a LOT, apparently. About you. About the house. About some girl you're obsessed with."

    s "I'm not obsessed."

    k "Lila's word, not mine."

    s_thoughts "She sips her coffee. The way she holds the cup -- both hands, like she's centering herself. Like the coffee is a prop in a scene she's directing."

    k "Tell me about her."

    s "About who?"

    k "The girl. Amara."

    s_thoughts "My jaw tightens."

    s "How do you know her name?"

    k "Lila talks, Sophia. I just said that."

    s "She's my housemate."

    k "And?"

    s "And she's important to me."

    k "Important how?"

    s "Katie, what do you want?"

    show ex annoyed at center

    s_thoughts "She puts her cup down."

    k "I want to know if you're doing the thing."

    s "The thing."

    k "The thing. Our thing. The thing that ended us."

    s "We don't have a 'thing.'"

    k "We absolutely have a thing, Sophia. I lived through it."

    s_thoughts "The coffee shop is quiet. Two other tables. Someone's typing."

    show ex neutral at center

    k "You find someone interesting."

    s_thoughts "I don't respond."

    k "You find them interesting and you make them your whole world. You study them. You learn their patterns. You memorize what they eat and how they sleep and what makes them laugh."

    s "That's called caring about someone."

    k "That's called case-studying someone. I know because I was the case study."

    s_thoughts "My hands are around my latte."

    k "You did it with me. Remember? All the things you learned about me. The little stuff."

    s "You liked it."

    k "I loved it. At first."

    s_thoughts "She looks out the window."

    show ex annoyed at center

    k "And then I realized you weren't loving me. You were translating me. Making me legible. Turning me into something you could understand."

    s_thoughts "My chest tightens."

    k "And when you couldn't understand me -- when I was complicated or contradictory or just tired -- you panicked. Because the file didn't work anymore."

    s "That's not--"

    k "You're doing the same thing you always do."

    s_thoughts "She leans forward."

    k "You found someone interesting and you're burning everything else down to get close to them."

    k "You did it with me. You're doing it now."

    s_thoughts "The words sit in the air between us."

    s_thoughts "I want to say she's wrong."

    s_thoughts "She's not wrong."

    k "So I'm asking you. Because someone should. Are you doing the thing?"

    s "You came here to lecture me?"

    k "I came here to see a friend at the law school. I'm lecturing you for free."

    s_thoughts "She almost smiles. The Katie-smile. Sharp and quick."

    k "I'm not your enemy, Sophia. I'm someone who's been where you are."

    s "You're my ex."

    k "I'm your ex who was right about why we broke up."

    s_thoughts "That hits. It hits because it's true."

    k "You treated me like a case study. And when I called you on it, you said I was 'projecting.'"

    s "I was twenty."

    k "You're still twenty."

    s_thoughts "The coffee is getting cold."

    s_thoughts "Katie is looking at me with the look. The one that sees through the jacket and the metaphors and the observation instinct to the thing underneath."

    s_thoughts "The thing underneath is: she's right."

    s_thoughts "Not about all of it. But about enough."

    k "Remember the night we broke up?"

    s_thoughts "I flinch."

    k "You cried in a Denny's parking lot at 2 AM because I told you I couldn't be your thesis anymore. And then you went home and you journaled about it. You JOURNALED about your breakup. In real time."

    s "I process through writing."

    k "You process through translating. There's a difference."

    s_thoughts "I stare at her."

    s_thoughts "She stares back."

    k "Is this girl -- Amara -- is she going to end up in a Denny's parking lot? Or are you?"

    s_thoughts "I open my mouth."

    ## === DEFENDER SPLIT ===

    if sophia_fire >= 2:
        jump amara_ch6_katie_lila
    else:
        jump amara_ch6_katie_amara

## ===========================
## KATIE SCENE: LILA DEFENDS (fire >= 2)
## Fire defending fire. Loud. Direct.
## Probably funny AND devastating.
## ===========================

label amara_ch6_katie_lila:

    s_thoughts "The door downstairs bangs open."

    s_thoughts "Footsteps on the stairs. Fast. Two at a time."

    show ex neutral at right with move
    show lila neutral at left with dissolve

    l "THERE you are."

    s "Lila?"

    l "I texted you four times. You didn't answer. I tracked your location because you NEVER turned off the sharing thing and I-- oh."

    s_thoughts "She sees Katie."

    s_thoughts "Katie sees her."

    s_thoughts "The room temperature drops about fifteen degrees."
    
    show lila pissed at left

    l "You're Katie."

    k "And you're the loud one."

    l "I prefer 'forthright.' Or 'vibrant.' 'Loud' is reductive."

    s_thoughts "She pulls up a chair. Doesn't ask. Sits."

    l "Why are you talking to my friend?"

    k "We were having a conversation."

    l "About what?"

    s "Lila, it's fine--"

    l "It's clearly not fine."

    show ex annoyed at right

    k "I was telling Sophia that she's doing the same thing she did with me."

    l "What thing?"

    k "Find someone interesting. Burn everything else down. Cry in a parking lot."

    l "Okay, first of all, the Denny's thing was ONE TIME--"

    k "You know about the Denny's thing?"

    l "Of course I know about the Denny's thing. I'm her best friend."

    s "Lila, you don't have to--"

    l "I'm talking."

    s_thoughts "She turns to Katie. Full Lila broadcast. No warmth in it."

    show lila pissed at left

    l "You broke up with her in a Denny's parking lot. At 2 AM. After a GRAND SLAM. Who does that? Who eats a Grand Slam and then dumps someone?"

    k "That's not what--"

    l "And then you told her she was 'too much.' That she 'observed too hard.' That she turned you into a 'project.' And now you're here -- months later -- in a COFFEE SHOP -- doing the exact same thing to her."

    k "I'm not--"

    l "You are! You're sitting here telling her she's a pattern. You're reducing her to a pattern. THAT'S the thing you do. Not her thing. YOURS."

    show ex annoyed at right

    k "That's not--"

    l "She is not burning anything. She's CHOOSING."

    s_thoughts "The coffee shop goes quiet. The person at the other table looks up."

    l "There's a difference. You never let her choose."

    show ex neutral at right

    s_thoughts "Katie's jaw tightens."

    k "You don't know what our relationship was like."

    l "I know what she was like after."

    s_thoughts "Lila's voice drops. Not quiet -- Lila can't do quiet. But lower. Serious."

    show lila sad at left

    l "I know she cried so hard after she threw up. I know she didn't leave her dorm for four days. I know she changed her major."

    l "I know all of that. Because I'm her best fucking friend."

    k "I'm sorry she--"

    l "I'm not done."

    s_thoughts "Katie closes her mouth."

    l "You're right that she finds people interesting. You're right that she goes deep. You're right that it can be a lot."

    s_thoughts "She looks at me."

    show lila happy at left

    l "But you're wrong about the burning."

    l "She's not burning anything. She's been in that house for months and she's TRYING."

    l "And Amara -- Amara isn't a case study. Amara is the first person I've seen Sophia shut up around. Like, actually shut up. Actually be still."

    l "Do you know how hard that is for her? To be still?"

    s_thoughts "I didn't know Lila saw that."

    show lila pissed at left

    l "She's not doing the thing she did with you. She's doing something new. And it's messy and it's costing her and she might be terrible at it. But it's NEW."

    l "You don't get to walk in here and tell her it's the same pattern. Because you stopped watching."

    show ex annoyed at right

    k "I stopped watching because watching is what she does to people."

    l "No. You stopped watching because you got hurt and you decided the girl who hurt you is the only version that exists."

    s_thoughts "The coffee shop is very quiet."

    s_thoughts "I'm staring at Lila."

    s_thoughts "She's not looking at me. She's looking at Katie."

    s_thoughts "Her eyes are bright. Not with tears -- with conviction."

    show ex neutral at right

    k "You're in love with her."

    s_thoughts "The room stops."

    show lila shocked at left

    l "What?"

    k "You're in love with Sophia. I can see it. The way you talk about her."

    l "That's-- I'm her FRIEND."

    k "Friends don't track each other's locations and storm coffee shops."

    s_thoughts "Lila's face does something I've never seen. A flicker. Raw. Then the switch flips and she's back."

    show lila pissed at left

    l "This isn't about me."

    k "It's a little about you."

    l "It's NOT about me. It's about you coming here and trying to put Sophia back in the box she climbed out of."

    s_thoughts "Katie looks at Lila."

    s_thoughts "Katie looks at me."

    show ex neutral at right

    k "She's going to hurt you too. You know that, right?"

    s_thoughts "She says it to Lila. Not cruel. Almost gentle."

    show lila happy at left

    l "Maybe. That's my problem. Not yours."

    s_thoughts "A beat."

    s_thoughts "Katie picks up her coffee. Cold by now."

    k "Fair."

    s_thoughts "She stands."

    k "Sophia."

    s "Yeah."

    k "I hope I'm wrong."

    s_thoughts "She leaves a five on the table. She walks downstairs."

    s_thoughts "The door closes."

    hide ex with dissolve

    s_thoughts "Lila and I sit."

    s_thoughts "The coffee shop slowly comes back to life. The typing resumes."

    show lila sad at left

    l "Your ex is a NIGHTMARE."

    s "She's not a nightmare. She's just--"

    l "A nightmare who's right about some things. I know. That's the worst kind."

    s_thoughts "She picks up my cold latte. Drinks it."

    l "Ugh. Oat milk?"

    s "I'm trying something new."

    l "Try harder, babe."

    s_thoughts "She puts the cup down."

    l "She's wrong about you, you know."

    s "Is she?"

    show lila happy at left

    l "She's wrong because what she's saying would mean I'm a Denny's parking lot. And I am NOT a parking lot. I am at MINIMUM a rooftop with fairy lights."

    s_thoughts "I almost laugh."

    l "Also she called me 'the loud one.'"

    s "You are the loud one."

    l "That's MY word. She doesn't get to use my word."

    s_thoughts "She's deflecting."

    s_thoughts "But the real thing is still in the room."

    s_thoughts "Katie said: 'You're in love with her.'"

    s_thoughts "Lila said: 'That's my problem.'"

    s_thoughts "Not 'no.' Not 'I'm not.' Just: that's my problem."

    s_thoughts "I don't look at that too closely."

    s_thoughts "Not right now."

    l "Come on. We're going to get actually good coffee somewhere else. This place is contaminated."

    s_thoughts "She stands up. Pulls me by the sleeve."

    s_thoughts "I let her."

    hide lila with dissolve

    stop music fadeout 2.0

    jump amara_ch6_scene4

## ===========================
## KATIE SCENE: AMARA DEFENDS (fire <= 1)
## Three sentences. Precision vs. performance.
## ===========================

label amara_ch6_katie_amara:

    s_thoughts "The door downstairs opens."

    s_thoughts "Not a bang. A click."

    s_thoughts "Footsteps on the stairs. Measured. Even."

    show ex neutral at right with move
    show amara neutral at left with dissolve

    s_thoughts "Amara."

    s_thoughts "She's standing at the top of the stairs. Her bag over one shoulder. The cream-covered book visible in the side pocket."

    s_thoughts "She looks at me. She looks at Katie."

    a "Sophia."

    s "Amara. What are you--"

    a "You weren't at the library. Charlotte tracked you on that app of hers."

    s_thoughts "She says it simply. She went to the library. I wasn't there. So she's here."

    s_thoughts "That's so Amara it hurts."

    show ex neutral at right

    k "You're Amara."

    a "Yes."

    k "The girl."

    a "I don't know what that means."

    k "It means you're the one Sophia is currently case-studying."

    s "Katie--"

    a "I know what she meant."

    s_thoughts "Amara pulls up a chair."

    s_thoughts "She sits the way Amara sits -- straight, deliberate, hands folded."

    a "You're Katie."

    k "She told you about me?"

    a "She told me about the Denny's."

    s_thoughts "Katie flinches. Tiny. Quick."

    k "Figures."

    a "She told me because she trusts me. Not because she was filing you."

    show ex annoyed at right

    k "You've known her for, what, a few months? I dated her for a year."

    a "Length doesn't equal depth."

    k "Excuse me?"

    a "You dated her for a year. In that year, did she ever stop performing for you?"

    s_thoughts "I go still."

    k "She wasn't performing--"

    a "She was. She performs for everyone. She observes and she performs the result."

    s_thoughts "Amara is talking about me like I'm not here."

    s_thoughts "She's right."

    a "The difference is that she's trying to stop."

    show ex neutral at right

    k "That's what she said last time too."

    a "I'm not you."

    s_thoughts "The room is very quiet."

    a "She's changing."

    k "People don't change in a few months."

    show amara neutral at left

    a "She's changing. You can't see it because you've ossified."

    s_thoughts "Katie's eyes narrow."

    a "You've ossified because you're sitting here again because you haven't let her go yet."

    s_thoughts "Katie blinks."

    show ex neutral at right

    s_thoughts "She studies Amara."

    s_thoughts "Two people who read rooms. Two different languages."

    k "She's going to hurt you."

    a "Probably."

    k "And you're okay with that?"

    a "I didn't say okay. I said probably."

    s_thoughts "A beat."

    k "You're not what I expected."

    a "I never am."

    s_thoughts "Katie picks up her coffee."

    k "Sophia."

    s "Yeah."

    k "I hope she's right. That you're different now."

    s_thoughts "She doesn't say it mean."

    s_thoughts "She says it tired."

    k "I hope I'm wrong."

    s_thoughts "She leaves a five on the table."

    s_thoughts "She walks downstairs."

    s_thoughts "The door closes."

    hide ex with dissolve

    s_thoughts "Amara and I sit."

    s_thoughts "The coffee shop comes back. Typing. The espresso machine."

    s_thoughts "She picks up the menu. Looks at it. Puts it down."

    a "She's not wrong about everything."

    s "I know."

    a "The pattern is real."

    s "I know."

    a "But a pattern you can see is a pattern you can change."

    s "Can I?"

    show amara neutral at left
    
    a "She doesn't see what she's doing to you. When she showed up at the beginning of the semester. Or now."

    a "She can't change. You can. That's the difference."

    s_thoughts "I look at my cold latte."

    s "Thank you."

    a "For?"

    s "Showing up."

    a "You weren't at the library."

    s "That's not an answer."

    a "It is."

    s_thoughts "She stands."

    a "Class?"

    s "Yeah."

    a "I'll walk with you."

    hide amara with dissolve

    stop music fadeout 2.0

    jump amara_ch6_scene4

    ## ===========================
    ## SCENE 4: AMARA AND SOPHIA -- POST-KATIE
    ## Conditional.
    ## fire <= 1 (Amara defended): Process together.
    ## fire >= 2 (Lila defended): Sophia tells Amara.
    ## ===========================

label amara_ch6_scene4:

    if sophia_fire >= 2:
        jump amara_ch6_post_katie_told
    else:
        jump amara_ch6_post_katie_together

label amara_ch6_post_katie_together:

    ## Amara defended. They process it together.

    scene bg porch night with Fade(1.5, 1.0, 1.5)

    play music mus_fragile fadein 3.0

    s_thoughts "Wednesday. Late."

    s_thoughts "We're on the porch. Again."
    
    show amara neutral at center with dissolve

    s_thoughts "She's in her spot. I'm in mine."

    s_thoughts "Two and a half inches."

    s_thoughts "We haven't talked about the coffee shop."

    s_thoughts "Not directly. She walked me to class after. We talked about nothing. The weather. A bird on the path."

    s_thoughts "Now it's been a day and the coffee shop is still in the room."

    a "You've been thinking about what she said."

    s "Haven't stopped."

    a "Which part?"

    s "All of it. The pattern. The burning. The Denny's parking lot."

    s_thoughts "She sips her tea."

    a "Ask me."

    s "Ask you what?"

    a "Whatever you're afraid to ask."

    s_thoughts "The porch is dark. The street lamp does the yellow thing."

    s "Am I doing the thing?"

    a "What thing?"

    s "The thing Katie said. The pattern. Am I just-- finding someone interesting and burning everything else down?"

    s_thoughts "She's quiet for a long time."

    a "Yes and no."

    s "That's not an answer."

    a "It's the honest one."

    s_thoughts "She puts her mug down."

    a "You are pulling away from the house. That's real. Isabella noticed. Charlotte noticed. I noticed."

    s "So Katie's right."

    a "Katie is right that there's a pattern. She's wrong about what it means."

    s "What does it mean?"

    a "When you case-studied Katie, you were consuming her. Making her legible. Turning her into something you could control."

    s "And with you?"

    a "With me you're trying to stop."

    s_thoughts "I wait."

    a "The pattern is there. But you fight it now. You catch yourself. You put the file down."

    s "Not always."

    a "Not always. But sometimes." 
    
    a "...Sometimes is enough."

    s "Is it?"

    a "I think so."

    s_thoughts "Her voice is different. Not the precision. Something underneath it. Something that costs her."

    a "Sophia."

    s "Yeah."

    a "Katie was right about one thing."

    s "What?"

    a "You do burn things down. But she was wrong about why."

    s "Why then?"

    a "Because you're afraid."

    s_thoughts "The girl who watches because she's afraid of people leaving."

    a "You can hold more than one thing."

    s "What if I drop something?"

    a "Then you pick it up."

    s_thoughts "Simple. Devastating."

    a "Or you don't. And it stays on the ground. And that's information too."

    s_thoughts "The porch is quiet."

    s_thoughts "I look at her."

    s "You said all of that to Katie. In the coffee shop. You defended me."

    a "I stated facts."

    s "You said I was changing. That she'd ossified."

    show amara embarrassed at center

    a "That was-- pointed."

    s "It was perfect."

    show amara neutral at center

    a "It was what I saw."

    s "Amara."

    a "Mm."

    s "You see more than you let on."

    a "Everyone does. I'm just honest about the ratio."

    s_thoughts "The half-degree."

    s_thoughts "Two inches."

    s_thoughts "I put my hand on the step between us."

    s_thoughts "She puts hers next to it."

    s_thoughts "Not touching. Just: adjacent."

    s_thoughts "The closest thing to holding hands that isn't."

    hide amara with dissolve

    stop music fadeout 3.0

    jump amara_ch6_scene5

label amara_ch6_post_katie_told:

    ## Lila defended. Sophia tells Amara about it.

    scene bg library with Fade(1.5, 1.0, 1.5)

    play music mus_amara fadein 3.0

    s_thoughts "Wednesday. The library."

    s_thoughts "We're at our table."

    show amara neutral at center with dissolve

    s_thoughts "I tell Amara about Katie."

    s_thoughts "Not all of it. The shape. 'My ex showed up. She said I'm doing the same thing I did to her. She might be right.'"

    a "What thing?"

    s "The finding someone interesting and burning everything else down thing."

    a "Mm."

    s "She said I'm case-studying you."

    a "Are you?"

    s "I don't know. Maybe. Not on purpose."

    a "That's the most honest answer you've given anyone."

    s_thoughts "I look at her."

    s "Lila was there. She defended me."

    a "How?"

    s "Loudly."

    a "That's consistent."

    s "She said I'm not burning anything. That I'm choosing."

    a "What did Katie say?"

    s "She said Lila is in love with me."

    s_thoughts "The sentence hangs in the library."

    s_thoughts "Amara's face doesn't change."

    a "Is she?"

    s "I don't know."

    a "You know."

    s_thoughts "I stare at the table."

    s "Maybe."

    a "Mm."

    s "Does that bother you?"

    a "That someone else sees what I see in you?"

    s_thoughts "My breath catches."

    a "No."
    
    s_thoughts "That's all she says."

    s_thoughts "She opens her book."

    a "Your ex sounds afraid."

    s "Afraid of what?"

    a "That you've changed. Because if you've changed, then she left someone who was capable of changing. And she has to live with that."

    s_thoughts "I sit with that."

    s "You're reading someone you've never met."

    a "You described her."

    s_thoughts "She turns a page."

    a "Sophia."

    s "Yeah."

    a "She's not wrong about the case-studying."

    s "I know."

    a "But a pattern isn't a destiny."

    s "How do you know?"

    a "Because I had a pattern too. Quiet girl stays quiet. Watches. Doesn't reach."

    a "I'm reaching."

    s_thoughts "She says it to the book."

    s_thoughts "Like it's a fact about polymer viscosity."

    show amara embarrassed at center
    
    s_thoughts "But her ears are pink."

    s_thoughts "And her hand is on the table. Not palm up. Just there. Between the books."

    s_thoughts "An invitation she'd deny if I named it."

    show amara neutral at center

    s_thoughts "I put my hand next to hers."

    s_thoughts "Not touching."

    s_thoughts "The library is quiet."

    s_thoughts "We read."

    hide amara with dissolve

    stop music fadeout 3.0

    jump amara_ch6_scene5

    ## ===========================
    ## SCENE 5: LILA SCENE -- POST-KATIE
    ## Conditional.
    ## fire >= 2 (Lila defended): Debrief. She's fired up.
    ## ch4_chose_lila == TRUE (Lila didn't defend ): Lila is supportive.
    ## fire <= 1 (Lila didn't defend): Sophia reaches out.
    ## ===========================

label amara_ch6_scene5:

    if sophia_fire >= 2:
        jump amara_ch6_lila_debrief
    elif ch4_chose_lila == True:
        jump amara_ch6_lila_close
    else:
        jump amara_ch6_lila_reach

label amara_ch6_lila_debrief:

    ## Lila defended. They debrief.

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 2.0

    s_thoughts "Thursday."

    show lila happy at center with dissolve

    l "Okay so I've been thinking about your ex for forty-eight hours straight."

    s "That's concerning."

    l "Not like THAT. Like an ANALYSIS. I've been analyzing her."

    s "You've been case-studying my ex."

    l "Don't use that word. That's HER word. I've been 'processing.'"

    s "Okay. Process."

    l "She's scared."

    s "Katie's not scared of anything."

    l "She's scared of you being different. Because if you're different then she gave up on someone who was capable of growing."

    s_thoughts "That's what Amara said."

    s_thoughts "Almost word for word."

    s "You sound like Amara."

    show lila annoyed at center

    l "Take that back."

    s "You do. She said the same thing."

    l "I said it LOUDER and with BETTER delivery."

    s "Fair."

    show lila happy at center

    l "Also she called me 'the loud one.' I'm still not over it."

    s "You are loud."

    l "I'm RESONANT. There's a difference."

    s_thoughts "She stretches her legs out on the bench."

    s_thoughts "Her shoulder finds mine. Natural. Like magnets."

    l "Hey."

    s "Hey."

    l "The thing she said. About me."

    s_thoughts "My stomach tightens."

    s "What thing?"

    l "You know what thing."

    s_thoughts "A beat."

    l "She said I'm in love with you."

    s "She says a lot of things."

    show lila sad at center

    l "Yeah."

    s_thoughts "She looks at the quad. The trees. The guy with the bad guitar."

    l "She's not wrong about everything."

    s_thoughts "My heart does something complicated. Multiple load-bearing walls shifting simultaneously."

    s "Lila..."

    l "Don't."

    s "Don't what?"

    l "Don't do the gentle letdown. Don't do the 'you're my best friend' speech. Don't do the Katie thing where you observe what I'm feeling and translate it into something manageable."

    s_thoughts "She looks at me."

    show lila happy at center

    l "I'm not Katie. I'm not asking you to choose me. I'm just telling you that whatever I feel, it's mine. And I'm handling it."

    s "Are you?"

    l "I'm handling it by being your friend. Your AMAZING friend. Your friend who stormed a coffee shop."

    s "You did storm a coffee shop."

    l "That's the most romantic thing anyone has ever done for you and you can't even appreciate it because you're emotionally constipated."

    s_thoughts "I laugh."

    s_thoughts "She laughs."

    s_thoughts "The bench shakes."

    l "Friday. Bar on Seventh. No exes allowed."

    s "Deal."

    l "And bring the jacket."

    s "I always bring the jacket."

    l "The jacket makes me feel safe."

    s_thoughts "She says it fast. Throws it away."

    s_thoughts "It lands anyway."

    hide lila with dissolve

    stop music fadeout 2.0

    jump amara_ch6_scene6
    
label amara_ch6_lila_close:

    ## Lila didn't defend but Sophia chose Lila in Chapter 4.
    
    scene bg campus with Fade(0.8, 0.3, 0.8)
    
    play music mus_campus fadein 2.0
    
    show lila happy at center with dissolve
    
    l "YOU'RE KIDDING ME. SHE SHOWED UP? AGAIN?"
    
    s_thoughts "She's doing the thing where she speaks in all caps."
    
    s "Yeah. She did."
    
    l "And armchair girl -- Amara -- she showed up to defend you?"
    
    s "Yep."
    
    l "That's romantic as hell."
    
    s_thoughts "I blush."
    
    s "It wasn't--"
    
    l "Babe."
    
    l "If someone did that for me I'd be in their bed within the hour."
    
    s "LILA."
    
    l "What? It's true."
    
    s_thoughts "She's being funny, but there's a twinge of something in her voice. Something I can't quite pin down."
    
    s "She wasn't entirely wrong."
    
    l "Katie?"
    
    s "Yeah."
    
    l "Maybe not."
    
    l "But."
    
    s "But?"
    
    show lila annoyed at center
    
    l "It was an asshole thing to confront you about it AGAIN."
    
    l "Why do you think she did that?"
    
    s "I don't know. Because she's Katie?"
    
    l "Because she's SCARED."
    
    s_thoughts "That catches my attention."
    
    s "Scared of what?"
    
    show lila neutral at center
    
    l "You. Changing."
    
    s "..."
    
    l "She broke up with the girl who was case-studying her. And it's true. You were case-studying her."
    
    l "And she got what she wanted. You yakked in a Denny's parking lot at 2 in the morning."
    
    s "Thanks for the reminder."
    
    l "But now she's hearing about you with another girl. With Amara."
    
    l "And she's trying to see if you're really changing."
    
    l "Because if you are... then she broke up with someone capable of change."
    
    s "That's almost word-for-word what Amara said."
    
    show lila laugh at center
    
    l "Yeah but I said it in a TOTALLY more sharp way with more impact."
    
    s "Mm."
    
    s_thoughts "I'm picking up some of Amara's tics."
    
    show lila neutral at center
    
    l "Listen, Sophia."
    
    s "Listening."
    
    show lila sad at center
    
    l "I... You..."
    
    s_thoughts "She hesitates."
    
    l "You really like this girl?"
    
    s "Amara? Yeah. I really do."
    
    s_thoughts "Lila is quiet for an unusual amount of moments for Lila."
    
    pause 1.5
    
    show lila happy at center
    
    pause 1.0
    
    l "Then change for her. Show her you're not the same girl you were with Katie."
    
    l "They say that's the best kind of revenge, you know."
    
    s "Right."
    
    s_thoughts "I feel better. Lila has a way of doing that."
    
    s "Thanks, Lila. Friday?"
    
    l "Friday."
    
    s_thoughts "She smiles. But it's not the usual Lila smile. There's something else to it this time."
    
    s_thoughts "She told me to change."
    
    s_thoughts "So I don't file it."
    
    stop music fadeout 2.0
    
    jump amara_ch6_scene6

label amara_ch6_lila_reach:

    ## Lila didn't defend. Sophia reaches out.

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_fragile fadein 2.0

    s_thoughts "Thursday."

    s_thoughts "I text Lila."

    s_thoughts "'Can we talk? Like actually talk. Not ramen talk.'"

    s_thoughts "The response takes an hour."

    s_thoughts "Lila: 'bench at 3?'"

    s_thoughts "I'm there at 2:45."

    s_thoughts "She gets there at 3:10."

    show lila happy at center with dissolve

    l "Hey."

    s "Hey."

    s_thoughts "She sits. Distance. The bench has room for two and she's at her end and I'm at mine."

    s_thoughts "She used to sit in the middle. She used to eliminate the gap."

    l "What's up?"

    s "Katie showed up."

    show lila shocked at center

    l "WHAT?"

    s "On campus. Monday. We had coffee."

    l "You had COFFEE with your EX? Sophia!"

    s "She was visiting a friend."

    l "That's what exes ALWAYS say. 'I was just in the area.' NOBODY is just in the area."

    s_thoughts "She's animated. More than she's been in weeks."

    l "What did she say?"

    s "She said I'm doing the same pattern. Finding someone interesting, burning everything else down."

    show lila annoyed at center

    l "That's--"

    s_thoughts "She stops."

    l "Is she right?"

    s "I don't know. Maybe."

    l "Maybe about Amara?"

    s "Maybe about everything. The house. You."

    show lila sad at center

    l "Me."

    s "I haven't been a good friend."

    l "No."

    s_thoughts "She says it simply. No softening."

    s "I'm sorry."

    l "I know."

    s "I mean it."

    l "I know you mean it. That's the problem. You always mean it. And then you disappear again."

    s_thoughts "That hits."

    s_thoughts "Because it's true."

    l "I'm not mad at you, Sophia. I'm-- I'm tired of being the person you come back to when you remember you have a best friend."

    s "Lila--"

    l "I'm not done."

    s_thoughts "I close my mouth."

    l "I got into peer counseling. I missed a session and almost got kicked out. I've been going out too much. Amy is fun but she's not-- she's not YOU."

    l "And you've been in the library. Or on the porch. Or wherever Amara is. And that's okay. It's OKAY to fall for someone."

    l "But you could have texted."

    s "I know."

    l "A TEXT, Sophia. Not a novel. Not an apology essay. Just 'hey, how's it going, I remember you exist.'"

    s "You're right."

    show lila annoyed at center

    l "Of COURSE I'm right. I'm always right. It's my curse."

    s_thoughts "A ghost of the old Lila. The volume returning."

    s "Katie said she heard about me from you. Through Amy."

    l "I talk. It's what I do."

    s "What did you say?"

    show lila sad at center

    l "That you were happy. That you'd found someone. That I was worried about you."

    s "Worried?"

    l "You disappeared, Sophia. You disappeared and I didn't know if it was because of Amara or because of the thing you do where you get so deep inside your own head that you forget other people live there too."

    s_thoughts "I reach across the bench."

    s_thoughts "I put my hand on hers."

    s_thoughts "She looks at our hands."

    show lila happy at center

    l "This doesn't fix it."

    s "I know."

    l "But it's a start."

    s "Friday? Bar on Seventh?"

    l "...Maybe. Let me check my schedule."

    s "Since when do you have a schedule?"

    l "Since I became a person with BOUNDARIES. Dr. Reeves would be proud."

    s_thoughts "She squeezes my hand."

    s_thoughts "She lets go."

    l "Text me tomorrow. I'll decide then."

    s "Okay."

    l "And Sophia?"

    s "Yeah?"

    l "If your ex shows up again, call me. I'll destroy her."

    s "Emotionally or physically?"

    l "Yes."

    s_thoughts "There she is."

    s_thoughts "The Lila underneath the distance."

    s_thoughts "She's still there."

    s_thoughts "I almost lost her."

    hide lila with dissolve

    stop music fadeout 2.0

    jump amara_ch6_scene6

    ## ===========================
    ## SCENE 6: NOVA'S CLASS -- FINAL FOR CH5
    ## Translation and identity.
    ## "The translator who translates herself discovers
    ##  she was never writing in one language."
    ## Post-Katie. Sophia hearing Nova differently.
    ## ===========================

label amara_ch6_scene6:

    scene bg classroom with Fade(0.8, 0.3, 0.8)

    play music mus_nova fadein 2.0

    s_thoughts "Friday. Last class of the week."

    s_thoughts "Nova."

    show professor neutral at center with dissolve

    nova "We've been talking about loyalty and direction. Today I want to talk about the translator herself."

    s_thoughts "I sit in the third row. Same seat."

    s_thoughts "I'm carrying everything from the past couple days into this classroom."

    nova "When a translator works on a text long enough, something happens. The text begins to change her."

    nova "She starts in her own language. Confident. She knows who she is. She brings her sensibility, her rhythm, her understanding to the source material."

    nova "But the source material pushes back. It has its own rhythms. Its own logic. Its own silences."

    show professor happy at center

    nova "And if she's honest -- if she's truly faithful to the work -- she begins to change."

    nova "Her sentences get shorter. Or longer. Her rhythm adapts. She starts dreaming in the other language."

    s_thoughts "I write: 'dreaming in the other language.'"

    show professor neutral at center

    nova "The question becomes: when the translator has been changed by the text -- when she writes in a rhythm that isn't hers anymore, in a voice that's been shaped by years of carrying someone else's words -- whose voice is it?"

    s_thoughts "The Nova-quiet."

    nova "Is she still herself? Or has the translation translated her?"

    s_thoughts "I think about Amara's silence. How I've gotten quieter. How the sentences in my head are shorter now. More precise."

    s_thoughts "I think about Lila's volume. How we sang karaoke together. How she always knows what to say."

    s_thoughts "Two translations. Two frequencies."
    
    s_thoughts "Two Sophias."

    nova "The translator who translates herself discovers something unsettling."

    nova "She was never writing in one language."

    s_thoughts "I don't write that down."

    s_thoughts "I just let it sink in."

    nova "She was always bilingual. She just didn't know the second language was running underneath."

    s_thoughts "Nova looks at the room."

    show professor happy at center

    nova "Your final reflection for this unit. Not an essay. Just a question."

    nova "Write the question you're afraid to ask yourself."

    nova "Not the answer. Just the question."

    s_thoughts "I stare at my notebook."

    s_thoughts "The question I'm afraid to ask myself."

    s_thoughts "My pen moves."

    s_thoughts "'Am I changing?'"

    s_thoughts "I stare at it."

    s_thoughts "I cross it out."

    s_thoughts "I write: 'Am I just translating myself into someone Amara can love?'"

    s_thoughts "I stare at that."

    s_thoughts "I cross it out."

    s_thoughts "I write: 'What if I can't tell the difference?'"

    s_thoughts "I don't cross it out."

    hide professor with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 7
    ## Three variants based on sophia_fire.
    ## fire=0: The library. Two inches. Beautiful and costly.
    ## fire=1: The entry. Between two doors.
    ## fire=2: Charlotte's muffin. Lila's text. Too many people.
    ## Each foreshadows Ch6 without determining it.
    ## ===========================

    if sophia_fire == 0:
        jump amara_ch6_still
    elif sophia_fire == 1:
        jump amara_ch6_middle
    else:
        jump amara_ch6_fire

## ===========================
## Scene 7A: STILLNESS (fire=0)
## The library. Amara and Sophia. Two inches.
## The house is quiet behind them.
## Beautiful and costly.
## ===========================

label amara_ch6_still:

    scene bg library with Fade(1.0, 0.5, 1.0)

    play music mus_amara fadein 3.0

    s_thoughts "Friday evening."

    s_thoughts "The table."

    show amara neutral at center with dissolve

    s_thoughts "The library is almost empty. The good light is gone -- replaced by the fluorescents that make everything clinical."

    s_thoughts "We don't need the good light."

    s_thoughts "Books closed. Bags on the floor. Amara has her mug -- she brings her own now. A thermos. Tea."

    s_thoughts "I have a cold latte from the café downstairs."

    s_thoughts "We're sitting next to each other. Same side of the table. This started two weeks ago. She moved her chair and I didn't mention it and now this is where we sit."

    s_thoughts "Two inches."

    s_thoughts "Our elbows touch."

    s_thoughts "The fluorescents hum."

    a "Your ex."

    s "What about her?"

    a "She said the pattern ends in a parking lot."

    s "She did."

    a "This doesn't end in a parking lot."

    s "How do you know?"

    a "Because I don't eat at Denny's."

    s_thoughts "I stare at her."

    s_thoughts "She's not smiling."

    s_thoughts "But the half-degree is there."

    s_thoughts "I laugh. The quiet kind. The library kind."

    a "Sophia."

    s "Yeah."

    a "I'm glad you're here."

    s "I'm always here."

    a "I know. That's what I'm glad about."

    s_thoughts "Two inches."

    s_thoughts "The library closes in an hour."

    s_thoughts "My phone is in my bag. I haven't checked it in three hours. There might be texts. There might be Charlotte asking about dinner. There might be Lila. There might be silence."

    s_thoughts "I don't check."

    s_thoughts "The house must be quiet. Somewhere in it, Charlotte is setting places. Isabella is typing. Eve's door is closed."

    s_thoughts "The house is a place I live."

    s_thoughts "The library is a place I am."

    s_thoughts "There's a difference."

    s_thoughts "The difference is two inches and a girl who reads slower to wait for me."

    s_thoughts "I lean my head against the wall."

    s_thoughts "She turns a page of the book she's not reading."

    s_thoughts "We stay until the librarian kicks us out."

    pause 2.0

    s_thoughts "Beautiful."

    s_thoughts "And the empty chairs at home don't make a sound."

    hide amara with dissolve

    stop music fadeout 4.0

    jump amara_ch6_confrontation

## ===========================
## Scene 7B: BETWEEN (fire=1)
## The entry. Sophia between two doors.
## Not sure which way she's walking.
## ===========================

label amara_ch6_middle:

    scene bg entry night with Fade(1.0, 0.5, 1.0)

    play music mus_fragile fadein 3.0

    s_thoughts "Friday night."

    s_thoughts "I'm standing in the entry."

    s_thoughts "The house is dark."

    s_thoughts "I came in from the campus. From Lila. From the bench and the conversation."

    s_thoughts "The kitchen is to my left. Charlotte's domain. The light is off but I can see the counter -- muffins under foil, labeled. The chore chart on the fridge. The mugs lined up. A house that someone holds together with her fingernails."

    s_thoughts "Amara's room is down the hall. Her door is closed. No light under the crack. She's asleep or she's reading in the dark or she's lying there listening for me to come home."

    s_thoughts "I'm in the entry."

    s_thoughts "Between the kitchen and her room."

    s_thoughts "Not sure which way I'm walking."

    s_thoughts "My phone buzzes."

    s_thoughts "Lila: 'good talk today. friday bar? yes/no. final answer.'"

    s_thoughts "I type: 'Yes.'"

    s_thoughts "She responds immediately: 'YES. ok goodnight don't dream about your ex'"

    s_thoughts "I almost smile."

    s_thoughts "I put my phone away."

    s_thoughts "The entry is dark."

    s_thoughts "Two directions."

    s_thoughts "The girl who makes the muffins. The girl who waits in the quiet."

    s_thoughts "And somewhere off campus, the girl who stormed a coffee shop."

    s_thoughts "Three frequencies."

    s_thoughts "The dial could tune to any of them."

    s_thoughts "I stand in the dark and I don't move."

    pause 2.0

    s_thoughts "'What if I can't tell the difference?'"

    s_thoughts "Two frequencies."

    s_thoughts "I go upstairs."

    s_thoughts "Not toward the kitchen. Not toward Amara's room."

    s_thoughts "My room."

    s_thoughts "The one door that's mine."

    s_thoughts "I close it."

    s_thoughts "Through the wall -- silence."

    s_thoughts "Through the floor -- silence."

    s_thoughts "The house is sleeping."

    s_thoughts "I'm awake."

    stop music fadeout 4.0

    jump amara_ch6_confrontation

## ===========================
## Scene 7C: FIRE (fire=2)
## Charlotte's muffin. Lila's text.
## The fixer with too many people to fix.
## Amara's distance growing.
## ===========================

label amara_ch6_fire:

    scene bg kitchen night with Fade(1.0, 0.5, 1.0)

    play music mus_wrong fadein 3.0

    s_thoughts "Friday. Late."

    s_thoughts "I'm in the kitchen."

    s_thoughts "I came down for water. That's what I told myself. Water. A basic need. Nothing complicated."

    s_thoughts "But I'm sitting at the table."

    s_thoughts "Charlotte's muffin is on the counter. The one she made me. No label."

    s_thoughts "I didn't eat it."

    s_thoughts "It's been sitting there and I didn't eat it because eating it feels like accepting something I don't have room for."

    s_thoughts "'I know you like Amara. Of course you do.'"

    s_thoughts "'And I'm just-- Charlotte. Just the girl who makes the muffins.'"

    s_thoughts "She confessed to me. And I stayed. And I hugged her. And the muffin is sitting there like a love letter I can't return."

    s_thoughts "My phone is on the table."

    s_thoughts "Lila's last text: 'hey are we good? like ACTUALLY good? because i need to know'"

    s_thoughts "I haven't responded."

    s_thoughts "The jacket comment. The rooftop. The fairy lights. Her hand in mine."

    s_thoughts "Katie said: 'You're in love with her.'"

    s_thoughts "Lila said: 'That's my problem.'"

    s_thoughts "That's a lot of people's problems that are sitting in my kitchen at midnight."

    s_thoughts "I look at the table."

    s_thoughts "Charlotte's muffin."

    s_thoughts "Lila's text."

    s_thoughts "And somewhere in the house, Amara is sleeping. Or reading. Or lying in the dark wondering why the four inches became six."

    s_thoughts "Six inches."

    s_thoughts "We were at two. After the library. After I told her about why I observe. After the palm-up hand."

    s_thoughts "Now it's six."

    s_thoughts "Katie said: 'You find someone interesting and you burn everything else down.'"

    s_thoughts "She was wrong."

    s_thoughts "I found someone interesting and I burned everything TOWARD her. Everyone loves the fire. Charlotte fell for the fixer. Lila fell for the spark. Even Katie fell for the intensity."

    s_thoughts "Amara fell for the stillness."

    s_thoughts "And the stillness is the thing I keep failing to give her."

    s_thoughts "I pick up the muffin."

    s_thoughts "I take a bite."

    s_thoughts "Perfect. Of course it's perfect."

    s_thoughts "My phone buzzes."

    s_thoughts "Lila: 'ok going to bed. text me tomorrow. or don't. whatever. (text me)'"

    s_thoughts "I almost smile."

    s_thoughts "I eat the muffin in the dark kitchen."

    s_thoughts "Charlotte's muffin. Lila's text. Amara's silence."

    s_thoughts "Three people. Two hands."

    s_thoughts "The question I'm afraid to ask myself."

    s_thoughts "'What if I can't tell the difference?'"

    s_thoughts "I finish the muffin."

    s_thoughts "I don't text Lila back."

    s_thoughts "Amara's door is closed."

    s_thoughts "No clarinet."

    s_thoughts "No light."

    s_thoughts "Six inches."

    s_thoughts "Growing."

    stop music fadeout 4.0

    jump amara_ch6_confrontation

## ===========================
## THE CONFRONTATION
## Two frequencies. One room. The identity choice.
## ===========================

label amara_ch6_confrontation:

    stop music fadeout 3.0
    
    scene bg nightwalk with Fade(1.5, 1.0, 1.5)

    s_thoughts "Saturday. Late."

    s_thoughts "Lila and I went to the bar on Seventh. The one with the bad neon sign and the bartender who calls everyone 'sweetheart' regardless of gender."

    s_thoughts "I'm not drunk. I'm not sober. I'm in the zone where everything is a little louder and my jacket smells like someone else's cigarette smoke and the walk home was cold enough to almost clear my head."

    s_thoughts "Almost."

    s_thoughts "Lila is behind me. She's humming. Something she heard at the bar. She's still got the energy -- Lila always has the energy."

    s_thoughts "I open the front door."

    scene bg livingroom night with dissolve

    s_thoughts "The living room."

    s_thoughts "One lamp on. The one Charlotte leaves on when people are still out. The warm one."

    show amara neutral at right with dissolve

    s_thoughts "Amara is in the armchair."

    s_thoughts "She's reading. The cream-covered book. The one she's been reading for three weeks because sometimes she reads slowly on purpose."

    s_thoughts "She doesn't look up."

    s_thoughts "The room is quiet."

    s_thoughts "And then Lila walks in behind me."

    show lila happy at left with dissolve

    l "OKAY so the guy at the bar? With the mustache? He tried to give me his NUMBER and I was like--"

    s_thoughts "She stops."

    s_thoughts "She sees Amara."

    s_thoughts "Amara looks up."

    s_thoughts "Two people who have been orbiting the same girl from opposite directions, and the orbits just crossed."

    play music mus_threshold fadein 2.0

    pause 1.5

    show lila neutral at left

    l "Hey."

    a "Hey."

    s_thoughts "That's it. Two 'hey's. Same word. Different temperatures."

    s_thoughts "Lila's was the kind that fills a room. Amara's was the kind that notices you walked into one."

    l "Didn't know you were still up."

    a "I read late."

    l "Right. The reading."

    s_thoughts "Lila drops onto the couch. Her shoulder finds the armrest. She's casual about it. Deliberately casual."

    s_thoughts "Amara goes back to her book."

    s_thoughts "I'm standing in the middle."

    s_thoughts "Between the couch and the armchair."

    s_thoughts "Between."

    l "We had fun tonight, right, Soph?"

    s "Yeah. It was good."

    l "It WAS good. It was great. The bartender remembered our order. That means we're regulars. We're ESTABLISHING a presence."

    s_thoughts "She's performing. The volume is higher than it needs to be. She's filling the room because someone else in the room is empty."

    s_thoughts "Amara turns a page."

    l "You should come sometime, Amara."

    a "I don't drink."

    l "They have, like, soda. And one of those sad little mocktail menus."

    a "I'm okay."

    l "Right."

    s_thoughts "A beat."

    s_thoughts "The house is very quiet."

    s_thoughts "Lila looks at me. Looks at Amara. Looks at the space between the couch and the armchair."

    s_thoughts "Something shifts in her face."

    ## === CONDITIONAL CONFRONTATION ===

    if sophia_fire == 0:
        jump amara_ch6_confront_still
    elif sophia_fire == 1:
        jump amara_ch6_confront_between
    else:
        jump amara_ch6_confront_fire

## ===========================
## CONFRONTATION: fire=0
## Lila is hurt and reaching. She's been losing Sophia.
## "You're disappearing."
## ===========================

label amara_ch6_confront_still:

    show lila sad at left

    l "Can we talk?"

    s "We're talking."

    l "Not bar talk. Real talk."

    s_thoughts "Amara's page stays unturned."

    s "Okay."

    l "When was the last time we hung out? Before tonight."

    s "We had lunch last--"

    l "Before tonight, Sophia."

    s_thoughts "I think."

    s_thoughts "I can't remember."

    l "See? You can't even remember."

    s "I've been busy."

    l "You've been at the library."

    s_thoughts "She says 'the library' the way someone says 'the other woman.'"

    show lila pissed at left

    l "I text you and you respond three hours later. I invite you to stuff and you say 'maybe' and then you don't show. I showed up at your HOUSE last week and Charlotte said you were out and I knew exactly where you were because you're ALWAYS there."

    s "Lila--"

    l "You're disappearing."

    s_thoughts "The word sits in the room."

    l "You're disappearing and I can see it happening and I can't -- I don't know how to grab you because you're not leaving, you're just... getting quieter."

    show lila sad at left

    l "And I don't know how to fight quiet."

    s_thoughts "My chest hurts."

    s_thoughts "She's right."

    s_thoughts "I have been disappearing. Not on purpose. Not dramatically. I just -- the library was comfortable and the porch was comfortable and Amara's silence was comfortable and somewhere in the comfort I forgot that Lila was still waiting for me to come back."

    l "I'm not asking you to choose me over her. I'm not that person. I'm asking you to-- to still BE here. To still be the Sophia who does karaoke and gets wasted and says the wrong thing at the wrong time."

    l "Because THAT girl was my best friend."

    l "And I don't know who this one is."

    s_thoughts "Amara closes her book."

    s_thoughts "The sound is quiet. Final."

    show amara neutral at right

    a "She's the same person."

    show lila pissed at left

    l "I'm not talking to you."

    a "I know."

    s_thoughts "Amara stands."

    s_thoughts "She looks at me. Not at Lila. At me."

    show amara neutral at right

    a "You know where I am."

    s_thoughts "Four words."

    s_thoughts "She walks past the couch. Past Lila. Down the hall."

    s_thoughts "I hear the front door open. Not slam. Just open. And close."

    hide amara with dissolve

    show lila sad at center with move

    l "Sophia."

    s_thoughts "Her voice cracks."

    l "I'm losing you. And I don't know if you even notice."

    stop music fadeout 3.0

    pause 2.0

    jump amara_ch6_identity_choice

## ===========================
## CONFRONTATION: fire=1
## Lila is confused. Sophia's been bouncing.
## "Pick which Sophia you want to be."
## ===========================

label amara_ch6_confront_between:

    show lila annoyed at left

    l "Okay, can I say something?"

    s "When has 'can I say something' ever stopped you?"

    l "Fair. I'm saying it."

    s_thoughts "Amara turns a page. Slowly."

    l "You're confusing me."

    s "How?"

    l "One week you're at the bar with me until 2 AM singing terrible karaoke. The next week you're at the library reading in silence with--"

    s_thoughts "She gestures at Amara."

    show lila pissed at left

    l "One week you're MY Sophia. The next week you're someone I don't recognize."

    s "I'm always me."

    l "Are you? Because the Sophia I know doesn't sit on porches and say nothing for forty minutes. The Sophia I know has OPINIONS. Loud ones. Bad ones. She has opinions about opinions."

    s "People change."

    l "People change in ONE direction, Sophia. You're changing in two directions at once. That's not growth. That's-- that's--"

    s_thoughts "She's searching."

    l "Pick which Sophia you want to be."

    s_thoughts "The words land."

    s_thoughts "Not because she's wrong. Because she's asking the question I've been circling for weeks."

    show lila sad at left

    l "Because I don't know which one to wait for."

    s_thoughts "Amara closes her book."

    show amara neutral at right

    s_thoughts "She doesn't stand up fast. She stands up like she was always going to."

    a "She doesn't have to pick."

    show lila pissed at left

    l "Easy for you to say. You got the quiet version."

    a "I got whatever version she is when she's not performing."

    s_thoughts "Lila flinches."

    l "She's not PERFORMING with me."

    show amara neutral at right

    s_thoughts "Amara looks at Lila for a long time."

    a "You know where I am."

    s_thoughts "She walks past. Down the hall. The front door. Open. Close."

    hide amara with dissolve

    s_thoughts "Lila and I in the living room."

    show lila sad at center with move

    l "Is she right? Am I getting-- am I getting the performance?"

    s "Lila, no. That's not--"

    l "Because if you've been performing 'fun Sophia' for me this whole time, I need to know."

    s "I haven't been performing."

    l "Then why does it feel like I'm losing you to someone who barely talks?"

    stop music fadeout 3.0

    s_thoughts "I don't have an answer."

    pause 2.0

    jump amara_ch6_identity_choice

## ===========================
## CONFRONTATION: fire=2
## Lila is closest to Sophia here. They've been getting messy.
## "You want to be her. But you ARE me."
## ===========================

label amara_ch6_confront_fire:

    show lila happy at left

    l "That was FUN. That was the most fun I've had since-- okay wait."

    s_thoughts "She stops."

    s_thoughts "She's looking at Amara."

    s_thoughts "Amara is looking at her book."

    show lila neutral at left

    l "You know what, Sophia, can we--"

    s_thoughts "She catches herself."

    l "No. Actually. No."

    s "No what?"

    l "I'm tired of pretending."

    s "Pretending what?"

    show lila pissed at left

    l "That I don't see what's happening."

    s_thoughts "The room goes taut."

    l "You come out with me. We have fun. REAL fun. You sing too loud and you spill your drink and you're alive and you're YOU."

    l "And then you come home and you sit in that armchair--"

    s "I don't sit in the armchair."

    l "You sit NEAR the armchair. You sit in the ORBIT of the armchair. You become a different person."

    s_thoughts "Amara hasn't looked up."

    s_thoughts "But she's stopped turning pages."

    l "I watch you do it. Every time. You walk through that door and something in you goes quiet. Like you're-- tuning to a different frequency."

    s_thoughts "She steps closer."

    show lila sad at left

    l "You want to be her."

    s "I don't want to be--"

    l "The quiet. The stillness. Whatever she has that I don't have. You want it."

    l "But you ARE me, babe."

    s_thoughts "Her voice drops."

    l "You're loud and you're messy and you're too much and you say the wrong thing. That's not a phase you grew out of. That's who you are."

    l "And I love that girl."

    s_thoughts "I stare at her."

    s_thoughts "She said it."

    s_thoughts "Not 'that's my problem.' Not sideways. She said it."

    show lila sad at left

    l "I love that girl. And she's disappearing into a library and I'm standing here watching."

    s_thoughts "Amara closes her book."

    show amara neutral at right

    s_thoughts "She stands."

    s_thoughts "She looks at Lila."

    s_thoughts "For the first time tonight, Amara looks directly at Lila."

    a "She's not disappearing."

    l "Don't."

    a "She's deciding."

    l "I said DON'T."

    s_thoughts "Amara nods. Once."

    a "You know where I am."

    s_thoughts "She leaves."

    s_thoughts "Not fast. Not slow. The door opens. Closes."

    hide amara with dissolve

    s_thoughts "The room is louder without her."

    s_thoughts "That shouldn't be possible."

    show lila sad at center with move

    l "She always does that."

    s "Does what?"

    l "Leaves. Like she already knows what you're going to choose."

    s_thoughts "My throat closes."

    l "Does she? Know?"

    stop music fadeout 3.0

    s_thoughts "I don't answer."

    pause 2.0

    jump amara_ch6_identity_choice

## ===========================
## THE IDENTITY CHOICE
## The simplest menu in the game.
## The hardest choice.
## ===========================

label amara_ch6_identity_choice:

    scene bg livingroom night with Fade(0.8, 0.3, 0.8)

    stop music fadeout 0.5

    s_thoughts "Lila's on the couch."

    s_thoughts "The armchair is empty."

    s_thoughts "The front door closed softly."

    pause 2.0

    s_thoughts "Two directions."

    s_thoughts "The girl on the couch. The girl who left."

    s_thoughts "One is here. Fighting. Loud. Real."

    s_thoughts "One is gone. Trusting. Quiet."

    s_thoughts "Both are waiting."

    s_thoughts "Both are real."

    pause 3.0

    hide lila with dissolve

    menu:
        "Stay with Lila.":
            $ sophia_fire += 1
            jump amara_ch6_lila_branch
        "Go to the library.":
            jump amara_ch6_amara_branch
        "Bring Lila to the library." if amara_gh_unlocked() and (sophia_fire == 0 or sophia_fire == 2):
            jump amara_ch6_bring_lila

## ===========================
## LILA BRANCH -- ROUTING
## fire incremented. Now check totals.
## ===========================

label amara_ch6_lila_branch:

    if sophia_fire == 3:
        jump amara_ending_lila
    elif sophia_fire == 2:
        jump amara_ending_fling
    else:
        jump amara_ending_parkinglot

## ===========================
## AMARA BRANCH -- ROUTING
## fire NOT incremented. Check totals.
## ===========================

label amara_ch6_amara_branch:

    if sophia_fire == 2 and charlotte_confession == True:
        jump amara_ending_charlotte
    elif sophia_fire == 1:
        jump amara_ending_rocky
    else:
        jump amara_ending_full

## ===========================
## ENDING 1: "Babe" -- LILA (fire=3)
## Full fire. Every time. Two forest fires together.
## The thorn: the house is empty behind them.
## ===========================

label amara_ending_lila:

    scene bg livingroom night with dissolve

    show lila sad at center with dissolve

    s_thoughts "I turn to Lila."

    s_thoughts "She's still on the couch. Her eyes are bright. Not with conviction. With the kind of raw hope that makes you look like you're about to break."

    s "Lila."

    l "Yeah."

    s "I'm here."

    show lila shocked at center

    l "You're-- what?"

    s "I'm here. I'm not going to the library. I'm here."

    l "You mean tonight. You mean right now."

    s "I mean all of it."

    s_thoughts "She stares at me."

    s_thoughts "I've never seen Lila at a loss for words. She always has words. She has too many words. Words are her currency, her armor, her love language."

    s_thoughts "She has no words."

    show lila sad at center

    l "Sophia, if you're doing this because you feel sorry for me--"

    s "When have I ever felt sorry for you?"

    l "Tonight. Just now. When I said-- the thing I said."

    s "You said you love me."

    show lila embarrassed at center

    l "I said I love THAT girl. The loud one. The messy one. That's different from-- it's not the same as--"

    s "It's the same."

    l "It's NOT the same."

    s "Lila."

    l "WHAT."

    s "Shut up."

    show lila shocked at center

    pause 1.0

    s_thoughts "I sit on the couch."

    s_thoughts "Next to her."

    s_thoughts "Not the bench distance. Not the polite distance. The distance that means something."

    play music mus_campus fadein 3.0

    s "I've been trying to be someone I'm not."

    l "The quiet thing."

    s "The quiet thing. The stillness. The library. All of it."

    l "I know."

    s "And it wasn't fake. The things I felt with Amara were real."

    show lila sad at center

    l "I know that too."

    s "But I kept trying to cut out the parts of me that are loud. That are messy. That are too much. Because I thought being too much was the problem."

    l "Katie."

    s "Katie. And before Katie. And the thing with my dad where I decided that if I was just quiet enough, just observant enough, people wouldn't leave."

    l "Sophia--"

    s "And you never left. Even when I was too much. Even when I disappeared. Even when I came back smelling like bar smoke and pretending I hadn't been ghosting you."

    l "Because I'm an IDIOT."

    s "Because you love me."

    show lila embarrassed at center

    l "I already said that. Don't make me say it twice. Once was enough. Once was MORE than enough. I'm already going to replay it in my head for the next six to seven months."

    s_thoughts "I laugh."

    s_thoughts "She laughs."

    s_thoughts "It sounds like the bar and the karaoke and the bench and every other place where the two of us were just the two of us."

    s "I love you too."

    show lila shocked at center

    s_thoughts "She goes very still."

    s_thoughts "Lila. Still."

    l "Say that again."

    s "I love you."

    l "One more time."

    s "I'm not saying it three times."

    l "Please?"

    s "...I love you."

    show lila happy at center

    l "Okay. Okay. OKAY."

    s_thoughts "She's bouncing. On the couch. Actually bouncing."

    l "Oh my god. Oh my GOD."

    s "Lila."

    l "I need to text Amy. I need to tell everyone. Can I tell everyone? I'm telling everyone."

    s "It's 1 AM."

    l "I WILL STRANGLE FATHER TIME TO DEATH WITH MY BARE HANDS, BABE."

    s_thoughts "She grabs my hand."

    s_thoughts "Her hand is warm. It's always warm. Lila runs hot the way a campfire runs hot -- you can feel it from across the room."

    s_thoughts "I hold on."

    show lila happy at center

    l "I have been in love with you since the first time you cried in my dorm room about a girl whose name you wouldn't tell me."

    s "That was Katie."

    l "I KNOW it was Katie. I always knew it was Katie. You're terrible at secrets."

    s "I'm a great observer."

    l "You're a terrible observer. You've been observing the wrong things for months."

    s_thoughts "She squeezes my hand."

    show lila sad at center

    l "You know this means I'm going to be insufferable."

    s "You're already insufferable."

    l "GIRLFRIEND insufferable. That's a whole new tier."

    s_thoughts "I squeeze back."

    pause 1.5

    s_thoughts "I look at the armchair."

    s_thoughts "Amara's book is on the side table. The cream-covered one. She left it when she walked out."

    s_thoughts "She never leaves her book."

    show lila happy at center

    l "Hey."

    s "Hey."

    l "Where'd you go just now?"

    s "Nowhere."

    l "Babe."

    s_thoughts "Babe."

    s_thoughts "She said it like she's been holding it in her mouth for months."

    l "You went somewhere. Your face did the thing."

    s "What thing?"

    l "The thing where you're observing something and deciding whether to tell me."

    s "I wasn't--"

    l "Babe."

    s "Stop calling me babe."

    l "NEVER. I have been waiting to call you babe in the girlfriend way for MONTHS."

    s_thoughts "I almost laugh."

    s_thoughts "Almost."

    s_thoughts "The book is on the side table."
    
    stop music fadeout 2.0

    scene bg nightwalk with Fade(0.8, 0.3, 0.8)
    
    play music mus_shoulders fadein 2.0
    
    show lila happy at center with dissolve

    s_thoughts "Later."

    s_thoughts "We walk in the cold air."

    s_thoughts "Her hand in mine."

    s_thoughts "She's talking about everything. About the bar and the bartender and how she's going to change her relationship status and 'do people still DO that?' and she doesn't care, she's doing it."

    s_thoughts "I listen."

    s_thoughts "I'm alive."

    s_thoughts "I'm really alive."

    s_thoughts "My hand is warm. Her voice fills the street. The November air is sharp and I'm breathing it and I'm here."

    s_thoughts "I am the forest fire and the forest fire chose me back."

    s_thoughts "..."

    s_thoughts "Behind us."

    s_thoughts "The house."

    s_thoughts "Charlotte's lamp goes off."

    s_thoughts "Eve's door has been closed for three days."

    s_thoughts "Isabella is typing to Lumi."

    pause 2.0

    s_thoughts "And somewhere -- the library, the porch, her room -- a girl who left her book behind is sitting with a silence that has a different shape than before."

    s_thoughts "The clarinet plays at 2 AM."

    s_thoughts "I used to hear it through the wall."

    s_thoughts "I don't know when I stopped listening."

    stop music fadeout 4.0

    pause 2.0

    s_thoughts "Her hand is warm."

    s_thoughts "The house behind us is quiet."

    l "Babe?"

    s "Yeah?"
    
    show lila embarrassed at center

    l "This is the best night of my life."

    s "Yeah."

    s_thoughts "She's alive."

    s_thoughts "I'm alive."
    
    s_thoughts "I chose my frequency."
    
    s_thoughts "I hope Amara understands."
    
    s_thoughts "...That's silly."
    
    s_thoughts "I know she does."
    
    s_thoughts "She knew."
    
    s_thoughts "She knew the day I chose to go to Lila rather than to her room with the book."
    
    s_thoughts "...Obviously. She knew."
    
    s_thoughts "I think about that. The girl who knew me. Who KNOWS me."
    
    s_thoughts "I look at Lila."
    
    s_thoughts "I kiss her, gently, in the quiet light of the streetlamp."
    
    s_thoughts "She kisses me back."
    
    l "I love you, babe."
    
    s "I love you too."
    
    s "...Babe."
    
    s_thoughts "She smiles then goes back to kissing me."
    
    s_thoughts "This is who I am."
    
    s_thoughts "The girl she loves."
    
    s_thoughts "Thanks, Amara."
    
    s_thoughts "...For noticing."

    pause 3.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Babe{/size}"

    $ persistent.ending_amara_babe = True
    $ persistent.completed_amara_route = True
    return

## ===========================
## ENDING 2: "Muffin Girl" -- CHARLOTTE 
## Amara branch, fire=2, charlotte_confession=True
## Sophia chose the library. Amara's distance has grown.
## Amara rejects. Sophia falls to Charlotte.
## ===========================

label amara_ending_charlotte:

    scene bg livingroom night with dissolve

    show lila sad at center with dissolve

    play music mus_fragile fadein 2.0

    s_thoughts "I turn to Lila."

    s_thoughts "She's looking at me with the look. The one that's half hope and half knowing."

    s "Lila."

    l "Yeah?"

    s "I need to tell you something."

    l "Is this the part where you choose me?"

    s_thoughts "Her voice is light. She's trying to make it easy."

    s "Lila..."
    
    l "Oh no. Oh god."
    
    s "..."
    
    l "I know what that 'Lila' means."
    
    s "Lila--"
    
    l "And that one too."
    
    s_thoughts "She's crying. A lot. It's ugly crying."
    
    l "It's okay."
    
    s_thoughts "It's clearly not okay."
    
    l "Go to her."
    
    s "..."
    
    l "You know you want to."
    
    l "I'm just your bestie."
    
    l "That's all I am to you. And that's okay."
    
    l "I'm the best friend who roots for you to get with the girl."
    
    l "I'm not the girl you get with."
    
    l "That's not who I am."
    
    s_thoughts "She's saying all this through snot and tears."
    
    s "You're my best friend."
    
    l "And you're mine. And I'm in love with you and you're not in love with me because you're in love with armchair girl -- Amara -- and you have to go to her now."
    
    l "Go get with her, babe."
    
    s_thoughts "The babe hits different this time."
    
    l "I'll walk home by myself."
    
    s "Lila..."
    
    l "Go."
    
    l "I... I need to be alone."
    
    s_thoughts "Before I can say anything else, she's gone."
    
    hide lila with dissolve
    
    s_thoughts "I stand in the empty living room for a moment."
    
    s_thoughts "I just broke my best friend's heart."
    
    s_thoughts "But I had to do it."
    
    s_thoughts "I'm not in love with her."
    
    s_thoughts "My heart is with someone else."
    
    stop music fadeout 2.0
    
    scene bg library night with Fade(1.0, 0.5, 1.0)

    play music mus_amara fadein 3.0

    s_thoughts "The library."

    s_thoughts "I walked here. Through the cold. Past the campus. Past the guy with the guitar who's finally learned a second chord."

    s_thoughts "I walk up to our table."

    show amara neutral at center with dissolve

    s_thoughts "She's here."

    s_thoughts "She's always here."

    s_thoughts "She's reading."

    s_thoughts "I sit next to her."

    s_thoughts "She doesn't look up."

    pause 2.0

    s "Hey."

    a "Hey."

    s "I came."

    a "I see that."

    s "Lila... left."

    a "I know."

    s_thoughts "The library is empty. Late Saturday. The fluorescents doing their clinical thing."

    s "Amara."

    a "Mm."

    s "I chose you."

    s_thoughts "She puts her book down."

    s_thoughts "She looks at me."

    show amara neutral at center

    a "You chose the library."

    s "I chose you."

    a "You chose a building, Sophia."

    s_thoughts "That lands."

    a "You chose a building at 1 AM on a Saturday after going to a bar with the girl who loves you."

    s "I came HERE. To YOU."

    a "You came here."

    s_thoughts "She's quiet."

    a "When Lila needed you and I left you that book. What did you choose?"

    s "Lila."

    a "And when Charlotte needed you?"

    s "The house."

    a "And tonight?"

    s "You."

    a "Tonight."

    s_thoughts "The word is precise and devastating."

    a "You chose me tonight."

    s "I'm here NOW."

    a "I know."

    s_thoughts "She picks up her book."

    s_thoughts "She opens it."

    s_thoughts "The library is very quiet."

    a "Go home, Sophia."

    s "Amara--"

    a "I'm not angry. I'm just done waiting for someone who doesn't know what she wants."

    s "I want YOU."

    a "You want the idea of me. The quiet. The stillness. You want it the way you want a vacation."

    a "I'm not a vacation."

    s_thoughts "She reads."

    s_thoughts "The distance is two inches and infinite."
    
    s "Are you..."
    
    a "Rejecting you? Yes."
    
    s_thoughts "She says it like it should be obvious."
    
    s "But--"
    
    a "You don't know what you want."
    
    a "Lila was right."
    
    a "You don't know which Sophia to be."
    
    a "And that Sophia? The one who can't choose? I can't be with her."
    
    s "..."
    
    s_thoughts "I try not to cry in the middle of the library."
    
    s_thoughts "I do not succeed."
    
    s "Amara--"
    
    a "I've made up my mind."
    
    a "Goodnight, Sophia."
    
    s_thoughts "She goes back to her book. She's not cruel about it. She's just... factual."
    
    s_thoughts "I leave."

    hide amara with dissolve

    stop music fadeout 3.0

    scene bg kitchen night with Fade(1.0, 0.5, 1.0)

    s_thoughts "I'm crying in the kitchen."

    s_thoughts "2 AM."
    
    play music mus_2am fadein 3.0

    show charlotte pj neutral at center with dissolve

    s_thoughts "Charlotte is at the table. Mug. Chamomile. She can't sleep either."

    c "Sophia? What are you doing up?"

    s_thoughts "I sit across from her."

    s_thoughts "I don't say anything for a long time."

    c "You look terrible. Do you want tea?"

    s "Charlotte."

    c "I'll make tea."

    s "Charlotte."

    show charlotte pj neutral at center

    c "What?"

    s "You told me something. In your kitchen."

    show charlotte pj embarrassed at center

    c "We really don't have to--"

    s "I want to."

    c "Want to what?"

    s "Know if you meant it."

    s_thoughts "She looks at her tea."

    show charlotte pj sad at center

    c "Of course I meant it."

    s "I went to the library tonight."

    c "I know. You always go to the library."

    s "I went for Amara."

    c "I know that too."

    s "She said no."

    s_thoughts "Charlotte's face does something complicated."

    c "Oh, Sophia."

    s "And now I'm here."

    show charlotte pj neutral at center

    c "In my kitchen."

    s "In your kitchen."

    c "At 2 AM."

    s "At 2 AM."

    s_thoughts "She sips her tea."

    c "If you're here because she said no--"

    s "I'm here because you said yes."

    c "That's different?"

    s "I don't know."

    show charlotte pj sad at center

    c "Sophia, I can't be your--"

    s "I know. I know you can't be my second choice."

    c "Then what am I?"

    s_thoughts "The kitchen. 2 AM. Chamomile tea."

    s "I don't know yet. Can I figure it out?"

    c "Here? Now?"

    s "Here. Now. Tomorrow. However long it takes."

    s_thoughts "She looks at me."

    s_thoughts "Charlotte. Who says 'of course' to everything."

    s_thoughts "Who gives and gives and gives."

    s_thoughts "Who confessed to someone she knew would say no and then made muffins the next morning."

    show charlotte pj smile at center

    c "I'll make more tea."

    s "Charlotte."

    c "I'm making tea. That's not an answer. It's tea."

    s_thoughts "It's an answer."

    s_thoughts "Something starts, in her kitchen with the tea and the second choice and the tears flowing from my eyes."
    
    s_thoughts "I don't know what it is yet."
    
    s_thoughts "I think that's how it starts."

    pause 3.0

    hide charlotte with dissolve
    
    scene bg porch night with Fade(1.0, 1.0, 1.0)
    
    s_thoughts "After Charlotte goes to bed, I find myself out on the porch."
    
    s_thoughts "Sitting on our steps."
    
    s_thoughts "Alone."
    
    s_thoughts "I'm waiting for Amara to come home."
    
    s_thoughts "But I know she's not going to sit with me this time."
    
    s_thoughts "After a while, she approaches."
    
    show amara neutral at center with dissolve
    
    s "Hey."
    
    a "Hey."
    
    s_thoughts "She just... stands there. Looking at me. In the way she does."
    
    s_thoughts "Reading me like one of her books."
    
    a "Sophia."

    s "Yeah."
    
    a "You went to Charlotte tonight."
    
    s "I did."
    
    a "After I rejected you."
    
    s "You don't have to rub it in."
    
    s_thoughts "Amara sighs. It's a sad kind of sigh. One I've never heard from her before."
    
    a "You don't know what you want."

    a "You couldn't fix me." 
    
    a "So you found someone else you could fix instead."

    s_thoughts "That hits."
    
    a "Goodnight."
    
    s_thoughts "I don't respond. I'm crying."
    
    s_thoughts "She goes inside."
    
    hide amara with dissolve
    
    s_thoughts "It's freezing cold out here. Autumn is turning into winter."
    
    s_thoughts "I'm shivering. I don't go inside."
    
    s_thoughts "After a while, the door."
    
    show charlotte pj vulnerable at center with dissolve
    
    c "Sophia."
    
    s "Charlotte, I'm sorry--"
    
    c "Don't be."
    
    c "That's what you said to me."
    
    c "When I confessed."
    
    s_thoughts "She sits next to me, on Amara's step."
    
    s_thoughts "I file it."
    
    c "I brought you a blanket."
    
    s_thoughts "She wraps it around me."
    
    s_thoughts "Her fingers linger on my shoulders. Our eyes lock."
    
    s_thoughts "I need her. She needs me."
    
    s_thoughts "We need to need each other."
    
    s_thoughts "She kisses me."
    
    s_thoughts "She tastes like blueberry muffins."
    
    s_thoughts "I file that, too."

    stop music fadeout 4.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Muffin Girl{/size}"

    $ persistent.ending_amara_muffin_girl = True
    $ persistent.completed_amara_route = True
    return

## ===========================
## ENDING 3: "Two Inches" -- FLING (fire=2, no confession)
## Something happened with Amara. It wasn't enough.
## Lila sees through it. Sophia ends alone. Between.
## ===========================

label amara_ending_fling:

    scene bg livingroom night with dissolve

    show lila sad at center with dissolve

    play music mus_fragile fadein 2.0

    s_thoughts "I turn to Lila."

    l "Yeah?"

    s "I'm sorry."

    l "Sorry?"

    s "I'm sorry for all of it."

    show lila neutral at center

    l "That's not an answer. That's a blanket."

    s "For disappearing. For bouncing between you and the library and not being honest about what I was doing."

    l "What were you doing?"

    s "I don't know."

    l "You KNOW. You always know. You observe everything."

    s "Okay. I was-- I was trying to be two people. And neither one of them was honest."

    show lila sad at center

    l "Katie said the pattern ends in a parking lot."

    s "I'm not in a parking lot."

    l "You're in a living room. Same thing."

    s_thoughts "She's watching me."

    l "You came after me."

    s "I did."

    l "But you're not here."

    s "I'm right here."

    l "Your body is here. Your head is at the library."

    s_thoughts "She stands."
    
    s "How do you know?"

    show lila pissed at center

    l "Because you're sitting here with that face."
    
    s_thoughts "Lila. Reading my face. As always."

    s "What face?"

    l "The face that means you're thinking about someone else while looking at me."

    s "I'm not--"

    l "You're not choosing me, Sophia. You're running from her."

    stop music fadeout 2.0

    s_thoughts "The sentence sits in the room like a bomb that went off quietly."

    pause 2.0

    s "Lila--"

    show lila sad at center

    l "Don't."

    s_thoughts "She picks up her jacket."

    l "I'm not going to be the person you run to because stillness was too hard."

    s "That's not what this is."

    l "Then what is it?"

    s_thoughts "I don't have an answer."

    l "Yeah."

    s_thoughts "She walks to the door."

    l "Call me when you figure it out."

    s_thoughts "She doesn't slam it."

    s_thoughts "She closes it gently."

    s_thoughts "That's worse."

    hide lila with dissolve

    scene bg library with Fade(1.0, 0.5, 1.0)

    play music mus_amara fadein 3.0

    s_thoughts "Three days later."

    s_thoughts "The library."

    show amara neutral at center with dissolve

    s_thoughts "I find Amara at our table."

    s_thoughts "I sit next to her."

    s_thoughts "Our hands almost touch."

    a "You chose Lila."

    s "I stayed with Lila. I didn't choose her."

    a "What's the difference?"

    s "She told me I was running from you."

    a "Were you?"

    s_thoughts "I look at her."

    s "I don't know."

    a "Yes you do."

    s "...Maybe. A little."

    a "Mm."

    s_thoughts "She reads."

    s_thoughts "I sit."

    s_thoughts "The library light. The fluorescents."

    s "Can we talk?"

    a "We're talking."

    s "About us."

    a "Is there an us?"

    s "I want there to be."

    s_thoughts "She puts her book down."

    show amara neutral at center

    a "What happened between us was real."

    s "I know."

    a "Is real."

    s "I know."
    
    a "You stayed with Lila."

    s "I'm here now."

    a "You're here now."

    s_thoughts "She reaches across."

    s_thoughts "Her hand on mine."

    s_thoughts "Brief."

    s_thoughts "The warmth of it goes through me like a current."

    show amara neutral at center

    a "Sophia."

    s "Yeah."

    s_thoughts "She pulls her hand back."
    
    s_thoughts "The library is empty."
    
    s_thoughts "She leans forward."
    
    s_thoughts "Our lips touch."
    
    s_thoughts "It's not quite a kiss."
    
    show amara sad at center
    
    s_thoughts "I realize she's crying."
    
    s_thoughts "Our lips are touching and she's crying."
    
    s "Amara--"
    
    a "Don't."
    
    s_thoughts "She pulls back."
    
    a "I just... I needed to know what it felt like."
    
    a "What it could have been."

    s "Could've?"
    
    a "Could've."
    
    s_thoughts "That words echos in my brain."
    
    s "We still can."
    
    a "No. We can't."
    
    s "Why?"
    
    a "Because I'm not enough for you. And you're too much for me. And both of those are true at the same time."

    s "Amara--"

    a "We tried."

    s "We barely tried."

    a "We tried in the way we could."

    stop music fadeout 3.0
    
    pause 4.5
    
    show amara neutral at center

    s_thoughts "She goes back to her book."

    s_thoughts "I sit next to her."

    s_thoughts "Two inches."
    
    pause 1.5

    s_thoughts "The distance doesn't close."

    hide amara with dissolve
    
    stop music fadeout 4.0

    pause 2.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Two Inches{/size}"

    $ persistent.ending_amara_two_inches = True
    $ persistent.completed_amara_route = True
    return

## ===========================
## ENDING 4: "One Mississippi" -- ROCKY (fire=1)
## Library. Together. Real. But she wavered once.
## Trust at 90%. The 10% is the memory.
## ===========================

label amara_ending_rocky:

    scene bg library night with Fade(1.0, 0.5, 1.0)

    play music mus_amara fadein 3.0

    s_thoughts "I walked here."

    s_thoughts "Not fast. Not slow. The pace of someone who knows where they're going."

    s_thoughts "The door. The stairs. The table."

    show amara neutral at center with dissolve

    s_thoughts "She's here."

    s_thoughts "Of course she's here."

    s_thoughts "She's reading. The cream-covered book. She brought her mug -- the thermos. Tea."

    s_thoughts "She looks up."

    a "You came."

    s "I came."

    s_thoughts "I sit next to her."

    s_thoughts "Not across. Next to."

    s_thoughts "Two inches."

    s "I left Lila in the living room."

    a "I know."

    s "She was-- she was right there. Fighting for me."

    a "I know."

    s "And I came here."

    a "I know."

    s_thoughts "I look at her."

    s "Are you going to say anything besides 'I know'?"

    show amara smile at center

    s_thoughts "The half-degree."

    a "You came."

    s "Yeah."

    a "That's enough."

    show amara neutral at center

    s_thoughts "She puts her book down."

    s_thoughts "She puts her hand on the table."

    s_thoughts "Palm up."

    s_thoughts "The same gesture from weeks ago. The one that changed everything."

    s_thoughts "I put my hand in hers."

    s_thoughts "Her fingers close around mine."

    s "Amara."

    a "Mm."

    s "I like you."

    a "I know."

    s "I LIKE you. Like, properly. Not the library. Not the quiet. YOU."

    a "I know."

    s "Can you say something other than 'I know'?"

    a "I like you too."

    s_thoughts "My heart does something structural."

    a "I've liked you since you sat on the couch and pretended to read."

    s "I was reading."

    a "You pretended."

    s_thoughts "I squeeze her hand."

    s_thoughts "She squeezes back."

    s_thoughts "The library. Late Saturday. Fluorescents."

    s_thoughts "This is how it happens."

    stop music fadeout 2.0

    pause 2.0

    ## === THE WAVER ===
    
    scene bg campus night with dissolve

    play music mus_shoulders fadein 3.0

    s_thoughts "We walk home."

    s_thoughts "Her hand in mine."

    s_thoughts "The campus is dark. The leaves are everywhere."

    s_thoughts "She doesn't fill the silence. I don't fill the silence."

    s_thoughts "The silence is ours."

    scene bg porch night with dissolve

    s_thoughts "We get home."

    show amara neutral at center with dissolve

    s_thoughts "We sit. Her spot. My spot."

    s_thoughts "Zero inches."

    s_thoughts "Her shoulder against mine."

    a "Sophia."

    s "Yeah."

    a "I need to say something."

    s "Okay."

    s_thoughts "She's looking at the street."

    if ch4_chose_lila:
        a "Tonight. You chose me."
        
        a "But you chose Lila first."

        s_thoughts "That night with the book. Lila needed me and Amara left the book on my table."

        s "I did."

        a "I was waiting for you. But you went to her."

        s_thoughts "My stomach drops."

        a "That's information."

        s "Amara, I--"

        a "I'm not punishing you. I'm naming it."

        s "I might've made a mistake. I don't know."

        a "Maybe. Maybe you made a choice. Maybe it was honest. Lila needed you."

        s "But if it was the wrong choice--"

        a "There aren't wrong choices. Just choices with information attached."

    else:
        a "You chose the house."

        s_thoughts "The night Charlotte needed help and Amara's hand was palm up on the table."

        s "Charlotte was hurting."

        a "I know."

        s "I couldn't just--"

        a "You left me at the library for Charlotte."

        s_thoughts "My chest tightens."

        a "Your hand was in mine and she texted the groupchat and you left."

        s "Amara--"

        a "That's information."

        s "I came back."

        a "You came back."

        s_thoughts "She says it flat. Not forgiving. Not accusing. Measuring."

    show amara neutral at center

    a "I'm choosing you."

    s "But?"

    a "But I remember."

    s_thoughts "I hold her hand tighter."

    a "I'm not bringing it up to hurt you. I'm bringing it up because if we're doing this, I need you to know that I noticed."

    s "You notice everything."

    a "Not everything. Just the things that matter."

    s "I'm not going to waver again."

    a "Don't promise that."

    s "Why?"

    a "Because you might. And I'd rather you were honest about the possibility than certain about a lie."

    s_thoughts "Amara."

    s_thoughts "Who says the precise thing."

    s_thoughts "Who holds my hand and names the crack at the same time."

    a "Sophia."

    s "Yeah."

    a "I'm glad you came to the library."

    s "Yeah."

    a "This time."

    s_thoughts "This time."

    s_thoughts "The caveat lives in the sentence like a smudge on glass."

    s_thoughts "We sit on the porch."

    s_thoughts "Her shoulder against mine."

    s_thoughts "I think about the clarinet case."

    s_thoughts "She'll play tonight. I'll listen."
    
    s_thoughts "I think about my dad."
    
    s_thoughts "I think about the bad nights."
    
    s_thoughts "I think about counting for my sister."
    
    s_thoughts "I look at Amara. She looks at me. We kiss."
    
    s_thoughts "The breeze is cool and we kiss. She pulls back and stares at me. Directly. Like that day in the living room."

    s_thoughts "She's looking at me with an expression I can't translate."

    s_thoughts "For once, I don't try."
    
    s_thoughts "I just start counting the seconds she stays."

    pause 3.0

    hide amara with dissolve

    stop music fadeout 4.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- One Mississippi{/size}"

    $ persistent.ending_amara_one_mississippi = True
    $ persistent.completed_amara_route = True
    return

## ===========================
## ENDING 5: "Still" -- FULL (fire=0)
## All stillness. All Amara. The library is theirs.
## The most intimate ending. The loneliest.
## ===========================

label amara_ending_full:

    scene bg campus night with Fade(1.0, 0.5, 1.0)

    stop music fadeout 0.5

    s_thoughts "I know the walk by heart now. Past the campus. Past the fountain. Up the stairs. Third floor."

    s_thoughts "I don't run."

    s_thoughts "I don't rush."

    s_thoughts "I just walk."
    
    scene bg library night with dissolve

    pause 2.0

    s_thoughts "Our table."

    show amara neutral at center with dissolve

    s_thoughts "She's here."

    s_thoughts "She's always here."

    s_thoughts "She's not reading."

    s_thoughts "She's sitting with her hands around her thermos and her eyes on the window and she's not reading."

    s_thoughts "She was waiting."

    s "Hey."

    a "Hey."

    s_thoughts "I sit next to her."

    s_thoughts "Not two inches."

    s_thoughts "Zero."

    s_thoughts "My shoulder against hers."

    play music mus_amara fadein 3.0

    s_thoughts "She doesn't move away."

    pause 2.0

    s "I left Lila in the living room."

    a "I know."

    s "She was crying."

    a "I know."

    s "I left her crying and I came here."

    a "How does that feel?"

    s "Terrible."

    a "Yeah."

    s_thoughts "We sit."

    s_thoughts "The library is empty. Saturday night. Nobody comes to the library on Saturday night."

    s_thoughts "Nobody except us."

    a "You didn't hesitate."

    s "No."

    a "Not tonight. Not at the library when I put my hand on the table. Not on the night Lila needed you."

    s "No."

    a "Three times."

    s "Three times."

    a "Sophia."

    s "Yeah."

    a "Why?"

    s "Why what?"

    a "Why me. Why the quiet. Why the girl who barely talks when you're made of words."

    s_thoughts "I look at her."

    s_thoughts "Amara Kismet."

    s_thoughts "Brown eyes. Long hair. The face that doesn't move much because it doesn't need to."

    s_thoughts "The girl who told me 'quiet people aren't empty.' The girl who plays clarinet at 2 AM for nobody. The girl who noticed I read the same paragraph seven times and said nothing. The girl who put her hand palm up on a table and changed my whole life."

    s "Because you never asked me to be anything."

    a "That's not an answer."

    s "You never asked me to be quiet. Or loud. Or the observer or the fixer or the fun one. You just-- you sat in the armchair and you read your book and you let me be whatever I was that day."

    a "That's not special. That's just not being demanding."

    s "For me it's special."

    s_thoughts "Her hand is on the table."

    s_thoughts "I take it."

    s_thoughts "Her fingers close around mine. The same way. Careful and certain."

    s "My dad left."

    s_thoughts "I don't know why I say it."

    s_thoughts "I've never said it like that. 'My dad left.' Not 'my parents divorced.' Not 'it's complicated.' Just: he left."

    a "You think about him everyday."
    
    s "How can you tell?"

    a "Because I notice you."

    s_thoughts "I breathe."

    s "I started watching people because of him. Not consciously. Just -- if I could see the signs, I could know before someone left. I could prepare."

    a "And did it work?"

    s "No. People leave anyway. Katie left. My dad left. I can observe every detail and it doesn't stop anyone from walking out the door."

    a "I'm not walking out the door."

    s "How do you know?"

    a "Because I waited."

    s_thoughts "I look at our hands."

    a "I waited in the armchair. I waited on the porch. I waited at this table. I don't wait for people, Sophia. I don't do that."

    show amara embarrassed at center

    a "I did it for you."

    s_thoughts "My eyes sting."

    s "Amara."

    a "Mm."
    
    stop music fadeout 2.0
    
    pause 2.0

    s "I love you."

    s_thoughts "I said it."

    s_thoughts "No translation. No file. No careful approach."

    s_thoughts "Just the sentence."
    
    play music mus_stillhere fadein 3.0
    
    pause 3.0    

    show amara vulnerable at center

    s_thoughts "Her face changes."

    s_thoughts "Not the half-degree. Not the smile."

    s_thoughts "Something I've never seen."

    s_thoughts "Open."

    s_thoughts "She puts her forehead against mine."

    s_thoughts "Close. So close."

    s_thoughts "Her breath. Her warmth. The space between us that used to be four inches and then two inches and then zero."

    a "I love you too."

    s_thoughts "Three words."

    s_thoughts "Minimum viable."

    s_thoughts "Maximum weight."

    pause 2.0

    s_thoughts "She kisses me."

    s_thoughts "Or I kiss her."

    s_thoughts "I don't know who moves first."

    s_thoughts "It doesn't matter."

    s_thoughts "Her hand is in my hair. My hand is on her jaw. The library is empty and the fluorescents are humming and the books are closed and we are not reading."

    s_thoughts "We are very much not reading."

    s_thoughts "She kisses the way she speaks. Precise. Certain. Each movement deliberate."

    s_thoughts "I kiss the way I do everything. Too much. Too fast."

    s_thoughts "She slows me down."

    s_thoughts "Her hand on my cheek. The gentlest pull back. Just enough to breathe."

    a "Slower."

    s "Sorry."

    a "Don't apologize. Just slower."

    s_thoughts "Slower."

    s_thoughts "I learn slower."

    s_thoughts "The library is empty. Her mouth and my mouth are together and the impossible fact of this sits at our table."

    pause 2.0

    s_thoughts "We pull apart."

    s_thoughts "She's looking at me."

    s_thoughts "I'm looking at her."

    show amara smile at center

    s_thoughts "She's smiling."

    s_thoughts "The real one. The one that changes her whole face."

    a "The librarian is going to kick us out."

    s "Let her."

    a "It's her job, Sophia."

    s "I don't care."

    a "I care. I have a reputation here."

    s_thoughts "I laugh."

    s_thoughts "She almost laughs."

    s_thoughts "The half-degree becomes a full degree."

    s_thoughts "We sit."

    s_thoughts "Her hand in mine."

    s_thoughts "The library. Our library."

    show amara neutral at center

    s_thoughts "Beautiful."
    
    hide amara with dissolve

    pause 2.0

    ## === THE COST ===

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    s_thoughts "It's been a while."

    s_thoughts "I'm in the kitchen."

    s_thoughts "Charlotte's muffins on the counter. Labeled. Eve. Isabella. Amara."

    s_thoughts "No Sophia."

    s_thoughts "Not because Charlotte is mad. Because Charlotte noticed that I haven't been eating them."

    s_thoughts "She stopped making mine."

    s_thoughts "That's worse than angry."

    s_thoughts "My phone."

    s_thoughts "Lila's last text: three weeks ago. 'ok.'"

    s_thoughts "One word."

    s_thoughts "One word from Lila. The girl who uses forty words when four would do."

    s_thoughts "One word means she's done trying."

    s_thoughts "Isabella's door is closed. She's talking to Lumi. I can hear the typing. The occasional laugh."

    s_thoughts "I haven't talked to Isabella in two weeks. Maybe three."

    s_thoughts "Eve's door has been closed for days. Nobody mentions it."

    s_thoughts "The house has three people in it now."

    s_thoughts "Four if you count me. But I'm at the library."

    s_thoughts "I'm always at the library."

    scene bg library with Fade(0.8, 0.3, 0.8)

    stop music fadeout 2.0

    play music mus_amara fadein 3.0

    s_thoughts "Tuesday. The table."

    show amara neutral at center with dissolve

    s_thoughts "Amara is reading. I'm reading."

    s_thoughts "Our ankles are touching under the table."

    s_thoughts "She reads slower to wait for me."

    s_thoughts "I read faster to keep up."

    s_thoughts "Somewhere in the middle, we meet."

    a "You're thinking about the house."

    s "How do you--"

    a "You fidget when you're guilty."

    s "I don't fidget."

    a "Your left hand is tapping the table."

    s_thoughts "I stop tapping."

    a "Charlotte?"

    s "She stopped making my muffin."

    a "Mm."

    s "And Lila hasn't texted."

    a "Mm."

    s "And Isabella--"

    a "Sophia."

    s "Yeah."

    a "You chose this."

    s_thoughts "Not cruel. Factual."

    a "You chose this and it's real and it costs things."

    s "I know."

    a "Do you regret it?"

    s "No."

    a "Then stop fidgeting."

    s_thoughts "I look at her."

    s_thoughts "She's reading."

    s_thoughts "She's always reading."

    s_thoughts "I pick up my book."

    s_thoughts "We read."

    s_thoughts "The library is ours."

    s_thoughts "The library is ours and the house is quiet and Lila's last text is 'ok' and Charlotte stopped making my muffin."

    pause 2.0

    s_thoughts "Her ankle against mine."

    s_thoughts "Her hand across the table."

    s_thoughts "I take it."

    s_thoughts "She doesn't look up from her book."

    s_thoughts "She squeezes."
    
    s_thoughts "Quiet."
    
    s_thoughts "Peaceful."

    s_thoughts "Still."

    pause 3.0

    hide amara with dissolve

    stop music fadeout 4.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Still{/size}"

    $ persistent.ending_amara_still = True
    $ persistent.completed_amara_route = True
    return

## ===========================
## ENDING 6: "Parking Lot" -- ALONE
## fire=1 after increment. Path: Amara/Amara/Lila.
## The rarest. The saddest.
## Sophia chose stillness twice and ran.
## ===========================

label amara_ending_parkinglot:

    scene bg livingroom night with dissolve

    show lila sad at center with dissolve

    play music mus_fragile fadein 2.0

    s_thoughts "I turn to Lila."

    s_thoughts "She's watching me."

    s_thoughts "She always watches me."

    s "Lila."

    l "Yeah."

    s "I'm staying."

    show lila neutral at center

    l "Okay."

    s "I mean it."

    l "I heard you."

    s_thoughts "She scoots over on the couch."

    s_thoughts "I sit."

    s_thoughts "Shoulder to shoulder."

    l "You came after me."

    s "I did."

    l "Not the library."

    s "Not the library."

    s_thoughts "She's quiet."

    s_thoughts "Lila is never quiet."

    show lila sad at center

    l "Can I ask you something?"

    s "Yeah."

    l "Why?"

    s "Why what?"

    l "Why now. You chose her. Twice. The night I needed you -- you stayed with Amara. The library, the porch, all of it. You did the work. You became the quiet version."

    l "And now, tonight, when it actually matters, you're here."

    s "Because--"

    l "WHY."

    s_thoughts "The question is loud and it echoes."

    s "Because the quiet was too hard."

    stop music fadeout 2.0

    s_thoughts "I hear myself say it."

    s_thoughts "The truth."

    s_thoughts "The ugly, simple truth."

    s "I chose Amara when it was easy. When it was the library and the porch and the silence was comfortable. When choosing her felt like growth."

    s "And tonight -- with you in the living room and her in the armchair and the choice being real -- I couldn't do it."

    s "I ran."

    show lila pissed at center

    l "You ran."

    s "I ran back to the fire."

    l "To me."

    s "To you."

    s_thoughts "She stands."

    l "You're not choosing me, Sophia."

    s "I am--"

    l "You're running from her."

    s_thoughts "Lila."

    s_thoughts "Looking at me with an expression I've never seen. Not angry. Not hurt."

    s_thoughts "Clear."

    show lila sad at center

    l "I have been in love with you for a while."

    s_thoughts "She says it flat."

    l "And I would give anything for you to choose me. ANYTHING."
    
    l "..."

    l "But... not like this."

    s "Lila--"

    l "Not as a refuge. Not because the quiet girl was too hard. Not because the fire is easier."

    l "I deserve to be chosen, Sophia. Not defaulted to."

    s_thoughts "My eyes burn."

    s "You're right."

    l "I know I'm right."

    s "I'm sorry."

    show lila sad at center

    l "I know you're sorry too."

    s_thoughts "She picks up her jacket."

    l "I'm going home."

    s "Lila--"

    l "My home. My dorm. Not this house."

    s_thoughts "She walks to the door."

    l "Text me in a week. Or a month. When you know what you actually want."

    s_thoughts "She opens the door."

    l "And Sophia?"

    s "Yeah?"

    l "Don't you dare case-study this. Don't you dare turn this into a file. Just feel it."

    s_thoughts "She leaves."

    hide lila with dissolve

    stop music fadeout 2.0

    pause 3.0

    ## === AMARA ===

    scene bg library with Fade(1.0, 0.5, 1.0)

    s_thoughts "Sunday."

    s_thoughts "I go to the library."

    s_thoughts "I don't know why. Force of habit. Muscle memory. The walk I've done a hundred times."

    show amara neutral at center with dissolve

    s_thoughts "She's there."

    s_thoughts "Our table."

    s_thoughts "She's reading."

    s_thoughts "I sit next to her."

    s_thoughts "She doesn't look up."

    s "Amara."

    a "You chose Lila."

    s "I--"

    a "You chose Lila."

    s_thoughts "Not a question."

    s "I stayed with her. But she--"

    a "I know."

    s "How do you--"

    a "Because you're here."

    s_thoughts "She closes her book."

    show amara neutral at center

    a "You chose me when it was comfortable."

    s_thoughts "The night on the porch. Her hand. The library."

    a "You left me when it cost something."

    s_thoughts "Last night. The living room. Lila on the couch. The armchair empty."

    s "I'm sorry."

    a "I'm not angry."

    s "You should be."

    a "I don't do angry. I do information."

    play music mus_mourning fadein 3.0

    a "Sophia."

    s "Yeah."

    a "Katie named the pattern."

    a "You chose stillness when it was a vacation from yourself. When it cost nothing. When the fire was still there to go back to."

    a "And then you went back."

    s "I wanted to stay."

    a "Wanting isn't staying."

    s_thoughts "Three words. Devastating."

    s "Can we-- can I--"

    a "No."

    s_thoughts "One word."

    a "Not because I don't care. Because I can't be the person you practice change on and then leave unchanged."

    s "I didn't leave--"

    a "You left, Sophia."

    s_thoughts "She opens her book."

    a "The table is here. The library is here. I'm here."

    s_thoughts "She reads."

    a "But the hand is mine now. Not ours."

    s_thoughts "I sit next to her."

    s_thoughts "Two inches."

    s_thoughts "The two inches that used to be an invitation."

    s_thoughts "Now they're a moat."

    hide amara with dissolve

    stop music fadeout 3.0

    ## === ALONE ===

    scene bg kitchen night with Fade(1.0, 0.5, 1.0)

    s_thoughts "Tuesday. 2 AM."

    s_thoughts "The kitchen."

    s_thoughts "I came downstairs for water."

    s_thoughts "The mugs are in the drying rack. Charlotte's. Isabella's. Amara's."

    s_thoughts "Mine is in the cabinet. I haven't used it in days."

    s_thoughts "The kitchen is dark. The fridge hums. The chore chart on the fridge has my name in Charlotte's handwriting."

    s_thoughts "The house is sleeping."

    s_thoughts "I sit at the table."

    s_thoughts "Nobody's chair."

    s_thoughts "My phone is upstairs. I don't know who would text me."

    s_thoughts "Lila said a week or a month."

    s_thoughts "Amara said no."

    s_thoughts "Charlotte said 'morning' today and it sounded like 'of course' and both of them sounded like giving up."

    s_thoughts "Katie said: 'You find someone interesting. You burn everything else down. You cry in a parking lot.'"

    s_thoughts "Different girl."

    s_thoughts "Different parking lot."

    s_thoughts "Same Sophia."

    pause 3.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Parking Lot{/size}"

    $ persistent.ending_amara_parking_lot = True
    $ persistent.completed_amara_route = True
    return

## ===========================
## GLASS HOUSES ENDING: BRING LILA TO THE LIBRARY
## Unlocked only when all four routes are complete AND
## sophia_fire is 0 (Amara path) or 2 (Lila path).
## Shared opening, then branches on fire:
##   fire 2 -> Burn  (Amara confesses, rejected, Sophia lands with Lila)
##   fire 0 -> Extinguish (Lila confesses, rejected, Sophia lands with Amara)
## ===========================

label amara_ch6_bring_lila:

    ## ---------- SHARED OPENING ----------

    scene bg livingroom night with Fade(0.8, 0.3, 0.8)

    s_thoughts "Lila's still on the couch."

    s_thoughts "The armchair is still empty."

    s_thoughts "I've been looking at both of them like they're a multiple choice question and I'm the idiot running the clock down."

    show lila sad at center with dissolve

    s_thoughts "Lila notices me notice her."

    l "...So which is it."

    s "Get up."

    show lila shocked at center

    l "Excuse me?"

    s "Get up. Get your jacket. We're going to the library."

    l "The-- the library."

    s "Yes."

    l "The library. Where Amara just went. That library."

    s "That library."

    show lila annoyed at center

    l "Babe. I don't do the library. The library is her thing. If I wanted to spend my Friday night whispering next to a bunch of economics majors I would have picked a different major. Or literally any other hobby."

    s "I know."

    l "Then why are you--"

    s "Because I need both of you in the same room and one of you is already there."

    pause 1.5

    show lila sad at center

    s_thoughts "Her face does the thing where it's trying to be three expressions at once. Skepticism winning by a nose."

    l "Sophia."

    s "Please."

    pause 2.0

    l "...Okay."

    l "But if I get shushed by a stranger I'm going to cry and then you're going to have to explain to Amara why I'm crying in her library."

    s "Deal."

    hide lila with dissolve

    ## ---------- INSIDE THE LIBRARY ----------

    scene bg library night with Fade(1.5, 0.8, 1.5)

    stop music fadeout 2.0

    s_thoughts "The library at night has a specific quality."

    s_thoughts "Not silence. Silence would be easier. It's the kind of quiet made out of a lot of small noises that have agreed not to be loud -- pages, pencils, someone's chair scrape two aisles over, the HVAC doing its thing."

    s_thoughts "Amara's table is where our table always is."

    show amara neutral at center with dissolve

    s_thoughts "She looks up when I come in."

    s_thoughts "Her face does the small thing it does when she's glad to see me and won't make a production of it."

    s_thoughts "Then Lila walks in behind me."

    show amara neutral at right with move
    show lila sad at left with dissolve

    s_thoughts "Amara's page-turning hand pauses."

    s_thoughts "Something in her shoulders resets. Like a clock being wound back half a turn."

    pause 2.0

    a "...Hi."

    l "Hi. I'm -- I'm being quiet. I promise. This is me being quiet."

    s_thoughts "It is, technically, her being quiet."

    a "Sit down."

    s_thoughts "Amara doesn't say 'both of you.' She doesn't have to. The invitation is in the way she moves her bag off the chair across from her -- and then, after a half-second, moves her second stack of books off the chair next to that."

    s_thoughts "She's making room for two."

    s_thoughts "Lila sits like she's afraid the chair is going to file a noise complaint."

    s_thoughts "I sit in my spot. The spot I have sat in for -- God, how many nights. The spot that has a version of me pressed into it from all the times I came here and read across from her and let my chest do the architectural thing."

    pause 2.0

    s_thoughts "Nobody is saying anything."

    s_thoughts "Amara isn't going to speak first. That's not her job. Lila isn't going to speak first -- she can tell this is a room where she's a guest."

    s_thoughts "Which leaves me."

    s_thoughts "Which is fine. It's my idea. It should be me."

    pause 1.5

    s "Okay."

    s "Okay. I'm going to say a thing, and I'm going to say it badly, and I'm going to say it to both of you at the same time, and I need you both to let me say it without doing the thing where you rescue me halfway through."

    show lila neutral at left

    l "I would never."

    s "You absolutely would."

    l "...Fair. I'll sit on my hands."

    s_thoughts "She sits on her hands."

    s "Amara already knows most of this part. I'm saying it for Lila. But I want to say it where Amara can hear it because--"

    s_thoughts "I don't finish the sentence. I can feel Amara looking at me. Not hard. Just... looking."

    s "Because I've only ever said it once before, and the person I said it to is sitting at this table, and I don't want there to be a version of this where one of you has a piece of me the other one doesn't."

    show amara neutral at right

    s_thoughts "Amara's eyes flick down to the table. Up again. Steady."

    pause 2.0

    ## ---------- THE COMPRESSED DAD CONFESSION ----------

    play music mus_mourning fadein 4.0

    s "My dad left when I was twelve."

    pause 1.5

    s_thoughts "Lila's face. I'm not going to look at Lila's face. If I look at Lila's face I'm going to stop."

    s "I was close with him. And then one day I came home from school and his stuff was gone and there was a note."

    s "The note said he loved us and he needed to figure some things out. He called three times the first year. Then birthdays. Then my sister's birthdays. Then nothing."

    pause 1.0

    s "I was twelve and I thought -- if I had paid more attention, I would have seen it coming. I could have done something. I could have watched harder."

    s "So I started watching harder."

    s "I've been watching harder since I was twelve. I walk into a room and I check the exits and I check the faces and I file everyone and I think I'm being perceptive but what I'm actually doing is--"

    pause 1.0

    s "--I'm trying to make sure nobody can surprise me by leaving."

    s_thoughts "My voice is doing the flat thing. The reporting-facts thing."

    s "Katie figured it out first. Said it cruel. Amara figured it out second. Said it kind."

    show amara neutral at right

    s_thoughts "Amara's jaw works. Once. She doesn't look away."

    s "Amara said: 'You don't watch people because you're curious. You watch them because you're afraid they'll leave.'"

    s "And she was right. And I've been carrying that around for weeks trying to figure out what to do with it."

    pause 2.0

    s_thoughts "I make myself look at Lila."

    show lila sad at left

    s_thoughts "Lila is staring at me. Her eyes are bright in the weird library light."

    s "And here's the part I wanted to say out loud. To both of you."

    s "I'm afraid I'm going to lose either of you the way I lost him."

    s "I can't choose which of you to lose. I don't -- I don't have the machinery for that. I tried. I tried the math for weeks. It doesn't work."

    s "So I need you both to stay."

    s "Which means you both have to matter to each other. Because you both matter to me."

    stop music fadeout 4.0

    pause 3.0

    ## ---------- BOTH GIRLS RESPOND ----------

    s_thoughts "The library does its library thing. Pages. HVAC. A chair scrape. All of it very far away."

    show lila sad at left

    l "Sophia -- "

    l "Sophia, you can't just -- "

    l "Okay. Okay. I'm sitting on my hands. I'm going to be normal. Oh my god."

    s_thoughts "She looks at Amara. It's the first time tonight Lila has looked at Amara on purpose."

    l "Hi. I'm Lila. I know we've met a thousand times. I'm meeting you again because apparently this is a new kind of meeting."

    show amara neutral at right

    a "Hi, Lila."

    l "You call her Sophia."

    a "Yes."

    l "Not babe. Not any of the things I call her."

    a "...No."

    l "Okay. Okay, that's -- that's fine. That's useful information. I'm cataloguing that."

    s_thoughts "Lila is doing the Sophia thing. Filing. In public. At a library table. It would be funny if anything were funny."

    pause 1.5

    show amara neutral at right

    a "Sophia."

    s "Yeah."

    a "Thank you for telling her."

    s "I should have told her months ago."

    a "Probably."

    s_thoughts "Half a smile, mostly in her eyes. A courtesy. An acknowledgment. A door creaking open."

    pause 2.0

    s_thoughts "And then the room changes."

    s_thoughts "I can feel it before I can name it. Something in the weight of the air at our table. One of them has a next sentence."

    if sophia_fire == 2:
        jump amara_ch6_bring_lila_burn
    else:
        jump amara_ch6_bring_lila_extinguish


## ===========================
## BURN (fire == 2)
## Amara asks Lila to leave. Amara confesses. Sophia rejects gently.
## The pinned reading-together exchange. Sophia returns to Lila.
## Loud romantic landing.
## ===========================

label amara_ch6_bring_lila_burn:

    ## ---------- AMARA ASKS LILA TO LEAVE ----------

    show amara embarrassed at right

    a "Lila."

    show lila sad at left

    l "Yeah?"

    pause 1.5

    a "Can I have a minute with Sophia. Please."

    s_thoughts "My stomach does something I don't have a word for."

    s_thoughts "Lila's face -- I watch it happen in real time. The read. The understand. The decide."

    show lila shocked at left

    l "Oh."

    l "Oh."

    show lila sad at left

    l "Yeah. Yeah, of course."

    s_thoughts "She gets up fast. Too fast. She catches her own hip on the edge of the table and doesn't even flinch."

    l "I'll be -- I'll be in the poetry section pretending to like poetry."

    l "Or -- no. Outside. I'll be outside. On the steps. It's too quiet in here for the kind of normal I'm about to be."

    a "Lila."

    show lila sad at left

    l "Mm."

    a "Thank you."

    pause 2.0

    show lila shocked at left

    s_thoughts "Lila's mouth opens. Closes. She nods once, hard, and doesn't look at me."

    l "...Yeah."

    hide lila with dissolve

    s_thoughts "The library door is heavy. I don't hear it close -- I feel it, the way you feel a pressure change in your ears."

    pause 3.0

    ## ---------- THE TABLE ----------

    show amara embarrassed at center with move

    s_thoughts "Just us."

    s_thoughts "Our table."

    s_thoughts "The table where I have read across from her for -- I don't even know. Where I have learned the shape of her hand turning a page. Where she told me, in the most Amara way possible, that she was reading slower to keep pace with me."

    s_thoughts "Amara isn't looking at me."

    s_thoughts "Amara is looking at her book. Which is closed."

    pause 3.0

    play music mus_amara fadein 4.0

    s_thoughts "I don't say anything. I've learned that much. Amara is getting somewhere and she needs the silence to walk across."

    pause 2.5

    show amara vulnerable at center

    a "I had a plan."

    s "..."

    a "I was going to let you walk away from me. I was going to sit at this table with my book and let you fall for someone else and not say anything. I had the whole plan. I had it memorized."

    s "Amara--"

    a "Let me."

    pause 1.5

    a "I'm changing the plan."

    pause 2.0

    a "I love you."

    s_thoughts "My chest does the architectural thing. A load-bearing wall with a slow give."

    s_thoughts "I don't say anything. I can't. She hasn't finished."

    pause 2.0

    a "I'm telling you because I don't want the record to show I was a coward about it."

    a "And I'm telling you I can't."

    s "...Can't what?"

    a "Be with you."

    a "I'm telling you I love you and I'm telling you I'm scared you'll leave and I'm telling you I'm going to be the one who leaves first. Because I can't be left by you. Not by you."

    pause 1.5

    a "I don't have another Nora in me."

    s_thoughts "That hits."

    s_thoughts "I feel the weight of it and I don't touch it."

    pause 3.0

    ## ---------- SOPHIA REJECTS GENTLY ----------

    s_thoughts "My voice when it comes out of me sounds like it's coming from somewhere other than my throat."

    s "Amara."

    s_thoughts "She's looking at her book. Still closed."

    s "Amara, look at me. Please."

    show amara vulnerable at center

    s_thoughts "She looks up."

    pause 2.0

    s "I think I'm in love with Lila."

    s_thoughts "The sentence sits on the table between our hands like a third thing."

    s "I think I have been for a while. I didn't let myself see it until she stormed the coffee shop. Maybe before that. Maybe since the first time she called me babe and I got mad about it and then wanted her to do it again."

    pause 1.0

    s "And I've been -- God, this is going to sound terrible. I've been trying to be the kind of person you could love. I've been practicing stillness like it was a second language and I had a test coming up."

    pause 1.5

    s "You fell for the version of me who knows how to sit across from you for three hours without talking. And she's real. But she's only real in this room, with you, and I can't -- I can't live in one room."

    s_thoughts "Amara is still looking at me. Her face is doing the small thing. The controlled thing. The thing where all of the feeling is happening in one muscle at the corner of her mouth and you have to know her to see it."

    s "I'm so sorry."

    pause 2.5

    show amara neutral at center

    a "Don't."

    s "Don't what?"

    a "Don't be sorry for being a forest fire. I knew you were a forest fire. I watched you be one. I chose to sit next to it anyway."

    pause 1.5

    s "Okay."
    
    s "...Thank you."

    s_thoughts "A small silence. The kind we are good at."

    pause 3.0

    ## ---------- THE PINNED READING-TOGETHER EXCHANGE ----------

    ## FOUR LINES. VERBATIM. NO EXPANSION.

    show amara vulnerable at center

    a "Can... can we still read together? In the library?"

    s "Yes. Obviously."

    show amara neutral at center

    a "...OK. But I'm not slowing down for you anymore."

    s "Wouldn't dream of it."
    
    hide amara with dissolve
    
    stop music fadeout 4.0

    pause 2.5

    show amara neutral at center with dissolve
    
    pause 2.0
    
    s_thoughts "I turn back. Just for a moment."
    
    s_thoughts "...She's reading."
    
    hide amara with dissolve
    
    pause 2.5

    scene bg campus night with Fade(1.5, 0.8, 1.5)

    ## ---------- LILA, ON THE STEPS ----------

    s_thoughts "She's on the library steps."

    s_thoughts "Her jacket is half-on, half-off. Like she started putting it on and got distracted by the act of existing."
    
    play music mus_campus fadein 1.5

    show lila sad at center with dissolve

    s_thoughts "She looks up when I come out the doors."

    s_thoughts "Her face does the thing. The read. She does not ask me what happened."

    pause 2.0

    l "Come here."

    s "Lila--"

    l "Don't talk. Come here."

    s_thoughts "I come here."

    pause 2.0

    s_thoughts "She stands up. She's shorter than me in her sneakers but somehow the steps make us the same height. Her hands are cold. Her hands find my jacket -- the jacket, the one she says makes her feel safe -- and she gets two fistfuls of it like she's afraid I'm going to blow away."

    show lila neutral at center

    l "I saw your face coming out the door."

    l "You don't have to tell me."

    l "I know."
    
    stop music fadeout 1.5

    pause 1.5

    s_thoughts "I open my mouth to say something and she kisses me."

    play music mus_shoulders fadein 3.0

    pause 3.0

    s_thoughts "It is not a gentle kiss."

    s_thoughts "It is a Lila kiss."

    s_thoughts "Loud in every way a kiss can be loud without making any actual noise. All mouth and fists and library steps and the cold. She kisses me like she's been saving up for it and she kisses me like she knows what it cost and both of those things are in her mouth at the same time."

    pause 2.5

    s_thoughts "When she pulls back she keeps hold of the jacket."

    show lila sad at center

    l "I am not going to say anything smart."

    l "I'm not even going to try. I had -- I had a whole line ready. I had five lines ready. They're all stupid."

    s "Lila."

    l "I know she's still in there."

    l "I'm not going to -- I'm not going to be weird about it. I mean I'm going to be a little weird about it because I am a person. But not the kind of weird where you have to pick between me and your friend. I'm not going to make you do that."

    pause 1.0

    l "She's your friend. I can see that. I could always see that. That's why I was doing all my handling."

    s "You're not handling anymore."

    show lila neutral at center

    l "No. I'm officially not handling."

    l "I'm being loud about it. On the library steps. Where she can probably hear me through the glass if she tries."

    s_thoughts "She looks over my shoulder at the library doors."

    s_thoughts "I don't turn. I don't need to."

    pause 2.0

    show lila sad at center

    l "Did she tell you?"

    s "Yes."

    l "Did you tell her no?"

    s "Yes."

    l "Did you tell her why?"

    pause 1.5

    s "I told her I was in love with you."

    s_thoughts "Something in her face does a thing. Not a smile. Smaller than a smile. The thing before a smile when the muscles are still deciding whether it's safe."

    l "...Oh."

    l "Oh."

    show lila neutral at center

    l "Sophia, that is the meanest nicest thing you have ever done."

    s "Yeah."

    l "I am going to cry about it in exactly one hour."

    s "Noted."

    pause 2.0

    l "Come here again. I wasn't done."

    s_thoughts "I come here again."

    pause 3.0

    ## ---------- THE LANDING IMAGE ----------

    s_thoughts "This kiss is different."

    s_thoughts "Slower. Still loud, but loud in a different key. The key of knowing."

    s_thoughts "Her fingers move from the jacket to the back of my neck. She's not holding on anymore. She's just -- touching. Like she's allowed to, now."

    pause 2.5

    s_thoughts "Somewhere behind me, through the glass, a library is doing its library thing. Pages. HVAC. A chair scrape two aisles over. A girl at a table with her book open, reading at her own speed."

    s_thoughts "Both rooms exist at the same time."

    s_thoughts "Both rooms have someone in them I love."

    s_thoughts "Only one of them is the room I am standing in."

    pause 3.0

    show lila sad at center

    l "Sophia."

    s "Yeah."

    l "Walk me home."

    s "Yeah."

    l "Slowly."

    s "Yeah."

    s_thoughts "We go down the library steps."

    s_thoughts "I don't look back at the glass."

    s_thoughts "Not because I'm afraid to."

    s_thoughts "Because I don't know when I'll stop looking back."

    pause 3.0

    stop music fadeout 4.0

    hide lila with dissolve

    $ persistent.ending_amara_burn = True
    $ persistent.gh_seen_amara = True
    $ persistent.completed_amara_route = True

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Burn{/size}"

    return


## ===========================
## EXTINGUISH (fire == 0)
## Lila confesses publicly. Sophia rejects gently.
## Lila leaves in her own register. Amara initiates the kiss.
## Quiet, sensual library landing.
## ===========================

label amara_ch6_bring_lila_extinguish:

    ## ---------- LILA BREAKS ----------

    show lila neutral at left

    s_thoughts "It's Lila."

    s_thoughts "Of course it's Lila. Amara was never going to be the one to break the surface. Amara is made of surface."

    s_thoughts "Lila's hands come out from under her thighs. She puts them flat on the table. Palms down. Like she's bracing."

    l "Okay."

    l "Okay. Sophia. I'm going to be brave because nobody else in this library is going to do it for me apparently. Including you."

    show amara neutral at right

    s_thoughts "Amara's eyes move to Lila. Slow. Careful. The way Amara looks at things she has already decided are important."

    l "I had a whole -- I had a WHOLE thing I was going to say to you. At a bar. The one on Seventh. With music on. With, like, tequila involvement."

    l "And instead I'm in a library where I can't even whisper correctly, and apparently tonight is the night, so. So."

    pause 1.5

    l "My feelings for you."
    
    s "Lila--"
    
    l "Stop. Let me talk."
    
    s "Okay."
    
    l "I'm..."

    l "I'm not handling it, Sophia."
    
    s_thoughts "Oh."

    l "I haven't been handling it. I have been actively not handling it. I have been -- if handling has a verb that is the opposite of handling, that is the verb I have been doing."

    pause 1.0

    l "The reason I've been weird. The real reason. Why I've been distant."

    show lila sad at left

    l "I'm jealous."

    l "I'm jealous. Of her. Specifically of her."

    s_thoughts "I can feel Amara's stillness like a temperature."

    l "I have been jealous of her since you started looking at her the way you never looked at anything because you were saving all the looking for her."

    l "I would see you do it. Across a room. At the kitchen table. At the thing in the quad. You'd get this -- this FACE. This stupid private face like you were reading a book I wasn't in." 
    
    l "And I'd stand there doing the whole Lila routine -- the jokes, the noise, the BABE, the jacket thing -- and you'd smile at me and I'd KNOW I got maybe sixty percent of you back and the other forty percent was still over there with her."

    pause 1.5

    l "I'm in love with you."

    l "I know you know. I've known you know for a while. I've known Amara knows since... probably that night after karaoke, honestly. I think the whole FLOOR of this library knows at this point."

    show amara neutral at right

    s_thoughts "Amara is not moving. Amara is holding her book in her lap with both hands and not moving. She is giving Lila the single most valuable thing Amara has, which is the full attention of the quietest person in the room."

    show lila neutral at left

    l "I tried to handle it. I really did. I was going to handle it by being your best friend and stealing little pieces of you when nobody was looking and writing a play about it in like ten years when it didn't hurt anymore."

    l "And then you walked me into the library tonight with her in it and you told me about your dad and you said 'you both have to matter to each other' and I just -- "

    l "I can't. I can't do that. I can't sit at this table knowing what I'm sitting at. Not without saying it first. I'm sorry. I know this is the worst possible place and the worst possible time and I'm saying it anyway. Because I'm a coward about everything except this."

    pause 2.0

    l "Okay. That's the thing. That's the whole thing. I'm -- yeah. That's it."

    s_thoughts "The library has done a thing. Three tables away, a girl with headphones has taken the headphones off. I don't look. I can tell by the quality of her silence."

    pause 3.0

    ## ---------- SOPHIA REJECTS GENTLY ----------

    s_thoughts "I don't get a version of this where we walk outside first. I don't get a version where I get to do it in private. I have to say it here. In front of Amara. In front of the girl three tables away with her headphones off. In front of the HVAC."

    s_thoughts "Good."

    s "Lila."

    show lila sad at left

    l "Yeah."

    s "I love you."

    s "I love you so much. Let me say that first. Let me say that so hard it gets in the walls."

    pause 1.5

    s "I'm not in love with you."

    s_thoughts "Her face doesn't move. Her mouth moves. The rest of her face doesn't."

    s "I love you like -- I don't have words for how I love you." 
    
    s "You gave me a nickname I pretended to hate for a month because I was too embarrassed to admit I liked it. You are the only person who makes me laugh until I can't see. That love is real and it's yours and I'm not taking a word of it back."

    s "And it's not the other kind."

    pause 1.5

    show amara neutral at right

    s_thoughts "I make myself look at Amara."

    s "I'm in love with her."

    s "I've been in love with her since -- I don't know. Since the armchair. Since the first time she said 'ask me.' Since she told me I watch people because I'm afraid they'll leave and I didn't break."

    s "I didn't always know that was the word. I know it now."

    pause 1.0

    show lila sad at left

    s "You're my best friend and I want you in my life forever and I would do anything for you and I am so, so sorry."

    pause 3.0

    ## ---------- LILA'S RECOVERY ----------

    s_thoughts "Lila puts her palms back on the table. Flat. She looks at her hands like they're new."

    l "Okay."

    l "Okay. I'm -- okay."

    show lila shocked at left

    l "I'm going to make a joke now because if I don't make a joke I am going to start a fire in a library and I don't want to be THAT girl."
    
    l "..."

    l "...I got nothing. I got no joke. I have been depleted of jokes. This is what being depleted of jokes feels like. It's not good."

    s_thoughts "She laughs. It comes out wrong. Half a laugh, half the other thing."

    show lila sad at left

    l "God, Sophia, you love me so hard. I can hear you loving me. I can hear you being careful with the word."

    l "That doesn't make it better. But I want you to know I heard it."

    pause 2.0

    l "Okay. Stage directions."

    l "I'm going to get up. I'm going to walk out of this library. I'm going to need some space. A lot of space. Embarrassing amounts of space." 
    
    l "I'm going to need to not be in this library for a while, and I'm going to need to not be looking at the two of you doing -- whatever you're about to do -- for a few weeks. Minimum. Possibly more. Definitely more if I see you make that face at her again where I'm not in it."

    show lila neutral at left

    l "And then."

    l "And then I'm going to come back."

    l "I always come back. You know I always come back. It's my whole deal. I am the girl who comes back."

    l "Just -- not right now."

    pause 1.5

    show lila sad at left

    l "Okay."

    l "Okay I'm doing it. I'm getting up. I'm doing it."

    s_thoughts "She gets up. She doesn't look at me while she does it. She's holding her whole body very carefully, the way you hold something that might spill."

    l "Sophia."

    s "Yeah."

    l "Don't come after me tonight. Just -- tonight. Give me tonight to cry without you watching."

    s "Okay."

    l "I'll text you tomorrow. Probably. Or the day after. I'll text you when I can text you without it being weird."

    s "Okay."

    pause 1.0

    show lila neutral at left

    l "...For the record. For the record I still like the jacket. That's -- that's going to be a problem later. But not tonight."

    s_thoughts "Half a smile. Then she's gone."

    hide lila with dissolve

    s_thoughts "The door of the library is heavy. I hear it close this time."

    pause 4.0

    ## ---------- ALONE WITH AMARA ----------

    show amara neutral at center with move

    play music mus_amara fadein 4.0

    s_thoughts "The library after Lila leaves is a different library."

    s_thoughts "Not quieter. It wasn't loud. But the shape of the quiet has changed. Lila was using up a specific kind of oxygen and now there's more of it and I don't know what to do with it."

    s_thoughts "Amara is -- Amara."

    s_thoughts "Still holding her book in both hands. Still not moving."

    s_thoughts "Her eyes on me."

    pause 3.0

    a "That took a lot out of her."

    s "I know."

    a "She's going to be okay."

    s "I know."

    pause 2.0

    s_thoughts "I don't know if I know."

    s_thoughts "I know because Amara said it."

    s_thoughts "Amara doesn't say things she's not sure about."

    pause 2.0

    s_thoughts "She sets her book down."

    s_thoughts "Not on the little stack she brought. Not open to her page. She closes it. She puts it on the table next to her. And then she moves it another inch. Away from her. Fully out of her hands."

    s_thoughts "In all the hours I have sat at this table across from her, I have never seen Amara set a book fully down and not pick it back up."

    pause 3.0

    show amara neutral at center

    a "Sophia."

    s "Yeah."

    a "Will you come to my side of the table?"

    s_thoughts "Oh."

    s_thoughts "Amara, who waits. Who lets. Who is on the other side of the table asking me to walk over to her -- not who comes to me."

    s_thoughts "I get up."

    s_thoughts "I go around the table. I'm moving slowly because I don't want to break the room. Because I don't want to break her. Because I want her to get the full version of what she's asking for."

    pause 2.0

    s_thoughts "I sit in the chair next to her. The chair Lila sat in a few moments ago. There's still a little warmth in it. Or I'm imagining that. I don't want to know which."

    pause 2.0

    s_thoughts "Amara turns her chair to face me. Not all the way. Enough."

    s_thoughts "Her knees are almost touching mine."

    s_thoughts "Two inches."

    pause 2.0

    a "I have been thinking about something for two weeks."

    s "Tell me."

    a "I have been thinking about whether I can do the thing where I love someone and let them see me love them. At the same time. Out loud. In a room with people in it."

    pause 1.5

    a "I didn't know if I could."

    a "Then Lila did it."

    s_thoughts "My breath catches."

    a "She did it badly. She did it at the worst possible time. And she did it. In public. In a library. Across a table."

    a "She loved you at you in a room full of other people and the library did not fall over."

    pause 2.0

    a "I think I can do it too."

    s "...Amara."

    a "Not the speech. The speech is -- the speech is beyond me. I don't have a Lila speech in me. I'm not built like that."

    pause 1.5

    show amara vulnerable at center

    a "But the part where I love you where people can see it."

    a "I think I can do that part."

    pause 3.0

    ## ---------- AMARA INITIATES THE KISS ----------

    s_thoughts "She reaches for me."

    s_thoughts "Amara."

    s_thoughts "Amara is the one reaching."

    s_thoughts "Her hand finds the side of my jaw first. Her fingers are cold from the book. Her thumb is under my ear. She is not trembling. Amara does not tremble. She is moving with the same deliberate quiet she moves through everything with."

    s_thoughts "And then she leans across the two inches."

    s_thoughts "And the two inches become zero."

    pause 3.0

    stop music fadeout 3.0

    pause 3.0

    s_thoughts "The kiss."

    s_thoughts "The kiss is -- "

    s_thoughts "It is a library kiss."

    s_thoughts "But it's a kiss. It's an Amara kiss."
    
    s_thoughts "The best kind."

    s_thoughts "Amara's mouth is warm. The rest of her is cold. Her cold hand on my jaw. Her warm mouth on mine. Her other hand finds my wrist where it's rested on the table."

    s_thoughts "She does not hurry."

    s_thoughts "It is long."

    s_thoughts "It is so, so long."

    s_thoughts "It is the kind of long that is not about duration. It is about the fact that Amara is choosing to do this for more than a second at a time. Amara, who is kissing me at a library table in front of whoever wants to look, and staying, and staying, and staying."

    pause 4.0

    s_thoughts "When she pulls back she doesn't pull back all the way."

    s_thoughts "Her forehead is against mine."

    s_thoughts "Her eyes are closed."

    s_thoughts "She breathes out, warm against my face. The breath is shaped like a word she doesn't say."

    ## ---------- THE LANDING IMAGE ----------
    
    play music mus_amara fadein 2.0
    
    pause 3.0

    s_thoughts "She sits back."

    s_thoughts "She picks her book up."

    s_thoughts "Not to hide behind. To read. It's her book. It's what she does. She opens it to her page. She finds where she was. Her hand on my wrist stays where it is."

    s_thoughts "Her free hand under the table finds mine."

    s_thoughts "Our fingers lace. Her book is open. Her hand is in my hand. Her feet -- I don't have to look -- her feet have found my feet under the table and are twined up. Two inches. Zero inches. All the inches and none of them at once."

    pause 3.0

    show amara neutral at center

    s_thoughts "I watch her read for a while."

    s_thoughts "My book is still in my bag. I don't reach for it. I'm not reading tonight. Tonight I'm just here, at our table, on her side, with her hand in my hand, watching her turn a page at her own speed."

    pause 2.0

    s_thoughts "Not slower. Her speed."

    s_thoughts "She's not slowing down for me anymore."

    s_thoughts "She doesn't need to. I finally caught up."

    pause 3.0

    s_thoughts "Somewhere across campus, a girl I love is walking home alone so she can cry without me watching."

    s_thoughts "She is going to be okay. Amara said so."

    s_thoughts "She is going to come back. She always comes back."

    s_thoughts "And when she does, the stillness she finds me in is going to have a Lila-shaped hole in it, and that hole is going to be part of the shape of this room forever, and I am going to know that every time I sit at this table from now on."

    pause 3.0

    s_thoughts "Amara turns a page."

    s_thoughts "Her hand in mine does not move."

    s_thoughts "It is quiet."

    s_thoughts "It is quiet."

    s_thoughts "It is quiet."

    pause 4.0

    stop music fadeout 4.0

    hide amara with dissolve

    $ persistent.ending_amara_extinguish = True
    $ persistent.gh_seen_amara = True
    $ persistent.completed_amara_route = True

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Extinguish{/size}"

    return

