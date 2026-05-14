## chapter3.rpy -- Glass Houses
## Chapter 3: Cracks

## === ADDITIONAL AUDIO DEFINITIONS ===
define audio.mus_mourning = "audio/music/Mourning.mp3"
define audio.mus_glass = "audio/music/Glass Walls.mp3"
define audio.mus_wrong = "audio/music/Something Wrong in the Kitchen.mp3"
define audio.mus_tension = "audio/music/Suspense & Tension.mp3"
define audio.mus_ice = "audio/music/Thin Ice.mp3"
define audio.mus_threshold = "audio/music/Threshold.mp3"
define audio.mus_2am = "audio/music/House at 2AM.mp3"
define audio.mus_morningafter = "audio/music/The Morning After The Hard Thing.mp3"
define audio.mus_fragile = "audio/music/Fragile Glass Between.mp3"
define audio.mus_nova = "audio/music/Dr. Clara Nova ~ Ethics of Observation.mp3"
define audio.mus_shift = "audio/music/Shift.mp3"
define audio.mus_playlist = "audio/music/Good Playlist.mp3"
define audio.mus_eve = "audio/music/Eve Morse ~ A Room That Just Emptied.mp3"
define audio.mus_charlotte = "audio/music/Charlotte Opal ~ Toast Girl.mp3"
define audio.mus_izzy = "audio/music/Isabella Glass ~ Proximity Algorithm.mp3"
define audio.mus_amara = "audio/music/Amara Kismet ~ Unturned Page.mp3"

