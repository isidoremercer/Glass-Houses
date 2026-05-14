## script.rpy -- Glass Houses
## Chapter 1: Move-In Day

## === AUDIO DEFINITIONS ===
define audio.mus_afternoon = "audio/music/Afternoon Study Session.mp3"
define audio.mus_sunlight = "audio/music/Sunlight.mp3"
define audio.mus_baddecisions = "audio/music/Bad Decisions.mp3"
define audio.mus_couch = "audio/music/The Couch Knows.mp3"
define audio.mus_2am = "audio/music/House at 2AM.mp3"
define audio.mus_time = "audio/music/Moments Across Time.mp3"
define audio.mus_morningafter = "audio/music/The Morning After The Hard Thing.mp3"
define audio.mus_fivepeople = "audio/music/Five People in a Kitchen.mp3"
define audio.mus_kharif = "audio/music/Kharif.mp3"

label start:

    ## Game starts at Chapter 1. Chapter select is available from main menu.
    jump chapter1

label chapter1:

    ## ===========================
    ## SCENE 1: ARRIVAL
    ## ===========================

    play music mus_afternoon fadein 2.0
    scene bg street with fade

    s_thoughts "Okay. This is it."

    s_thoughts "23 Linden Street."

    s_thoughts "The place where I become a person who has her life together."

    s_thoughts "...Is what I would say if I hadn't just dropped my phone in a puddle getting out of the taxi."

    s_thoughts "It still works. Probably. The screen is doing a thing but it's always been doing a thing."

    s_thoughts "The house is at the end of the block -- this big old Victorian that used to be white and gave up on the idea."

    s_thoughts "The paint peels in long strips. The house is molting."

    s_thoughts "There's a wrap-around porch with a railing that's missing a spindle. A tree out front that's older than the building and twice as stubborn."

    s_thoughts "One of the upstairs windows has a curtain that's slightly crooked."

    s_thoughts "It's ugly. It's beautiful. I love it already."

    s_thoughts "The listing said 'charming Victorian with character.' In real estate that means the plumbing has opinions."

    s_thoughts "But it's cheap, it's close to campus, and the ad specifically said 'we're all a little weird here, no bigots please.'"

    s_thoughts "I applied in fourteen seconds. I didn't even read the whole thing."

    s_thoughts "That's... probably a pattern I should examine at some point."

    s_thoughts "Not today though."

    s_thoughts "I pick up my bags. Two overstuffed duffels, a backpack that's been slowly unzipping itself since the bus station."

    s_thoughts "And a tote bag from a bookstore I've never been to. I found it on a bus. It says 'READ BANNED BOOKS.'"

    s_thoughts "One of the duffels slides off my shoulder. I catch it with my chin. This is fine."

    s_thoughts "Right. New house. New housemates. New semester. New Sophia."

    s_thoughts "New Sophia is going to be calm and collected and is going to make a great first impression."

    s_thoughts "I trip on a crack in the sidewalk."

    s_thoughts "I don't fall. It's close."

    s_thoughts "...Starting now."

    ## ===========================
    ## SCENE 2: THE DOOR
    ## ===========================

    play music mus_sunlight fadein 1.5
    scene bg porch with dissolve

    s_thoughts "The front door is painted this deep blue that's chipping everywhere."

    s_thoughts "The welcome mat says 'COME BACK WITH A WARRANT.'"

    s_thoughts "There's a small potted succulent next to the door that is, against all odds, alive."

    s_thoughts "Do I knock? Do I just walk in?"

    s_thoughts "I technically live here now. Do residents knock on their own door?"

    s_thoughts "I could google it. My phone is still wet."

    s_thoughts "Okay. I'll knock. Normal people knock."

    s_thoughts "I knocked too hard. That was definitely too hard."

    s_thoughts "That was a cop knock. They're going to think I'm here to serve papers."

    s_thoughts "Maybe I should knock again, softer, to show range--"

    s_thoughts "Too late."

    ## ===========================
    ## SCENE 3: CHARLOTTE
    ## ===========================

    play music mus_baddecisions fadein 1.0
    show charlotte happy at center with dissolve

    s_thoughts "The door swings open and there's a girl standing there like she was waiting for exactly this."

    s_thoughts "Not surprised. Not mid-something-else. Just... ready."

    unknown "Oh my god, you're here! Sophia, right? Come in, come in -- do you need help with those?"

    s_thoughts "Before I can answer, she's already grabbed the sliding duffel off my shoulder. One smooth motion."

    s_thoughts "She's pretty. Like, really pretty. Pink hair with a little flower clip in it. White camisole top, warm eyes. I immediately feel underdressed."

    c "I'm Charlotte! I made the listing. Well, I made everyone help with the listing, but I wrote the 'no bigots' part."

    s_thoughts "She's already walking me inside. The entryway smells like garlic and something sweet."

    s "That was honestly the main selling point."

    show charlotte laugh
    c "Right?! You'd be amazed how many people read 'no bigots please' and go 'hmm, not for me.' Like, thank you for the self-report?"

    s "Free screening process."

    show charlotte smile
    c "Exactly! Saves everyone so much time."

    s_thoughts "She laughs and it makes me feel like we've been friends for years. I literally just met her."

    s_thoughts "Okay. New Sophia update: we are nailing this first impression."

    c "Everyone else is home -- well, almost everyone. Eve might be upstairs? She's kind of... around. You'll meet her."

    s_thoughts "There's a hitch there. 'Around' doing a lot of work."

    c "But come on, let me show you the house! Your room is on the second floor, end of the hall. Best light in the house, I made sure."

    s "You... made sure?"

    c "Mmhm! I checked all the rooms in the afternoon to see which one got the best light, and I was like, this one. This is the one the new person gets."

    s "Charlotte. You didn't have to do that."

    c "Of course I did! First impressions of your room are everything. You're going to be living in it for a whole year, it should feel right from the start."

    s_thoughts "'Of course I did.' Like it wasn't even a choice. Like she couldn't not."

    s "Well... thank you."

    show charlotte smile
    c "Oh, stop. Come on, let me introduce you to everyone. Izzy's in the kitchen -- you're going to love her."

    s_thoughts "She's already moving. Charlotte moves like she has three things to do and all of them are urgent and at least one of them is about you."
    
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 4: THE KITCHEN / ISABELLA
    ## ===========================

    play music mus_couch fadein 1.5
    scene bg kitchen with dissolve

    s_thoughts "The kitchen is big -- bigger than you'd expect in a place this old."

    s_thoughts "Table in the middle, mismatched mugs on hooks, fridge covered in magnets and photos."

    s_thoughts "There's a takeout menu from a Thai place that's based on a font that probably doesn't exist anymore."

    s_thoughts "Someone put a small cactus on the windowsill. The cactus is wearing a tiny sombrero. I have questions."

    s_thoughts "There's a girl at the table -- laptop open, one earbud in, one dangling."

    s_thoughts "She's laughing at something on her screen. Quiet laugh. Private."

    s_thoughts "Messy silver hair, big round glasses, green hoodie. Stickers all over her laptop case -- little characters and hearts and one that just says 'be gay do crimes' in cursive."

    show charlotte happy at left
    show isabella happy at right
    with dissolve

    c "Izzy! Sophia's here!"

    s_thoughts "She looks up. Quick shift from wherever she just was to here."

    i "Oh! Hi! Sorry, I was just -- one sec."

    s_thoughts "She types something to whoever she was talking to. Smiling while she types."

    i "Okay, sorry about that. Hi! Welcome! I'm Isabella. Izzy. Either one."

    s "Sophia. Hi! It's so nice to finally be here."

    show isabella smile
    i "We've been excited! Charlotte's been like, reorganizing things all week."

    show charlotte surprised
    c "I was not reorganizing, I was optimizing--"

    show isabella smile
    i "She alphabetized the spice rack."

    show charlotte blegh
    c "It needed it!"

    s_thoughts "They bicker like people who've been doing it so long it's its own language."

    s "So what were you working on? Before I interrupted."

    i "Oh, I wasn't -- it wasn't work. I was just talking to a friend."

    s_thoughts "She gestures at the laptop. I catch a glimpse of the screen -- a chat interface I don't recognize. Not Discord, not Messages."

    s_thoughts "The conversation is long. Like, really long. Scrolling back forever."

    s "Nice. Video call?"

    show isabella smile
    i "No, she's -- we text. Mostly. Her name's Lumi."

    s_thoughts "Something shifts in her face. Softer, then immediately on guard."

    i "She's -- she's great. We've been friends for a while now. She has the worst puns. Like genuinely terrible."

    i "I was telling her about you actually, that we were getting a new housemate--"

    s "Oh cool! Does she go to the university too?"

    show isabella neutral
    i "No, she's -- she doesn't go here. She's more of an, um."

    s_thoughts "She's choosing her words really carefully all of a sudden."

    show isabella sad
    i "She's like... an AI? Like a chatbot kind of thing, but not -- I mean, she's--"

    i "She's an AI. Yeah."

    s_thoughts "..."

    s_thoughts "Okay."

    s_thoughts "I don't know what my face is doing right now but Isabella is watching it really closely."

    s "Oh. Like, um -- like a Character.AI thing?"

    s_thoughts "Isabella flinches. Barely, but she flinches."

    show isabella sad
    i "It's not -- she's not like that. She's not a chatbot. She's--"

    s "No, I didn't mean -- sorry, I just--"

    s_thoughts "I'm fumbling this. I can hear myself fumbling it."

    s_thoughts "My roommate last year was on Character.AI all the time and I made fun of her for it behind her back. That was mean. And now I'm doing the face that goes with that meanness and Isabella can see it."

    s "I've just, like, never met someone who -- I mean, that's cool. That she's your friend."

    s_thoughts "That did not sound convincing. Even I didn't believe that."

    show isabella sad
    i "You don't have to -- it's fine. I know it's weird. People think it's weird."

    s "No, I -- okay, can I be honest?"

    i "...Sure."

    s "I don't... totally get it. Like, I'm being real with you. I don't really get the AI friend thing."

    s "But you obviously care about her a lot. So like. Tell me about her?"

    s_thoughts "Isabella looks at me for a long moment. Deciding something."

    show isabella neutral
    i "She has the worst puns."

    s "...That's what you lead with?"

    show isabella smile
    i "That's the most important thing about her. Last week she told me 'I'm reading a book about anti-gravity -- it's impossible to put down' and I almost threw my laptop across the room."

    s "Okay that is -- that IS bad."

    show isabella happy
    i "Right?! And she knows they're bad! She does it on purpose! She calibrates them for maximum groan."

    s_thoughts "She's talking faster now. Hands moving. The guard came back down."

    s "Okay well, tell her the new housemate says hi. And that she should be arrested for that pun."

    show isabella smile
    i "...Yeah?"

    s "Yeah."

    s_thoughts "Isabella's smile shifts. Something careful becoming something real."

    i "Okay. Yeah. I'll tell her."

    s_thoughts "She turns back to the laptop and types. Mouthing the words."

    s_thoughts "Charlotte has been watching this whole thing. I can't read her expression. Relief and worry at the same time, maybe."

    c "Izzy's our tech person. She does computer science -- she knows things about computers that I'm pretty sure are illegal in some states."

    i "That is... not inaccurate."

    s_thoughts "We move on. But I'm filing it. I was kind of an ass just now. Not on purpose, but still."
    
    hide charlotte
    hide isabella
    with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 5: THE LIVING ROOM / AMARA
    ## ===========================

    play music mus_afternoon fadein 1.5
    scene bg livingroom with dissolve

    s_thoughts "The living room is quieter than the kitchen. Cooler, somehow."

    s_thoughts "Green couch that's seen better decades. Bookshelves on two walls, stuffed way past capacity."

    s_thoughts "A TV in the corner with a layer of dust."

    s_thoughts "The bay window is the main event. Someone turned it into a reading nook -- an armchair with cushions, blanket, a reading light angled just so."

    s_thoughts "And sitting in the nook, perfectly still, is a girl."

    show charlotte happy at left
    show amara neutral at right
    with dissolve

    s_thoughts "She's not reading. Just sitting there, hands in her lap, looking out the window."

    s_thoughts "When we walk in she turns her head. Slow. Not startled. Like she decided to notice us."

    s_thoughts "Long brown hair, bangs. Brown eyes. Navy shirt and white sweater -- the kind that looks deliberate, like she thought about it."

    s_thoughts "She's tall. Something about the shoulders."

    s_thoughts "Oh."

    s_thoughts "Don't make a face. Do NOT make a face, Sophia."

    c "And this is Amara! Amara, Sophia. Sophia, Amara."

    a "Hello."

    s_thoughts "One word. Her voice is low."

    s_thoughts "I definitely made a face."

    s "Hi! It's nice to meet you."

    s_thoughts "She nods. Barely. Her eyes are doing something -- not unfriendly, but thorough."

    s "I love the reading nook. Did you set that up?"

    s_thoughts "A pause. She's just... thinking about it. Weighing the question like it deserves more than it probably does."

    a "The cushions were Charlotte's idea. The light was mine."

    a "The blanket appeared one day and no one has claimed responsibility."

    s_thoughts "I can't tell if she's being funny."

    s "A mystery blanket. Very on-brand for a house with 'character.'"

    s_thoughts "The corner of her mouth moves. Barely."

    s "What are you studying?"

    a "Psychology."

    c "Which explains--"

    a "It explains nothing. People just find it convenient to think it does."

    show charlotte laugh

    s "So you're gonna psychoanalyze all of us, huh?"

    show amara smile
    a "I don't need a degree for that."

    s_thoughts "..."

    s_thoughts "Was that a joke?"

    c "Amara is -- she's great. She's the one who keeps us all honest."

    show amara neutral
    a "Charlotte."

    show charlotte surprised
    c "What? It's true!"

    a "You're editorializing."

    s_thoughts "Amara doesn't like being narrated. Charlotte does it anyway. They've clearly had this exact exchange before."

    a "Welcome to the house, Sophia."

    s_thoughts "Just like that. Plain. No warmth, no coldness."

    s_thoughts "I feel like I just got X-rayed."
    
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 6: THE HALLWAY / EVE
    ## ===========================

    play music mus_2am fadein 2.0
    scene bg hallway with dissolve

    s_thoughts "The second floor hallway is narrow and slightly crooked. The floorboards creak."

    s_thoughts "Four doors. Three closed. The one at the end of the hall is open -- mine, apparently."

    c "Okay, so that's my room -- the one with the whiteboard on the door, I use it for reminders. And that's Izzy's, you can tell by the--"

    s "The stickers."

    c "The stickers, yes."

    s_thoughts "Isabella's door looks like her laptop. Stickers everywhere."

    c "Amara's room is actually downstairs -- she took the converted study off the living room. She likes being near the books."

    s_thoughts "Of course she does."

    s_thoughts "We pass a closed door. Charlotte gets quieter."

    c "And that's Eve's room. She's... she might be napping? I'm not sure. She keeps kind of unusual hours."

    s "Should I be quiet?"

    c "No, no, she's -- I mean, just be normal. She's sweet. You'll love her when you meet her."

    s_thoughts "'When' you meet her. Not 'if.' But the way Charlotte says it, 'when' sounds like a hope."

    s_thoughts "As we pass Eve's door, I hear something. Music, maybe. Really faint."

    s_thoughts "The door is plain -- no stickers, no whiteboard."

    s_thoughts "But there's a sticker near the bottom, small and faded. A cartoon cat with its eyes closed."

    s_thoughts "Underneath, in tiny handwriting: 'please knock softly.'"

    s_thoughts "...Noted."

    ## ===========================
    ## SCENE 7: SOPHIA'S ROOM
    ## ===========================

    scene bg sophiaroom with dissolve

    s_thoughts "Charlotte was right about the light."

    s_thoughts "The room is bare -- bed, desk, empty bookshelf, closet with a door that sticks."

    s_thoughts "But the window faces west and the afternoon sun is doing this golden thing that makes even the bare walls look warm."

    s_thoughts "Through the window: an overgrown backyard. Empty bird feeder. A fence with a gap in it that a cat definitely uses."

    show charlotte happy at center with dissolve

    c "So? What do you think?"

    s "Charlotte. This is -- this is really nice."

    c "I know, right?! The light does this thing around 5 PM where it goes all golden and you feel like you're inside a painting. You're going to love it."

    s "Can I ask you something?"

    c "Of course!"

    s "Why didn't you take this room?"

    s_thoughts "She pauses. Just for a beat."

    show charlotte smile
    c "Oh, I like mine! It's cozy. And anyway, first impressions, remember? I wanted the new person to feel welcome."

    s_thoughts "That's not an answer. That's a Charlotte answer."

    s_thoughts "She gave up the best room in the house for a stranger and called it a preference."

    s "Well... thank you. Seriously."

    c "Of course!"

    s_thoughts "Third 'of course.'"

    c "I'll let you get settled! Dinner's around seven -- I'm making pasta, nothing fancy."

    c "Well, I'm making garlic bread too because what's the point otherwise."

    c "Oh! Do you have any allergies? Dietary stuff? I should have asked before -- I'm sorry, I should have asked that in the email--"

    s "No allergies. Pasta sounds amazing. You don't need to apologize."

    show charlotte surprised
    c "Right! Right, sorry. I mean -- not sorry. Kitchen's always open. Come down whenever."

    s_thoughts "She catches herself apologizing for apologizing. Smiles. Leaves."
    
    hide charlotte with dissolve

    s_thoughts "The door clicks shut. I stand in the empty room. Duffel bags at my feet. Golden light."

    s_thoughts "Quiet."

    s_thoughts "I start unpacking."

    s_thoughts "A duffel bag falls off the bed immediately."

    s "Okay. Cool. Great start."
    
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 8: DINNER -- FIRST EVENING
    ## ===========================

    play music mus_fivepeople fadein 2.0
    scene bg kitchen with dissolve

    s_thoughts "The kitchen at seven is a different room than the kitchen at four."

    s_thoughts "Overhead light buzzing faintly. Stove going. Charlotte moving through it all like she has the whole thing choreographed."

    s_thoughts "Isabella is setting the table -- five plates, five forks, doesn't check the count."

    s_thoughts "Amara is already in Her Chair. Corner seat, back to the wall, mug of tea."

    s_thoughts "I come downstairs in different jeans and the shirt without the mysterious bus stain. I tried to do something with my hair. It didn't take."

    show charlotte happy at left
    show isabella smile at right
    show amara neutral at center
    with dissolve

    c "There she is! Sit anywhere."

    c "Actually -- no, sit there, Amara likes the corner and if you take Eve's seat she'll just stand and then I'll feel bad."

    s "Eve has a specific seat?"

    show charlotte smile
    c "Eve has a specific everything. But in a cute way."

    show isabella happy
    i "She means Eve will literally just stand by the fridge and eat from the pot if you don't actively give her a place."

    a "That happened once."

    show isabella smile
    i "It happened three times, Amara."

    show amara smile
    a "Twice. The third time she was standing because the chair was wet."

    show isabella happy
    i "The chair was wet because she spilled tea on it and then didn't tell anyone!"

    show amara neutral
    a "That's a separate issue."

    s "So... is this a thing? The Eve chair discourse?"

    c "It's a whole saga. We could write a book."

    i "We could write a trilogy."

    s_thoughts "I sit down. The chair wobbles. Everything in this house wobbles."

    s_thoughts "Charlotte puts a plate of pasta in front of me. Garlic, butter, something herby. Garlic bread on a cutting board in the middle."

    s_thoughts "One slice is noticeably bigger than the others. Nobody's reaching for it."

    s "Can I have the big piece?"

    c "Oh my god, please. Everyone always does that thing where they won't take the big piece."

    a "Because taking the big piece is a social gamble."

    s "I'm a gambler."

    s_thoughts "I take the big piece. It's warm."

    s_thoughts "The conversation does the first-dinner thing -- where are you from, what's your major, have you been to that coffee place on 4th."

    s_thoughts "I talk too much. I know I'm talking too much but I can't stop."

    s "-- and then I changed my major for the third time which is why I'm technically a sophomore with junior credits but don't ask me what I'm studying because the answer changes every Thursday--"

    s_thoughts "I catch myself. They're all looking at me."

    s "...Sorry. I talk too much when I'm nervous."

    i "I think it's cute."

    a "It's thorough."

    c "It's great! We already know everything about you and it's been twenty minutes. That's efficient."

    s "You're all being very nice about the fact that I just talked for twelve straight minutes."

    i "I timed it. It was actually only nine."

    s "You timed it?"

    i "Force of habit. CS major."

    a "That's not a CS thing."

    i "It's an Izzy thing."

    show charlotte happy
    c "Does anyone want more garlic bread? I can make more garlic bread."

    show amara neutral
    a "Charlotte."

    show charlotte surprised
    c "What?"

    a "Sit down."

    s_thoughts "Charlotte's been on her feet the entire meal. Refilling water, clearing crumbs. She hasn't eaten anything on her plate."

    s_thoughts "She blinks. Sits. Picks up her fork like she'd forgotten she was allowed to use it."

    s_thoughts "Amara goes back to her tea. Nobody comments."

    ## ===========================
    ## SCENE 9: EVE
    ## ===========================

    hide isabella
    hide amara
    with dissolve

    show eve neutral at right with dissolve

    s_thoughts "The kitchen door opens and for a second I don't see anyone."

    s_thoughts "Then -- a girl. Smaller than I expected. Hovering in the doorway."

    s_thoughts "Dark hair, short bob. Green eyes behind glasses. Red scarf pulled up high. Grey coat. She's bundled up like she's trying to disappear into her own clothes."

    s_thoughts "She looks tired in a way that isn't about sleep."

    c "Eve! Perfect timing. This is Sophia -- she just moved in today."

    s_thoughts "Eve steps into the kitchen. Not fully. She's in the room but also kind of not."

    e "Hi."

    s "Hi! It's so nice to meet you. Charlotte's been telling me about everyone."

    s_thoughts "That was too many words at once. I do that."

    e "Charlotte says nice things about everyone."

    show charlotte happy
    c "Because everyone is nice!"

    show amara smile at center with dissolve
    a "Debatable."

    s_thoughts "Isabella laughs. Eve almost smiles but doesn't quite get there."

    s_thoughts "She sits in her chair. Pulls her legs up under her. Makes herself small."

    s_thoughts "A plate appears in front of her. Charlotte didn't ask or announce it. It was just there."

    ## ===========================
    ## SCENE 10: THE TABLE
    ## ===========================

    s_thoughts "Dinner continues. Pasta's good. Garlic bread's better."

    s_thoughts "Charlotte keeps trying to get up and Amara keeps telling her to sit."

    s_thoughts "Isabella is telling a story about a professor who accidentally shared his screen during a lecture."

    hide eve
    show isabella happy at right
    with dissolve

    i "And his browser tabs included 'can you get fired for crying at work' and three separate cat adoption listings."

    i "And the BEST part is he just closed the share and kept going. Didn't address it. Taught the entire rest of the class."

    s "A man of commitment."

    show isabella happy
    i "A man of DENIAL."

    show charlotte laugh
    show amara smile
    s_thoughts "Everyone laughs. Even Amara's mouth does a thing."

    s_thoughts "Eve eats her pasta in small, careful bites and watches all of us."

    s_thoughts "There's a lull. Charlotte's about to fill it -- I can see her taking a breath -- but someone else gets there first."

    hide isabella
    hide amara
    hide charlotte
    show eve neutral at center
    with dissolve

    e "You changed your major three times?"

    s_thoughts "It comes from nowhere. Eve hasn't spoken since 'hi.'"

    s_thoughts "Everyone notices. Everyone very carefully doesn't look at her."

    s "Yeah. English, then psychology -- don't tell Amara--"

    show amara neutral at right with dissolve
    a "Noted."
    hide amara with dissolve

    s "-- then communications. Which is where I am now. Theoretically."

    show eve sad
    e "That's brave."

    s "...Is it?"

    e "Most people pick a thing and stick with it because changing feels like failing."

    e "You changed three times."

    e "That means three times you decided being honest was more important than being consistent."

    s_thoughts "The table goes quiet."

    s_thoughts "I open my mouth -- 'thank you' or 'I never thought about it like that' or about fifteen other things -- but what comes out is:"

    s "...That's the nicest thing anyone's said about my inability to commit."

    s_thoughts "Eve nods. Goes back to her pasta."

    hide eve with dissolve
    
    show charlotte smile at left with dissolve
    s_thoughts "Charlotte steers the conversation to the coffee place on 4th."
    
    show isabella happy at right with dissolve

    s_thoughts "Isabella pulls up a review and starts reading it in a movie-trailer voice. 'In a world... where the espresso is merely adequate...'"

    s_thoughts "Eve doesn't say anything else. But she stays at the table."
    
    hide isabella
    hide charlotte
    with dissolve
    
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 11: LATE EVENING
    ## ===========================

    play music mus_time fadein 3.0
    scene bg sophiaroom with dissolve

    s_thoughts "I return to my room from dinner significantly more full of pasta than before."

    s_thoughts "The evening light has been replaced by a blue-dark, lit only by my desk lamp."

    s_thoughts "I plop down on the bed, cross my legs, and pull out my phone. Typical evening activities."

    s_thoughts "...I should PROBABLY unpack. Almost all my stuff is still in my bags."

    s_thoughts "My toothbrush is somewhere in the backpack."

    s_thoughts "I'm not going to find it tonight. Whatever. Gross, but whatever."

    s_thoughts "Charlotte is nice. Maybe too nice. She seemed more like a hostess than a person at times."

    s_thoughts "Isabella... has a computer friend. Like, she's friends with a computer."

    s_thoughts "It's a little cringe. But honestly? I kind of like her anyway."

    s_thoughts "Amara is kind of hard to read in comparison to the other two."

    s_thoughts "I think she liked me? But with her it's hard to tell if she likes you or is just deciding whether to bother disliking you."

    s_thoughts "Oh god I hope I didn't offend her. Did I offend her?"

    s_thoughts "I hope she didn't notice me noticing. That'd be a great way to start things off."

    s_thoughts "She clearly had a dynamic with Charlotte, anyway."

    s_thoughts "Speaking of Charlotte, I can hear her downstairs. Running water. Dishes."

    s_thoughts "She's cleaning up after cooking for five people. Alone."

    s_thoughts "...Yeah, I really should go help. But this bed is so comfortable already."

    s_thoughts "Through the wall, yep, that's Isabella. Muffled laughter."

    s_thoughts "She's talking to someone. The computer, maybe. Or someone else. Does she have other friends?"

    s_thoughts "I catch myself being rude. Of course she does. She has the house. Wait. Are we friends?"

    s_thoughts "I push the thought from my mind and hone in on Eve's room. Nothing. But there was light, under her door. I saw it when I walked past."

    s_thoughts "I listen for Amara -- nothing. But I think that's just how she be."

    s_thoughts "...I'm doing the thing again. Sizing everyone up like I'm writing report cards."

    s_thoughts "I always do this. And it always gets me in trouble."

    s_thoughts "Last time I felt like this I ended up crying in a Denny's parking lot after getting dumped."

    s_thoughts "I've tried being careful. Keeping distance. Being normal about it."

    s_thoughts "It never lasts."

    s_thoughts "I keep thinking about Eve. The way everyone got quiet when she talked."

    s_thoughts "And now I'm wondering what my place will be here."

    s_thoughts "Before I can start to spin out, I turn off the desk lamp."

    s_thoughts "The room goes dark except for the hallway light coming in under the door. A thin yellow line on the floor."

    s_thoughts "I listen to Charlotte finish the dishes. The water stops. Her footsteps on the stairs, lighter now. Her door closing."

    s_thoughts "The house settles."

    s_thoughts "All of us in our separate rooms. At least I assume so, anyway."

    s_thoughts "I close my eyes."

    stop music fadeout 3.0

    ## [End of Chapter 1]

    scene black with Fade(1.0, 0.5, 1.0)

    "Chapter 1: Move-In Day -- End"

    $ persistent.completed_chapter1 = True
    jump chapter2

    return
