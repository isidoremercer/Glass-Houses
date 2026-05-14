## charlotte_ch4.rpy -- Glass Houses
## Chapter 4: "The Honeymoon" -- Charlotte Route
## Act 1: "Of Course"

## === AUDIO DEFINITIONS ===
define audio.mus_charlotte = "audio/music/Charlotte Opal ~ Toast Girl.mp3"
define audio.mus_charlotte_sad = "audio/music/Charlotte Opal ~ Of Course.mp3"
define audio.mus_planned = "audio/music/Planned Evening.mp3"
define audio.mus_shoulders = "audio/music/Shoulders Touching.mp3"

## === CHARLOTTE ROUTE VARIABLES ===
## Defined in variables.rpy — do not duplicate here

## ===========================
## CHAPTER 4 START
## ===========================

label charlotte_ch4:

    ## ===========================
    ## SCENE 1: MORNING AFTER THE PARTY
    ## Charlotte is already up. The house smells like someone's taking care of it.
    ## The other girls filter through. Eve is absent.
    ## Charlotte manages the room without anyone noticing. Sophia notices.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_charlotte fadein 3.0

    s_thoughts "The kitchen smells like butter and something herby. Rosemary, maybe. Someone cooked here."

    s_thoughts "I know who that someone is."

    s_thoughts "Last night was -- yeah. Last night happened."

    s_thoughts "The party. The thing I said. The look on her face when I said it."

    s_thoughts "And then this morning. Toast. Cold toast. Charlotte on the edge of my bed, not smiling for once, and somehow that was the kindest thing anyone's ever done for me."

    s_thoughts "I come downstairs and the kitchen is already warm."

    show charlotte happy at center with dissolve

    c "Morning!"

    s_thoughts "There it is. The brightness. Like last night was a blip and this morning is the correction."

    s "Hey."

    c "I made frittata! It's a new recipe. There's coffee on the counter -- I used the good beans, the ones Eve hides behind the oat milk."

    s "She hides her coffee?"

    c "She thinks she hides her coffee. I reorganized the pantry last week."

    s_thoughts "Charlotte is wearing an apron. An actual apron. With lemons on it. She's plating food with the precision of someone who has done this every morning of her life and will do it every morning after."

    s_thoughts "The table is set for five."

    s_thoughts "Five forks. Five napkins. A little vase of flowers in the center that definitely weren't there yesterday."

    s "Charlotte. It's 7 AM."

    c "Flowers don't care what time it is!"

    s "Where did you even get flowers at 7 AM?"

    show charlotte smile at center

    c "The garden. There's a garden. Did you not know there's a garden? Behind the house? It's mostly weeds but there's lavender and some daisies that are really committed to being alive."

    s_thoughts "I did not know there's a garden."

    s_thoughts "Charlotte knows the house better than the house knows itself."

    show isabella sad at left with dissolve

    s_thoughts "Isabella shuffles in. Hoodie backwards."

    i "Nrrgh."

    c "Coffee's on the counter!"

    i "Bless you. Bless your entire family line."

    s_thoughts "Isabella pours coffee. Takes a sip. Her eyes close. Something in her shoulders unclenches."

    show isabella neutral at left

    i "Is that frittata?"

    c "New recipe! I added goat cheese."

    i "Charlotte. Charlotte, you beautiful maniac."

    show charlotte laugh at center

    s_thoughts "Charlotte beams. She plates a piece for Isabella. Plates one for me. Gets the mugs down -- she knows which ones. The one with the chip for me, the cat mug for Isabella."

    s_thoughts "She knows which mugs."

    s_thoughts "She hands me the chipped one and our fingers brush and she doesn't pull away and neither do I and that's probably nothing."

    s_thoughts "That's probably nothing."
    
    s_thoughts "...Probably."

    show amara neutral at right with dissolve

    s_thoughts "Amara materializes at the table. She's holding a book and a cup of tea that she apparently manifested from thin air."

    a "Morning."

    s "When did you get here?"

    a "Before you."

    s_thoughts "Fair."

    s_thoughts "Amara is reading. Charlotte is plating. Isabella is becoming a person one sip at a time. Eve's chair is empty."

    s_thoughts "I look at the empty chair. I look at Charlotte."

    s_thoughts "Charlotte is looking at the empty chair too. Her jaw does something -- a tiny flex, barely visible. Then she turns back to the stove."
    
    show charlotte happy at center

    c "I left a plate for Eve in the fridge. In case she's hungry later."

    s_thoughts "In case. Not when."

    s_thoughts "Charlotte says 'in case' like it's generosity. But the plate is already wrapped in cling film with Eve's name on a sticky note. Charlotte was always going to make the plate."

    s_thoughts "I catch myself. Am I reading too much into a plate? Into cling film?"

    s_thoughts "Charlotte catches me watching her. She smiles."

    show charlotte smile at center

    s_thoughts "It's a good smile. Warm. Easy. The kind of smile that makes you think everything is fine and you were being paranoid for noticing anything at all."

    s_thoughts "Maybe I was."

    c "You okay?"

    s "Yeah. The frittata is really good."

    c "You haven't tried it yet."

    s "I'm preemptively complimenting you."

    show charlotte laugh at center

    c "I'll take it!"

    s_thoughts "I try the frittata. It's really good. Of course it's really good."

    s_thoughts "Charlotte sits down across from me. She's got her own plate. She pushes the food around with her fork."

    s_thoughts "She's not eating."

    s_thoughts "I notice. I've been noticing since the first breakfast."

    s_thoughts "But this morning, with the toast still somewhere inside me and her face last night still somewhere behind my eyes, I don't file it. I just see it."

    s_thoughts "And I don't know what to do with seeing it."

    i "Sophia, you have frittata face."

    s "I don't have frittata face."

    i "You're staring at your plate like it asked you a philosophical question."

    s "Maybe it did."

    show isabella smile at left

    i "What did the frittata ask you?"

    s "Whether goat cheese belongs in eggs."

    c "It DOES."

    i "Controversial."

    a "It's eggs."

    s_thoughts "Normal morning. Five girls in a house. Four at the table. One absent. One not eating. The rest of us pretending both of those things are fine."

    s_thoughts "Charlotte is smiling at me across the table."

    s_thoughts "I smile back."

    s_thoughts "It feels real. I want it to be real. I think wanting it to be real might be the same thing."

    hide isabella
    hide amara
    hide charlotte
    with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 2: CAMPUS -- SOPHIA AND LILA
    ## Sophia tells Lila about the toast. Lila clocks it.
    ## Lila's sister subplot plants the sibling parallel.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)
    play music mus_campus fadein 2.0

    s_thoughts "Tuesday. The campus is doing that thing where it pretends autumn is romantic instead of just cold and damp."

    s_thoughts "Leaves everywhere. The kind of aggressive leaf coverage that says 'we're FESTIVE whether you like it or not.'"

    show lila happy at center with dissolve

    l "Okay. Tell me everything."

    s "About what?"

    l "Don't 'about what' me. You've got A Look."

    s "I don't have a look."

    l "You have the exact look of someone who was recently brought toast in a moment of emotional crisis. Spill."

    s "How could you possibly know about the toast?"

    show lila laugh at center

    l "I didn't! You just TOLD me about the toast! I guessed and you CONFIRMED!"

    s "I hate you."

    l "You love me. Toast. Go."

    s_thoughts "I tell her. Not all of it -- not the party, not the cruel thing, not the way Charlotte's face looked when she stopped smiling. Just the toast part. The morning-after part. Charlotte showing up with a plate and sitting on my bed and not asking what happened."

    l "That's either the sweetest thing I've ever heard or the biggest red flag I've ever heard."

    s "Why can't it be both?"

    l "Because those are mutually exclusive categories, Sophia."

    s "Are they though?"

    show lila annoyed at center

    l "People who show up with toast at 7 AM after a crisis are either in love with you or they're compulsive as hell."

    s "...What if it's both?"

    l "Then you're in trouble either way."

    s "That's your advice? 'You're in trouble'?"

    l "I never said I give good advice. I give CONFIDENT advice. There's a difference."

    s_thoughts "She's not wrong. On either count."

    s "She just -- she didn't ask me anything. She just showed up with toast and sat there. And it was enough. Nobody's ever been -- like, most people would want to address the elephant. Charlotte just made toast for it."

    show lila happy at center

    l "Babe."

    s "What."
    
    show lila laugh at center

    l "You're describing the toast with the same energy I describe my ex's biceps."

    s "I am NOT--"

    l "You are. You're toast-smitten. You have toast feelings."

    s "Lila."

    l "Toast. Feelings."
    
    show lila happy at center

    s_thoughts "I open my mouth to argue. Close it."

    s_thoughts "She might be right."

    s "I don't know what this is."

    l "I know what it is. It's the part where you like someone and instead of saying 'I like someone' you turn it into a research project."

    s "I don't do that."

    show lila shocked at center

    l "What about Katie? Is this a pattern, Sophia?"

    s "Thank you for the diagnosis."

    l "I'm HELPING."

    s_thoughts "She's not helping. She's also not wrong."

    show lila happy at center

    s "So what do I do?"

    l "Do you actually want advice or do you want me to tell you what you already decided?"

    s "...The second one."

    l "You already decided to fall for her. You decided when she brought the toast. You're just running the numbers after the fact."

    s_thoughts "..."

    s "Okay. Changing the subject. How are you?"

    l "Oh, TERRIBLE. My sister won't stop texting me."

    s "Isn't that nice?"

    show lila annoyed at center

    l "It WAS nice. For the first three hundred texts. But she's -- Sophia, she's building her whole IDENTITY around being Like Lila. She calls me her 'role model.' She signed up for business courses because I'M a business major. She started wearing RED GLASSES."

    s "She got your glasses?"

    l "MY glasses. My EXACT prescription frame. She went to my optometrist. She asked for the Lila Special."

    s "The Lila Special."

    l "That's what the receptionist called it. Apparently I'm a BRAND now."

    s "You literally just said everyone has a brand."

    show lila shocked at center

    l "Not like this! This isn't branding, this is -- she's sixteen and she's turning into ME and I'm not even sure I like being me most days! What happens when she finds out?"

    s "Finds out what?"

    l "That I'm making this up as I go! That the confidence is a BIT, Sophia! She thinks I know what I'm doing and I'm terrified she's going to model her whole life after someone who picked business because my Dad wanted it!"

    s_thoughts "Lila is gripping her coffee with both hands. Her voice is loud but her eyes aren't matching."

    s "Hey."

    l "I'm fine."

    s "You're not."

    show lila annoyed at center

    l "I'm -- okay, I'm not. But that's my problem. You've got toast feelings to deal with."

    s "Your sister looking up to you doesn't mean she's going to become you, Lila. People take pieces. She's taking the glasses and the confidence. She's going to figure out her own stuff."

    l "What if she takes the bad pieces?"

    s "Then she'll figure that out too."

    s_thoughts "Lila drinks her coffee. Looks at me over the rim."

    show lila happy at center

    l "When did you get smart?"

    s "I've always been smart. You just don't listen."

    l "I never listen. That's part of my brand."

    s_thoughts "She grins. It's real."

    s_thoughts "We sit with it for a minute. Two friends on a campus bench with coffee. Normal."

    l "Go get your toast girl, Sophia."

    s "Don't call her my toast girl."

    l "Toast. Girl."

    s "I'm leaving."

    l "TEXT ME UPDATES."

    hide lila with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 3: CHARLOTTE'S KITCHEN (Evening)
    ## Charlotte cooking for Sophia specifically. The pattern starts.
    ## Charlotte corrects. Sophia lets her or doesn't.
    ## CHOICE 1.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_charlotte fadein 2.0

    s_thoughts "I get home around six. The house is quiet."

    s_thoughts "No -- not quiet. Charlotte-quiet. Which means there's music playing softly from her phone and something simmering on the stove and the kitchen lights are dimmed to 'evening mode,' which Charlotte apparently has opinions about."

    s_thoughts "She's at the counter. Chopping. The knife sounds are even and rhythmic. She's in a zone."

    show charlotte smile at center with dissolve

    c "Oh! Hi! I didn't hear you come in."

    s "What are you making?"

    c "Just stir-fry. Nothing fancy."

    s_thoughts "It's fancy. There are julienned vegetables. Nobody julienned their vegetables for 'nothing fancy.'"

    c "I noticed you didn't eat lunch."

    s "How did you notice that?"

    c "Your lunchbox was on the counter this morning. It's still there."

    s_thoughts "I look. The lunchbox is still there. I forgot it."

    s_thoughts "Charlotte noticed it nine hours ago and has been waiting to feed me ever since."

    s "You didn't have to make--"

    c "I was already cooking! It's nothing. Sit."

    s "I don't want to just sit. Let me help."

    show charlotte surprised at center

    c "You want to help?"

    s "I have functional hands, Charlotte."

    show charlotte happy at center

    c "Okay! Okay, you can do the peppers. Here --"

    s_thoughts "She hands me a red pepper and a knife. I start cutting."

    s_thoughts "The cutting is... fine. It's pepper cutting. I'm cutting a pepper."

    c "So how was your day? Did you have Nova's class?"

    s "Yeah. She was talking about Foucault. Something about how institutions shape the people inside them."

    c "Oh, I love Foucault! Well -- I love the IDEA of Foucault. The actual reading makes my brain feel like it's been microwaved."

    s "That's the most relatable thing anyone's ever said about Foucault."

    show charlotte laugh at center

    c "I took a visual culture class last semester and we had to read Discipline and Punish and I think I blacked out for three chapters."

    s "That's actually more chapters than most people get through."

    c "See? Progress!"

    s_thoughts "She's chopping carrots. She's watching me cut the pepper."

    s_thoughts "I can feel her watching."

    c "You might want to -- here, the pieces are a little--"

    s "A little what?"

    c "Big? For stir-fry you want them thinner. So they cook evenly."

    s_thoughts "She reaches for the knife. Her hand hovers over mine."

    menu:
        "Charlotte reaches for the knife."

        "Let her take it.":
            $ charlotte_present += 1

            s_thoughts "I let her take the knife."

            s_thoughts "Her fingers close over mine for a second. Her hand is warm. She guides the knife at an angle."

            show charlotte smile at center

            c "See? Like this. Thin strips. They'll cook faster."

            s_thoughts "She's behind me, almost. Her chin is near my shoulder. Her hair smells like the rosemary from this morning."

            c "And you want to keep your fingers curled. Like a claw. So you don't lose any."

            s "You sound like a cooking show."

            c "I watch a LOT of cooking shows."

            s "I can tell."

            show charlotte happy at center

            s_thoughts "She steps back. Her hand stays on mine for one beat longer than it needs to."

            c "See? Better!"

            s_thoughts "The strips are thinner. They are objectively better."

            s_thoughts "My hand is warm where hers was."

            s_thoughts "I keep cutting. Charlotte goes back to her station. She's humming."

            s_thoughts "The kitchen is warm. The music is soft. Charlotte is humming and I'm cutting peppers and this is the easiest I've felt in weeks."

            s_thoughts "I should probably think about why it's this easy."

            s_thoughts "I don't."

            jump charlotte_ch4_dinner_served

        "\"I've got it.\"":
            $ charlotte_push += 1

            s "I've got it."

            s_thoughts "Charlotte's hand stops mid-reach."

            s_thoughts "Her smile does something. Not a flinch -- a flicker. A quarter-second where the expression resets like a screen refreshing."

            show charlotte smile at center

            c "Of course! Your way works too."

            s_thoughts "She pulls back. The 'of course' is seamless. If I hadn't been looking directly at her face, I would have missed the flicker entirely."

            s_thoughts "I keep cutting. The pieces are uneven. Charlotte doesn't mention it again."

            s "So you took visual culture?"

            c "Mm-hm! It was -- actually, can I tell you something kind of embarrassing?"

            s "Always."

            c "I picked it because I thought it would be easy. Art classes, right? Just look at paintings and have opinions."

            s "And?"

            show charlotte embarrassed at center

            c "And then Professor Morin made us write a twelve-page paper on the male gaze in Renaissance portraiture and I accidentally became really interested in it."

            s "Accidentally?"

            c "I wasn't SUPPOSED to care about Vermeer! I was supposed to get an easy A and fill an elective!"

            s "What happened?"

            show charlotte smile at center

            c "I got a B-plus and a new obsession. Morin said I was 'too focused on what the art was doing instead of what it was.'"

            s "What does that mean?"

            c "I think she meant -- I kept writing about what the paintings were for. Who they served. What purpose they had. Instead of just... looking at them."

            s_thoughts "Charlotte catches herself. Her eyes widen slightly."

            c "Sorry. That's boring. You don't want to hear about my--"

            s "It's not boring."

            s_thoughts "She looks at me."

            s_thoughts "Something passes between us. Something unplanned. Charlotte shared a thing she didn't mean to share and now it's sitting between us on the counter next to the unevenly chopped peppers."

            show charlotte happy at center

            c "...More garlic?"

            s "More garlic."

            s_thoughts "She changes the subject. But the thing she said is still there."

            s_thoughts "Too focused on what the art was doing instead of what it was."

            s_thoughts "I don't say anything. I just file it. Not the old kind, the Katie kind. Just... holding it."

            jump charlotte_ch4_dinner_revealed

    ## ===========================
    ## SCENE 4A: DINNER (Charlotte Serves)
    ## Charlotte plates for Sophia. Warm. Attentive. Too attentive.
    ## Charlotte doesn't eat much. Sophia doesn't notice. (The reader might.)
    ## ===========================

label charlotte_ch4_dinner_served:

    s_thoughts "Charlotte plates the food."

    s_thoughts "I don't mean she puts food on a plate. I mean she PLATES it. Garnish. A little drizzle of something. The vegetables arranged in a Charlotte kind of way."

    show charlotte happy at center

    c "Here!"

    s "Charlotte, this looks like a restaurant."

    c "It's just stir-fry!"

    s "It has a GARNISH."

    c "Cilantro is basically free."

    s_thoughts "We sit at the kitchen table. Just us. The house is upstairs -- Isabella's music leaking through the ceiling, the occasional creak that means Amara is moving between her room and the bathroom."

    c "So tell me about your classes. You're taking -- what, four this semester?"

    s "Three. Communications, the Nova class, and a psych elective I'm already regretting."

    c "Why regretting?"

    s "Because the professor has a goatee and keeps saying 'unpack that.'"

    show charlotte laugh at center

    c "Oh no."

    s "He said it seven times in one lecture. I counted."

    c "You COUNTED."

    s "I'm a noticer. It's a curse."

    show charlotte smile at center

    c "I like that about you."

    s_thoughts "She says it simple. Not loaded. Just a fact."

    s "What do you like about it?"

    c "That you pay attention. Most people don't. They're in a room and they see the room. You see -- I don't know. The thing behind the room."

    s "That sounds like I'm staring through walls."

    c "A little. But in a charming way."

    s_thoughts "She asks about my friends back home. About my mom. She remembers that I mentioned missing my mom's cooking a few weeks ago, and asks if I've called her recently."

    s "How do you remember that?"

    c "You mentioned it! During the -- was it the unpacking? You said your mom makes this pasta thing and you were worried you'd miss it."

    s "I said that once."

    show charlotte smile at center

    c "I pay attention too."

    s_thoughts "She does. She pays attention to me the way I pay attention to everyone. And from the inside, from the receiving end, it feels like being known."

    s_thoughts "Nobody's ever paid attention to me like this. I'm the one who watches. I'm not the one who gets watched."

    s_thoughts "Charlotte reaches across the table to refill my water from the pitcher. She does it without pausing the conversation. Seamless."

    s_thoughts "I look at her plate."

    s_thoughts "She's eaten maybe three bites."

    s_thoughts "The food is beautiful. She made it for me. She's watching me eat it. She's asking me questions about my life with genuine interest and she's barely touched her own plate."

    s_thoughts "I notice. I don't say anything."

    s_thoughts "It's probably nothing."

    c "Oh! I almost forgot. I was thinking we could do a house dinner this weekend. Not me cooking -- everyone cooking. Each person makes a dish."

    s "That's actually a great idea."

    show charlotte happy at center

    c "Right? Isabella can make -- well, Isabella can TRY to make something. And Amara's been making this really good tea. Not a dish but it counts. And Eve --"

    s_thoughts "She pauses on Eve."

    c "Eve said she might bring something."

    s "She said 'might'?"

    c "She said 'I'll think about it.' Which is Eve for 'maybe.'"

    s "Or Eve for 'no.'"

    show charlotte smile at center

    c "I choose to be optimistic!"

    s_thoughts "Charlotte smiles. I smile back. The kitchen is warm. The food is good."

    s_thoughts "I eat her cooking and she watches me eat it and it feels like domestic bliss."

    s_thoughts "It might be that. It might be something that looks exactly like it from the inside."

    s_thoughts "I can't tell."

    stop music fadeout 2.0
    jump charlotte_ch4_study

    ## ===========================
    ## SCENE 4B: DINNER (Charlotte Reveals)
    ## Charlotte talks about herself. Rare. Unplanned.
    ## The art history thing. Something real slips through.
    ## ===========================

