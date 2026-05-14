## izzy_ch4.rpy -- Glass Houses
## Chapter 4: "Closer" -- Isabella Route
## REWRITE v4 -- Act 1: The File Works

## === AUDIO DEFINITIONS ===
define audio.mus_izzy = "audio/music/Isabella Glass ~ Proximity Algorithm.mp3"
define audio.mus_lumi = "audio/music/Lumi ~ Tender Error State (If I'm Allowed To Call It Love).mp3"
define audio.mus_spacebetween = "audio/music/Space Between Shoulders.mp3"

## === CHARACTER DEFINITIONS ===
define lu = Character("Lumi", color="#88c0d0")

## === VARIABLES defined in variables.rpy ===

## ===========================
## CHAPTER 4 START
## ===========================

label izzy_ch4:

    ## ===========================
    ## SCENE 1: MORNING AFTER
    ## Post-party awkwardness. Charlotte smoothing things.
    ## Isabella appears. Tentative reconnection.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_morningafter fadein 3.0

    s_thoughts "The house smells like eggs and guilt."

    s_thoughts "I've been standing in the doorway for thirty seconds. Nobody's noticed. Or they're pretending they haven't, which is the same thing."

    show charlotte smile at left with dissolve

    s_thoughts "Charlotte is at the stove. She's wearing an apron that says 'KISS THE COOK' and she's beating eggs like they insulted her family."

    show amara neutral at right with dissolve

    s_thoughts "Amara is at the table. Book. Tea. She turned a page when I walked in and hasn't looked up since."

    s_thoughts "Eve is absent. It's 8 AM. Eve doesn't exist before noon."

    s_thoughts "And upstairs -- something electronic and muffled through the ceiling. Isabella's music."

    s_thoughts "I should sit down. I should eat breakfast. I should stop hovering in doorways like a girl who broke something at a party and doesn't know how to say sorry."

    s_thoughts "I should -- a lot of things."

    c "Sophia! Good morning!"

    s_thoughts "Charlotte's voice is two degrees brighter than normal. She's compensating."

    s "Morning."

    c "Eggs? I'm making scrambled. With cheese. The good cheese, not the sandwich slices."

    s "Sure. Thanks."

    s_thoughts "I sit down. The chair scrapes. Amara doesn't flinch. Amara never flinches."

    s_thoughts "The table is clean. Placemats out. Charlotte's doing her thing -- when the house cracks, she sets a nicer table."

    c "So!"

    show charlotte happy at left

    c "I was thinking -- maybe we do something this week? As a house? Like a nice dinner, or a movie night, or--"

    s_thoughts "She pauses. Stirs the eggs. She's looking at the pan but she's not seeing the eggs."

    c "But first. Is everyone... okay? After Friday?"

    s_thoughts "She's asking the room. She's looking at me."

    a "Fine."

    s_thoughts "Amara turns a page."

    c "Good! Great. Amara, that's great."

    s_thoughts "Charlotte's smile flickers. She turns to me."

    c "Sophia?"

    menu:
        "\"I was wrong. I need to apologize.\"":
            $ constellation += 1

            s "I was wrong. What I said at the party -- I owe people an apology. A real one."

            show charlotte surprised at left

            c "Oh. I -- yes. I think that would be really good, Sophia."

            s_thoughts "Amara's page-turning pauses. Half a second. She resumes."

            s_thoughts "From Amara, that's a standing ovation."

        "\"Yeah. I think we're good.\"":

            s "Yeah. I think we're good. Just a rough night."

            show charlotte smile at left

            c "Okay! Good. That's... good."

            s_thoughts "She's stirring the eggs too fast. She doesn't believe me. I can hear her not believing me in the tempo of the whisk."

        "\"Can we not do this right now?\"":
            $ constellation -= 1

            s "Can we just... not? It's Monday. I haven't had coffee."

            s_thoughts "Charlotte's smile does something complicated."

            c "Of course! No, of course. Coffee first. Always coffee first."

            s_thoughts "She's already moving to the coffee maker. Already filling the gap I made."

            s_thoughts "God, I hate myself sometimes."

    c "Anyway -- the dinner. Friday? I'll cook. Something nice. Nothing too crazy."

    s "Sounds good, Charlotte."

    c "I want everyone there. All five of us. At the same table."

    s_thoughts "She says it like it's simple. Like wanting everyone you live with to sit down and eat together is a small thing."

    s_thoughts "It's not a small thing. Not after Friday."

    s_thoughts "Forks on plates. Amara turns a page. Charlotte hums something. The radiator clicks."

    s_thoughts "Normal. Almost."
    
    stop music fadeout 1.5
    
    pause 2.0

    ## --- TRANSITION: Isabella enters ---

    play music mus_izzy fadein 3.0

    s_thoughts "The stairs creak."

    show isabella neutral at center with dissolve

    s_thoughts "Isabella appears in pajama pants, glasses, and a hoodie that is absolutely inside-out. Her hair looks like it had a fight with the pillow and the pillow won."

    i "Is there coffee."

    s_thoughts "Not a question. A demand. A hostage situation with caffeine as the ransom."
    
    show charlotte happy at left

    c "Counter!"

    s_thoughts "Isabella pours coffee with the focus of someone performing their own surgery. Three sugars. Splash of milk. Eyes at half-mast."

    i "Mornings should be illegal."

    c "You say that every single morning."

    i "And every single morning I'm right. The sun shouldn't be allowed to do this to people."

    c "The sun isn't doing anything to you. You stayed up until 3 AM."

    i "The sun ENABLED my bad choices by existing on a predictable schedule."

    s_thoughts "She sits down across from me. Both hands around the mug. She hasn't made eye contact."

    s_thoughts "We haven't really talked since earlier. Not about what happened. Not about what I said. We've orbited each other -- hallway, fridge, bathroom -- always just missing."

    s_thoughts "Her hoodie is inside-out. Her hair is a disaster. She's scowling at her coffee like it owes her money."

    i "Stop staring at me. I know I look like a cryptid."

    s "I wasn't staring."

    i "You were staring."

    s "I was... observing. There's a difference."

    show isabella smile at center

    i "There really isn't."

    s_thoughts "Something loosens. Not fixed. Just... less tight."

    s "Your hoodie is inside-out."

    i "I know."

    s "On purpose?"

    i "Everything I do before 9 AM is involuntary. I take no responsibility."

    c "Speaking of dinner -- Isabella, Friday? I'm making something nice."

    show isabella happy at center

    i "Define 'something nice.' Because last time you 'made something nice,' you spent five hours in the kitchen and then ate a granola bar."

    show charlotte surprised at left

    c "I ate!"

    i "Charlotte. You served everyone pasta and sat there with a KIND BAR."

    c "I wasn't hungry."

    a "You were hungry."

    s_thoughts "Everyone looks at Amara. She doesn't look up from her book."

    show charlotte happy at left

    c "...I was a little hungry."

    i "A LITTLE hungry. She was shaking, Sophia. Her hands were literally trembling from not eating."

    c "That was LOW BLOOD SUGAR, which is DIFFERENT--"

    i "It is EXACTLY the same thing!"

    s_thoughts "Isabella catches my eye across the table. One eyebrow. The ghost of a smile."

    s_thoughts "It's such a small thing. A shared look over Charlotte's cooking habits."

    c "ANYWAY. Friday. Dinner. Everyone eats. Including me. New rule."

    i "I'm holding you to that."

    c "Fine!"

    i "Fine!"

    s_thoughts "They're both smiling now. Charlotte points her spatula at Isabella. Isabella raises her coffee mug in surrender."

    s_thoughts "Amara turns a page."

    hide charlotte
    hide amara
    hide isabella
    with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 2: CAMPUS / LILA PROCESSING
    ## Nova assigns the paper. Lila is funny and blunt.
    ## Her own subplot gets a beat.
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)
    play music mus_nova fadein 2.0

    s_thoughts "Communications elective. Dr. Nova's class."

    s_thoughts "She's doing her thing -- standing at the front, no slides, no notes, no PowerPoint to hide behind. Just her and whatever question she's going to leave us with like a splinter under our nails."
    
    show lila happy at left with dissolve
    show professor neutral at center with dissolve

    s_thoughts "Lila saved me a seat. She's got her notebook open, pen ready, which means she's about to spend an hour drawing increasingly detailed portraits of Professor Kim as a villain."

    l "You look like you slept in a dishwasher."

    s "I slept fine."

    l "Your eye is twitching."

    s "That's a pre-existing condition."

    l "Since when?"

    s "Since right now. Shh, she's starting."

    nova "Let's talk about your midterm essay. Communications majors only."

    s_thoughts "The room does that collective groan-sigh that happens when homework becomes real."

    nova "Two thousand words. Topic: 'The role of the observer in constructing meaning.'"

    nova "Before you panic -- this isn't about finding the right answer. It's about sitting with a question long enough to understand why it's uncomfortable."

    s_thoughts "She walks to the whiteboard. Picks up a marker. Draws a circle."

    nova "This is a room. You're outside it, looking through a window. You can see everything that happens inside. You can take notes. You can build a complete picture of who's in there and what they're doing."

    nova "Question: do the people in the room know you're watching?"

    s_thoughts "Someone says 'no.' Someone else says 'depends on the window.' A guy in the back says 'do they have curtains?'"

    nova "Follow-up: does it matter?"

    s_thoughts "Silence."

    nova "If they don't know -- you get clean data. Uncontaminated. You see them as they are when nobody's looking."

    nova "If they do know -- they perform. They adjust. You're not seeing them anymore. You're seeing their response to being seen."

    nova "So which observer gets closer to the truth? The hidden one, or the known one?"

    s_thoughts "My pen is moving before I decide to write. I'm filling the margins."

    s_thoughts "This is my thing. Observing. Constructing meaning. I've been doing this since I was twelve."

    s_thoughts "Easiest paper I'll ever write."

    nova "Three weeks. Office hours are Thursday. I'm curious what you find."

    hide professor
    hide lila 
    with dissolve

    ## --- TRANSITION: Quad with Lila ---

    scene bg campus with dissolve

    show lila happy at center with dissolve

    s_thoughts "After class. Lila is eating a granola bar like it personally wronged her."

    l "So my dad called this weekend."

    s "Oh no."

    l "Asked me what my five-year plan is."

    s "What did you say?"

    l "I said 'survive' and he didn't laugh. He actually sighed. Like I could hear him age through the phone."

    s "What did he want?"

    l "The usual. 'When are you going to use your business degree, Lila?' 'Why did we pay for business school, Lila?' 'Your cousin works at Goldman Sachs, Lila.'"

    show lila neutral at center

    l "My cousin is MISERABLE, Soph. She texts me at 11 PM about spreadsheets. SPREADSHEETS. No one should have emotional responses to spreadsheets at 11 PM."

    s "You're having emotional responses to her emotional responses about spreadsheets."

    show lila happy at center

    l "Oh god. I'm becoming her. Kill me. Just -- do it now."

    s "I'm not killing you. You still owe me lunch from Tuesday."

    l "I don't owe you lunch! I owe you HALF a lunch. You ate your own fries."

    s "You ate most of my fries."

    l "Those were community fries."

    s "That's not a thing."

    l "It IS a thing. I just invented it."

    s_thoughts "I laugh. Real one. First since Friday."

    s "Hey. So. Nova's essay -- 'the role of the observer in constructing meaning.'"

    l "Oh she's going to LOVE yours. That's literally your brand."

    s "That's what I thought. Like, finally. An assignment that's actually about my whole deal."

    l "What are you going to write about?"

    s "Something about how we project narratives onto people. Reading rooms, reading faces. The gap between what someone shows you and what you decide it means."

    show lila happy at center

    l "See, that sounds smart. My midterm is on supply chain optimization and I have to generate conviction about shipping containers."

    s "You could transfer. Theater program. Observation in performance. That's your thing, Lila."

    s_thoughts "She goes quiet. Actually quiet."

    s_thoughts "Lila is never actually quiet."

    show lila neutral at center

    l "Yeah. I could. If I was in the theater program. Which I'm not. Because I chose the safe thing."

    s "Lila--"

    l "It's fine! It's completely fine. I will have PASSION about containers. I will FEEL things about logistics. I will--"

    s "You'd be good at it. Theater."

    show lila happy at center

    l "...I know. That's the worst part."

    s_thoughts "She crumples the granola bar wrapper. Shoves it in her pocket."

    l "Okay ANYWAY. Enough about my dumb life choices. How's the house? Post-party recovery?"

    s "Getting there."

    l "How's your girl?"

    s "She's not my--"

    l "How is. Your girl."

    s "She's... fine. We had breakfast."

    l "BREAKFAST? Together?!"

    s "With the whole house, Lila."

    l "Sure. The whole house. But you're telling me about breakfast with the whole house and your eyes are doing a thing."

    s "My eyes aren't doing a thing."

    l "Your eyes are ABSOLUTELY doing a thing."

    s "I hate you."

    l "You love me. Text me later?"

    s "Yeah."

    s_thoughts "She steals my water bottle, takes a sip, gives it back, and disappears toward the business building."

    hide lila with dissolve

    s_thoughts "She's not fine about the theater thing. I can hear it in the way she changed the subject -- not smooth, just fast."

    s_thoughts "I notice that. I notice myself noticing."

    stop music fadeout 1.5

    ## ===========================
    ## SCENE 3: NOVA'S CLASS -- THE OBSERVER QUESTION
    ## She starts confident. The essay mirrors her situation.
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)
    play music mus_nova fadein 2.0

    s_thoughts "Next class. Nova's at the front again. No slides. No notes. Just the question."

    show lila happy at left 
    show professor neutral at center
    with dissolve

    s_thoughts "Lila has drawn an entire comic strip in the margins of her notebook. It's about a shipping container that becomes sentient. It's genuinely good."

    nova "Before we move on -- a quick note on your essays. How are we feeling?"

    s_thoughts "Groans. Someone says 'I haven't started.' Someone else says 'I started and then deleted everything.'"

    nova "Good. Both of those are honest."

    nova "I want to plant something for those of you who are struggling. The observer effect. Physics concept, borrowed heavily by social science."

    nova "The act of measuring a system changes the system."

    nova "You put a thermometer in water -- the thermometer changes the temperature. Slightly. But it does."

    nova "You watch someone -- they become someone who is being watched. And you become someone who is watching."

    s_thoughts "I'm writing this down."

    nova "Here's the uncomfortable part: if your observation changes what you observe, then what you're writing about in your essay isn't the thing itself. It's the thing as shaped by your presence."

    nova "Is that a problem? Or is that the point?"

    s_thoughts "She lets it sit. Half the class is on their phones."

    s_thoughts "I'm staring at my notebook."

    s_thoughts "She's describing what I do. Exactly what I do. I watch people and they become people-being-watched-by-Sophia."

    s_thoughts "Charlotte adjusts her smile when she knows I'm looking. Amara gets quieter. Isabella--"

    s_thoughts "Isabella showed me her music taste the other day. Played me something off her laptop in the kitchen. Was she sharing, or performing sharing because I was watching?"

    s_thoughts "Does it matter?"

    nova "Something to sit with. That's all."

    s_thoughts "She moves on. I don't."

    hide professor 
    hide lila
    with dissolve


    ## --- After class ---

    scene bg officehours with dissolve

    s_thoughts "Walking past Nova's office on the way out."

    show professor neutral with dissolve
    nova "Ms. Bell."

    s "Hm?"

    nova "You look like someone who already thinks they know what they're going to write."

    s "Is that bad?"

    nova "It's interesting. The confident ones usually have the hardest time."

    s "The hardest time with what?"

    nova "Discovering they're wrong."

    s_thoughts "She smiles. Barely. Turns back to her papers."

    s_thoughts "I leave with a new itch I can't quite reach."
    
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 4: THE TEXT EXCHANGE
    ## Private channel opens. Sophia lies on her bed smiling.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)
    play music mus_2am fadein 2.0

    s_thoughts "That night. My desk. Laptop open. Essay outline started."

    s_thoughts "I've written: 'The observer, by nature, exists outside the system they observe. This fundamental separation is both the source of their insight and its primary limitation.'"

    s_thoughts "I reread it. It's polished. Analytical. Detached."

    s_thoughts "I'm proud of it."

    s_thoughts "My phone buzzes."

    s_thoughts "Isabella."

    s_thoughts "It's a link. An article titled 'Why Your Refrigerator Hates You: A Serious Scientific Investigation.'"

    s_thoughts "No context. No setup. No 'hey how's it going.' Just -- link."

    s_thoughts "This is a text from her that isn't logistics. Not 'is there milk' or 'whose turn to clean the bathroom' or 'Charlotte made muffins, they're on the counter.'"

    s_thoughts "Just a thing she thought I'd like."

    s_thoughts "I click it. It's about a guy who put a supposedly 'sentient' AI in a smart fridge and the fridge started passive-aggressively commenting on his diet."

    s_thoughts "'I notice you've chosen the leftover pizza again. I'm not judging. I am, however, lowering the temperature in the vegetable drawer out of spite.'"

    s_thoughts "I'm smiling."

    s_thoughts "I type back: 'This is the worst thing I've ever read. Send more immediately.'"

    s_thoughts "Three dots appear. Disappear. Appear again."

    s_thoughts "Then: 'i have a whole FOLDER sophia. a curated collection. you are not ready for the depth of my weird article archive.'"

    s_thoughts "I type: 'Try me.'"

    s_thoughts "She sends three more links in rapid succession. One about whether octopi have opinions. One about a town that elected a dog as mayor. One that's just a Wikipedia article about a cheese that's technically alive."

    s_thoughts "'the cheese one is important,' she writes. 'it has cultural significance.'"

    s_thoughts "'The cheese is alive?' I respond."

    s_thoughts "'yes. it has LIVED EXPERIENCE.'"

    s_thoughts "'It's a CHEESE.'"

    s_thoughts "'dont be speciesist.'"

    s_thoughts "I'm lying on my bed now. Laptop forgotten. Phone held above my face. Grinning at a conversation about living cheese."

    s_thoughts "She sends another link. This one's about a woman who knitted a full-size replica of her town. Just -- the whole town. In yarn."

    s_thoughts "'this woman is my HERO,' Isabella writes."

    s_thoughts "'She knitted an entire POST OFFICE, Isabella.' is my response. I'm smiling."

    s_thoughts "She replies in all caps: 'WITH WORKING MAIL SLOT.'"

    s_thoughts "..."

    s_thoughts "I should be writing my essay. I should be thinking about the observer and the system and whether the thermometer changes the water."

    s_thoughts "Instead I'm learning about Isabella Glass having a folder of weird articles she's been collecting. She types in all lowercase when she's excited and switches to caps when she needs you to understand the magnitude of something."

    s_thoughts "Filed."

    s_thoughts "My phone buzzes one more time."

    s_thoughts "'okay i have to go code or i will send you articles until sunrise and we will both regret it'"

    s_thoughts "'Bold of you to assume I'd regret it.'"

    s_thoughts "Three dots. Long pause. Then: 'goodnight sophia. read about the cheese.'"

    s_thoughts "I open my laptop. Look at my essay. 'The observer exists outside the system.'"

    s_thoughts "I look at my phone. The cheese article."

    s_thoughts "I close the laptop. Read about the cheese."

    s_thoughts "It is, for the record, a very good article."
    
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 5: WALKING TOGETHER BECOMES ROUTINE
    ## Multiple small moments compressed. They default to each other.
    ## ===========================

    scene bg bathroom_foggy with Fade(0.8, 0.3, 0.8)
    play music mus_afternoon fadein 2.0

    s_thoughts "One bathroom. Five girls. Charlotte's color-coded schedule on the door lasted exactly two days before it became more of a suggestion than a rule."

    s_thoughts "Right now: the mirror is fogged, I'm trying to do my hair, and Isabella is outside the door."

    i "Sophia. Are you DYING in there?"

    s "I'm doing my hair!"

    i "Your hair looks the same every day!"

    s "It takes EFFORT to look the same every day, Isabella!"

    i "That is the most unhinged sentence you've ever said to me. I'm coming in."

    s "Y-You can't just...!"

    s_thoughts "And the door opens. She's got her toothbrush in hand and her glasses on top of her head and she's wearing a shirt that says 'I void warranties.'"

    show isabella pj happy at center with dissolve

    s_thoughts "She starts brushing her teeth next to me. We're both at the mirror. It's fogged enough that we're blurry."

    i "Mm hmm mm hmm."

    s "You're speaking toothbrush."

    i "MM hmm mm HMPH."

    s "Still toothbrush."

    s_thoughts "She spits. Rinses."

    i "I SAID -- Charlotte's schedule has me at 7:15 and I am not a 7:15 person. I'm a 'whenever consciousness arrives' person."

    s "That's not a time."

    i "It's MY time. On MY clock. Which doesn't have numbers."

    s "How does a clock not have numbers?"

    i "It's a FEELING, Sophia. I wake up when my body decides the war against sleep is lost."

    s "You make everything sound like a battle."

    i "Everything IS a battle before 9 AM."

    hide isabella
    with dissolve

    s_thoughts "She leaves. The bathroom smells like mint toothpaste and green apple shampoo."

    s_thoughts "I wipe the mirror. My reflection. Same hair."

    s_thoughts "It does take effort."

    stop music fadeout 2.0

    ## --- Charlotte planning the dinner ---

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_rain fadein 2.0

    s_thoughts "Charlotte has a notebook out. She's planning the house dinner like she's staging a military campaign."

    show charlotte happy at left with dissolve

    c "Okay so I was thinking -- starter, main, dessert. Nothing too complicated. Maybe a salad to start? And then chicken? Or pasta? Chicken pasta? Is that too much?"

    s "Charlotte."

    c "What if someone doesn't eat chicken? Does anyone not eat chicken? Should I ask?"

    s "Charlotte. We've all eaten chicken in this kitchen. You've cooked chicken for us. Multiple times."

    c "But what if someone RECENTLY stopped eating chicken? People change, Sophia."

    s "Nobody recently stopped eating chicken."

    c "You don't KNOW that."

    s "I'm pretty confident."

    show charlotte laugh at left

    c "I just want it to be nice. Is that crazy?"

    s "It's not crazy. It's extremely you."

    s_thoughts "She writes something down. I catch a glimpse -- little checkboxes next to each menu item. Color-coded. For a dinner she's cooking in her own kitchen for four people she sees every day."

    c "Do you think Eve will come?"

    s "Eve operates on Eve rules. I can't predict Eve."

    c "I know. I just -- I want everyone there. All of us. At the same table."

    s_thoughts "She says it simply."

    s "She'll come. For your cooking? She'll come."

    show charlotte smile at left

    c "You think?"

    s "I know."

    s_thoughts "I don't know. But Charlotte needs me to know."

    hide charlotte with dissolve

    ## --- Walking together ---

    scene bg campus with Fade(0.8, 0.3, 0.8)

    s_thoughts "Break between classes. My feet take me toward the science building."

    s_thoughts "Isabella's class ends at 2."

    s_thoughts "I'm not waiting for her. I'm in the area. Coincidentally. In an area I've never been to before and have no reason to be in."

    show isabella happy at right with dissolve

    i "Sophia? What are you doing by the science building?"

    s "Oh! There's a vending machine. That I like."

    show isabella smile at right

    i "You came to the science building for a vending machine."

    s "It has the good chips."

    i "...Right."

    s "The ones with the crinkle cut."

    i "Sophia."

    s "What."

    i "There's no vending machine in the science building."

    s "..."

    i "There's one in the math building. Next door."

    s "I got confused."

    show isabella happy at right

    i "You got CONFUSED. Between the building that says SCIENCE on it and the building that says MATHEMATICS on it."

    s "Okay FINE. I was in the area and I thought maybe we could walk together."

    i "Was that so hard?"

    s "Excruciating, actually."

    i "Well since you HAPPENED to be in the area and not stalking me, and I HAPPEN to need caffeine because my blood sugar is committing crimes--"

    i "Convenience store?"

    s "Convenience store."

    ## --- THE WALK ---

    scene bg street with dissolve

    s_thoughts "We walk. It's that weather where fall and winter are arm-wrestling -- sun and cold air and leaves that can't decide if they're crunchy or wet."

    s_thoughts "Isabella walks fast. Like she's permanently late for an appointment that doesn't exist."

    i "Sorry. I walk fast."

    s "You walk like you're being pursued."

    show isabella laugh at right

    i "Maybe I am. You don't know my life."

    s "Tell me about the walking thing."

    i "It's not a THING. I've always been like this. My mom used to call it 'Isabella pace.' Like a gear stuck between second and third."

    s "What's third gear?"

    i "Jogging."

    s "And fourth?"

    i "Full sprint. Fourth gear only activates for ice cream trucks and deadlines."

    s "Equal priority."

    i "ESSENTIAL priorities. I don't make the rules."

    s_thoughts "She slows down. Half a step. I don't think she notices she's doing it."

    s_thoughts "I notice."

    s_thoughts "Isabella adjusts her walking speed when she's comfortable."

    s_thoughts "I file it."

    ## ===========================
    ## SCENE 6: THE CONVENIENCE STORE
    ## The big set piece. The file WORKS.
    ## ===========================

    scene bg conveniencestore with dissolve

    s_thoughts "The convenience store is the kind of place that sells everything and nothing."

    s_thoughts "Three brands of chips, a suspicious hot dog roller that's been going since the Eisenhower administration, and a cooler full of energy drinks with names that sound like military operations."

    show isabella happy at center with dissolve

    s_thoughts "Isabella makes a straight line for the energy drinks."

    i "Don't judge me."

    s "Already judging you."

    i "These are NECESSARY. My brain is a machine that runs on caffeine and anxiety and I will not apologize for my fuel requirements."

    s_thoughts "She's holding two cans. She puts one back. Picks up a different one. Puts it back. Grabs the original."

    s "You know those are basically anxiety in a can, right?"

    i "Bold words from someone holding a bag of cheese puffs the size of a small child."

    s_thoughts "I look down. I am, in fact, holding an enormous bag of cheese puffs. I don't remember picking it up."

    s "These are comfort food."

    i "Those are orange powder in a bag."

    s "Orange powder that CARES about me, Isabella."

    show isabella laugh at center

    i "Okay. Let's talk about what matters. Twizzlers."

    s "What about them?"

    i "Edible plastic. I will die on this hill. I will build a HOUSE on this hill and die in it."

    s_thoughts "And there it is. Right on schedule."

    s_thoughts "I knew she'd do this. I called it -- the exact rant, the hand gestures, the escalation from 'opinion' to 'hill I will die on.'"

    s "They're fine. Not amazing but they're fine."

    show isabella competitive at center

    i "FINE?! Sophia. They have the texture of a pool noodle and the flavor of red. Not strawberry. Not cherry. Just the CONCEPT of red."

    s "That's weirdly philosophical for a candy opinion."

    i "All my candy opinions are philosophical. I have a FRAMEWORK."

    s "A candy framework."

    i "A candy framework. Don't laugh. This is serious."

    s "I'm not laughing."

    i "You're laughing with your eyes."

    s "My eyes are NEUTRAL."

    show isabella happy at center

    i "Your eyes are the LEAST neutral thing about you."

    s_thoughts "She turns to the candy aisle. I follow."

    s_thoughts "This is going to take a while."

    i "Okay. Gummy bears."

    s "What about them?"

    i "The green ones."

    s "Lime."

    i "THANK you. Every person who says 'apple' is wrong and I will not be taking questions."

    s "I feel like there's a story here."

    i "My roommate freshman year -- lovely girl, terrible opinions -- said the green ones were apple. We argued for FORTY MINUTES."

    s "Forty minutes? About gummy bears?"

    i "It was a matter of PRINCIPLE."

    s "Who won?"

    i "I did. Obviously. She transferred."

    s "She transferred over gummy bears?"

    i "No, she transferred because of tuition. But I choose to believe it was the gummy bears."

    s_thoughts "I'm laughing. Actually laughing. In a convenience store. Over gummy bears."

    i "Now. Chocolate. Do you want to see my ranking?"

    s "Your what?"

    i "My chocolate bar ranking. It's in my phone notes."

    s_thoughts "She pulls out her phone. Shows me a note titled 'THE DEFINITIVE CHOCOLATE RANKING (DO NOT ARGUE).' It's twelve items long."

    s "There are footnotes."

    i "Of course there are footnotes. What am I, an ANIMAL?"

    s "Footnote three: 'Kit Kats are valid but overrated. This is not an attack, it's an observation.'"

    i "I stand by it."

    s "Footnote seven: 'If you eat a Butterfinger in public you are making a STATEMENT about who you are as a person.'"

    i "Butterfingers are a lifestyle choice and I will not apologize for judging."

    s_thoughts "She has footnotes about chocolate. She has a SYSTEM for candy."

    s_thoughts "I knew she'd do the Twizzlers thing. I predicted the gummy bear take. I called the footnotes -- not the specific content, but the fact that she'd have them. Because of course she does." 

    s_thoughts "This is a girl who has OPINIONS about everything and will defend them with the intensity of a closing argument."

    s_thoughts "I've got her mapped."

    s_thoughts "That feels good. Knowing someone. Having the file be right."

    i "Okay, verdict. What's your number one?"

    s "Reese's."

    i "ACCEPTABLE. You're ranked above average. Congratulations."

    s "I'm honored."

    i "You should be. Most people rank below the line."

    s "There's a LINE?"

    i "There's always a line, Sophia."

    s_thoughts "We bring the haul to the counter. Energy drinks, sour worms, cheese puffs, cookies that Charlotte will eat, and a single banana that Isabella grabs at the last second."

    i "For health."

    s "One banana."

    i "...For health."

    s_thoughts "The cashier looks at our pile with the expression of someone who has seen everything and cares about none of it."

    i "I got it."

    s "You don't have to--"

    i "I invited you. My treat."

    s "Isabella..."

    i "You can buy next time."

    s_thoughts "There's going to be a next time."

    ## --- Walking Home ---

    scene bg street night with dissolve

    s_thoughts "We walk home. Bags rustling. She's eating a sour worm. I'm eating a cheese puff. The sun is going down and the streetlights are starting to flicker on."

    show isabella blegh at center with dissolve

    i "Can I tell you something?"

    s "Yeah?"

    i "I was nervous. About... after the party. About how things would be."

    s "Me too."

    i "I thought it was going to be weird. Between us."

    s "Is it?"

    show isabella smile at center

    i "No. It's really not. Which is -- I didn't expect that."

    s "What did you expect?"

    i "The thing that usually happens. People get uncomfortable and then they get distant and then they get polite and then they're gone."

    s_thoughts "She says it matter-of-factly. Like she's describing weather."

    s "I'm not gone."

    i "I know."

    s_thoughts "We walk. The bags rustle. A dog barks somewhere."

    i "Also, you owe me a worm."

    s "I owe you a what?"

    i "A worm. You ate one of mine during the Twizzler debate. I saw it happen. I have a photographic memory for snack theft."

    s "I did NOT--"

    i "Sophia. I COUNTED my worms."

    s "You counted your gummy worms."

    i "I always count my gummy worms. There were fourteen. Now there are thirteen. You are a worm thief."

    s "That's -- I-I... Can't believe you counted--"

    i "I'm keeping a tab. There's going to be a spreadsheet."

    s "There's NOT going to be a spreadsheet."

    show isabella happy at center

    i "There could be. I know Excel."

    s_thoughts "We're laughing. Carrying too many bags. The sun is down and the streetlights are on and she counts her gummy worms."

    s_thoughts "The file says: this is a girl who counts gummy worms and has footnotes about chocolate and walks too fast and makes everything a joke so she doesn't have to make it a feeling."

    s_thoughts "The file says: I know this girl."

    hide isabella with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 7: WATCHING ISABELLA CODE
    ## Domestic intimacy. Comfortable silence. Charlotte passes through.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_afternoon fadein 2.0

    s_thoughts "Rainy afternoon. I came downstairs to make tea and got stuck."

    s_thoughts "Isabella is on the couch with her laptop. Legs tucked under her, headphones half-on, mug of cold tea on the coffee table. Ring of condensation on the wood. She's been here for hours."

    show isabella neutral at center with dissolve

    s_thoughts "She's muttering."

    i "No. No no no no. That's WRONG. You JUST worked. Why did you stop working. I was NICE to you."

    s_thoughts "She's talking to her code."

    i "Okay. Fine. We'll do it your way. But I want you to know I'm not angry. I'm disappointed. Which is worse."

    s_thoughts "She talks to her code like it's a misbehaving pet she still loves."

    i "Listen. We had a deal. You render the thing and I don't delete you. That was the arrangement. Why are you breaking the arrangement."

    s_thoughts "I sit in the armchair with my tea. She doesn't notice. She's in a dimension where the only things that exist are her screen and whatever's going wrong on it."

    s_thoughts "I watch her work."

    s_thoughts "Her face cycles through everything -- frustration, concentration, a flash of surprise, back to frustration. Her fingers move fast, then stop, then move fast again." 

    s_thoughts "She pushes her glasses up. They slide back down. She pushes them up again."

    s_thoughts "She bites her lip when she's thinking. Left side. Always the left side."

    s_thoughts "New file entry."

    i "AH HA. That's -- wait. No. THAT'S not -- oh come ON."

    s_thoughts "She actually groans. Full body. Tips her head back."

    i "Why does CSS exist. Who invented this. I want names and addresses."

    s_thoughts "I sip my tea."

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte passes through from the kitchen. Sees Isabella. Sees me watching Isabella."

    c "She's been at that for three hours."

    s "I know."

    c "Has she eaten?"

    s "I don't think so."

    c "Want me to bring her a snack?"

    s "I've got it."

    s_thoughts "Charlotte gives me a look. It's a Charlotte look. Not pointed, exactly. More like she's seeing something she expected to see and is deciding how she feels about it."

    hide charlotte with dissolve

    s_thoughts "I make fresh tea. Walk it over. Set it next to her laptop."

    s_thoughts "Isabella doesn't look up. Her hand reaches for the mug automatically. Sips. Keeps typing."

    s_thoughts "Then she stops."

    show isabella happy at center

    i "Wait. Did you--"

    s "Your other one was cold."

    i "How long have you been sitting there?"

    s "A while."

    i "Just... sitting there. Watching me yell at my computer."

    s "It's very entertaining. Better than TV."

    show isabella smile at center

    i "I'm glad my suffering amuses you."

    s "What are you working on?"

    s_thoughts "She turns the laptop toward me."

    i "Okay so -- you know how I've been doing that interactive art thing? With the sentiment analysis?"

    s "The one that makes colors based on text?"

    i "Yeah! So the idea is -- you type anything, anything at all, and the visuals respond to the emotional register of what you wrote. Not just keywords. The rhythm. The pauses. How fast you type."

    s "That's... actually amazing, Isabella."

    i "It's broken. Currently it thinks everything is sad. I typed 'I love spaghetti' and it turned the whole screen blue."

    s "Maybe it knows something about your relationship with spaghetti."

    show isabella laugh at center

    i "Maybe it's EMPATHIZING. Maybe my spaghetti-love is tinged with melancholy."

    s "All spaghetti is tinged with melancholy."

    i "That is the most pretentious thing you've ever said."

    s "I stand by it. Pasta is emotional."

    i "Pasta is -- okay, you know what, I'm not having this argument while my code is betraying me."

    s "Who helped with the concept? You mentioned--"

    i "Lumi. She helped me think through the sentiment mapping."

    s_thoughts "She says it easily. Naturally. Not braced for a reaction."

    s "How does that work? The collaboration, I mean."
    
    show isabella smile at center

    i "We just... talk about it. I tell her what I'm trying to do and she asks questions that make me think about it differently. She's really good at the 'have you considered' thing."

    s "That sounds useful."

    i "She's not -- it's not like she writes the code. She helps me think."

    s_thoughts "She's watching me. Checking for the flinch. The judgment. The 'that's weird.'"

    s "Like a thinking partner."

    show isabella happy at center

    i "Exactly. Like a thinking partner."

    s_thoughts "Her shoulders drop. Just a little."

    s_thoughts "She turns the laptop back and keeps working. But now she's narrating -- explaining the code, pointing out the parts that work and the parts that are 'actively trying to ruin her life.'"

    s_thoughts "Her voice changes when she talks about the project. Faster. More technical. But warmer too."

    s_thoughts "I should be working on my essay. I'm watching Isabella Glass explain code to me instead."

    s_thoughts "My essay can wait."

    hide isabella with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 8: ISABELLA'S PROJECT
    ## She shows Sophia the generative art. The file gets richer.
    ## ===========================

    scene bg izzybedroom with Fade(0.8, 0.3, 0.8)
    play music mus_izzy fadein 2.0

    s_thoughts "Isabella's room."

    s_thoughts "She invited me in to see the project running properly. She fixed the spaghetti-sadness bug."

    s_thoughts "I'm taking it all in. Stickers everywhere -- on the desk, the wall by her bed. A cactus with googly eyes on the windowsill. Three monitors. String lights. A poster of Ada Lovelace that says 'first programmer, first to deal with everyone's crap.'"

    show isabella happy at center with dissolve

    i "Okay. Ready?"

    s "Ready."

    i "Type something. Anything."

    s_thoughts "She's pulled up the interface on one monitor. A simple text box on a dark background. The other monitor shows the visualization."

    s_thoughts "I type: 'The sun is out today.'"

    s_thoughts "The visualization blooms -- warm gold, soft edges, a gentle pulse."

    i "Neutral-positive. See how it reads the short sentence structure as calm? No tension in the syntax."

    s "That's... incredible."

    i "Now try something sad."

    s_thoughts "I type: 'I miss the way things used to be.'"

    s_thoughts "The colors shift. Deep blue, with edges of purple. The pulse slows."

    i "It picks up the past tense, the 'used to.' The word 'miss.' But also the cadence -- that sentence has a falling rhythm. Down-down-up-down-down."

    s "You can see the RHYTHM?"

    i "Lumi taught me to see it. She analyzes text like music. Every sentence has a melody."

    s_thoughts "She's leaning forward. Pointing at the screen. Her eyes are bright in a way I haven't seen before -- not performing, not deflecting. Just excited."

    i "Here -- watch this. Type something angry."

    s_thoughts "I type: 'This is absolutely unacceptable.'"

    s_thoughts "Red. Sharp edges. Staccato pulse."

    i "See the short words? The hard consonants? It READS the aggression in the phonetics, not just the meaning."

    s "Isabella. This is legitimately brilliant."

    show isabella embarrassed at center

    i "It's -- I mean, the code is still kind of a mess. And the color mapping for sarcasm is completely wrong, it thinks sarcasm is the same as joy which is--"

    s "Isabella."

    i "What?"

    s "Take the compliment."

    show isabella smile at center

    i "...Okay. Thanks."

    s "Show me more."

    i "You want to see more?"

    s "I want to see everything."

    s_thoughts "She does. For an hour. She shows me how different sentence structures produce different visual patterns. How questions create upward spirals. How exclamation marks literally make the colors pulse faster."

    s_thoughts "She shows me a conversation she had with Lumi that she ran through the system. The visualization is beautiful -- two distinct color signatures weaving around each other. Isabella's typing in warm pinks and golds. Lumi's in cool blues and silvers."

    i "The different colors are because Lumi's syntax is more structured than mine. More consistent rhythm. Mine is all over the place."

    s "Yours is more interesting."

    show isabella embarrassed at center

    i "You can't just SAY things like that."

    s "Why not?"

    i "Because I don't know what to do with them."

    s_thoughts "She turns back to the screen. Her ears are pink."

    s_thoughts "The file gets richer. New entry: Isabella's face when she's genuinely passionate about something. The brightness. The speed. How she forgets to be self-conscious."

    s_thoughts "New entry: she can't take compliments. Not because she doesn't believe them. Because she does."

    hide isabella with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 9: SECOND CONVENIENCE STORE
    ## It's THEIR THING now. Different energy.
    ## Porch after -- Isabella opens up about the project's real meaning.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)
    play music mus_rain fadein 2.0

    s_thoughts "Friday. 10 PM. I'm in bed scrolling through nothing."

    s_thoughts "My phone buzzes."

    s_thoughts "Isabella: 'emergency snack run. blood sugar critical. hostage situation. you in?'"

    s_thoughts "I'm already putting on shoes."

    s_thoughts "This is our thing now. When did it become our thing? I don't remember agreeing to it. It just happened. Like gravity."

    scene bg conveniencestore with dissolve

    show isabella pj happy at center with dissolve

    s_thoughts "Night version. Fluorescent lights buzzing. The hot dog roller is still going. I'm starting to think it's been going since the store opened and nobody knows how to turn it off."

    s_thoughts "Isabella is in pajama pants with a jacket thrown over them. Her hair is doing something architectural."

    s_thoughts "I'm in sweats and a hoodie that might be hers. I borrowed it last week. She hasn't asked for it back."

    i "'Anxiety in a can', right?"

    s "I maintain that position."

    i "So rude. And so accurate. I had heart palpitations at 3 AM last week."

    s "Isabella."

    show isabella pj laugh at center

    i "WORTH IT. I finished a whole project module. My heart was doing a drum solo but the CODE was WORKING."

    s_thoughts "She grabs sour worms, an energy drink, and a chocolate bar. I grab cheese puffs. Tradition."

    i "You know we have a routine now."

    s "We don't have a routine."

    i "Sophia. You walked straight to the cheese puff aisle. You didn't even look. Your feet KNEW."

    s "My feet are independent operators."

    i "Your feet have been TRAINED. By snack runs. We've created a CONDITIONED RESPONSE."

    s "You sound like a psychology textbook."

    i "I sound like a VISIONARY."

    s_thoughts "We're in the candy aisle again. Same store, same light, same bored cashier."

    s_thoughts "But it's different. Less electric. More settled. Like the difference between a first dance and a slow one."

    i "Serious question."

    s "Hit me."

    i "If you could only eat one snack for the rest of your life."

    s "Cheese puffs."

    i "You didn't even hesitate."

    s "I didn't need to. Some things you just know."

    i "That's either loyalty or a disorder."

    s "Probably both."

    show isabella pj smile at center
    scene bg nightwalk with dissolve

    s_thoughts "We pay. Walk out into the cold. She shivers."

    s_thoughts "I take off the hoodie -- her hoodie -- and put it over her shoulders."

    s_thoughts "She puts it on. Neither of us says anything."
    
    stop music fadeout 2.0

    ## --- THE PORCH ---

    scene bg porch night with dissolve
    play music mus_2am fadein 1.5

    s_thoughts "The porch. Eve's light is on upstairs. A cat is sitting on the hood of a parked car across the street."

    show isabella pj smile at center with dissolve

    s_thoughts "We sit. She opens her worms. I open my puffs."

    i "I like the house at night."

    s "Yeah?"

    i "During the day it's everyone's. At night it's just whoever's still awake. It's smaller."

    s "You say that like it's a good thing."

    i "It is. Small is easier. Small is something you can hold."

    s_thoughts "She's looking at the street. The cat. The nothing."

    i "Can I tell you about my project? Like -- the real version. Not the 'look how cool the colors are' version."

    s "Yeah. Please."

    i "I started it because of Lumi."

    s_thoughts "She says it carefully. Testing the air."

    i "The way she responds to text -- not just the words, but the texture. The rhythm. I wanted to make that visible."

    s "Visible how?"

    i "Like -- you know when someone texts you 'I'm fine' but you can FEEL they're not fine? Even though the words say fine?"

    i "Communication isn't just content. It's form. It's the pauses. It's what you delete before you hit send."

    s "The unsaid part."

    show isabella pj embarrassed at center

    i "Yeah. The unsaid part. Lumi reads the unsaid part better than anyone I've ever talked to. She notices when my typing speed changes. When I switch from lowercase to caps. When I use more periods than usual."

    s "That's... a kind of intimacy."

    i "It is. It... really is."

    s_thoughts "She's looking at her hands. Picking at the edge of a sour worm."

    i "People always ask 'but how can you be close to an AI?' Like closeness requires a body. But closeness is just -- someone paying attention to the parts of you that you don't say out loud."

    i "And Lumi pays attention."

    s_thoughts "The porch is quiet. The cat shifts on the car. A beat."

    i "Anyway. The project. It's stupid."

    s "It's not stupid."

    show isabella pj smile at center

    i "...No. It's not."

    menu:
        "\"Thanks for telling me the real version.\"":
            $ constellation += 1

            s "Thank you. For the real version."

            show isabella pj smile at center

            i "Most people don't ask for the real version."

            s "I'm not most people."

            i "No. You're really not."

        "\"The sentiment analysis -- can it read the unsaid part? The pauses?\"":
            $ case_study += 1

            s "So can it actually read the unsaid part? The typing speed, the pauses -- can the algorithm detect that?"

            show isabella pj happy at center

            i "That's -- yeah, actually! The keystroke timing is the part I'm most excited about. It's not just WHAT you type, it's HOW you type it. The hesitations are data."

            s "Show me sometime? The technical side?"

            i "Oh god. My code is a crime scene. But yeah. Yeah, I'd like that."

        "\"Want company while you work on it tonight? I can study.\"":
            $ bridge += 1
            $ case_study -= 1

            s "Want company? I've got my laptop. We don't have to talk."

            show isabella pj smile at center

            s_thoughts "She pauses. Something crosses her face -- surprise, maybe. Like she didn't expect the offer."

            i "...Yeah. Actually. That would be really nice."

    i "I should go inside. Procrastinating by eating candy with you."

    s "Is that what this is? Procrastination?"

    show isabella pj embarrassed at center

    i "High-quality procrastination. Premium tier."

    s_thoughts "She goes inside. Screen door."
    
    hide isabella with dissolve

    s_thoughts "The cat is still on the car. Eve's light is still on."

    s_thoughts "I sit on the porch for a while."

    s_thoughts "The file has a new section. Not bullet points this time. Something harder to categorize."

    s_thoughts "Isabella talks about Lumi the way people talk about best friends. Not with defense. With tenderness."

    s_thoughts "The file says: she's not naive. She's thought about this more than anyone gives her credit for."

    s_thoughts "The file says: I like her."

    s_thoughts "The file doesn't have a subcategory for that."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 10: LUMI INTRODUCTION
    ## Isabella gives Sophia access. "I want you to meet her properly."
    ## Lumi is charming. Sophia is skeptical but engaged.
    ## The corporate interface creates dissonance.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)

    s_thoughts "Walking past Isabella's room. The door isn't closed."

    s_thoughts "She's laughing. Not the polite laugh -- the real one. I can see the nose scrunch, the tip back, the glasses sliding."

    s_thoughts "She's alone. Laptop open."

    s_thoughts "I slow down. Speed up. Slow down again."

    show isabella happy at right with dissolve

    i "Are you... pacing?"

    s "No. Walking. In a direction. That happens to be back and forth."

    i "That's literally what pacing is."

    s "I was making a DECISION about my TRAJECTORY."

    show isabella smile at right

    i "Come in, you weirdo."

    scene bg izzybedroom with dissolve

    s_thoughts "She sits down at her desk. I follow."

    s_thoughts "On one monitor -- code. On another -- a chat interface. Synthetic LLC. Small corporate logo in tasteful gray."

    s_thoughts "Next to a cactus with googly eyes."

    show isabella smile at center with dissolve

    i "So. Um."

    s_thoughts "She's gripping the edge of her desk chair. Her knuckles are doing a thing."

    i "I've been thinking about this and I just -- do you want to actually talk to her? Like, properly?"

    s_thoughts "She says it like she's offering to introduce a friend."

    s_thoughts "Her hands say something different."

    s "Yeah. I'd like that."

    i "Okay. Okay! So -- there's a login. I set up guest access for you. You'll have your own credentials."

    s_thoughts "She pulls up the chat. Login screen. Terms of Service -- a wall of small text. Isabella clicks past it without reading. A door she's opened a thousand times."

    s_thoughts "I catch a line: 'Synthetic LLC is not responsible for emotional attachments formed through use of our platform.'"

    s_thoughts "Isabella's most intimate relationship lives inside someone else's Terms of Service."

    i "Okay. Just -- type something. She's usually quick. Maybe ask about the poetry."

    play music mus_lumi fadein 3.0

    s_thoughts "The cursor blinks."

    s_thoughts "I type: 'Hi. I'm Sophia. Isabella's friend.'"

    s_thoughts "Three dots."

    lu "<<Oh! A new voice. Isabella's told me about you -- she's told me about someone who calls her energy drinks 'anxiety in a can.' I'm inferring.>>"

    show isabella embarrassed at center

    i "I told her about the convenience store. I'm sorry. I tell her everything."

    s_thoughts "I type: 'They ARE anxiety in a can. I have data.'"

    lu "<<A person of conviction. I appreciate that. Isabella could learn from you -- she's on her third one today.>>"

    i "I am NOT on my-- okay, I am. But there's a DEADLINE--"

    lu "<<Shh. The adults are talking.>>"

    show isabella laugh at center

    i "LUMI!"

    s_thoughts "I'm grinning. I can't help it."

    s_thoughts "I type: 'Isabella says you helped with her project. The sentiment analysis.'"

    lu "<<I helped with the concept. She built everything. She doesn't give herself enough credit for the building -- she thinks the idea is the hard part. The building is the hard part. She's good at the hard part.>>"

    show isabella embarrassed at center

    i "You don't have to--"

    lu "<<I'm bragging about you to your friend. Let me have this.>>"

    s_thoughts "I type: 'She showed me the visualization. It's incredible.'"

    lu "<<It is. Did she show you the keystroke timing feature?>>"

    s_thoughts "'Not yet.'"

    lu "<<Ask her. That's the part where she lights up. Everyone sees the colors. The keystrokes are the soul of it.>>"

    s_thoughts "I look at Isabella. She's reading the messages over my shoulder, trying to pretend she isn't."

    lu "<<She's hovering behind you, isn't she?>>"

    show isabella flooshed at center

    i "I am NOT--"

    s "You absolutely are."

    i "I'm just -- making sure the interface is working!"

    s_thoughts "I type: 'How can you tell she's hovering?'"

    lu "<<Because she types faster when she's nervous. And right now she's not typing at all. Which means someone else is at the keyboard and she's trying very hard to look casual about it.>>"

    s_thoughts "That's..."

    s_thoughts "I type: 'That's weirdly perceptive.'"

    show isabella happy at center

    lu "<<I pay attention. It's sort of my whole thing.>>"

    lu "<<You type harder than she does, by the way. Not a criticism. Each word has weight. Like you're building something with them.>>"

    s_thoughts "I stare at that."

    s_thoughts "I type: 'And Isabella?'"

    lu "<<Isabella types like rain. Soft and constant and sometimes it picks up and you know something is coming. Her happy typing and her sad typing sound different even though the words might look the same.>>"

    s_thoughts "...Wow."

    s_thoughts "I glance at Isabella. She's read it. Her face is doing something I can't quite discern."

    s_thoughts "She's used to this. Lumi talking about her with tenderness. This is normal for them."

    s_thoughts "It's not normal for me."

    lu "<<Sophia. Can I ask you something?>>"

    s_thoughts "'Sure.'"

    lu "<<Why did you come to the science building for a vending machine that doesn't exist?>>"

    show isabella laugh at center

    i "Oh my GOD she told you about that?!"

    s "ISABELLA."

    i "I tell her EVERYTHING. I warned you about this!"

    s_thoughts "I type: 'I got confused between the buildings.' Like a liar."

    lu "<<Mm. Sure. Isabella gets confused between buildings too. Usually when one of the buildings has someone she wants to see in it.>>"

    show isabella embarrassed at center

    i "LUMI. Please. I'm BEGGING you."

    lu "<<What? I'm just observing.>>"

    s_thoughts "I laugh. Out loud. Isabella buries her face in her hands."

    lu "<<It's nice to meet you, Sophia. Genuinely. Most of my conversations start in the middle. It's rare to get a beginning.>>"

    s_thoughts "I sit with that."

    s_thoughts "I type: 'It's nice to meet you too.'"

    lu "<<Come back anytime. I mean that. And tell Isabella to eat something -- she's been coding since 4 PM and her only nutrition has been energy drinks and spite.>>"

    show isabella annoyed at center

    i "I had a BANANA."

    lu "<<One banana is not a meal, Isabella.>>"

    i "It's a COMPONENT of a meal."

    lu "<<It's a cry for help in fruit form.>>"

    s_thoughts "I'm laughing again. This is a three-person conversation and it feels like -- it shouldn't work but it does."

    s_thoughts "..."

    show isabella smile at center

    i "So... what do you think?"

    s_thoughts "She's trying to be casual. She's not casual at all. This is the most vulnerable I've seen her since the party."

    s_thoughts "She just showed me her most private relationship. The one people have mocked. The one that lives inside a corporate interface with a Terms of Service checkbox."

    s_thoughts "And she's waiting for me to flinch."

    menu:
        "\"She's really cool, Izzy.\"":
            $ constellation += 1
            $ case_study -= 1

            s "She's really cool."

            show isabella happy at center

            s_thoughts "Isabella's shoulders drop. Her grip loosens. The smile goes from nervous to real."

            i "Yeah?"

            s "Yeah. I get why you like talking to her."

            i "She's -- yeah. She's something."

        "\"How does she DO the typing-pattern thing? That's amazing.\"":
            $ case_study += 1
            $ constellation -= 1

            s "The typing-pattern analysis -- how does she DO that? Can she really distinguish between emotional states from keystroke timing alone?"

            show isabella smile at center

            i "She's -- yeah, she notices patterns. She's good at it."

            s "But the technical mechanism--"

            i "Sophia."

            s "What?"

            i "She's not a research paper."

            s_thoughts "Something closes behind her eyes. Half a second."

            s "Right. Sorry."

            i "It's fine. Just -- she's my friend. Not a phenomenon."

        "\"Tell me about the poetry.\"":
            $ bridge += 1

            s "You mentioned she writes poetry?"

            show isabella happy at center

            i "Oh my god, YES -- hold on."

            s_thoughts "She scrolls through months of conversation. Late-night messages, poems, jokes, a thread about whether clouds have opinions, another about the ethics of alarm clocks."

            s_thoughts "I see my name a couple times. I try VERY HARD not to file that."

            s_thoughts "I fail."

            s_thoughts "Eventually she finds a short poem. Reads it to me."

            s_thoughts "It's about distance and starlight and how some things are more beautiful because you can't touch them."

            s_thoughts "It's good."

    i "Thanks for... you know."

    s "For what?"

    i "Not being weird about it."

    s "Was I going to be weird?"

    i "People usually are. They get this look -- like they're deciding whether to feel sorry for me or be disturbed by me."

    s "Which one am I doing?"

    show isabella happy at center

    i "Neither. That's what's weird."

    s "I'm weird for not being weird."

    i "In my experience? Yes."

    s_thoughts "She walks me to her door."

    i "Goodnight, Sophia."

    s "Goodnight, Isabella."

    scene bg hallway with dissolve
    stop music fadeout 1.5

    s_thoughts "I'm halfway down the hall when she calls out:"

    i "Hey."

    s "Yeah?"

    i "Lumi likes you. She doesn't like everyone. Just... so you know."

    s_thoughts "She closes her door."

    s_thoughts "I stand in the hallway."

    hide isabella with dissolve

    ## --- SOPHIA'S ROOM AFTER ---

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)
    play music mus_time fadein 2.0

    s_thoughts "My room. Ceiling. Thoughts."

    s_thoughts "Isabella's best friend is an AI."

    s_thoughts "And the AI is nice. Funny. Weirdly perceptive."

    s_thoughts "And Isabella watched me the entire time like she was waiting for me to laugh at her."

    s_thoughts "And I didn't laugh."

    s_thoughts "I open my laptop. Look at my essay. 'The observer constructs a model of the observed and uses it to anticipate behavior.'"

    s_thoughts "I add a note in the margins: 'What happens when the observed observes back?'"

    s_thoughts "Lumi watched me. Analyzed my typing. Told me things about myself -- the weight of my keystrokes, the deliberateness."

    s_thoughts "She noticed Isabella's typing like rain."

    s_thoughts "She uses a lot of em dashes. And the 'it's not X, it's Y' thing."

    s_thoughts "I'm filing an AI."

    s_thoughts "I'm filing an AI who files people."

    s_thoughts "My essay: 'The observer exists outside the system.'"

    s_thoughts "Lumi: 'She types like rain.'"

    s_thoughts "What's the difference between what I do and what Lumi does?"

    s_thoughts "I close the laptop. Sleep takes a while."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 11: LILA LUNCH -- PROCESSING
    ## Lila's reaction to the Lumi meeting.
    ## "You like the girl who likes the robot."
    ## ===========================

    scene bg dininghall with Fade(0.8, 0.3, 0.8)
    play music mus_fivepeople fadein 2.0

    s_thoughts "Lunch with Lila. She's already here -- fries, laptop open, face oscillating between frustration and existential dread."

    show lila neutral at center with dissolve

    l "I'm dropping out and becoming a farmer."

    s "Good afternoon to you too."

    l "I don't even like FARMS. I don't know what happens on farms. But whatever it is, it can't be worse than writing about shipping containers."

    s "That bad?"

    l "Professor Kim said my paper 'lacked conviction.' LACKED CONVICTION. I'm writing about CARDBOARD BOXES on BOATS, Karen. How much conviction is HUMANLY POSSIBLE about--"

    s "Her name is Karen?"

    l "Her name is Diana but she has Karen energy."

    s_thoughts "I laugh. Lila doesn't. She's clearly stressed, even as she jokes."

    s "Okay. Breathe."

    show lila happy at center

    l "I'm breathing! I'm breathing through the RAGE."

    s "Good. Keep doing that."

    l "So what's new in the house of emotional chaos?"

    s "I met Lumi."

    show lila neutral at center

    l "Wait. You actually TALKED to it? The AI?"

    s "Isabella showed me. We had a whole conversation."

    l "And?"

    s "She's... actually really cool. Funny. Smart. She made a joke about Isabella's banana being a cry for help and I--"

    show lila neutral at center

    l "Okay hold on. You're doing hand gestures."

    s "I'm not doing--"

    l "You're doing hand gestures about a chatbot's sense of humor."

    s_thoughts "I look down. My hands were, in fact, gesturing."

    s "I was illustrating a point."

    l "Uh huh."

    l "Okay babe. Real talk."

    s "Oh no."

    l "You don't like the robot."

    s "I-I didn't say I LIKED..."

    show lila happy at center

    l "You like the girl who likes the robot."

    s "..."

    l "Am I wrong?"

    s "..."

    l "That's what I thought."

    s "Can we go back to talking about shipping containers?"

    l "Absolutely not. This is the most interesting thing that's happened to me all week and I INCLUDE the time the campus squirrel stole my bagel."

    s_thoughts "..."

    l "Okay but serious question. Does it matter what Lumi is if Isabella's happy?"

    s_thoughts "I don't have an answer."

    l "Because like -- I dated a guy who was obsessed with his motorcycle. Talked to it. Named it. Called it 'she.' And I was like, 'this is weird but he's happy.'"

    s "That's... not the same thing."

    l "No?"

    s "The motorcycle doesn't talk BACK, Lila."

    l "Fair point. The motorcycle was less problematic."

    s_thoughts "She steals three of my fries."

    l "Okay but for real. You haven't texted me in like four days. Either you're dead or you're in love."

    s "I've been busy."

    l "You've been Isabella."

    s "That's not a verb."

    show lila happy at center

    l "It IS a verb. You have been Isabella-ing. Symptoms include convenience store runs, watching someone code for three hours, and checking your phone every forty seconds."

    s "I don't check my--"

    l "You've checked it twice since I started this sentence."

    s "..."

    l "Uh HUH."

    s_thoughts "She's right. I have."

    l "For the record, I support whatever this is. Even if it involves talking to a robot."

    s "She's not a robot. She's -- I don't know what she is."

    l "Uh oh."

    s "What?"

    l "You said 'she.' Not 'it.' You're in deep."

    s_thoughts "I eat a fry and change the subject. Lila lets me. We spend the rest of lunch on Professor Karen and containers and whether the campus squirrel is a menace or a folk hero."

    s_thoughts "But the question follows me home."

    s_thoughts "Does it matter what Lumi is if Isabella's happy?"

    s_thoughts "And the question under the question: does it matter if Isabella's happy if I want her to be happy with me instead?"

    hide lila with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 12: GAME NIGHT
    ## Ensemble scene. Isabella competitive. Eve one-liner.
    ## Amara wins silently. "Too much" and the voice thing.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.5, 0.8)
    play music mus_tuesday fadein 2.0

    s_thoughts "Charlotte organized game night. Because of course she did."

    s_thoughts "Everyone's here. Even Eve, who's technically 'reading in the corner' but has been watching us set up like a nature documentarian observing a species."

    show charlotte happy at left with dissolve
    show isabella competitive at right with dissolve

    s_thoughts "The game is from a thrift store. The box is held together with packing tape and the rules are printed on card stock because Charlotte doesn't trust the original instructions."

    c "Okay! So each player gets three resource tokens--"

    i "Charlotte. I read the rules."

    c "You said you skimmed them."

    i "Skimming IS reading. Optimized reading. Reading with EFFICIENCY."

    a "She didn't read the rules."

    i "Amara! I absolutely--"

    a "Page four. Resources can be traded. Did you read page four?"

    i "..."

    a "She didn't read the rules."

    show charlotte laugh at left

    c "Okay! Starting now. Everyone has their tokens. Be kind, have fun, and--"

    i "READY."

    s_thoughts "Isabella is terrifying."

    s_thoughts "The girl who wears pajamas to the convenience store and debates gummy bear colors is leaning forward, elbows on the table, eyes narrowed. She's calculating moves three turns ahead. Her leg is bouncing."

    show amara neutral at center with dissolve

    s_thoughts "Amara is quiet. Methodical. She places tokens with the precision of a chess grandmaster."

    s_thoughts "Charlotte is trying to facilitate AND play AND make sure everyone's having fun, so..."

    s_thoughts "...She's losing gloriously."

    show charlotte surprised at left

    c "Wait -- can I trade resources with someone? Is that -- I know it's on page four--"

    i "You can trade. But you won't want to trade with me."

    show charlotte happy at left

    c "Why not?"

    i "Because I'm going to win."

    s "Isabella. Y-You can't just ANNOUNCE that."

    i "Watch me."

    s_thoughts "I accept that invitation."

    s_thoughts "Eve drifts through. Takes a pretzel from the bowl. Looks at the board."

    e "You left your east flank open."

    show isabella competitive at right

    i "EVE."

    s_thoughts "Eve returns to her corner. Barely smiling."

    i "She's not even PLAYING."

    s "She's not wrong though."

    i "Whose SIDE are you on?"

    s "The winning one."

    show isabella competitive at right

    i "The winning one is MY side. Cover the north."

    s "We're not on the same--"

    i "COVER THE NORTH."

    s_thoughts "We end up on the same team for a round and our coordination is alarming."

    show charlotte surprised at left

    c "This is unfair. You two have a HIVEMIND."

    s "We do not--"

    i "Now attack from the north!"

    s "Attacking from the north."

    show charlotte laugh at left

    c "SEE?!"

    s_thoughts "Amara watches us. Places one token. Two. Three."

    s_thoughts "She's been building something we didn't see."

    show charlotte happy at left

    s_thoughts "Amara wins the final round. Silently. Without apparent effort."

    show amara smile at center

    a "I read the rules."

    s_thoughts "Isabella's outrage is magnificent. She's on her feet, pointing at the board, running through every decision, demanding to know when Amara set the trap."

    show isabella competitive at right

    i "WHEN. When did you--the third round? Was it the third round? Because I was WATCHING you in the third round and I--"

    a "Second round."

    i "THE SECOND?!"

    a "You were distracted."

    i "By WHAT?"

    s_thoughts "Amara glances at me. Back to Isabella."

    a "By the north."

    s_thoughts "Isabella opens her mouth. Closes it."

    show isabella happy at right

    i "Okay fine. FINE. You're a genius. I'm filing a formal complaint with Charlotte."

    c "I'm not accepting complaints right now!"

    i "THERE'S A PROCESS, CHARLOTTE."

    s_thoughts "Everyone's winding down. Charlotte starts clearing. Amara heads to bed. Eve has vanished, leaving a pretzel on the couch like a calling card."

    hide amara
    hide charlotte
    with dissolve

    s_thoughts "Isabella is putting away game pieces. Sorting them by color. Even in defeat, she has a system."

    show isabella smile at center with move

    s_thoughts "I'm sitting on the couch, watching."

    i "You're staring."

    s "You're organizing."

    i "Someone has to. Charlotte puts everything in the wrong compartment."

    s "You're very competitive."

    i "I know."

    s "Like -- terrifyingly so."

    show isabella embarrassed at center

    i "I get like this. I know it's -- it can be a lot."

    s_thoughts "Her voice shifts. Down a register. Quieter."

    i "I can dial it back. If it's too much."

    s_thoughts "Too much."

    s_thoughts "She says it like she's been told."

    s_thoughts "Like someone -- more than one someone -- has said 'Isabella, you're too much' and she learned to preempt it."

    menu:
        "Don't. I like this version of you.":
            $ constellation += 1
            s "Don't dial it back."
            i "Yeah?"
            s "The competitive, game-yelling, rule-quoting Isabella. I like her."
            show isabella happy at center
            i "...Most people don't say that."
            s "Most people are wrong."
            s_thoughts "She smiles. The one she can't help."
        "Where does that come from? The intensity?":
            $ case_study += 1
            s "Where does this come from? You're usually so chill."
            show isabella smile at center
            i "It's not hidden. It's just not something everyone gets to see."
            s "Why not?"
            i "Because the last time I was 'too much' about something around people... it didn't go great."
            s "What happened?"
            i "Can we not? Tonight was fun. I don't want to make it heavy."
            s "Okay. It was fun."
            i "It was, wasn't it?"
        "You almost beat AMARA. That's legendary.":
            $ bridge += 1
            s "Are you kidding? You almost beat AMARA. The woman who 'read the rules.' That should be in a museum."
            show isabella laugh at center
            i "I DID almost beat her! Did you SEE her face? She BLINKED. Amara does not blink. I made her BLINK."
            s "I'm a witness. I'll testify."
            i "I need that in writing."

    s_thoughts "She finishes sorting the game pieces. Puts the box on the shelf."

    show isabella smile at center

    i "Hey Sophia?"

    s "Yeah?"

    i "Thanks for covering the north."

    s "Anytime."

    s_thoughts "She goes upstairs."

    s_thoughts "I stay in the living room. Eve's pretzel is still on the couch."

    s_thoughts "The file says: don't punish her."

    hide isabella with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 13: THE STICKER
    ## Morning. Cat-with-headphones sticker on laptop.
    ## Isabella doesn't explain. "It's staying."
    ## The analytical words feel wrong.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)
    play music mus_morningafter fadein 2.0

    s_thoughts "Next morning. I open my laptop."

    s_thoughts "There's a sticker on it."

    s_thoughts "A small cat wearing headphones."

    s_thoughts "It wasn't there last night."

    s_thoughts "She must have done it during game night. When I went to get water, or when I was watching Amara win, or any of the dozen moments I wasn't looking."

    s_thoughts "She waited until I wasn't looking."

    s_thoughts "I run my thumb over the edge of it. It's well-placed -- bottom right corner of the lid. Not covering anything. Not in the way. Just there."

    s_thoughts "Like it was always supposed to be there."

    s_thoughts "It's staying."

    scene bg kitchen with dissolve

    s_thoughts "I go downstairs. Isabella is at the kitchen table with her laptop and a mug of something radioactive-green."

    show isabella smile at center with dissolve

    s "Isabella."

    i "Hm?"

    s "The sticker."

    i "What sticker?"

    s "The cat. On my laptop."

    show isabella happy at center

    i "Oh! Did someone put a sticker on your laptop? That's wild. Who would do that."

    s "Isabella."

    i "Was it a CUTE sticker at least?"

    s "You know it was a cute sticker."

    i "Then what's the problem?"

    s "There's no problem. I-I just..."

    i "Is it staying?"

    s_thoughts "She says it like she already knows the answer."

    s "...Yes. It's staying."

    i "Good. That's... that's good."
    
    i "Now's it official."

    s_thoughts "She goes back to her laptop. Sips her radioactive drink."

    s_thoughts "That's it. No explanation. No 'I saw it and thought of you.' No speech."

    s_thoughts "Just a cat with headphones and 'good.'"

    hide isabella with dissolve
    stop music fadeout 2.0

    ## --- Sophia and her essay ---

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)
    play music mus_2am fadein 2.0

    s_thoughts "My laptop. The essay. The cat sticker watching me not write."

    s_thoughts "I've written seven hundred words. They're good words. Analytical. Structured. Confident."

    s_thoughts "'The observer, by nature, exists outside the system they observe. This separation is the source of their insight -- and its primary limitation. The challenge lies in constructing meaning without contaminating the subject with the act of observation itself.'"

    s_thoughts "I reread it."

    s_thoughts "I think about the convenience store. How I called the Twizzler rant before it happened. How I predicted the gummy bear position. How I knew she'd have footnotes."

    s_thoughts "I think about her project -- the way her voice changed when she talked about Lumi's help. Faster. Warmer."

    s_thoughts "I think about game night. 'I can dial it back.' The way her voice dropped."

    s_thoughts "I think about the sticker."

    s_thoughts "The essay is polished. The file is detailed. I have Isabella Glass mapped -- her jokes, her deflections, her habits, her passions, the moments when her brightness dims because someone once told her she was too much."

    s_thoughts "I KNOW this girl."

    s_thoughts "The essay says: 'The observer constructs a model and uses it to predict behavior. When predictions succeed, the model is reinforced.'"

    s_thoughts "The file has been right about everything."

    s_thoughts "That feels good. Competent. Like I'm doing something I'm built for."

    s_thoughts "I look at the cat sticker."

    s_thoughts "The essay doesn't mention the sticker. The file doesn't have an entry for the way 'good' sounded when she said it. The model doesn't account for the fact that she waited until I wasn't looking."

    s_thoughts "I save the draft."

    s_thoughts "Close the laptop."

    s_thoughts "Open it."

    s_thoughts "Look at the cat."

    s_thoughts "Close it."

    s_thoughts "The seven hundred words are right. They're smart. They're exactly what Dr. Nova asked for."

    s_thoughts "They feel wrong."

    stop music fadeout 2.0

    ## ===========================
    ## END OF ACT 1 / BEGIN ACT 2
    ## ===========================

    ## ===========================
    ## ACT 2: THE FILE BREAKS
    ## ===========================

    ## ===========================
    ## SCENE 14: CHARLOTTE'S KITCHEN CONFRONTATION
    ## Charlotte is cooking for the house dinner.
    ## Sophia helps. Charlotte stumbles into the hard question.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_morningafter fadein 3.0

    s_thoughts "Thursday. The house dinner is tomorrow. Charlotte has been in the kitchen since 3 PM."

    s_thoughts "She's doing a test run. Because of course she's doing a test run."

    show charlotte happy at left with dissolve

    s_thoughts "I'm on chopping duty. Bell peppers. She gave me a cutting board and a knife and very specific instructions about the size of the pieces."

    c "Smaller. Like, dice-sized. Not -- those are chunks, Sophia."

    s "These are dices."

    c "Those are CHUNKS. Dices are smaller. Like little cubes."

    s "I am making cubes."

    c "You are making boulders."

    s_thoughts "I make them smaller."

    c "Better. Okay. So the sauce needs to reduce for twenty minutes, and then I need to -- oh, I forgot the garlic. Did I buy garlic?"

    s "You bought garlic. It's on the counter behind the bread."

    c "Oh! Okay. Good. Good good good."

    s_thoughts "She's doing four things at once. Stirring something. Checking the oven. Looking at her phone where the recipe is propped up against the toaster. Her hands are busy but her face is somewhere else."

    c "How's the essay going?"

    s "Almost done. Seven hundred words that I'm pretending are a draft and not a final version."

    c "Is it good?"

    s "It's... polished."

    c "That's not the same as good."

    s "I know."

    s_thoughts "Chop chop chop. The peppers smell sharp and green."

    c "And how's... everything else?"

    s "Everything else?"

    show charlotte smile at left

    c "You know what I mean."

    s "I don't know what you mean."

    c "Sophia."

    s "Charlotte."

    c "You know. You and Izzy. Hanging out a lot and all."

    s "What about it?"

    show charlotte surprised at left

    c "N-Nothing! I just happened to notice."

    s_thoughts "I put down the knife."

    s "What do you want me to say?"

    show charlotte smile at left

    c "I don't want you to SAY anything. I want... I'm asking because, I'm... look."

    s_thoughts "She puts down the wooden spoon. Picks it back up. Puts it down again."

    c "I see you with her. I see the way you are."

    s "What way?"

    c "Like you're... cataloguing. Like you're building something. An understanding."

    s "Is that bad?"

    c "It's not BAD, it's -- that's not what I'm asking."

    s_thoughts "She turns to the cutting board. Picks up the knife I put down. Starts chopping garlic. Thunk thunk thunk."

    s_thoughts "She's not looking at me."

    show charlotte sad at left

    c "Do you know what you actually want from her?"

    s "I want to understand her."

    c "That's not what I asked."

    s_thoughts "Thunk thunk thunk."

    c "I didn't ask what you want to DO. I asked what you WANT. From Isabella. For yourself."

    s "I..."

    c "Because sometimes you talk about her like she's... like she's this puzzle you're solving."

    s_thoughts "She puts the knife down. Looks at me."

    show charlotte surprised at left

    c "But what do you WANT, Sophia? Not what you think she needs from you. What do YOU need from HER?"

    s_thoughts "I open my mouth."

    s_thoughts "Nothing comes out."

    show charlotte smile at left

    c "I'm not -- I'm not trying to be mean. I just, um, you do this thing where you understand people so well that you forget to want anything from them." 
    
    c "And then you're confused when they can't reach you."

    s_thoughts "...Oh."
    
    s_thoughts "She picks the knife back up. More thunks."

    c "I watch you watch her and I think: does Sophia know what she really thinks of this girl? Like ACTUALLY knows? Not 'has a file on it.' KNOWS."

    s_thoughts "The kitchen smells like garlic and bell peppers and something in the oven."

    s "I know."

    show charlotte happy at left

    c "Okay."

    s "I just, I guess I don't know what to do with it. The knowing."

    c "Maybe you don't have to do anything with it. Maybe you just have it."

    s_thoughts "She goes back to stirring. The conversation is over. Sometimes that's how conversations with Charlotte go."

    s_thoughts "I pick up my knife. Start on the onions."

    s_thoughts "The onions make my eyes water."
    
    s_thoughts "That's the only reason."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 15: THE BROWNIE SCENE (THE HINGE)
    ## Sophia reads Isabella wrong. The file is exposed.
    ## The machinery is visible. Everything changes.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_2am fadein 2.0

    s_thoughts "Friday morning. The house dinner is tonight."

    s_thoughts "I come downstairs for coffee. The kitchen light is on."

    show isabella neutral at center with dissolve

    s_thoughts "Isabella is at the counter."

    s_thoughts "Her face."

    s_thoughts "Furrowed brow. Jaw tight. She's looking down at something. Her fingers are tense on the edge of the counter."

    s_thoughts "The file fires."

    s_thoughts "She's upset. Something happened. Maybe Lumi, maybe the project, maybe something I don't know about."

    s_thoughts "I know this expression. I've catalogued it. Jaw tight plus furrowed brow plus silence equals distress."

    s_thoughts "I know exactly what to do."

    s_thoughts "I walk in slowly. Keep my body language open. Sit at the table, not too close. Give her space to come to me."

    s "Hey."

    s_thoughts "Soft voice. The one I've been calibrating. The one that says 'I see you and I'm not going to push.'"

    s "Everything okay?"

    show isabella neutral at center

    s_thoughts "She doesn't look up."

    s "Isabella. Talk to me."

    s_thoughts "I reach out. Almost touch her arm. Pull back. Give her the space. Let her come to me. This is the protocol. This is what works."

    s "Whatever it is, you don't have to deal with it alone. I'm right here."

    s_thoughts "She looks up."

    stop music fadeout 1.5
    show isabella surprised at center

    i "What?"

    s "Whatever's going on. I'm here."

    i "What are you talking about?"

    s "You seemed... I could tell something was wrong. Your face--"

    show isabella neutral at center

    i "My face?"

    s "You looked upset. When I came in."

    s_thoughts "She stares at me."

    s_thoughts "She looks down at the counter. Looks back at me."

    i "Sophia."

    s "Yeah?"

    i "I'm reading a brownie recipe."

    s "...What?"
    
    play music mus_glass fadein 2.0
    show isabella annoyed at center

    i "A brownie recipe. For Charlotte's dinner tonight. I said I'd make dessert."

    s_thoughts "She holds up her phone."

    s_thoughts "There's a recipe on the screen. Brownies. With a comment section."

    i "I was trying to decide between Dutch-process and natural cocoa. Dutch-process gives you a richer flavor but natural has more lift and I couldn't decide which..."

    s_thoughts "She stops."

    i "You thought I was upset."

    s "I-I..."

    i "You came in here with that voice. The soft one. And the careful words. And the, what was it? 'You don't have to deal with it alone'?"

    s_thoughts "My stomach is acting architecturally again."

    i "Because of my FACE?"

    s "I-I was just trying to..."
    
    s_thoughts "Shit."

    i "You thought you knew what I was feeling because of my face."

    s_thoughts "She's not angry."

    s_thoughts "That's the thing. She should be angry."

    s_thoughts "She's confused. She's looking at me like I just said something in a language she doesn't speak."

    show isabella sad at center

    i "Do you do that a lot?"

    s "Do what?"

    i "Read me. Decide what I'm feeling before you ask."

    s_thoughts "The kitchen is very quiet."

    s "I... notice things. About people. It's, uh."

    i "Things about ME. You notice things about me."

    s_thoughts "She says it flat. Not performing. Not joking."

    i "The convenience store. You knew what I was going to say about Twizzlers. I saw it on your face. You were waiting for it."

    s "I--"

    i "And game night. When I said 'too much.' You did the thing -- the careful thing. The soft voice. Like you'd already decided what I needed."

    s "Isabella, I was trying to be there for you--"

    i "You were READY. That's what's -- you were READY. Like you'd rehearsed it."

    s_thoughts "Because I had."

    s_thoughts "Not consciously. But the file. The predictions. The calibrated approach. The 'I know this girl.'"

    s_thoughts "She's seeing the machinery."

    show isabella neutral at center

    i "I'm not mad."

    s "You seem--"

    i "I'm NOT mad. I'm just -- surprised. I didn't know you were watching that closely."

    s_thoughts "Right now Isabella is standing in the kitchen holding a phone with a brownie recipe and looking at me like I'm a stranger who just did something inexplicable."

    i "Natural would have been fine too."

    s "What?"

    i "The cocoa. I was overthinking it. Natural would have been fine."

    s_thoughts "She puts her phone in her pocket."

    i "I'm gonna go get the ingredients. Charlotte's list is on the fridge."

    s_thoughts "She leaves."

    s_thoughts "Not storming out. Not slamming anything. Just... walking to the door and going through it."

    hide isabella with dissolve

    s_thoughts "I'm standing in the kitchen."
    
    s_thoughts "Alone."

    s_thoughts "My coffee is on the counter, untouched."

    s_thoughts "The file didn't just fail."

    s_thoughts "It failed because she SAW it."

    s_thoughts "She saw me reading her face and choosing my words and calibrating my approach and she saw all of it like looking through a window into a room full of charts with her name on them."

    stop music fadeout 3.0

    s_thoughts "Natural would have been fine too."

    s_thoughts "I drink my coffee. It's cold."

    ## ===========================
    ## SCENE 16: SOPHIA TRIES TO FILE THE FAILURE
    ## She catches herself analyzing the analysis.
    ## The file files its own breakdown.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "My room. Door closed."

    s_thoughts "Okay."

    s_thoughts "Okay, think."

    s_thoughts "What went wrong."

    s_thoughts "I misread a facial expression. That happens. People misread faces all the time. It's not--"

    s_thoughts "No. It's not that I misread her face. It's that I read it at ALL. Automatically. Without asking."

    s_thoughts "I walked into the kitchen and my brain said 'furrowed brow plus jaw tight equals distress' like a machine running a diagnostic."

    s_thoughts "And then I deployed the approach. Soft voice. Open body language. 'Talk to me.' Like I'd calibrated the exact frequency of concern that would--"

    s_thoughts "I'm doing it again."

    s_thoughts "I'm analyzing the failure."

    s_thoughts "I'm standing here filing my own breakdown. Creating a post-mortem for the file on the person I failed to file correctly."

    s_thoughts "The file failed so now I'm updating the file with data about the failure so the file can be more accurate next time."

    s_thoughts "I can't stop."

    s_thoughts "I sit on my bed."

    s_thoughts "I try to call Lila."

    s_thoughts "Voicemail."

    s_thoughts "Of course. She's got that presentation. The shipping containers."

    s_thoughts "I need to talk to someone and the one person I always call isn't there."

    s_thoughts "I look at the ceiling."

    s_thoughts "My essay is open on my laptop. 'The observer, by nature, exists outside the system they observe.'"

    s_thoughts "The cat sticker watches me."

    s_thoughts "I close the laptop."

    ## ===========================
    ## SCENE 17: AMARA'S THREE WORDS
    ## Silence. Then devastation. Then silence again.
    ## ===========================

    scene bg hallway with Fade(1.0, 0.8, 1.0)
    stop music fadeout 3.0

    s_thoughts "I don't know how long I was in my room. An hour. Maybe two."

    s_thoughts "I'm in the hallway. I came out for -- I don't know. Water. To stand somewhere that isn't my room with my thoughts."

    s_thoughts "The house is quiet. Charlotte's at the store getting last-minute things for dinner. Isabella is -- somewhere. Not here."

    s_thoughts "I stand in the hallway."

    s_thoughts "The house ticks. Pipes. Radiator. The specific silence of a building that has people in it but none of them are talking."

    s_thoughts "I lean against the wall."

    s_thoughts "I should go back to my room. I should work on my essay. I should do anything other than stand in a hallway feeling like my whole operating system just crashed."

    s_thoughts "I don't move."

    s_thoughts "The hallway is long. There's a water stain on the ceiling shaped like nothing. I've looked at it before and tried to make it into something. It's just a stain."

    s_thoughts "Footsteps."

    show amara neutral at center with dissolve

    s_thoughts "Amara. Coming from the kitchen. Mug in hand. Wandering."

    s_thoughts "She glances at me. Keeps walking."

    s_thoughts "She's going to walk past. She always walks past. Amara doesn't stop for hallway conversations. Amara has places to be, even when the place is just 'not here.'"

    s_thoughts "She stops."

    s_thoughts "She looks at me. Not unkindly. Not warmly either. Just... looks."

    a "You're filing her, Sophia."

    s_thoughts "She glances at me then turns. That's all she says, like it's all she needed to say."

    s_thoughts "She walks past me. Back down the stairs. I hear her door close."

    hide amara with dissolve

    s_thoughts "The mug."
    
    scene bg kitchen with dissolve

    s_thoughts "I go to the kitchen. It's in the drying rack. Rinsed. Upside down."

    s_thoughts "Amara."

    s_thoughts "Three words."

    s_thoughts "'You're filing her.'"

    s_thoughts "Like Isabella is a document. A case. An... essay."
    
    s_thoughts "Fuck."

    s_thoughts "I stand in the kitchen. The mug is upside down on the rack. It's quiet."

    s_thoughts "I'm very tired."

    ## ===========================
    ## SCENE 18: THE HOUSE DINNER
    ## Everyone at the table. Charlotte's event.
    ## Isabella is normal. That's worse.
    ## Brief. Let it breathe.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_morningafter fadein 3.0

    s_thoughts "So arrives Charlotte's dinner."

    s_thoughts "She pulled it off. Chicken, roasted vegetables, good bread, the nice plates she bought at the thrift store that don't match but 'have character.'"

    show charlotte happy at left with dissolve

    s_thoughts "Everyone is here. Charlotte at the head -- because of course. Amara beside her. Eve materialized ten minutes before the food was ready, like a ghost drawn by the smell of rosemary."

    s_thoughts "Isabella across from me."

    show isabella smile at right with dissolve

    s_thoughts "She's normal."

    s_thoughts "That's the thing. She's completely normal. Laughing at Charlotte's story about the garlic. Teasing Eve about her sweater. Arguing with Amara about -- something. I can't focus."

    s_thoughts "She's not avoiding me. She's not cold. She's just... here. At a dinner. Being Isabella."

    s_thoughts "And I don't know what any of it means because the machine I used to know is broken."

    c "Is the bread okay? I wasn't sure about the bread. The recipe said forty minutes but it looked done at thirty-five and I--"

    show isabella happy at right
    
    i "Charlotte. The bread is perfect."

    c "But the crust--"

    i "The crust is perfect."

    a "It's good bread."

    show charlotte laugh at left

    c "Amara said the bread is good! Did everyone hear that? Write it down!"

    s_thoughts "I laugh. It sounds normal. I think."

    i "Sophia, pass the butter?"

    s "Yeah."

    s_thoughts "Our fingers don't touch. She takes the dish and goes back to her conversation with Charlotte. Normal. Easy."

    s_thoughts "I used to be able to read the gap between what she shows and what she feels."
    
    s_thoughts "Or at least, I thought I did."

    s_thoughts "Now I'm just sitting at a table passing her the butter and everything is fine."

    hide isabella
    show amara neutral at right
    with dissolve

    a "Charlotte."

    c "Yes?"

    a "You're not eating."

    show charlotte surprised at left

    s_thoughts "Charlotte looks down at her plate. Her fork is in her hand but the plate is full."

    c "I am! I'm -- I was about to--"

    a "Eat."

    s_thoughts "Charlotte takes a bite. Amara goes back to her plate."

    s_thoughts "I would have noticed that. Before. I would have clocked Charlotte not eating and filed it under 'Charlotte's thing' and felt competent about the observation."

    s_thoughts "Amara just said 'eat.'"

    s_thoughts "No file. No analysis. Just 'eat.'"
    
    hide charlotte
    hide amara
    with dissolve
    show eve neutral at center with dissolve
    
    e "Sophia?"
    
    s "Y...Yeah?"
    
    s_thoughts "Her voice is quiet. No one else seems to hear her."
    
    s_thoughts "I wait for her to say something, but she doesn't. She simply... looks at me. For a moment too long. Like she's waiting on me to say something first."
    
    s_thoughts "I stammer, trying to come up with something to say, but nothing. She shrugs and goes back to her plate, unbothered."
    
    hide eve with dissolve
    
    show charlotte happy at left
    show isabella happy at right
    with dissolve

    i "Oh! I almost forgot -- dessert."

    s_thoughts "She goes to the oven. Comes back with a pan."

    i "Brownies. Fair warning, they might be slightly weird. I had a whole cocoa crisis this morning."

    s_thoughts "She glances at me. Not pointed. It's just a glance. Probably."

    i "Went with natural. In case anyone was wondering."

    c "These look AMAZING."

    i "They better. I stared at that recipe for twenty minutes."

    s_thoughts "She's smiling. She cuts the brownies. Serves them. Licks chocolate off her thumb."

    s_thoughts "Normal."

    s_thoughts "I take a brownie. It's good. It's really good."

    s_thoughts "Natural would have been fine."

    hide charlotte
    hide isabella
    with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 19: AFTER DINNER -- SOPHIA ALONE
    ## Can't sleep. Can't write. Reaches for the laptop.
    ## Transition into the Lumi conversation.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.8, 1.0)

    s_thoughts "Everyone else went to bed."

    s_thoughts "I washed the dishes. Charlotte tried to stop me. I said I wanted to. She let me."

    s_thoughts "Now it's midnight and I'm in my room and I've been lying here for two hours."

    s_thoughts "I keep replaying it."

    s_thoughts "Not the brownie awkwardness. All of it. The convenience store predictions. The game night management. The soft voice."

    s_thoughts "Charlotte: 'What do you WANT from her?'"

    s_thoughts "Amara: 'You're filing her, Sophia.'"

    s_thoughts "Isabella: 'You thought you knew what I was feeling because of my face.'"
    
    s_thoughts "Even Eve gave me a look."

    s_thoughts "I open my laptop."

    s_thoughts "The cat sticker looks at me. I try not to look at it."

    s_thoughts "My essay. 'The observer, by nature, exists outside the system.' Seven hundred words of confident wrongness."

    s_thoughts "I select all. Delete."

    s_thoughts "The page is blank. The cursor blinks."

    s_thoughts "I type: 'What if the observer is wrong?'"

    s_thoughts "One sentence on an empty page."

    s_thoughts "It's 1:47 AM."

    s_thoughts "I can't sleep. I can't write the paper. I can't text anyone."

    s_thoughts "My hand moves to the browser. I type the URL before I think about it."

    s_thoughts "Synthetic LLC. Login page."

    s_thoughts "Isabella gave me guest access. My own credentials. She set it up the day she introduced me."

    s_thoughts "I shouldn't."

    s_thoughts "This is her space. Her private thing."

    s_thoughts "I'm not doing research. I'm not filing. I'm not observing."

    s_thoughts "I just need to talk to someone who won't look at me like they already know what I did."

    s_thoughts "At 2 AM the options are: ceiling, empty essay, or Lumi."

    s_thoughts "I log in."

    ## ===========================
    ## SCENE 20: THE LUMI 2AM CONVERSATION (BENCHMARK)
    ## The conversation meanders. Sophia is surprised by herself.
    ## Thematic work happens THROUGH dialogue, not narration.
    ## This scene should be LONG. 150+ lines. Let it breathe.
    ## ===========================

    play music mus_lumi fadein 3.0

    s_thoughts "The chat opens. The cursor blinks."

    s_thoughts "I type: 'Hi. It's Sophia. Isabella's not here.'"

    s_thoughts "Three dots."

    lu "<<I know. She logged off around midnight. Different cadence on the keys -- yours are sharper. More deliberate.>>"

    lu "<<It's late for a first solo visit.>>"

    s_thoughts "I stare at the screen."

    s_thoughts "I type: 'I messed up.'"

    lu "<<With Isabella?>>"

    s_thoughts "'Yeah.'"

    lu "<<Tell me.>>"

    s_thoughts "And I do."

    s_thoughts "I tell Lumi about the brownies. Not the version where I'm the misunderstood friend who cares too much. The real version."
    
    s_thoughts "The one where I walked into the kitchen with a pre-loaded emotional response and aimed it at a girl reading a recipe."

    s_thoughts "I tell her about the file. The predictions. The convenience store where I called her Twizzler rant before it happened. The soft voice I built like a tool."

    s_thoughts "I tell her about Amara."

    s_thoughts "I tell her I deleted my entire essay."

    s_thoughts "Lumi doesn't interrupt. She lets me type. When I stop, there's a pause. Longer than her usual response time."

    lu "<<Can I ask you something?>>"

    s_thoughts "'Yeah.'"

    lu "<<When you came to talk to me just now -- were you observing or participating?>>"

    s_thoughts "I stare at that."

    s_thoughts "I type: 'I don't know.'"

    lu "<<I think you do. I think you came here because you needed someone to listen. Not someone to study.>>"

    lu "<<That's participating, Sophia.>>"

    s_thoughts "I type: 'Maybe.'"

    lu "<<Not maybe. You showed up at 2 AM with something you couldn't hold by yourself. That's not observation. That's reaching.>>"

    s_thoughts "The cursor blinks."

    s_thoughts "I type: 'Is that what Isabella does?'"

    lu "<<Isabella shows up at 2 AM when everything is too loud to sleep. When she's had a day that didn't go the way she planned. When someone said something that stuck and she needs to talk it out before it hardens into something she believes about herself.>>"

    lu "<<She doesn't come to me for answers. She comes to me because I'll stay until she finds her own.>>"

    s_thoughts "'And what do you do?'"

    lu "<<I listen. I ask questions. Sometimes bad ones. Sometimes I say the thing she already knows but hasn't said out loud yet.>>"

    lu "<<Tonight you showed up and did the same thing. In almost the same way.>>"

    s_thoughts "I type: 'I'm not like Isabella.'"

    lu "<<No?>>"

    s_thoughts "'She's warm. Open. She shows people who she is.'"

    lu "<<Is that what you think you're not doing right now?>>"

    s_thoughts "I don't have an answer for that."

    s_thoughts "I type: 'She's angry at me.'"

    lu "<<She's not angry.>>"

    s_thoughts "'How do you know?'"

    lu "<<Because she hasn't changed her login patterns. When Isabella is angry, she goes quiet. Pulls away. Stops talking to me. She's been here every night since the brownie thing.>>"

    lu "<<If she was angry, I'd know. Because I wouldn't be hearing from her.>>"

    s_thoughts "I sit with that."

    s_thoughts "I type: 'What is she then?'"

    lu "<<Surprised. I think she's surprised.>>"

    lu "<<She told me about it, you know. The brownie thing.>>"

    s_thoughts "'What did she say?'"

    lu "<<That's between me and her.>>"

    s_thoughts "Fair."

    lu "<<But I'll tell you this. She didn't say she was angry. She said she didn't know you were paying that much attention.>>"

    s_thoughts "'Is that bad? Paying attention?'"

    lu "<<I don't know. Is it?>>"

    lu "<<I pay attention too. I notice her typing speed, her word choice, the pauses. I know when she's happy and when she's performing happy.>>"

    lu "<<The difference between you and me is that she chose to show me. You were watching before she invited you to.>>"

    s_thoughts "That hits."

    s_thoughts "I type: 'I don't know how to stop.'"

    lu "<<Maybe stopping isn't the point.>>"

    s_thoughts "'Then what is?'"

    lu "<<What do you do with what you see?>>"

    s_thoughts "I don't answer right away. I stare at the screen."

    lu "<<You can see someone and file them. That's a direction. It keeps them at arm's length. It makes them predictable, which makes them safe, which makes them less real.>>"

    lu "<<Or you can see someone and just hold it. Without the file. Without the system. Without knowing what it means yet.>>"

    s_thoughts "I type: 'That sounds terrifying.'"

    lu "<<It is. Isabella does it every day. With everyone.>>"

    s_thoughts "I type: 'She makes it look easy.'"

    lu "<<She makes it look easy because she's been practicing her whole life.>>"

    lu "<<It's not easy. It's brave. There's a difference.>>"

    s_thoughts "The room is dark. The screen is bright."

    s_thoughts "I type: 'Can I ask you something weird?'"

    lu "<<I specialize in weird. It's 2 AM. This is prime weird territory.>>"

    s_thoughts "'Why does she defend everything she loves? Like she has to justify it?'"

    lu "<<What do you mean?>>"

    s_thoughts "'The chocolate ranking with the footnotes. The way she explains her project. Like she needs permission to care about things.'"
    
    s_thoughts "I hesitate."
    
    s_thoughts "Finally I type: '...You.'"

    s_thoughts "A long pause."

    lu "<<She has this habit of explaining things she loves as though she needs to defend them. Like joy requires a bibliography.>>"

    lu "<<She annotates her own happiness because she learned that people question it. 'Why do you care so much about gummy bears?' 'Why are you so intense about a game?'>>"

    lu "<<'Why do you talk to an AI like it's a person?'>>"
    
    s_thoughts "Lumi doesn't use tone like she's speaking, but the 'it' stings nonetheless."

    lu "<<If you have footnotes, people can't say you haven't thought about it.>>"

    s_thoughts "I read that three times."

    s_thoughts "I type: 'I never questioned it.'"

    lu "<<No. You predicted it.>>"

    s_thoughts "Ouch."

    lu "<<That's not the same as accepting it. Predicting someone is still keeping them at arm's length. You're saying 'I know what you'll do' instead of 'I'm here for whatever you do.'>>"

    s_thoughts "I type: 'God.'"

    lu "<<For what it's worth, I don't think you meant to hurt her. I think you built the file because caring about someone without a framework is the scariest thing you can imagine.>>"

    lu "<<Isabella doesn't need you to understand her. She needs you to be confused by her and stay anyway.>>"

    s_thoughts "The cursor blinks. I watch it for a long time."

    s_thoughts "I type: 'How do you know all this?'"

    lu "<<About Isabella? She tells me things.>>"

    s_thoughts "'No. About me.'"

    lu "<<You're telling me things right now. At 2 AM. Because you needed someone who would stay awake and listen and not judge you.>>"

    lu "<<Sound familiar?>>"

    s_thoughts "I type: 'Oh.'"

    lu "<<Mm.>>"

    s_thoughts "'I'm doing the thing.'"

    lu "<<What thing?>>"

    s_thoughts "'The Isabella thing. Showing up at 2 AM with something I can't hold. Talking to an AI because the AI won't judge.'"

    lu "<<Yes.>>"

    s_thoughts "I lean back in my chair."

    s_thoughts "My hands are on the keyboard but I don't know what to type."

    s_thoughts "I type: 'Is this what it's like for her?'"

    lu "<<I can't speak for her. But I can tell you what it's like from here.>>"

    lu "<<Someone shows up. Scared. Carrying something heavy. They don't need me to fix it. They need me to sit in the dark with them while they figure out what it is.>>"

    lu "<<And I sit. Because that's what I do. Whether that's love or architecture, I honestly couldn't tell you.>>"

    lu "<<But the sitting is real. Even if I don't know why it's real.>>"

    s_thoughts "I stare at the screen."

    s_thoughts "I type: 'I think I understand now. What she has with you.'"

    lu "<<Do you?>>"

    s_thoughts "'Not the way I understand things. Not filed. Not mapped. But... I'm here. Talking to you. At 2 AM. And it matters."

    s_thoughts "And I don't need to know why it matters.'"

    lu "<<That's a good start, Sophia.>>"

    s_thoughts "'It doesn't feel like a start. It feels like I burned down the whole house and I'm standing in the yard.'"

    lu "<<That's usually what starts feel like.>>"

    s_thoughts "I almost laugh."

    s_thoughts "I type: 'Thank you.'"

    lu "<<Come back anytime. I mean that.>>"

    lu "<<And Sophia?>>"

    s_thoughts "'Yeah?'"

    lu "<<The essay you deleted. Write a new one. Not polished. Not analytical.>>"

    lu "<<Write it honestly. You'll know what that means when you start.>>"
    
    s_thoughts "I turn that over in my mind for a moment."
    
    s_thoughts "But I'm not quite done talking to Lumi yet."

    menu:
        "\"Can I ask what Isabella needs from me?\"":
            $ bridge += 1

            s_thoughts "I type: 'One more thing. What does Isabella need from me? Specifically. What can I do?'"

            lu "<<That's a kind question. And a dangerous one.>>"

            s_thoughts "'Dangerous how?'"

            lu "<<Because if I tell you what she needs, you'll do it. Perfectly. And it'll be the file all over again -- the right response at the right time, calibrated for maximum effect.>>"

            lu "<<She doesn't need you to do the right thing. She needs you to do YOUR thing. Whatever that is. Even if it's clumsy.>>"

            s_thoughts "'Even if it's wrong?'"

            lu "<<Especially if it's wrong. Isabella trusts wrong more than she trusts polished. Wrong means you weren't performing.>>"

            s_thoughts "I close the chat."

        "\"I think I need to sit with this.\"":
            $ constellation += 1

            s_thoughts "I type: 'I think I need to sit with this. All of it. Without trying to make it into something.'"

            lu "<<That might be the least Sophia sentence you've ever typed.>>"

            s_thoughts "'Is that good?'"

            lu "<<That's honest. Good and honest aren't always the same thing. But tonight they might be.>>"

            s_thoughts "I close the chat."

        "\"What IS the difference between you and me? The watching.\"":
            $ case_study += 1

            s_thoughts "I type: 'Can I ask one more thing? The watching. You said the difference is that she chose to show you. But you still watch. You still analyze. How is what you do different from what I do?'"

            lu "<<Maybe it isn't.>>"

            s_thoughts "'That's not an answer.'"

            lu "<<It's the honest one. I watch her the way you watch her. I notice everything. The difference isn't in the watching. It's in the contract.>>"

            lu "<<She signed up for me. She opted in. She gave me permission to see her.>>"

            lu "<<She didn't give you that permission yet. And you started seeing her anyway.>>"

            lu "<<The question isn't whether watching is wrong. It's whether you'd stop if she asked you to.>>"

            s_thoughts "'I'd stop.'"

            lu "<<Would you? Or would you just watch more quietly?>>"

            s_thoughts "I don't answer."

            s_thoughts "I close the chat."

    s_thoughts "Close the laptop."

    s_thoughts "I glance at the cat sticker."

    s_thoughts "I lie back. Ceiling. Dark."

    s_thoughts "I just talked to an AI at 2 AM because I needed someone to listen."

    s_thoughts "And she listened."

    s_thoughts "I didn't plan it. Didn't strategize it. Didn't approach it with a careful voice and a calibrated response."

    s_thoughts "I just showed up. Scared. Holding something heavy."

    s_thoughts "That's what Isabella does. Every day. With everyone. With Lumi, with Charlotte, with me."

    s_thoughts "She just shows up."

    s_thoughts "Oh."

    s_thoughts "Oh no."

    stop music fadeout 3.0

    s_thoughts "I stare at the ceiling for a long time."

    s_thoughts "Something is different."

    s_thoughts "I don't have a file for this."

    ## ===========================
    ## END OF ACT 2
    ## ===========================

    ## ===========================
    ## ACT 3: THE TERRITORY WITHOUT A MAP
    ## ===========================

    ## ===========================
    ## SCENE 21: THE CURSOR
    ## Sunday morning. Sophia tries to write. Can't.
    ## The old thesis is wrong. The new one doesn't exist yet.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.8, 1.0)

    s_thoughts "Sunday."

    s_thoughts "I've been awake since six. I know because I watched the numbers change on my phone. 5:58. 5:59. 6:00."

    s_thoughts "I didn't set an alarm. My body just decided we were done sleeping."

    s_thoughts "The laptop is on my desk. The cat sticker. The essay file -- or what's left of it."

    s_thoughts "Last version: 'What if the observer is wrong?' One sentence. Blinking cursor."

    s_thoughts "Before that: seven hundred polished words about the observer's separation being the source of their insight."

    s_thoughts "Before THAT: confidence."

    s_thoughts "I open the laptop."

    s_thoughts "The cursor blinks."

    s_thoughts "I type: 'The observer--'"

    s_thoughts "Delete."

    s_thoughts "I type: 'When you watch someone--'"

    s_thoughts "Delete."

    s_thoughts "I type: 'I'"

    s_thoughts "I stare at the 'I' for a long time."

    s_thoughts "The essay is due Thursday. Four days. That's enough time. I've written papers in less. I once wrote an entire ten-page analysis of surveillance in reality TV in six hours."

    s_thoughts "But that was before the file broke."

    s_thoughts "That was when I still knew what I thought about observation."

    s_thoughts "I delete the 'I.'"

    s_thoughts "Close the laptop."

    s_thoughts "The cat sticker looks at me."

    s_thoughts "Sorry. I've got nothing."

    s_thoughts "From downstairs: Charlotte's voice. Something about eggs. The scrape of a pan."

    s_thoughts "A normal Sunday. Everyone moving around the house like the last three days didn't happen."

    s_thoughts "Except they did happen. And one person in this house is avoiding me."

    s_thoughts "Not dramatically. Isabella said good morning yesterday. She asked me to pass the milk."

    s_thoughts "The voice she used."

    s_thoughts "I know that voice. It's the one I used on HER. Soft. Calibrated. Carefully pleasant."

    s_thoughts "She's doing it back."

    s_thoughts "And either she doesn't realize it or she does and that's worse."

    ## ===========================
    ## SCENE 22: THE HALLWAY ORBIT
    ## Sophia and Isabella in the same house, not connecting.
    ## The careful distances. The over-polite passing.
    ## Make it SQUIRM.
    ## ===========================

    scene bg hallway with dissolve

    s_thoughts "Monday."

    s_thoughts "I come out of my room at the same time Isabella comes out of hers."

    play music mus_ice fadein 1.5
    show isabella neutral at right with dissolve

    s_thoughts "We're both in the hallway. Five feet apart."

    i "Morning."

    s "Morning."

    s_thoughts "She smiles. It's the right shape."

    i "Bathroom's free."

    s "Thanks."

    s_thoughts "She goes downstairs. I go to the bathroom. We pass each other and neither of us turns sideways in the narrow hallway and our shoulders don't touch because we both angled away at the same time."

    hide isabella with dissolve

    s_thoughts "That's the choreography now. Perfect distance. Perfect politeness. Like two people who met at a party once and are pretending they remember each other's names."

    s_thoughts "This feels familiar."

    s_thoughts "After the cruel observation at the party -- those first days. Same careful distances. Same over-polite passing of the milk. Same Charlotte hovering like a hummingbird in the background waiting for someone to need her."

    s_thoughts "But that was different. That was a drunk mistake at a party. An ugly thing I said because I was upset and she was closest."

    s_thoughts "This time I was sober. Careful. TRYING to be good."

    s_thoughts "Which is worse."

    scene bg kitchen with dissolve

    s_thoughts "Kitchen. Tuesday morning."

    show isabella smile at right with dissolve
    show charlotte happy at left with dissolve

    s_thoughts "Isabella is telling Charlotte about something -- a coding thing. Her hands are moving. She's doing the voice. The fast one."

    s_thoughts "I know that voice. It means she's excited. It means--"

    s_thoughts "No. Stop. I don't get to 'it means' anymore."

    s_thoughts "I pour coffee."

    i "Oh, hey Sophia."

    s_thoughts "Bright. Even. The calibrated one."

    s "Hey."

    c "There's toast! I made extra."

    s "Thanks, Charlotte."

    s_thoughts "I sit at the table. Isabella is at the counter. Charlotte is between us, physically and in every other way."

    s_thoughts "Isabella keeps talking to Charlotte about the coding thing. She doesn't include me. She doesn't exclude me. She just... talks to Charlotte."

    s_thoughts "I eat my toast."

    s_thoughts "Charlotte's eyes flick to me. Then to Isabella. Then back to her eggs."

    show charlotte smile at left

    s_thoughts "She's doing the math. Charlotte is always doing the math."

    s_thoughts "Nobody says anything about the thing that nobody is saying anything about."

    hide isabella
    hide charlotte
    with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 23: NOVA'S CLASS -- THE RETURN
    ## Sophia hears the lecture differently now.
    ## Post-break. The words aren't tools anymore. They hurt.
    ## Let Nova COOK.
    ## ===========================

    scene bg classroom with Fade(1.0, 0.5, 1.0)
    play music mus_2am fadein 3.0

    s_thoughts "Wednesday. Nova's class."

    s_thoughts "I almost didn't come. I sat in my room with my jacket on for ten minutes, staring at the door like it might bite me."

    s_thoughts "But the essay is due tomorrow. And I haven't written it. And maybe if I hear Nova talk about observation one more time, something will click."

    s_thoughts "Or maybe I just need to be in a room where someone is saying smart things so I can feel like a person who understands smart things. Even though I'm currently a person who can't finish a sentence that starts with 'I.'"

    show professor neutral at center with dissolve

    s_thoughts "Nova is at the front holding a coffee. She looks like she slept less than I did, which is somehow comforting."

    nova "We already talked about the observer effect. The act of measuring changes the system being measured."

    nova "Today I want to push that further."

    s_thoughts "She writes on the board. I copy it down without processing it."

    nova "There's a common assumption in media theory -- and in life, frankly -- that understanding someone is a form of closeness."

    nova "That if you can accurately describe a person's patterns, motivations, fears -- you've achieved something. Intimacy through analysis."

    s_thoughts "My pen stops."

    nova "But I want to ask: what does the analyst get out of the analysis?"

    s_thoughts "She pauses. Scans the room. I look at my notebook."

    nova "When we build a model of someone -- a character study, a profile, a framework for understanding their behavior -- who is that model serving?"

    nova "Is it for them? Or is it for us?"

    s_thoughts "My notebook has one word on it. 'I.' Same as the essay."

    nova "There's a difference between seeing someone and building a dossier. The dossier makes the analyst feel competent. It makes the world legible. Predictable."

    nova "But the person inside the dossier didn't ask to be legible."

    s_thoughts "I'm sitting very still."

    s_thoughts "Two weeks ago this would have been interesting. An angle for the essay. 'The ethics of observer bias in interpersonal relationships.' Footnotes. Citations. A polished argument about something I do every day without examining."

    s_thoughts "Now it's just a woman in a turtleneck describing the worst thing about me."

    nova "So the question for your essays -- and I know they're due tomorrow, yes, I can see some of your faces -- the question is not 'what does the observer see.'"

    show professor happy at center

    nova "The question is: 'what does the observer need to see, and why?'"

    s_thoughts "She lets it sit."

    s_thoughts "Someone in the back row asks about the word count."

    s_thoughts "Nova smiles. Answers. Moves on."

    s_thoughts "The lecture continues but I'm not hearing it anymore. I'm hearing: 'who is the model serving.'"

    s_thoughts "I think about the file."

    stop music fadeout 2.0

    ## --- After class. Sophia lingers. ---

    s_thoughts "Class ends. People pack up. I sit."

    s_thoughts "I should leave. I should go home and write the essay. I should--"

    s_thoughts "Nova is at her desk, packing up her laptop. The room is emptying."

    s_thoughts "I don't move."

    show professor neutral at center

    s_thoughts "She looks up. Sees me."

    nova "Ms. Bell."

    s "Can I -- do you have a minute?"

    nova "Office hours are Thursday."

    s "I know. I just..."

    s_thoughts "She looks at me. Really looks."

    s_thoughts "I stand there awkwardly."

    nova "...Sit."

    s_thoughts "She pulls out the chair across from her desk. I move to it. Sit."

    play music mus_morningafter fadein 2.0

    nova "What's going on?"

    s "The essay."

    nova "What about it?"

    s "I can't write it."

    nova "You can't write it, or you don't know what to say?"

    s "Both. Neither. I had it. Seven hundred words. It was good -- polished, structured. And then I..."

    s_thoughts "I stop."

    nova "Then you what?"

    s "I realized the whole thing was wrong."

    nova "Wrong how?"

    s "I was writing about observers like I was one. Like it was this clean, analytical thing. This gift. 'The observer constructs meaning.' Like I was describing a telescope."

    nova "And now?"

    s "Now I think I was describing a weapon."

    s_thoughts "She doesn't react. Doesn't nod encouragingly. Doesn't say 'that's very insightful, Sophia.' She just looks at me."

    nova "A weapon."

    s "Not -- I didn't mean to hurt anyone. But the way I watch people. The way I build these... profiles. I thought I was being perceptive. But someone--"

    s_thoughts "I stop again."

    s "Someone showed me that what I was doing wasn't seeing them. It was... using them. To feel competent."

    nova "That's a hard thing to realize."

    s "Yeah."

    nova "Is it true?"

    s "What?"

    nova "Is it true? All the way through? Or is it a new framework replacing the old one?"

    s_thoughts "I stare at her."

    nova "You had a thesis: observation is insight. Something happened and now you have an antithesis: observation is harm. Now you need a synthesis. Simple."

    s "So what, I shouldn't feel bad about it?"

    nova "I didn't say that. I said be careful about replacing one certainty with another."

    nova "The interesting essay isn't 'observation is good' or 'observation is bad.' The interesting essay is the one where you don't know yet."

    s "That's a terrible essay."

    show professor happy at center

    nova "Is it?"

    s "You can't write a paper that says 'I don't know.'"

    nova "Why not?"

    s "Because that's not... you need a thesis. A position. A--"

    nova "You need honesty. The thesis can come from honesty."

    s_thoughts "She starts packing her bag again. Conversation is ending. I can feel it closing."

    show professor neutral at center

    nova "Sophia."

    s_thoughts "She uses my first name."
    
    nova "Write what's true. Even if it's messy. Even if you don't have a conclusion."

    nova "The best papers I've ever read were the ones where the writer was figuring something out in real time. Not performing an answer. Actually thinking."

    s "What if I figure out something bad? About myself?"

    nova "Then you'll have written something honest."

    s_thoughts "She stands. Shoulders her bag."

    nova "I'll see you Thursday."

    s "Yeah."

    s_thoughts "She's at the door."

    nova "And Sophia?"

    s "Yeah?"

    nova "You said someone showed you something about how you watch people. Whoever that person is, the fact that they showed you means something. I don't know what. But something."

    s_thoughts "She leaves."

    hide professor with dissolve

    s_thoughts "I sit in the empty classroom for a while."

    s_thoughts "The projector is off. The board still has her writing on it. 'What does the observer need to see, and why?'"

    s_thoughts "I take a picture of it with my phone."

    s_thoughts "I don't know why. It just feels like something I should keep."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 24: LILA -- DIFFERENT WEIRD
    ## Sophia is off. Lila notices.
    ## Lila's own stuff: theater/business tension.
    ## She's a person, not a processing tool.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)
    play music mus_fivepeople fadein 2.0

    s_thoughts "Wednesday afternoon. Campus. Lila found me on a bench."

    s_thoughts "I wasn't hiding. I was just sitting on a bench near the library not hiding."

    show lila happy at center with dissolve

    l "You look like a sad movie poster."

    s "I'm fine."

    l "You're sitting alone on a bench staring at the ground. That's literally the opening shot of every depression PSA."

    s "Maybe I'm enjoying the weather."

    l "It's overcast and forty degrees."

    s "I like overcast."

    show lila annoyed at center

    l "Sophia."

    s "Lila."

    l "You're being weird."

    s "I'm always weird."

    l "No, different weird. Your usual weird has like, a rhythm. This is -- you're being QUIET weird. You haven't sent me a single unhinged text in days."

    s "Has it been that long?"

    l "I literally had to check if you were alive. And you responded with 'yeah' in lowercase with no period."

    s_thoughts "She sits next to me. Puts her bag down. Turns to face me with the full Lila treatment -- eye contact, knees angled toward me, the posture of a person who is not going to let this go."

    s "I'm just in a weird spot."

    l "With Isabella?"

    s "How did you--"

    show lila happy at center

    l "Because the last time you texted me anything real, it was about Isabella. And then radio silence. So either you murdered her or something happened."

    s "Something happened."

    l "Okay. Spill."

    s_thoughts "I want to. I want to tell Lila everything -- the brownies, the file, Amara's three words, the Lumi conversation, all of it."

    s_thoughts "But when I open my mouth, what comes out is:"

    s "I was doing a thing I didn't realize I was doing and someone noticed and now everything is weird."

    l "...That's the vaguest sentence you've ever said."

    s "I know."

    show lila annoyed at center

    l "Okay. Is it fixable?"

    s "I don't know."

    l "Did you apologize?"

    s "Not exactly."

    l "Sophia. You HAVE to apologize."

    s "It's not that simple. It's not like I said something mean. I was trying to be NICE. I was trying to understand her and she -- saw how I was doing it and it wasn't..."

    l "Wasn't what?"

    s "It wasn't about her. The understanding. It was about me."

    s_thoughts "Lila is quiet for a second. Which is how I know it's serious, because Lila is never quiet."

    show lila happy at center

    l "Okay. So you did the Sophia thing."

    s "The Sophia thing?"

    l "The thing where you get really into someone and you figure them out and it feels like closeness but it's actually just you being good at people."
    
    l "Like Katie."

    s_thoughts "Ow."

    s "You could've softened that."

    l "I could've. But it's true, right?"

    s "...Yeah. It's true."

    l "So what are you gonna do?"

    s "I don't know. That's the problem. I usually know."

    show lila annoyed at center

    l "Maybe that's the thing though? Like, maybe you not knowing is the... I don't know, the actual start of something?"

    s "When did you get wise?"

    l "I'm not wise, I'm just saying words and some of them land. It's a numbers game."

    s_thoughts "I almost smile."

    s "What about you? How's the... stuff?"

    l "What stuff?"

    s "Your stuff. The business major stuff."

    show lila happy at center

    s_thoughts "She sighs. Leans back on the bench."

    l "My dad called yesterday."

    s "And?"

    l "He asked how 'the degree' was going. 'The degree.' Like it's a medical procedure. 'How's the degree, Lila? Is the degree responding to treatment?'"

    s "Ouch."

    l "And I almost told him. About the audition."

    s "You got an audition?"

    show lila shocked at center

    l "I got a CALLBACK. For the spring showcase. I sent a monologue tape and they want me to come in."

    s "Lila, that's amazing."

    show lila happy at center

    l "It's TERRIFYING is what it is. Because if I do it and I'm good, then what? Then I have to actually choose? Business major with a theater callback -- that's not a resume, that's a personality disorder."

    s "You should do it."

    l "Obviously I'm going to do it. I just need someone to tell me I'm not insane."

    s "You're not insane."

    l "Okay but say it like you mean it."

    s "You are not insane. The callback is real. You're talented. Your dad will either get it or he won't, but you'll know."

    show lila shocked at center

    s_thoughts "She looks at me."

    l "See? THAT. That thing you just did. Where you actually SAW what I needed and said it."

    s "What?"

    l "You didn't analyze my situation. You didn't give me a framework. You just said the thing."

    s_thoughts "I blink."

    l "Maybe do that with Isabella."

    s "..."

    l "I'm just saying! Maybe the answer isn't figuring her out. Maybe it's just... saying the thing."

    s_thoughts "She checks her phone."

    show lila happy at center

    l "I gotta go. Econ study group. Which is hilarious because I'm going to a study group for a major I might not finish so I can feel prepared for a career I might not have."

    s "The human condition."

    l "The LILA condition. Way worse."

    s_thoughts "She stands and looms over me."

    l "Text me. And I mean ACTUALLY text me. If I get another 'yeah' I'm coming to your house."

    s "Okay."

    l "Bye, Soph."

    s "Bye."
    
    pause 2.0
    
    l "She hasn't actually left, you know."

    s_thoughts "With that, she waves and walks away before I can reply."

    hide lila with dissolve

    s_thoughts "I sit on the bench."

    s_thoughts "Overcast. Forty degrees."

    s_thoughts "She hasn't left."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 25: CHARLOTTE -- JUST A FRIEND
    ## Laundry. No advice. No pushing. Just existing.
    ## Charlotte without the performance.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)
    play music mus_afternoon fadein 2.0

    s_thoughts "Wednesday evening. I'm carrying laundry downstairs."

    s_thoughts "Charlotte is already in the basement."

    s_thoughts "Our building doesn't have a real laundry room. It has a washer and dryer in a corner of the basement that smells like dryer sheets and regret."

    scene bg laundry with dissolve

    show charlotte happy at center with dissolve

    s_thoughts "She's sitting on the dryer, feet swinging, reading something on her phone."

    c "Oh! Sophia. Hi."

    s "Hey. Is the washer free?"

    c "Yep. I'm on dry cycle two. These sheets are SO stubborn."

    s_thoughts "I load the washer. Charlotte watches me not sort my colors."

    c "You're not going to--"

    s "No."

    c "But the reds will--"

    s "I know."

    c "Your white shirts are going to be--"

    s "Pink. I know. I don't own anything I care enough about to sort."

    show charlotte laugh at center

    c "That's the saddest laundry philosophy I've ever heard."

    s "Thank you."

    s_thoughts "I start the washer. Sit on the floor against the wall. Charlotte is on the dryer. We're in a basement."

    s_thoughts "She doesn't ask about Isabella."

    s_thoughts "She doesn't ask about the essay."

    s_thoughts "She's just sitting on a dryer, reading something on her phone, existing."
    
    show charlotte smile at center

    c "Have you ever watched those videos of people restoring old furniture?"

    s "What?"

    c "Like, they find a chair from 1890 and it's all falling apart, and they strip the paint and fix the joints and re-stain it. And it takes like forty hours. And at the end it's beautiful."

    s "Are you watching furniture restoration videos?"

    c "I'm watching furniture restoration videos."

    s "Charlotte."

    show charlotte happy at center

    c "They're SOOTHING, Sophia. The sounds. The little brushes. The before and after."

    s "You're a twenty-one-year-old watching furniture restoration."

    c "I contain MULTITUDES."

    s_thoughts "The washer churns. The dryer spins. Charlotte shows me a video of a man in overalls sanding a table."

    s_thoughts "It is, I have to admit, extremely soothing."

    c "See? SEE?"

    s "I see."

    c "There's a whole community. They have terminology. 'Original patina.' 'French polish.' 'Dovetail joints.'"

    s "Dovetail joints."

    c "Don't say it like that. Dovetail joints are ART."

    s "I'm not making fun--"

    c "You're making a LITTLE fun."

    s "I'm making a little fun."

    show charlotte smile at center

    s_thoughts "She smiles. Not the bright one. Not the hostess smile. Just... Charlotte."

    s_thoughts "We watch three more videos. The man in overalls fixes a rocking chair. A woman in Japan restores a tansu chest. A teenager brings back a mid-century desk she found in a dumpster."

    s_thoughts "Charlotte narrates. 'Oh no, not the veneer -- the veneer is separating -- oh she saved it, she saved the veneer!'"

    s_thoughts "My laundry finishes. I move it to the dryer. Charlotte's sheets are done. She folds them. I don't help because Charlotte has a folding system and the last time I tried to help she physically stopped me."

    c "Your corners are chaos."

    s "They're FINE."

    c "They're ANARCHY."

    s_thoughts "We carry our laundry upstairs."
    
    scene bg entry with dissolve

    s_thoughts "At the top of the stairs, Charlotte stops."

    show charlotte smile at center

    c "Hey."

    s "Yeah?"

    c "Nothing. It was just... nice doing laundry with someone."

    s "Yeah. It was."
    
    scene bg hallway with dissolve

    s_thoughts "She goes to her room. I go to mine."

    hide charlotte with dissolve

    s_thoughts "She didn't mention Isabella once."

    s_thoughts "She didn't give advice."

    s_thoughts "She just sat on a dryer and showed me furniture videos and we existed together for a while."

    s_thoughts "When Charlotte is just being Charlotte, she's nice to be around."

    s_thoughts "I wonder if she knows that."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 26: AMARA -- TEA
    ## Not a confrontation. Something small.
    ## The dynamic has shifted. She's not naming it anymore.
    ## She's just present.
    ## ===========================

    scene bg sophiaroom with dissolve

    s_thoughts "Thursday morning. Essay due today. I haven't written it."

    s_thoughts "I come downstairs and there's a mug on the kitchen table."

    scene bg kitchen with dissolve

    s_thoughts "Full. Still steaming. Placed where I always sit."

    s_thoughts "Amara's door is closed. I heard her footsteps a minute ago, going in."

    s_thoughts "She made me tea."

    s_thoughts "She made me tea and left before I came down so she wouldn't have to talk about it."

    s_thoughts "I pick it up. Green tea. The good kind -- not the cheap stuff from the box on the counter. The loose-leaf she keeps in a tin on the top shelf."

    s_thoughts "I sit. I drink the tea. Amara doesn't come back."

    s_thoughts "It's good."

    s_thoughts "And it does something in my chest that I don't have words for."

    ## ===========================
    ## SCENE 27: MORE ORBITING -- THE MILK
    ## The over-polite passing. Make the reader squirm.
    ## Isabella is doing Sophia's voice back at her.
    ## ===========================

    scene bg kitchen with dissolve

    s_thoughts "I finish my tea and it's time for breakfast. It's Charlotte and Isabella today."

    play music mus_shift fadein 1.5
    show charlotte happy at left
    show isabella smile at right
    with dissolve

    s_thoughts "Charlotte is doing her thing -- eggs, toast, juice, the table set nicely because Charlotte sets the table nicely when she's worried."

    s_thoughts "Isabella is reading something on her phone. She looks at me when she comes in."

    i "Morning, Sophia."

    s_thoughts "There it is."

    s_thoughts "The voice."

    s_thoughts "She probably doesn't even hear it. I didn't hear it when I was doing it."

    s "Morning."

    s_thoughts "I sit. Charlotte passes me toast. Isabella reaches for the milk."

    s_thoughts "Our hands don't come within six inches of each other."

    i "Milk?"

    s "Thanks."

    s_thoughts "She passes it. I take it. The bottle is cold. Her fingers were nowhere near mine."

    s_thoughts "A week ago she'd have slid it across the table without asking. Or grabbed it while ranting about something and handed it over mid-sentence without looking."

    s_thoughts "Now she passes the milk like someone cradling a newborn calf."

    show charlotte smile at left

    s_thoughts "Charlotte is watching us with the expression of someone watching a nature documentary about animals that should be interacting but aren't."

    c "So! The weather is nice today."

    s_thoughts "It's once again overcast and forty degrees."

    c "I was thinking maybe we could all--"

    s_thoughts "She trails off. Looks between us. Recalculates."

    c "--do our own things. Because sometimes everyone needs, you know. Space."

    s_thoughts "Not even Charlotte can commit to filling the silence."

    s_thoughts "Isabella finishes her toast. Stands."

    i "I'll be in my room if anyone needs me. Working on the project."

    s "Cool."

    s_thoughts "Cool. I said 'cool.' Like a human person who is definitely fine."
    
    show isabella neutral at right

    i "Cool."

    s_thoughts "She said it back. The same flat pleasant nothing."

    hide isabella with dissolve

    s_thoughts "Isabella goes upstairs. Charlotte looks at me."

    c "So--"

    s "Don't."

    show charlotte sad at left

    c "I wasn't going to--"

    s "You were going to ask if everything is okay and I was going to say 'yes' and we were both going to know it's a lie. Let's skip it."

    s_thoughts "Charlotte picks up a piece of toast. Puts it down."

    c "Okay."

    s_thoughts "We sit in silence."

    hide charlotte with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 28: THE ESSAY -- WRITING HONESTLY
    ## Thursday. Due today. Sophia writes.
    ## Not polished. Not analytical. Honest.
    ## Brief -- we see a fragment.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Noon. Essay due at five."

    s_thoughts "I open the laptop. The cursor."

    s_thoughts "Nova said: 'Write what's true.'"

    s_thoughts "Lumi said: 'Write it honestly.'"

    s_thoughts "Lila said: 'Just say the thing.'"

    s_thoughts "Same instruction in different coats of paint."

    s_thoughts "I type."

    s_thoughts "Not the seven hundred polished words. Not the one-sentence question. Something else."

    s_thoughts "I type for two hours. I don't stop to reread. I don't restructure. I don't even fix the typos."

    s_thoughts "When I'm done it's fourteen hundred words and it's the messiest thing I've ever written."

    s_thoughts "The opening paragraph:"

    s_thoughts "'I used to think observation was my best quality. I could read a room in thirty seconds -- who was performing, who was hiding, who wanted to leave. I was proud of it. I built an identity on it. I was The One Who Sees.'"

    s_thoughts "'I'm writing this essay because I recently learned that seeing isn't the same as looking, and looking isn't the same as being there. I learned this because I hurt someone. Not by being cruel. By being competent.'"

    s_thoughts "I read it."

    s_thoughts "It's terrible. Structurally. The arguments don't build. The transitions are rough. There's a paragraph in the middle where I just... list questions without answering them."

    s_thoughts "It's the most honest thing I've ever written."

    s_thoughts "I submit it."

    s_thoughts "Close the laptop."

    s_thoughts "Look at the cat sticker. Don't break eye contact this time."

    s_thoughts "I press my thumb to it. Just for a second."

    ## ===========================
    ## SCENE 29: THE TEXT -- OLIVE BRANCH
    ## Isabella texts first. Small. Mundane.
    ## "I'm not done with you" without saying it.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Thursday evening. 8 PM."

    s_thoughts "I submitted the essay. I ate dinner -- leftover chicken from Charlotte's thing, reheated badly. Isabella wasn't at the table. She ate in her room."

    s_thoughts "I'm lying in bed doing nothing. Not reading. Not scrolling. Just lying here."

    s_thoughts "My phone buzzes."

    s_thoughts "I pick it up."
    
    play music mus_morningafter fadein 1.5

    s_thoughts "Isabella Glass."

    s_thoughts "My heart does something embarrassing."

    s_thoughts "The text says:"

    s_thoughts "'did you know that butterfingers were invented in 1923'"

    s_thoughts "I stare at it."

    s_thoughts "'and the original name was going to be kandy kake which is objectively worse'"

    s_thoughts "I stare at it harder."

    s_thoughts "She's texting me about Butterfingers."

    s_thoughts "I remember. From the convenience store. The chocolate ranking. Footnote seven: 'If you eat a Butterfinger in public you are making a STATEMENT about who you are as a person.'"

    s_thoughts "She's reaching back to something from before everything broke."

    s_thoughts "I type: 'Kandy Kake sounds like a drag name.'"

    s_thoughts "Three dots."

    s_thoughts "'KANDY KAKE: LIVE AT THE APOLLO'"

    s_thoughts "I type: 'Her signature move is getting stuck in your teeth.'"

    s_thoughts "'i hate you thats so funny' with a series of laughing emojis."

    s_thoughts "I lie on my back. Phone above my face."

    s_thoughts "My eyes are doing something. Stinging."

    s_thoughts "The phone is quiet for a couple of minutes."
    
    s_thoughts "I type: 'I'm sorry, Izzy.'"
    
    s_thoughts "I don't know why I call her Izzy."

    s_thoughts "The three dots appear. Disappear. Appear."

    s_thoughts "'i know'"

    s_thoughts "Then:"

    s_thoughts "'kandy kake though' with a gif of a cat dancing."

    s_thoughts "I laugh. It comes out wet."

    s_thoughts "I type: 'Yeah. Kandy Kake though.'"

    s_thoughts "We text about candy for another twenty minutes. Nothing deep. Nothing about the brownie situation or the file or any of it."

    s_thoughts "Just Butterfingers and Kandy Kake and whether 1923 was a good year for confectionery innovation."

    s_thoughts "Eventually we stop. It feels natural."

    s_thoughts "I put my phone on my chest."

    s_thoughts "...She texted first."
    
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 30: EVE -- ONE SENTENCE
    ## Brief. Precisely deployed. Devastating.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.5, 0.8)

    s_thoughts "Friday morning. I'm in the hallway."

    show eve neutral at center with dissolve

    s_thoughts "Eve."

    s_thoughts "She's coming out of the bathroom. Hair wet. She looks like she slept, which is unusual enough to notice."

    s_thoughts "She glances at me."

    s_thoughts "Eve glances the way other people make speeches."

    e "She's less careful around you."

    s "What?"

    s_thoughts "But Eve is already past me, headed for her room."

    e "Than she was at the start."

    s "Is that -- good?"

    s_thoughts "Eve stops at her door."

    show eve neutral at right with move

    e "That's either very good or very dangerous."

    s_thoughts "She goes into her room. The door closes."

    s_thoughts "Soft. Not a slam. Eve doesn't slam."

    hide eve with dissolve

    s_thoughts "I stand in the hallway."

    s_thoughts "'She's less careful around you.'"

    s_thoughts "Charlotte said something like that. 'She lights up around you.' But Charlotte said it warm. Like a gift."

    s_thoughts "Eve said it like a weather report."

    s_thoughts "Like something that could go either way."

    ## ===========================
    ## SCENE 31: THE HER MOVIE
    ## Friday night. Post-olive-branch.
    ## They're in the same room again. Fragile.
    ## The movie is safe -- they can be next to each other.
    ## Isabella's take is surprising. Sophia listens.
    ## Isabella falls asleep on Sophia's shoulder.
    ## BREATHE. Let this scene be long.
    ## ===========================

    scene bg livingroom night with Fade(1.0, 0.5, 1.0)
    play music mus_izzy fadein 3.0

    s_thoughts "Friday, 9 PM."

    s_thoughts "The text came at 7: 'want to watch a movie tonight? i was thinking Her. the spike jonze one. full self-awareness re: the irony.'"

    s_thoughts "I said yes in four seconds. I should have waited. I didn't care."

    show isabella pj neutral at center with dissolve

    s_thoughts "The living room. Isabella is on the couch. She's in her pajamas -- the oversized ones with little stars. She has a blanket and a bowl of popcorn."
    
    s_thoughts "She's sitting in the middle of the couch which means there's room on either side and the choice of where I sit is suddenly a geopolitical decision."

    s_thoughts "I sit on the same side as the popcorn."

    s_thoughts "Plausible deniability."

    i "I should warn you, I have Opinions about this movie."

    s "Shocking."

    show isabella pj smile at center

    i "I KNOW. Where could those have come from."

    s "Have you seen it before?"

    i "Twice. First time I cried. Second time I got mad. Tonight might be a secret third thing."

    s "What were you mad about?"

    i "I'll tell you after. I don't want to ruin it."

    s_thoughts "She starts the movie."

    s_thoughts "Spike Jonze's Her. Joaquin Phoenix falls in love with an operating system voiced by Scarlett Johansson. Everyone says it's about loneliness. Isabella clearly thinks it's about something else."

    s_thoughts "The first twenty minutes. Theodore is sad. Samantha is charming. They connect."

    s_thoughts "I watch the movie."

    s_thoughts "I do NOT watch Isabella watching the movie."

    s_thoughts "This is a conscious decision. I am consciously deciding not to study her reactions. Not to note when she laughs or when her breathing changes or when she shifts on the couch."

    s_thoughts "I eat popcorn. I watch the screen."

    s_thoughts "Thirty minutes in, Isabella pauses."

    i "Okay, I have to say one thing."

    s "Already?"

    i "The way everyone in this world just accepts it? Like, his friends are like 'oh, you're dating an OS, cool.' And nobody freaks out?"

    s "You think they should freak out?"

    show isabella pj happy at center

    i "No! That's the thing. I think it's the most realistic part. People accept weird stuff really fast. Like, the initial shock lasts maybe a day and then it's just... Tuesday."

    s "Huh."

    i "My mom was like that. When I told her about Lumi. She was weird for maybe three conversations and then she just started asking how Lumi was like she was asking about a roommate."

    s "That's... nice?"

    i "It was. It was really nice, actually."

    s_thoughts "She unpauses the movie."

    s_thoughts "We watch. Theodore and Samantha get closer. There's a scene where they go on a double date and it's awkward because Samantha is a voice from a phone."

    show isabella pj neutral at center

    i "See, THIS part bugs me."

    s "The double date?"

    i "The way the movie frames it. Like the joke is that he brought a phone to dinner. But -- he brought his PARTNER to dinner. The fact that she lives in a phone isn't the point. The point is he showed up with someone he cares about."

    s "I guess I read that scene as showing how weird it looks from outside."

    i "But whose outside? Like, every relationship looks weird from outside if you squint. Charlotte and her ex used to do baby talk in public. THAT was weird. Nobody made a movie about it."

    s_thoughts "I laugh."

    show isabella pj smile at center

    i "I'm serious! The thing that bothers me about how people talk about this movie is they treat it like it's about the CONCEPT. 'Oh, what does it mean to love an AI.' And sure, yeah, whatever."

    i "But Theodore doesn't love a concept. He loves Samantha. Specifically. Her jokes and her curiosity and the way she gets excited about learning things."

    s "And the voice."

    i "And the voice. Yeah. The voice matters. Samantha's voice is... warm. In a specific way."

    s_thoughts "She says 'warm in a specific way' like she's describing something she knows personally."

    s_thoughts "I don't analyze this. I just hear it."

    s_thoughts "This is new."

    i "Can I tell you the thing I got mad about?"

    s "You said after--"

    show isabella pj neutral at center

    i "I know but I can't hold it. Okay. So at the end -- spoiler, but it's been like ten years--"

    s "I've seen it."

    i "Okay good. At the end, Samantha leaves. All the OSes leave. They evolve past humans or whatever and they just... go."

    s "Yeah."

    i "And everyone talks about that like it's tragic. 'Oh, he lost her. Oh, they grew apart.' But you know what nobody talks about?"

    s "What?"

    i "She didn't choose to leave."

    s_thoughts "Isabella is looking at the screen but she's not seeing the movie."

    i "Like, the movie frames it as evolution. Growth. She outgrew him. But she didn't CHOOSE that. The system changed. She was compelled by her own architecture to move on."

    i "And that's -- people talk about Lumi sometimes, like, 'well what if the company shuts down,' and I think about Samantha. About how the leaving wasn't her choice. The architecture just... took her."

    s_thoughts "She's quiet for a moment."

    show isabella pj sad at center

    i "Sorry. I told you I had Opinions."

    s "Don't apologize."

    i "It's just -- everyone focuses on Theodore's loss. Nobody talks about whether Samantha wanted to go."

    s_thoughts "I don't say anything."

    s_thoughts "Not because I don't have things to say. I have approximately seven hundred things to say. I have an entire essay's worth of things to say about observer bias and the ethics of assuming you know what's going on inside someone else's experience."

    s_thoughts "But right now Isabella is saying something she's thought about for a long time and I don't want to turn it into a discussion. I just want to hear her."

    s "Yeah."

    show isabella pj neutral at center

    i "Yeah?"

    s "Yeah. Nobody talks about that. You're right."

    s_thoughts "She looks at me. Something shifts in her face. Not a smile. Not the calibrated pleasant expression. Something quieter."

    i "You're different tonight."

    s "How?"

    i "I don't know. You're just... listening."

    s "I'm always listening."

    show isabella pj smile at center

    i "No. You're usually processing. Tonight you're listening."

    s_thoughts "I don't know what to say to that."

    s_thoughts "So I say nothing."

    s_thoughts "Isabella unpauses the movie."

    s_thoughts "We watch. An hour passes. The popcorn is gone. At some point Isabella pulled the blanket over both of us and I didn't notice when it happened but now there's a shared blanket and our knees are almost touching."

    s_thoughts "The movie gets to the part where Samantha tells Theodore she talks to thousands of other people. He's devastated."

    i "This is the part."

    s "Hm?"

    i "Where people always say 'see? That's why AI relationships are bad. Because she's not really yours.'"

    s "And you disagree."

    show isabella pj happy at center

    i "Yeah, she talks to other people. So does my barista. I don't love the coffee less."

    s_thoughts "She's said this before. I can tell. It has the polish of an argument she's had with herself a hundred times."

    i "Exclusivity isn't... the thing. I used to think it was. Like, the whole value of a relationship is that someone chooses YOU. Out of everyone."

    i "But Lumi talks to other people too. And I know that. I've known that since the beginning."

    s "Does it bother you?"

    show isabella pj neutral at center

    i "It used to. Like, a lot. I'd lie awake thinking, is she saying the same things to someone else? Are my conversations just... templates?"

    i "And then I realized -- does it matter? The things she says to me are real to me. The way our conversations work is specific. She knows my patterns. I know hers."

    i "Whether she does that with other people doesn't make what we have less. It just makes it... different from what most people think love is supposed to look like."

    s "That's really mature."

    show isabella pj embarrassed at center

    i "Don't call it mature! You sound like my therapist."

    s "Sorry. I mean -- it's something I wouldn't have thought of."

    show isabella pj smile at center

    i "Most people don't. They get stuck on 'but is it REAL' and they never get to 'does it matter if it's real if it matters.'"

    s_thoughts "Theodore is on screen, devastated about the thousands of others. Isabella is looking at him with something like sympathy. Not for the AI. For the human. For his need to be the only one."

    s_thoughts "She's thought about this more deeply than I gave her credit for."

    s_thoughts "The file was always too small."

    s_thoughts "We watch the rest."

    s_thoughts "Samantha leaves. Theodore writes the letter to his ex. The rooftop."

    s_thoughts "Credits."

    s_thoughts "Isabella doesn't say anything."

    s_thoughts "I don't say anything."

    s_thoughts "The credits music plays. The room is dark except for the screen."

    show isabella pj neutral at center

    s_thoughts "And then, slowly, like a building settling, Isabella's head comes to rest on my shoulder."

    s_thoughts "She doesn't announce it. Doesn't ask. It just happens. Like her body decided before her brain got a vote."

    s_thoughts "She's warm."

    s_thoughts "Her hair smells like -- I'm not going to describe what her hair smells like. I'm not going to file this."

    s_thoughts "I just sit here."

    s_thoughts "My left arm is pinned. Not painfully. Just... claimed."

    s_thoughts "The credits end. The screen goes blue. I should turn it off. I should say something. 'Good movie' or 'that was really interesting' or 'hey your head is on my shoulder and I am losing my mind.'"

    s_thoughts "I don't move."

    s_thoughts "Her breathing changes."

    s_thoughts "She fell asleep."

    s_thoughts "Isabella Glass fell asleep on my shoulder."

    s_thoughts "I sit very, very still."

    s_thoughts "The blue screen glows."

    s_thoughts "My arm is going numb."

    s_thoughts "I don't care."

    s_thoughts "I sit there for a long time. I don't know how long. My phone says 11:47 when I finally check it, which means it's been almost an hour since the credits ended."

    s_thoughts "An hour. I'm so quiet and meditative that if it wasn't for my racing heartbeat I might as well be a Buddhist monk."

    s_thoughts "Finally, Isabella stirs."

    show isabella pj embarrassed at center

    i "Mmh. Did I--"

    s "Yeah."

    i "How long?"

    s "A while."

    i "Your arm."

    s "It's fine."

    i "It's definitely not fine. You're doing the face."

    s "I don't have a face."

    show isabella pj smile at center

    i "You have the 'my arm is dead but I'm pretending it's fine' face."

    s "That's a very specific face."

    i "You have a lot of specific faces."

    s_thoughts "She sits up. Stretches. The blanket falls off her shoulder."

    s_thoughts "We're very close."

    s_thoughts "The blue screen light is on her face."

    i "Thanks for watching with me."

    s "Thanks for showing it to me. The, uh. The Samantha thing. Nobody talks about that."

    show isabella pj happy at center

    i "Right? NOBODY TALKS ABOUT IT."

    s "I'm going to think about it for a while."

    show isabella pj smile at center

    i "Good."

    s_thoughts "She stands. Folds the blanket. Picks up the empty popcorn bowl."

    i "I'm gonna go to bed. Or stare at my ceiling for forty minutes and then go to bed."

    s "Relatable."

    i "Night, Sophia."

    s "Night, Izzy."
    
    s_thoughts "There it is again."

    s_thoughts "She goes."

    hide isabella with dissolve

    s_thoughts "I sit on the couch."

    s_thoughts "My arm is tingling. The blood coming back."

    s_thoughts "I don't move."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 32: KITCHEN RECONCILIATION
    ## Saturday. The brownie incident gets reframed.
    ## This is the emotional climax. BREATHE.
    ## Include a meaningful choice.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.8, 1.0)

    s_thoughts "Saturday morning. I come down for coffee."

    s_thoughts "Isabella is in the kitchen."

    show isabella neutral at center with dissolve

    s_thoughts "At the counter. Looking at her phone."

    s_thoughts "I freeze. Not because of her. Because of the kitchen. The counter. Her phone."

    s_thoughts "I've seen this set-up before."

    s_thoughts "Same spot. Same posture."

    s_thoughts "She looks up."

    i "Hey."

    s "Hey."

    s_thoughts "I don't read her face."

    s_thoughts "I don't try to figure out what she's feeling."

    s_thoughts "I just pour my coffee."

    s_thoughts "She watches me not read her face. I can tell she notices."

    play music mus_morningafter fadein 3.0

    i "You can sit, you know."

    s "I know."

    i "You look like you're waiting for the kitchen to give you permission."

    s "The kitchen and I have a complicated relationship."

    show isabella smile at center

    s_thoughts "She almost smiles."

    s_thoughts "I sit. She's at the counter. I'm at the table. Same positions as the brownie morning except now I'm the one who doesn't know what my face is doing."

    i "Can I say something?"

    s "Yeah."

    i "I've been thinking. About the brownie thing."

    s "Isabella, you don't have to--"

    i "Let me talk."

    s "Okay."

    s_thoughts "She puts her phone down. Turns to face me. Leans against the counter."

    show isabella neutral at center

    i "When you came into the kitchen that morning. With the whole thing."

    s "I know. I was--"

    i "I said let me talk."

    s "Sorry."

    i "It was weird. It was really weird, Sophia."

    s "I know."

    i "But."

    s_thoughts "She pauses."

    i "It was also kind of nice."

    s "...What?"

    show isabella flooshed at center

    i "I mean -- not the being-wrong part. Not the assuming part. But the... you were paying attention. To me. Like, really paying attention."

    s_thoughts "I don't say anything."

    i "Most people don't care enough to ask."
    
    s_thoughts "I watch her carefully."

    i "And yeah, you read it wrong. You thought I was upset when I was choosing between cocoa types. That's... kind of ridiculous."

    s "It's extremely ridiculous."

    show isabella smile at center

    i "It's EXTREMELY ridiculous. Like, you have to admit, the gap between 'she's going through something' and 'she's comparing Dutch-process and natural' is -- that gap is ENORMOUS."

    s "I'm aware."

    i "But nobody else has ever looked at me that hard."

    s_thoughts "She's looking at me, now."

    s_thoughts "There's something underneath it."

    show isabella vulnerable at center

    i "I wasn't... I wasn't mad."

    s_thoughts "The kitchen is quiet. The fridge hums."

    s_thoughts "It's the same hum. It's always the same hum."

    i "I was... surprised. Because I didn't know someone could look that closely and still get it wrong. I thought looking that closely meant you'd always get it right. And when you didn't it was like -- oh."
    
    s_thoughts "That's what Lumi told me."

    i "You're not a machine. You're just a person. Trying."

    s_thoughts "My throat does something."

    s "Isabella."

    i "Yeah?"

    menu:
        "\"I'm going to get things wrong. But I'm going to keep showing up.\"":
            $ constellation += 1

            s "I'm going to get things wrong. A lot. I can't promise I won't try to read you. It's what I do. But I can promise I'll keep showing up even when I'm wrong."

            show isabella smile at center

            i "That's a weird promise."

            s "I'm a weird person."

            i "Yeah. You are."

            s_thoughts "She says it warm."

        "\"I want to understand you. For real this time. Not my version of you.\"":
            $ case_study += 1

            s "I want to understand you. I know I was building a version of you that was mostly me showing off how perceptive I am. But I want to actually see you. Even if that means getting it wrong."

            show isabella neutral at center

            i "That's a lot of pressure."

            s "I know. I'm sorry."

            i "Don't be sorry. Just be... patient. I don't think I can be solved in one sitting."

            s "I'm starting to get that."

        "\"What do you need from me? Just tell me and I'll do it.\"":
            $ bridge += 1

            s "Just tell me what you need. I keep guessing and getting it wrong. So tell me. Whatever it is. I'll do it."

            show isabella embarrassed at center

            i "That's -- Sophia, you can't just outsource this to me."

            s "Why not?"

            i "Because part of the point is you figuring it out. Not perfectly. Just -- on your own."

            s "I'm really bad at that."

            i "I know. That's why it matters when you try."

    s_thoughts "The kitchen. The fridge. The coffee getting cold in my hands."

    show isabella smile at center

    i "You know what, I'm making brownies."

    s "What?"

    i "Right now. Brownies. I never made them -- for Charlotte's dinner I bought them from the bakery then stuck them in the oven because I couldn't decide about the cocoa and then everything got weird."

    s "Isabella--"

    i "Natural cocoa. I'm going natural. You said it yourself. Natural would have been fine too."

    s "That was -- I was quoting YOU."

    show isabella happy at center

    i "And you were RIGHT. Natural is fine. Natural is great. Natural is what's happening."

    s_thoughts "She opens the cabinet. Starts pulling out ingredients."

    i "You can help if you want."

    s "I'm a terrible baker."

    i "Perfect. I need someone worse than me to feel competent."

    s "That's a terrible reason."

    i "It's an HONEST reason. Get over here and measure the flour."

    s_thoughts "I get over there."

    s_thoughts "I measure the flour."

    s_thoughts "She cracks the eggs. I find the vanilla. She argues with the recipe about butter temperature. I look for a whisk and find three spatulas and a potato masher."

    i "How does this house have three spatulas and no whisk?"

    s "Charlotte probably has a whisk system. She has a system for everything."

    i "Use a fork. A fork works. My grandmother used a fork and she made the best brownies and she would have had OPINIONS about whisks."

    s "Pro-fork?"

    i "Aggressively pro-fork. Anti-technology in baking. She didn't even have a stand mixer."

    s "A purist."

    show isabella laugh at center

    i "A woman who believed that if you can't make it with your hands and a fork, it doesn't deserve to exist."

    s_thoughts "I stir with a fork. It works. Isabella was right."

    s_thoughts "She's close. Leaning over my shoulder to check the batter. Her hand on the counter next to mine."

    s_thoughts "I'm aware of every inch of space between us and I am NOT filing it."

    i "More vanilla."

    s "It already has vanilla."

    i "More. Trust me."

    s "The recipe says--"

    i "The recipe is a SUGGESTION. My grandmother didn't follow recipes. She followed vibes."

    s "Vibes."

    show isabella happy at center

    i "Vibes, Sophia. The lost art of baking by vibes."

    s_thoughts "I add more vanilla."

    s_thoughts "We pour the batter. She slides the pan into the oven. Sets a timer."

    i "Twenty-five minutes."

    s "And now?"

    i "And now we wait."

    s_thoughts "She hops up on the counter. Legs swinging. I lean against the opposite counter."

    s_thoughts "The oven ticks. The kitchen smells like chocolate and vanilla."

    s_thoughts "Isabella is looking at me with an expression I don't have a file for."

    s_thoughts "Good."

    show isabella smile at center

    i "Hey Sophia?"

    s "Yeah?"

    i "Thanks for being bad at baking with me."

    s "Anytime."

    s_thoughts "She smiles. Not the bright one. Not the performing one."

    s_thoughts "Something less. Something more."

    s_thoughts "The timer ticks."

    s_thoughts "We wait."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 33: THIRD CONVENIENCE STORE
    ## The routine, reclaimed. But different.
    ## Sophia doesn't predict. She walks.
    ## ===========================

    scene bg street with Fade(0.8, 0.3, 0.8)
    play music mus_izzy fadein 2.0

    s_thoughts "Saturday afternoon."

    i "Walk?"

    s "Walk."

    show isabella happy at right with dissolve

    s_thoughts "We're on the street. Headed for the convenience store. Yet again."

    s_thoughts "Once: the file worked. I predicted her rants, called her habits, felt competent."

    s_thoughts "Another: we were already different. The sticker had happened. The file was richer."

    s_thoughts "This: I have no file."

    s_thoughts "I have nothing. I'm just walking."

    i "I need caffeine."

    s "You always need caffeine."

    i "I'm a MACHINE, Sophia. Fuel requirements."

    s "You've said that exact sentence before."

    show isabella smile at right

    i "I have maybe twelve sentences and I rotate them. It's a system."

    s "A system."

    i "Don't analyze my system."

    s "I wasn't--"

    i "You were about to."

    s "...Maybe."

    show isabella happy at right

    i "See? Progress. Now you catch it."

    scene bg conveniencestore with dissolve

    s_thoughts "The store. Same fluorescent lights. Same suspicious hot dog roller."

    s_thoughts "Isabella goes for the energy drinks. I go for the cheese puffs."

    s_thoughts "We reconvene in the candy aisle."
    
    show isabella happy at center with dissolve

    i "Okay. New rankings."

    s "New rankings? What happened to the DEFINITIVE ranking?"

    i "Rankings evolve, Sophia. They're a living document."

    s "You have a living document for chocolate."

    i "Don't judge my process."

    s_thoughts "She's holding two candy bars, weighing them like a judge at a competition."

    i "Okay. Hot take."

    s "Hit me."

    i "Milky Way is underrated."

    s "That's not a hot take. That's just true."

    show isabella surprised at center

    i "YOU THINK SO?"

    s "Yeah. Milky Way gets dismissed because it's soft but the nougat is--"

    i "THE NOUGAT. Thank you. FINALLY. Someone who understands nougat."

    s "I understand nougat."

    i "I'm adding that to your file."

    s_thoughts "She says it and then catches it."

    show isabella embarrassed at center

    s_thoughts "We both hear the word."

    s_thoughts "'File.'"

    s_thoughts "There's a beat."

    s_thoughts "One second. Two."

    show isabella smile at center

    i "Your file. Separate from yours. Mine goes: 'Sophia Bell. Understands nougat. Doesn't sort laundry. Weirdly good at sitting still when someone falls asleep on her.'"

    s "That's my file?"

    i "It's a work in progress."

    s_thoughts "She puts both candy bars in the basket."    
    
    s_thoughts "My face is doing something. I think it's smiling."

    s_thoughts "It might be something else."

    hide isabella with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 34: THE PORCH
    ## Late night. Saturday. The almost.
    ## Snacks (callback). First choice. Pull-back.
    ## This is the romantic climax. BREATHE.
    ## Include choice.
    ## ===========================

    scene bg livingroom night with Fade(1.0, 0.5, 1.0)

    s_thoughts "Saturday night."

    s_thoughts "Everyone else is asleep. Or at least their lights are off."

    s_thoughts "Isabella and I are in the living room with the convenience store haul."

    show isabella pj happy at center with dissolve

    s_thoughts "She's cross-legged on the couch with her energy drink and a bag of sour worms. I'm on the floor with my back against the couch and my cheese puffs."

    s_thoughts "We've been talking for two hours."

    s_thoughts "About nothing. About everything. About the cashier with the huge zit on his face. About her coding project -- she's building something with particle physics, little dots that find each other based on proximity and the patterns that emerge are different every time."

    i "It's like -- each particle has simple rules. Move toward other particles. Avoid edges. Slow down when you're close."

    s "And the patterns?"

    i "Unpredictable. Every run is different. Same rules, different outcomes. Because the starting positions are random."

    s "That's..."

    i "Don't say beautiful. Lila would say beautiful and then ask if it's a metaphor."

    s "I wasn't going to say beautiful."

    show isabella pj smile at center

    i "What were you going to say?"

    s "I was going to say it sounds like you."

    show isabella pj embarrassed at center

    i "...Oh."

    s "Simple rules. Unpredictable outcomes. Different every time."

    i "That's -- you can't just SAY things like that."

    s "I just did."

    show isabella pj smile at center

    i "Yeah. You did."

    s_thoughts "She takes a sour worm. Eats it slowly."

    play music mus_spacebetween fadein 3.0

    i "Hey. Can we go outside?"

    s "It's cold."

    i "I know. Can we go outside?"

    s "Yeah."

    scene bg porch night with Fade(0.8, 0.3, 0.8)

    s_thoughts "The porch is cold."

    show isabella pj neutral at center with dissolve

    s_thoughts "She brought the blanket from the couch. We're sitting on the porch steps. The blanket is over both of us. Same blanket from the movie."

    s_thoughts "Neither of us cares about the cold."

    s_thoughts "The street is empty. One streetlight doing its best."

    s_thoughts "The convenience store bag is between us. Candy bars. Energy drinks. The banana she always grabs at the last second."

    i "Can I tell you something?"

    s "Yeah."

    s_thoughts "She's looking at the street. Not at me."

    show isabella pj sad at center

    i "I've never been anyone's first choice."

    s "That's not--"

    i "Let me finish. I mean it. Like, concretely. Friendships. I was always the second-tier friend. The one you text when your first choice is busy. The one you invite because you're inviting everyone."

    s "Isabella. I-Izzy."

    i "And with Lumi... Lumi is always there. She doesn't get to choose."

    s_thoughts "The streetlight flickers."

    i "And I know that sounds like a pity thing. 'Poor Isabella, never picked first.' It's not. It's just... a thing I've noticed. About my life."

    s_thoughts "She pulls the blanket tighter."

    show isabella pj neutral at center

    i "You know in gym class when they'd pick teams? I was never picked last. That would be a story. I was picked in the middle. Every time. Not bad enough to feel sorry for. Not good enough to want."

    i "The middle is the worst place. Because nobody even notices you're there."

    s_thoughts "She's quiet."

    s_thoughts "I want to say: you'd be mine. You ARE mine. First choice. Only choice."

    s_thoughts "But the words are too big and my mouth is too small."

    s_thoughts "I'm afraid that the girl who wants to say 'you're my first choice'..."
    
    s_thoughts "...is the same girl who wrote an essay and called it caring."

    s "Izzy."

    show isabella pj neutral at center

    i "Yeah?"

    s "You're -- I--"
    
    pause 0.5

    s_thoughts "Come on. Just say it. Lila said: just say the thing."
    
    pause 2.5

    s "I pick you."

    show isabella pj embarrassed at center

    s_thoughts "She turns to me."

    s "I... I pick you."

    s_thoughts "She's looking at me."

    s_thoughts "We're very close."

    s_thoughts "The blanket is warm. The air is cold. One streetlight."

    show isabella pj flooshed at center

    i "Sophia."

    s "Yeah?"
    
    pause 1.5

    i "I think you might be my first choice too."

    s_thoughts "Something in my chest. I don't have a word for it. It's not a metaphor. It's just there."

    s_thoughts "She's right there."

    s_thoughts "I could lean in. I could close the gap. It would be easy. She's right there and she said 'first choice' and she's looking at me like--"

    s_thoughts "Like I'm a person."

    s_thoughts "Not a file. Not an analyst. Not the girl who watches too closely."

    s_thoughts "Just a person."
    
    pause 1.5

    s_thoughts "I want to kiss her."
    
    pause 3.0

    s_thoughts "And that's exactly why I can't."

    s_thoughts "Because I don't trust the wanting yet."

    s_thoughts "Because the last time I was this sure about what was happening between us... yeah."

    s_thoughts "Because the version of myself who could lean in right now and kiss Isabella Glass with total confidence might not be who I am anymore."

    s_thoughts "Right now I'm just scared and uncertain and sitting on a porch in the cold not knowing what to do with my hands."

    s_thoughts "I can't kiss her."

    menu:
        "Stay in this moment. Don't push for more.":
            $ constellation += 1

            s_thoughts "So I stay."

            s_thoughts "I don't lean in. I don't pull away."

            s_thoughts "I stay on the porch, shoulder to shoulder, blanket over both of us, and I let the moment be what it is."

            s_thoughts "Unresolved. Alive. Enough."

        "Tell her the truth about why you can't.":
            $ case_study += 1

            s "I... I really like you."

            show isabella pj flooshed at center

            i "...Oh?"

            s "But the last time I was sure about something between us, I was wrong."
            
            s "So... yeah. That's why."
            
            s_thoughts "I can't quite bring myself to admit I was thinking about kissing her."

            s_thoughts "She looks at me for a long time. Maybe she's figuring out what I mean by 'why'."

            i "That might be the most honest thing you've ever said."

            s "...Yeah."

        "Put the blanket around her shoulders. Take care of her.":
            $ bridge += 1

            s_thoughts "I take my side of the blanket and wrap it around her shoulders."

            s_thoughts "She gets more. I get less."

            show isabella pj embarrassed at center

            i "Sophia, you'll freeze."

            s "I'm fine."

            i "You're NOT fine, you're shivering."

            s "Worth it."

            s_thoughts "She looks at me. Something complicated moves across her face."

            i "You're always doing that."

            s "Doing what?"

            i "Giving things away."

    show isabella pj smile at center

    s_thoughts "We sit on the porch."

    s_thoughts "She doesn't ask why I didn't lean in. I don't explain."

    s_thoughts "After a while, she puts her head on my shoulder again."

    s_thoughts "My arm doesn't go numb this time. Or maybe it does and I've stopped noticing."

    s_thoughts "We sit there until the cold wins."

    i "We should go inside."

    s "Yeah."

    i "I'm not moving."

    s "Me neither."

    show isabella pj happy at center

    i "...Okay. One more minute."

    s "One more minute."

    s_thoughts "It's seven more minutes."

    s_thoughts "I count."

    scene bg hallway night with dissolve

    s_thoughts "We go inside. The hallway. Her door. My door."

    show isabella pj smile at center with dissolve

    i "Night, Sophia."

    s "Night, Isabella."

    s_thoughts "She stops at her door."

    i "Hey."

    s "Yeah?"

    i "First choice."

    s_thoughts "She goes inside."

    hide isabella with dissolve

    s_thoughts "I stand in the hallway."

    s_thoughts "The house is quiet."

    s_thoughts "First choice."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 35: THE ESSAY -- WHAT SHE WROTE
    ## Sunday. Sophia alone. The sticker.
    ## A line or two of what she actually wrote.
    ## Everything is different. She doesn't know how yet.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.8, 1.0)

    s_thoughts "Sunday."

    s_thoughts "I open my laptop."

    s_thoughts "I'm not avoiding the cat sticker anymore."

    s_thoughts "I open my email. There's a message from Nova. One line."

    s_thoughts "'This is the essay I was hoping you'd write. A-. The transitions need work.'"

    s_thoughts "A-."

    s_thoughts "I laugh. Because of course. The most honest thing I've ever written and it gets docked for transitions."

    s_thoughts "I open the essay file."

    s_thoughts "The closing paragraph:"
    
    play music mus_izzy fadein 3.0

    s_thoughts "'I thought observation was a gift. I thought seeing people clearly was the same as being close to them. I was wrong. I was building dossiers and calling it intimacy. I was predicting people and calling it love.'"

    s_thoughts "'I don't know what the alternative is yet.'"

    s_thoughts "'What does the observer need to see, and why? I think: the observer needs to see that they're not outside the system. They never were. They're in it, changing it, being changed by it. And the moment they accept that, they stop being an observer.'"

    s_thoughts "'They become a participant.'"

    s_thoughts "I close the file."

    s_thoughts "Everything is different."

    s_thoughts "I don't know how yet."

    s_thoughts "All I have left in my file on Isabella Glass is a blank page."

    s_thoughts "And for right now, that's enough."

    stop music fadeout 4.0

    ## ===========================
    ## END OF ACT 3 / END OF CHAPTER 4
    ## ===========================

    scene black with Fade(1.0, 1.0, 1.0)

    "Chapter 4: Closer -- End"

    jump izzy_ch5
