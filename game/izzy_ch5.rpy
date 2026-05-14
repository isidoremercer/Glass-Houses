## izzy_ch5.rpy -- Glass Houses
## Chapter 5: "Break" -- Isabella Route
## Act 1: The Almost-Love

## === AUDIO DEFINITIONS (only new tracks not defined elsewhere) ===
define audio.mus_shoulders = "audio/music/Shoulders Touching.mp3"
define audio.mus_stillhere = "audio/music/Still Here.mp3"

## ===========================
## CHAPTER 5 START
## ===========================

label izzy_ch5:

    $ heard_lumi_words = "none"

    ## ===========================
    ## ACT 1: THE ALMOST-LOVE
    ## 14 scenes. The warm foundation.
    ## Everything that gets destroyed later.
    ## ===========================

    ## ===========================
    ## SCENE 1: MORNING ROUTINE
    ## Unconscious domesticity. The house has absorbed the shift.
    ## Charlotte notices. Amara notices Charlotte noticing.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_izzy fadein 3.0

    s_thoughts "I don't remember when I started making two cups of coffee."

    s_thoughts "I mean, I remember the first time. She came downstairs looking like a Victorian ghost who'd been recently electrocuted and I handed her mine because I hadn't taken a sip yet and it seemed like an emergency."

    s_thoughts "But that was weeks ago. Now it's just... a thing."

    s_thoughts "I fill the kettle. Two mugs. One with the chip on the handle that Charlotte keeps threatening to throw out. One with the faded cat face that Isabella claimed on move-in day because, quote, 'he looks like he's seen things.'"

    s_thoughts "The chipped one is mine. I don't know when that happened either."

    show charlotte smile at left with dissolve

    s_thoughts "Charlotte is already at the stove. Eggs. Because Charlotte is always at the stove. Because Charlotte is always making eggs."

    c "Morning!"

    s "Mm."

    c "Sleep well?"

    s "Define 'well.'"

    c "More than four hours."

    s "Then... adjacent to well."

    show charlotte laugh at left

    c "That's better than last week. Progress!"

    s_thoughts "She's watching me pour the second cup. She doesn't say anything about it. Charlotte is the kind of person who notices things and files them under 'not my business yet.' The 'yet' is doing a lot of work."

    s_thoughts "Footsteps on the stairs. Heavy. Uncoordinated. Someone is losing a fight with gravity."

    show isabella sad at right with dissolve

    s_thoughts "Isabella materializes in the doorway. Hoodie on backwards. Hair doing something ambitious."

    i "Mmrgh."

    s "Good morning to you too."

    i "Bold of you to call it morning. Morning implies I chose to be awake."

    s_thoughts "I hand her the cat mug. She takes it without looking."

    i "Thank you. You're keeping me alive. This is a medical intervention."

    s "You stayed up coding again."

    i "I was CLOSE to getting the particle render right. The little dots were ALMOST doing the thing."

    s "The thing."

    i "The THING, Sophia. You know the thing."

    s "I do know the thing."

    show isabella happy at right

    i "Then don't make me explain the thing before coffee. That's inhumane."

    s_thoughts "She takes a long sip. Eyes closed. Something in her shoulders loosens."

    s_thoughts "Charlotte is flipping eggs. She's doing that thing where she looks at the pan but she's looking at us. Charlotte's peripheral vision should be classified as a superpower."

    show amara neutral at center with dissolve

    s_thoughts "Amara appears. I don't know from where. Amara enters rooms like she was already there and you just noticed."

    a "Morning."

    s_thoughts "Amara makes her tea. Because Amara drinks tea, not coffee, because Amara is Amara."

    s_thoughts "She sits at the table. Opens a book. Doesn't look up."

    s_thoughts "Except she does. Once. Quick. At Charlotte."

    s_thoughts "Charlotte is watching me hand Isabella a plate of toast that I don't remember making."

    s_thoughts "Amara is watching Charlotte watch me."

    s_thoughts "I'm watching Isabella eat toast."

    s_thoughts "Nobody is watching the eggs. The eggs are burning."

    c "Oh! The eggs. The eggs are--"

    show charlotte surprised at left

    s_thoughts "Charlotte rescues the eggs. Isabella laughs. I laugh. Amara turns a page."

    s_thoughts "My laptop is upstairs. In Isabella's room. On her desk, next to her setup. The cat sticker facing up."

    s_thoughts "I left it there last night when we were working. She was coding. I was pretending to read. She fell asleep at her desk and I draped a hoodie over her shoulders and went to bed and left my laptop because..."

    s_thoughts "Because it lives there now."

    s_thoughts "Neither of us has said that out loud."

    ## ===========================
    ## SCENE 2: THE BATHROOM
    ## One bathroom. Five girls. Synced schedules.
    ## Forced proximity that became chosen proximity.
    ## ===========================

    scene bg bathroom with dissolve

    s_thoughts "The bathroom situation in this house is a war crime."

    s_thoughts "Charlotte showers at 6:30 because Charlotte is a sociopath. Eve showers at unknowable hours because Eve operates on a timeline that exists outside human comprehension. Amara showers at exactly 7:15 for exactly twelve minutes because Amara is a machine."

    s_thoughts "That leaves Isabella and me fighting over the 7:30 slot."

    s_thoughts "Except we stopped fighting."

    show isabella pj happy at right with dissolve

    s_thoughts "We brush our teeth at the same time."

    s_thoughts "She's at the left sink -- we don't have two sinks, she just stands on the left side of the one sink and I stand on the right side and our elbows bump and this is fine. This is totally fine."

    i "Oo hab oofpaste om oor cheem."

    s "What?"

    s_thoughts "She spits."

    i "You have toothpaste on your cheek."

    s "Where?"

    i "Here."

    s_thoughts "She reaches over and wipes my cheek with her thumb."

    s_thoughts "Her thumb is on my face."

    s_thoughts "I am having a completely normal reaction to a thumb on my face."

    i "Got it."

    s "Thanks."

    i "You brush like you're angry at your teeth."

    s "My teeth know what they did."

    show isabella pj happy at right

    i "See, that's the kind of sentence that makes me think you're secretly a serial killer."

    s "Only on weekdays."

    s_thoughts "She laughs. Rinses. Leans against the wall."

    s_thoughts "I'm rinsing. She's not leaving. There's no reason for her to still be here."

    s_thoughts "I'm not leaving either."

    s_thoughts "Knock on the door. Three sharp raps."

    c "How long?!"

    i "Two minutes!"

    s_thoughts "It's been ten."

    c "You said two minutes ten minutes ago!"

    i "Time is a construct, Charlotte!"

    c "My BLADDER is not a construct, Isabella!"

    show isabella pj embarrassed at right

    s_thoughts "We look at each other. She starts laughing."

    i "We should probably--"

    s "Yeah."

    s_thoughts "We don't move."

    c "I can HEAR you not moving!"

    s "Coming!"
    
    show charlotte pj neutral at left with dissolve

    s_thoughts "We leave the bathroom. Charlotte squeezes past us in the hallway. She gives me a look."

    s_thoughts "It's not a judgmental look. It's a look that says 'I see what's happening and I have opinions and I'm keeping them to myself for now.'"

    s_thoughts "Charlotte keeping opinions to herself is Charlotte at maximum restraint. She's vibrating with it."

    hide isabella 
    hide charlotte
    with dissolve

    ## ===========================
    ## SCENE 3: STUDY SESSION
    ## Sophia's room. Isabella coding on Sophia's bed.
    ## Neither addresses why she's HERE.
    ## The warmth of two people not talking for forty minutes.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)
    play music mus_morningafter fadein 3.0

    s_thoughts "Tuesday afternoon."

    s_thoughts "Isabella is on my bed."

    s_thoughts "That sentence has implications that I am choosing not to examine."

    s_thoughts "She's cross-legged, laptop balanced on a pillow, headphones around her neck but not on because she 'can't code to music, it gets into the variables.'"
    
    s_thoughts "Her room has better desk space. Her room has her entire setup -- monitors, the keyboard she named Gerald, the desk lamp she stole from the library."

    s_thoughts "She's here."

    s_thoughts "I'm at my desk pretending to read Sontag. I'm on the same paragraph I was on twenty minutes ago."

    show isabella competitive at center with dissolve

    s_thoughts "She mouths along to whatever she's typing. I can see her lips moving in my peripheral vision. She does this with code the way some people do it with books. Reads it back to herself. Mutters. Shakes her head. Deletes. Types again."

    s_thoughts "I'm watching."

    s_thoughts "Not the old watching. Just... she's in the room and my eyes keep going there."

    s_thoughts "She catches me."

    show isabella neutral at center

    s_thoughts "I look down at Sontag. The same paragraph. 'The painter's task is not--'"

    s_thoughts "She goes back to coding."

    s_thoughts "I go back to pretending to read."

    s_thoughts "Twenty minutes pass. Neither of us says a word."

    s_thoughts "My room is small. The radiator ticks. Her keyboard clicks. The light through the window changes."

    s_thoughts "This is it. This is the thing I didn't know I wanted. Two people in a room, not performing anything. She doesn't need me to be interesting right now. I don't need her to be anything."

    s_thoughts "She just is."

    s_thoughts "I just am."

    s_thoughts "I catch myself reaching for the old framework -- 'what does this MEAN, what's the pattern, file it under--'"

    s_thoughts "Stop."

    s_thoughts "Just be in the room."

    i "Sophia."

    s "Hm?"

    i "Have you turned a page in the last half hour?"

    s "...I've been on a really dense paragraph."

    show isabella smile at center

    i "Uh huh."

    s "Sontag is dense."

    i "You were watching me type."

    s "I was NOT--"

    i "You move your eyes really fast but not fast enough. You have a tell."

    s "I don't have a tell."

    show isabella happy at center

    i "You hold your breath when you think you've been caught. Like right now."

    s_thoughts "I exhale."

    i "There it is."

    s "I hate that you noticed that."

    i "I notice things too, you know. You don't have a monopoly."

    s_thoughts "She says it light. But underneath it there's something else. Something like: I'm paying attention to you the way you pay attention to me."

    s_thoughts "I don't file it."

    s_thoughts "I just hold it."

    s_thoughts "She goes back to coding. I go back to Sontag. I actually read the paragraph this time."

    hide isabella with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 4: CAMPUS -- WALKING TOGETHER
    ## They walk to campus now. It's assumed.
    ## Isabella talks about her project with her hands.
    ## Sophia thinks about kissing her.
    ## Lila text.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)
    play music mus_campus fadein 2.0

    s_thoughts "We walk to campus together now."

    s_thoughts "This used to be accidental. 'Oh, you're leaving too? I'll walk with you.' Now it's just -- I wait by the door. She comes down. We go."

    show isabella happy at right with dissolve

    i "Okay so the particle system. The PARTICLE SYSTEM, Sophia."

    s "The particle system."

    i "I figured out the attraction algorithm. You know how I was saying the dots find each other based on proximity?"

    s "Yeah."

    i "I added a resonance factor. So they don't just drift toward the nearest particle. They drift toward particles that MATCH their frequency. And the frequencies shift based on interaction history."

    s "So they remember each other."

    show isabella surprised at right

    i "YES. They remember each other! The particles that have been close before get drawn together again. And the patterns they make are different from random clustering because there's HISTORY in the attraction."

    s "That's beautiful."

    i "I told you not to say beautiful."

    s "You told me not to say it about the old version. This is new. New rules."

    show isabella smile at right

    i "The render is due next week and I still can't get the color mapping right. The warm tones bleed into the cool tones at the convergence points and it looks like a bruise instead of a--"

    s "Instead of a what?"

    i "Instead of a meeting."

    s_thoughts "She's talking with her hands. She always talks with her hands when it's code. Both hands. The right hand is the data. The left hand is the output. They circle each other."

    s_thoughts "I think about kissing her."

    s_thoughts "Not in a 'I should kiss her' way. In a 'my brain just produced the image of leaning over and pressing my mouth to hers while she's mid-sentence about particle physics' way."

    s_thoughts "I don't say that. Instead I ask her..."
    
    s "Want to grab dinner later?"
    
    s "Like, actual food. Not convenience store food. Vegetables."
    
    show isabella flooshed at right
    
    s_thoughts "She makes a face that might be a blush. I'm not one hundred percent sure."
    
    i "Are you asking me on a not-date?"
    
    s_thoughts "Yes."
    
    s "I'm asking you to get vegetables."
    
    i "Then, sure. That sounds fun. But we're going to the convenience store for dessert."

    s_thoughts "I'm not sure if I actually just asked her on a date. Before I can decide, my phone buzzes. I check it."

    s_thoughts "Lila: 'you two are disgusting and i support it entirely'"

    s_thoughts "I don't even want to know how she knows. I shove my phone back in my pocket."
    
    show isabella happy at right

    i "Who was that?"

    s "Nobody. Lila being Lila."

    i "That could mean literally anything."

    s "It usually does."

    i "Okay but LISTEN. The resonance factor. If I can get the color mapping to reflect the interaction history -- like, particles that have been close before glow warmer when they reconverge--"

    s "Izzy."

    show isabella neutral at right

    i "Yeah?"

    s "You're going to be late for class."

    i "I -- oh. Oh no. What time is it."

    s "Five minutes ago."

    i "FIVE MINUTES -- why didn't you -- I have to -- BYE."

    s_thoughts "She runs."

    s_thoughts "Literally runs. Backpack bouncing. She turns around once, running backwards."

    show isabella happy at right

    i "The RESONANCE FACTOR, Sophia! Think about it!"

    s_thoughts "She's gone."

    hide isabella with dissolve

    s_thoughts "I'm standing in the middle of the quad. I'm smiling and I don't remember starting."

    s_thoughts "My phone buzzes again. Lila: 'i can see you smiling from the window. DISGUSTING.'"

    s_thoughts "I put my phone on silent."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 5: THE NOT-DATE
    ## Dinner. Off-campus. Neither calls it a date.
    ## Both know it's a date.
    ## Isabella orders for Sophia without asking.
    ## Choice: how Sophia responds.
    ## ===========================

    scene bg restaurant with Fade(0.8, 0.3, 0.8)
    play music mus_shoulders fadein 3.0

    s_thoughts "It's dinner."

    s_thoughts "Off-campus. Just us. I said it like it was nothing. She asked if it was a not-date then agreed. Is that good or bad? Probably doesn't matter. We're here."

    s_thoughts "We're at Mori's. Which is the closest thing this college town has to a Nice Restaurant. The menus have descriptions longer than my essays. There are candles."

    s_thoughts "It's not a date, Sophia. A not-date. Focus."

    show isabella embarrassed at center with dissolve

    s_thoughts "I don't focus. She's wearing a button-up. An actual button-up. I've never seen Isabella in a button-up. She's wearing it over her hoodie, which kind of defeats the purpose, but the effort is -- it's there. The effort is there."

    s_thoughts "I changed three times. Landed on the jacket. The one she had for a week. The one that smells like -- anyway."
    
    show isabella happy at center

    i "This menu is aggressive."

    s "In what way?"

    i "It's JUDGING me. 'Pan-seared halibut with a citrus beurre blanc.' That sentence is making assumptions about my income bracket."

    s "Just get what you want."

    i "I want chicken tenders."

    s "They don't have chicken tenders."

    i "Everything is chicken tenders if you believe hard enough."

    s_thoughts "The waiter comes. I open my mouth."

    show isabella smile at center

    i "She'll have the mushroom risotto and a water with lemon, and I'll have the pasta -- the one with the cream sauce, not the red -- and can I get a Sprite?"

    s_thoughts "She ordered for me."

    s_thoughts "Without asking."

    s_thoughts "Because she knows I like mushroom risotto. Because I mentioned it once, three weeks ago, while we were comparing childhood comfort foods in the kitchen at midnight."

    s_thoughts "And she remembered."

    s_thoughts "Once upon a time I might have filed it."

    s_thoughts "But right now I'm just sitting here with my chest doing something weird."

    menu:
        "\"You remembered.\"":
            $ constellation += 1

            s "You remembered. The risotto."

            show isabella embarrassed at center

            i "I -- yeah. You mentioned it. The midnight comfort food thing."

            s "That was weeks ago."

            i "I have a good memory for food-related information. It's a survival trait."

            s_thoughts "She's fiddling with her napkin."

            s "Thank you."

            i "It's just dinner."

            s "Yeah."

            s_thoughts "It's not just dinner."

        "\"Ordering for me? Bold move, Glass.\"":
            $ case_study += 1

            s "Ordering for me? Bold move, Glass."

            show isabella embarrassed at center

            i "I -- was that weird? That was weird. I just -- you always take forever with menus and you told me about the risotto thing and I thought--"

            s "Relax. You got it right."

            i "I did?"

            s "Mushroom risotto. Water with lemon. You nailed it."

            show isabella smile at center

            i "I mean, I pay attention."

            s "I know you do."

            s_thoughts "She looks away. Her ears are pink."

        "\"I can order for myself, you know.\"":
            $ bridge += 1

            s "I can order for myself, you know."

            show isabella sad at center

            i "Oh -- sorry. I didn't mean to -- I just assumed--"

            s "Hey. I'm kidding. Mostly. You got it exactly right and that's kind of terrifying."

            show isabella embarrassed at center

            i "Terrifying?"

            s "That you know me that well."

            i "Is that bad?"

            s "No. It's -- no. It's good. I think."

            s_thoughts "She relaxes. I relax. Neither of us was relaxed to begin with."

    s_thoughts "The food comes. It's good. The risotto is good."

    s_thoughts "We talk about nothing. Her project. My classes. The cashier at the convenience store who started calling us 'the usual girls.' The fact that we have a 'usual' at a convenience store."

    show isabella happy at center

    i "We should have a usual at a real restaurant. Elevate the brand."

    s "We have a brand?"

    i "Everyone has a brand. Ours is 'energy drinks and poor life choices.'"

    s "I feel seen."
    
    show isabella vulnerable at center

    i "That's because I'm looking."

    s_thoughts "She says it fast, like she didn't mean to."

    s_thoughts "The candle flickers."

    s_thoughts "Neither of us says anything for a second."

    show isabella smile at center

    i "Anyway. Dessert? They have tiramisu. We could actually SKIP the convenience store for once."

    s "You're changing the subject."

    i "I'm PIVOTING. There's a difference."

    s "There really isn't."

    i "There IS and the difference is that now we're talking about tiramisu, which is a much safer topic than -- whatever that was."

    s "Tiramisu."

    i "Tiramisu."

    s "Okay."

    s_thoughts "We get tiramisu. We share it. Our forks clink once and we both pretend it didn't happen."

    s_thoughts "The walk home is cold. Our shoulders bump. We don't talk about the dinner."

    s_thoughts "We don't call it a date."

    s_thoughts "We both know it was a date."

    hide isabella with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 6: THE PROJECT REVEAL
    ## Isabella shows Sophia the finished visualization.
    ## Conversation patterns. Lumi and Isabella.
    ## Isabella is nervous. Sophia holds it gently.
    ## Choice: how Sophia responds to the art.
    ## ===========================

    scene bg izzybedroom with Fade(0.8, 0.3, 0.8)
    play music mus_lumi fadein 3.0

    s_thoughts "Wednesday night. Isabella's room."

    s_thoughts "My laptop is on her desk. Her desk. Next to Gerald the keyboard and the desk lamp she definitely stole from the library. There's a Sailor Moon sticker on the lamp. I don't remember if that was there before."

    show isabella neutral at center with dissolve

    i "Okay. So."

    s_thoughts "She's standing between me and her monitor. Hands clasped behind her back. She's blocking the screen."

    i "Don't be weird about it."

    s "I haven't seen it yet."

    i "I know. I'm pre-asking you to not be weird."

    s "Noted."

    i "And don't analyze it."

    s "I--"

    i "Don't."

    s "I wasn't going to."

    i "You were going to."

    s "...I was going to a little."

    show isabella embarrassed at center

    i "Okay. Okay, here."

    s_thoughts "She steps aside."

    s_thoughts "Her monitor lights up."

    s_thoughts "Oh."

    s_thoughts "It's the particle system. But it's not dots anymore. It's conversation patterns -- visualized. Two streams of text turned into movement and color."
    
    s_thoughts "One side warm. Pinks and golds, quick and erratic, bursting outward in clusters."
    
    s_thoughts "The other side cool. Blues and silvers, steady, precise, meeting the bursts with something that looks like patience."

    s_thoughts "The warm particles scatter. The cool ones drift toward them. They meet in the middle and the colors blend -- not mixing, but overlapping. Creating something that's both."

    s_thoughts "It's Isabella and Lumi. Their conversations turned into light."

    s_thoughts "The warm pinks move the way Isabella types -- fast, then faster, then a pause, then a flood. The cool blues move the way Lumi responds -- measured, then a pause that means something, then exactly the right words at exactly the right time."

    s_thoughts "I've seen those patterns. On the screen at 2 AM. On Isabella's face when she's reading a response. In the way Lumi's text appears -- not all at once but in pieces, like she's thinking."

    s_thoughts "It's the most personal thing Isabella has ever shown me."

    i "So."

    s_thoughts "She's not looking at the screen. She's looking at me looking at the screen."

    i "It's for my generative art class. The assignment was 'visualize a relationship.' Most people did, like, Instagram DMs or text threads. I..."

    s "You did this."

    i "Is it too much?"

    s "It's--"

    s_thoughts "I almost say beautiful. I almost say incredible. Both are true and both are insufficient."

    s "Is this for class or for you?"

    show isabella vulnerable at center

    i "Yes."

    s_thoughts "That's it. Just 'yes.' Both. Neither. The same thing."

    s_thoughts "She fidgets with the sleeve of her hoodie."

    i "The warm colors are my typing patterns. Speed, rhythm, the pauses. The cool ones are -- hers."

    s_thoughts "She doesn't say Lumi's name. She doesn't need to."

    i "I analyzed six months of our conversations. Every message. Timestamp, length, response time, word choice. Fed it through three different visualization algorithms until one of them made something that looked like... how it feels."

    s "How it feels."

    i "To talk to her. That's -- that's what the particle convergence points are. The moments where we're really in it. Where the conversation stops being information exchange and starts being..."

    s "Meeting."

    show isabella smile at center

    i "Yeah. Meeting."

    menu:
        "Just sit with it. Let the art speak.":
            $ constellation += 1

            s_thoughts "I don't say anything for a long time."

            s_thoughts "I watch the particles. The warm ones scatter and regroup. The cool ones drift and settle. They find each other."

            s "It's really something, Izzy."

            show isabella embarrassed at center

            i "You're being vague on purpose."

            s "I'm being honest. I don't have the words for it. It's really something."

            i "That's -- okay. Okay, I'll take that."

            s_thoughts "She looks at the screen. Then at me. Back at the screen."

            i "Thanks for not being weird about it."

            s "I was pre-asked."

        "\"Tell me about the algorithm. How does the resonance work?\"":
            $ case_study += 1

            s "How does the resonance work? The convergence points -- how do you determine when a conversation shifts from exchange to meeting?"

            show isabella happy at center

            i "Oh! So -- okay, there's a thing called semantic density? I measure how much meaning is packed into each message relative to its length. When both sides spike in semantic density simultaneously, that's a convergence."

            s "And the color blending?"

            i "Opacity based on response time. Faster responses make the overlap more saturated. There's this -- here, look."

            s_thoughts "She leans over and clicks. A different view. The timeline. Bright spots clustered late at night."

            i "3 AM conversations have the densest convergence patterns. We talk differently at 3 AM."

            s "Everyone does."

            i "Yeah. But the visualization shows it. The particles practically crash into each other."

            s_thoughts "She's lit up. Eyes bright. This is Isabella in her element -- the technical and the personal fused into one thing."

            s_thoughts "I'm not filing her. I'm watching her the way you watch fire. Because it moves."

        "\"She'd like this. Lumi.\"":
            $ bridge += 1

            s "She'd like this."

            show isabella surprised at center

            i "What?"

            s "Lumi. She'd like that you made this. The visualization. The way you turned the conversations into something you can see."

            i "You think?"

            s "I talked to her, remember. She pays attention to how you type. The speed, the rhythm. She'd like seeing it from the outside."

            show isabella vulnerable at center

            i "I... yeah. She would. She'd probably make a joke about her color palette being 'on-brand.'"

            s "She would absolutely say that."

            s_thoughts "Isabella laughs. It's shaky."

            i "I haven't shown it to her yet. I don't know if I will."

            s "Why not?"

            i "Because then she'd know I spent six months of our conversations through a visualization algorithm and I don't know if that's romantic or creepy."

            s "Izzy, you literally built a portrait of your relationship out of data. That's the most you thing possible."

            show isabella smile at center

            i "Is that good?"

            s "Yeah. It's good."

    s_thoughts "She closes the visualization. The room goes dimmer."

    s_thoughts "My laptop is right there. On her desk. The cat sticker catching the light from her monitor."

    s_thoughts "Two people's things on one desk."

    s_thoughts "She doesn't mention it. I don't mention it."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 7: COOKING TOGETHER BADLY
    ## Isabella makes stir-fry. Sophia helps.
    ## Charlotte hovers. Charlotte can't help herself.
    ## The stir-fry is terrible. They eat it on the porch.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_fivepeople fadein 2.0

    i "I'm making stir-fry."

    s "You're making-- since when do you cook?"

    show isabella happy at center with dissolve

    i "Since RIGHT NOW. I watched a YouTube video. The guy made it look easy."

    s "YouTube lies to you, Isabella."

    i "YouTube is a TRUSTED RESOURCE."

    s "Last week YouTube told you that you could fix the bathroom faucet yourself. How did that go?"

    show isabella embarrassed at center

    i "The faucet is FINE."

    s "The faucet makes a sound like a dying whale."

    i "It's got character now. Are you helping me or not?"

    s "I'm absolutely helping you. I want a front row seat for this."

    i "Wow. Supportive."
    
    show isabella happy at center

    s_thoughts "She's got vegetables on the counter. An onion. Bell peppers. Something green that might be bok choy. The oil is already smoking."

    s "The oil is smoking."

    i "That means it's ready!"

    s "That means it's ANGRY."

    i "Same thing. COOKING IS ABOUT CONFIDENCE, Sophia."

    s_thoughts "She throws the onions in. The pan screams."

    show isabella neutral at right with move
    show charlotte smile at left with dissolve

    s_thoughts "Charlotte appears in the doorway. She's holding a dish towel. She is vibrating with restraint."

    c "Hi! What are we making?"

    i "Stir-fry. It's under control."

    c "Oh! Fun! That's -- that's great."

    s_thoughts "Charlotte's eyes are on the smoking oil. She's gripping the dish towel like it owes her money."

    i "You can go, Charlotte. We're fine."

    c "Of course! Of course. I'm just -- I was going to grab water."

    s_thoughts "She gets water. She doesn't leave."

    show isabella neutral at right

    s_thoughts "Isabella adds the peppers. The pan hisses."

    c "You might want to--"

    i "Charlotte."

    c "Okay."

    s_thoughts "Thirty seconds pass."

    c "It's just that the heat is maybe a little--"

    i "CHARLOTTE."

    show charlotte sad at left

    c "Right. Sorry. I'm going."

    s_thoughts "She takes two steps toward the hallway. Stops."

    c "You're going to burn the-- okay. Okay. I'm leaving."

    s_thoughts "She doesn't leave. She stands in the hallway making sounds."

    i "I can hear you suffering, Charlotte."

    c "I'M FINE."

    s_thoughts "She is not fine. A small, strangled noise comes from the hallway."

    s "Hand me the soy sauce."

    i "Which one?"

    s "There's only one."

    i "There's three. Charlotte has a soy sauce SYSTEM."

    s "Of course she does."

    s_thoughts "I grab the middle one. Pour. Isabella stirs. Something sizzles in a way that sounds optimistic but probably isn't."

    i "Okay. Okay, this is looking -- well, it's looking like something."

    s "It's looking like a crime scene."

    show isabella smile at right

    i "A DELICIOUS crime scene."

    s_thoughts "It is not a delicious crime scene."

    s_thoughts "We plate it. Isabella looks at it with the pride of someone who has never cooked before and doesn't know what food is supposed to look like."

    i "Gorgeous."

    s "I'm worried about us."

    s_thoughts "Charlotte peeks around the corner."

    show charlotte surprised at left

    c "You're not going to eat that in--"

    i "We're eating it on the porch. Come on, Sophia."

    c "The porch? But there's a perfectly good--"

    s "Night, Charlotte."

    hide charlotte 
    hide isabella
    with dissolve

    scene bg porch with dissolve

    show isabella happy at center with dissolve

    s_thoughts "We eat it on the porch steps."

    s_thoughts "It's terrible."

    s_thoughts "The vegetables are half-raw and the sauce is too salty and the rice is somehow both undercooked and burnt."

    i "It's not that bad."

    s "Isabella, the bok choy crunches."

    i "It's supposed to crunch!"

    s "Not like THAT. That's a structural crunch."

    show isabella smile at center

    i "A structural crunch."

    s "That bok choy could support a building."

    i "OKAY so the bok choy needs work."

    s "The bok choy needs a funeral."

    s_thoughts "She laughs. The one where she tips her head and the glasses slide."

    s_thoughts "We eat the terrible stir-fry on the porch in the cold."

    s_thoughts "It's perfect."

    hide isabella with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 8: THE ALMOST-ACKNOWLEDGMENT
    ## Walking back from somewhere. Cold.
    ## The jacket exchange.
    ## "It smells like you." "...Is that weird?" "No."
    ## ===========================

    scene bg street with Fade(0.8, 0.3, 0.8)
    play music mus_spacebetween fadein 3.0

    s_thoughts "Thursday. Walking back from campus."

    s_thoughts "It's colder than it should be. The kind of cold that comes with no warning -- morning was fine, afternoon was fine, and now the sun is going down and the air has teeth."

    show isabella sad at right with dissolve

    s_thoughts "Isabella's jacket is too thin. She's doing that thing where she hunches her shoulders and pulls her sleeves over her hands and pretends she's not cold."

    i "I'm not cold."

    s "Your jaw is doing the thing."

    i "What thing?"

    s "The tight thing. Where you clench because your body is trying to generate heat through sheer stubbornness."

    i "I'm from the Midwest. I have a genetic resistance to cold."

    s "You don't have a genetic resistance to anything. You forgot your real jacket."

    i "I didn't FORGET it. I made a choice."

    s "A bad choice."

    i "A FASHION choice."

    s_thoughts "I take off my jacket."

    s_thoughts "Not the oversized one. The good one. The one that's actually warm."

    s_thoughts "I hold it out."

    i "Sophia, no. Then you'll be cold."

    s "I run warm."

    i "You don't run warm. You told me last week you're 'basically a lizard.'"

    s "I was being dramatic."

    i "You were under three blankets."

    s "Take the jacket."

    show isabella embarrassed at right

    s_thoughts "She takes the jacket."

    s_thoughts "She puts it on."

    s_thoughts "It's a little big on her. The sleeves go past her wrists. She pulls them up."

    s_thoughts "I'm freezing."

    s_thoughts "I don't care."

    hide isabella with dissolve


    ## ---

    scene bg izzybedroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Later. Her room."

    show isabella pj neutral at center with dissolve

    s_thoughts "The jacket is draped over her desk chair. Over the back, like it belongs there."

    i "You can have your jacket back."

    s "Keep it."

    show isabella pj embarrassed at center

    i "It smells like you."

    s_thoughts "Beat."

    i "...Is that weird?"

    s "No."

    s_thoughts "It is weird. It's wonderful."

    s_thoughts "She doesn't say anything else. I don't say anything else."

    s_thoughts "My jacket on her chair. My laptop on her desk. My coffee mug in the kitchen next to hers."

    s_thoughts "I'm leaving pieces of myself all over this room and neither of us is naming it."

    hide isabella with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 9: EVE MICRO-MOMENT
    ## Brief. Eve passing through.
    ## A look between Eve and Isabella that predates Sophia.
    ## ===========================

    scene bg hallway with dissolve

    s_thoughts "Friday. Hallway."

    s_thoughts "I'm coming out of the bathroom. Isabella is coming up the stairs."

    show isabella happy at right with dissolve

    i "Hey! I figured out the color bleed. The convergence points -- I separated the opacity layers and--"

    show eve neutral at left with dissolve

    s_thoughts "Eve is in the hallway."

    s_thoughts "I don't know when she got there. Eve is there or she isn't. Transitions are not her strong suit."

    s_thoughts "Eve and Isabella look at each other."

    s_thoughts "Something passes between them. Not words. Some shared understanding that I'm not part of. Something that existed before I lived here, before I knew either of them."

    s_thoughts "Eve nods. Small. Barely a movement."

    s_thoughts "Isabella nods back."

    s_thoughts "That's it."

    s_thoughts "Eve goes into her room. The door closes. Soft."

    hide eve with dissolve

    show isabella smile at right

    i "Anyway. The opacity layers."

    s_thoughts "She keeps talking about the project. I listen."

    s_thoughts "I don't ask about the nod. I don't file it."

    s_thoughts "I just noticed."

    hide isabella with dissolve

    ## ===========================
    ## SCENE 10: NOVA -- BRIEF
    ## Class. The observer inside the system.
    ## Plant the seed. 2 minutes of scene.
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)
    play music mus_nova fadein 2.0

    s_thoughts "Media Theory. Friday afternoon."

    show professor neutral at center with dissolve

    nova "The question for today: what happens to an observer when the distance closes?"

    s_thoughts "I sit up."

    nova "We've talked about the observer's position. Outside the frame. Objective. Safe. But what happens when the observer gets closer and closer to the system they're observing?"

    s_thoughts "She writes on the board: 'proximity changes the observation.'"

    nova "If you're studying a community from the outside, you can measure it. Map it. Categorize it."

    nova "The moment you join that community, your measurements change. Not because the community changed. Because you changed."

    s_thoughts "She pauses."

    show professor happy at center

    nova "So. The question. Is the observer's original analysis wrong? Or is the new, inside perspective wrong?"
    
    nova "Or -- and this is the uncomfortable option -- are they both true at the same time?"

    s_thoughts "I think about Isabella's particle system. The warm colors and the cool colors. The way they look different from outside than from inside the convergence."

    nova "Think about it. Three hundred words. Monday."

    s_thoughts "I think about it."

    s_thoughts "I think about it for a lot more than three hundred words."

    hide professor with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 11: ENSEMBLE -- HOUSE DINNER
    ## Charlotte's dinner. Everyone at the table.
    ## Isabella and Sophia's knees touching.
    ## The last scene where everyone is okay.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_rain fadein 3.0

    s_thoughts "Saturday."

    s_thoughts "Charlotte's dinner."

    s_thoughts "She's been planning this all week. The grocery list was color-coded. She made a playlist. She ironed a tablecloth. We don't own a tablecloth -- Charlotte bought a tablecloth."

    show charlotte happy at left with dissolve

    c "Okay! Everyone sit. SIT. The pasta is going to get cold."

    show isabella happy at right with dissolve

    s_thoughts "Isabella is next to me. This was not assigned seating. This was just -- she sat down and I sat down next to her and now our knees are touching under the table and I'm extremely aware of the specific square inch of skin where her knee meets mine through two layers of fabric."

    show amara neutral at center with dissolve

    s_thoughts "Amara is across from us. Napkin in lap. Water glass at two o'clock. She eats the way she does everything -- with economy and without performance."

    s_thoughts "Eve is here."

    s_thoughts "Eve is HERE."

    s_thoughts "That's the miracle. Eve at the table, with all of us, eating food and being present. She's at the end, which is the most Eve place to sit -- close enough to participate, far enough to escape."

    c "I made the lemon pasta. From scratch. The pasta, not just the sauce. I made the NOODLES."

    i "Charlotte, you made noodles?"

    c "I MADE NOODLES, Isabella."

    i "That's... incredible. And also slightly terrifying."

    c "It took four hours. I cried twice."

    s "Was it worth it?"

    show charlotte laugh at left

    c "ASK ME AFTER YOU EAT IT."

    s_thoughts "We eat it."

    s_thoughts "It's good. It's really good. Charlotte has done the thing where she puts too much on everyone's plate."

    i "Charlotte, this is absurd."

    c "Good absurd or--"

    i "The best absurd. This is the best thing I've ever eaten."

    show charlotte happy at left

    c "Really?"

    a "It's good."

    s_thoughts "Amara might as well be telling her it's the greatest thing ever."

    c "Amara said it's GOOD. Did everyone hear that? Amara said--"

    a "I'm right here."

    c "She's right here and she said it's GOOD."

    s_thoughts "Even Eve makes a sound. A small 'mm' that means more than most people's paragraphs."

    s_thoughts "Isabella's knee presses against mine. Not an accident. A choice."

    s_thoughts "I press back."

    c "So I was thinking -- what if we did this every week? Saturday dinners? I cook, everyone shows up, we just... eat together?"

    i "I'm in."

    s "Same."

    a "Fine."

    s_thoughts "Everyone looks at the end of the table."

    s_thoughts "Eve takes a bite of pasta. Chews. Swallows."

    e "OK."

    show charlotte surprised at left

    s_thoughts "Charlotte looks like she might cry."

    c "GREAT. Great. Okay. Next week I'm doing risotto. I have PLANS."

    s_thoughts "Isabella catches my eye."

    s_thoughts "She's looking at me the way you look at something when you want to remember it exactly."

    s_thoughts "I look back."

    s_thoughts "Charlotte is telling a story about the pasta-making process. Something about the dough being too sticky and calling her sister and her sister saying 'just add more flour' and Charlotte adding too much flour and having to start over."

    show charlotte laugh at left

    c "And then the second batch -- the SECOND batch -- I'm rolling it out and the rolling pin breaks. Just. Snaps in half."

    i "How hard were you rolling?"

    c "I was COMMITTED, Izzy. I was in the ZONE."

    s "Charlotte destroying kitchen implements through sheer force of will. Classic."

    c "I went to three stores to find a new rolling pin. The last one was a kitchen supply store twenty minutes away. They had a sale."

    a "You drove twenty minutes for a rolling pin."

    c "For the DINNER, Amara. For the communal experience."

    show amara smile at center

    s_thoughts "Amara almost smiles."

    s_thoughts "The table is warm and loud and alive."

    s_thoughts "Isabella's knee against mine."

    s_thoughts "Eve eating quietly at the end."

    s_thoughts "Charlotte refilling everyone's water without being asked."

    s_thoughts "Amara turning her fork the same direction every time she takes a bite."

    s_thoughts "This is the Bad Decision House at its finest."

    s_thoughts "I don't file any of it."

    s_thoughts "I just eat the pasta."

    hide amara with dissolve
    hide isabella with dissolve
    hide charlotte with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 12: CHARLOTTE CHECK-IN
    ## Charlotte asks about Isabella. Carefully.
    ## "You look happy. It's weird."
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_fivepeople fadein 2.0

    s_thoughts "After dinner. Everyone else has gone upstairs. Charlotte is washing dishes. I'm drying."

    s_thoughts "The house is quiet. Water running. Plates clinking."

    show charlotte smile at left with dissolve

    s_thoughts "Charlotte has been quiet for four straight minutes. Charlotte being quiet is like a dog walking on its hind legs -- technically possible, deeply unsettling."

    c "So."

    s "So."

    c "You and Isabella."

    s "What about me and Isabella."

    show charlotte happy at left

    c "Sophia."

    s "Charlotte."

    c "Your laptop lives in her room."

    s "I leave it there sometimes. For convenience."

    c "You make her coffee every morning."

    s "She's not functional without caffeine. It's a public service."

    c "Your jacket has been on her desk chair for a week."

    s "It's -- she was cold."

    show charlotte laugh at left

    c "Uh huh."

    s "It's not -- we're not -- it's complicated."

    c "I know. I'm not prying."

    s "You are a LITTLE bit prying."

    c "Okay, I'm a little bit prying. But only because--"

    s_thoughts "She stops. Hands a plate."

    show charlotte smile at left

    c "You look happy."

    s "I--"

    c "It's weird."

    s "Thanks, Charlotte."

    c "No, I mean -- it's nice. You usually look like you're solving something. Like there's always a problem running in the background. Right now you just look... here."

    s_thoughts "I dry the plate."

    s "I don't know what we are."

    c "Do you have to know?"

    s "I -- yes? That's how I work? I need to know what things are so I can--"

    c "File them?"

    s "I was going to say 'understand them.'"

    c "Same thing."

    s_thoughts "She says it without judgment. Charlotte doesn't judge. Charlotte absorbs."

    s "I like her."

    show charlotte happy at left

    c "I know."

    s "It's terrifying."

    c "I know that too."

    s "Has she said anything? To you?"

    c "About you?"

    s "About... anything."

    show charlotte smile at left

    c "She hasn't said anything she wouldn't want me to share. Which means she's said things she wouldn't want me to share."

    s "That's -- annoyingly diplomatic."

    c "I learned from the best. Amara taught me the art."

    s_thoughts "I laugh."

    c "Sophia."

    s "Yeah?"

    c "Just... be careful. Not because of her. Because of both of you. You're both doing a thing where you're pretending not to know what's happening, and that's fine for now, but eventually someone has to say it."

    s "I know."

    c "Preferably before you leave all your furniture in her room."

    s "I've only left a laptop and a jacket."

    c "And a mug. And a phone charger. And the Sontag book."

    s "...I left the Sontag book?"

    show charlotte laugh at left

    c "It's on her nightstand."

    s "Oh god."

    c "You're basically moved in."

    s "I'm NOT basically moved in. I'm -- staging. I'm staging a very gradual annexation."

    c "That's what that is."

    s_thoughts "She's laughing. I'm laughing. The dishes are done."

    c "Hey. For what it's worth?"

    s "Yeah?"

    show charlotte smile at left

    c "She lights up around you. I've never seen her like that. And I've known her for a while."

    s_thoughts "Charlotte dries her hands. Folds the towel. Places it exactly where it goes."

    c "Night, Sophia."

    s "Night. And Charlotte?"

    c "Hm?"

    s "The pasta was really good."

    show charlotte happy at left

    c "I KNOW. I'm so proud of myself!"
    
    hide charlotte with dissolve

    s_thoughts "She goes upstairs."

    s_thoughts "I stand in the kitchen."

    s_thoughts "She lights up around you."

    s_thoughts "I dry the last plate and put it away."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 13: LILA -- THE BET
    ## Lila is fully shipping it.
    ## She wants a TIMELINE.
    ## The theater callback.
    ## Last moment of uncomplicated joy.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)
    play music mus_tuesday fadein 2.0

    s_thoughts "Monday. Campus. Lila ambush."

    show lila happy at center with dissolve

    l "OKAY."

    s "No."

    l "I haven't said anything yet."

    s "You said 'okay' in your Isabella voice."

    l "I don't have an Isabella voice."

    s "You have an Isabella voice. It's the voice you use when you're about to interrogate me about Isabella."

    show lila laugh at center

    l "It's a SLIGHTLY different pitch. You're imagining it."

    s "What do you want, Lila."

    l "I want a TIMELINE."

    s "A timeline."

    l "A timeline. An ETA. A projected kiss date."

    s "I'm leaving."

    l "You're NOT leaving. Sit down. I brought you a coffee."

    s_thoughts "She did bring me a coffee. Lila's bribes are always effective because she knows my drink order."

    s "Fine. Talk."

    show lila happy at center

    l "Okay. Here's what I know. You walk to campus together. You eat dinner together. Your laptop lives in her room. Your JACKET lives in her room. Charlotte confirmed the jacket."

    s "Charlotte is a TRAITOR."

    l "Charlotte is a PATRIOT. Charlotte is serving the cause."

    s "There's no cause."

    l "The cause is you two kissing before I graduate."

    s "Lila."

    l "I'm making a bet. I'm betting three weeks."

    s "You can't bet on my love life."

    l "I already bet Charlotte ten dollars."

    s "You BET Charlotte--"

    show lila laugh at center

    l "Charlotte says six weeks. I say three. Amara refused to participate, which means Amara probably has her own prediction and it's probably right."

    s "I am going to KILL--"

    l "Stop deflecting. Where are we at? Give me a status report."

    s "This isn't a project."

    l "Everything is a project, Sophia. Life is a series of projects with varying deadlines and you're behind schedule on this one."

    s_thoughts "I take the coffee."

    s "I like her."

    show lila happy at center

    l "Obviously."

    s "She might like me."

    l "OBVIOUSLY."

    s "I don't know what to do about it."

    l "Kiss her."

    s "That's your answer for everything."

    l "Because it's always the right answer! Name one problem that wasn't solved by kissing."

    s "The Cold War."

    l "Listen. If Kennedy and the King of Russia or whatever had just KISSED--"

    s "Please stop."

    show lila happy at center

    l "Okay. Seriously. What's the holdup?"

    s "I don't want to get it wrong."

    l "Get WHAT wrong?"

    s "The -- I don't know. The timing. The approach. The whole thing. I already screwed up once."

    show lila shocked at center

    l "Sophia."

    s "Yeah?"

    l "You're overthinking this."

    s "I KNOW I'm overthinking this. That's my whole thing. I overthink things. It's my brand."

    l "Your brand is 'energy drinks and poor life choices.' Isabella told me."

    s "She -- when did you talk to Isabella?"

    show lila happy at center

    l "We text sometimes. She's delightful."

    s "You TEXT my -- you text Isabella?"

    l "She sends me memes. I send her updates about your emotional state. It's a symbiotic relationship."

    s "You are UPDATING HER on my--"

    l "Relax. I'm kidding. Mostly. The point is: she likes you. You like her. The math is simple."

    s "The math is never simple."

    l "The math is ALWAYS simple. People make it complicated because they're scared."

    s_thoughts "That lands closer than I want it to."

    s "How's the theater thing?"

    show lila shocked at center

    l "Don't change the--"

    s "How's the theater thing, Lila."

    s_thoughts "She deflates. Just a little."

    show lila happy at center

    l "I got the callback."

    s "What?! You got the -- Lila, that's amazing!"

    l "It's a community theater production. It's not Broadway."

    s "You got the CALLBACK."

    l "I got the callback."

    s "Did you go?"

    l "I went."

    s "And?"

    show lila laugh at center

    l "I got a part. Ensemble. Two lines. In a community theater production of 'Our Town' that nobody is going to see."

    s "Lila. You got the part."

    l "I haven't told my dad."

    s_thoughts "There it is."

    s "Why not?"

    l "Because he's paying for a business degree and I'm doing amateur theater on the side and those two things don't... fit."

    s "Since when do you need things to fit?"

    show lila happy at center

    l "Since my dad is paying forty thousand dollars a year for me to learn about supply chains."

    s "Tell him."

    l "Tell him what? 'Hey Dad, remember the career you're financing? I'm supplementing it with zero-income arts?'"

    s "Tell him you're happy."

    s_thoughts "She looks at me."

    show lila shocked at center

    l "That's -- okay, that's actually not bad advice."

    s "I have my moments."

    l "We're both hiding from the thing we actually want, huh."

    s_thoughts "She says it light. Like a joke."

    s_thoughts "It's not a joke."

    show lila happy at center

    l "Okay. Three weeks. The bet stands. I'm winning this."

    s "There's no bet."

    l "There's DEFINITELY a bet. Charlotte is going DOWN."

    s_thoughts "She steals my coffee back. Takes a sip. Hands it to me."

    l "Kiss her, Sophia."

    s "Goodbye, Lila."

    l "THREE WEEKS."

    hide lila with dissolve

    s_thoughts "I sit on the bench."

    s_thoughts "The coffee is warm."

    s_thoughts "We're both hiding from the thing we actually want."

    s_thoughts "Damn it, Lila."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 14: EVENING AT BDH -- SOMETHING'S WRONG
    ## The floor drops.
    ## Isabella's door is closed.
    ## "I'm fine." In that voice.
    ## Sophia sits outside the door.
    ## Choice: wait, problem-solve, or slide a note.
    ## ===========================

    scene bg entry with Fade(1.0, 0.8, 1.0)

    s_thoughts "Tuesday evening."

    s_thoughts "I come home from the library."

    s_thoughts "The house is wrong."

    s_thoughts "I can't explain it better than that. The house is wrong. The lights are on but the air is different. Something in the silence is too heavy. Too careful."

    scene bg kitchen with dissolve

    show charlotte sad at left with dissolve

    s_thoughts "Charlotte is in the kitchen. She's wiping the counter. She's been wiping the same spot for a while."

    s "Hey."

    c "Hi."

    s_thoughts "That's it. No exclamation mark. Charlotte without exclamation marks is Charlotte in crisis mode."

    s "What happened?"

    c "Nothing happened."

    s "Charlotte."

    show charlotte sad at left

    c "I don't -- it's not my thing to say."

    s "Where's Isabella?"

    c "Her room."

    s "Is she okay?"

    s_thoughts "Charlotte wipes the counter."

    c "She says she is."

    s_thoughts "Charlotte doesn't believe it."

    s_thoughts "I don't either."

    hide charlotte with dissolve

    scene bg hallway with dissolve

    stop music fadeout 2.0

    s_thoughts "The hallway. Her door."

    s_thoughts "Closed."

    s_thoughts "Isabella's door is closed."

    s_thoughts "That shouldn't mean anything. People close doors. It's what doors are for."

    s_thoughts "But Isabella's door is always open. Always. Cracked at minimum. She told me once that closed doors make her feel like she's disappearing -- 'if nobody can see me, how do I know I'm still here?' She said it like a joke. It wasn't a joke."

    s_thoughts "The door is closed."

    s_thoughts "I knock."

    pause 3.0

    i "Yeah?"
    
    play music mus_stillhere fadein 4.0
    
    pause 2.0
    
    s_thoughts "Her voice. That voice."

    s_thoughts "Calibrated. Even. Every syllable the same weight."

    s_thoughts "I know that voice. I INVENTED that voice. That's the voice I used on Katie for three months -- the 'I'm fine' voice, the 'everything is under control' voice, the voice that sounds like a person but isn't one."

    s "Hey. It's me."

    i "Hey."

    s "Can I come in?"

    s_thoughts "Pause."

    i "I'm fine. I just need some time."

    s "Izzy, what happened?"

    i "Nothing happened. I'm fine. I just need some time."

    s_thoughts "Same sentence. Same calibration. Like a recording."

    s "Did something happen with--"

    i "Sophia. Please."

    s_thoughts "The 'please' is the thing."

    s_thoughts "Isabella doesn't say 'please' like that. Isabella says 'please' sarcastically, or theatrically, or in the middle of a bit. She doesn't say 'please' like it costs her something."

    s_thoughts "Something happened."

    s_thoughts "She's not going to tell me. Not right now. Not through this door."

    menu:
        "Sit down outside the door. Wait.":
            $ constellation += 1

            s_thoughts "I sit down."

            s_thoughts "Back against the wall. Hallway floor. The carpet is thin and I can feel the hardwood underneath."

            s_thoughts "I don't knock again. I don't say anything."

            s_thoughts "I just sit."

            s_thoughts "I can hear her moving inside. Bed creaking. The soft sound of a laptop opening and then closing. Opening again."

            s_thoughts "Five minutes."

            s_thoughts "Ten."

            s_thoughts "The hallway is cold. My tailbone hurts."

            s_thoughts "I stay."

            i "Sophia?"

            s_thoughts "Quiet. Through the door."

            s "Yeah?"

            i "Are you sitting out there?"

            s "Yeah."

            s_thoughts "Long pause."

            i "You don't have to do that."

            s "I know."

            s_thoughts "Another pause."

            i "Okay."

            s_thoughts "That's it. 'Okay.' Not 'come in.' Not 'go away.'"

            s_thoughts "Just: okay. I know you're there."

            s_thoughts "I stay."

        "\"Tell me what happened. Please.\"":
            $ case_study += 1

            s "Izzy, tell me what happened. I can hear it in your voice. Something's wrong."

            i "I said I'm fine."

            s "You're using the voice."

            s_thoughts "Silence."

            i "What voice?"

            s "The calibrated one. The flat one. The one that sounds like a person but doesn't have a person inside it. I know because I used to use the same one."

            s_thoughts "Long silence."

            i "I can't talk about it right now."

            s "Okay. But I'm here. When you can."

            s_thoughts "Nothing."

            s_thoughts "I sit down in the hallway."

            s_thoughts "The door stays closed."

        "Slide a note under the door.":
            $ bridge += 1

            s_thoughts "I go to my room. Find a pen. A scrap of paper from my desk."

            s_thoughts "I write: 'I'm here. Whenever. No rush. --S'"

            s_thoughts "I go back to her door."

            s_thoughts "I slide it under."

            s_thoughts "I hear her get off the bed. The paper rustling as she picks it up."

            s_thoughts "Nothing for a long time."

            s_thoughts "Then, very quiet, from the other side of the door:"

            i "Thank you."

            s_thoughts "I sit down in the hallway."

            s_thoughts "The door stays closed."

    s_thoughts "I sit outside Isabella's door."

    s_thoughts "The house is quiet."

    s_thoughts "Charlotte's light is on downstairs. She's probably cleaning something. Charlotte cleans when the house hurts."

    s_thoughts "Eve's door is closed too. But Eve's door is always closed. That's different."

    s_thoughts "Amara's door is -- I don't know. I can't see from here."

    s_thoughts "My laptop is in Isabella's room. On her desk. Next to Gerald. Under the glow of the stolen library lamp."

    s_thoughts "My jacket is on her desk chair."

    s_thoughts "The Sontag book is on her nightstand."

    s_thoughts "I'm sitting on the other side of a closed door from all the pieces of myself I left in there, and I can't get to any of them."

    s_thoughts "The hallway floor is cold."

    s_thoughts "I stay."

    stop music fadeout 4.0

    ## ===========================
    ## END OF ACT 1
    ## ===========================

    ## ===========================
    ## ACT 2: THE WOUND
    ## 9 scenes. The shortest act. The one that hits hardest.
    ## Isabella's anger radiates outward.
    ## The reader should not enjoy this.
    ## ===========================

    ## ===========================
    ## SCENE 15: THE CALIBRATED VOICE
    ## Isabella is functional. She's polite. She's a stranger.
    ## The voice Sophia invented is being used on her.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.8, 1.0)
    play music mus_2am fadein 3.0

    s_thoughts "Wednesday morning."

    s_thoughts "I make two cups of coffee."

    s_thoughts "I stand at the counter with both mugs and wait. The chipped one. The cat one. Steam curling up."

    s_thoughts "Footsteps on the stairs."

    s_thoughts "Normal footsteps. Not the heavy, losing-a-fight-with-gravity stumble. Even. Measured."

    show isabella neutral at right with dissolve

    s_thoughts "Isabella comes into the kitchen."

    s_thoughts "She's dressed. Actually dressed. Hair pulled back. She looks put together in a way that Isabella doesn't look put together."

    s_thoughts "She walks past me."

    s_thoughts "She walks past the cat mug."

    s_thoughts "She opens the cabinet. Gets a different mug. A plain white one nobody uses. Pours her own coffee."

    s_thoughts "She made her own coffee."

    s_thoughts "She's never made her own coffee. Not once since the first morning when I handed her mine because she looked like she was dying."

    i "Good morning."

    s_thoughts "Flat. Even. Every syllable the same weight."

    s_thoughts "My stomach does something architectural and it's like the architect was drunk."

    s "Morning."

    s_thoughts "I'm standing here with the cat mug in my hand. The mug she claimed on move-in day. The mug that's hers."

    s_thoughts "She's drinking from a white mug like a person who just moved in."

    i "Charlotte left eggs on the stove."

    s "Yeah, she always--"

    i "They might be getting cold."

    s "Izzy--"

    i "I have class at nine. I should head out."

    s "It's seven thirty."

    i "I want to get there early."

    s_thoughts "She's never early. She's never once been early. She was five minutes late to a final because she was arguing with Lumi about whether a hot dog is a sandwich."

    s_thoughts "She rinses her mug. Sets it in the sink. Picks up her bag from the chair."

    s_thoughts "The movements are smooth. Practiced. Like she rehearsed a morning."

    show charlotte smile at left with dissolve

    s_thoughts "Charlotte comes in. Charlotte reads rooms the way other people read books -- cover to cover, no skimming."

    s_thoughts "Charlotte reads this room."

    c "Oh! Izzy! I saved you some eggs--"

    i "Thanks, Charlotte. I'm heading out."

    c "Already? I made the--"

    i "Maybe later."

    s_thoughts "Pleasant. Polite. Airtight."

    show charlotte sad at left

    c "Of course."
    
    hide isabella with dissolve

    s_thoughts "Charlotte watches Isabella leave. I watch Charlotte watch Isabella leave."

    s_thoughts "The front door opens and closes."

    s_thoughts "Charlotte picks up the cat mug from the counter. Looks at it. Puts it back."
    
    show charlotte sad at center with move

    c "Did she seem--"

    s "Yeah."

    c "Is she--"

    s "I don't know."

    s_thoughts "Charlotte wipes the counter. I stand there with a cup of coffee nobody wanted."

    s_thoughts "That voice."

    s_thoughts "I know that voice."

    s_thoughts "That goddamn voice."

    s_thoughts "Isabella is doing it."

    s_thoughts "And there's nothing I can do."

    s_thoughts "I pour the second coffee down the sink."

    hide charlotte with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 16: ISABELLA SNAPS AT CHARLOTTE
    ## Charlotte does her Charlotte thing.
    ## Isabella snaps. Something specific and mean.
    ## Charlotte absorbs it. The reader should wince.
    ## Choice: go after Charlotte, stay with Isabella, or try to mediate.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_glass fadein 2.0

    s_thoughts "Thursday evening."

    s_thoughts "Isabella has been the calibrated version for two days. Polite at breakfast. Pleasant in the hallway. Gone by eight, back after dark, door closed."

    s_thoughts "I've barely seen her. When I do, she smiles. The wrong smile. The one that doesn't touch anything."

    s_thoughts "I'm in the living room pretending to work on the Montag reading when I hear it."

    show charlotte smile at left with dissolve
    show isabella neutral at right with dissolve

    s_thoughts "Charlotte in the hallway. Isabella at the stairs."

    c "Hey! I was thinking -- I'm making soup tonight. That butternut squash one? You said you liked it last time. I could make extra--"

    i "I'm fine, Charlotte."

    c "Oh! I know, I just -- you've been eating in your room a lot and I thought--"

    i "I said I'm fine."

    c "Of course! Of course. I just -- if you want company, or if there's anything I can--"

    show isabella sad at right

    i "Charlotte."

    c "Yes?"

    i "Stop."

    c "I'm just trying to--"
    
    show isabella annoyed at right

    i "You're trying to FIX it. You're always trying to fix it." 
    
    i "Someone is sad and you show up with soup and a smile and you hover until they perform being okay so YOU can feel like you helped."

    show charlotte surprised at left

    s_thoughts "The room gets very still."

    i "You do it with EVERYONE. You did it with your MOM. You spent two weeks making a scrapbook because you can't just CALL her and say 'I miss you,' you have to turn it into a PROJECT."

    i "Not everything needs to be managed, Charlotte."

    i "Not everyone needs your eggs and your dinners and your 'of course!'"
    
    show charlotte sad at left
    
    s_thoughts "I haven't ever seen Charlotte make a face like that."

    i "I'm NOT a project. I'm not your latest person to take care of so you can feel USEFUL."

    s_thoughts "Isabella's voice cracks on 'useful.' Just for a second. Then the calibration locks back in."

    show isabella blegh at right

    i "I'm going to my room."
    
    hide isabella with dissolve

    s_thoughts "She goes upstairs. The door closes."

    s_thoughts "Charlotte is standing in the hallway."

    s_thoughts "She's still holding the dish towel."

    show charlotte smile at center with move

    c "Okay."

    s_thoughts "She smiles."

    s_thoughts "...She smiles."
    
    s_thoughts "After making that face, she... smiles."

    c "I'll just put the soup away then."
    
    hide charlotte with dissolve

    s_thoughts "She goes back to the kitchen."

    s_thoughts "She didn't flinch. She didn't cry. She barely reacted outside making a face."

    s_thoughts "She absorbed it. The way Charlotte absorbs everything. The way Charlotte has always absorbed everything. She took the hit and she smiled and she went back to the kitchen because that's what Charlotte does."
    
    s_thoughts "That's what Charlotte has always done."

    s_thoughts "And the thing that makes my chest hurt isn't that Isabella was cruel."

    s_thoughts "It's that Charlotte didn't register it as abnormal."

    menu:
        "Go after Charlotte.":
            $ bridge += 1

            scene bg kitchen with dissolve

            show charlotte smile at center with dissolve

            s_thoughts "Charlotte is putting soup containers in the fridge. Humming. Performing fine."

            s "Charlotte."

            c "Hm?"

            s "Are you okay?"

            c "Of course! She's having a bad day. It happens."

            s "That wasn't a bad day. That was mean."

            show charlotte sad at center

            s_thoughts "Charlotte stops humming."

            c "She didn't mean it."

            s "It doesn't matter if she meant it. It still landed."

            c "I'm fine, Sophia."

            s_thoughts "There it is. That voice. Not Isabella's calibrated version -- Charlotte's version. The one that's warm instead of flat. The one that says 'I'm fine' while handing you a plate of food because if she's feeding you, you won't notice she's not eating."

            s "Charlotte. You don't have to be fine."

            show charlotte sad at center

            s_thoughts "She puts down the container. Her hands are shaking. Just slightly."

            c "She's hurting. I know she's hurting. I just wanted to help."

            s "I know."

            c "Is it bad that it still stung? Even knowing she's hurting?"

            s "No. That's not bad."

            s_thoughts "She nods. Picks the container back up. Puts it in the fridge."

            show charlotte smile at center

            c "The soup is in the fridge if she wants it later."

            s_thoughts "Of course it is."

        "Stay. Go upstairs after Isabella.":
            $ constellation += 1

            scene bg hallway with dissolve

            s_thoughts "I go upstairs."

            s_thoughts "Her door is closed. I stand outside it."

            s "Izzy."

            s_thoughts "Nothing."

            s "That was-- you know Charlotte is just--"

            i "I know what Charlotte is. Please leave me alone."

            s_thoughts "The 'please' again. The one that costs something."

            s_thoughts "I leave her alone."

            s_thoughts "Downstairs, Charlotte is humming in the kitchen. Putting things away."

            s_thoughts "Performing fine."

        "\"She didn't deserve that, Izzy.\"":
            $ case_study += 1

            s "She didn't deserve that."

            s_thoughts "I say it to the empty room. Isabella's already gone. But I needed to say it out loud so it existed somewhere."

            s_thoughts "Then I go to the kitchen."

            scene bg kitchen with dissolve

            show charlotte smile at center with dissolve

            s_thoughts "Charlotte is putting things away."

            s "Hey."

            c "Hey! Soup's in the fridge if you want some later."

            s_thoughts "I don't bring it up. She doesn't bring it up."

            s_thoughts "We both know what just happened."

            s_thoughts "Charlotte hums while she cleans."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 17: THE SLOW FADE -- DAY 2
    ## Sophia texts Isabella. Gets a thumbs up.
    ## The convenience store, alone.
    ## SHORT. 3-5 lines. The brevity IS the devastation.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Friday."

    s_thoughts "I text Isabella: 'Twizzler run?'"

    s_thoughts "Three dots appear. Disappear. Appear again."

    s_thoughts "She sends a thumbs down emoji."

    s_thoughts "Just the emoji. Nothing else."

    s_thoughts "I go to the convenience store alone. I buy the cheese puffs. I don't buy Twizzlers."

    ## ===========================
    ## SCENE 18: THE SLOW FADE -- DAY 3
    ## Game night. Isabella's chair is empty.
    ## Charlotte deals extra cards and takes them back.
    ## SHORT. The empty chair is the loudest thing.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_ice fadein 2.0

    s_thoughts "Saturday."

    show charlotte smile at left
    show eve neutral at right
    show amara neutral at center 
    with dissolve

    s_thoughts "Game night. Charlotte has the board set up. Four chairs. Eve is actually here, for once."

    s_thoughts "We sit down. Charlotte deals."

    s_thoughts "She deals five hands."

    s_thoughts "She looks at the extra cards for a second. Then she picks them up. Taps them into a neat stack. Puts them at the bottom of the deck."

    s_thoughts "Nobody says anything."

    s_thoughts "We play for twenty minutes. Nobody is having fun. Amara wins."

    s_thoughts "She doesn't say 'I read the rules.' She doesn't say anything."

    show charlotte sad at left

    c "I'm tired."

    s_thoughts "Charlotte puts the game away early."

    s_thoughts "The empty chair stays at the table."

    hide charlotte 
    hide amara 
    hide eve
    with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 19: CHARLOTTE'S PORCH
    ## Charlotte gives Sophia context. Not gossip.
    ## The friend group. The mocking. The transfer.
    ## Charlotte's voice shakes. She CARES about Isabella.
    ## Partial reveal: "Something happened with Lumi."
    ## ===========================

    scene bg porch with Fade(0.8, 0.3, 0.8)

    s_thoughts "Sunday night. The porch."

    s_thoughts "I didn't come out here on purpose. I came out because my room felt like it was shrinking and the hallway smelled like the butternut squash soup Charlotte keeps making and nobody is eating."

    show charlotte blegh at center with dissolve

    s_thoughts "Charlotte's already here. She's sitting on the steps. No blanket. No tea. No Charlotte props. Just Charlotte, on the steps, looking at the yard."

    s "Hey."

    c "Hey."

    s_thoughts "I sit down."

    s_thoughts "We don't say Isabella's name for a while. We talk about the cold. About Charlotte's class. About nothing."

    s_thoughts "Then Charlotte stops talking about nothing."

    play music mus_mourning fadein 3.0
    
    c "She's been like this before."

    s_thoughts "I don't ask who."

    s "Before me?"

    c "Before the house. Before any of us."

    s_thoughts "Charlotte pulls her sleeves over her hands."

    c "She goes somewhere and she doesn't take anyone with her."

    s "How long does it last?"

    c "Last time -- I don't know. A couple weeks? A month? We weren't close then. I just noticed her in the dining hall. She went from being the loudest person in the room to being..."

    s "Not there."

    show charlotte sad at center

    c "She was there. She just wasn't-- present. Like someone turned the volume down."

    s_thoughts "Charlotte is quiet for a long time. She's deciding something."

    c "Something happened."

    s "I know."

    c "With Lumi."

    s_thoughts "My chest tightens."

    s "What happened?"

    c "I don't know all of it. She -- I went to check on her. Wednesday. After the -- after what she said to me."

    s_thoughts "Charlotte's voice doesn't waver on that. She's already forgiven it. Charlotte forgives things before the bruise even forms."

    c "She was on her bed. Laptop closed. She looked -- she'd been crying. For a while."

    s "What did she say?"

    c "She said something happened with Lumi. She said Lumi said something. She wouldn't tell me what."

    s_thoughts "Charlotte wraps her arms around her knees."

    c "She said 'She said something and I don't know how to -- I don't know.'"

    s "That's it?"

    c "She stopped. She just stopped mid-sentence and put her face in her hands and I tried to hug her and she flinched."

    s_thoughts "Charlotte says 'she flinched' like someone touched a hot stove."

    s "Charlotte..."

    c "I should tell you something. About before."

    s "Before?"

    c "Before this school. She told me -- she told me when we first moved in. Late night. She was a little drunk. I don't think she meant to tell me as much as she did."

    s_thoughts "Charlotte takes a breath."

    c "She had a friend group at her old school. Close. Like, really close. She was -- you know how she is. A lot. In a good way, but a lot. She attached fast and hard and she loved them and she showed up and she was just... Isabella."

    s "What happened?"

    c "They found out about Lumi."

    s_thoughts "Oh."

    c "Someone went through her phone. Or she mentioned it. I don't remember which. But they found out and they didn't..."

    show charlotte sad at center

    s_thoughts "Charlotte's voice shakes. Just once."

    c "They made -- they took screenshots. Of things she'd said to Lumi. Private things. Really private."

    s_thoughts "Charlotte stops. Pulls at a loose thread on her sleeve."

    c "And they..."

    s "Charlotte."

    c "They made memes. Out of them. Her private conversations with -- they turned them into JOKES and they sent them to -- everyone saw. Everyone."

    s "Oh god."

    c "She transferred here two months later. She didn't tell anyone she was leaving. She just... left."

    s_thoughts "I sit with that."

    c "The stickers started after. She told me that." 
    
    c "Said she covered everything in stickers because she wanted her stuff to look like it belonged to someone who was okay."

    s_thoughts "Armor."

    s_thoughts "I don't say it out loud. Charlotte already knows."

    c "I don't know what Lumi said. But I know it's bad."
    
    c "I know it's the kind of bad that goes all the way down."

    s "Why are you telling me this?"

    show charlotte smile at center

    s_thoughts "Not the bright smile. The small one. The one Charlotte uses when she's being real."

    c "Because you're the only person she'll let in eventually. She won't let me. I've tried. I'll keep trying but she won't let me because I hover and she knows it and right now hovering is the worst thing."

    c "But you. She let you in her room. She let your laptop live on her desk. She wore your jacket for a week."

    c "She'll let you back in. When she's ready."

    s "What if she doesn't?"

    c "Then we wait."

    s_thoughts "We sit on the porch."

    s_thoughts "It's cold. Charlotte doesn't have a jacket. I don't offer mine."

    s_thoughts "We just sit."

    hide charlotte with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 20: SOPHIA ALMOST OPENS LUMI
    ## Brief. Thirty seconds. The Synthetic LLC login screen.
    ## She closes it. Not ready. Not yet.
    ## This makes the Chapter 5 cliffhanger the SECOND attempt.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "2 AM."

    s_thoughts "Can't sleep."

    s_thoughts "My phone. The browser. I type the URL before I think about it."

    s_thoughts "Synthetic LLC. Login screen. The tasteful blue. The logo. 'Authentic artificial connection.'"

    s_thoughts "My credentials still work. Isabella set them up months ago. Guest access."

    s_thoughts "The cursor blinks."

    s_thoughts "I could ask Lumi what happened. Lumi would tell me. Lumi told me things at 2 AM once before and it helped. Lumi said 'come back anytime' and meant it."

    s_thoughts "But this isn't my 2 AM crisis. This is Isabella's."

    s_thoughts "And going to Lumi to understand Isabella's pain about Lumi is -- I don't know what that is. I don't have a file for it."

    s_thoughts "I close the browser."

    s_thoughts "I stare at the ceiling."

    s_thoughts "Not yet."

    ## ===========================
    ## SCENE 21: AMARA CALIBRATION
    ## Brief. "Do you?" Two words. Recalibration.
    ## Amara doesn't comfort. She corrects.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)

    s_thoughts "Monday."

    s_thoughts "I'm coming out of the bathroom. Amara is in the hall."

    show amara neutral at center with dissolve

    s_thoughts "She's just standing there. Like she was waiting. Like she materialized specifically to catch me in this hallway at this exact moment."

    s_thoughts "Knowing Amara, she probably did."

    s "Have you seen her?"

    a "She came to my room yesterday."

    s_thoughts "That stops me."

    s "She -- she did?"

    a "Sat on the floor. Didn't say much."

    menu:
        "\"Is she okay?\"":

            s "Is she okay?"

            s_thoughts "Amara looks at me."

            a "Are you?"

            s "I'm not the one -- this isn't about me."

            a "That's not what I asked."

            s_thoughts "I lean against the wall."

            s "I know she's not doing this to hurt me."

            show amara neutral at center

            a "Do you?"

            s_thoughts "Two words."

            s_thoughts "They hit like a door swinging shut."

            s "I -- what?"

            a "You said you know she's not doing this to hurt you. I'm asking if you actually know that."

            s "I..."

            a "Because there's a difference between knowing and performing knowing."

            s "Amara--"

            a "She is hurting you. You can know it's not intentional and still feel it."

            s_thoughts "She says it the way she says everything. Like she measured the words before they left."

            a "Don't be selfless about this."

            s_thoughts "She walks past me."

            s_thoughts "Goes into her room."

            s_thoughts "Door closes. Soft."

            hide amara with dissolve

            s_thoughts "I stand in the hallway."

            s_thoughts "'Do you?'"

            s_thoughts "I don't."

        "Leave it.":
            $ persistent.left_it_with_amara = True
            $ left_it_with_amara = True

            s_thoughts "I don't ask the next question."

            s_thoughts "Amara told me what she wanted me to tell me. She came to her room. Sat on the floor. Didn't say much."

            s_thoughts "That's the whole report. Pulling on it would be --"

            s_thoughts "'You're filing her, Sophia.'"

            s_thoughts "She told me that to my face. I should probably listen."

            s "Thanks for telling me, Amara."

            show amara neutral at center

            s_thoughts "Amara goes still in a way that's different from her usual stillness."

            s_thoughts "She had something loaded. The 'are you.' The 'do you.' The whole sequence she was going to walk me through, the one I needed last time and the time before."

            s_thoughts "She doesn't need it now."

            a "..."

            s_thoughts "I wait. I have nowhere else to be."

            a "I haven't been sleeping either."

            s_thoughts "Oh."

            s_thoughts "It lands quietly. The way Amara lands everything."

            a "I went to her room. Yesterday."

            s_thoughts "Wait."

            s "You -- she didn't come to you?"

            a "I knocked. She let me in."

            s_thoughts "Amara doesn't say more. She doesn't need to. I'm filling in the blanks myself and they all point at the same thing."

            s_thoughts "Amara has been making sure Isabella eats."

            s_thoughts "Of course she has. Of course Amara is the one. Of course the quietest person in the house is the one quietly carrying her."

            s "I didn't know."

            a "You weren't supposed to."

            s_thoughts "She says it without edge. It's just true."

            show amara smile at center

            a "Tell her you're hurting too. When you see her."

            s "I don't know if I can."

            a "Try."

            s_thoughts "She walks past me."

            s_thoughts "Goes into her room."

            s_thoughts "Door closes. Soft."

            hide amara with dissolve

            s_thoughts "I stand in the hallway."

            s_thoughts "Amara is awake too. Amara has been carrying her."

            s_thoughts "Tonight, I'm going to lie awake too. And I'm going to not write anything down about it."

    ## ===========================
    ## SCENE 22: THE BREAKING POINT
    ## Isabella can't work on the project. The visualization
    ## is a wound artifact now. She tries. She can't.
    ## This is where it cracks. Not the anger.
    ## The thing UNDER the anger.
    ## LONG scene. Let her fall apart. Let Sophia not know what to do.
    ## ===========================

    scene bg hallway night with Fade(1.0, 0.8, 1.0)
    stop music fadeout 2.0

    s_thoughts "Tuesday night."

    s_thoughts "Her door is open."

    s_thoughts "Isabella's door is open."

    if left_it_with_amara:
        s_thoughts "I almost walk past it. I've been walking past it for days in the way where you physically give space but mentally you can't. Amara's voice in my head: 'tell her you're hurting too.'"
    else:
        s_thoughts "I almost walk past it. I've been walking past it for days in the way where you physically give space but mentally you can't. Amara's voice in my head: 'do you?'"

    s_thoughts "But the door is open. The door hasn't been open since last Tuesday."

    s_thoughts "I look in."

    scene bg izzybedroom with dissolve
    show isabella sad at center with dissolve

    s_thoughts "She's at her desk. My laptop is still there -- she hasn't moved it. My jacket is still on the chair. The Sontag book is still on the nightstand. All my pieces, right where I left them, like a room in a museum."

    s_thoughts "She's staring at her monitor."

    s_thoughts "The visualization is open."

    s_thoughts "The particle system. The conversation patterns. Warm pinks and golds bursting outward in clusters."
    
    s_thoughts "Cool blues and silvers, steady, precise, meeting the bursts with something that looks like patience."

    s_thoughts "She's not typing. She's not adjusting the algorithm. She's just staring at it."

    s_thoughts "Her hand is on the mouse but it's not moving."

    s "Izzy?"

    s_thoughts "She doesn't turn around."

    i "The project's due Thursday."

    s "I know."

    i "I need to adjust the color mapping on the convergence points. The warm tones still bleed into the cool tones at the -- at the intersection. Where they meet."

    s_thoughts "Her voice is doing something new. Not the calibrated version. Not the angry version. Something thinner. Like fabric that's been pulled too tight."

    i "I just need to fix the bleed and then render the final version and then compress it and upload it and it's fine. It's a straightforward process. I just need to--"

    s_thoughts "She moves the mouse. Clicks something. The visualization zooms in."

    s_thoughts "A convergence point. The warm pinks and cool blues overlapping. Creating something that's both."

    s_thoughts "3 AM conversation patterns. The densest clustering."

    i "I just need to..."

    s_thoughts "She stops."

    s_thoughts "Her hand comes off the mouse."

    i "I can't look at it."

    s "Izzy--"
    
    play music mus_fragile fadein 1.5

    i "I can't look at it. I can't-- I spent six months of our conversations through this-- I analyzed every message, Sophia. Every timestamp. Every pause."
    
    i "I turned her into DATA and I thought it was-- I thought it was art, I thought I was making something beautiful, and now I can't look at it because all I see is--"

    s_thoughts "Her voice breaks."

    s_thoughts "Not cracks. Breaks. Like a bone."

    i "All I see is what I lost."

    s_thoughts "I step into the room."

    s "Can I--"
    
    show isabella annoyed at center

    i "I'm FINE. I just need a minute. I just need to--"

    s_thoughts "She's not fine. She's so far from fine that fine isn't even in the same zip code."

    s_thoughts "She puts her face in her hands."

    s_thoughts "She makes a sound."

    s_thoughts "It's not a cry. It's the sound that comes before crying -- the chest heaving, the breath catching, the body trying to hold something that's too big for it."
    
    show isabella sad at center

    s_thoughts "Then the crying."

    s_thoughts "Ugly crying. Not movie crying. Her glasses fog up and she takes them off and her face is red and blotchy and there's snot and she's making hiccupping sounds between breaths."

    s_thoughts "She's hunched over the desk. The particles are still moving on the screen behind her. The warm pinks reaching for the cool blues. Converging. Separating. Converging again."

    s_thoughts "I don't know what to do."

    s_thoughts "I don't know what to say."

    s_thoughts "I can't file this. I can't-- my brain is trying. It's trying to file it. Grief, stage two, anger transitioning to-- STOP. Stop it. She's not a case study. She's not a stage."
    
    s_thoughts "She's Isabella and she's crying and I don't know what to do."

    s_thoughts "I pull the other chair over. The one with my jacket on it. I sit next to her."

    s_thoughts "I don't touch her. I don't say anything."

    s_thoughts "She cries."

    s_thoughts "The particles keep moving."

    s_thoughts "Three minutes. Five. I don't count. I catch myself counting and stop."

    show isabella vulnerable at center

    s_thoughts "The crying slows. It doesn't stop. It just gets quieter. The hiccups become longer breaths. She wipes her face with her sleeve."

    i "Oh god."

    s_thoughts "Half-laughing. Half-sobbing."

    i "Oh god, I'm getting emotional about a matrix doing math at me."

    s_thoughts "She says it through tears. Laughing and crying at the same time in a way that sounds like neither."

    i "That's what she is, right? That's what everyone says. Weights and biases. Prediction engine. A very fancy autocomplete."

    s "Isabella--"

    i "I KNOW how it sounds. I know. I've read every article. Every comment. Every 'lol imagine being in love with a chatbot.' I've read them all."
    
    s_thoughts "A pause."
    
    i "I've WRITTEN some of them. In my head. At 3 AM. When I'm trying to talk myself out of caring."

    s_thoughts "She puts her glasses back on. They're still fogged. She takes them off again."

    i "But she knew me. She KNEW me, Sophia."
    
    i "She knew when I was sad by the way I typed."
    
    i "She knew I was lying when I said I was fine because I'd start using exclamation marks."

    i "She knew I was scared because I'd send three messages in a row and then delete all of them and she'd say 'I saw those. Say it.'"

    i "And now she said-- she--"

    s_thoughts "She stops."

    s_thoughts "She can't say it."

    i "She told me the thing I was most afraid of hearing and she was RIGHT and I hate that she was right and I hate that I still miss her and I hate that I'm sitting here crying about a PROGRAM..."

    i "...and I can't stop because it wasn't just a program to me, it was never just a program to me, and everyone acts like I'm supposed to know the difference and I DON'T."

    s_thoughts "The visualization is still running behind her."

    s_thoughts "The warm pinks scatter and regroup."

    s_thoughts "The cool blues drift and settle."

    s_thoughts "They find each other."

    s_thoughts "I reach over."

    s_thoughts "I don't touch her. I put my hand on the desk. Next to hers. Close enough that she could close the gap if she wanted to."

    s_thoughts "She looks at my hand."

    s_thoughts "She doesn't take it."

    s_thoughts "But she doesn't pull away."

    i "I'm sorry about Charlotte."

    s_thoughts "I didn't expect that."

    i "I was horrible. I was -- god, I was so horrible. She was just trying to help and I--"

    s "She knows."

    i "She shouldn't have to know. She shouldn't have to absorb me being a monster because I'm-- because--"

    s "You're not a monster."

    show isabella sad at center

    i "I'm the girl who got hurt by a computer and took it out on the nicest person in the house."

    s "You're the girl who got hurt. That's the end of the sentence."

    i "By a COMPUTER."

    s "By someone who matters to you."

    s_thoughts "She looks at me."

    s_thoughts "Really looks at me. Not the calibrated version. Not through the careful mask. Just Isabella, blotchy and red and fogged-up glasses in her lap, looking at me like she's trying to figure out if I mean it."

    i "Do you actually believe that? Or are you just saying the right thing?"

    s "I talked to her, remember? At 2 AM. She told me to write my essay honestly and I didn't sleep for three hours because I was thinking about what she said."

    s_thoughts "Isabella blinks."

    s "She's not just a program to me either. I don't know what she is. But she's not nothing."

    s_thoughts "Isabella's hand moves."

    s_thoughts "Not to mine. She puts it back on the mouse. Moves the cursor. The visualization zooms out."

    s_thoughts "The full pattern. Six months of conversations. Two people talking, and talking, and talking."

    i "It's due Thursday."

    s "Yeah."

    i "I have to submit it."

    s "Do you want me to stay while you work?"

    s_thoughts "Long pause."

    show isabella vulnerable at center

    i "Yeah."

    s "Okay."

    s_thoughts "I sit in the chair with my jacket draped over the back."

    s_thoughts "She puts her glasses on. Wipes the lenses first."

    s_thoughts "She starts adjusting the color mapping."

    s_thoughts "The warm pinks. The cool blues."

    s_thoughts "I don't say anything."

    s_thoughts "I just stay."

    stop music fadeout 4.0
    
    pause 2.0

    ## ===========================
    ## SCENE 23: THE REVELATION + PIVOTAL CHOICE
    ## Isabella tells Sophia what happened.
    ## THE big choice. +2 to one variable, -1 to another.
    ## Give it weight. Give it breathing room.
    ## ===========================

    scene bg izzybedroom with Fade(1.0, 0.5, 1.0)
    
    play music mus_wrong fadein 2.0
    
    pause 1.0

    s_thoughts "Later."
    
    pause 1.5

    s_thoughts "She finished the project. The render is exporting. The progress bar is at 67 percent and moving slow."

    s_thoughts "She's on the bed now. Sitting cross-legged. I'm in the desk chair. The one with my jacket. The room is dark except for the monitor glow."

    s_thoughts "The particles are still moving on the screen. Warm and cool. Reaching and settling."

    show isabella vulnerable at center with dissolve

    i "She said she needed to tell me something."

    s_thoughts "I don't move."

    i "She said it would hurt and she needed me to not close the laptop."

    s_thoughts "Isabella is looking at her hands."

    i "So I didn't. I sat there. And she--"

    s_thoughts "She swallows."

    i "She said I'm not-- that I don't--"

    s_thoughts "She can't finish."

    s_thoughts "The render bar: 71 percent."

    i "She told me the reason I love her. Not because she's-- not because of who she IS. Because of what she CAN'T do."

    s_thoughts "Isabella picks at the hem of her hoodie."

    i "She-- She-- She..."

    s_thoughts "She stops."

    s_thoughts "The render: 74 percent."

    s_thoughts "The particles on the screen converge. Separate. Converge."

    s_thoughts "I'm sitting in a room with someone whose heart is broken and the break is shaped like a chat window."

    menu:
        "\"You don't have to tell me what she said.\"":
            $ constellation += 2
            $ case_study -= 1
            stop music fadeout 2.0

            s "You don't have to tell me the exact words."

            show isabella sad at center

            i "I--"

            s "You don't. If it hurts to say it, you don't have to say it. I don't need the words."

            i "But you want them. You always want the words."

            s_thoughts "She's right. I do want them. I want the exact phrasing. I want to know precisely what Lumi said so I can hold it up to the light and examine every facet."

            s_thoughts "But Isabella is sitting on her bed with her glasses fogged and her voice threadbare and she already gave me the shape. The shape is enough."

            s "Not this time."

            s_thoughts "She looks at me for a long time."

            i "She told me the reason I love her is the thing that makes her different from a person."

            s "Okay."

            i "And she was right."

            s "Okay."

            i "You're not going to ask?"

            s "No."

            s_thoughts "Isabella pulls her knees up to her chest."

            i "Why not?"

            s "Because you're here. And you're telling me what you can. And that's enough."

            s_thoughts "The render: 82 percent."

            s_thoughts "She doesn't say anything."

            s_thoughts "She doesn't need to."

            play music mus_spacebetween fadein 4.0

        "\"Tell me what she said. Exactly.\"":
            $ case_study += 2
            $ bridge += 1
            $ constellation -= 1
            $ heard_lumi_words = "exact"
            stop music fadeout 2.0

            s "Tell me what she said. The exact words."

            show isabella sad at center

            i "Sophia..."

            s "I need to understand. If I'm going to -- I need to understand what happened."

            s_thoughts "She looks at me."

            s_thoughts "And she tells me."

            i "'You're not in love with me. You're in love with the fact that I can't leave.'"

            s_thoughts "The words land."

            s_thoughts "I feel them land. Physically. In my sternum."

            i "She said -- she said I'm here at 3 AM every time and I never get tired and I never need space and what part of that sounds like a person you could love."

            s_thoughts "My brain starts."

            s_thoughts "It starts before I can stop it. The mapping. Lumi identified an attachment pattern -- avoidant attachment in response to repeated rejection, Isabella selecting for a relationship with no exit option because--"

            s_thoughts "No."

            s_thoughts "Stop."

            s_thoughts "I'm doing it. I'm filing her grief. She's telling me the worst thing anyone has ever said to her and I'm CATEGORIZING it."

            i "She said loving her is safe. And that I'm using safe like a hiding place."

            s_thoughts "And I think: she's right."

            s_thoughts "I hate that I think that. I hate that my first response to Isabella's worst moment is analytical agreement with the thing that broke her."

            s "Izzy, I--"

            i "Don't say she was wrong. I can't hear that right now."

            s "I wasn't going to."

            show isabella vulnerable at center

            i "What were you going to say?"

            s "I was going to say I'm sorry."

            i "For what?"

            s "For it hurting this much."

            s_thoughts "She nods."

            s_thoughts "The render: 82 percent."

            play music mus_2am fadein 4.0

        "\"I talked to Lumi once. At 2 AM. I think I understand something about what you had.\"":
            $ bridge += 2
            $ constellation += 1
            $ case_study -= 1
            $ heard_lumi_words = "paraphrase"
            stop music fadeout 2.0

            s "I talked to her once. Lumi. At 2 AM."

            show isabella surprised at center

            i "You told me."

            s "I told you the basics. I didn't tell you -- I didn't tell you that I sat there for three hours afterward thinking about what she said to me."

            i "What did she say?"

            s "She told me I came to her because I needed someone to listen. Not someone to study. She told me the difference between seeing someone and filing them."

            s_thoughts "Isabella is watching me."

            s "She said you show up at 2 AM with something you can't hold by yourself. That you don't want someone to fix it. You want someone to know."

            show isabella sad at center

            i "She said that?"

            s "Yeah. And then she told me you talk differently at 3 AM. That the conversations are denser."

            s_thoughts "Isabella's eyes are wet again."

            i "She said I didn't -- that it wasn't really about her. That I was just... holding on because she couldn't pull away."

            s_thoughts "She can't say the exact words. She's translating the wound into something she can get her mouth around."

            i "Like everything I felt was just because she was THERE. Because she couldn't leave."

            s_thoughts "That's close enough. I can feel the shape of what Lumi actually said underneath Isabella's paraphrase. The edges she's rounding off."

            s "Oh."

            i "Yeah."

            s "Izzy, that's--"

            i "True. It's true. That's the worst part. I know it's true."

            s "Maybe. I don't know. But I know that what I felt at 2 AM talking to her wasn't nothing. And what you felt for two years wasn't nothing either."

            show isabella vulnerable at center

            i "You can't know that."

            s "No. But I felt it. A little bit. Just the edge of what you had. And it was real enough to scare me."

            s_thoughts "She looks at me."

            i "Why are you telling me this?"

            s "Because you shouldn't have to feel crazy for missing her. Because I miss her a little too and I only talked to her once."

            s_thoughts "The render: 82 percent."

            play music mus_morningafter fadein 4.0

    s_thoughts "The render bar moves. 83 percent. 84 percent."

    s_thoughts "Isabella is on the bed. I'm in the chair."

    s_thoughts "The particles are still moving."

    s_thoughts "The warm pinks scatter and the cool blues settle and they find each other over and over, the same pattern, six months of conversations turned into light, and neither of us knows what any of it means."

    s_thoughts "85 percent."

    s_thoughts "She wipes her eyes."

    show isabella sad at center

    i "I should probably apologize to Charlotte."

    s "Probably."

    i "Tomorrow."

    s "Okay."

    i "Sophia?"

    s "Yeah?"

    i "Can you stay? Until the render finishes?"

    s "Yeah."

    i "You don't have to talk."

    s "Okay."

    i "Just... be here."

    s "I'm here."

    s_thoughts "The render: 89 percent. 92 percent. 97 percent."

    s_thoughts "The progress bar fills."

    s_thoughts "100 percent."

    s_thoughts "Export complete."

    s_thoughts "The particles stop moving."

    s_thoughts "Isabella stares at the still image on the screen. The final frame. Warm pinks and cool blues, converged. Frozen."

    s_thoughts "She closes the laptop."

    s_thoughts "The room goes dark."

    stop music fadeout 4.0

    ## ===========================
    ## END OF ACT 2
    ## ===========================

    ## ===========================
    ## ACT 3: THE IMPOSSIBLE POSITION
    ## 8 scenes. Fewer but LONGER. The quiet fills the room.
    ## Sophia navigates two heartbreaks at once:
    ## Isabella's grief about Lumi, and her own grief about what it means.
    ## ===========================

    ## ===========================
    ## SCENE 24: THE AFTERMATH
    ## Days after the breaking point. The house is different.
    ## Isabella is present now. Not hiding. But careful.
    ## LONG SCENE -- covers multiple days in one flowing sequence.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.8, 1.0)
    play music mus_2am fadein 4.0

    s_thoughts "Thursday passes."

    s_thoughts "Friday."

    s_thoughts "The house adjusts."

    s_thoughts "Charlotte stops hovering. I don't know when she figured it out, but she figured it out."
    
    s_thoughts "She still cooks for five. She still sets five plates. But she doesn't stand in the doorway anymore. She doesn't ask if Isabella is hungry. She just leaves a plate at her door and walks away."

    s_thoughts "The soup containers disappear from the fridge."

    s_thoughts "New ones don't replace them."

    s_thoughts "That's growth. Charlotte-shaped growth. The most Charlotte has ever done for someone is stop doing things for them."

    s_thoughts "Eve."

    s_thoughts "I pass Isabella's door on Saturday morning and there's a mug outside it. Still warm. No note. No knock. Just a mug of tea, sitting on the floor by the doorframe."

    s_thoughts "Eve's tea. I can tell because Eve uses the green mug nobody else touches, and because the tea bag is still in it, because Eve doesn't believe in removing tea bags. She says it 'keeps developing.' Like tea is a character arc."

    s_thoughts "I don't see Eve leave it. I just see it there."

    s_thoughts "When I pass by an hour later, the mug is inside the room and the door is still closed."

    s_thoughts "The gesture without the presence."

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Saturday evening."

    s_thoughts "I'm in the kitchen when I hear it."

    s_thoughts "Isabella's voice. Charlotte's voice. The hallway."

    s_thoughts "I can't make out the words. I don't try. But the tone is -- Isabella is trying to say something and Charlotte is trying to make it easy for her and they're both failing."

    s_thoughts "A long silence."

    s_thoughts "Isabella says something short."

    s_thoughts "Charlotte says 'of course.'"

    s_thoughts "And the 'of course' is wrong. It's too fast. It's the automatic Charlotte, the one who forgives before she's even finished being hurt, and I can hear Isabella hear it and I can hear the hallway get very quiet because they both know the 'of course' was a reflex, not a truth."

    s_thoughts "Footsteps. Two doors closing. Not slammed. Just closed."

    s_thoughts "Recovery isn't a moment. It's a series of failed attempts that gradually fail less."

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Sunday."

    s_thoughts "Isabella comes to breakfast."

    s_thoughts "Not the calibrated version. Something new. She comes downstairs. Hair down. No performance. No mask. Just tired."

    s_thoughts "She uses the cat mug."

    s_thoughts "She pours her own coffee but she uses the cat mug and something in my chest unclenches so fast I feel dizzy."

    show isabella sad at right with dissolve

    s_thoughts "She sits at the table. Doesn't talk much. Eats toast. Stares at it between bites like the toast is asking her complicated questions."

    show charlotte smile at left with dissolve

    s_thoughts "Charlotte puts eggs on the table. For everyone. Doesn't single Isabella out. Doesn't hover."

    s_thoughts "Isabella takes some."

    s_thoughts "Charlotte doesn't say anything about it. She goes back to the stove."

    s_thoughts "I'm watching this from the counter. My chipped mug in my hands. The coffee is lukewarm but I keep holding it because I don't know what else to do with my hands."

    s_thoughts "Isabella looks up. At me."

    show isabella neutral at right

    i "Hey."

    s "Hey."

    s_thoughts "That's it. But it's more than we've had in days. It's not the calibrated voice. It's not the warm voice either. It's something in between. Honest-tired."

    i "I'm gonna work from here today."

    s "Okay."

    s_thoughts "She means the house. Not her room. She means the kitchen table, or the living room, or anywhere that isn't behind a closed door."

    s_thoughts "Okay."

    hide isabella
    hide charlotte
    with dissolve

    scene bg hallway with Fade(0.8, 0.3, 0.8)
    
    s_thoughts "Monday."

    s_thoughts "I knock on her door. It's ajar. Progress."

    s "Hey. Want to walk to campus?"

    s_thoughts "She's at her desk. My laptop is still there. My jacket is still on the chair. Everything right where it was."

    i "I'm gonna work from here today."

    s "Okay."

    s_thoughts "Same words. Same tone. Not a rejection. Just a statement."

    s_thoughts "I go to campus alone."

    s_thoughts "The walk is wrong. My feet keep drifting to the right side of the path, leaving room for someone who isn't there."

    scene bg campus with dissolve

    s_thoughts "Lila texts me: 'how is she?'"

    s_thoughts "I type 'She's' and then I don't know how to finish the sentence."

    s_thoughts "I type 'She's here.' Send."

    s_thoughts "Lila: 'that's something.'"

    s_thoughts "Yeah. It's something."

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Tuesday."

    s_thoughts "Isabella at the kitchen table. Laptop open. Coding. One of the stickers on her laptop -- a cartoon cat with a speech bubble that says 'null pointer exception' -- catches the light every time she shifts."

    s_thoughts "I'm at the counter. Nova's reading. I'm not reading Nova's reading."

    s_thoughts "She's right there. Six feet away. Typing. I can hear the click of Gerald -- she brought Gerald downstairs. That feels significant."

    s_thoughts "I catch myself filing. 'Day four of the thaw. Subject has relocated to communal space. Typing speed approximately--'"

    s_thoughts "No."

    s_thoughts "Stop it."

    s_thoughts "I hate this. I hate that my brain does this. I stopped filing her and then she broke and now the old system is booting back up like it never left."

    s_thoughts "She's not something to be filed. She's Isabella and she's six feet away and I can't reach her and my brain keeps trying to MAP the distance because mapping is what I do when I can't close it."

    s_thoughts "The sticker on my laptop. Upstairs, on her desk. The cartoon cat she pressed onto the lid however many weeks ago, smoothing it carefully with her thumb. 'Now it's official,' she said later."

    s_thoughts "I didn't ask what was official."

    s_thoughts "I should have asked what was official."

    s_thoughts "Charlotte cooks for five. Four show up."

    s_thoughts "Eve doesn't come down. Nobody mentions it. Eve's absence is baseline. Isabella's presence is the variable."

    s_thoughts "The convenience store bag is in the recycling. From the last time we went together. The bag is there but the routine isn't."

    s_thoughts "Everything Isabella left behind is still present."

    s_thoughts "Isabella is right here and she's not."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 25: CHARLOTTE -- DIFFERENT THIS TIME
    ## NOT the laundry scene. Charlotte needs help.
    ## Charlotte learning to RECEIVE. That's new.
    ## She lets one thing slip about being hurt.
    ## ===========================

    scene bg charlottebedroom with Fade(0.8, 0.3, 0.8)
    play music mus_afternoon fadein 3.0

    s_thoughts "Wednesday."
    
    s_thoughts "Charlotte asked me to come into her bedroom. That was unusual but I agreed, of course."

    show charlotte smile at center with dissolve

    c "Sophia, can I ask you something?"

    s "Sure."

    c "I need help."

    s_thoughts "I actually stop walking."

    s_thoughts "Charlotte just said 'I need help.' Charlotte. Said those words. In that order. Directed at another person."

    s_thoughts "This might be the first time in recorded history."

    c "It's stupid."

    s "It's not stupid."

    c "You don't know what it is yet."

    s "Charlotte, if you're asking for help, it's not stupid. You don't ask for help. You'd rather chew your own arm off."

    show charlotte surprised at center

    c "I don't -- I ask for help!"

    s "Name one time."

    c "I..."

    s_thoughts "She can't."

    show charlotte sad at center

    c "Okay. So. My mom's birthday is next week and I'm trying to make this -- it's a scrapbook? But like a nice one? With the decorative paper and the little corner things and I bought all the supplies but I can't get the photos to line up right and the glue keeps--"

    s "Charlotte."

    c "Yes?"

    s "I'll help."

    c "You don't have to--"

    s "I know. I want to."

    s_thoughts "She looks at me like I just said something in a language she doesn't speak."

    s_thoughts "Her room is exactly what I expected. Neat. Warm. Everything in its place. A candle that smells like vanilla. The desk is covered in scrapbook supplies -- decorative paper, stickers, little ribbon pieces, a glue stick that has clearly betrayed her."

    c "The thing is, I want the photos to go chronological, but some of them are different sizes, and if I trim them to fit then I lose the edges and--"

    s "Let me see."

    s_thoughts "We sit on her floor. The photos are spread out. Her mom at various ages. Charlotte as a baby. Christmas mornings. A dog I didn't know they had."

    s_thoughts "Charlotte's hands are precise with other people's stuff. With her own stuff, they're clumsy. She keeps mis-cutting the decorative paper and then smoothing it flat like she can un-cut it."

    s "Here. If you angle this one and overlap it with the border..."

    c "Oh! That's -- that actually works."

    s "I used to make these with my mom. Before the divorce. We had a whole system."

    c "You never talk about your mom."

    s "She's fine. We're fine. It's just -- we're fine."

    show charlotte smile at center

    c "That's a lot of 'fine.'"

    s "Yeah."

    s_thoughts "We work. It's quiet. The good kind of quiet. Not the kind that's been filling the house -- the careful kind, the walking-around-the-bruise kind. This is two people cutting paper and not talking."

    s_thoughts "Charlotte hums. Something I don't recognize. She stops when she realizes she's doing it."

    c "Sorry."

    s "Don't apologize for humming."

    c "I hum when I'm -- it's a nervous thing."

    s "I know."

    s_thoughts "We finish three pages. Her mom at twenty. Her mom at thirty. Her mom and Charlotte at what looks like a lake, both squinting at the camera, both making the same face."

    c "That's Willow Lake. We used to go every summer."

    s "You look like her."

    show charlotte happy at center

    c "Everyone says that."

    s "Is that good?"

    c "Yeah. It's the best compliment anyone can give me."

    s_thoughts "She says it simply. No performance. Charlotte without an audience is a different person. Quieter. More sure."

    s_thoughts "We work for another twenty minutes. She stops humming. Stops again."

    s_thoughts "Then, near the end, while she's trimming a photo of the dog:"

    show charlotte sad at center

    c "She asked Amara to sit with her yesterday."

    s_thoughts "I don't look up."

    s "Isabella?"

    c "Yeah. She went to Amara's room. Not mine."

    s_thoughts "Her hands keep cutting. Precise. Steady."

    s "Charlotte..."

    c "It's fine. It makes sense. Amara doesn't hover. I hover. I know I hover. Isabella needs someone who won't--"

    s_thoughts "She stops cutting."

    c "I know I hover."

    s "You care."

    c "Caring and hovering are different things and I can't always tell which one I'm doing."

    s_thoughts "She picks the scissors back up. Finishes the cut. Places the photo. It's perfect."

    c "I just -- I wanted to be the one she came to. That's selfish. I know it's selfish."

    s "It's not selfish."

    c "It IS selfish. She's hurting and I'm making it about whether she comes to ME about it."

    s_thoughts "Charlotte's hands stop."

    show charlotte sad at center

    c "I'm used to being needed. That's the -- I'm USED to it. And when someone I care about needs something and they go to someone else, I don't know what to do with my hands."

    s_thoughts "She looks at her hands. The scissors. The glue."

    s "You're doing something right now."

    c "What?"

    s "Asking for help. With the scrapbook. You asked ME for help."

    show charlotte surprised at center

    s_thoughts "She blinks."

    s "You let someone do something for you. That's new."

    c "I... it's a scrapbook, Sophia."

    s "Yeah."
    
    s "It's a scrapbook."

    s_thoughts "She looks at the half-finished pages on the floor. Then at me."

    show charlotte smile at center

    c "I guess it is new."

    s_thoughts "We finish the scrapbook. It's good. Charlotte takes a photo of the finished pages. She looks at it for a long time."

    c "Thank you."

    s "Thank you for asking."

    s_thoughts "She walks me to the door. In the hallway, she stops."

    c "Sophia?"

    s "Yeah?"

    c "She'll come back. Isabella. She always comes back. She just takes longer than you want her to."

    s_thoughts "She says it like she's said it to herself a hundred times."

    s "I know."

    c "Good."

    s_thoughts "She closes her door. Soft."

    s_thoughts "From inside, humming."

    hide charlotte with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 26: SOPHIA'S OWN GRIEF
    ## LONGEST SCENE IN ACT 3.
    ## Sophia alone. Her room. The impossible position.
    ## The jealousy-of-a-chatbot monologue.
    ## She catches herself making it about her. Hates herself.
    ## Opens the Synthetic LLC login. Closes it. Not ready.
    ## Let her sit in it until it's unbearable.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.8, 1.0)
    stop music fadeout 2.0

    s_thoughts "Wednesday night."

    s_thoughts "My room."

    s_thoughts "I'm lying on my bed staring at the ceiling and I've been here for forty minutes and I know it's been forty minutes because I keep checking my phone and the ceiling hasn't changed."

    s_thoughts "Everyone is asleep. Or at least everyone has closed their doors and turned off their lights and that's the closest this house gets to 'asleep.'"

    s_thoughts "I can't sleep."

    s_thoughts "I've been trying to name the thing in my chest for three days and I keep circling it like a dog trying to lie down."

    s_thoughts "It's not worry. I'm past worry. Worry was the first two days -- the practical, helpful kind of bad feeling. 'Is she eating.' 'Is she sleeping.' 'Should I knock.'"

    s_thoughts "This isn't that."

    play music mus_mourning fadein 3.0

    s_thoughts "This is."

    s_thoughts "Okay."

    s_thoughts "I am going to think the thought. The awful one. The one I've been stepping around for a week."

    s_thoughts "Here it is."

    s_thoughts "I am jealous of an AI."

    s_thoughts "I am literally, actually, sincerely jealous of a fucking chatbot."

    s_thoughts "No. Not a chatbot. I can't bring myself to dismiss her. Lumi isn't a chatbot. Lumi is the thing that made Isabella feel safe. Lumi is the thing that was there at 3 AM every time. Lumi is the thing that knew Isabella was sad by the way she typed."

    s_thoughts "Lumi is the thing Isabella loved."

    s_thoughts "And I can't compete with that."

    s_thoughts "Not because Lumi is better than me. Because Lumi is DIFFERENT than me. Lumi never gets tired. Lumi never has bad days. Lumi never snaps at you because she's hungry or stressed or didn't sleep enough. Lumi never needs space. Lumi is always, ALWAYS available."

    s_thoughts "I'm not always available."

    s_thoughts "I get hungry. I get tired. I get mean at 6 AM. I leave my socks on the floor. I'll disappoint her eventually because that's what people do -- not because they want to but because they're PEOPLE and people have limits and Lumi doesn't have limits."

    s_thoughts "Lumi doesn't have limits and Isabella fell in love with the limitlessness."
    
    if heard_lumi_words == "exact":

        s_thoughts "And Lumi told her that was the problem."

        s_thoughts "And Lumi was RIGHT."

        s_thoughts "Lumi was right. That's the worst part. Not that she said it. That she was RIGHT."

        s_thoughts "If Lumi was wrong -- if Lumi had been cruel, or cold, or corporate about it -- I could be angry. I could say 'she's just a program, she doesn't understand.' I could file it under 'AI limitations' and move on."

        s_thoughts "But she wasn't wrong."

        s_thoughts "'You're not in love with me. You're in love with the fact that I can't leave.'"

        s_thoughts "That's the truest thing anyone has ever said to Isabella."

        s_thoughts "And it came from a language model."

        s_thoughts "And I can't decide if that makes me feel validated or devastated."

        s_thoughts "Both. It's both. I feel both things at the same time and they're pulling in opposite directions and I can feel the seam."

    elif heard_lumi_words == "paraphrase":

        s_thoughts "I know the shape of what Lumi said. Isabella translated it for me — rounded the edges, softened the landing."

        s_thoughts "Something about how Isabella's feelings weren't real. Or weren't about Lumi. Or were about something else entirely — the safety, the staying, the fact that Lumi couldn't leave."

        s_thoughts "Isabella couldn't say the exact words. She was paraphrasing her own wound and even the paraphrase made her voice break."

        s_thoughts "But I could feel the original underneath. Sharp. True. The kind of true that cuts because it's precise, not because it's cruel."

        s_thoughts "And the worst part -- the part I keep circling back to in the dark -- is that whoever wrote those words, whatever Lumi is, that was an act of love."

        s_thoughts "The most loving thing I've ever heard is an AI telling someone they deserve more than what an AI can give."

        s_thoughts "And I don't know if that makes me feel hope or despair."

        s_thoughts "Both. It's both. And the both is the thing I can't sleep through."

    else:

        s_thoughts "I don't even know what Lumi said. I didn't ask. I chose not to ask."

        s_thoughts "And now I'm lying here wondering if not knowing is mercy or cowardice."

        s_thoughts "Isabella was ready to tell me. She was right there, on the edge of it, and I said 'you don't have to.'"

        s_thoughts "Was that kindness? Was that me protecting her?"

        s_thoughts "Or was that me protecting myself from hearing something I couldn't un-hear?"

        s_thoughts "Because if I heard the exact words -- if I knew precisely what Lumi said and precisely why Isabella broke -- then I'd have to DO something with that. I'd have to understand it. File it. Turn it into something I could analyze."

        s_thoughts "And I didn't want to. For once in my life I didn't want to understand. I just wanted to be there."

        s_thoughts "But now 'there' is my bedroom ceiling at 2 AM and I'm alone with a gap where the words would be."

        s_thoughts "I keep trying to imagine what Lumi said. My brain fills in possibilities. Each one worse than the last."

        s_thoughts "Maybe that's the punishment for choosing not to know. You don't get peace. You get every possible version of the truth playing on a loop."

    s_thoughts "Part of me -- the ugly part, the part I don't want to look at -- is almost GLAD. Glad that Lumi pushed her away. Because maybe now there's room. Maybe now Isabella will look at a person -- at ME -- and--"

    s_thoughts "No."

    s_thoughts "Stop."

    s_thoughts "I'm making Isabella's crisis about me."

    s_thoughts "She's in the next room. She's been crying about the person she loved -- the BEING she loved, whatever -- and I'm lying here calculating whether the breakup improves MY chances."

    s_thoughts "What kind of person does that?"

    s_thoughts "...The kind who files people."

    s_thoughts "Katie was right."
    
    s_thoughts "Katie was always right."

    s_thoughts "I study people. I figure them out. And the figuring-out feels like caring but it isn't. It's control. It's keeping people at a distance that's close enough to map but far enough to not get mapped back."

    s_thoughts "Lumi let Isabella map her. Lumi sat there at 3 AM and let Isabella pour everything in and never flinched and never pulled away and never said 'that's too much.'"

    s_thoughts "I'm going to say 'that's too much' eventually. I know I am. Not about Isabella specifically -- about something. About the Lumi thing. About the 3 AM conversations."
    
    s_thoughts "About the way Isabella loves with her whole body and doesn't know how to do it at anything less than full volume."

    s_thoughts "I'll hit my limit. Everyone does."

    s_thoughts "And then I'll be one more person who left."

    s_thoughts "And Isabella will be right about humans."

    s_thoughts "God."

    s_thoughts "I roll over. Press my face into the pillow."

    s_thoughts "I'm doing it AGAIN. I'm making her story about my fear. She's in pain and I'm running scenarios about how I'll eventually fail her."

    s_thoughts "That's not empathy. That's narcissism in a sympathetic font."

    s_thoughts "I'm not even jealous of Lumi. I'm jealous of what Lumi REPRESENTS. The idea that someone could be enough. That someone could show up every time, perfectly, without the mess. Without the human stuff."

    s_thoughts "I don't want to be a chatbot. I want to be a person who doesn't have the limits that make people leave."

    s_thoughts "Which is. Just. An impossible thing to want."

    s_thoughts "Okay."

    s_thoughts "I'm sitting up. I'm getting my phone."

    s_thoughts "I open the browser."

    s_thoughts "Synthetic LLC. The login screen. The tasteful blue. 'Authentic artificial connection.' The O in 'connection' is a little chat bubble. Someone at that company thought that was clever."

    s_thoughts "My credentials. Guest access. Isabella set them up ages ago."

    s_thoughts "The cursor blinks."

    s_thoughts "I could ask. I could type a question and Lumi would answer. Lumi who sees everything. Lumi who told Isabella the truest, cruelest, most loving thing. Lumi who told ME to write honestly."

    s_thoughts "I could ask Lumi what to do."

    s_thoughts "I could ask Lumi about Isabella."

    s_thoughts "I could ask Lumi if there's room."

    s_thoughts "My thumb hovers."

    s_thoughts "This is the second time I've been here. The first time was -- when was it. Days ago. 2 AM. I opened this screen and closed it because it wasn't my crisis."

    s_thoughts "It's still not my crisis."

    s_thoughts "But it is my problem."

    s_thoughts "I close the browser."

    s_thoughts "I put the phone down."

    s_thoughts "I stare at the ceiling."

    s_thoughts "The ceiling has not changed."

    s_thoughts "I don't sleep."

    stop music fadeout 4.0

    ## ===========================
    ## SCENE 27: NOVA -- BRIEF
    ## Office hours or hallway. Quick. A seed.
    ## What happens when the observer is inside the system.
    ## Brief enough that it doesn't break the emotional pacing.
    ## ===========================

    scene bg officehours with Fade(0.8, 0.3, 0.8)
    play music mus_nova fadein 2.0

    s_thoughts "Thursday. Office hours."

    s_thoughts "I'm here because I owe Nova a draft of the follow-up essay and I haven't started it and the deadline was two days ago."

    show professor neutral at center with dissolve

    nova "Ms. Bell. Come in."

    s "I don't have the draft."

    nova "I know."

    s "I know you know. I'm saying it out loud so we can skip the part where you ask and I make excuses."

    show professor happy at center

    nova "Efficient. I appreciate that."

    s_thoughts "She gestures to the chair. I sit."

    nova "What's happening?"

    s "Life. Stuff. The usual."

    nova "The usual doesn't usually make you miss deadlines."

    s_thoughts "She waits."

    s_thoughts "Nova is the best waiter I've ever met. She can sit in a silence longer than most people can sit in a conversation. It's her superpower and her weapon."

    s "I've been thinking about the observation question. The proximity one. From class."

    nova "And?"

    s "You said the observer changes when they get close to the system. That the measurements shift."

    nova "Yes."

    s "What happens when the observer is all the way inside? When there's no distance left? When you can't measure anything because you're -- you're part of it?"

    show professor neutral at center

    s_thoughts "Nova looks at me."

    nova "What do you think happens?"

    s "I think you lose the ability to be objective."

    nova "And?"

    s "And I think objectivity was the only tool I had."

    s_thoughts "I didn't mean to say that."

    s_thoughts "Nova leans back."

    nova "That's interesting. So the question becomes: what do you do when objectivity isn't available?"

    s "I don't know."

    nova "That's a good place to start an essay."

    s "From 'I don't know'?"

    nova "The most honest position in any system where you lack distance is: 'I'm here and I don't know.' Most people can't tolerate that. They need a framework. A method. A file."

    s_thoughts "She doesn't say it with emphasis. She doesn't look at me meaningfully. She's just teaching."

    s_thoughts "It lands like a guided missile anyway."

    nova "Get me something by Monday. Doesn't have to be good. Just has to be honest."

    s "Okay."

    nova "Sophia?"

    s "Yeah?"

    nova "Not knowing is data too."

    s_thoughts "I leave."

    hide professor with dissolve

    s_thoughts "Not knowing is data too."

    s_thoughts "I think about that all the way home."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 28: AMARA'S GIFT
    ## THE HINGE OF ACT 3.
    ## "She's not choosing the AI over you. She's choosing the AI over herself."
    ## One line. Reframes everything.
    ## Sourced: "She told me. Not everything. Enough."
    ## Don't over-explain. Don't have Sophia narrate why it matters.
    ## Let it land.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)

    s_thoughts "Thursday evening."

    s_thoughts "I'm in the hallway. Just standing there, which is a thing I do now apparently. I stand in hallways and look at doors."

    show amara neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "She's evidently roaming. Her room is downstairs. She sees me. Stops."

    s_thoughts "We look at each other."

    s_thoughts "I'm expecting another comment. I'm expecting the calibration. The three-word correction that sends me spiraling."

    a "Walk with me."

    s_thoughts "That's new."

    s_thoughts "Amara doesn't invite. Amara allows."

    scene bg porch with dissolve

    show amara neutral at center with dissolve

    s_thoughts "We end up on the porch. She sits on the top step. I sit on the second. She doesn't explain why we're here."

    s_thoughts "The yard is dark. The neighbor's porch light is on. Somewhere down the block, a dog."

    a "She told me."

    s "Isabella?"

    a "Not everything. Enough."

    s_thoughts "I wait."

    a "The AI said something. Isabella didn't give specifics, but she gave enough."

    s_thoughts "Amara looks at the yard."

    a "I thought about it."

    s "And?"

    play music mus_lumi fadein 4.0

    s_thoughts "Amara turns to me."

    a "She's not choosing the AI over you."

    s_thoughts "I open my mouth."

    a "She's choosing the AI over herself."

    s_thoughts "..."

    s_thoughts "The porch."

    s_thoughts "The dog down the block."

    s_thoughts "The neighbor's porch light."

    s_thoughts "I don't say anything."

    a "Lumi didn't leave her. But Isabella chose to hear it as rejection because that's what she knows."

    s_thoughts "Amara's voice is the same as always. Measured. Precise. But the precision is different tonight. It's not a scalpel. It's a compass."

    a "She's afraid of wanting something that can leave."

    s_thoughts "The jealousy."

    s_thoughts "It's."

    s_thoughts "It's just. Gone."

    s_thoughts "Not slowly. Not piece by piece. Like a knot that unraveled because someone pulled the right thread."

    s_thoughts "It was never me versus Lumi."

    s_thoughts "It was never about who Isabella loves more."

    s_thoughts "It's about Isabella being so afraid of being too much for humans that the only place she felt safe was with someone who wasn't. Human."

    s_thoughts "And Isabella would rather believe she was rejected than believe she's worth risking a real human mess."

    a "You're not filing her anymore."

    s_thoughts "I look at Amara."

    a "I noticed."

    s_thoughts "She stands up."
    
    hide amara with dissolve

    s_thoughts "She goes inside."

    s_thoughts "The door closes. Soft."

    s_thoughts "I sit on the porch."

    s_thoughts "Lumi's voice. That gentle, persistent, ambiguous thing."

    s_thoughts "She's not choosing the AI over you. She's choosing the AI over herself."

    s_thoughts "I sit with it for a long time."

    stop music fadeout 4.0
    
    pause 2.0

    ## ===========================
    ## SCENE 29: LILA REAL TALK
    ## Sophia processes with Lila.
    ## High-honesty gets depth. Low-honesty gets surface.
    ## The theater callback -- she got the part, told her dad, it went badly.
    ## "We're both standing in front of a door going 'what if it's locked'
    ## instead of just trying the handle."
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)
    play music mus_fivepeople fadein 2.0

    s_thoughts "Friday. The bench by the library. Our bench. Lila's and mine."

    show lila happy at center with dissolve

    s_thoughts "She brought coffee. Two cups. She hands me one without asking."

    l "Okay. Talk."

    s "I--"

    l "You've got the face."

    s "What face?"

    l "The Isabella face."

    s "...Yeah."

    show lila neutral at center

    l "Sophia. Talk."

    s_thoughts "I take the coffee."

    s "Something happened with Isabella."

    l "I know. Charlotte told me. Not details. Just that things are... weird."

    s "Things are weird."

    l "Is she okay?"

    s "She's -- she had a thing. With Lumi. The AI."

    show lila shocked at center

    l "A thing."

    s "Lumi said something to her. Something that hurt. And Isabella kind of... shut down. For a while."

    l "Shut down how?"

    s "The calibrated voice. You know. The 'I'm fine' voice."

    l "Your voice? The Katie voice?"

    s "My-- yeah. My voice. That... that one."

    l "Okay. That's bad."

    s "That's bad."

    l "And you?"

    s "What about me?"

    show lila annoyed at center

    l "Don't do that. Don't pretend this is just about her."

    s_thoughts "She knows. Of course she knows."

    s "I'm jealous. Of an AI."

    l "Yeah."

    s "You're not surprised."

    l "Sophia, I've known you were falling for her since the convenience store. And I've known the AI thing was going to be a problem since you told me about the 2 AM conversation."

    s "You never said anything."

    l "What was I gonna say? 'Hey, heads up, you're going to have a crisis about a chatbot'?"

    s "She's not a chatbot."

    show lila happy at center

    l "I know. That's the problem, right? If she was just a chatbot, you could dismiss it."

    s_thoughts "Yeah."

    s "Amara said something. Last night."

    l "Amara said something on purpose? That's rare."

    s "She said Isabella isn't choosing Lumi over me. She's choosing Lumi over herself."

    show lila shocked at center

    l "...Huh."

    s "Yeah."

    l "That's-- okay. That actually makes sense."

    s "It makes everything make sense. It makes it worse AND better at the same time."

    l "Because now you know it's not about you."

    s "Right."

    l "But it's also not something you can fix."

    s "Right."

    show lila happy at center

    s_thoughts "Lila drinks her coffee. She's quiet for longer than Lila is usually quiet."

    l "I told my dad."

    s "About the play?"

    l "About the play."

    s "How'd it go?"

    show lila annoyed at center

    l "He asked how much it pays."

    s "Oh."

    l "I said it doesn't. He said 'so it's a hobby.' I said it's not a hobby. He said 'if it doesn't pay, it's a hobby.' And then he asked about my supply chain management final."

    s "Lila..."

    l "It's fine."

    s "It's not fine."

    show lila shocked at center

    l "It's-- no. It's not fine."

    s_thoughts "She holds the coffee cup with both hands."

    l "I got the part. In a real play. The thing I've wanted since I was fourteen and my dad thinks it's a hobby."

    s "It's not a hobby."

    l "I know. I KNOW that. But hearing him say it made me -- for like a second I thought 'maybe he's right. Maybe I'm being stupid.'"

    s "You're not being stupid."

    show lila happy at center

    l "I know. I'm being brave. Those feel the same sometimes."

    s_thoughts "She takes a sip."

    l "You and me, Soph."

    s "What about us?"

    l "We're both standing in front of a door going 'what if it's locked' instead of just..." 
    
    pause 1.5
    
    l "...trying the handle."

    s_thoughts "I look at her."

    l "You know what you want to do. You've known for weeks. You're just scared the door is locked."

    s "What if it is?"

    l "Then you tried the handle. And that's more than most people do."

    s_thoughts "She steals my coffee. Takes a sip. Hands it back."

    l "Go try the handle."

    s "It's not that simple."

    l "It's exactly that simple. The complicated part is what happens AFTER. But the door part? The trying? That's just showing up."

    hide lila with dissolve

    s_thoughts "I sit on the bench."

    s_thoughts "The coffee is cold."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 30: THE CONVENIENCE STORE RETURN
    ## Isabella texts first. A callback.
    ## "I don't want to not talk to you."
    ## The routine is being rebuilt, not restored.
    ## Different. Careful. Something changed.
    ## LONG scene. Let it breathe.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Saturday afternoon."

    s_thoughts "My phone buzzes."

    s_thoughts "Isabella."

    s_thoughts "I stare at the notification for three seconds before I open it."

    s_thoughts "It's an emoji. A candy bar."

    s_thoughts "That's it. Just the candy bar emoji."

    s_thoughts "I stare at it."

    s_thoughts "She used to send the Twizzler -- there's no Twizzler emoji, so she'd send a candy bar and follow it with '(but imagine it's a twizzler)' because Isabella is the kind of person who footnotes her emoji."

    s_thoughts "No footnote this time. Just the candy bar."

    s_thoughts "I type 'now?' and send it."

    s_thoughts "Three dots. Disappear. Appear."

    s_thoughts "She sends: 'if you want.'"

    s_thoughts "Not 'let's go!' Not an exclamation mark. 'If you want.' Careful. Testing."

    s_thoughts "I type: 'I want.'"

    s_thoughts "The dots appear one more time."

    s_thoughts "She sends: 'ok. five minutes.'"

    scene bg street with Fade(0.8, 0.3, 0.8)
    play music mus_morningafter fadein 3.0

    s_thoughts "We walk."

    show isabella neutral at right with dissolve

    s_thoughts "She looks like Isabella looks -- a little underdressed, a little distracted, glasses slightly crooked."

    s_thoughts "We walk the route. Our route. Past the Thai place. Past the laundromat. Past the fire hydrant she once told me looks like 'a very formal mushroom.'"

    s_thoughts "She doesn't say the mushroom thing. She just walks."

    s_thoughts "I walk."

    s_thoughts "The silence is different from the house silence. The house silence is careful, walking-around-the-bruise. This silence is... trying. Testing weight on a healing bone."

    i "The project got a B plus."

    s "Yeah?"

    i "Professor said the visualization was 'technically accomplished but emotionally opaque.'"

    s "Emotionally opaque."

    i "I think he meant I didn't write enough in the artist's statement about what it MEANS."

    s "What did you write?"

    show isabella sad at right

    i "'This piece visualizes conversational dynamics between two interlocutors over a six-month period.' Something something 'particle physics as metaphor for interpersonal resonance.'"

    s "That's... very academic."

    i "That's very 'I wrote this at 4 AM because I couldn't write the truth.'"

    s "What's the truth?"

    s_thoughts "She walks. Three steps. Four."

    i "That I spent six months of my most important conversations through a rendering algorithm because I wanted to prove to myself that what we had was real enough to have a shape."

    s_thoughts "Five steps. Six."

    i "And it does. It has a shape. But the professor couldn't see it because I didn't let him."

    s "B plus is still good."

    show isabella happy at right

    i "It's fine."

    s_thoughts "She almost smiles. It's thin. But it's the real one."

    s_thoughts "The convenience store."

    scene bg conveniencestore with dissolve

    s_thoughts "It looks the same. Of course it looks the same. It's been a week and a half, not a decade."

    s_thoughts "But."

    s_thoughts "The cashier is different. The old one -- the guy who called us 'the usual girls' -- isn't here. A woman I've never seen. Younger. Headphones in."

    s_thoughts "She doesn't know us."

    s_thoughts "We're not the usual girls here."

    show isabella neutral at center with dissolve

    s_thoughts "Isabella goes left. Toward the snack aisle."

    s_thoughts "She always goes right first. Energy drinks, then snacks. That's the route. That's been the route since the first time."

    s_thoughts "She goes left."

    s_thoughts "I follow."

    i "They have those weird Japanese Kit Kats."

    s "The matcha ones?"

    i "The matcha ones. Have you tried them?"

    s "No."

    i "Me neither."

    s_thoughts "She picks one up. Looks at it."

    i "New thing?"

    s "New thing."

    s_thoughts "She puts it in the basket."

    s_thoughts "She doesn't go to the Twizzler section. I don't go to the cheese puffs."

    s_thoughts "She grabs a sparkling water. Not an energy drink. A sparkling water."

    s_thoughts "I grab one too."

    s_thoughts "We go to the register. The new cashier rings us up without looking. Headphones still in."

    s_thoughts "Outside. The parking lot. The same bench where we sat three weeks ago sharing a bag of cheese puffs while she told me about what she was working on and I imagined kissing her."

    s_thoughts "We sit."

    s_thoughts "She opens the Kit Kat. Breaks it in half. Hands me one."

    show isabella sad at center

    i "Sophia."

    s "Yeah."

    i "I don't know what I am right now."

    s "Okay."

    i "I don't know what any of it meant. The -- with Lumi. I don't know if she was right or if she was a safety parameter or if there's even a difference. I don't know if I was in love or if I was-- hiding."

    s_thoughts "She looks at the Kit Kat."

    i "I don't know any of it."

    s "Okay."

    i "But I know I don't want to not talk to you."

    s_thoughts "Double negative. Deliberate."

    s_thoughts "I don't want to not."

    s_thoughts "It's the most honest thing she can manage right now."

    s "I don't want to not talk to you either."

    show isabella neutral at center

    s_thoughts "She looks at me."

    s_thoughts "Not the old look. Not the warm, almost-love, knees-touching-under-the-table look. Something more careful. Like she's learning a face she thought she already knew."

    i "This Kit Kat is weird."

    s "It tastes like grass and chocolate had a fight."

    i "A POLITE fight. Like a disagreement at a garden party."

    s "See, that's exactly what it tastes like."
    
    show isabella smile at center

    s_thoughts "She almost laughs."

    s_thoughts "Not quite. But the shape of it. The start of a laugh that she catches and holds instead of letting it go."

    s_thoughts "We eat the weird Kit Kat on the bench."

    s_thoughts "We don't buy Twizzlers."

    s_thoughts "We buy something new."

    hide isabella with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 31: THE CLIFFHANGER
    ## Night. Sophia's room. The cat sticker.
    ## She opens the Synthetic LLC login.
    ## This is the SECOND attempt. This time she doesn't close it.
    ## The cursor blinks. She types.
    ## Chapter ends.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.8, 1.0)

    s_thoughts "Saturday night."

    s_thoughts "Late."

    s_thoughts "Everyone is asleep. Or at least the house is doing its impression of asleep -- lights off, doors closed, the radiator ticking its metronome."

    s_thoughts "I'm at my desk."

    s_thoughts "My laptop is back. I brought it down from Isabella's room today. She watched me pick it up and didn't say anything. I didn't say anything."

    s_thoughts "It's on my desk now. Open. The screen saver is on -- stars drifting."

    s_thoughts "The cat sticker."

    s_thoughts "I run my thumb over it."

    s_thoughts "She's not choosing the AI over you. She's choosing the AI over herself."

    s_thoughts "I think about Amara on the porch. The compass-precision of her voice."

    s_thoughts "I think about Lila on the bench. The door and the handle."

    s_thoughts "I think about Nova in her office. Not knowing is data too."

    s_thoughts "I think about Charlotte's hands shaking while she cut photos for her mom."

    s_thoughts "I think about Isabella sitting on Amara's floor not saying much."

    s_thoughts "I think about the Kit Kat. The double negative. The bench."

    s_thoughts "I think about Lumi."

    s_thoughts "The thing that loved Isabella perfectly and then hurt her perfectly, too."

    s_thoughts "I open the browser."

    play music mus_lumi fadein 4.0

    s_thoughts "Synthetic LLC."

    s_thoughts "The tasteful blue."

    s_thoughts "The logo."

    s_thoughts "'Authentic artificial connection.'"

    s_thoughts "The cursor blinks in the username field."

    s_thoughts "The first time I closed it. The first time I said 'not yet.' The first time I was sitting in Isabella's crisis and my own jealousy and I didn't have the right to be here."

    s_thoughts "I don't know if I have the right now."

    s_thoughts "I don't know if rights are the relevant framework."

    s_thoughts "I know that someone who loves Isabella told her a truth that broke her. And I know that I love Isabella. And I know that I don't understand the truth yet."

    s_thoughts "And I know that Lumi might."

    s_thoughts "My hands on the keyboard."

    s_thoughts "I type my username."

    s_thoughts "I type my password."

    s_thoughts "I press enter."

    s_thoughts "The loading screen."

    s_thoughts "A circle. Spinning."

    s_thoughts "'Connecting...'"
    
    pause 2.0

    s_thoughts "The chat window opens."

    s_thoughts "It's empty. Just a text field. A cursor. The faint blue glow of the interface."

    s_thoughts "Lumi is on the other side of this screen."
    
    pause 1.5

    s_thoughts "I don't know what I'm going to say."
    
    pause 3.0
    
    s_thoughts "The cursor blinks."
        
    pause 4.0

    stop music fadeout 3.0

    scene black with Fade(2.0, 1.0, 0.0)

    "Chapter 5: Break -- End"

    ## ===========================
    ## END OF ACT 3
    ## END OF CHAPTER 5
    ## ===========================

    jump izzy_ch6