label charlotte_ch4_dinner_revealed:

    s_thoughts "Dinner is less polished than Charlotte's usual productions. The stir-fry is good but it's just stir-fry. No garnish. No drizzle. She's slightly off her game."

    s_thoughts "Better."

    show charlotte smile at center

    c "So the Morin class -- I keep going back to it. She assigned this paper about Vermeer. The milk maid painting?"

    s "I think I've seen it."

    c "Everyone's seen it. Woman pouring milk. Beautiful light. Domestic scene. And the argument is -- is Vermeer celebrating this? Is he saying 'look, domestic work is worthy of art'? Or is he saying 'look, this is where women belong'?"

    s "What did you argue?"

    show charlotte embarrassed at center

    c "Okay, don't laugh."

    s "I won't."

    c "I argued that the painting is a room. Like -- the woman is inside the painting the same way she's inside the room. The frame IS the walls. She can't leave. She's beautiful and she's pouring milk and she doesn't know she's being watched."

    s "That's not a bad argument."

    c "Morin said it was 'interesting but underdeveloped.' Which is professor for 'you're onto something but I don't know what.'"

    s "Or professor for 'I didn't expect you to be this smart.'"

    show charlotte surprised at center

    s_thoughts "Charlotte blinks."

    c "That's -- no. She didn't mean--"

    s "Charlotte. You just made an argument about the politics of domestic labor in seventeenth century Dutch painting. Over stir-fry. That's smart."

    show charlotte embarrassed at center

    c "It's just an interest! It's not like -- I'm not like you and Isabella. You two are SMART smart. I'm just--"

    s "You're just what?"

    s_thoughts "She stops. Her mouth opens. Closes."

    c "...I'm just someone who likes looking at paintings."

    s "So was Vermeer."

    show charlotte smile at center

    s_thoughts "She laughs. It's not the big laugh. It's a small, surprised one."

    c "Did you just compare me to Vermeer?"

    s "In the loosest possible sense."

    c "I'm telling everyone you compared me to Vermeer."

    s "Please don't."

    c "Isabella! SOPHIA COMPARED ME TO--"

    s "I will take the stir-fry away."

    show charlotte laugh at center

    c "Fine. Fine! But I'm remembering this."

    s_thoughts "She eats. Actually eats. Not the pushing-food-around thing. She takes a bite and chews and swallows and takes another bite."

    s_thoughts "I don't know if she notices she's doing it. Charlotte eats when she's not thinking about eating. When she's distracted by something real."

    s_thoughts "The Vermeer thing distracted her."

    s_thoughts "I hold that. Quietly."
    
    stop music fadeout 2.0

    jump charlotte_ch4_study

    ## ===========================
    ## SCENE 5: STUDY SESSION IN THE LIVING ROOM
    ## Evening. Sophia's essay. Charlotte's art history paper.
    ## The tea that arrives without asking.
    ## CHOICE 2.
    ## ===========================

label charlotte_ch4_study:

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_morningafter fadein 2.0

    s_thoughts "Thursday evening. The living room."

    s_thoughts "I'm on the floor with my back against the couch because I read better on the floor and I don't know why and I've stopped examining it."

    s_thoughts "Charlotte is on the couch behind me. Laptop open. She's been typing for twenty minutes with a focus I didn't know she had."

    s_thoughts "The house is alive and quiet. Isabella's music bleeds through the ceiling -- something electronic and bass-heavy. Amara is in the armchair with a book, reading at a speed that suggests she's either a genius or pretending."

    s_thoughts "Nobody is talking. It's comfortable."

    s_thoughts "Charlotte gets up."

    show charlotte smile at center with dissolve

    s_thoughts "Five minutes later she comes back with two cups of tea."

    s_thoughts "I didn't ask for tea. She knows how I take it. Splash of milk, one sugar. She sets it on the floor next to me."

    c "Here."

    s "Thanks."

    s_thoughts "That's the whole exchange. She sits back down. Starts typing again."

    s_thoughts "The tea is perfect."

    s_thoughts "I drink it and try to focus on my essay. Nova assigned a paper on 'the container and the message' -- how the medium shapes content. I've written one sentence: 'The container is not neutral.'"

    s_thoughts "I look at Charlotte over my shoulder. She's staring at her screen with the expression of someone wrestling with a paragraph."

    s_thoughts "Her laptop is angled toward me. I can see the top of the document."

    s_thoughts "Art History 302. Something about domestic interiors."

    menu:
        "Charlotte's art history paper is right there."

        "Don't look. Her business.":
            $ charlotte_present += 1

            s_thoughts "I turn back to my essay."

            s_thoughts "Charlotte's work is Charlotte's work. I don't need to read it. I don't need to know what she's writing about. She'll tell me if she wants to."

            s_thoughts "I write my second sentence. 'The frame determines what's inside it.'"

            s_thoughts "That's two sentences. Progress."

            s_thoughts "Amara turns a page. Charlotte types. The house breathes."

            s_thoughts "Forty minutes pass."

            s_thoughts "I look up from my essay. Charlotte is asleep."

            s_thoughts "She's curled on the couch with her laptop sliding toward the edge. Her mouth is slightly open. One hand is still on the keyboard."

            s_thoughts "She looks younger when she sleeps. The brightness is off. The readiness. Whatever engine runs Charlotte's constant awareness of everyone in the room -- it's idling."

            s_thoughts "She's just a girl on a couch."

            s_thoughts "I catch the laptop before it falls. Set it on the coffee table."

            s_thoughts "The document is visible. The title: 'The Room She Built: Domestic Labor and Self-Erasure in Vermeer's Interior Paintings.'"

            s_thoughts "I read the first line. 'The milk maid does not know she is being watched.'"

            s_thoughts "I don't read more."

            s_thoughts "I get the blanket from the hall closet. The one nobody claims but everyone uses. I put it over her."

            s_thoughts "She doesn't wake up. She turns toward the warmth."

            s_thoughts "I go to bed."

            s_thoughts "In the morning, the blanket is folded on the arm of the couch. There's a sticky note on top."

            s_thoughts "'Thank you :)'"

            s_thoughts "Charlotte's smiley face is perfectly round."

            s_thoughts "I put the sticky note in my pocket."

            s_thoughts "I don't examine why."

            jump charlotte_ch4_eve_tension

        "\"What are you writing about?\"":
            $ charlotte_push += 1

            s "Hey. What are you writing?"

            show charlotte surprised at center

            c "Hm? Oh -- just my art history paper. It's nothing."

            s "You've been typing for forty minutes. That's not nothing."

            show charlotte embarrassed at center

            c "It's -- okay. It's about Vermeer. The domestic paintings. I'm arguing that..."

            s_thoughts "She hesitates. Not the Charlotte pause that means she's assembling her words. A different pause. The one that means she's deciding how much to show."

            c "I'm arguing that the women in Vermeer's paintings are trapped inside the frame the same way they're trapped inside the rooms. The painting IS the domestic space. The viewer is looking IN, and the woman doesn't know she's being watched."

            s "That's... Charlotte, that's actually really good."

            show charlotte smile at center

            c "You think?"

            s "The frame as architecture. The painting as a room."

            c "YES. Exactly. And the thing is -- the light. Vermeer's light is always coming from the left. Always through a window. It's beautiful but it's also the only source. The women are illuminated by a light they didn't choose, from a window they can't reach."

            s "Like domestic labor."

            c "Like domestic labor! The work is made beautiful by someone else's gaze. The milk maid doesn't know her pouring is art. She's just pouring milk. Vermeer made it ART. The beauty is imposed, not chosen."

            s_thoughts "Charlotte is talking faster now. Her hands are moving. I've never seen Charlotte talk with her hands."

            c "And the rooms -- they're always small. Tight. Intimate. The viewer feels close to her. But the closeness is surveillance. You're watching someone who doesn't know they're being watched, and the painting makes that feel like tenderness."

            s "Surveillance as tenderness."

            show charlotte happy at center

            c "Surveillance as tenderness! Morin is going to either love that or fail me."

            s "She'll love it."

            c "You don't know Morin."

            s "I know a good argument when I hear one."

            s_thoughts "Charlotte goes quiet. She's looking at me like she didn't expect this. Like she expected me to nod and say 'cool' and let her go back to typing."

            c "Sorry. I was rambling."

            s "You weren't."

            c "I was. I got -- I get carried away with this stuff. It's not interesting to other people."

            s "Are you writing about yourself?"

            show charlotte surprised at center

            s_thoughts "It comes out before I think about it."

            s_thoughts "Charlotte's face does something. Not the flicker. Something deeper."

            show charlotte smile at center

            c "...More tea?"

            s "Charlotte."

            c "Do you want more tea? I'm getting more tea."

            s_thoughts "She's already up. Already moving. The Charlotte escape hatch. The question hangs in the air behind her."

            s_thoughts "She comes back with tea. Two cups. She doesn't mention the Vermeer thing again."

            s_thoughts "But her paper is still open on the laptop."

            s_thoughts "'The Room She Built: Domestic Labor and Self-Erasure in Vermeer's Interior Paintings.'"

            s_thoughts "..."

            s_thoughts "Yeah."

            jump charlotte_ch4_eve_tension

    ## ===========================
    ## SCENE 7: EVE TENSION -- FIRST BEAT
    ## Charlotte's chore chart. Eve's absence from it.
    ## The jaw tighten. The 'of course' that isn't.
    ## ===========================

label charlotte_ch4_eve_tension:

    stop music fadeout 1.5
    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_baddecisions fadein 1.5

    s_thoughts "Friday morning."

    s_thoughts "There's a new thing on the fridge."

    s_thoughts "Color-coded. Laminated. Charlotte's handwriting, which is so neat it looks printed."

    s_thoughts "It's a chore chart."

    s_thoughts "Each person has a color. Charlotte is pink. Isabella is purple. Amara is blue. I'm peach. Eve is green."

    s_thoughts "Charlotte's column has six tasks. Eve's column is blank."

    show charlotte happy at left with dissolve

    c "I figured we should organize things a little! Just so nobody feels like they're doing more than their share."

    s_thoughts "Charlotte is doing more than her share. Charlotte has always been doing more than her share. The chart is a way to pretend the distribution is equal."

    show isabella neutral at right with dissolve

    i "Charlotte, you gave yourself six things."

    c "Some of them are small!"

    i "One of them is 'general kitchen maintenance.' That's not a chore. That's a lifestyle."

    show charlotte smile at left

    c "I like a clean kitchen!"

    s_thoughts "Eve walks in."

    show eve neutral at center with dissolve

    s_thoughts "She stops at the fridge. Looks at the chart. Reads it."

    s_thoughts "Doesn't say anything."

    c "Eve! I left a spot for you on the schedule. Whenever you get a chance!"

    e "I'll think about it."

    c "Of course! No rush."

    s_thoughts "Charlotte's jaw tightens. A fraction of a second. If I blinked, I'd miss it."

    s_thoughts "'Of course' -- said with the same brightness as every other 'of course.' But this one has something behind it. A coiled thing."

    s_thoughts "Eve pours coffee. She doesn't look at the chart again."

    e "Thanks for the coffee."

    c "Always!"
    
    hide eve with dissolve

    s_thoughts "Eve leaves. Charlotte watches her go."

    s_thoughts "The smile is still there. The jaw is still tight."

    show charlotte happy at left

    c "She'll sign up. She just needs time."

    i "Charlotte."

    c "She'll sign up!"

    s_thoughts "Isabella and I make eye contact. Isabella raises one eyebrow."

    s_thoughts "Charlotte is already reorganizing the fridge magnets."

    ## charlotte_eve not tracked yet in Act 1 — this is observational.
    ## Act 2 escalates with real choices about taking sides.

    hide charlotte
    hide isabella
    with dissolve

    stop music fadeout 1.5

    ## ===========================
    ## SCENE 8: CONVENIENCE STORE
    ## Charlotte has a list. Charlotte knows the layout.
    ## Charlotte can't stop making the world more organized.
    ## CHOICE 3.
    ## ===========================

    scene bg conveniencestore with Fade(0.8, 0.3, 0.8)
    play music mus_tuesday fadein 2.0

    s_thoughts "Saturday afternoon. Charlotte asked if I wanted to come to the store."

    s_thoughts "She has a list. A physical list. On paper. With checkboxes."

    show charlotte happy at center with dissolve

    c "Okay. Eggs first. They're in the back left."

    s "You know the layout?"

    c "I've been coming here since move-in. Third week I made a mental map."

    s "You made a mental map of a convenience store."

    c "It's efficient!"

    s_thoughts "She's already moving. I follow."

    s_thoughts "Charlotte in a convenience store is like watching a conductor in front of an orchestra. She moves through the aisles with purpose. She knows where things are. She checks items off the list with a pen she brought specifically for this purpose."

    s_thoughts "She also straightens a tilted can of beans as she passes. She doesn't break stride."

    s "You just fixed that can."

    c "It was crooked."

    s "It bothers you that it was crooked?"

    show charlotte smile at center

    c "Everything has a place. Things are better in their place."

    s_thoughts "She says it like it's about canned goods."

    s_thoughts "We walk the aisles. Charlotte picks up things not on the list -- the olive oil Isabella likes, the tea Amara drinks, a specific brand of granola bar that I mentioned liking once, two weeks ago, in passing."

    s "You remembered the granola bars?"

    c "You said you liked them!"

    s "I said that once. While eating a completely different thing."

    show charlotte happy at center

    c "I listen. Sue me."

    s_thoughts "Charlotte listens the way I watch. With everything."

    s_thoughts "At the checkout, the total is higher than I expected. Charlotte already has her card out."

    menu:
        "Charlotte reaches for the card reader."

        "Let Charlotte pay.":
            $ charlotte_present += 1

            s "You sure?"

            show charlotte smile at center

            c "Of course! My treat."

            s "Charlotte, this is groceries. Groceries aren't a treat."

            c "Groceries are ABSOLUTELY a treat. Do you know how exciting eggs are when you're the one choosing them?"

            s "I don't think anyone has ever been excited about choosing eggs."

            c "You haven't lived."

            s_thoughts "She pays. She carries the heavier bag without being asked."

            s_thoughts "I let her."

            jump charlotte_ch4_walk_carries

        "\"Split it.\"":
            $ charlotte_push += 1

            s "Split it."

            show charlotte surprised at center

            c "Oh -- I don't mind! Really, it's--"

            s "I know you don't mind. Split it."

            s_thoughts "Charlotte hesitates. Her hand is on the card reader. My hand is on mine."

            s_thoughts "For a second she looks -- lost. Like I changed the rules of a game she's been playing for so long she forgot there were rules."

            show charlotte smile at center

            c "...Of course!"

            s_thoughts "She splits it. But the rhythm is off. She's quieter as we leave the store."

            jump charlotte_ch4_walk_surprised

    ## ===========================
    ## SCENE 9A: WALK HOME (Charlotte Carries)
    ## Charlotte carries bags. Charlotte talks about her sister.
    ## Charlotte asks about Sophia's mom. She remembers.
    ## ===========================

label charlotte_ch4_walk_carries:

    scene bg street with dissolve

    show charlotte happy at center with dissolve

    s_thoughts "Charlotte carries the heavier bag on her left shoulder. The lighter one swings from her right hand. She offered to take mine. I said no. She didn't push."

    c "I was thinking about the house dinner. Sunday maybe? Everyone makes a dish."

    s "That could be fun."

    c "Isabella said she'd try to cook something. Which is brave."

    s "Or dangerous."

    show charlotte laugh at center

    c "Both! But that's Isabella."

    s_thoughts "She laughs. The bright one."

    c "My sister called today."

    s "Oh yeah? How is she?"

    c "She's good. She's always good."

    s_thoughts "A beat."

    show charlotte smile at center

    c "I made sure she'd be good."

    s_thoughts "She says it casual. Like it's a small thing. Like 'making sure her sister would be good' is the same as straightening a can on a shelf."

    c "She's sixteen. Starting to think about colleges. She wants to go somewhere close to me, which is--"

    s "Sweet?"

    c "Terrifying."

    s_thoughts "I look at her."

    show charlotte embarrassed at center

    c "Not -- it's not that I don't want her close! I just -- she's been next to me her whole life. It might be good for her to be somewhere new. To figure out who she is without--"

    s_thoughts "She stops herself."

    show charlotte smile at center

    c "Anyway! She's great. How's your mom? You mentioned you hadn't called her in a while."

    s "Charlotte."

    c "Hm?"

    s "How do you remember everything I've ever said?"

    c "I don't remember EVERYTHING."

    s "Name one thing you've forgotten."

    show charlotte happy at center

    c "I can't name what I've forgotten! That's the whole point of forgetting!"

    s "See? You even have a logical defense for it."

    c "I just -- I like knowing things about people. It makes it easier to--"

    s "To what?"

    s_thoughts "She pauses. The bag shifts on her shoulder."

    c "To be useful."

    s_thoughts "Useful."

    s_thoughts "Not 'to be close to people.' Not 'to connect.' Useful."

    s_thoughts "Charlotte carries the bags. Charlotte remembers the details. Charlotte makes the toast. Charlotte is useful."

    s_thoughts "I don't say anything. We walk."

    s_thoughts "She changes the subject to my mom. I tell her we talked last week. She asks what we talked about. I tell her."

    s_thoughts "She remembers all of it. I know she'll remember all of it."

    s_thoughts "I let her carry the heavy bag."

    hide charlotte with dissolve
    stop music fadeout 2.0

    jump charlotte_ch4_nova

    ## ===========================
    ## SCENE 9B: WALK HOME (Charlotte Surprised)
    ## The even split breaks the rhythm.
    ## Charlotte is off-script. The real laugh appears.
    ## ===========================

label charlotte_ch4_walk_surprised:

    scene bg street with dissolve

    show charlotte neutral at center with dissolve

    s_thoughts "The walk home is different."

    s_thoughts "Charlotte is carrying her bag. I'm carrying mine. Equal weight. Equal distribution. And Charlotte doesn't know what to do with the extra hand."

    s_thoughts "She's been quiet since the store. Not upset-quiet. Processing-quiet. Like I moved a piece on a board she didn't know was a game."

    c "I always pay."

    s "What?"

    c "At stores. I always pay. It's not a -- I don't do it to be weird. I just--"

    s "I know."

    c "My mom used to send me to the store when I was -- young. For groceries. I was the one who went. And she'd give me the money and I'd buy what we needed and carry it home and it was MY thing. The shopping. I was good at it."

    s "How young?"

    show charlotte embarrassed at center

    c "Like... ten? Eleven? I don't know. Young enough that the cashier would ask where my mom was."

    s "Charlotte."
    
    show charlotte smile at center

    c "It wasn't -- it sounds worse than it was! She was just -- busy. And I liked doing it. I liked being the one who knew what we needed."

    s_thoughts "She says it with a smile. The smile is doing a lot of work."

    s "What did you need?"

    show charlotte surprised at center

    c "What?"

    s "You said you knew what everyone needed. What did you need?"

    s_thoughts "Charlotte opens her mouth. Closes it."

    s_thoughts "A dog on a leash tangles itself around a fire hydrant across the street. The owner is trying to untangle it. The dog is thrilled. The situation is escalating."

    s_thoughts "Charlotte snorts."

    show charlotte laugh at center

    s_thoughts "Not the bright laugh. Not the Charlotte laugh. A snort. An actual snort-laugh. She covers her mouth."

    c "That was NOT a cute laugh."

    s "It was a great laugh."

    c "It was a FARM ANIMAL laugh."

    s "Do it again."

    show charlotte embarrassed at center

    c "I can't do it again! It just happened!"

    s "Then I'll wait for another dog."

    c "You can't just PRODUCE snort-laughs on command, Sophia. They're a natural phenomenon."

    s "A natural phenomenon."

    show charlotte smile at center

    c "Like -- like weather. You can't make weather."

    s "You're comparing your laugh to weather."

    c "I'm comparing my laugh to a NATURAL AND UNPREDICTABLE ATMOSPHERIC EVENT."

    s_thoughts "She's smiling. Crooked. Unplanned."

    s_thoughts "The dog owner finally frees the dog. The dog immediately tangles itself again."

    s_thoughts "Charlotte doesn't snort this time. But the smile stays. The real one."

    s "For what it's worth."

    c "Hm?"

    s "I like the farm animal laugh."

    show charlotte flooshed at center

    s_thoughts "She doesn't say 'of course.' She doesn't say anything."

    s_thoughts "She shifts her bag to the other shoulder. Our hands bump."

    s_thoughts "Neither of us moves away."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 10: NOVA'S CLASS
    ## Brief. Performance and representation.
    ## "The container changes the thing inside it."
    ## Sophia thinks about Charlotte.
    ## ===========================

