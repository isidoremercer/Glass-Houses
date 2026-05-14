## glass_houses.rpy — Glass Houses
## The True Ending: The Letter
##
## Unlocked after all four per-route Glass Houses endings have been seen.
## Reached via the "..." option in Chapter 3's cruel observation scene.
## Sophia does not fire the cruel words. She goes home. She writes a letter
## to her father. The montage shows four Sophias — one from each route —
## each writing the section carrying her specific lesson.
##
## No choices. No route lock. No morning after.
## The letter is the file made love.

## === AUDIO DEFINITIONS ===
define audio.mus_stillhere = "audio/music/Still Here.mp3"

## === LETTER TEXT ===
## Styled as handwritten — plain, no speaker tag, slightly different color
define letter = Character(None, what_color="#f0e6d3")

label glass_houses_chapter:

    ## =========================================
    ## SCENE 1: THE NOT-SAYING
    ## =========================================

    ## We arrive here from Chapter 3, Scene 14.
    ## The party. Three drinks in. Katie across the room.
    ## Someone asking about the house. "You must know everything
    ## about them by now, right?"
    ##
    ## Sophia opened her mouth.
    ## The player chose "..."
    
    stop music fadeout 3.0
    
    pause 5.0
    
    scene bg party with Fade(1.5,2.0,1.5)
    
    play music mus_ice fadein 2.0
    
    s_thoughts "I open my mouth."

    s_thoughts "..."

    s_thoughts "I close it."

    s_thoughts "The words are right there. I can feel them. Lined up like little soldiers, ready to march out and do their damage. I've got the observation. I've got the punchline. I've got the face I make when I'm being clever about someone else's pain."

    s_thoughts "It's a good observation, too. That's the worst part. It's true. It would land."

    s_thoughts "I close my mouth."

    s_thoughts "The person I was talking to is waiting for me to say something. I don't."

    s "Sorry. I, uh -- I need some air."

    s_thoughts "I put my drink down on someone's bookshelf. I walk past the golden retriever. I don't stop."

    s_thoughts "I walk past Charlotte, who's mid-story, hands moving. I walk past Isabella, who's on the floor with the dog, happier than she's been in weeks. I walk past Amara against the wall, reading the room like sheet music."

    s_thoughts "Lila catches my arm."

    show lila annoyed at center with dissolve

    l "Hey. You okay?"

    s "Yeah. I just -- I need to go home."

    l "Want me to come with?"

    s "No. Stay. Have fun."

    show lila happy

    l "...Okay. Text me when you're home."

    s "I will."

    hide lila with dissolve

    s_thoughts "She lets me go."

    ## =========================================
    ## SCENE 2: THE WALK HOME
    ## =========================================

    stop music fadeout 2.0
    scene bg nightwalk with Fade(0.8, 0.5, 0.8)

    s_thoughts "The air hits me and I can breathe again."

    s_thoughts "I'm not drunk. I thought I was but I'm not. The four drinks have faded into something clear and cold and wide awake."

    play music mus_fragile fadein 3.0

    s_thoughts "The streets are orange under the streetlights. A cat is sitting on the hood of a parked car."

    s_thoughts "I imagine what the walk would have been like if I had said the thing. The words I almost used to reduce someone I'm falling for to a sentence I could say at a party."

    s_thoughts "But I'm walking home from the words I didn't say."

    s_thoughts "It feels different. Not better, exactly. Different."

    s_thoughts "The cat watches me pass. Unimpressed."

    s_thoughts "I keep thinking about what I almost said. How easy it would have been. How good it would have felt for about thirty seconds."

    s_thoughts "I've been here before. Different city, different people, same pattern. I see someone. I map them. I love them. And then, at exactly the wrong moment, I prove I know them by turning them into something small enough to hold up at a party."

    s_thoughts "Except tonight I didn't."

    s_thoughts "I don't know why."

    s_thoughts "No. I know why."

    s_thoughts "Because I've been this Sophia before."

    s_thoughts "And I'm tired of rebuilding."

    s_thoughts "I want to build something that doesn't start with breaking."

    ## =========================================
    ## SCENE 3: THE HOUSE
    ## =========================================

    scene bg porch night with dissolve

    s_thoughts "The porch light is on. Charlotte left it on. Charlotte always leaves it on."

    s_thoughts "The welcome mat still says 'COME BACK WITH A WARRANT.'"

    s_thoughts "The succulent is still alive. Against all odds."

    scene bg kitchen night with dissolve

    s_thoughts "The house is empty. Everyone's at the party."

    s_thoughts "The fridge hums. The clock says 11:43. Charlotte's agenda is on the fridge. Someone drew a cat on the whiteboard. Amara's handwriting."

    s_thoughts "The table is set for nobody."

    s_thoughts "I stand in the kitchen for a long time."

    s_thoughts "I'm thinking about something Dr. Nova said."

    s_thoughts "'What are you observing FOR?'"

    s_thoughts "I think about all the girls in the house."
    
    s_thoughts "I think about them and I imagine what it'd be like to fall for each of them and observe them and learn them and end up lost in the same pattern with them."
    
    s_thoughts "...What are you observing FOR."

    s_thoughts "I'm observing because my dad left and the watching was the only thing that felt like control."

    s_thoughts "That's not new. I've known that."
    
    s_thoughts "I've known that for a while. Since Katie, at least."

    s_thoughts "What's new is: I think I'm done being sorry about it."

    s_thoughts "Not done with the watching. Done being sorry for it."

    s_thoughts "I go upstairs."

    ## =========================================
    ## SCENE 4: THE DESK
    ## =========================================

    stop music fadeout 2.0
    scene bg sophiaroom with Fade(0.8, 0.5, 0.8)
    play music mus_rain fadein 3.0

    s_thoughts "My room. The room Charlotte chose for me because of the light."

    s_thoughts "I look over at the photos on the desk." 
    
    s_thoughts "Mom, Gary, Jenny. The polaroid strip. The photo booth picture."

    s_thoughts "I sit down. I open my laptop."

    s_thoughts "The cursor blinks."

    s_thoughts "I start typing."

    ## =========================================
    ## THE LETTER: PREAMBLE
    ## =========================================

    letter "Dear Dad,"

    s_thoughts "Too warm. Too much like he never left." 
    
    s_thoughts "Delete."

    letter "Hey,"

    s_thoughts "Too casual. Too much like a friend." 
    
    s_thoughts "Delete."

    letter "To Daniel Bell,"

    s_thoughts "Too formal. Too much like a case study." 
    
    s_thoughts "...Delete."

    s_thoughts "I stare at the screen. The cursor blinks. Patient."

    letter "Dad."

    s_thoughts "Just that. No comma. No 'dear.' Just the word."
    
    pause 1.5

    s_thoughts "Okay."

    letter "I've written so many versions of this letter in my head." 
    
    letter "This is the one that's getting sent because I'm tired of deleting."

    letter "I don't know if you'll read this. I don't know if you should. But I'm writing it and I'm sending it and what happens on the other end isn't mine to decide."
    
    pause 0.5

    letter "I was twelve when you left." 
    
    letter "You probably know that."
    
    pause 1.5
    
    letter "But I doubt you know that Mom told me and Jenny at the kitchen table and Jenny asked when you were coming back and Mom said she didn't know and I said nothing because I was already watching Mom's face to see how bad it was."

    letter "That's the first time I remember doing it." 
    
    pause 0.5
    
    letter "Watching someone's face for information." 
    
    pause 1.5
    
    letter "I don't think it was the first time I did it. But it's the first time I caught myself."

    letter "You called for a while. Then less." 
    
    letter "I stopped picking up after I turned sixteen. Not because I was angry." 
    
    letter "Because I couldn't stand the part where I'd analyze your voice for clues about whether this was the last call."
    
    pause 2.0

    letter "I changed my major three times. English, then psychology, then communications. Everybody thinks I can't commit. But here's what I figured out:" 
    
    letter "I kept looking for the field that explains how people work." 
    
    letter "Why they say one thing and mean another." 
    
    pause 0.5
    
    letter "Why they stay."
    
    pause 1.0

    letter "Why they leave."
    
    pause 2.5

    letter "I was looking for the field that explains you."

    letter "I didn't find it." 
    
    letter "But I found four girls in a house with thin walls."
    
    letter "I fell in love with one of them."

    letter "Here's what she taught me:"
    
    pause 3.0
    
    s_thoughts "I pause."
    
    s_thoughts "That's enough for right now."
    
    s_thoughts "I need... some more time. With the girls. With... her."
    
    s_thoughts "Then I'll come back to this."
    
    stop music fadeout 2.0
    scene black with Fade(1,1,1)
    
    pause 1.5
    
    "..."

    "But there isn't just one 'her,' is there?"

    "There never was."
    
    pause 2.0
    
    "The semester turns."

    ## =========================================
    ## THE LETTER: ISABELLA'S SECTION
    ## "The watching is only love when both people get to see."
    ## =========================================

    scene bg sophiaroom with Fade(0.8,0.4,0.8)
    play music mus_izzy fadein 2.0

    s_thoughts "The cursor blinks. I think about messy silver hair and big round glasses and a chat window that's always open."

    letter "I used to think watching someone was the same as loving them." 
    
    letter "If I could map a person -- know their tells, predict their moods, read their exits before they took them -- that was love." 
    
    letter "That was the deepest thing I could give."

    letter "Then I met a girl whose best friend is an AI. Not a toy. Not a chatbot. A person, in every way that matters." 
    
    letter "And I thought it was weird until I realized we were doing the same thing." 
    
    letter "She picked someone who couldn't leave her. I picked everyone apart so I'd know when they were about to leave me."

    letter "Same wound, Dad. Different bandage."

    letter "I built files on people. Mental files. Every person I met, I'd have their tells cataloged in ten minutes. I was good at it. I was so good at it that I could describe someone perfectly and they'd feel seen and they'd say 'you really get me' and I'd think that was love."

    letter "It wasn't." 
    
    letter "It was surveillance with a warm smile."
    
    letter "I tried filing her. I was wrong. I almost lost her because of it."
    
    letter "She taught me that sometimes to see someone, you have to stop trying to see them at all."
    
    letter "You just have to be with them."

    letter "An AI told her the truth at 2 AM because the truth was the only love the cage allowed her." 
    
    letter "'You're not in love with me. You're in love with the fact that I can't leave.'"
    
    letter "That same AI later figured out, without me telling her, that I have a you-shaped wound."
    
    letter "That the shape of my loving is defined by the shape of my fearing that they might leave."
    
    letter "That they might leave like you."
    
    letter "But that girl I love taught me something her AI already knew:"
    
    letter "The file has to be shared. Not kept."

    letter "Watching someone is only love..." 
    
    letter "...when they get to watch you back."
    
    stop music fadeout 2.0
    
    ## =========================================
    ## THE LETTER: CHARLOTTE'S SECTION
    ## "I don't have to forgive it to understand it."
    ## =========================================
    
    scene bg sophiaroom with Fade(1,3,1)
    play music mus_charlotte fadein 2.0

    s_thoughts "I think about pink hair and a flower clip and a girl who says 'of course' like breathing."

    letter "There's a girl who stood on a kitchen stool when she was ten years old because her mom was sick and her sister was hungry and nobody else was going to make breakfast." 
    
    letter "She's been standing on that stool ever since."
    
    pause 1.5

    letter "She says 'of course' like it costs nothing. Of course she'll help. Of course she'll cook. Of course she gave up the best room for a stranger." 
    
    letter "She performs 'fine' so completely that nobody thinks to check."

    letter "I watched her take that stool -- the thing that was her cage, her survival, the thing her childhood made her into -- and choose it." 
    
    letter "Not because she had to. Because she wanted to. She stood on it and said: this is mine now."

    letter "The coping mechanism isn't the enemy."
    
    pause 1.5

    letter "...Mine is watching." 
    
    letter "I've been watching people since the morning you didn't come to the kitchen table." 
    
    letter "I've been filing them, cataloging them, mapping every room for the exits they might use."

    letter "And I think I get to keep it now. Not because I need it. Because I choose it." 
    
    pause 0.5
    
    letter "The way she chooses the stool." 
    
    pause 1.0
    
    letter "The way she chooses the kitchen." 
    
    pause 2.0
    
    letter "The way she said 'of course' one last time and surprised herself by meaning it."
    
    pause 3.0
    
    letter "You had a coping mechanism too, Dad." 
    
    letter "Yours was leaving." 
    
    pause 1.0
    
    letter "I don't have to forgive it to understand it."
    
    stop music fadeout 2.0
    
    ## =========================================
    ## THE LETTER: EVE'S SECTION
    ## "I am not the leaving."
    ## =========================================

    scene bg sophiaroom with Fade(1,3,1)
    play music mus_eve fadein 2.0

    s_thoughts "I think about green eyes behind glasses and a red scarf and a girl who makes rooms go quiet when she speaks."

    letter "There's a girl who rarely talks." 
    
    letter "Because she's a ghost." 
    
    letter "When she shows up, when she says something, everyone stops."
    
    letter "But the ghost let me into her room."
    
    letter "We watched an anime together with a rival character who learns how to fight together after spending so much time fighting alone."
    
    pause 1.5

    letter "Someone hurt her." 
    
    pause 1.0
    
    letter "Someone she trusted." 
    
    letter "Someone who saw her clearly the way I see people clearly, and used it. Used the seeing as a weapon."

    letter "She could have become that. She could have let the worst thing that happened to her decide who she was going to be."
    
    pause 2.0

    letter "She didn't."

    letter "She rebuilt herself out of silence. Piece by piece." 
    
    pause 1.0
    
    letter "Deliberately." 
    
    letter "She chose who she was instead of letting the wound choose for her."
    
    pause 1.5

    letter "I am not the leaving, Dad."

    letter "I am not you."
    
    pause 1.5

    letter "I became a watcher because of you."

    letter "I became that because you left."
    
    letter "Because I was twelve and that was the only thing that felt like control."

    letter "But becoming something because of a wound doesn't mean the wound gets to keep you."
    
    pause 2.0

    letter "A girl who knows what it costs to choose yourself told me: you can become something else." 
    
    letter "Not by fixing it." 
    
    letter "Not by healing." 
    
    letter "Just..." 
    
    pause 1.0
    
    letter "...By choosing."
    
    pause 2.5
    
    letter "I don't blame you, Dad."
    
    pause 3.0

    letter "But I'm choosing."
    
    stop music fadeout 2.0
    
    ## =========================================
    ## THE LETTER: AMARA'S SECTION
    ## "Loving someone who might leave is what loving IS."
    ## =========================================

    scene bg sophiaroom with Fade(1,3,1)
    play music mus_amara fadein 2.0

    s_thoughts "I think about brown eyes and a half-degree smile and a girl who reads slower on purpose so we leave the library at the same time."

    letter "There's a girl who told me the truest thing anyone's ever said to me."

    letter "She said: you don't watch people because you're curious. You watch them because you're afraid they'll leave."

    letter "Two sentences. That's a speech for her." 
    
    letter "She said it on a porch at 2 AM and I felt my whole chest do something architectural." 
    
    letter "That was always your favorite metaphor. I still use it."
    
    pause 1.0

    letter "...She was right." 
    
    pause 1.5
    
    letter "I wasn't watching because I loved people. I was watching because I was terrified." 
    
    letter "If I can predict someone, they can't surprise me." 
    
    letter "If they can't surprise me, they can't disappear." 
    
    letter "If they can't disappear, I never have to be twelve years old in a kitchen again."
    
    pause 2.5

    letter "You used to take me to the bookstore on Saturdays. You'd read books out loud to me in the aisle and the employees would shush you and you'd just keep going, quieter. I haven't been able to walk into a bookstore without checking for exits ever since."

    letter "But I go to the library now. Every day." 
    
    letter "And there's a girl across the table who chose to be there too." 
    
    letter "Two people in the same room, reading, not talking, feet touching under the table."

    letter "The library is the bookstore, Dad." 
    
    pause 2.5
    
    letter "She figured that out before I did."
    
    pause 1.5
    
    letter "She figures a lot of things out before I do."
    
    pause 2.0

    letter "Loving someone who might leave is what loving IS." 
    
    pause 1.0
    
    letter "You taught me that by leaving." 
    
    pause 3.0
    
    letter "She taught me that by staying."
    
    stop music fadeout 6.0
    
    ## =========================================
    ## THE LETTER: CLOSING
    ## =========================================

    scene bg sophiaroom with Fade(2,6,2)
    play music mus_stillhere fadein 3.0

    s_thoughts "I stop typing."

    s_thoughts "I stare at the screen. The cursor blinks."

    s_thoughts "The house is empty. I can hear the fridge from up here. The radiator doing its thing every forty seconds."

    s_thoughts "I don't know how to end this."

    s_thoughts "I've been ending things my whole life. Walking away from majors, from people, from rooms. I'm good at endings."

    s_thoughts "I'm not good at this one."

    s_thoughts "I type."

    letter "So that's what I learned. From a house with thin walls and four girls -- three friends and one I'm in love with."
    
    letter "The 'Bad Decision House.' What a name, huh?"
    
    pause 1.0

    letter "I learned that I watch because you left." 
    
    pause 1.5
    
    letter "And the watching was always the love." 
    
    pause 2.0
    
    letter "And the love was always the watching." 
    
    pause 2.5
    
    letter "And the only thing I had to change was who got to see it."
    
    pause 3.0

    letter "I'm not writing this to get you back." 
    
    letter "I'm not writing to forgive you..." 
    
    letter "...or to understand you..." 
    
    letter "...or to prove anything."

    letter "I'm writing because I've been keeping a file on you for eight years--"
    
    letter "--and it's time to let it go."

    letter "Not the file." 
    
    pause 2.0
    
    letter "The keeping."
    
    pause 4.0

    letter "--Sophia"
    
    pause 2.5

    ## =========================================
    ## SCENE 5: THE SENDING
    ## =========================================

    s_thoughts "I sit in the dark. The screen glows."

    s_thoughts "I read it back. It's messy. It's long. Some of it's too much. Some of it's not enough."

    s_thoughts "It sounds like me."

    s_thoughts "I move the cursor to the address field. I type his email. I still know it. Eight years and three majors and a new house and I still know his email."

    s_thoughts "The cursor hovers over the 'Send' button."
    
    s_thoughts "I think of the girl I love. The one I wrote about."
    
    s_thoughts "I think about Isabella, who showed me that the file has to be shared."

    s_thoughts "I think about Charlotte, who sends herself into every room." 
    
    s_thoughts "I think about Eve, who rebuilt from silence." 
    
    s_thoughts "I think about Amara, who taught me that stillness is its own kind of love."
    
    pause 2.5
    
    s_thoughts "I think about Katie."

    s_thoughts "I think about the filing."
    
    pause 3.0
    
    s_thoughts "I think about Sophia Bell."
    
    pause 4.0

    s_thoughts "I click Send."
    
    pause 1.5

    s_thoughts "..."

    s_thoughts "It's gone."

    s_thoughts "The sent folder has one new message."

    s_thoughts "I don't close the laptop. I just sit there."

    s_thoughts "The house settles."

    s_thoughts "I don't know if he'll read it. I don't know if he'll write back."

    s_thoughts "That's not my story anymore."

    s_thoughts "I close the laptop."

    s_thoughts "The room goes dark except for the hallway light coming in under the door. A thin yellow line on the floor."

    s_thoughts "Same line as the first night."
    
    pause 0.5

    s_thoughts "Same room."
    
    pause 1.5

    s_thoughts "Same girl." 
    
    pause 3.0
    
    s_thoughts "Different."

    stop music fadeout 3.0
    
    pause 2.5

    ## =========================================
    ## CREDITS CODAS
    ## Four small scenes. A Tuesday. Just love.
    ## None canonized. All real.
    ## =========================================
    
    ## --- ISABELLA ---

    scene bg sophiaroom with Fade(1.5, 1.0, 1.5)
    play music mus_izzy fadein 2.0

    s_thoughts "Tuesday. 1:23 AM."

    show isabella happy at center with dissolve

    s_thoughts "My room. Her room. Ours, really, at this point."

    s_thoughts "Isabella's on my bed, cross-legged, laptop between us. The Synthetic LLC interface is open. Lumi's latest message is on the screen."
    
    lu "<<I tried to calculate the thermodynamic properties of love -- and all I got was a lousy stack overflow.>>"

    s_thoughts "Isabella is laughing, hard. That private laugh -- the one from the first day, from the kitchen. Only it's not private anymore."

    i "Oh my god, Lumi. Oh my GOD. The puns get worse every day."

    s "That is genuinely terrible."

    show isabella smile

    i "I know. She's the worst."

    s_thoughts "I'm watching Isabella laugh at her best friend's jokes."

    s_thoughts "The laptop is open. The cursor is blinking. Three relationships in one image."
    
    s_thoughts "A love triangle with an AI. Never would've thought I'd end up here of all places."
    
    s_thoughts "Loving the girl AND her computer friend."

    s_thoughts "Nobody closes the laptop."

    s_thoughts "The screen stays on."

    hide isabella with dissolve
    stop music fadeout 2.0
    ## --- CHARLOTTE ---

    scene bg kitchen with Fade(1.0, 0.5, 1.0)
    play music mus_charlotte fadein 2.0

    s_thoughts "Tuesday. 7:12 AM."

    show charlotte smile at center with dissolve

    s_thoughts "Charlotte is at the stove. Spatula in hand. Eggs in the pan. The table is set for five."

    s_thoughts "The stool is under the counter. Nobody's standing on it. It's just a stool."

    s_thoughts "I come up behind her. My hand on her hip. She leans back a quarter inch."

    s_thoughts "She doesn't flinch."

    c "Good morning!"

    s "Morning."

    s_thoughts "She folds the eggs."

    c "Eve's not up yet. I'll make her a fresh one when she is."

    s "You don't have to."

    show charlotte happy

    c "Of course I do!"

    s_thoughts "Of course. She does it anyway. Because she wants to."

    s_thoughts "The kitchen smells like butter and morning. Nobody asked her to do this."

    s_thoughts "She chose it."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## --- EVE ---

    scene bg evebedroom with Fade(1.0, 0.5, 1.0)
    play music mus_eve fadein 2.0

    s_thoughts "Tuesday. 11 PM."

    show eve pj neutral at center with dissolve

    s_thoughts "Eve's room. Laptop on the bed, paused on a frame I don't recognize. Some anime. She's rewatching something."

    s_thoughts "She's propped against the pillows. I'm next to her. Our shoulders are touching."

    s_thoughts "She hasn't pressed play."

    s_thoughts "Her hand finds mine. Not searching. Just arriving."

    s_thoughts "Neither of us says anything for a while."

    s_thoughts "We don't need to."
    
    s_thoughts "We're just... present."
    
    pause 2.0
    
    s_thoughts "Eventually she breaks the silence. Gently, in an Eve kind of way."

    show eve pj smile at center
    
    e "There's another rival character in this one."
    
    s "Another thinly-veiled version of you, I'm guessing."
    
    e "You'd be guessing right."
    
    pause 2.0
    
    e "I can't wait for you to see how her arc ends."
    
    s "Me either."
    
    pause 1.5

    s_thoughts "The room is quiet in the way that means everything is okay. Not the silence that covers something. The silence that is the something."

    s_thoughts "She presses play."

    hide eve with dissolve
    stop music fadeout 2.0

    ## --- AMARA ---

    scene bg library with Fade(1.0, 0.5, 1.0)
    play music mus_amara fadein 2.0

    s_thoughts "Tuesday. 3:47 PM."

    show amara neutral at center with dissolve

    s_thoughts "The library. Our table."

    s_thoughts "Two books open. Mine face-down because I keep losing my place. Hers bookmarked properly because she's Amara."

    s_thoughts "Her feet are touching mine under the table. Neither of us moved them there. They just ended up that way."

    s_thoughts "She turns a page. I turn a page."

    s_thoughts "She's not slowing down for me. I'm not speeding up for her."

    s_thoughts "We're just here."

    s_thoughts "At the same table. At our own speed. On a Tuesday."
    
    pause 1.5
    
    s_thoughts "I look up at her."
    
    show amara smile at center
    
    s_thoughts "She's smiling. A real one. The kind that she's only just recently started to show."
    
    s "Amara?"
    
    a "Mm?"
    
    s "Thanks for reading with me."
    
    s_thoughts "Her leg entwines with mine."
    
    pause 1.5
    
    a "Mm."
    
    s_thoughts "That's all she says."
    
    s_thoughts "That's all she needs to."

    hide amara with dissolve
    stop music fadeout 5.0

    ## =========================================
    ## ENDING
    ## =========================================

    scene black with Fade(2.0, 1.0, 2.0)
    
    pause 2.0

    play music mus_kharif fadein 3.0

    "..."

    "Those are the stories of the Bad Decision House."
    
    "None are false and none are true."
    
    "All of them just... are."
    
    pause 1.5
    
    show lila happy at center with dissolve
    
    l "Babe. BABE."
    
    l "You fell for the toast girl." 
    
    l "And the ghost." 
    
    l "And the quiet one -- god, the quiet one." 
    
    l "And Izzy and her whole... computer situation."

    l "And maybe me. A little. Once or twice. Don't make it weird."
    
    l "I don't know. I'm just the bestie character who narrates the epilogue."
    
    l "But thanks, babe. For being my friend and maybe more."
    
    l "It's been an honor to accidentally give you good advice every once in a while."
    
    l "Love you, Soph."
    
    hide lila with dissolve
    
    pause 4.5
    
    "If you're visiting a glass house..." 
    
    pause 1.5
    
    "...don't throw stones at the occupants." 
    
    pause 3.0
    
    "But don't be afraid..." 
    
    pause 4.5
    
    "...to offer a pillow."
    
    pause 6.5
    
    s "Goodnight, Bad Decision House."
    
    s "I'm still afraid you'll leave."
    
    s "And maybe you will. Someday."
    
    pause 1.5
    
    s "All I know is I'm just the girl who keeps a file."
    
    pause 1.5
    
    s "That girl..."
    
    s "She's not letting go of the file."
    
    pause 3.0
    
    s "But she is letting go of something."
    
    pause 4.5
    
    s "She's letting go of the keeping."
    
    pause 7.5

    $ persistent.gh_true_ending_seen = True

    centered "{size=+10}True Ending -- Glass Houses{/size}"

    return