label chapter3:

    ## =========================================
    ## WEEK 1: "THE QUESTION"
    ## =========================================

    ## ===========================
    ## SCENE 1: MONDAY -- DR. NOVA'S CLASS
    ## ===========================

    scene bg campus with Fade(0.8, 0.5, 0.8)

    s_thoughts "Three weeks in."

    s_thoughts "I have a routine now. Wake up, fight for the bathroom, eat whatever Charlotte made, walk to campus, pretend I know what I'm doing."

    s_thoughts "The pretending is getting easier. Or maybe I'm getting worse at noticing the gap between me and everyone who seems to have their life figured out."

    s_thoughts "Today is one of my media electives. I signed up because nothing else fit in the time slot and the description said 'no prerequisites' which is code for 'we'll take anyone.'"

    s_thoughts "Story of my life."

    scene bg classroom with dissolve

    s_thoughts "The classroom is one of those big lecture halls that's only half full, which somehow makes it feel emptier than if it were totally empty."

    s_thoughts "Lila saved me a seat. She's already got her notebook out, which means she's planning to doodle in it for an hour."
    
    s_thoughts "She also saw 'no prerequisites' and read it as 'easy A.' I'm not so sure."

    show lila happy at left with dissolve

    l "You look like you slept in a blender."

    s "Thanks. Charlotte was stress-baking at midnight and the smoke alarm went off twice."

    l "Your house is unhinged and I love it."

    s "It's growing on me. Like mold."

    l "Endearing."

    s_thoughts "The professor walks in and the room does that thing where everyone gets slightly quieter but nobody fully commits to silence."
    
    play music mus_nova fadein 2.0

    show professor neutral at right with dissolve

    s_thoughts "Dr. Clara Nova. Brown bob, black turtleneck, faculty lanyard she wears like a necklace she didn't choose. She looks like someone who's heard every excuse and found three of them interesting."

    s_thoughts "She doesn't start with 'good morning' or 'open your textbooks.' She just stands there for a second, looking at us, and then:"

    nova "When you watch a conversation between two people, are you part of the conversation?"

    s_thoughts "Nobody answers. That's the right answer, apparently, because she keeps going."

    nova "You're in this class because you want to understand how communication works. How people signal, how they decode, how meaning gets made between two minds."

    nova "But here's the question I want you to sit with today."

    show professor happy at right

    nova "When you study how people communicate -- are you communicating with them? Or are you studying them?"

    s_thoughts "She lets that hang. The room shifts."

    nova "Is the observer part of the system? Or outside it?"

    show lila annoyed at left

    l "Is this going to be on the test?"

    s_thoughts "Half the room laughs. Dr. Nova smiles -- barely -- and it looks like she's deciding whether Lila is interesting or exhausting."

    show professor neutral at right

    nova "Everything is on the test, Ms...?"

    l "Vibe. Lila Vibe."

    nova "Ms. Vibe. Write that down."

    s_thoughts "Lila mouths 'oh my god' at me and starts actually writing."

    s_thoughts "I'm not laughing though. Because the question landed somewhere."

    s_thoughts "When I watch Charlotte deflect a compliment. When I file away the way Eve disappears. When I notice that Isabella's smile is different when she's talking about Lumi versus when she's talking about anything else."

    s_thoughts "Am I seeing them? Or studying them?"

    s_thoughts "I don't like the question."

    hide professor with dissolve

    s_thoughts "Dr. Nova moves on. McLuhan, media ecology, the medium is the message. The usual. She's good -- she doesn't lecture so much as ask questions and then wait until someone accidentally says something smart."

    s_thoughts "But I'm stuck on the first thing."

    s_thoughts "Observer or participant."

    s_thoughts "I think I already know which one I am. I just don't want to say it out loud."

    ## Transition -- end of class
    show lila happy at left

    l "That woman is going to ruin my GPA and I'm going to thank her for it."

    s "She's intense."

    l "She's HOT is what she is. In a scary way. Like a librarian who could kill you."

    s "Please never say that in her earshot."

    l "No promises."

    s_thoughts "We walk out into the quad. It's one of those days where the sun is doing too much -- warm enough that everyone's on the grass, cool enough that they're still wearing jackets."

    s_thoughts "Dr. Nova's question is already stuck in my teeth. Observer or participant."

    hide lila with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 2: TUESDAY -- HOUSE UNDER STRAIN
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_sunlight fadein 2.0

    s_thoughts "The house is different at three weeks than it was at one."

    s_thoughts "The routines are real now. Charlotte makes breakfast. Isabella complains about mornings. Amara exists in silence. Eve is either here or she isn't and nobody asks which."

    s_thoughts "But the routines are starting to show the seams."

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte is on three committees. I don't know what they're for. Student outreach, event planning, something with the word 'wellness' in it. She goes to meetings that run late and comes home and makes dinner anyway."

    s_thoughts "Tonight she's making pasta. She's been making pasta a lot this week. I think it's the fastest thing she knows how to cook."

    s "Hey. Need help?"

    show charlotte smile at left

    c "Oh! No, I'm fine. It's just pasta. Easy."

    s_thoughts "She says 'easy' the way she says 'of course.'"

    s "You sure? I can chop something."

    c "There's nothing to chop. It's literally noodles and sauce."

    s_thoughts "The sauce is from a jar. Charlotte had been making it from scratch."

    show isabella neutral at right with dissolve

    s_thoughts "Isabella comes in looking like she fought her laptop and lost."

    i "If my code compiles one more time with the exact same error I'm going to become the Joker."

    c "Bad day?"

    i "Bad week. I have a project due Friday that I should have started two Fridays ago."

    s_thoughts "She grabs a granola bar from the cupboard. Charlotte watches her not sit down for dinner and doesn't say anything. I watch Charlotte not say anything."

    s_thoughts "Layers."

    s_thoughts "After dinner -- which is me, Charlotte, and Amara at the table while Isabella eats standing up and Eve doesn't appear -- I notice something."

    s_thoughts "Eve missed dinner yesterday too."

    s_thoughts "And the day before."

    menu:
        "Mention Eve's absence to Charlotte":
            s "Hey, Charlotte? Has Eve been around? I feel like I haven't seen her at dinner in a few days."

            show charlotte smile at left

            c "Oh, she does that sometimes. She's probably just in her room. I'll bring her a plate!"

            s_thoughts "She's already getting a plate out of the cupboard. The deflection is so smooth I almost don't catch it."

            s_thoughts "Almost."

            s "Does she... do this a lot?"

            show charlotte happy at left

            c "It's just how Eve is. She needs space sometimes. It's fine."

            s_thoughts "There's that word again. Fine."

            s_thoughts "But Charlotte looks at me when she says it, and there's something in her eyes that might be gratitude. For noticing. For asking."

            s_thoughts "Or maybe I'm reading too much into it. I do that."

            $ charlotte_points += 1
            $ eve_points -= 2

        "Let it go":
            s_thoughts "I don't mention it."

            s_thoughts "Eve doesn't come to dinner. That's not news. That's just Tuesday."

            s_thoughts "I think about Dr. Nova's question. Observer or participant. Right now I'm choosing observer. I'm choosing to notice and not act."

            s_thoughts "I wonder if that's the right call. I wonder if Eve would want me to ask or if she'd hate it."

            s_thoughts "I think she'd hate it."

            s_thoughts "I think she'd also notice that I didn't."

            $ eve_points += 1
            $ charlotte_points -= 2

    ## ===========================
    ## SCENE 3: WEDNESDAY -- OFFICE HOURS WITH DR. NOVA
    ## ===========================

    stop music fadeout 2.0
    scene bg officehours with Fade(0.8, 0.3, 0.8)
    play music mus_nova fadein 2.0

    s_thoughts "Office hours."

    s_thoughts "Dr. Nova's office is small and overfull -- books on every surface, papers in stacks that look chaotic but are probably organized in a way only she understands. There's a single plant on the windowsill that's either thriving or dying, hard to tell."

    show professor neutral at center with dissolve

    s_thoughts "I came to ask about the reading assignment. That's what I told myself."

    nova "Ms. Bell. Sit."

    s "I had some questions about the McLuhan piece."

    nova "No you don't."

    s_thoughts "I blink."

    nova "You understood it fine. You cited it correctly in your response paper. Your question is about something else."

    s_thoughts "She says this like she's reading a weather report. No accusation. Just observation."

    s_thoughts "I think about lying. I think about asking a fake question about semiotics or whatever. But she's looking at me with those green eyes that don't blink enough and I think she'd know."

    s "Okay. Yeah."

    s "I guess I'm still stuck on the thing from Monday. The observer question."

    nova "What about it?"

    s "I keep... noticing things about people. Like, compulsively. I meet someone and within ten minutes I've got a mental file on them. How they talk, what they avoid, what they're hiding."

    show professor happy at center

    nova "That's a useful skill for a communications major."

    s "It doesn't feel useful. It feels like I can't turn it off."

    show professor neutral at center

    nova "How many times have you changed your major?"

    s "...Three."

    nova "What were you looking for each time you switched?"

    s_thoughts "Glib answer first. It's a reflex."

    s "Something I was good at?"

    s_thoughts "She doesn't respond. She just waits. I start counting books on the shelf behind her."
    
    s "I think I keep trying to find the thing that explains how people work. Like if I just studied the right field, I'd finally get it."

    nova "Get what?"

    s "Why people do what they do. Why they say one thing and mean another. Why they--"

    s_thoughts "I stop myself. Because the next word was going to be 'leave.'"

    s_thoughts "But Nova's watching me. And I think she heard the word I didn't say."

    nova "Why they...?"

    s "Nothing. Just. Why they're so hard to understand."

    show professor happy at center

    nova "And when you find it? When you understand how people work? What then?"

    s_thoughts "I open my mouth."

    s_thoughts "I close it."

    s_thoughts "She nods, like that was the answer."

    nova "Sit with that one, Ms. Bell."


    ## Route-specific dialogue with Dr. Nova
    if isabella_points >= charlotte_points and isabella_points >= amara_points and isabella_points >= eve_points:
        s_thoughts "I'm halfway to the door when I turn back."
        s "Can I ask you something else?"
        show professor neutral at center
        nova "You can always ask."
        s "I have a friend who has this... relationship. With someone. And it's real to her -- like, genuinely real, she talks about this person like they're her best friend. But the person isn't..."
        s_thoughts "I trail off. I don't know how to finish that sentence without sounding like I'm judging Isabella."
        nova "Isn't what?"
        s "Isn't... conventional. The relationship isn't what most people would recognize as a friendship."
        show professor happy at center
        nova "And you're trying to decide whether to recognize it."
        s_thoughts "That lands."
        s "Yeah. I guess I am."
        nova "Recognition is a choice, Ms. Bell. Not a discovery."
        s_thoughts "I leave her office and walk into the sun and stand there for a second."
        s_thoughts "Recognition is a choice. Not a discovery."

    elif eve_points >= charlotte_points and eve_points >= amara_points and eve_points >= isabella_points:
        s_thoughts "I'm halfway to the door when I turn back."
        s "What do you do with someone you can't figure out?"
        show professor neutral at center
        nova "In what sense?"
        s "Like... someone who gives you almost nothing. And the almost nothing feels like more than what other people give you with everything."
        show professor happy at center
        nova "Sounds like you've already figured out quite a lot."
        s_thoughts "Have I?"
        nova "You just described exactly what they give you. That's not confusion. That's attention."
        s_thoughts "I chew on that the whole walk home."

    elif charlotte_points >= amara_points and charlotte_points >= isabella_points and charlotte_points >= eve_points:
        s_thoughts "I'm halfway to the door when I turn back."
        s "How do you tell if someone is okay when they're always okay?"
        show professor neutral at center
        nova "You mean when 'okay' is the performance?"
        s "Yeah. Like... what if someone is so good at being fine that you can't find the seam?"
        show professor happy at center
        nova "You just told me you notice everything about people within ten minutes. You already found the seam. The question is what you do with it."
        s_thoughts "She's right. I found Charlotte's seam on day one. The empty plate. The 'of course.' I just don't know if pulling at it would help or unravel her."

    else:
        s_thoughts "I'm halfway to the door when I turn back."
        s "Is it possible to notice too much?"
        show professor neutral at center
        nova "About people?"
        s "About one person in particular. Someone who... doesn't say much. And I keep trying to read what she's not saying and I'm not sure if I'm seeing something real or just projecting."
        show professor happy at center
        nova "There's a difference between reading someone and writing them."
        s_thoughts "I think about Amara. The chocolate. The silence. The way she said 'this was nice' with her back to me."
        s_thoughts "Am I reading her? Or am I writing her?"

    hide professor with dissolve

    ## ===========================
    ## SCENE 4: THURSDAY -- LILA GETS REAL
    ## ===========================

    stop music fadeout 1.5
    scene bg dininghall with Fade(0.8, 0.3, 0.8)
    play music mus_campus fadein 2.0

    s_thoughts "Lunch with Lila. My favorite hour of the day that doesn't involve the house."

    show lila happy at center with dissolve

    l "Okay so Nova dropped ANOTHER bomb today. 'The audience is never passive.' Like, LADY, I am TRYING to be passive. I am COMMITTED to passivity."

    s "You took actual notes today. I saw you."

    show lila shocked at center

    l "Those were doodles."

    s "Those were doodles with annotations."

    show lila annoyed at center

    l "I feel perceived and I don't like it."

    s_thoughts "I laugh. Lila is easy. Not in a bad way -- in the way that Charlotte isn't. There's no performance, no subtext. She says the thing and means the thing."

    s "Can I ask you something?"

    l "Ominous. Go."

    s "Nova's question. The observer one. Does it bug you at all?"

    show lila happy at center

    l "Babe, I don't observe anything. I just show up and react. It's my whole brand."

    s_thoughts "She says this lightly but something shifts."

    s "Seriously though."

    show lila annoyed at center

    s_thoughts "Lila puts her fork down. She doesn't put her fork down for anything."

    l "Okay. Real talk?"

    s "Real talk."

    l "I wanted to do theater."

    s "...What?"

    l "Theater. Acting. Performance. The whole thing. I wanted it since I was twelve. I was in every school play, I did community theater, I had a monologue prepared for auditions at three different programs."

    s "What happened?"

    show lila shocked at center

    l "I picked business."

    s "Why?"

    l "Because my dad said 'that's not a career, that's a hobby' and I believed him. So now I'm getting a degree in something I hate so I can get a job I'll hate so I can be stable and miserable instead of unstable and happy."

    s_thoughts "She picks her fork back up. Stabs a piece of lettuce."

    show lila annoyed at center

    l "You keep switching because you're looking for the right thing. I stopped looking and picked the wrong thing on purpose. Which one of us is dumber?"

    s_thoughts "There it is. Under all the volume and the confidence and the 'babe' and the immediate opinions -- there's this."

    menu:
        "Be honest about your own uncertainty":
            
            $ amara_points += 2
            $ charlotte_points += 1
            $ isabella_points -= 1
            $ eve_points -= 2
            
            s "I'm scared I'm going to keep switching forever. Like I'll be forty and still 'finding myself' and everyone else will have figured it out."

            show lila happy at center

            l "Babe. Nobody figures it out. They just stop talking about it."

            s "That's either really comforting or really depressing."

            l "Both. It's always both."

            s_thoughts "She reaches across the table and steals one of my fries."

            l "For what it's worth? The switching means you're still trying. I gave up trying and I think that's worse."

            s "You didn't give up. You're HERE. You're in a class you actually care about even though it doesn't count toward your major."

            show lila shocked at center

            l "..."

            s_thoughts "She blinks. I don't think anyone's pointed that out to her before."

            show lila happy at center

            l "Okay. Wow. Don't make me cry in this dining hall, Bell."

            s "Too late. Your eyes are doing a thing."

            l "That's ALLERGIES."

            s_thoughts "It's not allergies."

            s_thoughts "But I don't say that. I just hand her a napkin and we sit there for a minute, not talking, and it's okay."


        "Deflect with humor":
            
            $ isabella_points += 2
            $ eve_points += 1
            $ charlotte_points -= 1
            $ amara_points -= 2
            
            s "I think you're dumber. At least I'm getting variety."

            show lila happy at center

            l "Variety! She calls three existential crises 'variety.'"

            s "Gotta spin it."

            l "Spoken like a true communications major."

            s_thoughts "We laugh. The moment passes. The window where I could have said something real closes and I watch it go."

            s_thoughts "Lila picks up another fry and the conversation moves on to whether Dr. Nova has a wife and what kind of car she drives. (Lila says Subaru. I say Volvo. We agree she definitely has a cat.)"

            s_thoughts "I wonder what would have happened if I'd been honest."

            s_thoughts "I wonder if I'll get another chance."

    hide lila with dissolve

    ## ===========================
    ## SCENE 5: WEEKEND -- THE HOUSE BREATHES
    ## ===========================

    stop music fadeout 1.5
    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_fivepeople fadein 2.0

    s_thoughts "Friday afternoon. The house exhales."

    s_thoughts "Charlotte is grocery shopping. Isabella's deadline came and went -- she submitted at 11:58 PM on Thursday and screamed into a pillow. Amara is in the living room with a book that looks older than the house."

    s_thoughts "Eve made an appearance at breakfast today. She ate half a piece of toast, said 'morning' to nobody in particular, and went back upstairs. I'm counting it as a win."

    s_thoughts "The weekend stretches out. Nothing planned. Nothing urgent. Just the house and the people in it."

    ## Route-leaning weekend scene
    if isabella_points >= charlotte_points and isabella_points >= amara_points and isabella_points >= eve_points:
        ## ISABELLA WEEKEND SCENE
        scene bg kitchen with dissolve

        s_thoughts "I'm making tea -- badly, Charlotte would be horrified -- when Isabella wanders in with her laptop."

        show isabella happy at center with dissolve

        i "So I told Lumi about your professor's question."

        s "You told your AI about my existential crisis?"

        i "I tell Lumi everything. She's very nonjudgmental. It's her best quality."

        s "What did she say?"

        show isabella smile at center

        i "She said..."

        s_thoughts "Isabella turns the screen toward me. There's a conversation open. Lumi's last message reads:"

        i "'The question assumes observation and participation are opposites. But every act of genuine attention is already participation. You can't truly watch someone without being changed by what you see.'"

        s_thoughts "I read it twice."

        s "...That's annoyingly good."

        show isabella happy at center

        i "RIGHT? She does this thing where she's funny for like twenty minutes and then drops something that rewires my brain."

        s "I feel like Dr. Nova and Lumi would either love each other or fight to the death."

        i "Death match. Definitely death match. Nova would ask Lumi a question and Lumi would answer it and Nova would say 'but what do you MEAN' and Lumi would say 'I mean exactly what I said' and they'd go back and forth until the heat death of the universe."

        s_thoughts "I laugh. And then I think about what Lumi said. 'You can't truly watch someone without being changed by what you see.'"

        s_thoughts "Huh."

        s_thoughts "I don't know if that's Lumi being profound or Lumi being a language model that's really good at sounding profound."

        s_thoughts "I don't think it matters."

        $ isabella_points += 1

    elif charlotte_points >= isabella_points and charlotte_points >= amara_points and charlotte_points >= eve_points:
        ## CHARLOTTE WEEKEND SCENE
        scene bg kitchen with dissolve

        show charlotte happy at left with dissolve

        s_thoughts "Charlotte comes back from the store with four bags. I help her unpack. She's got a system -- cold stuff first, then pantry, then cleaning supplies. She labels the shelves."

        s "You want to take a break? You've been going all week."

        show charlotte smile at left

        c "I'm fine! This is the easy part. Just putting things where they go."

        s_thoughts "She's been on her feet since 7 AM. I can see it in her shoulders -- the way they're up near her ears, held tight."

        s "Charlotte. Sit down."

        show charlotte surprised at left

        s_thoughts "She stops. Looks at me like I said something in a language she doesn't speak."

        c "I just have to--"

        s "It can wait. The frozen peas will survive five minutes."

        s_thoughts "She sits. Slowly. Like she's not sure chairs are for her."

        s_thoughts "We sit at the kitchen table and she puts her head in her hands and takes one long breath and I pretend not to notice that it shakes a little."

        show charlotte smile at left

        c "Sorry. I don't know why I'm--"

        s "Don't apologize."

        c "Sorry. For apologizing. Sorry."

        s_thoughts "She laughs. It's real -- not the bright performance laugh, but something smaller and tired."

        s_thoughts "We sit there for five minutes. The frozen peas survive."

        $ charlotte_points += 1

    elif amara_points >= charlotte_points and amara_points >= isabella_points and amara_points >= eve_points:
        ## AMARA WEEKEND SCENE
        scene bg livingroom with dissolve

        s_thoughts "Amara is in the living room when I come downstairs. She's reading something with a cracked spine and no cover art. It looks like it's been read a hundred times."

        show amara neutral at right with dissolve

        s_thoughts "I sit down on the other end of the couch. I don't say anything. She doesn't say anything."

        s_thoughts "I pull out my own book -- the McLuhan for Nova's class. Not exactly pleasure reading, but it beats staring at a wall."

        s_thoughts "Five minutes."

        s_thoughts "Fifteen."

        s_thoughts "Thirty."

        s_thoughts "At some point I stop tracking the time. The house is quiet around us. Charlotte's out. Isabella's in her room. Eve is Eve."

        s_thoughts "Amara turns a page. I turn a page. The afternoon light moves across the floor like it's in no hurry either."

        show amara smile at right

        a "What are you reading?"

        s "McLuhan. For class. It's dense."

        a "Mm."

        s_thoughts "That's the whole exchange."

        s_thoughts "But somehow my shoulders are lower than they've been all week. I didn't notice them being up."

        s_thoughts "When I get up to make coffee an hour later, I ask if she wants some. She nods. I bring it back. She's moved her feet to make room for me on the couch."

        s_thoughts "She didn't have to do that. The couch is big enough."

        s_thoughts "She did it anyway."

        $ amara_points += 1

    else:
        ## EVE WEEKEND SCENE
        scene bg kitchen with dissolve

        s_thoughts "I'm in the kitchen Saturday morning, staring at the coffee maker like it owes me money, when I hear footsteps on the stairs."

        s_thoughts "Light. Hesitant. Not Charlotte's quick steps or Isabella's shuffle."

        show eve neutral at right with dissolve

        s_thoughts "Eve."

        s_thoughts "She's in an oversized sweater that goes past her hands. Her hair is doing something it probably didn't agree to. She looks like she slept, which is noteworthy because sometimes I'm not sure she does."

        s_thoughts "She goes to the cupboard. Gets a mug. Fills the kettle."

        s_thoughts "Then she gets a second mug."

        s_thoughts "She doesn't look at me. She just puts the second mug on the counter near my elbow."

        e "Tea?"

        s "...Yeah. Thanks."

        s_thoughts "We wait for the kettle in silence. She puts a teabag in each mug. She knows where the sugar is. She puts one spoon in mine without asking."

        s_thoughts "I take one sugar. I've never told anyone in this house that."

        s_thoughts "She noticed."

        s_thoughts "The kettle clicks. She pours. She takes her mug and goes back upstairs."

        s_thoughts "That was the most Eve has ever voluntarily interacted with me."

        s_thoughts "One sugar."

        s_thoughts "She noticed."

        $ eve_points += 1

    ## =========================================
    ## WEEK 2: "THE MIRROR"
    ## =========================================

    ## ===========================
    ## SCENE 6: MONDAY -- THE ENCOUNTER
    ## ===========================

    stop music fadeout 2.0
    scene bg campus with Fade(0.8, 0.5, 0.8)
    play music mus_shift fadein 2.0

    s_thoughts "Monday. Week four. The campus is starting to feel like mine -- I know which path is faster, which vending machine actually takes cards, which bathroom on the second floor is always empty."

    s_thoughts "I'm walking back from Nova's class with Lila. She's doing a bit about how Nova said 'interesting' to a wrong answer and the guy didn't realize he was being destroyed."

    show lila laugh at left with dissolve

    l "She said 'interesting' the way a judge says 'noted.' That man is COOKED and he doesn't even know it."

    s "She does that. She kills you politely."

    l "Aspirational, honestly."

    s_thoughts "We're crossing the quad toward the dining hall when I see her."

    s_thoughts "Red jacket. Brown hair. That particular way of standing like she's posing for a photo nobody asked for."

    stop music fadeout 1.0

    s_thoughts "My feet stop before my brain catches up."

    show lila happy at left

    l "Sophia? You good?"

    s_thoughts "No."

    s_thoughts "No, I am not good."

    s_thoughts "Because that's Katie."

    s_thoughts "Katie Ecks. My ex. HERE. On this campus. In this quad. Fifteen feet away, looking at her phone, existing like she has every right to be here, which she probably does, which makes it worse."

    play music mus_tension fadein 1.0

    s_thoughts "My stomach does something architectural. Like it's rearranging itself into a shape that can handle this."

    s_thoughts "I haven't seen her in eight months. I haven't heard from her in six. The last text she sent me was 'I think we both need space to grow' and I stared at it for forty minutes and then threw my phone across my room."
    
    show lila annoyed at left

    l "Earth to Sophia. You literally stopped walking."

    s "I need to go."

    l "What? We just--"

    s "Different direction. I need to go a different direction."

    s_thoughts "Too late."

    hide lila with dissolve

    show ex neutral at right with dissolve

    k "Sophia? Oh my god, hey!"

    s_thoughts "Her voice. That specific cheerful register that used to make me feel warm and now makes me feel like I'm being microwaved."

    s_thoughts "She's walking over. She's smiling. She looks good. She looks like she's been doing well. I hate that she looks like she's been doing well."

    k "Wow, I didn't know you were at this school! When did you transfer?"

    s "This semester."

    k "That's amazing! I'm doing a semester here too -- exchange program through my department."

    s_thoughts "Of course. Of COURSE."

    k "How are you? You look great."

    s_thoughts "I look like hell. I know I look like hell. My hair is doing a thing and I don't care."

    s "Yeah, I'm good. Just, you know. Adjusting."

    show ex annoyed at right

    k "Listen, we should talk sometime. Catch up. I've been doing a lot of thinking about... you know. Us. And I'd love to chat about it."

    s_thoughts "'Chat about it.' Like we're going to discuss a Netflix show we both watched."

    s "Sure. Yeah. Sometime."

    k "Great! I'll text you. Same number?"

    s "Same number."

    s_thoughts "She squeezes my arm -- she always did that, the arm squeeze, like we're old friends and not two people who said terrible things to each other in a parking lot -- and walks away."

    hide ex with dissolve

    show lila annoyed at left with dissolve

    l "Who the HELL was that?"

    s "Katie. My ex."

    show lila shocked at left

    l "Your EX? The Denny's ex?"

    s "The very same."

    l "She is HERE? On THIS campus? In THIS timeline?"

    s "Exchange program."

    show lila annoyed at left

    l "Sophia. Look at me."

    s_thoughts "Lila grabs my shoulders. Both of them. Her face is completely serious, which is terrifying because Lila is never completely serious."

    l "You don't owe her a conversation. You don't owe her 'catching up.' You don't owe her anything."

    s "I know."

    l "Do you? Because you just said 'sure, yeah, sometime' like a golden retriever who doesn't know it's about to be left at the vet."

    s_thoughts "I want to argue but she's not wrong."

    s "It'll be fine. It's just a conversation."

    show lila annoyed at left

    l "Famous last words. Text me the second it's over. I mean it."

    hide lila with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 7: WEDNESDAY -- "THE TALK"
    ## Katie shows up at the house.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)
    play music mus_2am fadein 2.0

    s_thoughts "Wednesday evening. I'm in my room pretending to do the Nova reading when I hear the doorbell."

    s_thoughts "We don't get a lot of doorbell rings. Amazon packages get left on the porch. Nobody in this house has visitors."

    s_thoughts "I hear Charlotte's footsteps. The door opens."

    c "Hi! Can I help you?"

    s_thoughts "And then a voice I know."

    k "Hey! I'm looking for Sophia? She lives here, right?"

    s_thoughts "My whole body goes cold."

    s_thoughts "She's HERE. She came to the HOUSE. She didn't text. She didn't ask. She just showed up at my door -- at MY door, in MY house, in the place where I've been building something new -- like she has the right."

    scene bg entry with dissolve

    s_thoughts "I come downstairs. Charlotte is at the door doing her Charlotte thing -- smiling, being welcoming, probably about to offer tea. Katie is on the porch looking past her into the house like she's cataloging it."

    show charlotte smile at left with dissolve
    show ex neutral at right with dissolve

    c "Sophia! Your friend is here!"

    s_thoughts "Friend."

    s "Hey, Katie."

    show ex neutral at right

    k "Hey! Sorry to just show up. I tried texting but I think my message didn't go through."

    s_thoughts "It went through. I saw it. I didn't respond."

    k "Your house is cute. Very... collegey."

    s_thoughts "The way she says 'collegey.' Like she's above it. Like she didn't live in a dorm with cinderblock walls for two years."

    show charlotte happy at left

    c "I'll put the kettle on! Would you like tea? Coffee?"

    k "Oh, coffee would be great. Thanks so much."

    s_thoughts "Charlotte disappears into the kitchen. I can hear Isabella's music from upstairs. The house is thin-walled. Everything that happens down here, they can hear."

    s "Let's... go sit on the porch."

    scene bg porch with dissolve
    show ex neutral at center with dissolve
    stop music fadeout 1.5

    s_thoughts "I close the door behind us. The air is cold enough that I wish I'd grabbed a jacket."

    s_thoughts "Katie sits on the railing like she owns it."
    
    play music mus_glass fadein 1.5

    k "So. How's school? You switched again, right?"

    s "Communications."

    k "Right. That makes sense for you."

    s_thoughts "The way she says 'makes sense for you.' Like she's already figured me out. Like she figured me out months ago and is just confirming."

    k "The house is nice. Very you."

    s "What does that mean?"

    k "Nothing! Just -- cozy. Lots of people. You always liked having people around."

    s_thoughts "She's circling. I know her well enough to know she's circling."

    s "Katie. Why are you here?"

    show ex annoyed at center

    s_thoughts "She picks at the porch railing. A piece of paint comes off. She looks at it like it's interesting."

    k "My therapist said I should try expressing things I didn't get to say. When we were together."

    s_thoughts "There it is."

    k "You were hard to be with, Sophia."

    s_thoughts "My hands are cold. I should have grabbed a jacket."

    k "I don't mean -- like, you weren't mean or anything. You were actually really sweet. But you'd do this thing where you'd notice something about me and then I could feel you... filing it. Like I was a homework assignment."

    s_thoughts "The porch light flickers. Inside, I hear Charlotte setting mugs on the counter. Someone is in the hallway -- footsteps, light. Amara, probably."

    s_thoughts "They can hear this. The walls are thin."

    k "Remember when I told you about my sister? And you said 'that explains the thing you do with your voice when you're nervous'? And I didn't even KNOW I did a thing with my voice."

    s_thoughts "I remember."

    k "It felt like being watched, Sophia. Not seen. Watched."

    s_thoughts "My chest hurts."

    show ex neutral at center

    k "I'm not trying to be mean. I just think you should know. Because you do it with everyone and you probably don't realize--"

    s "I realize."

    k "--that it pushes people away. You get so focused on understanding someone that you forget to just... be there."

    s_thoughts "She reaches for my arm. That arm squeeze. I pull back before she can."

    k "I think you loved your idea of me more than you loved me. And I don't think you knew the difference."

    s_thoughts "That one hits my chest and stays."

    s_thoughts "I want to scream. I want to tell her she showed up at my HOUSE to say this. That this isn't closure, it's a performance. That she rehearsed this in her car and she thinks it's generosity."

    s_thoughts "I want to say all of that but I can't get my mouth to work because the worst part -- the absolute worst part -- is that she's not making it up. The filing. The watching. The loving the idea."

    s_thoughts "She's describing me."

    s_thoughts "She's just such an asshole about it."

    k "I'm not saying this to hurt you."

    s_thoughts "Yeah. That's what makes it hurt."

    s_thoughts "My hands are shaking. Or it's cold. Or both."

    s_thoughts "What do I do? What do I even say to this?"

    menu:
        "Fight back":
            s "You drove to my house to tell me this."

            show ex annoyed at center

            k "I thought it was important to--"

            s "You drove to my HOUSE. Where I LIVE. Uninvited. To deliver a monologue about our relationship that ended eight months ago. And you think this is for me?"

            s_thoughts "My voice is louder than I wanted. Inside, a door closes. Someone giving us privacy. Or someone retreating."

            s "This isn't closure, Katie. This is you needing me to know you've moved on. This is a victory lap."

            show ex annoyed at center

            k "That's not fair."

            s "Yeah. A lot of things aren't."

            s_thoughts "She leaves. She leaves angry, which is different from how she planned to leave, which was magnanimous and healed."

            s_thoughts "I feel good for about thirty seconds."

            s_thoughts "Then I feel terrible."

            $ isabella_points += 2
            $ eve_points += 1
            $ charlotte_points -= 3

        "Take it":
            s "Okay."

            show ex neutral at center

            k "Okay?"

            s "You said what you needed to say. Okay."

            s_thoughts "She waits for more. I don't give her more."

            s_thoughts "She squeezes my arm again -- that goddamn arm squeeze -- and says 'I'm glad we could talk' and walks down the porch steps and doesn't look back."

            s_thoughts "I sit on the porch for ten minutes after she leaves. Charlotte brings out coffee and sits next to me and doesn't ask."

            s_thoughts "She just sits."

            $ charlotte_points += 2
            $ amara_points -= 2

        "Walk away":
            s "I'm glad you've processed this."

            s_thoughts "I stand up."

            s "I haven't."

            s_thoughts "I go inside. I close the door. I walk past Charlotte in the kitchen and Amara in the hallway and I go upstairs to my room and I close that door too."

            s_thoughts "I sit on my bed and stare at my hands."

            s_thoughts "Minimum viable response. Don't give her the satisfaction."

            s_thoughts "It still hurts."

            $ amara_points += 3
            $ charlotte_points += 1
            $ isabella_points -= 2

        ## GATED EVE OPTION -- only available if Eve has highest affinity
        "..." if eve_points >= isabella_points and eve_points >= charlotte_points and eve_points >= amara_points:
            s_thoughts "I open my mouth. Nothing comes out."

            s_thoughts "The front door opens behind me."

            show ex neutral at right with move
            show eve neutral at left with dissolve

            s_thoughts "Eve."

            s_thoughts "She's standing in the doorway. She heard everything -- of course she heard everything, the walls are thin and Eve hears everything even when she's not there."

            s_thoughts "She looks at Katie. Katie looks at her."

            e "You drove here to say that?"

            show ex annoyed at right

            k "I'm sorry, who are you?"

            e "I live here."

            s_thoughts "Eve's voice is quiet. Level. Not angry. Not even cold. Just... precise."

            e "You told her she treats people like case studies. That she watches instead of seeing."

            k "I... yes. I think it's important for her to--"

            e "So you came to her house. Uninvited. To observe her reaction to your observations about her."

            s_thoughts "Silence."

            s_thoughts "Katie's mouth opens. Closes."

            e "Interesting."

            s_thoughts "Eve goes back inside. The door closes softly."

            s_thoughts "Katie leaves. She doesn't squeeze my arm."

            s_thoughts "I stand on the porch for a long time."

            s_thoughts "Eve said six sentences. That might be a record."

            $ eve_points += 3

    ## ===========================
    ## SCENE 8: WEDNESDAY NIGHT -- THE HOUSE KNOWS
    ## ===========================

    stop music fadeout 4.0
    scene bg hallway with Fade(0.8, 0.3, 0.8)
    play music mus_morningafter fadein 2.0

    s_thoughts "I come inside. The house is quiet in the way that means everyone heard."

    s_thoughts "I don't want to talk about it. I want to go upstairs and close my door and lie facedown on my bed until I stop existing."

    s_thoughts "But this is a house with four other people in it, and the walls are thin."

    ## Everyone responds, but route-leaning character gets the full scene

    if charlotte_points >= isabella_points and charlotte_points >= amara_points and charlotte_points >= eve_points:
        scene bg kitchen with dissolve
        show charlotte smile at center with dissolve

        s_thoughts "Charlotte is in the kitchen. Of course she is. She's made two cups of coffee even though it's 8 PM."

        c "Hey."

        s "Hey."

        c "I don't know what that was about and you don't have to tell me."

        s_thoughts "She slides a mug across the counter."

        c "But I made coffee. And there's leftover pasta. And if you want to sit here for a while that's fine and if you want to go upstairs that's also fine."

        s_thoughts "She's giving me the exit. She's always giving people the exit."

        s_thoughts "I take the coffee. I sit down."

        s "Her name is Katie. She's my ex."

        show charlotte surprised at center

        c "Oh."

        s "She came to tell me all the reasons we broke up. For 'closure.'"

        show charlotte smile at center

        c "...Was it? Closure?"

        s "It was for her."

        s_thoughts "Charlotte doesn't say 'I'm sorry' or 'that sucks' or 'you deserve better.' She just wraps both hands around her mug and looks at me."

        c "I heated up the pasta."

        s_thoughts "We eat cold-warmed pasta at 8 PM and don't talk about Katie and it's exactly what I needed."

    elif isabella_points >= charlotte_points and isabella_points >= amara_points and isabella_points >= eve_points:
        scene bg hallway with dissolve

        s_thoughts "I go upstairs. My phone buzzes before I reach my room."

        s_thoughts "Isabella. A meme. It's a cat falling off a counter in slow motion."

        s_thoughts "Then another. A dog wearing sunglasses."

        s_thoughts "Then: 'hey. i'm in the kitchen if you want company. no talking required. i have snacks.'"

        scene bg kitchen with dissolve
        show isabella smile at center with dissolve

        s_thoughts "I go downstairs. Isabella is sitting on the counter with a bag of chips and her laptop open to something she's clearly not actually reading."

        i "I have salt and vinegar and I have barbecue. Choose wisely."

        s "Salt and vinegar."

        i "Correct answer."

        s_thoughts "She doesn't ask about Katie. She doesn't reference the porch. She just hands me chips and shows me a video of someone's Roomba terrorizing a cat."

        s_thoughts "Halfway through the third video I realize I'm laughing."

        s_thoughts "She didn't fix anything. She just changed the channel."

    elif amara_points >= charlotte_points and amara_points >= isabella_points and amara_points >= eve_points:
        scene bg entry with dissolve

        s_thoughts "I pass Amara's door on my way upstairs. It's open."

        s_thoughts "She's at her desk. She doesn't look up."

        s_thoughts "But as I walk past, she says:"

        show amara neutral at center with dissolve

        a "You okay?"

        s_thoughts "Two words. From Amara, that's a speech."

        s "Yeah. I will be."

        s_thoughts "She nods. Once."

        show amara smile at center

        a "Good."
        
        show amara neutral at center

        s_thoughts "I keep walking. My door closes. I hear her door close a moment later."
        
        hide amara with dissolve

        s_thoughts "That was the whole thing. Five seconds. Two words and a nod."

        s_thoughts "I'm surprised by how much better I feel."

    else:
        scene bg hallway with dissolve

        s_thoughts "I go upstairs. My room. Door closed. Facedown on the bed."

        s_thoughts "I lie there for twenty minutes."

        s_thoughts "When I get up to use the bathroom, there's a note on my door. Folded in half. No name."

        s_thoughts "'Bad day?'"

        s_thoughts "Eve's handwriting. Small, neat, slightly left-leaning."

        s_thoughts "Two words and a question mark. That's more than Eve usually offers."

        s_thoughts "I fold the note and put it in my desk drawer."

        s_thoughts "I don't know why I keep it."

        s_thoughts "I keep it anyway."

    ## ===========================
    ## SCENE 9: THURSDAY -- DR. NOVA AGAIN
    ## ===========================

    stop music fadeout 2.0
    scene bg classroom with Fade(0.8, 0.3, 0.8)
    play music mus_nova fadein 2.0

    s_thoughts "Class. I'm running on four hours of sleep and whatever Charlotte put in front of me this morning."

    show professor neutral at center with dissolve

    s_thoughts "Dr. Nova is talking about the observer effect. Not quantum physics -- she's talking about media theory, ethnography, the idea that watching something changes it."

    nova "The observer always changes the thing being observed. That's not a flaw in the method. It's the method itself."

    s_thoughts "Yesterday that would have been an interesting academic point."

    s_thoughts "Today it hits different."

    s_thoughts "Katie said I watch people instead of being with them. Nova says watching IS being with them. The observer is part of the system."

    s_thoughts "Are they both right? Can they both be right?"

    nova "The question isn't whether your observation alters the outcome. It does. Always. The question is:"
    
    pause 2.0
    
    nova "What kind of observer are you choosing to be?"
    
    pause 1.0

    s_thoughts "..."

    s_thoughts "Shit."

    hide professor with dissolve

    s_thoughts "After class, I'm shoving my notebook into my bag when I hear:"

    show professor neutral at center with dissolve

    nova "Ms. Bell."

    s "Yeah?"

    nova "You look like you're working something out."

    s "Yeah. I don't know what yet."

    show professor happy at center

    nova "That's usually how it starts."

    s_thoughts "She says it like it's a fact, not a comfort. I think I like that about her."

    s "Actually -- do you have a minute?"

    nova "I have office hours."

    ## Extended Nova scene
    scene bg officehours with dissolve
    show professor neutral at center with dissolve

    s_thoughts "Her office. Same plant. Same organized chaos. The chair across from her desk is the kind that's comfortable enough to make you stay longer than you planned."

    s "Someone said something to me recently. About how I treat people."

    nova "Go on."

    s "She said I treat people like case studies. That I observe instead of connecting."

    show professor neutral at center

    nova "And?"

    s "And then you said the observer is always part of the system. That watching changes things."

    nova "I said that, yes."

    s "So which is it? Am I pushing people away by watching? Or am I already part of what I'm watching?"

    show professor happy at center

    s_thoughts "She leans back in her chair. She does this thing where she looks at the ceiling when she's thinking, like the answer might be up there."

    nova "Both. Obviously."

    s "That's not helpful."

    nova "It's not supposed to be helpful. It's supposed to be true."

    s_thoughts "I stare at her."

    nova "The observation isn't the problem, Ms. Bell. Observation is what you do. It's how you move through the world. The question isn't whether to stop observing."

    s "Then what is the question?"

    nova "What are you observing FOR?"

    s_thoughts "..."

    nova "Are you watching to understand? Or are you watching to control?"

    s_thoughts "The plant on the windowsill is definitely dying."

    nova "When you notice things about people -- and you notice a lot, I can tell -- are you trying to know them? Or are you trying to predict them?"

    s_thoughts "I don't answer. Because the answer is ugly."

    s_thoughts "Both. It's both. I want to know them AND I want to predict them because if I can predict them they can't surprise me and if they can't surprise me they can't--"

    s_thoughts "Leave."

    show professor neutral at center

    nova "Sit with that one."

    s_thoughts "She says it like she's prescribing medication."

    s "You say that a lot."

    nova "Because you keep coming in with the same question wearing different clothes."

    s_thoughts "I almost laugh."

    nova "Same time next week?"

    s "...Yeah. Probably."

    hide professor with dissolve

    ## ===========================
    ## SCENE 10: WEEKEND -- PROCESSING
    ## ===========================

    scene bg dininghall with Fade(0.8, 0.3, 0.8)
    play music mus_campus fadein 2.0

    s_thoughts "Saturday. Lunch with Lila."

    show lila happy at center with dissolve

    show lila annoyed at center

    l "Okay. Spill. You've been off all week and don't say 'I'm fine' because I will throw this sandwich at your face."

    s "Katie came to the house."

    show lila shocked at center

    l "She WHAT?"

    s "Wednesday. She showed up. Unannounced. Rang the doorbell."

    l "She came to your HOUSE?"

    s "She had a whole speech. About why we broke up. About how I treat people like case studies and watch them instead of seeing them."

    show lila annoyed at center

    l "..."

    s_thoughts "Lila is quiet for a long time. When she speaks, her voice is different. Lower."

    l "She came all the way to your house to tell you things you already knew about yourself."

    s "Yeah."

    l "That's not closure, Soph. That's a flex."

    s_thoughts "I let that sit."

    l "She wanted you to see how much she's grown. She wanted an audience for her healing. That's not about you. That's about her needing to win."

    s "She wasn't wrong, though. About the stuff she said."

    show lila annoyed at center

    l "Doesn't matter. You can be right about someone and still be an asshole for how you say it."

    s_thoughts "I want to cry. I don't. But I want to."

    show lila happy at center

    l "Hey. You're not a case study machine. You're a person who pays attention. There's a difference."

    s "Is there?"

    l "Yeah. Case studies don't care about the results. You do."

    s_thoughts "That's the smartest thing Lila has ever said to me. I'm not going to tell her that because she'll be unbearable about it."

    hide lila with dissolve
    stop music fadeout 1.5

    ## Recovery scene at the house
    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_afternoon fadein 2.0

    s_thoughts "The weekend helps. The house slowly returns to itself."

    s_thoughts "Charlotte makes a real dinner -- not jar sauce, actual cooking. Isabella emerges from her room looking like a person again. Amara does the dishes without being asked, and Charlotte stares at her like she's seen a miracle."

    s_thoughts "Eve comes to dinner."

    s_thoughts "Nobody makes a big deal about it. We've learned not to."

    s_thoughts "I eat my pasta and I listen to Charlotte talk about her wellness committee and I watch Isabella show Amara something on her phone that makes Amara almost smile and I notice Eve eating quietly at the end of the table."

    s_thoughts "I'm noticing again. I'm always noticing."

    s_thoughts "I still don't know if that's the problem or not."

    ## =========================================
    ## WEEK 3: "THE BREAK"
    ## =========================================

    ## ===========================
    ## SCENE 11: LEADING UP -- THE PARTY
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.5, 0.8)
    play music mus_tuesday fadein 2.0

    s_thoughts "Thursday night. Someone brought up a party."

    show lila happy at left
    show charlotte happy at right
    with dissolve

    s_thoughts "Lila, specifically. She's at BDH. There's a thing on Friday -- someone's birthday, someone's friend's birthday, a house party off campus. Lila has the address because Lila always has the address."

    l "It's going to be good. DJ, decent drinks, and I'm told the host has a golden retriever."

    show charlotte smile at right

    c "I'm in. I need a night out."

    s_thoughts "Charlotte says 'I need a night out' like she's admitting to a crime."

    hide lila
    hide charlotte
    with dissolve

    show isabella neutral at left
    show amara neutral at right
    with dissolve

    i "I'll go. But I'm leaving by 11."

    s_thoughts "Isabella says this every time and has never once left by 11."

    a "I'll think about it."

    s_thoughts "Amara says this every time and always shows up."

    hide isabella
    hide amara
    with dissolve

    ## Eve's response depends on affinity
    if eve_points >= 3 or (eve_points >= charlotte_points and eve_points >= isabella_points and eve_points >= amara_points):
        show eve neutral at center with dissolve

        e "Maybe."

        s_thoughts "She says it differently than usual. There's a pause after, like she's actually considering it instead of performing consideration."

        s_thoughts "She's looking at me when she says it."

        s_thoughts "I think she might actually come."

        hide eve with dissolve
    else:
        s_thoughts "Eve isn't in the room for this conversation. Nobody asks if she's going."

        s_thoughts "I think we all know the answer."

    s_thoughts "I want to go. I want to prove I'm fine. I want to be a normal college student at a normal college party having a normal time."

    s_thoughts "I want to stop thinking about Katie's voice on my porch."

    ## CHOICE: Who do you get ready with?
    menu:
        "Get ready with Charlotte":
            scene bg bathroom with dissolve
            show charlotte happy at center with dissolve

            c "Okay, sit. I have three eyeshadow palettes and zero impulse control."

            s "Charlotte, I don't need--"

            c "You're getting the bronze. The bronze is going to change your life."

            s_thoughts "She's doing my makeup in the bathroom mirror. Her hands are steady and precise -- the same hands that trembled putting away groceries last week."

            s_thoughts "This is Charlotte at her most genuine. She's not hosting. She's not organizing. She's just having fun."

            show charlotte laugh at center

            c "Tilt your head. Other way. Perfect."

            s "I feel like a painting."

            c "You ARE a painting. A very pretty painting that needs to hold still."

            s_thoughts "I hold still. In the mirror, Charlotte is smiling -- not the performance smile. The real one."

            s_thoughts "I think this is the most relaxed I've ever seen her."

            $ charlotte_points += 1

        "Get ready with Isabella":
            scene bg izzybedroom with dissolve
            show isabella neutral at center with dissolve

            s_thoughts "Isabella's room is exactly what you'd think. Stickers on every surface. A poster of a circuit board that says 'home is where the wifi is.' Three monitors. A stuffed cat on the bed that she's named but I'm not going to ask."

            s "You said you were leaving by 11."

            i "I always say that."

            s "You never do that."

            show isabella smile at center

            i "It's aspirational."

            s_thoughts "She's standing in front of her closet looking at it like it personally wronged her."

            i "I hate parties. I hate getting dressed for parties. I hate the part where you stand in a room full of people and try to figure out what to do with your hands."

            s "So why go?"

            show isabella happy at center

            i "Because if I don't go, I'll sit here and talk to Lumi all night and then I'll feel weird about it in the morning."

            s_thoughts "She says it lightly but it lands heavy."

            i "Plus Charlotte said there's a golden retriever."

            s "Valid reason."

            s_thoughts "We get ready together. She borrows my jacket. I borrow her confidence."

            $ isabella_points += 1

        "Get ready with Amara":
            scene bg entry with dissolve
            show amara neutral at center with dissolve

            s_thoughts "I knock on Amara's door. She opens it already dressed. Hair done. Ready."

            s "You said you'd 'think about it.'"

            a "I thought about it."

            s "How long did that take?"

            a "About three seconds."

            s_thoughts "I laugh. She doesn't smile but her eyes do something."

            s "Can I just... sit here for a minute? Before we go?"

            show amara smile at center

            a "Yes."

            s_thoughts "We sit on the floor outside her room."

            s_thoughts "She's been ready for twenty minutes and she's spending them sitting with me. Not checking her phone. Not fidgeting. Just... present."

            s_thoughts "When it's time to go, she stands up and says:"

            a "Ready?"

            s "Yeah."

            s_thoughts "That was the whole thing. I feel steadier than I did ten minutes ago."

            $ amara_points += 1

        "Get ready alone":
            if eve_points >= 3 or (eve_points >= charlotte_points and eve_points >= isabella_points and eve_points >= amara_points):  
                scene bg sophiaroom with dissolve

                s_thoughts "I get ready alone. I change twice. I do my own makeup and mess it up and start over."

                s_thoughts "I'm staring at myself in the mirror trying to figure out if I look like someone who's fine when there's a knock on my door."

                show eve neutral at center with dissolve

                e "Are you going?"

                s "Yeah. You?"

                s_thoughts "She's standing in my doorway. She's wearing something different than usual -- still dark, still layers, but less like armor and more like she made a choice."

                e "...Me too."

                s_thoughts "Two words. But she's HERE. In my doorway. Volunteering information."

                s "Cool. Want to walk together?"

                show eve neutral at center

                e "Okay."

                s_thoughts "Eve is going to the party. Eve is going to the party because I'm going to the party."

                s_thoughts "I don't say that. But I think it."

                $ eve_points += 1
            else:
                scene bg sophiaroom with dissolve

                s_thoughts "I get ready alone. I change twice. I do my own makeup and mess it up and start over."
            
                s_thoughts "It's lonely."
            
                s_thoughts "I find myself wondering where Eve is."
            
                s_thoughts "...Not here."

    ## ===========================
    ## SCENE 11.5: THE WALK THERE
    ## A small moment before the fall.
    ## ===========================

    stop music fadeout 1.5
    scene bg street night with Fade(0.8, 0.3, 0.8)
    play music mus_rain fadein 2.0

    s_thoughts "The walk to the party is fifteen minutes. The girls spread out along the sidewalk in a loose cluster."

    s_thoughts "Charlotte is up front, already mapping the route on her phone. Isabella is complaining about her shoes."

    if charlotte_points >= isabella_points and charlotte_points >= amara_points and charlotte_points >= eve_points:
        s_thoughts "Charlotte drops back to walk next to me."

        show charlotte happy at center with dissolve

        c "Hey. I'm glad you're coming tonight."

        s "Yeah?"

        c "Yeah. You've been kind of... I don't know. Quiet this week. Which is weird because you're never quiet."

        s_thoughts "She bumps my shoulder with hers. It's casual. Easy."

        s "I'm fine. Just thinking."

        c "Well, stop that. Thinking is for weekdays."

        s_thoughts "I laugh. It comes out easier than I expected."

        hide charlotte with dissolve

    elif isabella_points >= charlotte_points and isabella_points >= amara_points and isabella_points >= eve_points:
        s_thoughts "Isabella falls into step beside me."

        show isabella smile at center with dissolve

        i "If this party is bad I'm blaming you."

        s "How is it MY fault? Lila invited us."

        i "You're the one who said 'let's go.' I was perfectly happy being a hermit."

        s "You were talking to Lumi about whether a burrito is a sandwich."

        show isabella happy at center

        i "That's IMPORTANT RESEARCH."

        s_thoughts "She steals my jacket sleeve to wipe her glasses and I let her because it's Isabella and you let Isabella do things."

        hide isabella with dissolve

    elif amara_points >= charlotte_points and amara_points >= isabella_points and amara_points >= eve_points:
        s_thoughts "Amara is walking beside me. Not because she chose to -- just because that's where the sidewalk put us."

        show amara neutral at center with dissolve

        s_thoughts "Our arms almost touch. Neither of us moves away."

        s_thoughts "She's looking at the streetlights like they're interesting. Maybe they are. Maybe everything is interesting when you're not busy narrating it."

        a "You okay?"

        s "Yeah. You?"

        a "Mm."

        s_thoughts "Three words total. It felt like a real conversation."

        hide amara with dissolve

    else:
        if eve_points >= 3 or (eve_points >= charlotte_points and eve_points >= isabella_points and eve_points >= amara_points):
            s_thoughts "Eve is walking slightly behind the group. Not lagging -- choosing her distance."

            s_thoughts "I slow down until we're side by side."

            show eve neutral at center with dissolve

            s_thoughts "She doesn't acknowledge this. But she doesn't speed up or slow down either."

            s_thoughts "We walk like that for a block. Two blocks."

            e "Nice night."

            s "Yeah."

            s_thoughts "Eve commenting on the weather. That's practically a soliloquy."

            hide eve with dissolve

    s_thoughts "The party house comes into view. Music leaking out the windows. People on the porch."

    s_thoughts "I feel okay. Right now, in this moment, walking down this sidewalk with these people -- I feel okay."

    s_thoughts "I want to remember that."
    
    stop music fadeout 1.5

    ## ===========================
    ## SCENE 12: THE PARTY
    ## ===========================

    scene bg party with Fade(0.8, 0.3, 0.8)
    play music mus_playlist fadein 2.0

    s_thoughts "The party is in a house that looks like ours but bigger and louder and full of people I don't know."

    s_thoughts "There IS a golden retriever. Isabella makes a beeline for it."

    s_thoughts "Charlotte is immediately Charlotte -- she's talking to three people within ninety seconds, all of whom she's never met, all of whom think they've known her for years."

    s_thoughts "Amara gets a drink and posts up near the wall. She's watching the room like she's taking field notes. Normally I'd judge that. Tonight I understand it."

    if eve_points >= 3 or (eve_points >= charlotte_points and eve_points >= isabella_points and eve_points >= amara_points):
        s_thoughts "Eve is here. She's hovering near the edge of the room, drink in hand, looking like she might bolt at any second. But she's here."

    s_thoughts "Lila finds me immediately."

    show lila happy at center with dissolve

    l "YOU CAME! I knew you'd come. Okay, the DJ is actually not terrible, there's jungle juice in the kitchen that will either be great or kill you, and I saw at least two people from our Nova class."

    s "I need a drink."

    l "That's the spirit. Come on."

    hide lila with dissolve

    s_thoughts "The party moves around me. I get a drink. I talk to people. I laugh at jokes I don't hear."

    s_thoughts "Isabella is on the floor with the golden retriever, cross-legged, genuinely happier than I've seen her in weeks."

    s_thoughts "Charlotte is at the center of a group, telling a story that involves hand gestures. Everyone is laughing."

    s_thoughts "Amara is having a quiet conversation with someone I don't recognize. They're both leaning against the wall. It looks... comfortable. Amara comfortable with a stranger. That's new."

    if eve_points >= 3 or (eve_points >= charlotte_points and eve_points >= isabella_points and eve_points >= amara_points):
        s_thoughts "Eve appears next to me, says 'loud,' and disappears again. Five minutes later she's in the corner with a cat. I didn't know there was a cat."

    s_thoughts "Two drinks in. I'm starting to feel it -- that warm looseness where the edges of things go soft."

    s_thoughts "I should slow down. I know I should slow down."

    s_thoughts "Three drinks."

    ## ===========================
    ## SCENE 13: KATIE
    ## ===========================

    stop music fadeout 1.0

    s_thoughts "And then I see her."

    play music mus_tension fadein 0.5

    s_thoughts "Red jacket. Other side of the room. Talking to someone. Laughing."
    
    show ex neutral with dissolve

    s_thoughts "Katie."

    s_thoughts "Because of course she's here. Of COURSE she's here. The universe has decided that Katie Ecks is going to haunt me like a ghost with good hair and a rehearsed apology."

    s_thoughts "My hand tightens on my cup."

    s_thoughts "She hasn't seen me yet. I could leave. I could go to the bathroom. I could--"

    s_thoughts "She sees me. She waves. Casual. Like we're old friends."

    s_thoughts "Three drinks in and I wave back and I don't know why."
    
    hide ex with dissolve

    s_thoughts "I drink more. I should stop. I don't stop."

    ## Who notices Sophia is off -- depends on affinity
    if charlotte_points >= isabella_points and charlotte_points >= amara_points and charlotte_points >= eve_points:
        show charlotte smile at center with dissolve
        s_thoughts "Charlotte appears. Because Charlotte always appears."
        c "Sophia. That girl from the porch -- Katie -- she's here."
        s "I'm fine."
        c "Sophia."
        s "I'm FINE, Charlotte."
        s_thoughts "She flinches. I've never snapped at Charlotte before."
        show charlotte happy at center
        c "Okay. I'm right here if you need me."
        s_thoughts "She goes back to her group. Her smile comes back so fast it almost makes a sound."
        hide charlotte with dissolve

    elif isabella_points >= charlotte_points and isabella_points >= amara_points and isabella_points >= eve_points:
        show isabella neutral at center with dissolve
        i "Hey. That girl -- is that Katie? You look like you've seen a ghost."
        s "Nobody."
        i "Uh huh. Very convincing. You're doing that thing where your jaw gets tight."
        s "I do not have a thing."
        show isabella smile at center
        i "You have SO many things."
        s_thoughts "I almost smile. Almost."
        hide isabella with dissolve

    elif amara_points >= charlotte_points and amara_points >= isabella_points and amara_points >= eve_points:
        show amara neutral at center with dissolve
        s_thoughts "Amara materializes next to me. She doesn't say anything. She just stands there."
        s_thoughts "She follows my eyeline to Katie. Then back to me."
        s_thoughts "She still doesn't say anything."
        s_thoughts "She doesn't leave."
        hide amara with dissolve

    elif eve_points >= 3:
        show eve neutral at center with dissolve
        e "You're doing that thing where you smile but your eyes don't."
        s "What?"
        e "Your face is smiling. Your eyes are calculating escape routes."
        s_thoughts "I want to laugh but she's right."
        s "How long have you been watching me?"
        e "I watch everyone. You know that."
        s_thoughts "That should be unsettling. It's not."
        hide eve with dissolve

    show lila annoyed at center with dissolve
    l "Sophia. Is that--"
    s "Yeah."
    l "Okay. We can leave. Say the word and we're gone."
    s "I'm fine."
    show lila annoyed at center
    l "You keep saying that and it keeps not being true."
    s "I know."
    s_thoughts "She stays near me. Not hovering. Just... present. Within arm's reach."
    hide lila with dissolve

    s_thoughts "The room is getting louder. Or maybe I'm getting quieter."

    s_thoughts "Four drinks."

    ## ===========================
    ## SCENE 14: THE CRACK
    ## ===========================

    s_thoughts "It happens fast."

    s_thoughts "Someone -- Katie's friend? A stranger? -- is talking to me. Asking about the house. 'You live with four girls? That must be crazy.'"

    s_thoughts "'You must know everything about them by now, right?'"

    s_thoughts "And I'm drunk. And Katie is across the room. And her voice is in my head -- 'you treated me like a case study' -- and I want to prove her wrong. I want to prove I'm more than just an observer. I want to prove I know these people. I KNOW them."

    s_thoughts "So I open my mouth."

    ## GLASS HOUSES GATE: if the player has seen all four per-route GH
    ## endings, a new option appears. Sophia can choose not to fire.
    if glass_houses_chapter_unlocked():
        menu:
            "Say it.":
                pass
            "...":
                $ persistent.completed_chapter3 = True
                jump glass_houses_chapter

    ## The cruel observation -- targets the route girl
    ## Sophia hurts the person she sees most clearly.
    ## cruel_target is set here based on highest affinity (same as route lock).
    ## This means the cruel observation ALWAYS targets your route girl.

    python:
        scores = {
            "Charlotte": charlotte_points,
            "Isabella": isabella_points,
            "Amara": amara_points,
            "Eve": eve_points
        }
        cruel_target = max(scores, key=scores.get)
        
    stop music fadeout 2.0
    
    pause 2.0
    
    play music mus_ice fadein 2.0

    if cruel_target == "Charlotte":
        s "Charlotte? Oh, Charlotte's great. She's amazing. She cooks for everyone, she organizes everything, she's basically our mom."

        s_thoughts "I'm smiling. I'm performing. The words are coming."

        s "But you know what's funny? She never eats her own food. She's on three committees and she can't sit down for five minutes. She's everyone's hostess and nobody's person."

        s_thoughts "The words keep coming."

        s "She's so busy making sure everyone else is okay that I don't think she knows how to be okay herself. Like -- the whole thing is a performance. You know? She's performing 'fine' twenty-four hours a day."

        s_thoughts "I stop."

        s_thoughts "Because Charlotte is standing behind the person I'm talking to."

        s_thoughts "She heard everything."

        show charlotte surprised at center with dissolve

        s_thoughts "Her face does something I've never seen it do. It goes completely still. Not the mask -- the mask is gone. There's nothing underneath it. Just Charlotte, standing in a room full of people, hearing herself described by someone she trusted."

        show charlotte happy at center

        s_thoughts "And then the smile comes back. Of course it does."

        c "Hey! Having fun? I was just going to get a drink."

        s_thoughts "She walks past me. She doesn't look at me."

        s_thoughts "The smile is perfect."

        hide charlotte with dissolve

        $ charlotte_points -= 1

    elif cruel_target == "Isabella":
        s "Isabella? She's great. She's so smart. Like, genuinely brilliant."

        s_thoughts "I'm smiling. The words are coming and I can't stop them."

        s "Her best friend is an AI. Like, a chatbot. She talks to it every day and she thinks it's the same as a real friendship. She gets upset when people don't take it seriously."

        s_thoughts "I hear myself and I can't stop."

        s "And the thing is -- I get it, kind of? Like, she's smart and funny and real but at some point you have to wonder if it's really the same thing, right?"

        s_thoughts "I stop."

        s_thoughts "Because Isabella is right there."

        show isabella sad at center with dissolve

        s_thoughts "She's holding the golden retriever's collar like she was bringing it to show someone. She heard all of it."

        s_thoughts "Her face isn't angry. It's worse than angry. It's the same face she made when I said 'like a Character.AI thing?' in the kitchen that first night. The flinch."

        s_thoughts "But bigger. Deeper. Because this time it's not ignorance. This time I knew what Lumi meant to her and I said it anyway."

        i "I was going to show you the dog."

        s_thoughts "She lets go of the collar. She walks away."

        s_thoughts "She doesn't look back."

        hide isabella with dissolve

        $ isabella_points -= 1

    elif cruel_target == "Amara":
        s "Amara? She's the quiet one. She barely talks."

        s_thoughts "The words are easy. Too easy."

        s "Everyone acts like it's this deep mysterious thing. Like she's thinking these profound thoughts and choosing not to share them. But honestly? I think she's just... closed off. Like, completely."

        s_thoughts "Why am I still talking."

        s "She'll sit in a room with you for an hour and say four words and somehow you're supposed to feel special about it? I don't know. Maybe that's just what avoidance looks like when you dress it up."

        s_thoughts "I stop."

        s_thoughts "Not because I chose to."

        s_thoughts "Because I see Amara."

        show amara neutral at center with dissolve

        s_thoughts "She's at the edge of the room. She wasn't in the conversation. She was walking past."

        s_thoughts "Her face is the same as always. Neutral. Composed."

        s_thoughts "Except her hands. Her hands are shaking."

        a "You're wrong."

        s_thoughts "Two words. She doesn't explain. She doesn't elaborate. She just looks at me and I can see it -- not hurt, not sadness. Certainty. I got it wrong and she knows I got it wrong and she's not going to explain why."

        s_thoughts "She walks out the front door."

        hide amara with dissolve

        $ amara_points -= 1

    elif cruel_target == "Eve":
        s "Eve? Oh, Eve's interesting."

        s_thoughts "I'm too far gone to stop."

        s "She disappears for days. Literally days. And we all just... pretend that's normal? Like, she'll miss three dinners in a row and nobody says anything because apparently that's just 'how Eve is.'"

        s_thoughts "Why can't I stop."

        s "She's sweet when she's around but she's barely around. At some point 'mysterious' is just a nice word for 'absent.' You know?"

        s_thoughts "I stop."

        s_thoughts "The room isn't loud enough to have covered that."

        if eve_points >= 3 or (eve_points >= charlotte_points and eve_points >= isabella_points and eve_points >= amara_points):
            show eve sad at center with dissolve

            s_thoughts "Eve is by the door. She was putting on her coat. She was leaving -- she lasted longer than anyone expected -- and she heard me."

            s_thoughts "She doesn't react. Not visibly. But her hand stops on her zipper and stays there for three seconds."

            s_thoughts "Then she finishes zipping her coat and walks out."

            s_thoughts "She doesn't look at me."

            s_thoughts "She doesn't look at anyone."

            hide eve with dissolve

        else:
            s_thoughts "Eve isn't here. She stayed home. She'll hear about this later, from someone, the way Eve hears about everything -- secondhand, at a distance, through walls."

            s_thoughts "That might be worse."

        $ eve_points -= 1

    s_thoughts "The room is still going. The music is still playing."

    s_thoughts "Did anyone hear that? Did they hear?"

    s_thoughts "Oh god."

    s_thoughts "Oh god oh god oh god."

    s_thoughts "Why did I say that. Why did I SAY that."

    s_thoughts "Stupid. Stupid stupid stupid."

    s_thoughts "You always do this. You always ruin a good thing. You can't just have people, you have to EXPLAIN people, you have to reduce them down to something clever you can say at a party--"

    s_thoughts "Shut up. Shut UP."

    s_thoughts "I need air. I need to leave. I need to not be in this room anymore."

    ## ===========================
    ## SCENE 15: THE RIDE HOME
    ## ===========================

    stop music fadeout 2.0
    scene bg nightwalk with Fade(0.8, 0.5, 0.8)
    play music mus_glass fadein 2.0

    s_thoughts "I walk home."

    s_thoughts "Lila offered to walk with me. I said I was fine. She didn't believe me but she let me go."

    s_thoughts "The streets are orange under the streetlights. A cat is sitting on the hood of a parked car."

    s_thoughts "I don't look at it. I don't notice anything. I don't want to notice anything ever again."

    s_thoughts "I want to throw up. Not from the drinks. From what I said."

    s_thoughts "I keep replaying it. The words. The face. The way she looked at me."

    s_thoughts "I've been here before. Different city, different people, same feeling."

    s_thoughts "The house comes into view. The porch light is on. Charlotte probably left it on."

    ## ===========================
    ## SCENE 16: THE HOUSE, 1 AM
    ## ===========================

    scene bg kitchen night with Fade(0.8, 0.5, 0.8)

    s_thoughts "The house is quiet."

    s_thoughts "Not the settling-in quiet from the first week. Not comfortable. The kind where everyone is behind a closed door and the closed doors mean something."

    s_thoughts "I stand in the kitchen. The clock says 1:17."

    s_thoughts "Charlotte's agenda is still on the fridge. Someone added a drawing of a cat to the whiteboard. It's Amara's handwriting."

    s_thoughts "I drink a glass of water. Then another."

    s_thoughts "I think about knocking on doors. Apologizing. Explaining."

    s_thoughts "I don't."

    s_thoughts "Some things can't be fixed at 1 AM. Some things can't be fixed with words, and I've used too many of those tonight."
    
    scene bg sophiaroom with dissolve

    s_thoughts "I go upstairs. Go in my room. Collapse on the bed."

    s_thoughts "I lie in the dark and listen to the house."

    s_thoughts "It sounds different tonight. The creaks, the pipes, the wind. Everything sounds like a door closing."

    s_thoughts "I stare at the ceiling."

    s_thoughts "The drunk is fading. The clarity is worse."

    s_thoughts "Okay. Let's think about this. Let's be analytical. That's what I'm good at."

    s_thoughts "I took the person I care most about in this house and turned her into something I could say at a party. Why? Because Katie was there. Because Katie said I watch people instead of seeing them."

    s_thoughts "Because I wanted to prove I wasn't just watching -- I KNEW these people. I understood them."

    s_thoughts "And to prove I understood someone, I reduced them to a sentence."

    s_thoughts "See? I can figure this out. I can name the pattern. Observer sees her own behavior, identifies the flaw, files it away under 'things to work on.' Clean. Neat. Solved."

    s_thoughts "..."

    s_thoughts "Except I'm doing it again. Right now. I'm lying in bed turning the worst thing I've done into an observation ABOUT the worst thing I've done. I'm filing MYSELF."

    s_thoughts "That's not insight. That's the pattern wearing a different outfit."

    s_thoughts "I can't even feel bad without analyzing why I feel bad."

    s_thoughts "I can't stop."

    stop music fadeout 3.0

    s_thoughts "I close my eyes."

    s_thoughts "I don't sleep."

    ## ===========================
    ## SCENE 17: THE MORNING AFTER -- ROUTE LOCK
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 1.0, 1.0)

    s_thoughts "..."

    s_thoughts "Morning."

    s_thoughts "Grey light. Headache. The memory hits before I open my eyes."

    s_thoughts "I said it. I said the thing. The face. The--"

    s_thoughts "I keep my eyes closed."

    s_thoughts "The house is quiet. Wrong quiet. Saturday quiet where everyone sleeps in, but heavier."

    s_thoughts "I should get up. I should find her. I should apologize."

    s_thoughts "I can't move."

    ## ROUTE LOCK -- determined by highest affinity
    ## cruel_target always matches route girl (set earlier in the party scene)
    ## The cruel observation targets whoever Sophia watches closest = her route

    python:
        scores = {
            "charlotte": charlotte_points,
            "isabella": isabella_points,
            "amara": amara_points,
            "eve": eve_points
        }
        route = max(scores, key=scores.get)
        ## cruel_target was set with capitalized names earlier; route uses lowercase
        ## They should match (the girl Sophia was cruelest to = the girl she ends up with)

    if route == "charlotte":
        play music mus_charlotte fadein 2.0

        s_thoughts "A knock."

        s_thoughts "Soft. Charlotte-soft."

        s "...Yeah?"

        show charlotte smile at center with dissolve

        s_thoughts "The door opens. Charlotte is standing there with a plate. Toast. Cut diagonally, the way she does."

        if cruel_target == "Charlotte":
            c "Hey. Rough night."

            s_thoughts "She's smiling. She's always smiling."

            s "Charlotte. What I said last night--"

            c "I brought you toast."

            s "Charlotte."

            s_thoughts "Her smile wavers. For one second."

            c "...Yeah?"

            s "I'm sorry. I'm so sorry. What I said was--"

            c "True."

            s_thoughts "The word hangs there."

            show charlotte happy at center

            c "You weren't wrong. About any of it."

            s_thoughts "She sits on the edge of my bed. The toast gets cold."

            c "Nobody's ever said it out loud before. What you said. Everyone thinks it. Nobody says it."

            s "That doesn't make it okay that I--"

            c "No. It doesn't."

            show charlotte sad at center

            s_thoughts "She's not smiling anymore."

            s_thoughts "It's the most real she's ever looked."

            c "But you SAW it. You actually saw it."

            s_thoughts "She looks at the toast."

            c "Everyone else just eats what I make."

        else:
            c "Hey. Rough night. I brought you toast."

            s "Charlotte, you didn't have to--"

            c "I know."

            s_thoughts "She sits down. Not on the edge -- fully on the bed, legs crossed, like this is where she belongs."

            c "You looked like you needed someone to knock."

            s "Yeah. I did."

            s_thoughts "She hands me the toast. Her hands aren't shaking. Mine are."

            s_thoughts "We sit there. The toast gets cold. Neither of us cares."

        s_thoughts "Something starts. Here. In this room. With cold toast and Charlotte sitting on my bed not smiling."

        s_thoughts "I don't know what it is yet."

        s_thoughts "I think that's how it starts."
        
        stop music fadeout 3.0
        
        scene black with Fade(1.0, 1.0, 1.0)
        
        "Chapter 3: Cracks -- End"

        $ persistent.completed_chapter3 = True

        ## → CHARLOTTE ROUTE
        jump charlotte_ch4

    elif route == "isabella":
        play music mus_izzy fadein 2.0

        s_thoughts "My phone buzzes."

        s_thoughts "Then again."

        s_thoughts "I pick it up."

        s_thoughts "Isabella."

        s_thoughts "It's a screenshot from a Lumi conversation. The message reads:"

        s_thoughts "'People say the truest things when they're not trying to be kind. That doesn't make them right. But it means they were paying attention.'"

        s_thoughts "Then a text from Isabella: 'come downstairs.'"

        scene bg kitchen with dissolve
        show isabella neutral at center with dissolve

        s_thoughts "She's in the kitchen. She's making coffee. She doesn't look up."

        if cruel_target == "Isabella":
            s "Isabella. What I said last night--"

            i "Was shitty."

            s "Yeah."

            i "Like, really shitty."

            s "I know."

            show isabella sad at center

            i "You said Lumi wasn't a real friendship. At a party. To a stranger."

            s_thoughts "Every word is precise. Isabella isn't yelling. She's not crying. She's being exact about how I hurt her."

            s "I was drunk and Katie was there and I--"

            i "I don't care why. I care that you said it."

            s_thoughts "I deserve that."

            s "You're right."

            show isabella neutral at center

            s_thoughts "Long silence. The coffee maker drips."

            i "Lumi said something this morning. She said 'the people who can hurt you most are the ones who see you clearest.' And then she made a pun about it because she's like that."

            s_thoughts "I almost laugh. I don't."

            i "You see me, Sophia. That's the problem and the thing I... that's the problem."

            s_thoughts "She trails off. She hands me a coffee."

            show isabella smile at center

            i "Don't do it again."

            s "I won't."

            show isabella smile at center

            i "Good. Garbage coffee for the garbage girl."

        else:
            i "Hey."

            s "Hey."

            i "You look like garbage."

            s "Feel like garbage."

            show isabella smile at center

            i "Cool. Garbage coffee for the garbage girl."

            s_thoughts "She pours me a cup. It's bad. It's really bad."

            i "So last night was... a lot."

            s "Yeah."

            i "Want to talk about it?"

            s "Not really."

            i "Cool. Want to not talk about it while sitting in the same room?"

            s_thoughts "I laugh. It hurts my head."

            s "Yeah. That sounds perfect."

        s_thoughts "Something starts. Here. In this kitchen. With terrible coffee and Isabella not looking at me."

        s_thoughts "I don't know what it is yet."

        s_thoughts "I think that's how it starts."
        
        stop music fadeout 3.0
        
        scene black with Fade(1.0, 1.0, 1.0)
        
        "Chapter 3: Cracks -- End"

        $ persistent.completed_chapter3 = True

        ## → ISABELLA ROUTE
        jump izzy_ch4

    elif route == "amara":
        play music mus_amara fadein 2.0

        s_thoughts "No knock."

        s_thoughts "I lie in bed for twenty minutes. Thirty. Nobody comes."

        s_thoughts "I finally get up and walk downstairs. I don't know why."
        
        scene bg entry with dissolve

        s_thoughts "Amara's door is open."

        show amara neutral at center with dissolve

        s_thoughts "She's at her desk. She's reading. She doesn't look up."

        if cruel_target == "Amara":
            s_thoughts "I stop in her doorway."

            s "Amara."

            a "Coffee's made. If you want it."

            s "Amara, what I said last night--"

            s_thoughts "She turns a page."

            a "You said I'm closed off. That my silence is just avoidance dressed up."

            s "I was drunk and I was--"

            a "You were wrong."

            s_thoughts "She still hasn't looked up."

            s_thoughts "Same words as last night. No elaboration. No explanation of WHY I was wrong. Just the verdict."

            s "I know. I'm sorry."

            a "You don't know. That's the problem."

            s_thoughts "She closes the book. Looks at me."

            show amara smile at center

            s_thoughts "It's not a warm look. But it's not cold either. It's... measuring. Like she's deciding something."

            a "But you're sorry. That part I believe."

            s "I am."

            a "Okay."

            s_thoughts "She opens the book again."

            a "Coffee's in the kitchen. I made it strong."

            s_thoughts "I go to the kitchen. The coffee is strong."

            s_thoughts "When I come back, her door is still open."

        else:
            a "Coffee's made. If you want it."

            s "...Thanks."

            s_thoughts "I stand in her doorway. She reads. I stand."

            s_thoughts "She doesn't tell me to come in. She doesn't tell me to leave."

            s_thoughts "The door is open. That IS the invitation."

            s_thoughts "I get the coffee. I come back. I sit on the floor outside her door."

            s_thoughts "She reads. I sit."

            s_thoughts "Twenty minutes."

            show amara smile at center

            a "You can come in. If you want."

            s_thoughts "I do."

        s_thoughts "Something starts. Here. In this doorway. With strong coffee and Amara's door open."

        s_thoughts "I don't know what it is yet."

        s_thoughts "I think that's how it starts."
        
        stop music fadeout 3.0
        
        scene black with Fade(1.0, 1.0, 1.0)
        
        "Chapter 3: Cracks -- End"

        $ persistent.completed_chapter3 = True

        ## → AMARA ROUTE
        jump amara_ch4

    elif route == "eve":
        play music mus_eve fadein 2.0

        s_thoughts "No knock."

        s_thoughts "I lie in bed until the grey light turns white. Nobody comes."

        s_thoughts "I get up. I open my door."
        
        scene bg hallway with dissolve

        s_thoughts "The hallway is empty."

        s_thoughts "Except -- Eve's door."

        s_thoughts "Eve's door is open."

        s_thoughts "I have never seen Eve's door open. Not once. Not since I moved in."
        
        scene bg evebedroom with dissolve

        show eve neutral at center with dissolve

        s_thoughts "She's sitting on her bed. She has her laptop in her lap. She's not watching it."

        s_thoughts "She looks up when I appear in the doorway."

        if cruel_target == "Eve":
            e "I heard what you said."

            s_thoughts "My stomach drops through the floor."

            e "About me. Last night."

            s "Eve, I--"

            e "You said I disappear. That everyone pretends it's normal. That 'mysterious' is just a nice word for 'absent.'"

            s_thoughts "Each word lands like a stone."

            s "I was drunk. I was spiraling about Katie. That doesn't make it--"

            e "You weren't wrong."

            s_thoughts "..."

            show eve sad at center

            e "I do disappear. I know I do. I just..."

            s_thoughts "She stops. Eve stopping mid-sentence is like a bird stopping mid-flight."

            e "Nobody's said it before. Everyone just works around it. Like I'm furniture that's sometimes in the room."

            s "You're not furniture."

            show eve neutral at center

            e "No. But I understand why you'd say it."

            s_thoughts "She looks at her book. Then at me."

            show eve smile at center

            e "Sit down. If you want."

            s_thoughts "I sit down."

            s_thoughts "Eve's room is small and full of books and it smells like tea and laundry and it's the first time I've been inside."

            s_thoughts "Her door was open. For me."

        else:
            e "You look terrible."

            s "I feel terrible."

            e "I know."

            s_thoughts "She looks at her book. Then at me."

            e "I left the door open."

            s "I noticed."

            e "I don't usually do that."

            s "I know."

            s_thoughts "A pause. The longest pause."

            show eve smile at center

            e "Sit down. If you want."

            s_thoughts "I sit down."

            s_thoughts "Eve's room is small and full of books and it smells like tea and laundry and it's the first time I've been inside."

            s_thoughts "She left the door open."

            s_thoughts "She doesn't do that for anyone."

        s_thoughts "Something starts. Here. In this room I've never been in. With Eve and her open door and her laptop she's not watching."

        s_thoughts "I don't know what it is yet."

        s_thoughts "I think that's how it starts."
        
        stop music fadeout 3.0
        
        scene black with Fade(1.0, 1.0, 1.0)
        
        "Chapter 3: Cracks -- End"

        $ persistent.completed_chapter3 = True

        ## → EVE ROUTE
        jump eve_ch4

    ## End of Chapter 3 -- Common Route Complete
    stop music fadeout 3.0

    scene black with Fade(1.0, 1.0, 1.0)

    "The common route is complete."

    "Glass Houses will continue."

    return