label charlotte_ch4_nova:

    scene bg classroom with Fade(0.8, 0.3, 0.8)
    play music mus_nova fadein 2.0

    s_thoughts "Monday. Nova's class. Performance and Representation in Media."

    show professor neutral at center with dissolve

    s_thoughts "Dr. Nova is talking about performance theory. Goffman. The presentation of self in everyday life."

    nova "Today we're talking about Goffman. Front stage. Back stage. The idea that every social interaction is, on some level, a performance."

    s_thoughts "I write that down."

    nova "I'm not going to summarize Goffman for you. You have the reading. What I want to ask is this:"

    s_thoughts "She pauses. Scans the room."

    nova "When does performance become identity? At what point does the mask stop being something you wear and start being your face?"

    s_thoughts "I stop writing."

    nova "And is that a tragedy? Or is that just... what identity is?"

    s_thoughts "She lets the question sit. Nobody answers. Nova doesn't seem to expect an answer."

    s_thoughts "I think about Charlotte."

    nova "For Wednesday. Identify a performance in your own life. Not someone else's. Yours."

    s_thoughts "Class ends. People pack up."

    s_thoughts "I don't move."

    s_thoughts "Nova is at her desk. I hover."

    nova "Ms. Bell."

    s "Can I ask you something? About the assignment."

    nova "It's due Wednesday. That's non-negotiable."

    s "No, I know. I just -- when you say 'identify a performance.' What if someone's performance is so good that they don't know they're performing?"

    show professor happy at center

    nova "Whose performance are we talking about?"

    s "Mine. Hypothetically."

    nova "Mm."

    s_thoughts "She's not buying it. Nova never buys it."

    nova "Here's what I'll say. The paper is about YOUR performance. Not someone else's. If you find yourself writing about another person, ask yourself what that deflection is performing."

    s_thoughts "Ow."

    s "That's not what I--"

    nova "What's your essay about so far?"

    s "The container is not neutral."

    nova "That's one sentence."

    s "It's a good sentence."

    show professor neutral at center

    nova "What's the container made of?"

    s_thoughts "I open my mouth."

    s_thoughts "I think about Charlotte again."

    s "...I'm working on it."

    nova "Mm."

    s_thoughts "She starts packing her bag. Conversation over."

    nova "Sophia. One thing."

    s "Yeah?"

    nova "The most interesting performances are the ones the audience enjoys. That's what makes them hard to see."

    s_thoughts "She leaves."

    s_thoughts "I sit in the empty classroom."

    s_thoughts "The board says: 'When does the mask become the face?'"

    s_thoughts "I don't take a picture of it this time."

    s_thoughts "I don't need to. It's already stuck."

    hide professor with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 11: HOUSE DINNER PREP (Ensemble)
    ## Charlotte organizing. Isabella failing. Amara precise.
    ## Eve arrives late with a store-bought pie.
    ## Charlotte's face does the thing.
    ## CHOICE 4.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_fivepeople fadein 2.0

    s_thoughts "Sunday. The house dinner."

    s_thoughts "Charlotte has been planning this since Wednesday. There are notes on the fridge. There's a timeline. The timeline has color-coded sections."

    s_thoughts "The kitchen is chaos."

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte is at the center of it. She's supposed to be making just her dish -- a salad, allegedly -- but she's also prepping Isabella's mise en place, re-organizing the spice rack, and monitoring the oven temperature."

    show isabella neutral at right with dissolve

    i "Charlotte, I told you I've got this."

    c "You do! You absolutely do! I'm just -- the onions need to be--"

    i "I KNOW about the onions, Charlotte."

    c "Of course!"

    s_thoughts "Isabella is making pasta. 'From scratch,' she said, which means she watched one YouTube video and bought flour. The dough looks like a crime scene."

    i "This is SUPPOSED to look like this."

    s "Is it?"

    i "In Italy, this would be considered rustic."

    s "In Italy, they would consider this grounds for deportation."

    show isabella embarrassed at right

    i "You're supposed to be on my side."

    s "I'm on the side of edible food."

    show charlotte smile at left

    s_thoughts "Charlotte's hands are twitching. She wants to fix Isabella's pasta so badly her whole body is vibrating with it."

    c "I could just -- if you want, I could--"
    
    show isabella neutral at right

    i "Charlotte. No."

    c "Okay! Okay."

    show amara neutral at center with dissolve

    s_thoughts "Amara is at the end of the counter. She's making rice. Just rice. Perfectly measured, perfectly timed, in a pot she washed before and after measuring the water."

    s_thoughts "It's going to be the best thing at the table and nobody will notice because it's rice."

    a "The oven is beeping."

    c "Oh! That's my -- one second--"

    s_thoughts "Charlotte rushes to the oven. Then back to the salad. Then checks on Isabella's sauce. Then re-checks the oven."

    s_thoughts "She's doing four things. She's doing four things and pretending she's doing one thing."

    s_thoughts "The door opens. Footsteps."

    hide amara
    show eve neutral at center
    with dissolve

    s_thoughts "Eve walks in carrying a pie."

    s_thoughts "A store-bought pie. In the plastic shell. Price tag still on it."

    e "I brought dessert."

    s_thoughts "Charlotte's face does the thing."

    s_thoughts "It happens fast. A flash of something -- disappointment? Frustration? Relief that Eve showed up at all? -- before the smile snaps back like a rubber band."

    show charlotte happy at left

    c "That looks wonderful!"

    s_thoughts "Eve sets the pie on the counter. She doesn't stay. She drifts toward the hallway."

    e "Let me know when we're eating."

    hide eve with dissolve
    
    s_thoughts "She's gone."

    s_thoughts "Charlotte stares at the pie. Her hands are still for the first time in an hour."

    c "Okay! So we've got pasta, salad, rice, and pie. That's a meal!"

    i "That's barely a meal."

    c "It's a COLLABORATIVE meal. That's what matters."

    s_thoughts "Charlotte is smiling. Charlotte is managing. Charlotte is doing three people's jobs."

    menu:
        "Charlotte is doing too much."

        "Help her. Start setting the table.":
            $ charlotte_present += 1

            s_thoughts "I start setting the table."

            c "Oh! You don't have to--"

            s "I want to."

            show charlotte smile at left

            s_thoughts "Charlotte looks at me. The smile softens."

            c "...Thank you."

            s "Where are the good plates? The ones you hide from Isabella?"

            show charlotte laugh at left

            c "They're not HIDDEN, they're PRESERVED. Top shelf. Behind the cereal."
            
            show isabella annoyed at right

            i "I KNEW you had secret plates!"

            c "They're not secret! They're for occasions!"

            i "This is an occasion!"

            c "This is EXACTLY an occasion!"
            
            show isabella neutral at right

            s_thoughts "I get the plates. I set the table. Charlotte watches me do it and something in her body relaxes."

            s_thoughts "She goes back to the salad. Her movements are slower now. Less frantic."

            s_thoughts "I set five plates."

            jump charlotte_ch4_dinner_perfect

        "\"Charlotte. Sit down.\"":
            $ charlotte_push += 1

            s "Charlotte. Sit down."

            show charlotte surprised at left

            s_thoughts "She freezes. The salad tongs are mid-air."

            c "I'm fine! I just want everything to be--"

            s "Sit. Down."

            s_thoughts "The kitchen goes quiet. Isabella looks up from her pasta crime. Amara doesn't look up but she's listening."

            show charlotte neutral at left

            s_thoughts "Charlotte sets the tongs down. She sits on the stool by the counter."

            s_thoughts "She doesn't know what to do with her hands."

            s_thoughts "They hover. They reach for the dish towel. They pull back. They settle in her lap. They clasp."

            c "The salad isn't--"

            s "I'll finish the salad."

            c "But the dressing needs--"

            s "Charlotte."

            show charlotte sad at left

            s_thoughts "She stops."

            s_thoughts "She sits there. On the stool. In the middle of the kitchen she runs. And she looks -- I don't know. Small. Like the competence was a prosthetic and someone took it away."

            i "...Hey, Charlotte?"

            show charlotte neutral at left

            c "Yeah?"

            i "Your salad dressing is really good. What's in it?"

            s_thoughts "Charlotte blinks. Then, slowly, her face rebuilds."

            show charlotte smile at left

            c "Oh! It's just olive oil, lemon, dijon, a little honey--"

            i "A LITTLE honey? Charlotte, you put a little honey in everything."

            c "Honey is a VERSATILE ingredient!"

            s_thoughts "She takes a grape from the salad bowl. Eats it."

            s_thoughts "I don't think she notices she did it."

            jump charlotte_ch4_dinner_messy

    ## ===========================
    ## SCENE 12A: THE PERFECT DINNER
    ## Charlotte radiant. Toast. The shoulder touch.
    ## ===========================

label charlotte_ch4_dinner_perfect:

    scene bg kitchen with dissolve

    show charlotte happy at left
    show isabella smile at right
    show amara neutral at center
    with dissolve

    s_thoughts "Dinner is beautiful."

    s_thoughts "Not perfect-beautiful. House-beautiful. Isabella's pasta is overcooked but she owns it. Amara's rice is flawless. Charlotte's salad has edible flowers because Charlotte found edible flowers in the garden she apparently maintains in secret."

    s_thoughts "Eve is at the table. She's eating the pie she brought. She doesn't say much but she's here."

    c "I just want to say -- I'm really glad we're all here."

    i "Charlotte is about to make a toast."

    c "It's not a TOAST. It's a statement."

    i "She's toasting."

    c "I'm not toasting!"

    s "You're a little bit toasting."

    show charlotte embarrassed at left

    c "OKAY. Fine. A small toast."

    s_thoughts "She raises her glass. Water."

    c "To the house. And to -- to all of us being here. In this weird, creaky house. Together."

    i "To the Bad Decision House."

    a "BDH."

    s_thoughts "We clink glasses. Charlotte is radiant. She's in her element -- everyone at the table, everyone fed, everyone present."

    s_thoughts "Isabella says Charlotte is 'hosting her own life.' Charlotte laughs. The 'of course' laugh."

    s_thoughts "Later. Clearing up."

    hide isabella
    hide amara
    with dissolve

    show charlotte smile at center with move

    s_thoughts "Charlotte washes dishes. I dry. We don't talk about it. We just fall into it."

    s_thoughts "Our shoulders touch."

    s_thoughts "Charlotte doesn't move away."

    s_thoughts "Neither do I."

    c "Tonight was nice."

    s "Yeah."

    c "I like when everyone's here."

    s "I know you do."

    s_thoughts "Something crosses Charlotte's face. She wasn't expecting to be seen in that sentence."

    s_thoughts "She recovers. Fast."

    show charlotte happy at center

    c "More dishes?"

    s "More dishes."

    s_thoughts "We wash dishes. Our shoulders touch. The kitchen is warm."

    s_thoughts "I don't think about what it means. I just let it happen."

    hide charlotte with dissolve
    stop music fadeout 2.0

    jump charlotte_ch4_porch

    ## ===========================
    ## SCENE 12B: THE MESSY DINNER
    ## Charlotte sat down. The food is imperfect. Charlotte eats.
    ## ===========================

label charlotte_ch4_dinner_messy:

    scene bg kitchen with dissolve

    show charlotte smile at left
    show isabella embarrassed at right
    with dissolve

    s_thoughts "Dinner is chaos."

    s_thoughts "Isabella's pasta is a disaster. She serves it with pride."

    i "I call it deconstructed."

    s "You call it that because you can't call it pasta."

    i "It's CONCEPTUAL pasta."

    show amara neutral at center with dissolve

    s_thoughts "Amara ate her rice before everyone sat down."

    a "I was hungry."

    s "Amara, we were literally about to sit down."

    a "Hungry."

    s_thoughts "Eve is at the table. Eating pie. Her pie is actually really good."

    c "Eve, this pie is really good."

    s_thoughts "Charlotte says it and the surprise in her own voice is the most honest thing she's said all day."

    show charlotte surprised at left

    c "Like -- actually really good. Where did you get it?"

    e "The bakery on 5th."

    c "I didn't know they made pie."

    e "They make lots of things."

    s_thoughts "Eve says it flat. But there's a flicker of something. Almost a smile."

    s_thoughts "Charlotte ate."

    s_thoughts "Actually ate. I watched her take a second helping of Isabella's disastrous pasta and look vaguely confused about it, like her own appetite surprised her."

    show charlotte happy at left

    s_thoughts "The table is loud. Isabella is defending her pasta. Amara is eating another bowl of rice. Eve is cutting pie into precise slices."

    s_thoughts "Charlotte is in the middle of it. But not as the conductor. Just as a person at a table."

    s_thoughts "She catches my eye across the mess."

    s_thoughts "Smiles. Back stage smile."

    s_thoughts "It's the best she's looked all week."

    hide charlotte
    hide isabella
    hide amara
    with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 13: THE PORCH (Night)
    ## After dinner. Charlotte asks a real question.
    ## CHOICE 5: The most important binary in Act 1.
    ## ===========================

label charlotte_ch4_porch:

    scene bg porch night with Fade(0.8, 0.3, 0.8)
    play music mus_2am fadein 3.0

    s_thoughts "Night."

    s_thoughts "The house is settling. That particular sound a house makes when everyone is winding down -- water in the pipes, a door closing softly, Isabella's music fading out."

    s_thoughts "Charlotte and I are on the porch."

    s_thoughts "She suggested it. 'Get some air?' And I said yes because of course I said yes."

    show charlotte neutral at center with dissolve

    s_thoughts "She's quieter than usual. The dinner took something out of her. Not energy. Something else."

    s_thoughts "It's like watching a machine idle. Charlotte without the brightness is Charlotte at rest, and she doesn't seem to know how to be at rest."

    c "The stars are out."

    s "Yeah."

    c "I used to know the constellations. My sister and I would look at them from the backyard. She'd point and I'd name them."

    s "Which ones?"

    c "Orion. Always Orion. Because it's the easy one."

    s "The easy one?"

    c "Three in a row. Anyone can find it."

    s_thoughts "She's looking up. Not at me."

    c "Sophia."

    s "Yeah?"

    c "Do you think I try too hard?"

    s_thoughts "The question is so quiet I almost miss it."

    s_thoughts "Charlotte isn't looking at me. She's looking at the sky."

    s_thoughts "The question isn't casual. It's not a 'haha, I'm so Type A' self-deprecation. It's real."
    
    s_thoughts "She's asking because she doesn't know. She's asking because she needs someone to tell her."

    menu:
        "\"I think you care a lot. There's nothing wrong with that.\"":
            $ charlotte_push += 1

            s "I think you care a lot. There's nothing wrong with that."

            show charlotte smile at center

            s_thoughts "Charlotte exhales. Something in her shoulders drops."

            c "Yeah?"

            s "Yeah. The dinner, the chart, the -- all of it. You care about this house. About us. That's not trying too hard. That's just... you."

            c "It's just me."

            s "It's just you."

            s_thoughts "She looks at me. The mask slides back on -- I can almost see it happen. I gave her permission."

            show charlotte happy at center

            c "Thanks, Sophia."

            s "For what?"

            c "For saying that. Nobody's ever -- I mean, people say 'you're so nice' and 'you do so much' but nobody ever says 'there's nothing wrong with it.' Usually there's a 'but' coming."

            s "No but."

            c "No but."

            s_thoughts "She's looking at me."

            s_thoughts "The porch light is doing something to her face. Making the angles softer. Making her eyes bigger."

            s_thoughts "Charlotte leans in."
            
            s_thoughts "I can feel her breath. My chest is doing something architectural."
            
            s_thoughts "Our eyes lock then close and then--"

            s_thoughts "She kisses me."

            s_thoughts "On the porch. Under the light. With the house behind us and the stars above and it's exactly the kind of kiss that Charlotte would plan except I don't think she planned it."

            s_thoughts "Her lips are warm. She tastes like the mint tea she had after dinner."

            s_thoughts "She pulls back."

            show charlotte flooshed at center

            c "I -- sorry. Was that--"

            s "Yeah."

            c "Yeah as in 'yeah that was okay' or yeah as in--"

            s "Yeah as in do it again."

            s_thoughts "She does it again."

            s_thoughts "This one is longer. Her hand comes up to the side of my face. She's gentle. Of course she's gentle."

            s_thoughts "I stop thinking."

            s_thoughts "I just kiss Charlotte on the porch and it's easy."

            s_thoughts "It's so easy."
            
            hide charlotte with dissolve
            
            scene bg sophiaroom with dissolve

            s_thoughts "Later. In my room. Staring at the ceiling."

            s_thoughts "My lips still feel warm."

            s_thoughts "I replay the kiss seven times. Each time it's perfect."

            s_thoughts "Each time it's exactly what I needed."

            s_thoughts "That thought should probably concern me more than it does."

            $ charlotte_kissed_porch = True

            stop music fadeout 3.0
            jump charlotte_ch4_isabella_seed

        "Stay quiet. Sit with the question.":
            $ charlotte_present += 1

            s_thoughts "I don't answer."

            s_thoughts "Not because I don't want to. Because the question deserves more than a quick reassurance."

            s_thoughts "Charlotte asked a real question. The least I can do is let it be real."

            s_thoughts "The silence stretches. Five seconds. Ten."

            s_thoughts "Charlotte doesn't fill it. That's the remarkable thing. Charlotte ALWAYS fills silence. Silence is a gap and Charlotte fills gaps. But this time she's just waiting."

            s_thoughts "She's waiting because she actually wants to know."

            show charlotte sad at center

            s_thoughts "Her eyes get a little wet. She blinks. Once. Hard."

            c "Sorry. I don't know where that came from."

            s "Don't apologize."

            c "Of course. Sorry. I mean--"

            s_thoughts "She laughs."

            s_thoughts "Something cracked and small and real."

            show charlotte neutral at center

            c "I just said 'of course sorry I mean' like that's a sentence."

            s "It's a very Charlotte sentence."

            c "It is, isn't it?"

            s_thoughts "We sit there. The porch. The dark. The question still hanging."

            s "Charlotte."

            c "Mm."

            s "I don't know if you try too hard. I think you do a lot. I think sometimes you do things before anyone asks you to."

            c "Is that bad?"

            s "I think it means nobody's ever had a chance to ask."

            show charlotte sad at center

            s_thoughts "She doesn't say anything."

            s_thoughts "The silence is different this time. Not Charlotte-performing-silence. Just silence."

            c "Goodnight, Sophia."

            s "Goodnight, Charlotte."

            s_thoughts "She goes inside. The porch light clicks off."

            s_thoughts "In the morning, Charlotte is brighter than usual. She's made muffins. There are MUFFINS."

            s_thoughts "She's compensating."

            s_thoughts "I know she's compensating."

            s_thoughts "The muffins are really good."

            $ charlotte_kissed_porch = False

            stop music fadeout 3.0
            jump charlotte_ch4_isabella_seed

    ## ===========================
    ## SCENE 14: ISABELLA -- THE REVEAL SEED
    ## Isabella says something about Charlotte that has edges.
    ## The crush. The thing that happened before Sophia arrived.
    ## CHOICE 6.
    ## ===========================

label charlotte_ch4_isabella_seed:

    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_morningafter fadein 2.0

    s_thoughts "Next afternoon. Charlotte's not home -- she mentioned a study group."

    s_thoughts "Isabella is at the kitchen table with her laptop. She's got three tabs open and a look on her face like the code personally insulted her."

    show isabella neutral at center with dissolve

    i "This function is GASLIGHTING me."

    s "Functions can't gaslight you, Isabella."

    i "This one is. It returns the right value in isolation and the wrong value in context. That's gaslighting."

    s "That's a scoping issue."

    show isabella surprised at center

    i "Since when do you know about scoping issues?"

    s "You've explained it to me like four times."

    i "And you LISTENED? That's the most romantic thing anyone's ever done for me."

    s_thoughts "She says 'romantic' and her eyes flicker. Like she heard herself say it."
    
    s_thoughts "I file it and don't respond."

    show isabella neutral at center

    s_thoughts "She goes back to coding."

    s_thoughts "I make coffee. The kitchen is quiet."

    s "Can I ask you something?"

    i "If it's about the faucet, I maintain that it's fine."

    s "It's about Charlotte."

    s_thoughts "Isabella stops typing."

    show isabella neutral at center

    i "What about Charlotte?"

    s "How's she -- I mean. You've lived with her longer. Is she always like this?"

    i "Like what?"

    s "Like... on. Always on. Always cooking and planning and fixing things."

    s_thoughts "Isabella leans back in her chair."

    show isabella sad at center

    i "She does that, you know. Makes you feel like you're the only person in the room. She's... really good at that."

    s_thoughts "There's something in Isabella's voice."

    i "She knows your coffee order before you tell her. She remembers the thing you mentioned once. She shows up with toast."

    s "You know about the toast?"

    show isabella smile at center

    i "Charlotte has a toast PROTOCOL. Anyone has a bad night, the toast appears. It's like a natural disaster response but for feelings."

    s_thoughts "She's joking. But the joke has an undertow."

    i "Just..."

    s "Just what?"
    
    show isabella sad at center

    i "She's really good at making you feel like you're getting everything. Just make sure you actually are."

    s_thoughts "It sounds like advice."

    s_thoughts "It sounds like a warning."

    s_thoughts "It sounds like someone who knows."

    menu:
        "Isabella's tone has edges."

        "\"You sound like you're speaking from experience.\"":
            $ charlotte_push += 1
            $ persistent.pushed_izzy_visible = True

            s "You sound like you're speaking from experience."

            show isabella embarrassed at center

            s_thoughts "Isabella's hands still on the keyboard."

            i "I -- we've just lived together for a while. You know?"

            s "Isabella."

            i "I know how she works. That's all. She's my best friend. I know how she operates."

            s "That's not what I asked."

            show isabella sad at center

            s_thoughts "She looks at the laptop. The code. The blinking cursor."

            i "Charlotte is -- Charlotte makes it easy. That's not a warning, it's just a fact."

            s "Isabella."

            i "I'm fine. It was -- it was a long time ago. Like, last semester long ago. Before you moved in."

            s "You liked her."

            show isabella neutral at center

            i "I liked the way she made me feel. Which is -- yeah. I liked her. I got over it."

            s "Did you?"

            i "I got over the active part. The residual part is none of your business."

            s_thoughts "She says it with a half-smile. It's not mean. It's a boundary."

            i "Look, I'm not telling you not to -- whatever you're doing with Charlotte. She's good. She's genuine. I think. I just -- it's hard to know if it's Charlotte being Charlotte for Charlotte or Charlotte being Charlotte for you."

            s_thoughts "I sit with that."

            i "And by the time I figured out I couldn't tell, I'd already decided it didn't matter. Which is -- that's probably not the answer you wanted."

            s "There wasn't a question."

            show isabella smile at center

            i "There's always a question with you, Sophia."

            s_thoughts "She goes back to coding. The conversation is over."

            s_thoughts "But the thing she said stays."

            s_thoughts "Charlotte being Charlotte for Charlotte."
            
            s_thoughts "Or Charlotte being Charlotte for me."

            jump charlotte_ch4_act1_end

        "Let it go.":
            $ charlotte_present += 1

            s_thoughts "I don't push."

            s_thoughts "Isabella said what she was going to say. Pushing her for more would be the old Sophia -- the filer, the observer, the one who pries open other people's drawers."

            s_thoughts "I let it sit."

            s "Thanks, Isabella."

            show isabella surprised at center

            i "For what?"

            s "For the heads up."

            i "It wasn't a heads up. It was just -- I want you to be happy. Both of you. I want you both to be happy."

            s_thoughts "She says 'both of you' with a careful neutrality that costs her something."
            
            s_thoughts "It's the 'I want you both to be happy' that you can only say when you didn't get to be happy in the way you wanted to be happy."

            show isabella smile at center

            i "Now can you please look at this function and tell me if I'm insane?"

            s "You're insane."

            i "I mean specifically about the scoping issue."

            s "I'm not a programmer. You know this."

            i "You know about scoping issues! You said it yourself!"

            s "I know the WORD. I don't know the thing."

            i "That's literally the same as knowing the thing."

            s "It is absolutely not."

            s_thoughts "She argues. I argue back. Normal."

            s_thoughts "But underneath it, her face in that moment -- when she said Charlotte makes you feel like you're the only person in the room."

            s_thoughts "She wasn't warning me about Charlotte."

            s_thoughts "She was remembering what it felt like."

            jump charlotte_ch4_act1_end

    ## ===========================
    ## ACT 1 END
    ## The honeymoon's first half. Everything warm.
    ## Everything easy. Everything too easy.
    ## ===========================

label charlotte_ch4_act1_end:

    hide isabella with dissolve
    stop music fadeout 3.0

    scene black with Fade(1.0, 0.5, 1.0)

    if charlotte_kissed_porch:
        s_thoughts "She kissed me on the porch. Under the light. And I said 'do it again' and she did."
        s_thoughts "It was easy."
        s_thoughts "It was so easy."
    else:
        s_thoughts "She asked me if she tries too hard. On the porch. In the dark. And I let the question sit there and her eyes got wet and she went inside and made muffins in the morning."
        s_thoughts "She says 'of course' the way other people breathe."

    s_thoughts "I am falling for her."

    s_thoughts "I am falling for her and I can't tell which Charlotte I'm falling for."

    s_thoughts "The terrifying thing is that Charlotte might not know either."

    s_thoughts "The more terrifying thing is that it might feel exactly the same either way."

    ## END OF ACT 1

    jump charlotte_ch4_act2

## ===========================
## ===========================
## ACT 2: "THE DRIFT"
## The relationship formalizes. The warmth continues.
## The seams start showing. Charlotte's "of course" gets louder.
## ===========================
## ===========================

label charlotte_ch4_act2:

    ## ===========================
    ## SCENE 15: MORNING ROUTINES
    ## Show synced schedules through CHANGED DETAILS.
    ## Charlotte's mug next to Sophia's. Two place settings already out.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_charlotte fadein 3.0

    s_thoughts "Something shifted."

    s_thoughts "I don't know when. There wasn't a conversation. There wasn't a moment where Charlotte said 'let me reorganize my morning around you' and I said 'yes please.'"

    s_thoughts "It just happened."

    if charlotte_kissed_porch:
        s_thoughts "Since the porch -- since her lips and the mint tea and the 'do it again' -- the house has rearranged itself. Or Charlotte rearranged it. Same thing."
    else:
        s_thoughts "Since the porch -- since the question and the wet eyes and the muffins that appeared like an apology for feeling something -- the house has rearranged itself. Or Charlotte rearranged it. Same thing."

    s_thoughts "Two mugs on the counter. Mine and hers. Already out. The chipped one and the one with the sunflower. Side by side."

    s_thoughts "Two place settings at the table. Not five. Two. The others will add their own when they come down. But these two are already here."

    s_thoughts "Charlotte's phone alarm goes off at 6:45. Mine goes off at 7:15. By the time I'm downstairs, the coffee is made and she's reading something on her laptop and she looks up like she's been waiting but isn't going to say so."

    show charlotte smile at center with dissolve

    c "Morning!"

    s_thoughts "Same brightness. Same warmth. But now there's something underneath it. A claim."

    s "Morning. Is that the good coffee?"

    c "I used the last of Eve's beans. Don't tell her."

    s "You're going to get us both killed."

    show charlotte laugh at center

    c "She'll never know! I'm replacing them today."

    s_thoughts "She will. She'll replace them with the exact same brand. She probably has a backup bag somewhere."

    s_thoughts "I sit down. The coffee is perfect. The toast is already in the toaster. She didn't ask if I wanted toast."

    s_thoughts "She knew."

    s_thoughts "Two weeks ago that would have felt like being seen. Today it feels like being predicted."

    s_thoughts "I don't know when those became different things."

    show charlotte happy at center

    c "I moved your jacket, by the way. It was on the banister and I hung it in the coat closet. I hope that's okay."

    s "You moved my jacket?"

    c "It was going to fall! The banister is curved and jackets slide off. I've lost two scarves to that banister."

    s "Charlotte, I put it there on purpose."

    show charlotte surprised at center

    c "On the banister? On purpose?"

    s "I put it there because I'm going to grab it on my way out."

    c "Oh! Of course. I'll -- I can move it back."

    s "It's fine."

    c "Are you sure? I didn't mean to--"

    s "Charlotte. It's a jacket."

    show charlotte smile at center

    c "Right. Of course!"

    s_thoughts "The second 'of course' in ninety seconds. I'm counting now."

    s_thoughts "She gets up to check the toast. Her hand brushes my shoulder as she passes. Automatic. A gesture that's become a habit that's become a fact."

    s_thoughts "The toast pops. She butters it. She knows how much butter."

    s_thoughts "She sets it in front of me and sits back down and picks up her coffee and everything is warm and easy and I have a thought I don't want to have."

    s_thoughts "Charlotte didn't ask if I wanted toast."

    s_thoughts "Charlotte never asks."

    s_thoughts "Charlotte just knows."

    s_thoughts "And knowing is supposed to be the romantic part."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 16: LILA'S REACTION
    ## Lila clocks the relationship.
    ## "Things don't just happen, Sophia. She MADE it happen."
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)
    play music mus_campus fadein 2.0

    s_thoughts "Campus. Lila. The bench."

    s_thoughts "She's got a smoothie the color of a traffic cone and she's drinking it with the intensity of someone training for combat."

    show lila happy at center with dissolve

    l "So?"

    s "So what?"

    l "SO. You and Toast Girl. What's the status? Are you a thing? Are you a situation? Are you a 'it's complicated' which is code for 'we're a thing but I'm being weird about it'?"

    s "We're... a thing. I think."

    show lila shocked at center

    l "You THINK?"

    s "We haven't had The Talk. But we've had the -- the mornings. The coffee. She makes me toast."

    l "She makes you toast EVERY MORNING?"

    s "She makes me toast every morning."

    l "Sophia. That's not dating. That's a subscription service."

    s "That's not--"

    l "You're enrolled in Charlotte's Toast Plan. Premium tier. Butter included."

    s "Lila."

    show lila happy at center

    l "I'm kidding. Mostly."

    s_thoughts "She takes a long pull of the smoothie. The straw makes the sound of a drain dying."

    l "Okay. Real talk. You're happy?"

    s "Yeah."

    l "Like genuinely happy, or like 'someone is being nice to me and I've forgotten what that feels like so I'm calling it happy'?"

    s "...The first one?"

    show lila annoyed at center

    l "That question mark is doing a LOT of work."

    s "I am happy. She's -- Lila, she's good. She's kind. She remembers things. She shows up."

    l "All true."

    s "So what's the problem?"

    l "I didn't say there was a problem."

    s "Your face is saying there's a problem."

    show lila happy at center

    l "My face is saying I want more smoothie."

    s "Lila."

    l "Okay. Okay!"

    s_thoughts "She puts the smoothie down."

    show lila annoyed at center

    l "When did Charlotte last say no to you?"

    s "What?"

    l "No. Nope. Nah. Can't do it. Don't want to. When did she last say any version of that?"

    s_thoughts "I open my mouth."

    s_thoughts "I close it."

    l "That's what I thought."

    s "That doesn't mean--"

    l "Has she ever picked the restaurant? Picked the movie? Said 'I want to do THIS' instead of 'what do you want to do?'"

    s "She picked the -- she suggested we go to the--"

    l "Did she suggest it because she wanted to go, or because she thought you'd want to go?"

    s_thoughts "I don't answer."

    l "Things don't just happen, Soph. The mornings. The coffee. The toast. Someone made that happen. Which one of you was it?"

    s "She's just -- she's a caring person. That's who she is."

    l "I know. That's what worries me."

    s "What does that even mean?"

    show lila happy at center

    l "It means -- okay. My sister. Remember my sister?"

    s "The Lila Special."

    l "The Lila Special. She's still doing it. She dyed her hair blonde. She joined the debate team because I was on the debate team in high school."

    s "You were on the debate team?"

    l "For three weeks. I got kicked off for 'excessive personal attacks.' The POINT is -- she's building herself around me. And I'm terrified because she doesn't know who she is WITHOUT me to copy."

    s "And you think Charlotte is--"

    l "I think Charlotte is building herself around you. And around Isabella. And around the house. And around everyone she's ever met. And at some point there's no Charlotte left in the middle."

    s_thoughts "The smoothie sits between us."

    s "That's not the same."

    l "Maybe not."

    s "Charlotte has a whole life. She has her art history thing. She has opinions."

    l "What's her favorite movie?"

    s "..."

    l "What does she do for FUN? Not for the house. Not for you. For her."

    s "She -- she bakes."

    l "For who?"

    s_thoughts "For the house. For everyone. For me."

    s "..."

    show lila annoyed at center

    l "I'm not saying she's a bad person. I'm saying you should be the one watching for once."

    s "I AM watching. That's what I do."

    l "No, babe. You're being WATCHED. Charlotte is watching you and you're so busy enjoying being watched that you stopped doing the thing. She's got your number and you handed it to her."

    s_thoughts "That lands."

    s_thoughts "I don't want it to land."

    show lila happy at center

    l "I could be wrong. I'm probably wrong. I give terrible advice."

    s "You give terrible advice."

    l "Go home. Kiss your toast girl. Be happy. But ask her what movie she wants to watch and don't let her say 'whatever you want.'"

    s "Okay."

    l "And text me."

    s "Okay."

    l "And tell her she owes me a toast for introducing you to each other. By which I mean existing on the same campus. Same difference, really."

    s_thoughts "I laugh. It doesn't quite clear the thing Lila put in my chest."

    s_thoughts "When did Charlotte last say no?"

    s_thoughts "When DID Charlotte last say NO?"

    hide lila with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 17: CHARLOTTE'S BEDROOM
    ## Sophia sees Charlotte's room for the first time.
    ## It's disappointingly, revealingly NORMAL.
    ## ===========================

    scene bg charlottebedroom with Fade(0.8, 0.3, 0.8)
    play music mus_morningafter fadein 2.0

    s_thoughts "I've been in the house for a while now. I've been in everyone's room."

    s_thoughts "Amara's room is Amara: sparse, precise, a single plant on the windowsill that's thriving because Amara probably has a watering schedule calibrated to the minute."

    s_thoughts "Isabella's room is Isabella: stickers on the laptop, cables everywhere, three empty energy drink cans forming what she insists is 'an art installation.'"

    s_thoughts "Eve's room is -- I've never been in Eve's room. Nobody's been in Eve's room."

    s_thoughts "Charlotte's door has always been open. That's the thing. It's always open and she's never in it."

    s_thoughts "She's in the kitchen. The living room. The common spaces. Charlotte exists in shared space. Her room is where she sleeps."

    s_thoughts "Today she invited me in."

    show charlotte smile at center with dissolve

    c "Sorry about the -- it's not very--"

    s "Charlotte."

    s_thoughts "The room is normal."

    s_thoughts "I don't know what I expected. Some kind of reveal. A curated aesthetic. Pinterest boards. Fairy lights. Color-coordinated throw pillows. The Charlotte Experience: Bedroom Edition."

    s_thoughts "Instead it's just a room. Bed. Desk. Closet. A few family photos on the wall. Scrapbook supplies are in a clear box on the shelf, organized but not displayed."

    s_thoughts "The bed is made. Of course the bed is made. But it's made simply -- not the hotel-corners thing, just pulled up and smoothed."

    s_thoughts "There are no decorations. No motivational quotes. No personality."

    s_thoughts "The kitchen has personality. The living room has personality. The chore chart has more personality than this room."

    c "I know it's kind of boring."

    s "It's not boring."

    c "It IS boring. I keep meaning to decorate but I never -- there's always something else to do."

    s "Something in the kitchen."

    show charlotte embarrassed at center

    c "Something EVERYWHERE. The house is big! Things need doing!"

    s "Charlotte, when was the last time you were in this room for longer than sleeping?"

    s_thoughts "She thinks. Actually thinks."

    show charlotte neutral at center

    c "...I read in here sometimes. At night."

    s "When?"

    c "When everyone else is asleep."

    s_thoughts "Charlotte's room is the room of someone who doesn't exist when nobody's watching."

    s_thoughts "No -- that's not fair. Charlotte exists. She just exists OUT THERE. In the spaces between people. In the kitchen at 7 AM and the living room at 9 PM and the porch when someone needs air."

    s_thoughts "This room is what's left over."

    s_thoughts "I look at the photos. Charlotte and her sister. Charlotte and what must be her mom -- similar eyes, similar smile. A photo from what looks like a school event. Charlotte's smile is the same in every picture."

    s_thoughts "Exactly the same."

    c "That's my sister. Sophie."

    s "Your sister's name is Sophie?"

    show charlotte happy at center

    c "I KNOW. When I met you I almost died. 'Hi, I'm Sophia.' I was like -- universe, really? REALLY?"

    s "Charlotte."

    c "Hm?"

    s "Can I sit?"

    c "Of course!"

    s_thoughts "Third 'of course' today."

    s_thoughts "I sit on the bed. Charlotte hovers for a second -- not sure where to put herself in her own room."

    s_thoughts "She sits at the desk."

    s_thoughts "In her own bedroom. She sits at the desk. Like a guest."

    s "Come here."
    
    c "...O-Okay."

    show charlotte flooshed at center

    s_thoughts "She sits next to me. On her own bed. Looking slightly startled to be on it with company."

    s "Tell me about Sophie."

    show charlotte smile at center

    c "She's sixteen. She's -- she's great. She's so smart, Sophia. Like actually smart, not just school-smart. She asks these questions that I never thought to ask."

    s "Like what?"

    c "Like -- last week she asked me why I always answer the phone on the first ring. And I said 'because that's polite' and she said 'no, it's not polite, it's anxious.'"

    s "Smart kid."

    c "Too smart. She's going to figure everything out before I do."

    s "Figure what out?"

    show charlotte neutral at center

    s_thoughts "Charlotte pauses."

    c "She's just -- she doesn't need me the way she used to. And that's good. That's GOOD."

    s "You said 'good' twice."

    c "Because it IS."

    s "Okay."

    c "It is!"

    s "I said okay."

    show charlotte embarrassed at center

    c "...I'm doing the thing, aren't I."

    s "A little."

    c "Of course I am."

    s_thoughts "Four."

    s_thoughts "We sit on Charlotte's bed in Charlotte's room that doesn't look like Charlotte."

    s_thoughts "I want to put something in it. A poster. A lamp. Something that says 'Charlotte was here.'"

    s_thoughts "But that's my impulse, not hers."

    s_thoughts "And I'm starting to realize the difference matters."
    
    show charlotte vulnerable at center
    
    c "...Want to go out tonight?"
    
    s_thoughts "A date."
    
    s "Yes please."
    
    show charlotte happy at center
    
    s_thoughts "She smiles. It's warm. It's pleasant. It's Charlotte."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 18: THE DATE
    ## Charlotte plans everything perfectly. TOO perfectly.
    ## One moment where the performance shows.
    ## CHOICE 7.
    ## ===========================

    scene bg restaurant with Fade(0.8, 0.3, 0.8)
    play music mus_planned fadein 2.0

    s_thoughts "Charlotte planned our date."

    s_thoughts "'I found a place, if you want?' she said, like she'd stumbled across a restaurant by accident. Like she hadn't researched the menu, checked for allergies she doesn't have, made a reservation for a table by the window."

    s_thoughts "The restaurant is nice. Not fancy -- Charlotte-nice. Warm lighting. Linen napkins. A candle that smells like vanilla."

    show charlotte happy at center with dissolve

    s_thoughts "Charlotte is wearing a new top. I notice because I notice. She didn't mention it."

    c "I love this place. The pasta is really good."

    s "Have you been here before?"

    c "Once! With Isabella. She ordered three appetizers."

    s "That tracks."

    show charlotte smile at center

    s_thoughts "Charlotte is charming. With the waiter, with me, with the couple at the next table who accidentally bumped her chair."

    s_thoughts "The waiter comes."

    c "Hi! How's your night going?"

    s_thoughts "The waiter -- a guy, early twenties, tired eyes -- blinks. He's not used to being asked."

    s_thoughts "They talk for a minute. Charlotte asks about the specials. She already knows the specials. I can tell because she asks about them in the wrong order -- she's pretending to hear them for the first time."

    c "The gnocchi sounds amazing. Sophia, you'd love the gnocchi."

    s "Would I?"

    c "It's got brown butter and sage. You like brown butter."

    s "How do you know I like brown butter?"

    show charlotte embarrassed at center

    c "You -- I made that pasta thing last week and you said the brown butter was the best part."

    s "I said that once."

    c "I listen!"

    s_thoughts "She listens."

    s_thoughts "It's like being known by an algorithm."

    s_thoughts "That's not fair."

    s_thoughts "It's not fair and I thought it anyway."
    
    show charlotte happy at center

    s_thoughts "She recommends dishes. She mentions the wine list. She asks about my day and my classes and whether I've started the Nova essay."

    s_thoughts "She listens like it's the most important thing she's ever heard."

    s_thoughts "At some point, I realize she's already ordered. Not for me -- she ordered FOR herself. But the dish she ordered is the one I almost ordered before changing my mind."

    s_thoughts "She read me deliberating and adjusted."

    s_thoughts "Or she just likes the same food."

    s_thoughts "Or she trained herself to like the same food."

    s_thoughts "I need to stop."

    c "What do you need?"

    s "What?"

    show charlotte smile at center

    c "From me. In this... whatever this is. What do you need?"

    s_thoughts "She asks it like it's a menu. Like she can prepare whatever I order."

    menu:
        "\"Just you.\"":
            $ charlotte_present += 1

            s "Just you."

            s_thoughts "Charlotte's face does something complicated. Not a flinch. Not a smile. Something between a search and a reset."

            show charlotte happy at center

            c "Of course."

            s_thoughts "She says 'of course' and it sounds like a receipt."

            s_thoughts "But her hand is on the table and mine is on the table and when our fingers find each other it's warm and I don't think she planned that part."

            s_thoughts "I don't think she planned the way her thumb moves across my knuckle."

            s_thoughts "I hold onto that."

            jump charlotte_ch4_date_end

        "\"I need you to stop asking what I need.\"":
            $ charlotte_push += 1

            s "I need you to stop asking what I need."

            show charlotte surprised at center

            s_thoughts "Charlotte freezes. Her wine glass stops mid-lift."

            c "I -- what?"

            s "You do this. You ask what people need and then you become it. I don't want you to become what I need. I want to know what YOU need."

            show charlotte neutral at center

            s_thoughts "The restaurant hums around us. The couple at the next table laughs about something."

            c "I don't know how to do that."

            s_thoughts "She says it flat. Not performed. Not bright."

            s_thoughts "The most honest thing Charlotte has said in three weeks."

            s "What?"

            c "I don't know how to not -- I don't know how to be in a room with someone and not think about what they need. I've been doing it since I was ten."

            s_thoughts "Since she was ten."

            s_thoughts "I want to push. I want to ask why ten. I want to open the drawer."

            s_thoughts "But Charlotte just told me the truest thing she's said since we met and the truest thing I can do back is not turn it into an investigation."

            s "Okay."

            c "Okay?"

            s "You said you don't know how. That's okay. We'll figure it out."

            s_thoughts "Charlotte stares at me."

            show charlotte smile at center

            c "...You're not going to try to fix that?"

            s "No."

            c "Most people would try to fix that."

            s "I'm not most people."

            c "No. You're not."

            s_thoughts "Her hand is on the table. Mine finds it."

            s_thoughts "We sit there."

            s_thoughts "The food comes. It's good. Charlotte eats some of hers."

            jump charlotte_ch4_date_end

        "\"I don't know yet. Let's just eat.\"":
            $ charlotte_present -= 1

            s "I don't know yet. Let's just eat."

            c "Of course!"

            s_thoughts "She brightens immediately. The question evaporates. She's already picking up the menu, already moving to the next thing."

            s_thoughts "I let a real question dissolve because answering it would have meant being in it."

            s_thoughts "Charlotte is already talking about the dessert options."

            s_thoughts "The moment is gone."

            jump charlotte_ch4_date_end

label charlotte_ch4_date_end:
    
    scene bg nightwalk with dissolve

    s_thoughts "After dinner, we walk. The street is that kind of cold where your hands find excuses to be in pockets or in other hands."

    s_thoughts "Charlotte's hand is in mine."

    show charlotte smile at center with dissolve

    c "That was nice."

    s "It was."

    c "We should do it again."

    s "We should."

    s_thoughts "She squeezes my hand. I squeeze back."

    s_thoughts "The restaurant was perfect. The food was perfect. Charlotte was perfect."

    s_thoughts "I keep waiting for the thing that isn't perfect."

    s_thoughts "I keep waiting for Charlotte not to be perfect."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 19: EVE TENSION #2
    ## Escalation from the chore chart.
    ## Charlotte managing the house AND the relationship.
    ## Eve should be RIGHT.
    ## CHOICE 8.
    ## ===========================

    scene bg hallway with Fade(0.8, 0.3, 0.8)
    play music mus_baddecisions fadein 1.5

    s_thoughts "Thursday."

    s_thoughts "The bathroom has become a battleground."

    s_thoughts "Nobody is fighting, though. That's the Charlotte way."

    show charlotte happy at left with dissolve

    c "I just think if everyone does their part, nobody has to do more than--"

    show eve neutral at right with dissolve

    e "I do my part."

    c "The bathroom hasn't been cleaned since--"

    e "I cleaned it Tuesday."

    c "Oh. Okay! I must have missed that."

    s_thoughts "Charlotte's smile is structural. Load-bearing. It does not waver."

    s_thoughts "I was in the bathroom Wednesday. It was clean."

    s_thoughts "Charlotte was in the bathroom Thursday morning. She recleaned it."

    s_thoughts "Because Charlotte's version of clean and everyone else's version of clean are not the same thing, and Charlotte can't admit that."

    e "Charlotte. I cleaned it."

    c "I know! I'm sure you did. I just--"

    e "You just what?"

    show charlotte smile at left

    c "Nothing. It's fine!"

    s_thoughts "Eve looks at Charlotte. Charlotte looks at the sponge she's holding."

    e "You recleaned it."

    c "I didn't--"

    e "I can see the scrub marks. You used the other sponge. The one you keep under the sink."

    s_thoughts "Charlotte has a secret sponge."

    s_thoughts "Charlotte has a secret sponge for recleaning things other people already cleaned."

    show charlotte embarrassed at left

    c "I just -- there was a spot--"

    e "There's always a spot."

    s_thoughts "Eve's voice is flat. Not angry. Not mean. Just flat. Eve stating a fact."

    s_thoughts "And the fact is: Charlotte can't let go."

    s_thoughts "Charlotte looks at me."

    s_thoughts "Eve doesn't."

    menu:
        "Charlotte is looking at me for backup."

        "\"I think Charlotte's just trying to keep things fair.\"":
            $ charlotte_push += 1
            $ charlotte_eve -= 1

            s "I think Charlotte's just trying to keep things fair."

            s_thoughts "Eve's eyes move to me. Slow."

            show eve annoyed at right

            e "Fair."

            s "The chart is--"

            e "The chart is Charlotte deciding what's fair and everyone agreeing because it's easier than arguing."

            s_thoughts "Eve walks out."

            hide eve with dissolve

            show charlotte smile at left

            c "She'll come around. She just needs--"

            s_thoughts "Charlotte is rearranging the sponges."

            s_thoughts "Later, I go to the bathroom. It's spotless. It was spotless before Charlotte recleaned it."

            s_thoughts "Eve was right."

            s_thoughts "I backed the wrong side because it was easier."

            jump charlotte_ch4_mom_call

        "\"Charlotte... did you actually check the bathroom?\"":
            $ charlotte_eve += 1
            $ charlotte_present += 1

            s "Charlotte."

            show charlotte smile at left

            c "Hm?"

            s "Did you actually check the bathroom before you cleaned it again?"

            s_thoughts "Charlotte's hand tightens on the sponge."

            show charlotte neutral at left

            c "I -- I'm sure I--"

            s "Or did you just clean it because you always clean it?"

            s_thoughts "The kitchen is quiet."

            s_thoughts "Eve says nothing. She doesn't need to."

            show charlotte sad at left

            c "I just..."

            c "I like things to be a certain way."

            s "I know."

            c "Is that so bad?"

            s_thoughts "She's asking me. Like the porch. Like the question that hangs."

            s "It's not bad. But it's not about the bathroom."

            s_thoughts "Charlotte doesn't answer."

            s_thoughts "Eve leaves. Quietly. Not a retreat. She just doesn't need to be here anymore. She made her point. Charlotte heard it."

            hide eve with dissolve

            s_thoughts "Charlotte washes the sponge. Wrings it out. Sets it in its place."

            s_thoughts "She doesn't say 'of course.'"

            s_thoughts "Progress."

            jump charlotte_ch4_mom_call

        "\"I don't want to get in the middle of this.\"":
            $ charlotte_present -= 1
            $ charlotte_eve -= 1

            s "I don't want to get in the middle of this."

            s_thoughts "I leave the kitchen."

            s_thoughts "Behind me, I hear Charlotte's voice -- bright, cheerful, filling the gap I left."

            c "It's fine! It's totally fine. I just--"

            s_thoughts "I close my door."

            s_thoughts "Eve was right. Charlotte needed someone to not take her side. And I walked away."

            s_thoughts "The path of least resistance. The one Charlotte paved for me by being easy."

            jump charlotte_ch4_mom_call

    ## ===========================
    ## SCENE 20: CHARLOTTE'S MOM CALLS
    ## THE KEY SCENE. Charlotte's voice CHANGES on the phone.
    ## This is the ORIGINAL performance.
    ## This is where Charlotte learned to be Charlotte.
    ## ===========================

label charlotte_ch4_mom_call:

    stop music fadeout 4.0
    scene bg hallway with Fade(0.8, 0.3, 0.8)

    s_thoughts "Saturday afternoon."

    s_thoughts "I'm coming out of my room to get water when I hear Charlotte's voice from the hallway."

    s_thoughts "Her phone is pressed to her ear. She hasn't seen me."

    s_thoughts "And her voice is--"

    s_thoughts "Different."
    play music mus_charlotte_sad fadein 3.0

    show charlotte happy at center with dissolve

    c "No, everything's great! School is GREAT. The house is really good, Mom. Everyone's getting along."

    s_thoughts "The brightness. I know Charlotte's brightness. I've been living inside it for weeks."

    s_thoughts "This is not that."

    s_thoughts "This is the original. This is where Charlotte learned to be bright."

    c "I'm eating, yes I'm eating! I had eggs this morning. And a smoothie."

    s_thoughts "She didn't have a smoothie. She had coffee. I watched her have coffee."

    c "Of course! Of course I'm taking care of myself. Mom."

    s_thoughts "The 'of course' -- it's the same words. The same intonation. But pitched up half a degree. Brighter. More emphatic."

    c "Yes! I'm sleeping. Eight hours. Well, seven. Well -- I'm sleeping, okay?"

    s_thoughts "She laughs."

    s_thoughts "I know Charlotte's laughs. The bright one. The surprised one. The real one."

    s_thoughts "This is a fourth laugh. I haven't heard it before."

    c "Sophie? She's good. I talked to her yesterday. She's doing so well in school. I'm so proud of her."

    s_thoughts "Her voice cracks slightly on 'proud.' She covers it."

    c "No, I don't need anything. I'm fine. I'm really fine."

    s_thoughts "She says 'I'm fine' the way a building says 'I'm standing.' Technically true."

    c "Yes. Mom. Yes. Of course."

    s_thoughts "She pauses. Listens. Her jaw tightens."

    c "I know you worry. You don't have to worry. That's my -- that's not -- I know."

    s_thoughts "Lower now. The brightness dimming."

    c "I'm glad you're doing well. I'm really glad. The new meds are helping?"

    s_thoughts "She listens."

    c "That's really good, Mom. I'm really happy for you."

    s_thoughts "She means it. I can hear that she means it."

    s_thoughts "I can also hear someone who has to mean it."

    c "I love you too. I'll call Sunday. Yes. Yes. Of course."

    s_thoughts "She hangs up."

    s_thoughts "Her phone hand drops to her side."
    
    show charlotte sad at center

    s_thoughts "She stands in the hallway."

    s_thoughts "The mask is off."

    s_thoughts "Not dramatically. Not a breakdown. She just stands there with her phone at her side and her eyes fixed on the wall and she looks -- she looks tired."
    
    s_thoughts "In a way she never looks. A tiredness she keeps in the same place she keeps her room: private, undecorated, functional."

    s_thoughts "She breathes in. Breathes out."

    s_thoughts "She turns the corner."

    s_thoughts "She sees me."

    show charlotte happy at center

    s_thoughts "The smile is back before I can count to one."

    c "Hey! I didn't see you there. Want some--"

    s "Charlotte."

    c "I was going to make lunch. Are you hungry?"

    s "I heard some of that."

    show charlotte neutral at center

    s_thoughts "Her hand tightens on the phone."

    c "Oh. It was just my mom. We talk every couple of weeks."

    s "You sounded different."

    c "Different how?"

    s "Brighter."

    s_thoughts "She blinks."

    s_thoughts "Nobody's ever named it before."

    c "That's just... my phone voice. Everyone has a phone voice."

    s "Your... phone voice."

    c "I do! I have a phone voice! It's normal!"

    s "You told her you had a smoothie."

    show charlotte embarrassed at center

    c "...I was going to have a smoothie."

    s "You told her you slept eight hours."

    c "Seven. I corrected it."

    s "You told her everything is great and everyone's getting along."

    c "Everyone IS--"

    s "You and Eve had a fight three days ago."

    show charlotte sad at center

    s_thoughts "Charlotte's face does something. Not the flicker. Not the reset. Something slower."

    c "It wasn't a fight."

    s "Okay."

    c "She just -- she worries. And when she worries--"

    s_thoughts "Charlotte stops."

    c "When she worries, I make it worse by not being okay. So I'm okay."

    s "For her."

    c "For her."

    s_thoughts "She says it like a fact. Like 'the sky is blue, Mom.'"

    s_thoughts "I want to pull every thread. I want to ask about the meds in particular. Meds for what?"

    s_thoughts "But Charlotte is standing in a hallway holding a phone and smiling and I don't think she's smiling."

    s_thoughts "Pulling threads right now would be another version of the performance."

    s "Do you want lunch?"

    show charlotte surprised at center

    s_thoughts "Charlotte blinks."

    c "What?"

    s "Lunch. Do you want lunch? I'll make it."

    c "You'll -- you don't have to--"

    s "I know. Do you want lunch?"

    show charlotte neutral at center

    s_thoughts "She stares at me."

    s_thoughts "I think she's trying to figure out if this is a trap. If I'm about to make lunch and then use it as leverage to have A Conversation."

    s_thoughts "I'm not. I'm going to make lunch and it's going to be bad because I can't cook and we're going to eat it and I'm not going to ask about her mom."

    c "...Yeah. Lunch sounds good."

    s "Cool. I'm thinking grilled cheese."

    c "Can you make grilled cheese?"

    s "I can make two pieces of bread with cheese in between them on a hot surface. Whether that counts as grilled cheese is between me and God."

    show charlotte smile at center

    s_thoughts "It's not the bright smile. It's not the performance smile."

    s_thoughts "It's the tired one. The one she keeps in her room."

    c "I'll supervise."

    s "You'll sit at the table and not touch the stove."

    c "...Of course."

    s_thoughts "This one sounds different."

    s_thoughts "We go to the kitchen."

    s_thoughts "I make grilled cheese. It's terrible."

    s_thoughts "Charlotte eats it."

    hide charlotte with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 21: SOPHIA BEING MESSY
    ## Charlotte encounters Sophia's actual mess.
    ## Charlotte tries to FIX Sophia's mood. Sophia pushes back.
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)
    play music mus_2am fadein 2.0

    s_thoughts "Monday."

    s_thoughts "I am having a day."

    s_thoughts "Nova handed back the essay drafts. Mine said 'Where's the rest?' in red ink. That's it. No notes. No feedback. Just 'where's the rest' like a doctor telling you to cough."

    s_thoughts "My mom called and asked about my 'plans' which is code for 'are you still changing your major every semester' and I said 'I have plans' which is code for 'I have no plans.'"

    s_thoughts "I have been lying on my bed for forty minutes. There are socks on the floor. Not a pair. Four individual socks from four different pairs. I don't know where their partners are. They're probably living better lives."

    s_thoughts "A knock."

    show charlotte smile at center with dissolve

    c "Hey! I noticed you've been up here a while. Everything okay?"

    s "Fine."

    c "You don't sound fine."

    s "I said I'm fine."

    c "I made tea."

    s_thoughts "She's holding a mug. Of course she's holding a mug. Charlotte's answer to everything is a warm beverage."

    c "It's chamomile. For--"

    s "I don't want tea."

    show charlotte surprised at center

    s_thoughts "Charlotte pauses in the doorway."

    c "Okay. Do you want to talk about--"

    s "No."

    c "I could--"

    s "Charlotte, I don't need you to fix this."

    show charlotte neutral at center

    s_thoughts "That came out hard."
    
    s_thoughts "Good. I meant it to come out hard."

    s_thoughts "Charlotte's hand tightens on the mug."

    c "I wasn't trying to fix--"

    s "You're standing in my doorway with tea and an action plan. That's fixing."

    c "It's tea, Sophia..."

    s "It's never just tea with you. It's tea and then 'have you tried' and then a list of solutions for a problem I didn't ask you to solve."

    show charlotte sad at center

    c "I... just... um..."

    s_thoughts "She doesn't finish."

    s_thoughts "Good. Maybe now she'll--"

    c "Okay."

    show charlotte smile at center

    c "It's fine! I'll leave the tea in case you change your mind."

    s_thoughts "She sets the mug on my desk. She leaves."

    hide charlotte with dissolve

    s_thoughts "The smile as she left. The 'it's fine.' The not-slamming of the door."

    s_thoughts "I roll over. Stare at the ceiling."

    s_thoughts "I'm right. She WAS managing me. She does that. She does it to everyone. The tea was a tool, not a gift."

    s_thoughts "..."

    s_thoughts "The tea sits on my desk. Getting cold."

    s_thoughts "..."

    s_thoughts "I drink it twenty minutes later."

    s_thoughts "It's perfect. The temperature is wrong but everything else is exactly how I take it. She remembered the honey."

    s_thoughts "She remembered the honey."

    s_thoughts "I feel like garbage."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 22: THE SLIP
    ## Charlotte says "my girlfriend" accidentally.
    ## The most tender moment in the chapter.
    ## CHOICE 9.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_shoulders fadein 2.0

    s_thoughts "Two days later."

    s_thoughts "I apologized for the tea thing. Charlotte said 'of course' and 'it's nothing' and 'honestly, I was being pushy' which is Charlotte apologizing for being apologized to."

    s_thoughts "We're okay. I think. The way Charlotte does 'okay.'"

    s_thoughts "I'm in the living room. Charlotte and Isabella are in the kitchen. I can hear them through the door."

    show isabella neutral at left with dissolve

    s_thoughts "They're talking about -- something mundane. Groceries. Plans."

    s_thoughts "I'm not really listening."

    s_thoughts "And then--"
    
    show charlotte smile at right with dissolve

    c "When me and Sophia went to that restaurant, we--"
    
    show charlotte vulnerable at right

    s_thoughts "Charlotte stops."

    s_thoughts "I can hear the stop. The air changes."

    show isabella sad at left

    s_thoughts "Isabella's voice, carefully calibrated:"
    
    show isabella happy at left

    i "You and Sophia went to a restaurant?"

    c "I mean -- I didn't mean... W-We're not... uh... are we?"

    s_thoughts "I look up from my book at that. Not what, now?"

    s_thoughts "Charlotte is standing in the kitchen doorway."
    
    s_thoughts "She's looking at me."

    show charlotte flooshed at right with dissolve

    s_thoughts "Her face is -- I've never seen this expression. Not the performance. Not the brightness. Not even the crack."

    s_thoughts "It's hope. Raw hope. The kind you're supposed to have outgrown."

    c "Are we?"
    
    s_thoughts "Chest. Architectural."

    s "Yeah."

    s_thoughts "Because of course we are. We've been acting like it for weeks. The mornings. The coffee. The toast. Her hand in mine after dinner."

    s_thoughts "Charlotte's face LIGHTS. The whole thing. Like someone turned on every lamp in a house at once."

    show charlotte happy at right

    c "Of course we are!"

    s_thoughts "I can SEE the moment the spontaneous reaction gets filed and processed and Charlotte goes from 'oh my god she said yes' to 'this is what a girlfriend says when her girlfriend says yes.'"

    c "I mean -- I knew. I just didn't know if--"

    s_thoughts "Isabella. I look at Isabella."

    show isabella smile at left

    i "Congrats, you two."

    s_thoughts "Her voice is almost perfect."

    s_thoughts "Almost."
    
    s_thoughts "She leaves."

    hide isabella 
    with dissolve

    s_thoughts "Later. Charlotte is on her phone. I catch a fragment."

    show charlotte happy at center with move

    c "Yeah, she's -- my girlfriend."

    s_thoughts "She says it like she's testing the weight. Like 'girlfriend' is a new word in a language she's learning."

    c "My girlfriend. She's -- yeah."

    s_thoughts "She hasn't seen me."

    s_thoughts "I could let it pass. The word has been said. The label exists. We're official."

    menu:
        "\"Say it again.\"":
            $ charlotte_present += 1

            s "Say it again."

            show charlotte surprised at center

            s_thoughts "Charlotte spins. Phone against her chest."

            c "How long have you been there?"

            s "Long enough. Say it again."

            show charlotte embarrassed at center

            c "My... girlfriend?"

            s "Again."
            
            show charlotte vulnerable at center

            c "My girlfriend."

            s_thoughts "Quieter. The performance is peeling off. Layer by layer."

            s "One more time."

            show charlotte sad at center

            c "My girlfriend."

            s_thoughts "Almost a whisper."

            s_thoughts "She's holding the word like it's fragile and she's not sure she's allowed to have it."

            s "That's the one."

            show charlotte flooshed at center

            s_thoughts "Her eyes are wet."

            s_thoughts "She blinks. Doesn't wipe them. Doesn't laugh it off."

            c "...Yeah?"

            s "Yeah."

            s_thoughts "She stands there. Phone still against her chest. Eyes shining."

            s_thoughts "I... I think this might be the Charlotte nobody sees. And she's letting me see."

            s_thoughts "I want to hold this moment with both hands."

            s_thoughts "I want to put it somewhere Charlotte can't 'of course' it away."

            c "...Okay. I should -- I should finish this call."

            s "Okay."

            c "Okay."

            s "Charlotte?"

            c "Yeah?"

            s "I like when you say it."

            show charlotte smile at center

            s_thoughts "She doesn't say 'of course.' She doesn't say anything. She just smiles. The one she keeps in her room."

            s_thoughts "Then she turns back to her phone and her voice is bright again and she's Charlotte again and the moment is over."

            s_thoughts "But it happened."

            jump charlotte_ch4_isabella_checkin

        "\"So we're official?\"":
            $ charlotte_push += 1

            s "So we're official?"

            show charlotte surprised at center

            c "How long have you been--"

            s "The girlfriend thing. We're doing this?"

            show charlotte happy at center

            c "I -- yes? If you want to? I want to. I mean, I thought we already were, but I didn't want to assume--"

            s "Charlotte. We've been dating for three weeks."

            c "I know! I just -- labels are -- I didn't want to presume--"

            s "You presumed everything else. The coffee. The mornings. The toast."

            show charlotte embarrassed at center

            c "That's different."

            s "How?"

            c "Because -- those are things I can do FOR you. A label is something I do WITH you. And I don't--"

            s_thoughts "She stops."

            c "I don't assume people want things with me. I assume they want things from me."

            s_thoughts "The room is very quiet."

            s "Charlotte."

            c "That sounded sadder than I meant it."

            s "It sounded exactly as sad as you meant it."

            show charlotte neutral at center

            s_thoughts "She doesn't deny it."

            s "We're official."

            show charlotte smile at center

            c "...Okay."

            s "Say it."

            c "My girlfriend."

            s "There you go."

            s_thoughts "She smiles. The complicated one."

            jump charlotte_ch4_isabella_checkin

        "Let it pass.":
            $ charlotte_present -= 1

            s_thoughts "I let it pass."

            s_thoughts "Charlotte said the word. The word exists now. We're official."

            s_thoughts "I don't need to make it a moment. It can just be a fact."

            s_thoughts "It can just be a fact and Charlotte can go on performing 'girlfriend' the way she performs everything else and I can go on accepting it."

            s_thoughts "She hangs up the phone. Sees me."

            show charlotte happy at center

            c "Oh! Hey. I was just--"

            s "I heard."

            c "You heard?"

            s "Girlfriend. Cool."

            show charlotte smile at center

            c "...Cool."

            s_thoughts "The moment passes. Charlotte files it away."

            s_thoughts "I let the moment pass quietly."

            jump charlotte_ch4_isabella_checkin

    ## ===========================
    ## SCENE 23: ISABELLA'S CHECK-IN
    ## Isabella watches Charlotte and Sophia.
    ## The crush subtext deepens.
    ## ===========================

label charlotte_ch4_isabella_checkin:

    stop music fadeout 4.0
    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Later that week."

    s_thoughts "Charlotte is out. Study group. Isabella and I are in the kitchen."

    show isabella neutral at center with dissolve

    s_thoughts "Isabella is on her phone. She's been on her phone a lot lately. Looking at something with an expression I can't quite read -- concentrated, a little sad, a little warm."

    s_thoughts "She puts it down when I sit."
    
    s_thoughts "Something seems off. I file it."
    
    play music mus_glass fadein 1.5
    
    i "How's it going?"

    s "With?"

    i "With... generally. With Charlotte. With the whole 'girlfriend' thing."

    s "You heard."

    i "I was there. Remember? 'When me and Sophia went to that restaurant, we--'"

    s_thoughts "She imitates Charlotte's voice. It's eerily accurate."

    i "The face she made. Like she'd swallowed a secret."

    s "Are you okay?"

    show isabella surprised at center

    i "What? Yeah. Why?"

    s "You did the thing. Where you describe Charlotte and your voice goes--"

    i "My voice doesn't go anything."

    s "Isabella."

    show isabella sad at center

    i "...I'm happy for you. Genuinely."

    s "I know."

    i "I just -- be careful."

    s "You keep saying that."

    i "Because you keep needing to hear it."

    s "What does 'be careful' even mean?"

    show isabella neutral at center

    s_thoughts "Isabella picks up her phone. Puts it back down."

    i "It means Charlotte will take care of you. She'll take such good care of you that you'll forget she needs taking care of too. And by the time you remember, she'll have convinced you she doesn't."

    s "That sounds like you're--"

    i "Speaking from experience? Yeah. A little."

    s "Isabella."

    i "It was a long time ago. It doesn't--"

    s "It clearly does."

    show isabella sad at center

    s_thoughts "Isabella looks at me. For a second her face is completely open."

    s_thoughts "Then she picks up her phone. The expression I can't read is back."

    i "I should check on something."

    s "The function that's gaslighting you?"

    show isabella smile at center

    i "Different gaslighting function this time."

    s_thoughts "She goes back to her phone. The conversation is over."

    s_thoughts "But I caught the expression this time. The one on her face when she was looking at her phone."

    s_thoughts "It wasn't code."

    s_thoughts "...Lumi."

    s_thoughts "I don't ask. It's not my drawer to open."

    hide isabella with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 24: LILA DEEPER
    ## Lila pushes harder.
    ## "When did Charlotte last say no to you?"
    ## Lila's sister subplot deepens.
    ## ===========================

    scene bg dininghall with Fade(0.8, 0.3, 0.8)
    play music mus_campus fadein 2.0

    s_thoughts "Lunch. Lila. She's got a different smoothie this time. This one is purple."
    
    s_thoughts "She washes down the fry she just stole from me with it."

    show lila happy at center with dissolve

    l "So you're OFFICIAL official. Like, labels and everything."

    s "Labels and everything."

    s_thoughts "She slurps the smoothie. If she has thoughts, she doesn't say them."

    l "Listen. My sister. Update."

    s "The Lila Special?"

    l "She joined the BUSINESS CLUB. My sister. Who wanted to be a veterinarian. Joined the business club because -- and I quote -- 'Lila said business is where the future is.'"

    s "Did you say that?"

    show lila shocked at center

    l "I said that when I was DRUNK at Thanksgiving! I said business is where the future is because Dad was standing right there and I was trying to get him off my back! And she WROTE IT DOWN."

    s "She wrote it down?"

    l "In her planner. In PEN. 'Business is where the future is. -Lila.'"

    s "She attributed it to you."

    l "Like a QUOTE. I'm being CITED in my little sister's planner. Sophia, do you know how terrifying that is? She's building her whole life around someone who doesn't even have her own life figured out."

    s_thoughts "She puts the smoothie down."

    show lila annoyed at center

    l "And the worst part is I can't tell her to stop because she's happy. She's happy being Like Lila. And me saying 'stop being like me' would break something in her that I can't fix."

    s "Lila."

    show lila happy at center

    l "Point is. I watch my sister build herself around me and I can't stop it. And at some point I gotta ask: who is she when nobody's watching?"

    s_thoughts "I think of Charlotte."

    l "You're making a face."

    s "I'm thinking."

    l "About Charlotte?"

    s "About whether you're right."

    show lila happy at center

    l "I'm always right. I'm just usually right about the wrong things."

    s_thoughts "She finishes the smoothie."

    l "Go home. Love your toast girl. Just... keep watching."

    s "I always watch."

    l "I know. That's why I'm telling you."
    
    stop music fadeout 2.0
    hide lila with dissolve

    ## --- Later. Sophia's room. ---

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "I don't know why I look up Charlotte's old Instagram."

    s_thoughts "I scroll. Two years of posts."

    s_thoughts "Every photo is someone else. Sophie at a recital. A group shot at homecoming. 'Happy birthday, Mom!' 'So proud of Sophie!' 'Best night with these girls!'"

    s_thoughts "Not a single selfie. Not a single photo where Charlotte is the subject."

    s_thoughts "Charlotte is the photographer. Charlotte is always the photographer."

    s_thoughts "She doesn't exist in her own feed."

    s_thoughts "I close the app."

    s_thoughts "Charlotte's empty room. Charlotte's Instagram full of other people. Charlotte's 'of course' that means 'I can handle this before you ask.'"

    s_thoughts "I sit with it."

    ## --- Kitchen. Amara. ---

    scene bg kitchen with dissolve
    play music mus_2am fadein 2.0

    s_thoughts "I go downstairs for water."

    show amara neutral at center with dissolve

    s_thoughts "Amara is making tea. The kettle clicks off."

    s "Hey."

    a "Hey."

    s_thoughts "We exist in the kitchen. Amara doesn't do small talk."

    s "Amara?"

    a "Hm."

    s "Do you think Charlotte's happy?"

    s_thoughts "Amara pours her tea. Looks at me."

    a "She's always okay."

    s_thoughts "Three words."

    s_thoughts "She takes her tea to her room."

    hide amara with dissolve

    s_thoughts "She's always okay."

    s_thoughts "She's ALWAYS okay."

    s_thoughts "And I've been letting her be."

    stop music fadeout 2.0

    ## ===========================
    ## END OF ACT 2
    ## The relationship is official. The warmth continues.
    ## The cracks are showing. Charlotte's "of course" is getting louder.
    ## The mom call revealed the original performance.
    ## ===========================

label charlotte_ch4_act2_end:

    scene black with Fade(1.0, 0.5, 1.0)

    s_thoughts "Charlotte is my girlfriend."

    s_thoughts "Charlotte is my girlfriend. I let the word sink in. I toss it around my mind like dough I'm beating the hell out of."
    
    s_thoughts "We're official now. She's my toast girl. I'm her... something."
    
    s_thoughts "That word. 'Something.' Toast Girl is warm. Comforting. Always there."

    s_thoughts "I'm her girlfriend. Obviously."
    
    s_thoughts "Of course I am."
    
    s_thoughts "...Of course."
    
    s_thoughts "..."

    ## END OF ACT 2

    jump charlotte_ch4_act3

## ===========================
## ===========================
## ACT 3: "THE SEAMS"
## The cracks deepen. Charlotte's performance starts failing.
## The Vermeer paper. Eve confrontation. The porch confession.
## ===========================
## ===========================

label charlotte_ch4_act3:

    ## ===========================
    ## SCENE 25: MOVIE NIGHT
    ## Charlotte can't pick a movie. "What do you WANT to watch?"
    ## The question that hangs.
    ## CHOICE 10.
    ## ===========================

    scene bg livingroom with Fade(1.0, 0.5, 1.0)
    play music mus_morningafter fadein 3.0

    s_thoughts "Two weeks in."

    s_thoughts "Two weeks of being Charlotte's girlfriend and I still can't tell you Charlotte's favorite color."

    s_thoughts "Not because she doesn't have one. Because every time I ask, she says 'I like them all!'."

    s_thoughts "Friday night. Living room. The couch."

    show charlotte happy at center with dissolve

    c "Movie night!"

    s "Movie night."

    c "So what do you want to watch?"

    s "What do YOU want to watch?"

    c "I'm easy! Whatever you're in the mood for."

    s "Charlotte. Pick a movie."

    show charlotte smile at center

    c "Okay! Sure. Let me just--"

    s_thoughts "She picks up the remote. Opens the streaming app. Scrolls."

    s_thoughts "And scrolls."

    s_thoughts "And scrolls."

    show charlotte neutral at center

    c "There's a lot of options."

    s "Pick one."

    c "I'm picking! I just want to make sure you'll--"

    s "Charlotte."

    c "What?"

    s "I didn't ask what I'd like. I asked what YOU want."

    show charlotte embarrassed at center

    s_thoughts "Charlotte stares at the screen. Her thumb hovers over the remote. I can see her cycling through choices -- not for what she wants but for what she thinks I'd approve of."

    c "I don't -- I mean there's this one thing."

    s "Pick it."

    c "You haven't even heard what it is."

    s "Pick it."

    show charlotte surprised at center

    s_thoughts "She clicks. Something appears on the screen. It's -- huh."

    s_thoughts "It's a documentary about furniture restoration."

    c "We can change it."

    s "No."

    c "It's boring, I know, it's just -- this guy restores antique tables and he's really -- we can change it."

    s "Is this what you want to watch?"

    show charlotte neutral at center

    c "...Yes?"

    s "Then we're watching it."

    c "You're going to hate it."

    s "Maybe."

    c "It's about SANDING, Sophia. There's an entire segment on types of sandpaper."

    s "I'm riveted already."

    show charlotte embarrassed at center

    s_thoughts "She's tense. I can feel it through the couch. For the first ten minutes she keeps glancing at me. Checking."

    s_thoughts "Fifteen minutes in, the guy is explaining why you have to strip the old varnish before you can see the grain underneath. 'You can't know what you're working with until you take off what someone else put on it,' he says."

    s_thoughts "Charlotte's eyes are on the screen."

    s_thoughts "Twenty minutes. Her shoulder touches mine. She stops checking. I put my arm around her."

    s_thoughts "Thirty minutes and she's leaning forward."

    show charlotte happy at center

    c "See? See how he's following the grain? You HAVE to follow the grain or you damage it. You can't impose a direction on wood."

    s "You know a lot about this."

    c "I watched like thirty of these during finals week last year. They're -- they're meditative."

    s "So you have a secret furniture restoration obsession."

    show charlotte embarrassed at center

    c "It's not an OBSESSION. It's a -- a thing I watch when I can't sleep."

    s "When you can't sleep."

    c "Everyone has a thing."

    s_thoughts "Charlotte's thing. The thing she watches when nobody's awake to need her."

    s_thoughts "Forty minutes. The guy finishes the table. It's beautiful."

    show charlotte smile at center

    s_thoughts "Charlotte's face in the light of the screen. Just -- watching something she chose."

    s_thoughts "She looks like someone I haven't met yet."

    menu:
        "The documentary ends."

        "\"This is so much better than what I would have picked.\"":
            $ charlotte_present += 1

            s "This is so much better than what I would have picked."

            show charlotte happy at center

            c "Really?"

            s "I would have picked something terrible. You saved us."

            c "I did? I mean -- I did!"

            s_thoughts "She relaxes. But she relaxes because I approved. Because I told her the choice was good."

            s_thoughts "That's not the same as feeling safe enough to choose."

            s_thoughts "I know that."

            s_thoughts "I take it anyway."

            jump charlotte_ch4_chore_blowup

        "\"Tell me why you love this.\"":
            $ charlotte_push += 1

            s "Tell me why you love this."

            show charlotte surprised at center

            c "What?"

            s "The sanding. The grain. The guy with the old tables. Why do you love it?"

            c "I don't -- I wouldn't say I LOVE it."

            s "You just spent ten minutes explaining sandpaper grades to me. You love this. Tell me why."

            show charlotte neutral at center

            s_thoughts "She's quiet for a second. Not the performing-quiet. The thinking-quiet."

            c "...He takes something broken. Or not broken -- covered. Something with layers of paint and varnish that someone else put on it. And he strips it all back. And underneath there's this -- this wood that's been there the whole time."

            c "And it's beautiful. And nobody could see it because it was buried under what everyone else decided it should look like."

            s_thoughts "She stops."

            c "That sounds dumb."

            s "That doesn't sound dumb."

            c "It sounds like a metaphor."

            s "It is a metaphor."

            show charlotte embarrassed at center

            c "I didn't mean it to be a metaphor! I just like the sanding!"

            s "You like the sanding AND it's a metaphor."

            c "...Okay. Maybe."

            s_thoughts "She pulls her knees up. Wraps her arms around them."

            s_thoughts "She looks young."

            s_thoughts "She looks covered in varnish."
            
            s_thoughts "That's a metaphor."

            s_thoughts "I don't share that."

            jump charlotte_ch4_chore_blowup

    ## ===========================
    ## SCENE 27: THE CHORE CHART BLOWUP
    ## Eve conflict #3. The final escalation before the confrontation.
    ## Eve says the true thing about Charlotte's need to control.
    ## CHOICE 12 (renumbered).
    ## ===========================

label charlotte_ch4_chore_blowup:

    stop music fadeout 2.0
    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_baddecisions fadein 1.5

    s_thoughts "Saturday morning."

    s_thoughts "The chore chart has been updated."

    s_thoughts "Not just updated. Revised. There's a new color -- orange, for 'shared tasks.' Charlotte has reorganized the entire system. There are sub-categories now. 'Kitchen maintenance (daily).' 'Kitchen maintenance (weekly).' 'Bathroom (mirrors separate from surfaces).'"

    s_thoughts "Eve's column has been filled in. By Charlotte."

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte is at the counter. Wiping something. The counter is already clean."

    show eve neutral at right with dissolve

    s_thoughts "Eve walks in. Sees the chart."

    s_thoughts "Reads it."

    e "You filled in my column."

    c "I just thought it would be easier if I--"

    e "You filled in my column."

    show charlotte smile at left

    c "I didn't want you to feel pressured! I just picked things that seemed--"

    e "You picked things FOR me."

    c "Easy things! Small things. I wasn't--"

    e "Charlotte."

    s_thoughts "Eve's voice is level. Not raised. Eve doesn't raise her voice."

    e "I don't need you to decide what I do in this house."

    show charlotte neutral at left

    c "I wasn't deciding! I was suggesting. It's a suggestion."

    e "It's laminated."

    s_thoughts "It is laminated."

    c "Laminating doesn't mean--"

    e "You laminated my chores. That's not a suggestion. That's an assignment."

    s_thoughts "Charlotte's hands are still on the counter. The sponge -- the regular one, not the secret one -- is clenched in her fist."

    show charlotte sad at left

    c "I just want the house to work."

    e "The house works."

    c "It doesn't work if nobody--"

    e "It works. You just don't like how it works unless you're the one making it work."

    s_thoughts "The kitchen is very quiet."

    s_thoughts "Charlotte's jaw is doing the thing. The flex. The hold."

    s_thoughts "Eve is looking at her. Not angry. Not mean. Patient, almost. Like she's been waiting to say this."

    e "You want the house to be what you need it to be. And that's not the same as what it needs to be."

    show charlotte neutral at left

    s_thoughts "Charlotte's smile doesn't come back."

    s_thoughts "That's new."

    s_thoughts "Usually the smile resets in under a second. The rubber band snaps back. The performance catches up."

    s_thoughts "This time Charlotte just stands there. Holding a sponge. Not smiling."

    s_thoughts "Eve watches. Then she nods -- not dismissive, just done -- and walks out."

    hide eve with dissolve

    s_thoughts "Charlotte hasn't moved."

    menu:
        "Charlotte is standing in the kitchen alone."

        "Go to her.":
            $ charlotte_present += 1
            $ charlotte_eve -= 1

            s_thoughts "I go to her."

            s "Hey."

            show charlotte smile at left

            s_thoughts "The smile comes back. Slower this time. Like a computer booting up."

            c "I'm fine! Eve is just -- she's having a day."

            s "Charlotte."

            c "Really. It's fine. She's right, I shouldn't have filled in her column. I'll fix it."

            s_thoughts "She's already reaching for the chart. Already fixing. Already moving."

            s "You don't have to fix it right now."

            c "I know! But I want to. It's better if I just--"

            s_thoughts "Her hands are shaking."

            s_thoughts "Barely. Just a tremor. She grips the sponge tighter and it stops."

            c "I'm going to redo the chart. Without Eve's column. She can do her own."

            s "Okay."

            c "It's FINE."

            s_thoughts "She says 'fine' like a wall going up. Brick by brick."

            s_thoughts "I backed her. I'm standing next to her in the kitchen while she rebuilds the chart and I'm letting her."

            s_thoughts "Eve was right. I know Eve was right."

            s_thoughts "But Charlotte is right here and shaking and I can't do both."

            jump charlotte_ch4_amara_line

        "Side with Eve. \"She has a point.\"":
            $ charlotte_push += 1
            $ charlotte_eve += 1

            s "Charlotte."

            show charlotte smile at left

            c "I'm fine! I'll just redo the--"

            s "She has a point."

            show charlotte surprised at left

            s_thoughts "Charlotte stops."

            s "The laminating. Filling in her column. You decided what Eve should do without asking her."

            c "I was trying to HELP."

            s "I know. But helping someone without asking if they want help isn't helping. It's managing."

            show charlotte sad at left

            s_thoughts "Charlotte's face goes still. The kind of still where something just landed."

            c "I'm not -- I don't manage people."

            s "Charlotte."

            c "I DON'T."

            s_thoughts "Her voice cracks. Just slightly. On the 'don't.'"

            s_thoughts "She sets the sponge down. Carefully. Lines it up with the edge of the sink."

            c "...Okay."

            s "Okay?"

            c "Okay. I hear you."

            s_thoughts "She doesn't say 'of course.' She doesn't smile."

            s_thoughts "She just stands there."

            s_thoughts "Progress. Maybe."

            jump charlotte_ch4_amara_line

        "Leave the room.":
            $ charlotte_present -= 1
            $ charlotte_push -= 1
            $ charlotte_eve -= 1

            s_thoughts "I leave the kitchen."

            s_thoughts "I hear Charlotte behind me. The sponge. The scrubbing. The sound of someone cleaning a counter that doesn't need cleaning."

            s_thoughts "I should go back."

            s_thoughts "I don't."

            jump charlotte_ch4_amara_line

    ## ===========================
    ## SCENE 32: AMARA'S LINE
    ## Spaced from Eve's confrontation.
    ## Maximum devastation.
    ## ===========================

label charlotte_ch4_amara_line:

    stop music fadeout 2.0
    scene bg entry with Fade(0.8, 0.3, 0.8)

    s_thoughts "Later. The house is quiet in that way it gets after an argument nobody acknowledged."

    s_thoughts "Amara is reading by the door. She's zipping through it."

    show amara neutral at center with dissolve

    s "Amara."

    a "Hm."

    s "About Charlotte..."

    s_thoughts "Amara looks at me."

    s_thoughts "She doesn't blink."

    a "Have you ever seen Charlotte want something?"

    s "What?"

    a "Not give something. Not do something. Want."

    s_thoughts "I open my mouth."

    s_thoughts "I close it."

    hide amara with dissolve

    s_thoughts "Amara goes into her room."

    s_thoughts "I stand in the same spot for a while."

    s_thoughts "Have I ever seen Charlotte want something?"

    s_thoughts "She wants the house to work. She wants everyone to be fed. She wants me to be happy."

    s_thoughts "Those are things she wants FOR other people."

    s_thoughts "What does Charlotte want for Charlotte?"

    s_thoughts "..."

    ## ===========================
    ## SCENE 27: THE VERMEER PAPER
    ## Charlotte talks about or shows Sophia the paper.
    ## "The Room She Built" -- about women trapped in beautiful
    ## domestic interiors. The essay IS Charlotte writing about herself
    ## without knowing it.
    ## ===========================

label charlotte_ch4_vermeer:

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_charlotte fadein 2.0

    s_thoughts "Sunday."

    s_thoughts "Charlotte is on the couch. Laptop open. She's been working on the paper all weekend."

    show charlotte smile at center with dissolve

    c "I finished it."

    s "The Vermeer paper?"

    c "The Vermeer paper. It's done. Submitted. Twelve pages. I might throw up."

    s "Can I read it?"

    show charlotte embarrassed at center

    c "It's -- it's not very--"

    s "Charlotte."

    c "...Okay."

    s_thoughts "She turns the laptop toward me."

    s_thoughts "'The Room She Built: Domestic Labor and Self-Erasure in Vermeer's Interior Paintings.'"

    s_thoughts "I read."

    s_thoughts "The first line: 'The milk maid does not know she is being watched.'"

    s_thoughts "Charlotte argues that Vermeer's women are trapped inside two frames simultaneously -- the physical frame of the painting and the domestic frame of the room. They can't leave. They don't know they're being observed. The viewer's tenderness is the cage."

    s_thoughts "She writes about light. How Vermeer's light always comes from the left, through a window the women can't reach. 'The illumination is imposed. The beauty is not chosen.'"

    s_thoughts "'The milk maid's labor becomes art because someone else decided it was art. She was just pouring milk.'"

    s_thoughts "She writes about the rooms. Small, intimate, closed. 'The viewer feels close to her. But closeness is surveillance. The domestic space creates a performance of intimacy that the subject did not consent to.'"

    s_thoughts "She writes about erasure. 'The milk maid has no name. She has a function. She pours milk. She is defined by her labor. The painting preserves her as permanent service -- beautiful, silent, always working. She has been turned into the room itself.'"

    s_thoughts "I read it twice."

    show charlotte neutral at center

    c "Is it bad?"

    s "Are you kidding?"

    c "The conclusion is weak. I know the conclusion is weak. I ran out of--"

    s "This is brilliant."

    show charlotte surprised at center

    c "It's not--"

    s "The thing about the light. 'The illumination is imposed.' That's -- Charlotte, that's a real argument."

    show charlotte embarrassed at center

    c "It's just Vermeer."

    s "It's not just Vermeer."

    s_thoughts "I say it before I can stop myself."

    s_thoughts "Charlotte goes still."

    c "What does that mean?"

    s_thoughts "I could push. I could say it. 'You're writing about yourself.'"

    s_thoughts "I could say that."

    s_thoughts "But Charlotte looks proud. Actually proud. For five seconds."

    s "It means it's a really good paper. That's what it means."

    show charlotte smile at center

    c "...Thanks."

    s "You should celebrate."

    c "It's just a paper."

    s "Charlotte. You wrote twelve pages about Vermeer. Twelve GOOD pages."

    c "Everyone works hard."

    s_thoughts "There it is. The deflection. The minimizing."

    s_thoughts "I know what Amara would say. Have you ever seen Charlotte want something?"

    s_thoughts "She built it and she doesn't know what she built."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 28: NOVA OFFICE HOURS
    ## Brief. Charlotte's paper. Nova says something oblique.
    ## "The difference between describing a cage and living in one."
    ## ===========================

    scene bg officehours with Fade(0.8, 0.3, 0.8)
    play music mus_nova fadein 2.0

    s_thoughts "Thursday. Nova's office hours."

    s_thoughts "I don't know why I'm here. I don't have a question about the assignment. I have a question about Charlotte's paper."

    s_thoughts "That should tell me something."

    show professor neutral at center with dissolve

    nova "Ms. Bell. No essay emergency today?"

    s "I wanted to ask about something. Not my paper."

    nova "Whose paper?"

    s "A friend's. Art history. It's about Vermeer."

    nova "Why are you asking me about someone else's paper?"

    s "Because I think she wrote something she doesn't understand."

    show professor happy at center

    nova "Mm."

    s_thoughts "Nova leans back. She does that -- the lean. The silence that means 'keep going, I'm not helping you yet.'"

    s "She wrote about domestic labor and self-erasure. About how Vermeer's women are trapped in the painting the same way they're trapped in the room. And it's good. It's really good. But she doesn't see that she's--"

    nova "That she's what?"

    s "That she's describing herself."

    show professor neutral at center

    nova "And you want to tell her that."

    s "Shouldn't I?"

    nova "What would that accomplish?"

    s "She'd know. She'd see it."

    nova "Would she?"

    s_thoughts "Nova picks up a pen. Sets it down."

    nova "There's a difference between describing a cage and living in one, Sophia. Your friend wrote an excellent paper about a cage. That doesn't mean she knows she's in it. And pointing at the bars from the outside doesn't open them."

    s "So I just -- don't say anything?"

    nova "I didn't say that. I said pointing at bars from the outside doesn't open them. Sometimes it just makes the person inside grip them harder."

    s_thoughts "I sit with that."

    nova "How's your paper coming?"

    s "I have three sentences."

    nova "Progress."

    s "Is it?"

    nova "It's more than one."

    s_thoughts "She's not smiling. Nova doesn't smile when she's teaching. She smiles when she's done."

    nova "One more thing."

    s "Yeah?"

    nova "When someone writes about a cage without knowing they're in it -- that's interesting scholarship. When someone outside the cage reads it and wants to break in -- that's something else."

    s "What is it?"

    nova "That's your essay, Ms. Bell. Figure it out."

    hide professor with dissolve
    stop music fadeout 2.0
    
    scene bg campus with dissolve

    s_thoughts "I leave her office."

    s_thoughts "Pointing at the bars from the outside doesn't open them."

    s_thoughts "Sometimes it makes the person inside grip them harder."

    s_thoughts "I have been wanting to see behind Charlotte's mask since the first breakfast."

    s_thoughts "I have been pushing and watching and analyzing and asking and the whole time Charlotte has been smiling back and performing 'being seen' for me because that's what I wanted."

    s_thoughts "I wanted to see through her."

    s_thoughts "And Charlotte gave me exactly that. Like I was getting somewhere."

    s_thoughts "...Am I?"

    ## ===========================
    ## SCENE 29: 2AM BAKING
    ## Charlotte stress-baking alone. Sophia finds her.
    ## CHOICE 11.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "2 AM."

    s_thoughts "I can't sleep. The Nova thing. The Vermeer paper. The bars and the cage and the pointing."

    s_thoughts "I go downstairs for water."

    s_thoughts "The kitchen light is on."

    play music mus_2am fadein 3.0

    show charlotte pj smile at center with dissolve

    s_thoughts "Charlotte is at the counter. She's in pajamas. The cute yellow ones. Her hair is up in a clip."

    s_thoughts "She's baking."

    s_thoughts "There are four dozen cookies on the cooling rack. There's another batch in the oven. There's flour on her nose and her cheek and her left forearm."

    c "I couldn't sleep! I'm trying this new recipe. Lemon poppy seed. I thought the house might want--"

    s "It's 2 AM."

    c "I know! Time got away from me."

    s "There are four dozen cookies."

    show charlotte pj embarrassed at center

    c "For the house! For everyone!"

    s "There are five of us."

    c "Some of us like seconds."

    s "Nobody needs eight cookies each."

    show charlotte pj neutral at center

    c "...Okay. Maybe I'm stress baking. A little."

    s_thoughts "She says 'a little' while standing in a kitchen covered in flour with enough cookies to feed a classroom."

    menu:
        "\"What's stressing you?\"":
            $ charlotte_push += 1

            s "What's stressing you?"

            show charlotte pj smile at center

            c "Oh, nothing specific! It's just -- you know. The paper. And the Eve thing."

            c "And my sister called and she's having trouble in one of her classes and I can't DO anything from here, and my mom's medication got adjusted and she said she's fine but she always says she's fine, and the chore chart clearly isn't working and I don't know how to make it work without making everyone feel--"

            s_thoughts "She stops. Takes a breath."

            c "It's not a big deal! I just have a lot on my plate."

            s "You're making cookies because the plate is metaphorical and the cookies are literal."

            show charlotte pj surprised at center

            c "...Did you just psychoanalyze my baking?"

            s "Am I wrong?"

            show charlotte pj neutral at center

            c "No. Which is rude."

            s "Tell me about your mom's meds."

            show charlotte pj embarrassed at center

            c "They're adjusting them. It's routine. She's been on them for years. Sometimes they tweak the dosage and she gets -- she's fine. It's normal."

            s "You said 'fine' three times."

            c "Because she IS."

            s "Okay."

            c "She IS, Sophia."

            s "I said okay."

            show charlotte pj sad at center

            s_thoughts "Charlotte wraps cookies in wax paper. Her movements are precise. Controlled."

            c "When I was a kid, she... she didn't. The meds."

            s "...Oh."

            c "T-This isn't a big thing. I'm just baking and talking. People bake and talk."

            s_thoughts "She packages the cookies. One for each housemate, labeled with their name. Eve's label is the neatest."

            c "I should clean up."

            s "I'll help."

            c "You don't have to--"

            s "I know."

            s_thoughts "We clean the kitchen at 2 AM. Charlotte washes. I dry."

            jump charlotte_ch4_isabella_jealousy

        "\"Scoot over. I'll do the frosting.\"":
            $ charlotte_present += 1

            s "Scoot over."

            show charlotte pj surprised at center

            c "What?"

            s "I'll do the frosting. Where's the frosting?"

            c "You want to -- it's 2 AM."

            s "I'm aware. Frosting."

            show charlotte pj happy at center

            c "It's in the -- the bowl by the mixer. But you don't have to--"

            s "Charlotte. Frosting. Now."

            s_thoughts "She scoots."

            s_thoughts "I pick up the frosting bag. I have no idea what I'm doing."

            s "How do I--"

            c "You squeeze from the top. Gently."

            s_thoughts "I squeeze. The frosting comes out in a blob that looks like a crime."

            s "Nailed it."

            show charlotte pj laugh at center

            s_thoughts "Charlotte snort-laughs."

            s_thoughts "The farm animal one. The one she can't fake."

            c "That is OBSCENE."

            s "It's abstract."

            c "It's a BLOB."

            s "It's an impressionist blob."

            s_thoughts "I do the next one. Worse. On purpose."

            show charlotte pj happy at center

            c "Sophia, you're making them WORSE."

            s "I'm making them UNIQUE."

            c "You drew a -- is that supposed to be a face?"

            s "It's a self-portrait."

            show charlotte pj laugh at center

            s_thoughts "She's laughing. Really laughing. The kind where her whole body moves and her eyes close and she grabs the counter."

            c "Stop -- stop, you're wasting the -- Sophia--"

            s "I'm an artist. You can't rush art."

            c "That's not ART, that's a BIOHAZARD."

            s_thoughts "I draw something on the next cookie that is genuinely terrible. A flower. Allegedly."

            s_thoughts "Charlotte is crying. Laughing-crying."

            show charlotte pj smile at center

            s_thoughts "It's 2:30 AM. The kitchen is covered in flour. The cookies are hideous. Charlotte has frosting on her nose."

            s_thoughts "She wipes her eyes."

            c "These are the worst cookies I've ever seen."

            s "Best cookies."

            c "They look like they were decorated by a raccoon."

            s "A talented raccoon."

            show charlotte pj neutral at center

            s_thoughts "She's quiet for a second. Looking at the cookies."

            c "Thanks."

            s "For ruining your cookies?"

            c "For not asking what's wrong."

            s_thoughts "I look at her."

            s_thoughts "She looks at me."

            s_thoughts "2:30 AM. Flour everywhere. Frosting on her nose."

            s_thoughts "I don't ask what's wrong."

            s_thoughts "We eat cookies. They're terrible."

            s_thoughts "They're perfect."

            jump charlotte_ch4_isabella_jealousy

        "\"I'll let you do your thing.\"":
            $ charlotte_present -= 1

            s "I'll let you do your thing."

            show charlotte pj smile at center

            c "Okay! There'll be cookies in the morning!"

            s_thoughts "I go back to bed."

            s_thoughts "I lie there and listen to Charlotte baking alone at 2 AM."

            s_thoughts "The oven opens. Closes. A timer beeps. She resets it."

            s_thoughts "I could go back down."

            s_thoughts "She'd make it easy. She'd smile and hand me a cookie and pretend she wasn't standing in a flour-covered kitchen at 2 AM because she doesn't know how to sit still when her brain won't stop."

            s_thoughts "I roll over."

            s_thoughts "In the morning there are cookies labeled with everyone's name on the counter."

            s_thoughts "Eve's label is the neatest."

            jump charlotte_ch4_isabella_jealousy

    ## ===========================
    ## SCENE 30: ISABELLA'S JEALOUSY FLASH
    ## Brief. One involuntary moment.
    ## Isabella reaches for Charlotte and catches herself.
    ## ===========================

label charlotte_ch4_isabella_jealousy:

    stop music fadeout 1.5
    scene bg kitchen with Fade(0.8, 0.3, 0.8)
    play music mus_shift fadein 2.0

    s_thoughts "Morning."

    s_thoughts "Charlotte is making eggs. I'm sitting at the counter with coffee. Normal."

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte reaches up to the top shelf. The paprika. She's on her toes. Her shirt rides up. I'm staring at the strip of skin above her hip because I'm her girlfriend and I'm allowed to stare."

    show isabella neutral at right with dissolve

    s_thoughts "Isabella walks in."

    s_thoughts "Charlotte is still on her toes. Still reaching."

    s_thoughts "Isabella's hand moves."

    s_thoughts "Not toward the shelf. Toward Charlotte. Toward the small of Charlotte's back, the way you steady someone who's reaching too high."

    s_thoughts "The hand gets halfway there."

    s_thoughts "It stops."

    s_thoughts "Isabella's face does something. A flash -- recognition, then correction, then careful blankness."

    s_thoughts "Her hand drops. She picks up her mug instead."

    show isabella smile at right

    i "Careful. I lost a mug to that shelf."

    show charlotte laugh at left

    c "That was ONE time."

    i "It was my FAVORITE mug. The one with the cat."

    c "I got you a new cat mug!"

    i "It's not the same cat, Charlotte."

    s_thoughts "Normal. Easy. The bickering."

    s_thoughts "But I saw the hand."

    s_thoughts "Isabella's hand reaching for the small of Charlotte's back."

    s_thoughts "Isabella is looking at her phone now. The expression. The one I caught before."

    s_thoughts "She types something. Smiles at the screen. A private smile."

    s_thoughts "I don't say anything."

    s_thoughts "Charlotte didn't see the hand. Charlotte never sees the hand."

    hide charlotte
    hide isabella
    with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 36: THE SISTER CALL
    ## Charlotte's sister calls. Placed before the confession.
    ## The sister doesn't need Charlotte the way Charlotte needs to be needed.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)
    play music mus_charlotte fadein 2.0

    s_thoughts "I'm spending some time with Charlotte in the living room."

    s_thoughts "Charlotte's phone rings. She looks at the screen. Her face does the thing -- not the mom-thing, something warmer."

    show charlotte happy at center with dissolve

    c "Sophie! Hey!"

    s_thoughts "I'm on the couch. I can hear both sides."

    s_thoughts "Charlotte's voice is different with her sister. Not the mom-pitch. Closer to real."

    c "How'd the test go? Did you use the study method I--"

    s_thoughts "A pause. Charlotte's face flickers."

    c "Oh. You used a different one. That's -- that's great! Which one?"

    s_thoughts "Charlotte is nodding. Her grip on the phone is tight."

    c "Flashcards are totally -- I just thought the outline method might--"

    s_thoughts "Another pause."

    show charlotte neutral at center

    c "No, I know you can figure it out yourself! I just want to make sure--"

    s_thoughts "Even from here I can hear the voice on the other end. Young, exasperated, fond."

    s_thoughts "'Charlotte, I'm FINE.'"

    c "I know! I know. I just--"

    s_thoughts "'You always just.'"

    show charlotte sad at center

    s_thoughts "Charlotte is quiet."

    c "...You're right. I do always just."

    s_thoughts "The voice on the phone softens. Says something I can't make out."

    c "I'm proud of you. You know that, right? I'm really proud."
    
    show charlotte smile at center

    s_thoughts "She's smiling. The tired one."

    c "Love you too. Go study."

    s_thoughts "She hangs up."

    s_thoughts "Stands there for a second."

    show charlotte neutral at center

    c "She's growing up."

    s "I heard."

    c "She doesn't need me to -- she figured out her own study method. She used to call me before every test and I'd walk her through the outline thing and now she--"

    s_thoughts "She stops."

    c "She doesn't need me to check in this much. I just..."

    s_thoughts "She doesn't finish."

    s_thoughts "She goes to the kitchen. I hear the fridge open. Something being rearranged."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 31: EVE CONFRONTATION
    ## The real one. Eve says the devastating thing.
    ## Charlotte doesn't smile it away.
    ## ===========================

label charlotte_ch4_eve_confrontation:

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "A while later -- maybe an hour or so -- I walk into the kitchen and the air is wrong."
    
    play music mus_glass fadein 2.0

    show charlotte neutral at left with dissolve
    show eve neutral at right with dissolve

    s_thoughts "Charlotte is at the sink. Eve is by the fridge. They're not speaking."

    s_thoughts "The new chore chart -- the one Charlotte redid after the blowup -- is on the floor. Not torn down. Fallen. The magnet gave out."

    s_thoughts "Neither of them picked it up."

    e "You rearranged the fridge again."

    c "I was organizing--"

    e "My food. You rearranged my food."

    show charlotte smile at left

    c "Everything was -- it's more efficient if the--"

    e "Stop."

    s_thoughts "Eve's voice is different. Not the flat Eve-voice. Something underneath it."

    show eve annoyed at right

    e "I need to say something to you and I need you to not say 'of course' or 'it's fine' or make me tea."

    s_thoughts "Charlotte's hands find the counter. She grips it."

    show charlotte neutral at left

    c "Okay."

    e "You can't manage everything. I know you want to. I know it's how you--"

    s_thoughts "Eve pauses. Recalibrates."

    e "The chore chart. The fridge. The sponge. The way you reclean things. The way you fill in other people's schedules. The way you can't let a counter be slightly dirty or a dish sit in the sink or a person be slightly unhappy."

    c "I'm just trying to keep--"

    e "You're trying to control. It feels like helping and it is helping and it's also controlling. Both things are true."

    s_thoughts "Charlotte's knuckles are white on the counter."

    show eve neutral at right

    e "You want the house to be what you need it to be. And you're so busy making it perfect that you can't see it's suffocating."

    s_thoughts "The kitchen is silent."

    s_thoughts "Charlotte's jaw."

    s_thoughts "Not the flex. Not the hold."

    s_thoughts "Something let go."

    show charlotte sad at left

    s_thoughts "Her mouth opens. Closes."

    s_thoughts "Eve watches. She doesn't soften it. She doesn't add a 'but you're great' or an 'I don't mean to be harsh.'"

    s_thoughts "She lets it sit."

    e "I'm not saying this to be cruel. I'm saying it because nobody else will."
    
    s_thoughts "She looks at me as she says that. I try to keep my face blank. I don't."

    s_thoughts "Charlotte doesn't say 'of course.'"

    s_thoughts "Charlotte doesn't say anything."

    s_thoughts "Eve nods. Picks up the chore chart from the floor. Sets it on the counter."

    e "You should keep this. But let people fill in their own column."

    hide eve with dissolve

    s_thoughts "Eve leaves."

    s_thoughts "Charlotte stands at the counter."

    s_thoughts "She doesn't scrub. She doesn't smile. She doesn't make tea."

    s_thoughts "She just stands there."

    s_thoughts "I'm in the hallway. She doesn't know I'm here."

    s_thoughts "I watch her pick up the chore chart. Look at it. Fold it in half."

    s_thoughts "Put it in the recycling."

    s_thoughts "She doesn't put up a new one."

    hide charlotte with dissolve
    stop music fadeout 3.0

    ## ===========================
    ## SCENE 37: THE BODY BETRAYS HER
    ## Something involuntary. Something she can't "of course" away.
    ## Charlotte vulnerable sprite appears.
    ## ===========================

label charlotte_ch4_body_betrays:

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    s_thoughts "Friday."

    s_thoughts "Two days since Eve. Charlotte hasn't mentioned it."

    s_thoughts "She's been -- not bright. That's the thing. She's been Charlotte but the brightness is a shade off now."

    play music mus_charlotte_sad fadein 3.0

    show charlotte smile at center with dissolve

    s_thoughts "She's making dinner. Normal. Routine. The knife is hitting the cutting board in that even rhythm."

    c "I was thinking we could eat on the porch tonight. It's nice out."

    s "Sure."

    c "And I got that bread you like. The sourdough from the place on--"

    s_thoughts "She reaches for the bread."

    s_thoughts "Her hand misses."

    s_thoughts "Not by a lot. An inch. Maybe less. Her fingers close on air where the bread should be."

    s_thoughts "She adjusts. Grabs it."

    c "There we go!"

    s_thoughts "But I saw."

    s_thoughts "Her hand misjudged the distance. Her coordination -- Charlotte's coordination, the woman who chops vegetables in perfect rhythm and plates food like a restaurant -- was off by an inch."

    s_thoughts "She's cutting again. The rhythm is the same."

    s_thoughts "Except it isn't."

    s_thoughts "The knife hesitates. A fraction of a second between cuts. She covers it by adjusting her grip."

    show charlotte happy at center

    c "So the porch, yeah? I'll set it up."

    s_thoughts "She puts down the knife."

    s_thoughts "She puts it down because her hand is shaking."

    show charlotte vulnerable at center

    s_thoughts "Not a lot. A tremor. The kind you can hide by gripping the counter or picking something up or crossing your arms."

    s_thoughts "Charlotte looks at her hand."

    s_thoughts "She looks at it like it belongs to someone else."

    s_thoughts "She sees me seeing it."

    s_thoughts "And for the first time -- the very first time -- Charlotte cannot smile."

    s_thoughts "Her mouth moves. The muscles try. The corners attempt to lift."

    s_thoughts "They don't make it."

    c "I'm... Yeah."

    s_thoughts "That's all she says."

    c "Can we go outside?"

    s "Yeah."

    s_thoughts "She leaves the bread on the counter. The knife half-through a tomato."

    s_thoughts "She walks to the porch."

    s_thoughts "I follow."

    hide charlotte with dissolve

    ## ===========================
    ## SCENE 38: THE PORCH CONFESSION
    ## THE CLIMAX.
    ## CONDITIONAL: Push path gets rehearsed vulnerability.
    ## Present path gets the raw, broken version.
    ## CHOICE 15: +3 pivotal.
    ## ===========================

label charlotte_ch4_porch_confession:

    scene bg porch with dissolve

    s_thoughts "Charlotte sits on the step. Not the chair. The step. Closer to the ground."

    s_thoughts "I sit next to her."

    s_thoughts "The neighborhood is doing its evening thing. Someone's TV. A dog bark. The distant hum of cars on a road we can't see."

    ## CONDITIONAL CONFESSION
    ## Push path: charlotte_push > charlotte_present — rehearsed vulnerability
    ## Present path: charlotte_present >= charlotte_push — raw, broken version

    if charlotte_push > charlotte_present:
        ## === PUSH PATH: THE REHEARSED VERSION ===
        ## Charlotte delivers a packaged confession. It's real information
        ## but performed. She's giving Sophia what Sophia has been asking for.

        show charlotte sad at center with dissolve

        s_thoughts "Charlotte is quiet for a long time."

        s_thoughts "When she speaks, her voice is different. Not the bright-voice. Not the phone-voice."

        s_thoughts "Something she's practiced."

        c "I want to tell you something."

        s "Okay."

        c "I know you've been -- watching. Noticing. The things I do. The way I am. And you deserve to know why."

        s_thoughts "She takes a breath. Organized."

        c "My mom has bipolar disorder. She was diagnosed when I was seven. Before that, she was just -- she was Mom. And Mom was sometimes amazing. Spontaneous and fun and she'd wake us up at midnight to go look at the moon." 
        
        c "And sometimes Mom was gone. Not physically. She was in her room but she wasn't -- there."

        s_thoughts "Charlotte's hands are in her lap. Still. Controlled."

        c "When I was ten, she had a really bad episode. My dad was working double shifts. Sophie was five. And nobody made dinner."

        s "Charlotte."

        c "So I made dinner. I was ten and I couldn't really cook but I knew where the pasta was and I knew how to boil water. I made pasta and I set the table. Four places. Even though Mom wasn't coming down."

        s_thoughts "She pauses. Exactly the right length."

        c "I set her place anyway. Because if the table looked right, then everything was fine. And if everything looked fine, then it was fine."

        s_thoughts "I'm listening. I'm hanging on every word."

        s_thoughts "And something is wrong."

        s_thoughts "It's too clean. Too organized. Charlotte is confessing the way Charlotte does everything -- with structure, with care, with the awareness of what the listener needs."

        s_thoughts "She's performing vulnerability."

        s_thoughts "The information is real. The delivery is Charlotte."

        c "I learned to set extra places. To check the locks. To make sure Sophie got to school. To answer the phone on the first ring because what if it was important."

        c "My mom got better. She's on medication now. She's good. Our relationship is good. She calls me and I call her and it's warm and real."

        c "But I'm still setting extra places, Sophia. I'm still -- of course I'm still--"

        s_thoughts "She stops. Hears herself."

        s_thoughts "'Of course.' Even here. Even now."

        s_thoughts "Her eyes are dry."

        s_thoughts "She delivered the whole thing without crying. Without breaking. Without a single crack in the narrative."

        s_thoughts "Because Charlotte has told this story before. Maybe to herself. Maybe in the mirror. She's rehearsed it. She knows the beats."

        s_thoughts "She's giving me what I've been digging for."

        c "I know I'm too much. I know the chore chart is too much and the baking is too much and the way I rearrange people's food is too much. I just -- I don't know how else to be in a room with people."

        s_thoughts "She looks at me."

        s_thoughts "She looks at me the way Charlotte looks at everyone: gauging what I need."

        c "So. There it is."

        s_thoughts "There it is."

        s_thoughts "The story. The wound. The explanation. Delivered with the same precision as the chore chart."

        s_thoughts "I wanted behind the mask. Charlotte opened the door."

        s_thoughts "But the room behind the door is also decorated by Charlotte."

    else:
        ## === PRESENT PATH: THE RAW VERSION ===
        ## Charlotte delivers the unpackaged version. Half-sentences.
        ## Starts and stops. Can't finish thoughts.
        ## Broken. Real.

        show charlotte sad at center with dissolve

        s_thoughts "Charlotte doesn't say anything for a long time."

        s_thoughts "Not Charlotte-silence. Not the loaded pause before a pivot."

        s_thoughts "She's just sitting there. On the step. Looking at her hands."

        s_thoughts "When she starts talking, it doesn't sound like Charlotte."

        c "My mom..."

        s_thoughts "She stops."

        c "When I was -- there was a time when--"

        s_thoughts "She stops again."

        s_thoughts "She puts her head in her hands."

        c "I can't do this the way I planned to do this."

        s "You planned to do this?"

        c "I had a whole -- I've been thinking about how to say this for weeks. Months. Since before you. I have a VERSION, Sophia. A clean one. With the right pauses. I practiced it."

        s "So say the messy one."

        show charlotte neutral at center

        s_thoughts "She looks at me."

        s_thoughts "She looks at me and I can see her deciding. Not Charlotte-deciding, where she calculates the best angle. Just -- deciding whether to jump."

        c "My mom is bipolar."

        s_thoughts "She says it flat."

        c "She got diagnosed when I was seven. But it was -- before that -- she was already -- I didn't know the word for it. I just knew Mom had good days and bad days and the good days were really good and the bad days she didn't come out of her room."

        s_thoughts "Charlotte's voice is uneven. Not the practiced cadence."

        c "And I was -- Sophie was little. Sophie was four? Five? I don't remember. She was little enough that she didn't understand why Mom stayed in bed."

        s "Charlotte, you don't have to--"

        c "I want to."

        s_thoughts "She takes a breath. It shakes."

        c "I made dinner. I was ten. I don't know how old exactly -- I just remember the stool. I had to stand on a stool to reach the stove and I burned the first batch of pasta because I didn't know you had to stir it."

        s_thoughts "She laughs. It's not a laugh."

        c "And I set the table. And I set Mom's place even though she wasn't coming down. Because -- because if the table looked right--"

        s_thoughts "Her voice breaks."

        show charlotte sad at center

        c "I was ten, Sophia. I was ten and I was making sure the table looked like everything was fine because if the table was fine then the house was fine and if the house was fine then Mom would come down and if Mom came down then--"

        s_thoughts "She can't finish."

        s_thoughts "She's not crying. I don't know if she can right now."

        c "Sophie needed lunch. For school. I didn't know how to make sandwiches. I just -- I put bread and cheese together and cut the crusts off because Sophie didn't like crusts and I put it in her bag and she went to school and I went to school and we were fine."

        c "We were fine."

        c "We were always fine."

        s_thoughts "The 'of course' voice. But stripped. The skeleton of it."

        c "Mom got better. The medication. The therapy. She's good now. She's really good. I love her. Our relationship is good."

        s_thoughts "She says it like she's bracing for someone to argue."

        c "But I'm still -- I still check. I still set extra places. I still answer the phone on the first ring. I still--"

        s_thoughts "She gestures at the house behind us."

        c "I'm still standing on the stool."

        s_thoughts "The porch is quiet."

        s_thoughts "Charlotte is sitting on the step with her hands in her lap and she looks like a kid. Like the ten-year-old who learned to be fine."

        s_thoughts "And she looks terrified."

    ## === BOTH PATHS CONVERGE FOR THE CHOICE ===

    s_thoughts "..."
    
    s_thoughts "Charlotte is looking at her hands."

    s_thoughts "The porch light is on. The neighborhood is quiet."

    s_thoughts "She just told me the thing. The thing underneath the 'of course' and the smile and the chore chart and the eggs every morning."

    s_thoughts "She just told me why she sets extra places."

    menu:
        "Hold her.":
            $ charlotte_present += 3

            s_thoughts "I put my arms around her."

            s_thoughts "She's rigid for a second. Like she didn't expect it. Like being held is something she gives, not something she receives."

            s_thoughts "Then she folds."

            show charlotte sad at center

            s_thoughts "She leans into me. Her face against my shoulder. She's breathing unevenly."

            s_thoughts "She cries. A little. The acceptable kind -- the kind that says 'I'm having a feeling' without saying 'I'm breaking.'"

            c "I'm okay."

            s_thoughts "She says it into my shoulder."

            c "I'm fine."

            s "You don't have to be."

            c "I know. I know. I'm just -- I'm okay."

            s_thoughts "She pulls back. Wipes her eyes. The mask reassembles."

            show charlotte smile at center

            s_thoughts "It's fast. Practiced. She was vulnerable and now she's not and the vulnerability was real but the recovery was performed."

            c "Sorry. I didn't mean to--"

            s "Don't apologize."

            c "Of course. Sorry. I mean --"

            s_thoughts "She laughs. The tired one."

            c "Thank you. For listening."

            s "Always."

            s_thoughts "She leans her head on my shoulder. The porch light hums."

            s_thoughts "I held her. She let me."

            s_thoughts "But 'I'm fine' came back so fast."

            s_thoughts "I wonder if she told me so she could stop carrying it, or if she told me because she could feel me reaching for it."

            s_thoughts "I wonder if Charlotte knows the difference."

            jump charlotte_ch4_act3_end

        "\"You don't have to set them anymore.\"":
            $ charlotte_push += 3

            s "You don't have to set them anymore."

            show charlotte surprised at center

            s_thoughts "Charlotte looks at me."

            s_thoughts "Really looks at me. Not the gauging look. Not the 'what does she need' look."

            c "I don't know how to stop."

            s "I know."

            c "I don't know who I am if I'm not -- if I'm not doing the thing. The plates. The chart. The eggs. If I stop doing all of that, what's left?"

            s "..."

            c "What's LEFT, Sophia?"

            s_thoughts "Her voice cracks."

            s "You. Whatever that is. That's left."

            show charlotte sad at center

            c "You don't know what that is. I don't know what that is."

            s "I know."

            c "Then how can you--"

            s "I don't have to know. I just have to be here."

            s_thoughts "Charlotte stares at me."

            s_thoughts "The porch light buzzes."

            c "Of course you know."

            s_thoughts "She says it quiet."

            c "You notice everything."

            s "Not everything."

            c "More than anyone."

            s_thoughts "She's not crying. She's past the place where crying helps."

            s_thoughts "But her face is open. Not the performed open. Not the mask with the crack. Just -- open. The way a room looks when all the furniture is gone and you can see the walls."

            c "I'm still standing on the stool."

            s "I heard you."

            c "I've been standing on the stool for ten years."

            s "I know."

            c "..."

            c "You can't fix that."

            s "I'm not trying to."

            s_thoughts "She looks at me for a long time."

            s_thoughts "Then she puts her head on my shoulder."

            s_thoughts "Not the performed lean. Not the romantic gesture. Just -- weight. Charlotte's actual weight. Resting."

            s_thoughts "She doesn't say 'of course.'"

            s_thoughts "She doesn't say anything."

            s_thoughts "The porch light hums."

            s_thoughts "We sit."

            jump charlotte_ch4_act3_end

        "\"I'm glad you told me.\"":
            $ charlotte_present -= 3
            $ charlotte_push -= 3

            s "I'm glad you told me."

            show charlotte neutral at center

            s_thoughts "Charlotte's face reads it instantly."

            s_thoughts "Not anger. Not disappointment."

            s_thoughts "Recognition."

            s_thoughts "She performed vulnerability and got a performance back."

            c "Of course."

            s_thoughts "The mask slides on. Harder than before. Like someone slamming a door they'd been holding open."

            show charlotte happy at center

            c "We should eat. The bread's still on the counter."

            s "C-Charlotte--"

            c "I'm fine! Really. That was -- it was good to talk about it. I feel better."

            s_thoughts "She doesn't feel better."

            s_thoughts "She feels like she opened a door and nobody walked through."

            s_thoughts "And the door is closing."

            s_thoughts "And I let it."

            c "Come on. I'll finish the tomato."

            s_thoughts "She goes inside."

            s_thoughts "I sit on the porch."

            s_thoughts "I said the polite thing. The kind thing. The empty thing."

            s_thoughts "Charlotte deserved more than 'I'm glad you told me.'"

            s_thoughts "She deserved someone who would sit on the step and not need a response."

            s_thoughts "I gave her a receipt instead."

            jump charlotte_ch4_act3_end

    ## ===========================
    ## SCENE 35: ACT 3 END
    ## Note: coda cut during revision.
    ## The end of Scene 34 hits by itself.
    ## ===========================

label charlotte_ch4_act3_end:

    stop music fadeout 3.0
    hide charlotte with dissolve
    
    scene black with Fade(1.5, 0.5, 1.5)
    "Chapter 4: Honeymoon -- End"
    
    ## ===========================
    ## END OF ACT 3 / END OF CHAPTER 4
    ## ===========================

    jump charlotte_ch5
