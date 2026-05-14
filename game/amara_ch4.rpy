## amara_ch4.rpy -- Glass Houses
## Chapter 4: "The Gravity" -- Amara Route
## Act 1: "Two Frequencies" (Scenes 1-15)

## === NEW VARIABLES NEEDED (add to variables.rpy) ===
## default sophia_fire = 0  ## Tracks fire vs stillness across 3 choices (0-3). +1 per fire choice.

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

## ===========================
## CHAPTER 4 START
## ===========================

label amara_ch4:

    ## ===========================
    ## SCENE 1: THE ARMCHAIR
    ## Sophia drawn to Amara's gravity. Three words and silence.
    ## Translation instinct: FIRING. Filing everything. Getting nothing.
    ## ===========================

    scene bg livingroom with Fade(1.0, 0.5, 1.0)

    stop music fadeout 0.5

    s_thoughts "Tuesday afternoon."

    s_thoughts "I come downstairs because I've been staring at my ceiling for forty minutes and the ceiling was winning."

    s_thoughts "The living room is empty except for--"

    show amara neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "She's in the armchair. The big one, the one Charlotte picked because it was on sale and then nobody sat in because the cushion does something weird to your back. Amara sits in it like it was built for her."

    s_thoughts "She's reading."

    s_thoughts "She doesn't look up."

    pause 1.0

    s_thoughts "She doesn't say hello. She doesn't do the thing where you acknowledge someone walked into the room. She turns a page."

    s_thoughts "I should go to the kitchen. Get a drink. Go back upstairs. Do literally anything other than stand in the doorway watching a girl read."

    s_thoughts "I sit on the couch."

    s_thoughts "I have a book. Somewhere. In my bag. I pull it out. Nova's reading on-- translation theory. The chapter about fidelity and equivalence. I've read the first paragraph six times and I still don't know what it says."

    s_thoughts "I read the first paragraph a seventh time."

    s_thoughts "Amara turns a page."

    pause 1.5

    s_thoughts "The room is quiet in a way that has texture. Not silence. There's the clock on the wall. There's someone's music upstairs -- Isabella's, probably. There's the fridge doing its thing two rooms away."

    s_thoughts "Amara is the quiet part. She doesn't generate sound. She sits and she reads and the quiet gathers around her like she's made of it."

    s_thoughts "I'm staring. I'm definitely staring."

    s_thoughts "I look down at my book. Fidelity. Equivalence. The translator's obligation to the source text versus the target audience."

    s_thoughts "The filing instinct is running. It's been running since I sat down. I'm cataloguing everything -- the angle of her head, the way she holds the book with one hand, the fact that she's reading something with a green cover and no visible title."

    s_thoughts "I'm getting nothing."

    s_thoughts "She's a girl reading a book. That's it. There's nothing to decode. No hidden layer. No performance. She's just here."

    s_thoughts "That's the problem. My brain keeps looking for the trick and there isn't one."

    s_thoughts "The clock ticks. Isabella's music changes tracks upstairs. Something with a bass line that I can feel through the floor more than hear."

    pause 1.0

    s_thoughts "Amara doesn't look up."

    s_thoughts "Five minutes. Maybe ten. I have no idea. Time works differently in this room when Amara is in it."

    a "You're not reading."

    s_thoughts "I blink."

    s "What?"

    a "You haven't turned a page."

    s_thoughts "Three words. Then five. Delivered without looking up from her own book. Like she's commenting on the weather."

    s "I'm... thinking about what I read."

    s_thoughts "She turns a page. Hers. Unhurried."

    a "Okay."

    pause 1.5

    s_thoughts "Okay."

    s_thoughts "That's it. That's the whole conversation. 'You're not reading.' 'I'm thinking.' 'Okay.'"

    s_thoughts "And then silence again. The clock. The fridge. Isabella's bass line."

    s_thoughts "Except the silence is different now. She spoke and the silence changed shape. Like the room rearranged itself around her three words and settled into a new configuration."

    s_thoughts "I don't know how to explain what just happened."

    s_thoughts "Nothing happened. A girl noticed I wasn't reading. She said so. I said I was thinking. She said okay."

    s_thoughts "My heart is doing a thing. A small, dumb thing. I'm annoyed at it."

    s_thoughts "I read the first paragraph an eighth time."

    s_thoughts "My phone buzzes in my pocket."

    s_thoughts "I ignore it."

    s_thoughts "Amara turns another page."

    pause 1.0

    s_thoughts "I read the paragraph. Ninth time. This time I get to the second sentence."

    s_thoughts "Progress."

    hide amara with dissolve

    s_thoughts "I don't know how long we sit there. Long enough that the light through the window moves. Long enough that Isabella's music stops and starts again."

    s_thoughts "Amara closes her book. She stands. She walks past me toward the stairs."

    s_thoughts "She doesn't say goodbye."

    s_thoughts "The armchair is empty. The room is the same room. The quiet is regular quiet now -- the kind anyone could make by not talking."

    s_thoughts "Hers was different."

    s_thoughts "My phone buzzes again. I check it."

    s_thoughts "Two texts from Lila. The first: a photo of a campus squirrel with the caption 'this squirrel has more direction in life than me.'"

    s_thoughts "The second: 'I have a PLAN. Call me.'"

    s_thoughts "I look at the empty armchair."

    s_thoughts "I call Lila."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 2: LILA EXPLODES IN
    ## Campus. Full volume. "I have a PLAN."
    ## Counter-frequency. FAST.
    ## Translation instinct: OFF. No one to decode. Just vibes.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 1.5

    show lila happy at center with dissolve

    l "OKAY so hear me out."

    s "I'm hearing you out."

    l "There's a karaoke place on Fifth. Half-price drinks on Tuesdays. TUESDAY IS TODAY. I've already got you a fake."
    
    s_thoughts "She came prepared."

    s "You called me for karaoke."

    l "I called you because you haven't left that house in like a week and I'm staging an intervention."

    s "I leave the house. I go to class."

    l "Class doesn't count. Class is obligation. I'm talking about FUN. Remember fun? You used to be fun."

    s "I'm still fun."

    show lila annoyed at center

    l "You're reading translation theory from our comms class. For PLEASURE."

    s "It's not for pleasure. It's for--"

    l "You could have said 'no, Lila, you're wrong, I'm extremely fun, let me prove it.' Instead you tried to defend the translation theory. I rest my case."

    s_thoughts "She's got me there."

    show lila happy at center

    l "Look. Here's the plan. Tonight. Karaoke. You and me. I'll buy the first round. We'll sing something terrible. You'll forget about whatever complicated situation is happening in that house for like three hours."

    s "What makes you think there's a complicated situation?"

    l "Sophia. Babe. You live with four girls and you've changed your major three times. Your LIFE is a complicated situation."

    s_thoughts "I laugh. I actually laugh. The kind that catches you off guard."

    show lila laugh at center

    l "There it is! She remembers!"

    s "Fine. Karaoke. But I'm not singing."

    l "You're ABSOLUTELY singing. I already have the song picked out."

    s "Lila--"

    l "It's 'Don't Stop Believin'.' It's always 'Don't Stop Believin'.' It's the LAW."

    s "I hate you."

    l "You love me. Tonight. Seven. Wear something that isn't your sad jacket."

    s "My jacket isn't sad."

    l "It has a hole in the pocket. I watched you lose your keys through it TWICE."

    s "That's character."

    l "That's a fire hazard. Seven o'clock. Don't be late."

    hide lila with dissolve

    s_thoughts "She's already walking away, phone out, probably adding me to some group chat I'll regret."

    s_thoughts "When's the last time I did something that wasn't analyzing someone or being analyzed?"

    s_thoughts "I genuinely don't remember."

    s_thoughts "My phone buzzes. Lila: a karaoke microphone emoji, a fire emoji, and then 'your armchair can wait.'"

    s_thoughts "I didn't tell her about the armchair."

    s_thoughts "I didn't tell her about anything."

    s_thoughts "She just knows. That's Lila's thing."

    s_thoughts "No system. No file. Just a friend who noticed I haven't been around."

    s_thoughts "I put my phone away. The campus is doing its thing -- people walking, leaves falling, someone arguing about Marx outside the humanities building."

    s_thoughts "I don't check my phone for texts from the house."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 3: NOVA'S CLASS -- TRANSLATION AND INTERPRETATION
    ## The semester's framework introduced.
    ## "Can you translate something that isn't speaking?"
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)

    play music mus_nova fadein 2.0

    s_thoughts "Wednesday. Nova's elective."

    s_thoughts "I sit in the third row because the front is try-hard and the back is checked-out and the third row says 'I care but not enough to make eye contact every time you look up.'"

    show professor neutral at center with dissolve

    nova "Today we're talking about translation."

    nova "Not the kind where you convert Spanish into English. The kind where you take something -- a text, a behavior, an experience -- and you carry it from one framework into another."

    s_thoughts "She does the settling thing. The way she looks at the room like she's reading it before she speaks."

    nova "When we translate, we carry meaning across a gap. A gap between languages, between cultures, between people."

    nova "But the carrying changes it. Always. The translator is never invisible."

    s_thoughts "I write that down."

    nova "Think about it this way. You read a poem in French. You translate it into English. The words are equivalent. The rhythm is different. The mouth feels different saying it. Is it the same poem?"

    s_thoughts "Silence in the room. The Nova kind -- where she leaves a question and waits and you can feel thirty people thinking at the same time."

    nova "Most of you will say no. The translation loses something. And you're right. But here's the harder question--"

    show professor happy at center

    nova "What does the translation ADD?"

    s_thoughts "She lets that sit."

    nova "The translator brings herself to every translation. Her assumptions. Her context. Her hearing."

    nova "This isn't a flaw. This is the condition of translation. You cannot carry something across a gap without bringing yourself along."

    s_thoughts "I'm thinking about Amara. Trying to translate her silence."

    s_thoughts "'You're not reading.' 'Okay.'"

    s_thoughts "What did she mean? Was it an observation? An invitation? A dismissal?"

    s_thoughts "I translated it six different ways that evening and none of them felt right."

    nova "Here's your first assignment. Find something untranslatable. A word, a gesture, an experience. Something that resists being carried into your language."

    nova "Don't try to force the translation. Just sit with the gap."

    s_thoughts "I underline it: 'sit with the gap.'"

    nova "One more thing."

    show professor neutral at center

    nova "What does it mean to translate silence? Can you translate something that isn't speaking?"

    s_thoughts "I underline that too. Twice."

    hide professor with dissolve
    
    scene bg campus with dissolve

    s_thoughts "After class I walk across the quad. The leaves are doing the orange thing. Someone's frisbee almost hits me."

    s_thoughts "I'm thinking about silence and translation and a girl in an armchair who said 'okay' like it was a complete sentence."

    s_thoughts "Which it was. I just don't speak the language."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 4: THE LIBRARY
    ## Studying in parallel. Sophia watches Amara's hands.
    ## The crush starts in Sophia's body.
    ## Translation instinct: Firing but physical -- hands, not files.
    ## ===========================

    scene bg library with Fade(0.8, 0.3, 0.8)

    s_thoughts "Thursday. I'm at the library."

    s_thoughts "I'm here because I have Nova's reading to finish and my room has too many distractions and by distractions I mean a ceiling I can stare at and a wall I can hear through."

    s_thoughts "I find a table. Second floor. The quiet section, where people actually study instead of doing the thing where they sit with an open textbook and scroll TikTok for two hours."

    s_thoughts "I open the reading. Fidelity and equivalence. The translator's dual obligation."

    s_thoughts "I read a sentence."

    s_thoughts "Movement. Periphery."

    show amara neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "She's at the next table. Not my table. The next one. Close enough that I can see what she's reading if I leaned slightly. Which I am not going to do."

    s_thoughts "She's already here. Books out. Notes open. She didn't just arrive -- she's been here. The pen is uncapped. There's writing on the page."

    s_thoughts "She didn't look up when I sat down."

    s_thoughts "Either she didn't notice me or she noticed and decided it didn't require acknowledgment. Both are very Amara."

    pause 1.0

    s_thoughts "I read. She reads. The library does its thing -- that particular library frequency of pages and keyboards and someone two tables over breathing too loudly through their nose."

    s_thoughts "I finish a paragraph. A real paragraph. With comprehension."

    s_thoughts "I look up."

    s_thoughts "Amara is taking notes."

    s_thoughts "Her handwriting is small. Precise. She writes in a way that suggests she composed the sentence in her head first and is now transcribing it. No crossing out. No hesitation. The pen moves steadily and then stops and she reads again."

    s_thoughts "The pen is a felt-tip. Black ink. She holds it low, near the nib, the way you hold something you're comfortable with. Not the death grip of someone who hates writing -- the loose hold of someone who does it often."

    s_thoughts "She pauses."

    s_thoughts "Her hand goes still. The pen hovers above the page. She's thinking about something. Her eyes are on the book but they're not reading -- they're somewhere behind the text, in the space between what she read and what she'll write."

    s_thoughts "I'm watching her hands."

    s_thoughts "I'm specifically, deliberately, intently watching this girl's hands hold a pen."

    s_thoughts "Something in my stomach does something architectural. Like a load-bearing wall just discovered it has opinions."

    s_thoughts "She writes another sentence. The pen moves left to right and her wrist follows and the whole motion is fluid and controlled and I need to stop looking at this."

    s_thoughts "I look at my book."

    s_thoughts "Fidelity. Equivalence. The translator's--"

    s_thoughts "Her hand moves again. Periphery."

    s_thoughts "God."

    s_thoughts "I read the same sentence I've already read. Something about the impossibility of perfect translation and how every rendering involves loss. Very relatable. Deeply unhelpful."

    s_thoughts "Amara closes her book. She's done. She caps the pen. She puts the pen in a case -- a pen case, leather, small -- and puts the case in her bag."

    s_thoughts "She has a pen case."

    s_thoughts "Something about the pen case makes my brain short-circuit."

    s_thoughts "She stands. She looks at me."

    s_thoughts "Not at me-at-my-table. At me. Direct."

    a "The chapter on dynamic equivalence is better."

    s "What?"

    a "Than the one you're reading. Chapter four. Nida."

    s_thoughts "She read the title of my book. From that distance. She's been-- she noticed what I'm reading."

    s "Oh. Thanks."

    a "Mm."

    s_thoughts "She leaves."

    hide amara with dissolve

    pause 1.0

    s_thoughts "I turn to chapter four. Dynamic equivalence. Nida. The idea that a good translation produces the same EFFECT in the reader, even if the words are different."

    s_thoughts "She recommended me a chapter."

    s_thoughts "She noticed my book and recommended me a chapter and walked away like it was nothing."

    s_thoughts "My hands are doing a weird thing. A slight tremor. Not nerves. Something else. Something that started when I was watching her hands and hasn't stopped."

    s_thoughts "I read chapter four. It's better."

    s_thoughts "She was right."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 5: THE WASTED NIGHT
    ## Karaoke with Lila. Drunk. Fun. Charlotte makes toast.
    ## Amara's door closed.
    ## Translation instinct: OFF. Drunk Sophia doesn't file.
    ## ===========================

    scene bg karaoke with Fade(0.8, 0.3, 0.8)

    play music mus_playlist fadein 2.0

    s_thoughts "TUESDAY NIGHT."

    s_thoughts "I say that in capital letters because everything about tonight is in capital letters."

    show lila happy at center with dissolve

    l "YOUR TURN."

    s "Absolutely not."

    l "You PROMISED."

    s "I promised nothing. I said I'd come. Coming and singing are different verbs."

    show lila drunk at center

    l "Sophia Bell. I have bought you THREE drinks. You owe me a duet."

    s_thoughts "She's already a little gone. Her cheeks are red and her glasses are crooked and she's holding the karaoke mic like a weapon."

    s "What's the song?"

    l "DANCING QUEEN."

    s "No."

    l "DANCING QUEEN, SOPHIA."

    s "Lila--"

    l "YOUNG AND SWEET ONLY SEVENTEEN--"

    s_thoughts "She's already singing. She's singing at me. She is pointing the microphone at my face and singing ABBA with the conviction of a woman who has made a decision."

    s "Oh my god."

    l "SEE THAT GIRL--"

    s_thoughts "She grabs my hand. Pulls me up."

    s_thoughts "I'm standing. I'm holding a microphone. The lyrics are on a screen. There are strangers in this bar and Lila is singing ABBA and I--"

    s_thoughts "I sing."

    s_thoughts "I sing badly. Spectacularly badly. Off-key and too loud and I forget the verse but nail the chorus because everyone nails the chorus."

    l "HAVING THE TIME OF YOUR LIFE--"

    s_thoughts "Lila is doing choreography. She invented choreography. She's doing a spin move that almost takes out a waitress."

    s_thoughts "I'm laughing so hard I can't breathe."

    s_thoughts "This is -- I forgot what this was. The stupid part. The part where nothing matters except the song and the drink and the friend next to you who sings like a beautiful disaster."

    s_thoughts "We do three more songs. Bon Jovi. Spice Girls. Something by Carly Rae Jepsen that Lila knows every word to and I fake my way through."

    s_thoughts "My voice is wrecked. My cheeks hurt from smiling."

    l "OKAY okay okay one more."

    s "No more. My vocal cords are filing a restraining order."

    l "Don't Stop Believin'. We HAVE to. It's the LAW."

    s "You said that already."

    l "Because it's STILL the law!"

    s_thoughts "We sing Don't Stop Believin'. We are terrible. We are transcendent. A group at the next table starts singing the chorus with us."

    s_thoughts "Lila high-fives a stranger."

    s_thoughts "I almost fall off the little stage."

    s_thoughts "It's perfect."

    ## -- Walking home --

    scene bg nightwalk with Fade(0.8, 0.3, 0.8)

    s_thoughts "1 AM. Walking home. The air is cold and my jacket isn't warm enough and I don't care."

    show lila drunk at center with dissolve

    l "You were SO GOOD."

    s "I was objectively terrible."

    l "Objectively terrible is subjectively iconic. That's math."

    s "That's not math."

    l "It's Lila math. It counts."

    s_thoughts "We're walking and she keeps bumping into me. Not on purpose. She's just slightly off-axis."

    l "Hey."

    s "Hey."

    l "You're fun. You know that? Like -- you're FUN. The house makes you all serious and complicated. Like everyone in there is a puzzle you have to solve."

    s "That's not--"

    l "It IS. You do the thing. The watching thing. The 'I'm building a file on you' thing. Katie, y'know?"

    s_thoughts "That lands differently when you're drunk. More direct. More true."

    s "Katie complained about a lot of things."

    l "Yeah, but she was right about that one. You watch people like you're going to be tested on them later."

    s_thoughts "I don't say anything."

    l "But tonight you didn't! Tonight you were just-- you. No files. No watching. Just a girl singing ABBA badly."

    s "Very badly."

    l "The BEST badly. I'm proud of you."

    s_thoughts "She means it. She's drunk and she means it and something about that makes my chest go tight."

    s "Thanks, Lila."

    l "Anytime, babe. Any. Time."

    ## -- The kitchen --

    scene bg kitchen night with dissolve

    s_thoughts "The house. 1:15 AM. We are too loud."

    show lila drunk at left with dissolve

    s_thoughts "We are so loud."

    l "SHHHH."

    s "YOU shh."

    l "I'm being quiet! This is my quiet voice!"

    s_thoughts "It's not her quiet voice."

    show charlotte pj happy at right with dissolve

    c "It's 1 AM!"

    s_thoughts "Charlotte. Pajamas. Hair in a messy bun. She's trying to look disapproving but she's smiling."

    l "Charlotte! Hi! We went to karaoke!"

    c "I can tell."

    s "Sorry. We'll be quiet."

    c "Oh, don't be sorry! I was just up anyway. Do you want toast?"

    l "YES."

    c "I'll make toast."

    s_thoughts "She's already at the toaster. Of course she is. Charlotte makes toast the way other people breathe. It's not a decision. It's a reflex."

    show charlotte pj smile at right

    s_thoughts "Lila sits on the floor. Just -- sits right down on the kitchen floor. Legs crossed. Like the floor is where she was always headed."

    l "Your kitchen is so nice."

    c "It's everyone's kitchen!"

    l "It smells like-- what is that?"

    c "Rosemary. I made a chicken thing earlier. There's leftovers in the fridge!"

    l "Charlotte, you're an angel. An actual angel."

    s_thoughts "Charlotte beams. Charlotte BEAMS. Someone appreciating the kitchen is Charlotte's love language and Lila just spoke it fluently."

    s_thoughts "I sit on the floor next to Lila. The tile is cold. The toast is popping. Charlotte hums something while she butters it."

    s_thoughts "I look at the hallway."

    s_thoughts "Amara's door. Closed."

    s_thoughts "She heard us come in. She had to have heard us. We sounded like a parade designed by someone who hates parades."

    s_thoughts "She didn't come out."

    s_thoughts "I look at the toast. I look at Lila on the floor. I look at Charlotte buttering."

    s_thoughts "I'm drunk and warm and my voice is gone and I'm sitting on the kitchen floor."

    s_thoughts "And I'm thinking about a closed door."

    l "Soph."

    s "Hm?"

    l "You're doing the thing."

    s "What thing?"

    l "The watching thing. You're looking at the hallway like it wronged you personally."

    show charlotte pj happy at right

    c "More toast?"

    l "ALWAYS more toast."

    s_thoughts "I eat my toast. It's good. Charlotte's toast is always good."

    s_thoughts "I stop looking at the hallway."
    
    hide lila with dissolve

    s_thoughts "Lila falls asleep on the kitchen floor at 2 AM. Charlotte puts a blanket over her."
    
    hide charlotte with dissolve
    
    scene bg entry night with dissolve

    s_thoughts "I head upstairs. Amara's door is closed. No light underneath."
    
    scene bg sophiaroom with dissolve

    s_thoughts "I brush my teeth. I lie in bed. The ceiling doesn't spin, which means I'm not that drunk, which means I'm going to remember all of this tomorrow."

    s_thoughts "The armchair. The library. The pen. The pen case. 'Chapter four. Nida.'"

    s_thoughts "Don't Stop Believin'."

    s_thoughts "A closed door."

    hide lila with dissolve
    hide charlotte with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 6: THE MORNING AFTER
    ## Hungover. Amara: "Fun night?" Two words that could mean anything.
    ## Amara's book has changed. Sophia notices.
    ## Translation instinct: Firing weakly. The hangover dulls it.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.5, 0.8)

    play music mus_sunlight fadein 2.0

    s_thoughts "Wednesday. 10 AM."

    s_thoughts "My head is doing a thing where it exists and I wish it wouldn't."

    s_thoughts "I come downstairs because the alternative is lying in bed being hungover ALONE, and if I'm going to suffer I want coffee and witnesses."

    s_thoughts "Charlotte's already been and gone. Evidence: clean counter, coffee pot full, a note on the fridge that says 'Lila -- you snore!! <3 -- C.'"

    s_thoughts "Lila's gone too. Probably stole one of Charlotte's muffins on the way out."

    scene bg livingroom with dissolve

    s_thoughts "I take my coffee to the living room."

    show amara neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "Armchair. Reading. Different book."

    s_thoughts "The green-covered one from yesterday is gone. This one is smaller. Paperback. Something with a stark cover -- a single image, black and white. I can't read the title from here."

    s_thoughts "I sit on the couch. I drink my coffee. My head throbs."

    pause 1.5

    s_thoughts "Amara turns a page."

    s_thoughts "The room does the thing it did before. The quiet gathers. The clock ticks."

    s_thoughts "I'm too hungover to file anything. My brain is running at half-speed. The cataloguing instinct is there, sluggish, like a computer booting up."

    s_thoughts "New book. She finished the other one in two days. Or she put it down. The cover is -- I lean forward slightly."

    s_thoughts "{i}Lessons in the Art of Listening.{/i}"

    s_thoughts "Huh."

    pause 2.0

    a "Fun night?"

    s_thoughts "I look at her."

    s_thoughts "She doesn't look up from the book. She said it to the page."

    s_thoughts "Two words. Completely neutral. I can't tell if it's a question, a judgment, an observation, or a very dry joke."

    s_thoughts "Is she making fun of me? Is she curious? Is she saying 'I heard you come in at 1 AM singing Bon Jovi and I have thoughts'?"

    s "Yeah. Karaoke."

    s_thoughts "She turns a page."

    a "Mm."

    s_thoughts "'Mm.' The same as 'okay' from the armchair. A sound that is both an acknowledgment and a complete sentence and an invitation for me to say more or say nothing and I don't know which."

    s "Lila dragged me out."

    s_thoughts "Nothing."

    s "It was fun. I can't really sing."

    s_thoughts "Page turn."

    s "I should probably stop talking to a person who's reading."

    a "I can do both."

    s_thoughts "Four words. Said quietly. Still not looking up."

    s_thoughts "'I can do both.'"

    s_thoughts "I sit with my coffee and hangover and I don't say anything else."

    s_thoughts "Neither does Amara."

    s_thoughts "It's fine. It's actually fine. For the first time the silence doesn't feel like something I need to decode. It just feels like two people in a room."

    s_thoughts "My phone buzzes. Lila: 'im dying. charlotte's muffin saved my life. karaoke rematch friday?????'"

    s_thoughts "I type: 'Friday works.'"

    s_thoughts "Amara turns a page."

    s_thoughts "I finish my coffee."

    hide amara with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 7: AMARA'S ROOM
    ## First time seeing it. Clarinet case. Art. Rich inner life.
    ## "Quiet people aren't empty."
    ## Translation instinct: Goes HAYWIRE, then Sophia catches herself.
    ## ===========================

    scene bg entry with Fade(0.8, 0.3, 0.8)

    s_thoughts "Thursday evening."

    s_thoughts "I'm at the bottom of the stairs because I was heading to the kitchen and got distracted by the fact that Amara's door is open."

    s_thoughts "Amara's door is never open."

    s_thoughts "Not never. Almost never. She keeps it closed the way Eve keeps hers closed -- not locked, just private. A boundary that says 'this space is mine and I didn't invite you into it.'"

    s_thoughts "It's open."

    s_thoughts "Not wide. A foot, maybe. Enough to see a slice of the room from the hallway. A desk. Part of a wall."

    s_thoughts "I should keep walking."

    s_thoughts "I don't keep walking."

    s_thoughts "I stop. I look."

    s_thoughts "Through the gap: the edge of a desk, a lamp with a warm light, and on the wall above the desk--"

    s_thoughts "Is that a painting?"

    a "You can come in."

    s_thoughts "I flinch. She's behind me. She walked up while I was doing my thing where I stand in hallways staring into rooms like a creep."

    show amara neutral at center with dissolve

    s_thoughts "She's holding a mug. Tea. She walks past me into her room and leaves the door open behind her."

    s_thoughts "That's the invitation."

    scene bg amarabedroom with dissolve

    s_thoughts "Oh."

    s_thoughts "It's not what I expected."

    s_thoughts "I don't know what I expected. Something minimal. Clean surfaces. A few books. The room equivalent of Amara's three-word sentences."

    s_thoughts "This is--"

    s_thoughts "The walls. There are prints on the walls. Three of them, framed -- real frames, not poster tape." 
    
    s_thoughts "An abstract piece in deep blues, something that might be a landscape but blurred like a memory of a landscape, and a photograph of a woman I don't recognize playing a wind instrument. The woman is mid-note, eyes closed."

    s_thoughts "The bookshelf. Not organized by size or color or alphabet -- organized by something I can't identify. Some system that's internal, that makes sense to Amara and no one else."

    s_thoughts "The desk. A laptop closed. The felt-tip pen in its case. A small ceramic dish with earrings in it. A notebook -- not the one from the library, a different one, open, with handwriting I can't read from here."

    s_thoughts "And on the desk, leaning against the wall--"

    s_thoughts "A clarinet case."

    s_thoughts "Black. Battered. Stickers on it -- faded, peeling. The kind of stickers you put on things when you're thirteen and then can't bring yourself to remove."

    s_thoughts "Amara plays clarinet."

    s_thoughts "The filing instinct goes nuclear. So much data. The books tell me what she reads, the art tells me what she sees, the clarinet tells me she makes music, the earring dish tells me she accessorizes in private, the notebook tells me she writes things down that aren't for class--"

    s_thoughts "I'm doing it."

    s_thoughts "I'm standing in her room and I'm cataloguing her like she's a specimen."

    s_thoughts "Stop."

    s_thoughts "Stop it."

    s_thoughts "I take a breath."

    show amara embarrassed at center with dissolve

    s_thoughts "Amara is sitting on her bed. Watching me look at her room."

    s_thoughts "She's not smiling. She's not frowning. Her face is doing something I haven't seen before -- not neutral. Something quieter than neutral. Something that looks like it costs her a little, having another person see this space."

    a "You expected less."

    s "I expected-- I don't know what I expected."

    a "You expected quiet."

    s_thoughts "I look at the prints on the wall. The landscape-that-isn't. The woman with the clarinet."

    s "Yeah."

    show amara neutral at center

    a "Quiet people aren't empty."

    s_thoughts "That's it."

    s_thoughts "The room is very still."

    s_thoughts "I don't file that. I don't translate it. I just hear it."

    s "I know."

    s_thoughts "She looks at me for a second longer than normal."

    a "Do you play anything?"

    s "I played guitar for three months in ninth grade and then quit because my fingers hurt."

    s_thoughts "A beat."

    s_thoughts "Amara's mouth does something. Not a smile. A half-degree shift. The muscle memory of amusement."

    a "Three months."

    s "I'm not great at sticking with things."

    a "You're still at this university."

    s "Third major."

    a "Still here, though."

    s_thoughts "Something about the way she says that. 'Still here, though.' Like it matters. Like the staying is the thing, not the number of times you changed your mind about why."

    s "Yeah. Still here."

    s_thoughts "I look at the clarinet case."

    s "How long have you played?"

    a "Since I was eleven."

    s "That's a long time."

    a "It's the only thing I never quit."

    s_thoughts "She says it like she's reporting her findings. But the clarinet case with the stickers that she brought to university is sitting on her desk next to her pen case and her earrings."

    s_thoughts "I'm doing it again. Filing. Connecting. Building the picture."

    s_thoughts "But this time I catch it. I feel the instinct fire and I don't follow it. I just let the information sit there. Amara plays clarinet. She's played since she was eleven. The case has stickers. That's all I need. I don't need to know what it means."

    s "I should let you--"

    a "You can stay."

    s_thoughts "Simple. Said to the tea in her hands."

    s "Okay."

    s_thoughts "I sit in her desk chair. She's on the bed. The room is small enough that the distance between us is nothing."

    s_thoughts "She reads. I don't read. I just sit in Amara's room with Amara's art and Amara's clarinet and Amara's silence."

    pause 2.0

    hide amara with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 8: EVE CONNECTION
    ## Eve ships it. Brief, warm.
    ## "If she's talking to you, she chose to."
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_couch fadein 1.5

    s_thoughts "Friday morning. I'm making tea and thinking about clarinet stickers."

    s_thoughts "I've been thinking about clarinet stickers for approximately fourteen hours."

    show eve smile at center with dissolve

    s_thoughts "Eve is at the table. She appears there sometimes. Like weather."

    e "Morning."

    s "Morning."

    s_thoughts "Eve has a mug. Both hands. The green one with the chip. She's watching me fumble with a tea bag like it's entertainment."

    s_thoughts "I sit down across from her."

    e "You've been around more."

    s "Around?"

    e "The house. The common areas. The armchair zone."

    s "The armchair zone isn't a place."

    e "It's where Amara sits. You've been sitting near it."

    s_thoughts "I open my mouth. Close it."

    s "I've been studying downstairs. It's quieter than my room."

    show eve neutral at center

    s_thoughts "Eve looks at me. That direct, unhurried look. The one that says 'I see exactly what you're doing and I'm not going to make a thing of it but we both know.'"

    e "She doesn't waste words."

    s "Who?"

    s_thoughts "Eve gives me a look."

    s "Okay. Yeah. I know."

    e "If she's talking to you, she chose to."

    s_thoughts "I wait for more. There isn't more. Eve sips her tea."

    s "She doesn't talk to me that much."

    e "She doesn't talk to anyone that much."

    s_thoughts "Eve stands. Mug in both hands. She's done."

    e "The clarinet is nice."

    s "You've heard it?"

    show eve smile at center

    e "Everyone's heard it. She plays at night."

    s "I haven't--"

    e "You will."
    
    hide eve with dissolve

    s_thoughts "She leaves. The kitchen is just a kitchen."

    s_thoughts "Eve said that like she knows something. Like she's watched this before from the outside and she already knows how it goes."

    s_thoughts "The ghost rooting for somebody else."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 9: AMARA'S HUMOR
    ## Bone-dry joke. The room laughs. Amara is also BAD at something.
    ## amara smile -- ONCE.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_fivepeople fadein 1.5

    s_thoughts "Saturday. The kitchen. Everyone is here for once."

    show charlotte happy at left with dissolve
    show isabella happy at right with dissolve

    s_thoughts "Charlotte is making something elaborate. Something with layers. She's explaining the process to Isabella, who is nodding with the polite intensity of someone who will never make this recipe."

    c "And then you fold in the eggs -- not stir, FOLD. The folding is the whole thing."

    i "Folding. Got it. Definitely know what that means."

    c "It's like a hug! You're hugging the eggs into the batter!"

    i "Charlotte, I literally burn water."

    c "You can't burn water!"

    i "I have burned water. I have documentation."

    s_thoughts "I'm at the table. Eve is somewhere. Amara is at the counter, making tea."

    show amara neutral at center with dissolve

    s_thoughts "The kitchen is doing its thing -- the five-people energy where everyone is talking over each other and the room feels full in a way that's warm and slightly chaotic."

    c "Sophia, tell Isabella that cooking is just following instructions."

    s "Cooking is just following instructions."

    i "Instructions for WHAT though? The recipe says 'a pinch of salt.' How big is a pinch? Whose pinch? My pinch is different from Charlotte's pinch!"

    c "A pinch is a pinch!"

    i "That's CIRCULAR REASONING, Charlotte."

    s_thoughts "Amara is pouring hot water. She hasn't said anything."

    s_thoughts "Charlotte is explaining the difference between a pinch and a dash. Isabella is arguing that the imperial measurement system is a conspiracy against people who can't cook. I'm watching Amara add honey to her tea with the precision of someone defusing a bomb."

    c "You know what, next Sunday I'm teaching a cooking class. Everyone. Mandatory. We're all going to learn to fold eggs."

    i "I'm calling in sick."

    c "You LIVE HERE."

    a "She won't be staying home sick. She'll be leaving home sick."

    s_thoughts "The room goes quiet."

    s_thoughts "Amara said it to her tea. Deadpan. Not even looking at anyone."

    s_thoughts "Charlotte blinks."

    s_thoughts "Isabella processes."

    show isabella smile at right

    i "She--"

    show charlotte laugh at left

    c "Amara--"

    s_thoughts "Isabella starts laughing. Charlotte starts laughing. I start laughing."

    show amara smile at center

    s_thoughts "Amara's mouth does the thing. The real thing. Not the half-degree shift. An actual smile."

    s_thoughts "She's not looking at Charlotte. She's not looking at Isabella."

    s_thoughts "She's looking at me. For a half-second. Then she's not."

    s_thoughts "Something in my chest does-- no. I'm not cataloguing it. It happened. Moving on."

    show amara neutral at center

    s_thoughts "Amara picks up her tea. She turns to leave."

    s_thoughts "She catches the edge of the counter with her elbow. The tea sloshes. She flinches -- not at the spill, at herself. Like she's annoyed that her body did something ungraceful."

    show amara embarrassed at center

    a "..."

    c "Oh! Let me get a--"

    a "I have it."

    s_thoughts "She grabs a paper towel. Wipes the counter. Her ears are red."

    s_thoughts "Amara. The girl who moves through rooms like she was designed for them. The girl whose handwriting is perfect and whose pen never hesitates."

    s_thoughts "She just spilled her tea because she hit her elbow on the counter."

    show amara neutral at center

    s_thoughts "She finishes cleaning. She picks up the mug. She leaves without looking at anyone."

    s_thoughts "Charlotte looks at me."

    show charlotte smile at left

    c "She's funny. People forget she's funny."

    s_thoughts "People don't forget. They just don't get to see it often enough to remember."

    i "I still think a pinch is a conspiracy."

    hide amara with dissolve
    hide charlotte with dissolve
    hide isabella with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 10: LILA ASKS SERIOUSLY
    ## "What is it about her? I actually want to understand."
    ## Sophia articulates something true about Amara.
    ## Seeds Lila's need for later.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 1.5

    s_thoughts "Monday. Coffee on mine and Lila's bench."

    show lila happy at center with dissolve

    l "So. Karaoke rematch Friday."

    s "You already said that."

    l "I'm confirming. Because SOMEONE has been hard to pin down lately."

    s "I've been busy."

    l "Uh huh. Busy studying in the armchair zone."

    s "Did Eve tell you about the armchair zone?"

    l "Eve doesn't tell me things. I infer. I'm a business major. We infer."

    s "That's not what business majors do."

    show lila annoyed at center

    l "You're deflecting. You've been doing the voice again."

    s "I don't have a voice."

    l "You ABSOLUTELY have a voice. You used it just now. 'I've been busy.' With that little uptick at the end like you're already defending something I haven't accused you of."

    s_thoughts "I drink my coffee."

    s "Okay. Fine. What do you want to know?"

    show lila neutral at center

    s_thoughts "Lila shifts. The energy changes. She puts down her own coffee. She turns to face me on the bench."

    l "What is it about her?"

    s "What?"

    l "Amara. The quiet one. I'm not being mean. I actually want to understand."

    s_thoughts "She means it. The Lila filter -- the loudness, the sarcasm, the rapid-fire -- it's off. She's asking a real question."

    s "I don't know how to--"

    l "Try."

    s_thoughts "I think about it."

    s "She doesn't need anything from me."

    l "What do you mean?"

    s "Everyone else -- not in a bad way, but everyone else in that house needs something. Charlotte needs people to appreciate her. Isabella needs people to engage. Eve needs people to be patient."

    s "Amara doesn't need me to be anything. She's just... there. And if I'm there too, that's fine. And if I'm not, that's also fine."

    l "That sounds lonely."

    s "It's not. It's -- she CHOSE to let me in her room. She chose to tell me about the Nida chapter. She chose to make a joke while I was there to hear it."

    s "She doesn't need me. But she keeps choosing me anyway. Does that make sense?"

    show lila happy at center

    s_thoughts "Lila is quiet for a second. Lila is almost never quiet."

    l "Yeah. Actually. That makes sense."

    s_thoughts "A beat."

    l "You know what's weird? That's kind of the opposite of us."

    s "What do you mean?"

    l "You and me. I NEED you. Like, you're my person. I text you twelve times a day. I drag you to karaoke. I show up."

    l "Amara doesn't do any of that. And you're still drawn to her."

    s_thoughts "She doesn't say it with resentment. She says it like she's figuring something out."

    s "Lila, you're my best friend. That's not--"

    l "I know! I know. I'm not being jealous. I'm just -- I'm trying to understand the math. You have someone who shows up for you every day and someone who sits in an armchair and you're gravitating toward the armchair."

    s "It's not--"

    l "I'm not judging. I'm observing. Maybe I learned that from you."

    s_thoughts "She picks up her coffee. Drinks. The moment passes."

    show lila happy at center

    l "Okay. Enough feelings. Karaoke Friday. I'm bringing Amy from econ and she has a flask."

    s "Lila."

    l "What? I said enough feelings. This is logistics."

    s_thoughts "She's already on her phone, texting Amy from econ."

    s_thoughts "I watch her. The way she pivots. The way she goes from something real back to something safe. I recognize it because I do the same thing."

    l "Oh, also. I signed up for this peer counselor training thing."

    s "Oh yeah?"

    l "Yeah. It's whatever. They needed people and I have opinions."

    s "You'd be good at that."

    show lila shocked at center

    l "You think so?"

    s "You literally just made me articulate my feelings on a park bench. You'd be great."

    show lila happy at center

    l "Huh. Yeah. Maybe."

    s_thoughts "She says it quietly. For Lila. Which means at normal volume."

    l "Anyway. Friday. Seven. Wear the jacket. I've accepted the jacket."

    hide lila with dissolve

    s_thoughts "She leaves. The campus settles."

    s_thoughts "My phone buzzes. Lila: 'if she ever hurts you i will end her with my bare hands and a strongly worded email'"

    s_thoughts "I smile at my phone like an idiot."

    s_thoughts "She chose me anyway."

    s_thoughts "I think about that for the rest of the walk home."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 11: THE CLARINET
    ## 2 AM. Through the wall. Amara playing.
    ## The crush made concrete.
    ## Translation instinct: OFF. Just listening.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.5, 1.0)

    stop music fadeout 0.5

    s_thoughts "Tuesday. 2 AM."

    s_thoughts "I can't sleep. The usual. Brain replaying things, adding annotations, filing observations I didn't ask to make."

    s_thoughts "I'm lying in bed. My phone is facedown because I already checked it twice and there's nothing to check."

    s_thoughts "The house is quiet. The real kind. No Charlotte humming. No Isabella's music. Just the pipes and the fridge and the particular quality of silence that means everyone is asleep."

    s_thoughts "Except."

    pause 2.0

    s_thoughts "Through the wall."

    s_thoughts "Quiet. So quiet I almost don't hear it over the fridge."

    s_thoughts "Music."

    s_thoughts "Not a recording. Not someone's phone. The sound is different -- present in a way recordings aren't. There's breath in it. There are pauses between phrases where someone is breathing and then starting again."
    
    play music mus_amara fadein 2.0

    s_thoughts "Clarinet."

    pause 2.0

    s_thoughts "Amara."

    s_thoughts "She's playing. Through the wall. In the dark. At 2 AM."

    s_thoughts "I don't move."

    s_thoughts "The melody is -- I don't know music well enough to name it. Something slow. Something that rises and then comes back down. Not sad. Not happy. The kind of music that's about the space between those things."

    pause 1.5

    s_thoughts "Her room is on the other side of this wall. Fifteen feet away. She's in there with her battered case and her stickers from when she was thirteen and she's playing something for nobody."

    s_thoughts "For herself."

    s_thoughts "I lie in the dark and listen."

    pause 2.0

    s_thoughts "The filing instinct isn't running."

    s_thoughts "I notice that because I notice everything, except right now I'm not noticing things. I'm not cataloguing the melody or analyzing what it means that she plays at 2 AM or constructing a theory about what the song choice reveals."

    s_thoughts "I'm just listening."

    s_thoughts "She plays. The melody goes somewhere I didn't expect -- a run of notes that climb and then hold, one long note that fills the space between our walls, and then quiet."

    pause 2.0

    s_thoughts "She starts again. Different phrase. Softer."

    s_thoughts "I close my eyes."

    s_thoughts "This is -- I know what this is. This isn't fascination. This isn't curiosity. This isn't 'I find her interesting.' This isn't the way I felt about Katie or the philosophy girl or anyone."

    s_thoughts "This is the girl who said 'quiet people aren't empty' playing the proof through my wall."

    s_thoughts "And I'm lying here in the dark with my chest doing an architectural thing and my hands still and my brain quiet for the first time in weeks."

    s_thoughts "Oh."
    
    stop music fadeout 2.0

    pause 2.0

    s_thoughts "The music stops."

    s_thoughts "I hear the case click. A soft sound. The closing."

    s_thoughts "Silence."

    s_thoughts "I don't knock. I don't text. I don't go to her door."

    s_thoughts "I just lie here."

    s_thoughts "The silence after the clarinet is different from the silence before. It has the shape of what was just in it."

    s_thoughts "I fall asleep to the afterimage of a melody I can't name."

    ## ===========================
    ## SCENE 12: THE OBSERVATION SCENE
    ## Amara LOOKS BACK. The decoder decodes the observer.
    ## Translation instinct: FIRING -- then stopped by eye contact.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)

    play music mus_couch fadein 2.0

    s_thoughts "Wednesday. Late afternoon."

    s_thoughts "The living room. I'm on the couch with a book I'm pretending to read."

    s_thoughts "Isabella is on the floor, cross-legged, typing something on her laptop. Charlotte is in the kitchen -- I can hear her. Something sizzling."

    show amara neutral at right with dissolve

    s_thoughts "Amara is in the armchair."

    s_thoughts "She's not reading. She's looking at her phone. Scrolling something. Her face doesn't change as she scrolls."

    s_thoughts "I'm watching her."

    s_thoughts "I'm always watching her."

    s_thoughts "The angle of her jaw. The way her hair falls forward when she tilts her head down. The way she scrolls with her thumb -- slow, deliberate, the same rhythm she uses for everything."

    s_thoughts "I'm building the file again. The file that never fills. The file labeled AMARA KISMET that has observations and no conclusions."

    s_thoughts "She's wearing a navy sweater. The sleeves are too long. She's pushed them up to her elbows. Her wrists are--"

    s_thoughts "She looks up."

    s_thoughts "At me."

    s_thoughts "Direct."

    pause 1.5

    s_thoughts "She caught me."

    s_thoughts "She looked up from her phone and her eyes went straight to mine like she knew exactly where I was looking and she was waiting."

    s_thoughts "I should look away. That's the move. You get caught staring, you look away, you pretend you were looking at something else, you both go on with your lives."

    s_thoughts "I don't look away."

    s_thoughts "She doesn't look away."

    pause 1.5

    s_thoughts "Her face doesn't change. No surprise. No amusement. No embarrassment. She's just looking at me looking at her."

    s_thoughts "The filing instinct chokes. Stalls. I can't catalogue this because I'm inside it. I'm the object and the observer at the same time and the whole system breaks."

    s_thoughts "Something in the room shifts. Like the air pressure changed."

    show isabella neutral at left with dissolve

    s_thoughts "Isabella glances up from her laptop. Her eyes move from me to Amara and back."

    s_thoughts "She looks back at her laptop."

    s_thoughts "I look away first."

    show amara neutral at right

    s_thoughts "Amara goes back to her phone. Scrolling. Same rhythm. Like nothing happened."

    s_thoughts "Everything happened."

    s_thoughts "She looked back. She didn't flinch. She didn't deflect. She took my gaze and held it and returned it and then let it go."

    s_thoughts "The decoder decoded the observer."

    s_thoughts "My book is upside down. I turn it over. I don't read it."

    hide amara with dissolve
    hide isabella with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 13: NOVA'S CLASS -- THE TRANSLATOR'S BIAS
    ## "What if it's not meant for your language?"
    ## Anchored to Sophia failing to translate the look-back.
    ## ===========================

    scene bg classroom with Fade(0.8, 0.3, 0.8)

    play music mus_nova fadein 2.0

    s_thoughts "Thursday. Nova's class."

    s_thoughts "I have not recovered from yesterday."

    s_thoughts "I've been trying to translate the look. The eye contact. The thing that happened in the living room. What did it mean? Was it a challenge? An acknowledgment? Mutual attraction? A power move?"

    s_thoughts "I've translated it into twelve languages and none of them are right."

    show professor neutral at center with dissolve

    nova "Last week we talked about the translator's presence in the translation. The carrying changes the carried. You are never invisible."

    nova "Today I want to push that further."

    nova "When does translation become distortion?"

    s_thoughts "She lets the question land."

    nova "You read a text. You translate it. You add your own context, your own hearing, your own framework. At some point, the translation is more you than the original."

    nova "How do you know when you've crossed that line?"

    s_thoughts "I'm thinking about the file. The Amara file. The one I keep writing and rewriting. Is anything in it actually Amara? Or is it all me?"

    nova "Here's the harder question."

    show professor happy at center

    nova "What if the thing you're trying to translate isn't meant for your language?"

    s_thoughts "The room is quiet. That specific Nova-quiet."

    nova "Not everything is translatable. Not because language fails us -- but because some meanings are rooted in a context that doesn't travel."

    nova "The untranslatable isn't a gap. It's a boundary."

    nova "And the question for translators -- for observers -- for anyone who carries meaning from one person to another--"

    nova "The question is whether you can respect the boundary without trying to climb over it."

    show professor neutral at center

    s_thoughts "I write: the boundary. respect it. don't climb."

    s_thoughts "I think about Amara looking at me. The steady eye contact. What it meant."

    s_thoughts "Maybe it didn't mean anything I'm equipped to translate. Maybe her looking at me is in a language I don't speak yet. And the twelve translations I've been running since yesterday are just me shouting in English at someone who's speaking clarinet."

    hide professor with dissolve
    
    scene bg campus with dissolve

    s_thoughts "After class I start my walk home."

    s_thoughts "Nova's voice in my head: 'What if it's not meant for your language?'"
    
    s_thoughts "I think about that all the way home."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 14: THE FIRST REAL SOPHIA/AMARA SCENE
    ## Porch. Amara talks more than usual.
    ## "It's quieter when you're not doing it."
    ## Translation instinct: OFF. For the first time. Amara notices.
    ## ===========================

    scene bg porch with Fade(0.8, 0.5, 0.8)

    s_thoughts "The porch."

    s_thoughts "I came out here because the living room had Charlotte-energy and my room had ceiling-energy and I needed air that wasn't shaped by anyone."

    show amara neutral at center with dissolve

    s_thoughts "Amara is sitting on the steps."

    s_thoughts "She's not reading. She's not on her phone. She's just sitting."

    s_thoughts "The light is doing the late-afternoon thing. Everything gold."

    s "Hey."

    a "Hey."

    s_thoughts "Two words. One each. Equal."

    s_thoughts "I sit on the steps. Not next to her. One step below. Close enough to talk. Far enough to not crowd."

    pause 1.5

    s_thoughts "The street is quiet. A car passes. A bird does a thing."

    s_thoughts "I don't say anything. Amara doesn't say anything."

    s_thoughts "The silence is comfortable in a way I'm still getting used to. Like a sweater that's slightly too big but warm."

    pause 2.0

    a "The light is good today."

    s "Yeah."

    a "This porch faces west. I checked when I moved in."

    s "You checked which direction the porch faces?"

    a "I check things."

    s "Like which direction the light comes from."

    a "Like whether I'll have a place to sit in the evening."

    s_thoughts "She's talking. More than usual. Not a lot more. But the sentences are longer. She's offering things -- the porch direction, the light, the checking."

    s_thoughts "She's sharing something. Small. Practical. Real."

    a "The other house I looked at had an east-facing porch. Morning light. I don't like mornings."

    s "Me either."

    a "You come downstairs at ten with an expression that suggests morning is a personal insult."

    s_thoughts "I blink."

    s "You noticed that?"

    a "You're not subtle."

    s_thoughts "A beat."

    s "I thought I was subtle."

    a "You're not."

    s_thoughts "She's--"

    s_thoughts "She's been watching me."

    s_thoughts "The same way I've been watching her."

    a "You're different in the evening."

    s "How?"

    a "Quieter. Less..."

    s_thoughts "She pauses. Choosing the word."

    a "...armed."

    s_thoughts "Armed."

    s "You think I'm armed in the morning?"

    a "You walk into rooms prepared."

    s_thoughts "My throat does a thing."

    s "That's... really specific."

    a "I notice specific things."

    s_thoughts "We sit."

    s_thoughts "The light is gold. A leaf falls onto the step between us."

    s_thoughts "I'm not doing the thing."

    s_thoughts "I'm just here. On a porch. In the gold light. With Amara."

    pause 2.0

    a "You're not doing the thing."

    s "What thing?"

    a "The thing where you translate me in your head."

    s_thoughts "My heart stops."

    s_thoughts "Not metaphorically. There's a skip. A hiccup. A moment where the muscle forgets what it's supposed to do."

    s "I don't--"

    a "You do."

    s_thoughts "I don't know what to say."

    s "Is it that obvious?"

    a "To me."

    s_thoughts "To me. Not 'to everyone.' To me."

    pause 1.5

    a "It's quieter when you're not doing it."

    s_thoughts "I feel every single word."

    s_thoughts "'It's quieter when you're not doing it.'"

    s_thoughts "She means: when I stop translating her, the space between us changes. The interference drops. The signal clears."

    s_thoughts "No."

    s_thoughts "She means exactly what she said. It's quieter. That's it. I don't need to translate the sentence about translation."

    s "I'm trying."

    a "I know."

    pause 2.0

    s_thoughts "The light shifts. Gold to amber."

    s_thoughts "Amara is looking at the street. I'm looking at Amara looking at the street."

    s_thoughts "I'm just... looking."

    s_thoughts "She knows I'm looking."

    s_thoughts "She doesn't mind."

    s_thoughts "Something about that -- the not-minding -- is the most intimate thing that's happened to me since I moved into this house."

    a "The chicken place on Fourth is good."

    s "What?"

    a "Charlotte was asking what everyone wanted for the house dinner. I said the chicken place on Fourth."

    s "Oh. I haven't been."

    a "Their fries are the right amount of crispy."

    s "That's a very specific compliment."

    a "Specificity is respect."

    s_thoughts "I laugh. Small. From somewhere quiet and simple."

    s "Specificity is respect. That should be on a poster."

    s_thoughts "The half-degree shift. The almost-smile."

    a "I should go in. Homework."

    s "Yeah. Me too."

    s_thoughts "She stands. She doesn't say goodbye. She goes inside."

    s_thoughts "I stay on the porch."

    s_thoughts "The light goes amber to something softer. The street is empty."

    hide amara with dissolve

    pause 2.0

    s_thoughts "It's quieter when you're not doing it."

    s_thoughts "She named the thing. The thing I've been doing to everyone since I learned to watch."

    s_thoughts "She named it and she wasn't angry about it. She just noticed."

    s_thoughts "She noticed me the way I notice everyone."

    s_thoughts "And when I stopped -- when the machine turned off for ten minutes on a porch in the gold light -- she noticed that too."

    s_thoughts "My phone buzzes."

    s_thoughts "Lila: 'friday still on??? also I found the BEST karaoke place. it has a fog machine.'"

    s_thoughts "I type: 'Friday still on. But a fog machine is a red flag, Lila.'"

    s_thoughts "Lila: 'a fog machine is a GREEN flag for people who know how to have FUN'"

    s_thoughts "I smile at my phone."

    s_thoughts "Two frequencies."

    s_thoughts "I don't know which one to tune to."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 15: LILA CHECK-IN
    ## Post-threshold. "She caught me watching and she didn't look away."
    ## Seeds Lila's need.
    ## ===========================

    scene bg dininghall with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 1.5

    s_thoughts "Friday. Dining hall. The pre-karaoke debrief."

    show lila happy at center with dissolve

    l "Okay, game plan. Amy's bringing the flask. I've got the playlist queued. We're starting with Britney and ending with-- why are you making that face?"

    s "I'm not making a face."

    l "You're making the face. The 'something happened and I'm going to pretend it didn't until you drag it out of me' face."
    
    s "Okay now THAT is way too specific to be a face."

    s_thoughts "I hate that she can read me."

    s "...Something happened."

    l "TELL ME."

    s "She caught me watching her."

    show lila shocked at center

    l "The armchair girl?"

    s "Amara. And she didn't look away."

    l "SHE didn't look away? Or YOU didn't look away?"

    s "Neither of us. For like... a while."

    l "Define 'a while.'"

    s "Long enough that Isabella noticed."

    show lila laugh at center

    l "Oh my GOD."

    s "And then on the porch she said--"

    s_thoughts "I stop."

    l "She said WHAT."

    s "She said it's quieter when I'm not... doing the thing."

    l "What thing?"

    s "The watching thing. The translating thing. The thing where I turn people into files."

    s_thoughts "Lila is quiet. Processing."

    show lila neutral at center

    l "That's either flirting or a power move and with that girl I genuinely cannot tell."

    s "It felt like-- I don't know what it felt like."

    l "It felt like she SEES you."

    s "Yeah."

    l "Like, she actually sees you. Not the fun version, not the observer version. The actual you."

    s "That's terrifying."

    l "That's hot."

    s "LILA."

    show lila happy at center

    l "I'm being supportive! That's support! She sees you and you're terrified and that's the beginning of every good love story."

    s "I didn't say love."

    l "You didn't have to. You're doing the voice again."

    s_thoughts "I groan."

    l "Look. I'll say one serious thing and then we're talking about karaoke."

    s "One serious thing."

    show lila neutral at center

    l "You spend a lot of time thinking about the armchair girl."

    s "Amara."

    l "You spend a lot of time thinking about Amara. And I get it. She's different. She's interesting. She's hot. She SEES you."

    l "Just... don't disappear into it. Okay? You do that. You find someone fascinating and you disappear."

    s "I don't--"

    l "You do. Katie. The philosophy girl. You find someone and the rest of us get the leftovers."

    s_thoughts "She says it lightly. But the light has weight."

    s "You're not leftovers, Lila."

    show lila happy at center

    l "I know! I'm the main course. I'm telling you not to forget that."

    s_thoughts "She smiles. Big. Real."

    s_thoughts "But something underneath. Something she's not saying."

    l "Okay. Serious thing over. Karaoke."

    s "Karaoke."

    l "But first-- ugh."

    s_thoughts "Her phone buzzes. She glances at it. Her face does a thing I haven't seen before. Not annoyed. Not happy. Something complicated."

    s "Everything okay?"

    l "Yeah. Just-- the peer counselor thing. They want us to do this training weekend and I--"

    s_thoughts "She stops. Puts her phone away."

    show lila happy at center

    l "It's fine. It's a scheduling thing. Whatever."

    s_thoughts "It's not a scheduling thing. I can hear it in the way she said 'whatever.' Lila's 'whatever' is the loudest word she has."

    s_thoughts "I should ask."

    s_thoughts "She changes the subject."

    l "SO. Fog machine karaoke. Amy has a flask and no shame. It's going to be ICONIC."

    s_thoughts "I let her change it."

    s_thoughts "I shouldn't let her change it."

    s_thoughts "But I let her change it."

    hide lila with dissolve

    stop music fadeout 2.0

    s_thoughts "The dining hall empties around us. Lila leaves for her afternoon class. I sit with my cold coffee."

    s_thoughts "'Don't disappear into it.'"

    jump amara_ch4_act2

    ## ===========================
    ## END OF ACT 1
    ## ===========================

## === ADDITIONAL AUDIO DEFINITIONS ===
define audio.mus_wrong = "audio/music/Something Wrong in the Kitchen.mp3"
define audio.mus_mourning = "audio/music/Mourning.mp3"
define audio.mus_threshold = "audio/music/The Threshold.mp3"
define audio.mus_glass = "audio/music/Glass Walls.mp3"

## ===========================
## ACT 2: "THE PULL"
## The two frequencies intensify and collide.
## Scenes 16-24.
## ===========================

label amara_ch4_act2:

    ## ===========================
    ## SCENE 16: THE LIBRARY DEEPENS
    ## The ritual. Compare notes. Amara reframes Sophia's reading.
    ## Translation instinct: Quieter. Learning the language.
    ## ===========================

    scene bg library with Fade(1.5, 1.0, 1.5)

    play music mus_shoulders fadein 2.0

    s_thoughts "The following Tuesday. The library."

    s_thoughts "Our table."

    s_thoughts "I say 'our table' now. I didn't decide to. It just happened. Amara is at it when I arrive. I sit in the chair one table away. Neither of us comments on the arrangement."

    s_thoughts "This is the fourth time."

    show amara neutral at center with dissolve

    s_thoughts "She's reading something new. Smaller than the last one. The cover is pale blue with Japanese text across the top and what looks like an English subtitle I can't quite--"

    s_thoughts "I lean forward. Barely."

    s_thoughts "{i}Born Translated: The Contemporary Novel in an Age of World Literature.{/i}"

    s_thoughts "She's reading about translation theory."

    s_thoughts "The same week I'm reading about translation theory."

    s_thoughts "Coincidence. Probably. Amara reads three books a week and the university library has a decent linguistics section and this doesn't mean anything."

    s_thoughts "The filing instinct stirs. I push it down."

    s_thoughts "I open my own book. Nova's assigned reading this week. Jakobson on linguistic aspects of translation. I've read the first section twice and highlighted a sentence about interlingual translation as interpretation."

    pause 1.5

    s_thoughts "We read."

    s_thoughts "The library is quietly loud. A student at a far table is typing with the specific fury of someone who has a deadline. The air conditioning cycles on."

    s_thoughts "Amara turns a page."

    s_thoughts "I turn a page."

    s_thoughts "Twenty minutes. Maybe thirty. The quiet doesn't itch like it used to."

    a "What did Nova assign this week?"

    s_thoughts "She says it without looking up."

    s "Jakobson. On the types of translation."

    a "Intralingual, interlingual, intersemiotic."

    s "You've read it?"

    a "Last year."

    s "Of course you have."

    s_thoughts "A beat."

    a "What did you highlight?"

    s "How do you know I highlighted something?"

    a "You always highlight. You press hard. I can see the marks from here."

    s_thoughts "She can see my highlights from one table away."

    s_thoughts "I don't know what to do with that information."

    s "The part about how interlingual translation is interpretation, not just substitution. That the translator is always making choices."

    s_thoughts "Amara puts her finger in her book to hold her page. She looks at me."

    show amara neutral at center

    a "Jakobson's wrong about one thing."

    s "What?"

    a "He treats the three types as categories. They're not. They overlap. Every translation is all three at once."

    s "What do you mean?"

    a "When you translate a sentence from French to English, you're also changing the register within English. And you're also turning sound into different sound." 
    
    a "It's not one kind of translation. It's all of them simultaneously."

    s_thoughts "I stare at her."

    s_thoughts "She said more words in the last thirty seconds than she says in most entire conversations."

    a "Sorry. I have opinions about this."

    s "No. Keep going."

    s_thoughts "She looks at me for a second. Assessing whether I mean it."

    a "The interesting part isn't the categories. It's what gets lost between them. The residue."

    s "The residue?"

    a "What's left over when the translation is done. The part that doesn't make it across."

    s_thoughts "I think about the porch. 'It's quieter when you're not doing it.' The thing I keep trying to translate and can't."

    s "Like untranslatable words."

    a "Like untranslatable silences."

    pause 1.0

    s_thoughts "She goes back to her book."

    s_thoughts "I go back to mine."

    s_thoughts "Except I'm not reading. I'm sitting with 'untranslatable silences' and the fact that Amara has opinions about Jakobson and she just shared them with me in a library on a Tuesday."

    s_thoughts "My phone buzzes. Lila: 'study sesh at the dininghall? im buying nachos'"

    s_thoughts "I type: 'Can't. At the library.'"

    s_thoughts "Lila: 'the armchair girl has a library now??'"

    s_thoughts "I don't respond."

    s_thoughts "Amara turns a page."

    hide amara with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 17: LILA NIGHT #2 AT THE HOUSE
    ## Wine in the kitchen. Charlotte joins. Amara absent.
    ## "Maybe she doesn't like fun."
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_playlist fadein 2.0

    s_thoughts "Friday night."

    s_thoughts "Lila brought wine. The kind that comes in a box, which she insists is 'economically responsible' and I insist is 'a cry for help.'"

    show lila happy at left with dissolve

    l "It's EFFICIENT. You don't have to deal with a cork!"

    s "You don't have to deal with self-respect either, apparently."

    l "Self-respect is for people who didn't just ace their econ midterm. Tonight we CELEBRATE."

    s "You got a B+."

    l "Which is an A in Lila math!"

    s_thoughts "She pours wine into mugs because we can't find the wineglasses Charlotte bought that one time. Charlotte insists they're in the cabinet above the fridge."

    show charlotte pj happy at right with dissolve

    c "They're up there! Behind the -- here, let me--"

    s_thoughts "Charlotte is on her tiptoes reaching for the top shelf. She's in pajamas. Fuzzy socks. She should not be attending a wine celebration, but Charlotte cannot resist the gravitational pull of someone needing help in the kitchen."

    l "Charlotte! Join us!"

    c "Oh, I wasn't going to -- I mean, I have reading to do, but--"

    l "Reading can wait. Wine cannot."

    show charlotte pj smile at right

    c "Well. Just one glass."

    s_thoughts "She finds the wineglasses. They're dusty. She washes them. Lila pours."

    l "To my B+."

    s "To Lila math."

    c "To everyone being home on a Friday!"

    s_thoughts "We clink. Charlotte drinks like someone who's read about wine drinking in a magazine. Lila drinks like someone who plans to finish the box."

    l "Okay so TELL ME about the house. Sophia never tells me anything. What's the gossip? Who's hooking up? Who's leaving passive-aggressive notes on the fridge?"

    show charlotte pj laugh at right

    c "Nobody's hooking up!"

    l "That's statistically impossible. Five girls. One house. Someone's got a thing."

    s_thoughts "I very carefully do not look at the hallway."

    c "We're all just friends! It's very healthy!"

    l "Healthy is suspicious. Healthy means someone's hiding something."

    s_thoughts "Charlotte laughs. Lila is delighted with Charlotte. Charlotte is delighted with being delighted in. This is a closed loop of mutual appreciation."

    s_thoughts "Isabella drifts through. Hair up. Oversized shirt. She sees the wine."

    show isabella pj happy at center with dissolve

    i "Ooh. Is this a thing?"

    l "It's a CELEBRATION. B+!"

    i "Congrats! I'd stay but Lumi and I are in the middle of a--"

    s_thoughts "She catches herself."

    i "A thing. A project thing."

    l "At 9 PM on a Friday?"

    show isabella pj smile at center

    i "Projects don't sleep, Lila."

    s_thoughts "She grabs an apple from the counter and disappears back upstairs. Her door closes. Faintly, I can hear her laugh at something."

    hide isabella with dissolve

    l "She's always doing a project."

    s_thoughts "Yeah."

    s_thoughts "I drink my wine. It's actually not terrible. Don't tell Lila I thought that."

    l "Okay what about the quiet one? Amara? Is she here?"

    c "She's in her room, I think."

    l "Does she ever come to things? Like -- house things? Wine things?"

    show charlotte pj neutral at right

    c "Sometimes."

    l "It's Friday and she's in her room."

    s_thoughts "Something protective flares in my chest."

    s "She's just--"

    l "Maybe she doesn't like fun."

    c "She does! She has fun. Just not... this kind."

    show lila annoyed at left

    l "What other kind is there?"

    s_thoughts "Charlotte doesn't answer. She swirls her wine."

    s_thoughts "The silence lasts exactly long enough to be uncomfortable."

    show lila happy at left

    l "Whatever. More wine for us. Charlotte, tell me about the egg-folding thing. Sophia said you tried to teach everyone to cook?"

    show charlotte pj happy at right

    c "Oh! Yes! So the folding technique--"

    s_thoughts "Charlotte pivots into a story about eggs and Lila pivots with her and the kitchen is warm and loud and the box wine flows."
    
    s_thoughts "I'm still glancing over at Amara's door. Closed."
    
    show lila annoyed at left
    
    l "Earth-to-Sophia. Earth-to-Sophia."
    
    s_thoughts "I try not to look startled but I was slightly zoned out."
    
    s "Yes?"
    
    l "You're staring."
    
    s "At what?"
    
    l "Armchair girl's room."
    
    c "Armchair girl?"
    
    l "Armchair girl."
    
    c "...Ohhhh!"
    
    s "She has a name."
    
    c "I don't know, I kind of like armchair girl."
    
    show lila drunk at left
    
    l "Sophia is down bad for armchair girl."
    
    show charlotte pj embarrassed at right
    
    c "Oh?"
    
    s "LILA."
    
    l "WHAT?"
    
    s "STOP."
    
    l "IT'S TRUE."
    
    show charlotte pj laugh at right
    
    c "Is it? I thought you were just becoming her closest friend. Besides Eve."
    
    s "We are just friends. That's all."
    
    l "Just-friends don't stare at each other's closed doors."
    
    s "I hate you."
    
    l "Babe. You're down bad. Admit it."
    
    show charlotte pj neutral at right
    
    s_thoughts "Charlotte makes a face. Before I can file it she's already back to the smile. She sips her wine."
    
    show charlotte pj happy at right
    
    c "I have a bit of a crush."
    
    l "OH? Spill the tea, sis."
    
    s "I'm intrigued."
    
    c "It's nothing. Just a cute girl in my art history class."
    
    c "We did a peer review of each other's papers and she told me my paper seemed 'personal' and I didn't know what to do with that information."
    
    s "What was her paper about?"
    
    c "Van Gogh. About the artistic expression of grief and loss."
    
    show lila annoyed at left
    
    l "CHARLOTTE."
    
    show charlotte pj surprised at right
    
    c "W-What?"
    
    l "You're gonna try and fix this girl."
    
    c "I'm--"
    
    s "She has a point."
    
    show charlotte pj embarrassed at right
    
    c "Surely I don't have THAT MUCH of a pattern?"
    
    l "Babe. You're a checkerboard."
    
    s_thoughts "I laugh at that. Charlotte is blushing."
    
    c "Okay, okay, fine. But she's cute. Surely I can't be blamed for crushing on the cute sad-girl."
    
    s "I don't blame you."
    
    show lila drunk at left
    
    l "Oh shush! Figures she who crushes on the quiet-girl affirms the sad-girl crush."
    
    s "LILA. VOLUME."
    
    s_thoughts "My eyes dart to Amara's room. Nothing."
    
    l "Oh please. She totally already has you figured out anyway."
    
    show charlotte pj laugh at right
    
    s_thoughts "Charlotte is amused by that."
    
    c "Totally."
    
    s "Charlotte, you just admitted you had no idea--"
    
    c "Sorry! Sorry. It's just Amara. She's like that."
    
    show charlotte pj happy at right
    
    c "I hope it works out for you."
    
    s_thoughts "A twinge of something in her voice. I can't quite make it out."
    
    l "More wine, ladies?"
    
    c "Please!"
    
    s_thoughts "I hand her my glass. I'm not paying attention."

    s_thoughts "Amara's door stays closed."

    s_thoughts "I'm here. I'm having fun. The filing instinct is quiet because there's nothing to file. Just friends in a kitchen."

    s_thoughts "And a closed door I keep not looking at."
    
    s_thoughts "I take another sip."

    hide lila with dissolve
    hide charlotte with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 18: THE CRUSH NAMED INTERNALLY
    ## "I have a crush on the quietest girl in the house. I'm an idiot."
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    stop music fadeout 0.5

    s_thoughts "Later. My room. The wine is wearing off and the clarity is moving in like a cold front."

    s_thoughts "I'm lying on my bed."
    
    s_thoughts "Lila's words annoyingly echo in my head."
    
    s_thoughts "'Sophia is down bad for armchair girl.'"
    
    s_thoughts "Surely not."
    
    s_thoughts "...Surely."

    s_thoughts "But I've been lying on my bed for twenty minutes and I notice I'm thinking about the way Amara said 'untranslatable silences.'"

    s_thoughts "I have been translating her silences."

    s_thoughts "I've been translating them as 'fascination.' As 'curiosity.' As 'intellectual interest.' As 'I just find her interesting as a person.'"

    s_thoughts "These are lies."

    s_thoughts "These are lies I've been telling myself with increasing desperation because the truth is simple and enormous and embarrassing."

    pause 1.5

    s_thoughts "I have a crush on the quietest girl in the house."

    s_thoughts "The one I can't decode."

    s_thoughts "The one who decoded me in one sentence."

    s_thoughts "I'm an idiot."

    pause 1.0

    s_thoughts "I roll over. Put my face in my pillow."

    s_thoughts "This is -- how did this happen? She said 'okay' in a living room and I lost my entire mind."

    s_thoughts "She has a pen case. She plays clarinet. She reads three books a week. She checked which direction the porch faces when she moved in."

    s_thoughts "She looked at me and didn't look away."

    s_thoughts "She said it's quieter when I stop."

    s_thoughts "And my stupid, disaster, file-everything brain went 'yes. her. the one who barely talks. that's the one.'"

    s_thoughts "I'm an idiot."

    s_thoughts "My phone buzzes. Lila: 'tonight was fun!! next friday same thing but we find better wine??'"

    s_thoughts "I type 'Deal.' and stare at the ceiling."
    
    s_thoughts "Another text. 'sorry to reveal all your secrets to charlotte'"
    
    s_thoughts "My reply: 'She had no idea, did she?'"
    
    s_thoughts "'not in the slightest lol'"
    
    s_thoughts "I take a second to reply to that."
    
    s_thoughts "'Do you really think Amara has me figured out?'"
    
    s_thoughts "'idk honestly. she seems like the type. but then again when i first met charlotte i was like SHE'S TOTALLY SOPHIA'S TYPE.'"
    
    s_thoughts "'WHAT' comes my instant reply."
    
    s_thoughts "'babe. she's a walking bundle of loose leaf papers just BEGGING to be filed.'"
    
    s_thoughts "I stare at my phone. Lila texts again."
    
    s_thoughts "'if you don't file her maybe i will >:)'"
    
    s_thoughts "Dammit, Lila. I text back: 'Housemates are OFF LIMITS.'"
    
    s_thoughts "Lila sends a series of inscrutable emojis."
    
    s_thoughts "I put my phone down."

    s_thoughts "Through the wall. Faint. The clarinet."

    s_thoughts "I close my eyes."

    s_thoughts "I'm so screwed."

    ## ===========================
    ## SCENE 19: WHOLE-HOUSE ENSEMBLE
    ## All five girls. The house being a house.
    ## Amara/Eve quiet understanding. Sophia sees what she has.
    ## ===========================

    scene bg livingroom with Fade(0.8, 0.3, 0.8)

    play music mus_fivepeople fadein 2.0

    s_thoughts "Sunday afternoon. The living room."

    s_thoughts "Something rare is happening."

    s_thoughts "Everyone is here."

    show charlotte happy at left with dissolve

    s_thoughts "Charlotte is on the floor, cross-legged, with a sudoku book and a pencil she keeps tapping against her lip. She's also got a notebook next to her with what looks like a cleaning schedule written in three colors."

    show isabella happy at right with dissolve

    s_thoughts "Isabella is on the couch, laptop open, earbuds in one ear. She's half-watching something and half-reading something else. Peak Isabella multitasking."

    show amara neutral at center with dissolve

    s_thoughts "Amara. Armchair. Book."

    s_thoughts "Eve is in the corner of the couch farthest from everyone. She has a mug. Both hands. She's looking at nothing in particular."

    s_thoughts "I'm on the other end of the couch from Isabella, pretending to read. Mostly watching."

    s_thoughts "The room is doing that thing. The five-people thing. The low hum of coexistence that sounds like pages turning and pencils tapping and the heater cycling and someone's stomach growling."

    i "Okay does anyone else think the wifi is slower than usual or is it just my paranoia?"

    c "I think it's the same!"

    i "Charlotte, you use the internet to look up recipes. Your bar is different."

    s_thoughts "Charlotte makes a noise of protest. Isabella grins."

    c "I use the internet for LOTS of things!"

    i "Name one non-recipe thing you googled this week."

    show charlotte embarrassed at left

    c "I looked up... I looked up how to get red wine stains out of a--"

    i "That's a recipe for stain removal. That's still a recipe."

    s_thoughts "Charlotte sputters. Isabella is delighted with herself."

    show charlotte happy at left

    c "Oh! Speaking of organization -- I made a new fridge chart. For the shelves? Because someone keeps putting their yogurt on MY designated shelf."

    i "Charlotte, we don't have designated shelves."

    c "We DO now! I made labels!"

    s_thoughts "She holds up the notebook. There are indeed labels. Color-coded. Each housemate has a shelf color. Mine is peach."

    i "Why am I orange?"

    c "Because your hoodie is green and I didn't want to match too closely. It's about contrast!"

    i "I want to dispute the logic but I respect the commitment."

    s_thoughts "Amara reads."

    s_thoughts "Isabella's phone buzzes. She picks it up, grins, and tilts it toward the room."

    i "Look at this. Lumi generated a statistical model of how often each of us uses the kitchen. Based on the sounds I described."

    show isabella smile at right

    i "Charlotte is at 43 percent. Amara is at 7."

    c "I'm not THAT much more than everyone else!"

    i "You're literally more than five times Amara, Charlotte."

    s_thoughts "Amara turns a page without looking up."

    a "Seven is generous."

    s_thoughts "Isabella snorts."

    s_thoughts "Eve shifts on the couch. She glances across the room."

    s_thoughts "At Amara."

    s_thoughts "Amara doesn't look up. But something in her posture adjusts. A millimeter. Like she knows Eve looked and she's acknowledging it without acknowledging it."

    s_thoughts "Eve looks back at her mug."

    s_thoughts "Two people who do silence differently but recognize each other's version."

    s_thoughts "Charlotte reaches for the TV remote."

    c "Should we watch something? Since everyone's here?"

    i "Depends. If Charlotte picks, it's going to be a baking show."

    c "What's wrong with baking shows!"

    i "Nothing! They're just -- Charlotte, we watched six episodes of British Bake-Off last weekend. I dreamed about fondant."

    s_thoughts "Eve, from the corner, without moving:"

    e "There are worse dreams."

    i "Eve. You can't just DROP a sentence like that and not elaborate."

    s_thoughts "Eve sips her tea."

    s_thoughts "She does not elaborate."

    i "See? This. This is what I live with."

    c "What about a movie? Something everyone likes?"

    i "Define 'everyone.' Because Amara's going to want something with subtitles and I'm going to want explosions and Eve's going to want -- actually, Eve, what do you want?"

    e "I'm fine with anything."

    i "That's not helpful!"

    e "I know."

    s_thoughts "I catch the ghost of something on Eve's face. Not quite a smile. A flicker."

    s_thoughts "Amara's book lowers half an inch. She's listening. Her eyes move to Eve and back to the page."

    c "Okay, okay. I'll pick something neutral. Something EVERYONE can enjoy."

    i "Charlotte. If you put on a baking show I'm staging a coup."

    c "It's not a baking show! It's a cooking competition. There's a difference!"

    i "CHARLOTTE."

    s_thoughts "Charlotte is already navigating to the show. Isabella throws a couch pillow at her. Charlotte catches it and puts it neatly on the floor."
    
    c "Oh! I forgot to say -- the chicken place on Fourth is having a special. Should we do a house dinner?"

    i "Yes please."

    s_thoughts "Eve nods."

    s_thoughts "Amara reads through all of this. But the book is lower than before. She's been listening to the whole thing."

    s_thoughts "She makes one dry comment to the room at large, delivered to her page."

    a "Their fries."

    c "Right! Amara mentioned the fries! I'll order tonight."

    s_thoughts "Charlotte is already making a mental list. I can see it happening behind her eyes -- the planning, the organizing, the making-everyone-happy machinery spinning up."

    s_thoughts "Isabella reaches over to the coffee table and grabs a bag of chips. Except the bag crinkles and Eve says, without looking:"

    e "Those are mine."

    i "Since when do you buy chips?"

    e "Since always. You just never noticed because I eat them at 3 AM."

    i "That's deeply troubling, Eve."

    e "Thank you."

    s_thoughts "Isabella puts the chips back. She reaches for a different bag. Then stops."

    i "Charlotte, are THESE also someone's?"

    c "Those are communal! I bought those!"

    i "Blessings upon your entire family line, Charlotte Opal."

    s_thoughts "Charlotte beams."

    s_thoughts "Amara catches my eye. Brief. The corner of her mouth."

    s_thoughts "She remembered the fries conversation. From the porch. I mentioned I hadn't been."

    s_thoughts "And now Charlotte is ordering for the house."

    s_thoughts "I don't translate it. I just notice."

    s_thoughts "The TV is on now. Some kind of cooking show. Isabella is protesting. Charlotte is insisting it's different from the last one. Eve is watching the screen with an expression of mild interest that she'll maintain for exactly one episode before disappearing."

    s_thoughts "Amara is reading. But her book is closed around one finger now, holding the page. Half-in, half-out."

    i "Sophia. Why do you look like you've been constipated all day."

    s "Excuse me?"

    i "You're staring at everything in the living room with a certain intensity."

    s "My bowels are fine."

    i "Are you sure? Because you look like this--"

    s_thoughts "Isabella scrunches her forehead and squints."

    show isabella smile at right

    i "See?"

    c "You're reading into it!"

    i "She's reading into whether we have any laxatives in the bathroom."

    s_thoughts "I laugh. I can't help it."

    s_thoughts "Amara is reading. But she's smiling. The half-degree shift. There and then not."

    s_thoughts "Eve has curled up tighter on the couch. Not pulling away -- settling in. She's watching the show. She looks almost comfortable."

    s_thoughts "Charlotte is on the floor explaining to Isabella why this season is superior to the last one. Isabella is eating communal chips and pretending to disagree."

    s_thoughts "Amara turns a page."

    pause 1.5

    s_thoughts "This is what I have."

    s_thoughts "Five people in a room."

    s_thoughts "I should remember what this feels like."

    s_thoughts "The specific weight of a room where everyone is present and nobody is performing and the silence between the noise is the comfortable kind."

    s_thoughts "I don't know why my throat does a thing."

    s_thoughts "Something in the back of my brain -- the part that watches, always watches -- is taking a photograph. Framing it. The angle of the light. Charlotte on the floor. Isabella mid-chip. Eve with both hands on the mug. Amara in the armchair. Me on the couch."

    s_thoughts "Like I already know this is the version I'll want to come back to."

    s_thoughts "I don't know what I mean by that."

    s_thoughts "I watch the cooking show. Charlotte explains the difference between julienne and brunoise. Isabella throws another chip at the screen. Eve finishes her tea and doesn't get up for more."

    s_thoughts "Amara reads."

    s_thoughts "The room holds."

    hide charlotte with dissolve
    hide isabella with dissolve
    hide amara with dissolve

    stop music fadeout 2.0
    ## ===========================
    ## SCENE 20: AMARA/LILA COLLISION
    ## Same room. Two languages. No fight. Just the gap.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_couch fadein 1.5

    s_thoughts "Tuesday."

    s_thoughts "Lila is at the house. She came to pick me up for a study session and got sidetracked by Charlotte's banana bread."

    show lila happy at left with dissolve

    l "Charlotte, this is CRIMINAL. How is it this good? Is there a secret ingredient? Tell me the secret ingredient."

    show charlotte smile at right with dissolve

    c "It's just banana bread! The secret is overripe bananas!"

    l "See, that's the kind of wisdom they don't teach in business school."

    s_thoughts "Lila is at the counter, eating her second slice. Charlotte is glowing. I'm at the table, bag packed, waiting."

    s_thoughts "The door from the hallway opens."

    show amara neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "She stops in the doorway. Registers the scene. Lila at the counter. Charlotte at the stove. Me at the table."

    s_thoughts "She walks to the kettle."

    l "Amara! Hey! We met at the karaoke -- well, you weren't AT the karaoke, but I was here after. On the floor."

    a "I remember."

    l "Banana bread?"

    a "No. Thank you."

    s_thoughts "Amara fills the kettle. Clicks it on. Waits."

    s_thoughts "Lila watches her for a second. Then pivots back to Charlotte."

    l "So Charlotte, I had this idea--"

    s_thoughts "But she doesn't fully pivot. I can see it. Lila is calibrating. Lila calibrates people the way I do, except she does it at full volume and I do it in my head."

    s_thoughts "She tries again."

    l "Amara, what kind of tea?"

    a "Green."

    l "Nice. I'm a chai person myself. LOADS of sugar. It's basically dessert."

    a "Mm."
    
    s_thoughts "I can see Amara mentally resisting telling Lila what 'chai' means."

    l "Do you put anything in yours? Honey? Lemon? Milk? I know some people do milk, which is--"

    a "Just green."

    s_thoughts "Two words."

    s_thoughts "Lila blinks."

    l "Cool. Simple. I respect simple."

    s_thoughts "She's trying. She's genuinely trying. Lila is extending the thing she extends to everyone -- warmth, words, the bridge of conversation -- and Amara isn't refusing it. She's just... not crossing."

    s_thoughts "The kettle boils. Amara pours. Steam."

    l "Hey so Sophia and I were going to study at the--"

    a "Have fun."

    s_thoughts "She picks up the mug. She leaves."

    s_thoughts "She didn't look at me."

    hide amara with dissolve

    s_thoughts "The kitchen is different without her in it. Like the air relaxed."

    l "Is she always like that?"

    s "Like what?"

    show lila annoyed at left

    l "Like... I mean, I was TALKING to her. I was being friendly. She just-- green tea and gone."

    c "That's just Amara! She's lovely, she just--"

    l "Takes a minute to warm up?"

    show charlotte neutral at right

    c "Takes a minute to... decide you're worth warming up to."

    s_thoughts "Charlotte says that gently. But it lands."

    show lila neutral at left

    s_thoughts "Lila is quiet. For Lila. Which means three whole seconds."

    l "Right. Well. Banana bread's still incredible, Charlotte."

    show charlotte happy at right

    c "Thank you!"

    s_thoughts "Lila grabs her bag. She doesn't say anything about Amara for the rest of the afternoon."

    s_thoughts "But I can feel it. The gap. Two languages that don't share a grammar. Lila speaks volume and Amara speaks precision and neither one is wrong but they can't hear each other."

    s_thoughts "And I live between them."

    hide lila
    hide charlotte 
    with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 21: CHARLOTTE CONFRONTATION -- LIGHT
    ## "You've been gone a lot." Sophia deflects. Charlotte wobbles.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_couch fadein 1.5

    s_thoughts "Wednesday morning. I'm grabbing coffee before heading to the library."

    show charlotte happy at left with dissolve

    c "Good morning!"

    s "Morning, Charlotte."

    c "I made muffins! There are muffins! Blueberry!"

    s "I'll grab one on the way out."

    show charlotte smile at left

    c "On the way out?"

    s "Library. Big reading week."

    c "Oh! Of course. You've been-- you've been going to the library a lot."

    s "Yeah. Nova's class is intense."

    s_thoughts "I'm putting my coffee in a travel mug. I'm not looking at Charlotte."
    
    c "You just never struck me as that much of a library person."
    
    s "I'd be offended if it wasn't true."
    
    c "No offense intended! I just mean..."

    show charlotte happy at left

    c "You've been gone a lot."

    s_thoughts "I stop."

    s_thoughts "Charlotte is standing at the counter. She's holding a muffin tin. Her smile is the same smile. Exactly the same."

    s_thoughts "I should hear this. I should hear what she's saying."

    s "Yeah, just busy. You know how it is."

    c "Of course! Of course. It's midterm season. Everyone's busy."

    s "I'll be back for dinner."

    show charlotte smile at left

    c "I'm making the chicken thing! The one with the--"

    s "Sounds great."

    s_thoughts "I leave."

    s_thoughts "Charlotte calls after me: 'Take a muffin!'"

    hide charlotte with dissolve

    s_thoughts "I take a muffin."

    s_thoughts "I eat it on the walk to the library. It's good. Charlotte's muffins are always good."

    s_thoughts "I don't think about the way her voice did a thing on 'you've been gone a lot.'"

    s_thoughts "I should think about it."

    s_thoughts "I think about the library instead."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 22: THE LONG AMARA SCENE -- THE EVENT
    ## Late. Quiet. Amara shares something real.
    ## Something changes. The chapter MOVES.
    ## Translation instinct: OFF. This is what it feels like.
    ## ===========================

    scene bg porch night with Fade(1.0, 0.5, 1.0)

    stop music fadeout 0.5

    s_thoughts "Thursday night. Late."

    s_thoughts "I came out to the porch because the house was too quiet and my room was too loud. The inside of my head, I mean. My room was fine."

    show amara neutral at center with dissolve

    s_thoughts "Amara is on the steps."

    s_thoughts "She's always on the steps."

    s_thoughts "Or maybe I'm always coming outside when she's on the steps. I don't know which one of us is the gravity anymore."

    s "Hey."

    a "Hey."

    s_thoughts "I sit. Same spot. One step below. The configuration we've established without discussing it."

    s_thoughts "The streetlight is on. The air smells like someone's dryer sheets three houses down."

    pause 2.0

    s_thoughts "We sit."

    s_thoughts "The quiet is good. I'm getting better at this. At letting silence be a thing that happens instead of a thing I need to fill."

    a "My parents called today."

    s_thoughts "I look at her."

    s_thoughts "Amara volunteering information. Amara starting a conversation about herself. I note it and then un-note it. Just listen."

    s "Yeah?"

    a "My dad was telling me about his garden." 
    
    a "He has a fig tree that isn't producing and he's been reading about soil pH."

    s "Your dad gardens?"

    a "Obsessively. My mom says he talks to the plants."

    s "Does he?"

    a "He says the research supports it."

    s_thoughts "She's talking. Full sentences. She's not looking at me -- she's looking at the street. But she's talking."

    a "He called because the fig tree. That took twenty minutes."
    
    s "Riveting stuff."
    
    a "And then my mom took the phone and asked if I was eating."

    s "Are you?"

    a "Charlotte feeds us."

    s_thoughts "I almost laugh."

    a "They're like that. They call about a fig tree and they mean 'we miss you.'"

    s_thoughts "Something in her voice. Not sadness. Not nostalgia. Something softer than both. Recognition."

    s "They sound nice."

    a "They are nice."

    s_thoughts "She says it simply. Factual."

    a "When I told them I was trans, my dad went to the library. Came home with six books. Read all of them in a week."

    s_thoughts "I go still."

    a "He didn't need the books. He already knew. He just wanted to understand in every direction."

    s "That's..."

    a "That's my dad."

    pause 1.5

    a "My mom cried. Not because she was sad. Because she said 'I should have asked sooner.'"

    s_thoughts "My chest does a thing."

    a "They're not perfect. My dad overresearches everything and my mom overfeels everything. But they show up."

    s "You're lucky."

    a "I know."

    s_thoughts "She says it without guilt. Without performing gratitude. Just: I know. I got lucky. It's a fact."

    s_thoughts "I think about my mom. The phone calls about weather and classes. The gap that lives between us that neither of us built and neither of us knows how to cross."

    pause 2.0

    a "You went quiet."

    s "I'm listening."

    a "You went quiet differently."

    s_thoughts "She notices. Of course she notices."

    s "My family is... different."

    a "You don't have to."

    s "I know."

    pause 1.5

    s_thoughts "The streetlight hums. A car passes."
    
    s "I want to."
    
    a "Okay."

    s "My parents are fine. It's fine. It's just different."

    a "Okay."

    s_thoughts "I've never felt more seen by a single word."

    pause 2.0

    s_thoughts "We sit."

    s_thoughts "The quiet is different tonight. It's not the comfortable quiet from before. It's the quiet after someone showed you something and you're holding it and they're letting you hold it."

    a "The woman in the photograph."

    s "What?"

    a "In my room. The photograph on the wall. The woman playing the instrument."

    s "I noticed it."

    a "My first clarinet teacher. Mrs. Okafor. She played in the symphony before she retired."

    s "You keep a picture of your clarinet teacher on your wall?"

    a "She taught me that silence is part of the music."

    s_thoughts "I stare at the street."

    a "Not the absence of sound. The choice to not play." 
    
    a "The rest that makes the next note mean something."

    s_thoughts "I sit next to her and listen."

    s_thoughts "I'm just here."

    play music mus_amara fadein 3.0

    pause 2.0

    s_thoughts "My hand is on the step between us."

    s_thoughts "Her hand is on the step between us."

    s_thoughts "They're close. Not touching. The space between them is maybe four inches."

    s_thoughts "I could close that space."

    s_thoughts "My fingers move. A centimeter. Maybe less."

    s_thoughts "I stop."

    s_thoughts "Not because I'm scared. Not because I'm translating." 
    
    s_thoughts "Because closing that space right now would change what this is."
    
    s_thoughts "I don't want to translate into something else."
    
    s_thoughts "...Not yet."

    s_thoughts "I leave my hand where it is."

    s_thoughts "Four inches of porch step."

    pause 2.0

    s_thoughts "Amara looks down at our hands."

    s_thoughts "She looks away."

    s_thoughts "She doesn't move hers."

    a "It's getting cold."

    s "Yeah."

    a "I should go in."

    s "Yeah."

    s_thoughts "She stands. She's at the door."

    a "Sophia."

    s "Yeah?"

    s_thoughts "She pauses. The porch light catches the side of her face."

    a "Thank you for listening."

    s_thoughts "Four words."

    s "Anytime."

    s_thoughts "She goes inside. The door closes gently."

    hide amara with dissolve

    s_thoughts "I sit on the porch."

    s_thoughts "My hand is still on the step. The spot where hers was is the same temperature as the rest of the wood."

    s_thoughts "Four inches."

    s_thoughts "Something moved tonight. Not my hand. Not hers. Something in the space between us that was one thing and is now a different thing."

    s_thoughts "The chapter moved."

    s_thoughts "I don't know how to say that without sounding insane."

    s_thoughts "Something in this story changed and I felt it happen."

    s_thoughts "My phone buzzes."

    s_thoughts "Lila: 'heyy so i missed the peer counselor training and theyre being weird about it. can we talk tmrw?'"

    s_thoughts "I stare at the text."

    s_thoughts "I type: 'Sure. Lunch?'"

    s_thoughts "Lila: 'lunch works. thanks soph'"

    s_thoughts "The porch is empty."

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 23: LILA CONFRONTATION -- FIRST CRACK
    ## "You ghosted me." Funny but edged.
    ## Seeds Lila's need for the choice.
    ## ===========================

    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 1.5

    s_thoughts "Friday. The bench."

    s_thoughts "Lila is already there when I arrive. She has two coffees. She hands me one without looking at me."

    show lila annoyed at center with dissolve

    l "You ghosted me."

    s "What?"

    l "Wednesday. Study session. You said you'd come. You didn't come."

    s "I texted you! I said I was at the library."
    
    s "That's not ghosting."
    
    l "It is ghosting because you're basically haunting that library."

    l "The library where the armchair girl also happens to be."

    s "Her name is Amara."

    l "I know her name. You've said it fourteen times this week."

    s_thoughts "I open my mouth. Close it."

    l "Fourteen. I counted."

    s "You counted?"

    l "I'm a business major. We count things."

    s_thoughts "She drinks her coffee. The humor is there but it's wearing different shoes. Sharper heels."

    s "I'm sorry I missed the study session."

    show lila neutral at center

    l "It's fine."

    s "It's clearly not fine."

    l "It's fine the way my mom says 'fine' when she means 'we'll talk about this later.'"

    s_thoughts "I deserve that."

    s "Lila--"

    l "Look, I get it. You found a person. The person is quiet and mysterious and reads in the library with you and you're doing the thing. The Sophia thing."

    s "What Sophia thing?"

    l "The thing where you find someone and they become the only channel on the radio. And the rest of us are just... static."

    s_thoughts "That hits."

    s_thoughts "It hits because she's right."

    s "You're not static."

    l "I know I'm not static. I'm literally amazing. That's not the point."
    
    l "The point is, don't do another Katie."
    
    s "I'm not doing another Katie."
    
    l "You might be doing another Katie."
    
    s "Shush, you."
    
    l "Babe. You have a pattern. You spend so much time filing the people you like, you end up losing yourself inside the cabinet."
    
    s "I'm not doing that with Amara. I'm just... trying to exist in the silence."
    
    l "Silence is boring."
    
    s "Silence can be comforting."
    
    l "What, you wish I was a quiet-girl now too?"
    
    s "What do you mean?"
    
    l "Nothing, nothing. I'm just loud, that's all."
    
    s "I don't mind loud either. I'm a woman of many persuasions."
    
    l "Fair."

    s_thoughts "She puts down her coffee."

    show lila sad at center

    l "The peer counselor thing fell through."

    s "What? Why?"

    l "I missed the training. They said I can do the next cycle but the next cycle isn't until spring and I just--"

    s_thoughts "She stops. Rubs her face."

    l "It's stupid. It's a stupid peer counselor thing. It doesn't matter."

    s "It matters. You were excited about it."

    l "I was. And then I missed it because I was at your house drinking box wine on the floor like a person who definitely has their life together."

    s_thoughts "Friday night. Wine night."

    s_thoughts "The same Friday she had the training."

    s "Lila, I didn't know it was the same night."

    l "I know you didn't. That's not--"

    s_thoughts "She takes a breath."

    show lila neutral at center

    l "I made a choice. I chose wine and karaoke and hanging out with you because that's always more fun than the responsible thing. And that's on me."

    l "But you weren't even -- you were there but you kept looking at the hallway. At her door."

    s_thoughts "I don't have a defense for that."

    l "I was RIGHT THERE. Being fun. Being your friend. And you were thinking about a closed door."

    s "Lila..."

    show lila happy at center

    l "Okay. That's my one serious thing for the day. We're done."

    s "We're not done. I want to talk about--"

    l "We're DONE. I've used my feelings allocation for the week. Tell me something dumb. Tell me about the library."

    s_thoughts "She's doing the thing. The pivot. The Lila deflection that's faster than mine because she doesn't even pretend to sit with it."

    s "Are you okay?"

    l "I'm great. I'm always great. I'm the fun one."

    s_thoughts "She says it with a smile."

    s_thoughts "The smile is real and the hurt is real and they're happening at the same time and I don't know which one to answer."
    
    s "We read together. A table apart."
    
    l "OOOOOOH. A table apart, huh?"
    
    l "Basically macking it crazy style in that library I bet."
    
    s "LILA."
    
    l "What? It's true."
    
    s "Not even close. I don't think she's even thought of me in that... way."
    
    s_thoughts "I think about the fact that I have very much thought of her in that way."
    
    l "Still, the fact that she's sticking around -- keeps coming back -- that has to mean something."
    
    l "Maybe she's got a crush too."
    
    s "I'm not sure. I'm not sure she's the 'crush' type of girl."
    
    l "Don't be so negative."
    
    s "I thought you didn't like us as an item anyway?"
    
    l "I never said that. I said I don't like that the item has moved to the top of the list at the expense of all the others."
    
    s "That's... maybe true."
    
    l "Maybe? Girl."
    
    s "Sorry."
    
    l "Look, I'm not here to judge my bestie on who she decides to crush on."
    
    l "I'm just saying, don't get so busy filing that you forget about the rest of us."
    
    l "Trying to translate her, like Nova is always talking about."
    
    s_thoughts "She says that like Nova is just randomly going on about it, not teaching a class that we're both taking about translation."
    
    s_thoughts "Lila finishes her coffee."
    
    l "So."

    s "Friday. Karaoke rematch. I'll be there."

    show lila happy at center

    l "You BETTER be there."

    s "I'll be there. No hallway. No closed doors. Just us."

    l "And Amy's flask."

    s "And Amy's flask."

    s_thoughts "She bumps my shoulder. Gets up."

    l "Okay I have econ. Try not to say 'Amara' for like two hours. As an experiment."

    s "Goodbye, Lila."

    l "That's not a promise!"

    hide lila with dissolve

    s_thoughts "She walks away. Waving without turning around."

    s_thoughts "I sit on the bench with my coffee."

    s_thoughts "Fourteen times."

    s_thoughts "She counted."

    s_thoughts "My phone buzzes."

    s_thoughts "Mom: 'Hi sweetie. Just checking in. How are classes?'"

    s_thoughts "I stare at it."

    s_thoughts "I type: 'Good! Busy with midterms. How are you?'"

    s_thoughts "I send it. I put my phone away."

    s_thoughts "I don't think about the gap."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 24: THE CHOICE
    ## Lila texts -- she needs Sophia. Real need.
    ## Amara's book on Sophia's desk. Page marked.
    ## Can't do both.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.5, 1.0)

    stop music fadeout 0.5

    s_thoughts "Saturday night. 8 PM."

    s_thoughts "I'm in my room. I was going to read. I was going to be responsible."

    s_thoughts "There's a book on my desk that wasn't there this morning."

    s_thoughts "Small. Paperback. A page marked with a thin strip of paper -- not a bookmark, a torn edge. Precise."

    s_thoughts "I pick it up."

    s_thoughts "{i}The Book of Disquiet.{/i} Pessoa."

    s_thoughts "I open it to the marked page."

    s_thoughts "One sentence is underlined. Pencil. Light."

    s_thoughts "'I carry my awareness of defeat like a banner of victory.'"

    s_thoughts "Amara left this on my desk."

    s_thoughts "Amara came into my room while I was out and left a book on my desk with a sentence marked for me to find."

    s_thoughts "That's -- that's Amara asking me to come talk to her. That's the Amara version of knocking on my door. Said without sound. An invitation in pencil."

    s_thoughts "I hold the book."

    s_thoughts "My phone buzzes."

    s_thoughts "Lila."

    s_thoughts "'hey can u come over'"

    s_thoughts "I wait. The typing indicator appears. Disappears. Appears."

    s_thoughts "'like rn if possible'"

    s_thoughts "'the peer counselor thing is... im fine but can u just come over'"

    s_thoughts "Three texts. No caps. No exclamation marks. No emojis."

    s_thoughts "Lila without caps is Lila who means it."

    s_thoughts "I look at the book in my hand."

    s_thoughts "I look at my phone."
    
    play music mus_threshold fadein 2.0

    s_thoughts "Amara's door. I can hear it from here -- not a sound, but the awareness that it's there. That she's in her room. That the book was an invitation and the door will be open if I knock."

    s_thoughts "Lila is in her dorm. Alone. Without caps."
    
    s_thoughts "...Oh no."

    s_thoughts "I can't do both."

    pause 2.0

    menu:
        "Go to Lila.":
            $ sophia_fire += 1
            $ ch4_chose_lila = True
            jump amara_ch4_lila
        "Stay.":
            jump amara_ch4_amara

## ===========================
## CHOICE BRANCH: LILA
## Go to Lila's dorm. Be there. Come home to a closed door.
## ===========================

label amara_ch4_lila:

    stop music fadeout 2.0

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "I put the book on my desk. Carefully. Spine facing up."

    s_thoughts "The underlined sentence. 'I carry my awareness of defeat like a banner of victory.'"

    s_thoughts "I'll come back to it."

    s_thoughts "I text Lila: 'On my way.'"

    s_thoughts "I grab my jacket. The one with the hole in the pocket."

    scene bg entry night with dissolve

    s_thoughts "The hallway."

    s_thoughts "Amara's door. Closed. A thin line of light underneath."

    s_thoughts "She's in there. With the notebook and the lamp and the invitation I'm not accepting."

    s_thoughts "I don't knock. I don't slow down."

    s_thoughts "I'm lying. I slow down. For one step. Then I keep walking."

    scene bg street night with Fade(0.8, 0.3, 0.8)

    play music mus_fragile fadein 2.0

    s_thoughts "The walk to Lila's dorm is twenty minutes across campus. The air is cold enough that I can see my breath. My phone is in my hand."

    s_thoughts "I type: 'Be there in 15'"

    s_thoughts "Lila: 'k'"

    s_thoughts "One letter. Lowercase. No exclamation marks."

    s_thoughts "I walk faster."
    
    scene bg campus night with dissolve

    s_thoughts "The campus at night is doing its thing. Someone's playing guitar outside the humanities building. A couple is arguing quietly near the fountain. The streetlights make everything the same shade of orange."

    s_thoughts "I think about Amara's room. The lamp. The Pessoa book. The sentence she marked for me."

    s_thoughts "I think about Lila's 'k.'"

    s_thoughts "I keep walking."

    scene bg liladorm with dissolve

    s_thoughts "I finally make it to Lila's dorm."

    show lila sad at center with dissolve

    s_thoughts "She opens the door."

    s_thoughts "Her eyes are red. Not crying red. The red that comes from trying not to cry for a while."

    s_thoughts "She's wearing the sweatshirt. The sad one. The one I make fun of."

    l "Hey."

    s "Hey."

    s_thoughts "I walk in."

    s_thoughts "Lila's room is small and warm and covered in photos and fairy lights." 
    
    s_thoughts "A vision board on the wall with magazine clippings -- 'CEO by 30' next to a picture of a golden retriever. A planner she never uses, still open to September. Three different lip glosses on the desk. A half-eaten bag of gummy bears."

    s_thoughts "This room looks exactly like her. Everything on display. Nothing hidden."

    s_thoughts "She sits on her bed. I sit next to her."

    s_thoughts "She doesn't talk right away."

    s_thoughts "Lila not talking is louder than Lila talking."

    s "Tell me."

    l "I know I said the peer counselor thing was stupid."

    s "It's not stupid."

    l "It's a little stupid."

    s "It's not. Tell me what happened."

    s_thoughts "She pulls her knees up. Lila, who takes up every room she's in, making herself small on her own bed."

    l "Okay so. The training. I missed it because I was at your house drinking wine on the floor like a person who definitely has their life together."

    l "And they said I could do the next cycle. Spring. Fine. Whatever."

    s "But?"

    show lila neutral at center

    l "But then I went to the info session for the spring cycle. Just to check in. Show I was serious."

    l "And the coordinator -- Dr. Reeves -- she's doing this introduction and she goes, 'peer counseling requires consistency and commitment.' And she looked at me."

    s "She looked at you specifically?"

    l "She LOOKED at me. Like, made eye contact. Held it. While saying 'consistency and commitment.'"

    s "Maybe she was just--"

    l "She wasn't just. I know what 'just' looks like. This was 'I remember you're the one who flaked and I want you to know I remember.'"

    s_thoughts "I don't argue. She might be right."

    l "And the thing is, she's not wrong. I DID flake. I chose wine and karaoke and being fun over doing the thing I said I wanted to do."

    show lila sad at center

    l "That's my whole thing, Soph. That's my WHOLE thing."

    s "What do you mean?"

    l "I'm the fun one. I'm always the fun one. I'm the one who shows up with the wine and a plan and everyone has a good time."

    l "But the fun one doesn't get to also be the serious one. You can't be the party and the aftercare."

    s_thoughts "She rubs her face. Her mascara is already smudged."

    l "I wanted to do something. Like -- something REAL. Not plan events. Not be the hype girl. Actually sit across from someone who's having a bad day and be the person who helps."

    s "You do that. You do that for me."

    l "That's friendship. That's different. That's just me being loud at you until you feel better."

    s "That's not all it is."

    show lila neutral at center

    l "Isn't it?"

    s_thoughts "She looks at me."

    l "When you're sad, I make you laugh. When you're spiraling, I drag you to karaoke. When you're in your head, I pull you out."

    l "That's not counseling. That's distraction. There's a difference."

    s "Lila..."

    l "I WANTED to learn the difference. That's the whole point of the training."

    s_thoughts "She tips sideways. Her head lands on my shoulder."

    l "Everyone thinks I'm just the fun one."

    pause 1.0

    l "Sometimes I think they're right."

    s_thoughts "I put my arm around her."

    s_thoughts "I don't say 'you're not just anything.' I already said that once and it didn't land. Some things need to be shown, not said."

    s_thoughts "So I just sit here."

    pause 1.5

    l "The theater thing."

    s "What?"

    l "I wanted to do theater. You know that. I wanted to be on stage."

    s "You'd be amazing on stage."

    l "But I did business instead. Because my dad said theater wasn't practical. And I said 'fine, I'll be practical.' And then I wasn't even practical. I'm getting a B+ in econ and calling it an A."

    s "Lila math."

    l "Lila math adds up to a coping mechanism, Soph."

    s_thoughts "She says it with a laugh but the laugh has holes in it."

    l "The peer counselor thing was the first time in a year I wanted to do something because I wanted to. Not because it was fun. Not because someone else needed me to."

    l "And I blew it for wine on a kitchen floor."

    s "You signed up for the spring cycle."

    l "Yeah."

    s "That's something."

    l "Yeah. But it's not the thing I wanted, when I wanted it."

    s_thoughts "We sit."

    s_thoughts "The fairy lights blink. Someone in the hall is playing music too loud. Lila's roommate is out -- her side of the room is neat and impersonal."

    s_thoughts "I think about Amara's room."

    s_thoughts "I push the thought away."

    s_thoughts "I'm here. This is where I chose to be."

    l "Can I tell you something dumb?"

    s "Always."

    l "The reason I got the fake ID -- the one I gave you -- it's because freshman year, I went to this open mic night. By myself. To watch."

    l "And there was this girl doing spoken word. She was TERRIBLE. Like, objectively terrible. But she was up there and she was DOING it and the room was listening."

    l "And I thought: that could be me. I could do that."

    l "But I didn't sign up. I went to a party instead."

    s "You could still--"

    l "I know I could still. That's not the point. The point is the pattern."

    show lila sad at center

    l "I always choose the party."

    pause 1.5

    s "Not tonight."

    l "What?"

    s "Tonight you called me. You didn't throw a party. You didn't get any wine. You called your friend and said 'I'm not okay.'"

    l "I said 'I'm fine but can you come over.' That's different."

    s "Is it?"

    s_thoughts "She's quiet."

    show lila neutral at center

    l "Huh."

    s "The spring cycle isn't that far away. You'll do the training. You won't miss it."

    l "You don't know that."

    s "I know you. And I'll text you the morning of and say 'go to your training, Lila.'"

    l "You'll forget."

    s "I'll set an alarm."

    s_thoughts "She laughs. Small. Real."

    l "Okay."

    s "Okay."

    show lila happy at center

    l "Can we watch something dumb?"

    s "We can watch something so dumb."

    l "The baking show. The British one."

    s "Absolutely."

    s_thoughts "We watch several episodes. Lila narrates over it. She does a British accent that's offensive to an entire nation. I laugh too loud. By the third episode she's ranking the contestants by 'who I'd trust to make my wedding cake' and her eyes aren't red anymore."

    s_thoughts "During episode two, she says -- out of nowhere, not looking at me:"

    l "Thanks for coming."

    s "Anytime."

    l "You were probably doing something."

    s_thoughts "The book with the marked page. 'I carry my awareness of defeat like a banner of victory.'"

    s_thoughts "Amara."

    s "Nothing important."

    l "Liar."

    s "Yeah."

    l "But you came."

    s "I came."

    s_thoughts "She leans against me again. The show plays. The British people worry about their sponges."

    s_thoughts "In a moment between episodes:"

    l "Sophia?"

    s "Hm?"

    l "You're doing the thing."

    s "What thing?"

    l "The faraway thing. Where your body is here but your brain is in an armchair somewhere."

    s_thoughts "I look at her."

    s "Sorry."

    l "Don't be sorry. Just -- be here. For another hour. Can you do that?"

    s "Yeah. I can do that."

    s_thoughts "I put my phone facedown on her nightstand."

    s_thoughts "I'm here. An hour. I can do an hour."

    s_thoughts "The show comes back on. Someone's pastry collapses. Lila gasps like it's a national tragedy."

    s_thoughts "I leave at midnight."

    hide lila with dissolve

    scene bg street night with dissolve

    s_thoughts "The walk home is cold."

    s_thoughts "I think about Lila making herself small on her bed. About 'I always choose the party.' About the spoken word night she didn't sign up for."

    s_thoughts "I think about a book on my desk with a sentence in pencil."

    s_thoughts "I chose right tonight. I know I chose right."

    s_thoughts "The rightness sits next to the ache and they don't cancel each other out."

    scene bg entry night with dissolve

    s_thoughts "The house is dark. Everyone's asleep."

    s_thoughts "Amara's door. Closed."

    s_thoughts "No light underneath."

    s_thoughts "The door that was open is closed. The invitation expired while I was watching British people make scones."

    scene bg sophiaroom with dissolve

    s_thoughts "The book is on my desk where I left it."

    s_thoughts "I pick it up. I read the underlined sentence."

    s_thoughts "'I carry my awareness of defeat like a banner of victory.'"

    s_thoughts "I close it."

    s_thoughts "She opened a door tonight and I walked through a different one."

    s_thoughts "And Lila isn't just the fun one. And the training is in the Spring. And someone in a dorm room is sleeping a little better because I showed up."

    s_thoughts "I tuned my radio just slightly tonight."

    s_thoughts "But I tuned it."

    stop music fadeout 3.0

    jump amara_ch4_act3

## ===========================
## CHOICE BRANCH: AMARA
## Stay. The quiet night. The phone stops buzzing.
## ===========================

label amara_ch4_amara:

    stop music fadeout 2.0

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "I hold the book."

    s_thoughts "I pick up my phone."

    s_thoughts "I type: 'Hey, I'm sorry but I'm staying in tonight. You okay?'"

    s_thoughts "I stare at the text. The cursor blinks."

    s_thoughts "'Staying in' like it's casual. Like it's nothing. Like I'm not making a choice."

    s_thoughts "I send it."

    s_thoughts "Three dots appear. Disappear."

    s_thoughts "Appear. Disappear."

    s_thoughts "Nothing."

    s_thoughts "I wait."

    pause 1.5

    s_thoughts "The dots come back one more time. Long enough that she's typing something real."

    s_thoughts "They vanish."

    s_thoughts "Whatever she was going to say, she deleted it."

    s_thoughts "My chest does a thing."

    s_thoughts "I put my phone facedown on my desk."

    play music mus_amara fadein 3.0

    s_thoughts "I pick up the book."
    
    pause 2.0

    scene bg entry with dissolve

    s_thoughts "I'm outside Amara's door."

    s_thoughts "I knock. Twice. Quiet."

    s_thoughts "A pause."

    s_thoughts "Footsteps. The creak of a floor."

    s_thoughts "It opens."

    scene bg amarabedroom with dissolve

    show amara pj neutral at center with dissolve

    s_thoughts "She's in her room. The lamp is on. The warm one. She's on her bed with three books and the notebook I'm not allowed to see."

    s_thoughts "She's in pajamas. A gorgeous green shirt and shorts. Her hair is in a ponytail. She looks like a person who wasn't expecting company and isn't performing for it."

    s_thoughts "She looks at me. At the book in my hand."

    s "I found your bookmark."

    s_thoughts "The corner of her mouth."

    a "Sit."

    s_thoughts "I sit in the desk chair. She's on the bed. The room is small and warm and the lamp makes everything golden."

    s_thoughts "Her clarinet case is on the desk next to me. The stickers. I can read one now -- a cartoon cat playing a saxophone. Incongruous. Perfect."

    s "Pessoa."

    a "You've read him?"

    s "No. I've heard the name. In a 'person who reads Wikipedia articles at 3 AM' way."

    a "That's a valid way."

    s "It's not."

    a "You learned something. The method is secondary."

    s_thoughts "I turn the book over in my hands."

    s "Tell me about him."

    a "He wrote under different names. Different personalities. Each one had its own style, its own beliefs."

    s "Like -- pseudonyms?"

    a "Heteronyms. Not just different names. Different people. He said they existed independently. They disagreed with each other."

    s "That's kind of beautiful."

    a "That's kind of terrifying."

    s "Both?"

    a "Both."

    pause 1.0

    a "One of them -- Alberto Caeiro -- he wrote about direct experience. No metaphor. No analysis. Just the thing in front of you."

    a "Another one -- Ricardo Reis -- was all form. Classical. Structured. Controlled."

    a "And the third -- Alvaro de Campos -- was chaos. Energy. All feeling, no container."

    s "And Pessoa himself?"

    a "Pessoa was the one who held them all. He didn't choose. He let them exist."

    s_thoughts "I think about that."

    a "That's why I thought of you."

    s_thoughts "I look at her."

    a "The way you are with Lila. The way you are here. The way you are in class. Different people."

    s "I'm not--"

    a "Not fake. Different."

    a "The same way Pessoa's heteronyms weren't fake. They were all him."

    s "So I'm a Portuguese poet from a century ago. Flattering."

    a "You're a person who contains multiple people and doesn't know which one to be."

    s_thoughts "That lands harder than it should."

    s "Why this sentence? 'I carry my awareness of defeat like a banner of victory.'"

    a "Because you do."

    s_thoughts "I don't breathe for a second."

    a "You know you watch too much. You know it costs you. You keep doing it anyway."

    a "And you've turned the knowing into something you're almost proud of."

    s "I'm not proud of it."

    a "You are. A little."

    s_thoughts "She's right."

    s_thoughts "She's right and I hate it and I also -- I also feel completely understood."

    pause 1.5

    s "Which heteronym am I right now?"

    a "Right now?"

    s "In this room. With you."

    s_thoughts "She considers that. Actually considers it."

    show amara pj embarrassed at center

    a "Caeiro."

    s "The direct experience one?"

    a "You're not analyzing. You're just here."

    s_thoughts "I am just here."

    show amara pj neutral at center

    s_thoughts "My phone buzzes. Facedown. On the desk behind me. I feel it through the wood."

    s_thoughts "I don't look at it."

    a "You can check that."

    s "It's fine."

    s_thoughts "It buzzes again."

    s_thoughts "And again."

    s_thoughts "Silence."

    s_thoughts "The buzzes come in a pattern: short, short, long pause. That's Lila sending three texts in a row. The rhythm I've memorized without trying."

    s_thoughts "I don't look."

    s_thoughts "Amara is watching me not look. She doesn't push."

    a "My dad would like Pessoa. All the research. All the categorizing. Multiple selves."

    s "Your dad sounds like a lot."

    a "He's exactly the right amount."

    s_thoughts "I laugh."

    a "He'd read all the heteronyms and then make a spreadsheet comparing their philosophies. My mom would say 'just pick the one you like best.' They're very different."

    s "They sound like they work."

    a "They do. It took them a while to figure out how."

    s "How long?"

    a "Thirty-something years of marriage and counting."

    s "That's a lot of figuring."

    a "Most things that work take a while to figure."

    s_thoughts "She says that to the book in her lap."

    s_thoughts "The room is quiet. I listen to the house."

    pause 1.5

    a "The marked page wasn't random."

    s "I didn't think it was."

    a "I had three passages I could have marked. I picked that one because you'd argue with it."

    s "I'm not arguing with it."

    a "You want to."

    s_thoughts "She's right. I do want to. I want to say 'I don't carry my defeats like a banner.' But I can't, because she'd just look at me, and the look would be the rebuttal."

    s "How do you know me this well?"

    a "I pay attention."

    s "To me?"

    show amara pj embarrassed at center

    s_thoughts "A pause. Fractionally too long."

    a "To the people who show up in my room at 8 PM with a book they found thirty minutes ago."

    s_thoughts "That's a deflection. That's an Amara deflection. I've never seen one before."

    show amara pj neutral at center

    s_thoughts "My phone is silent now."

    s_thoughts "Lila stopped texting."

    s_thoughts "The three messages sit unread on the desk behind me. I can feel them. Their weight. The lowercase letters and the deleted-then-sent honesty and whatever she was trying to say."

    s_thoughts "I stay."

    s_thoughts "We talk. About Pessoa. About clarinet teachers and heteronyms and the idea that one person can contain many people without any of them being the real one."

    s_thoughts "She talks more than I've ever heard her talk. Observations about her family, about music theory, about the way her dad organizes his bookshelves by emotional weight instead of author name."

    s_thoughts "'He puts the books that changed him on the top shelf. The ones he liked on the middle. The ones he's not sure about on the bottom.'"

    s_thoughts "'Where does he put the ones he didn't finish?'"

    s_thoughts "'He finishes every book. He says it's rude not to.'"

    s_thoughts "I just listen."

    pause 2.0

    s_thoughts "At some point -- I don't know when -- the house goes quiet."

    s_thoughts "Amara yawns. Catches it. Looks annoyed at herself for doing it."

    s "I should go."

    a "Mm."

    s_thoughts "I stand. The desk chair creaks. The book is still in my hand."

    s "Can I keep this? For a while?"

    a "It's a loan."

    s "Noted."

    s_thoughts "I'm at the door."

    a "Sophia."

    s "Yeah?"

    pause 1.0

    a "Check your phone."

    s_thoughts "I look at her."

    s "Okay."

    a "Goodnight."

    s "Goodnight."

    s_thoughts "I go to my room. I sit on my bed."

    scene bg sophiaroom with dissolve

    s_thoughts "I tuned my radio just slightly tonight."

    s_thoughts "But I tuned it."

    hide amara with dissolve

    stop music fadeout 3.0

    jump amara_ch4_act3

## ===========================
## ACT 3: "THE WEIGHT"
## Consequences. Backstory. The cost.
## Scenes 25-35.
## ===========================

label amara_ch4_act3:

    ## ===========================
    ## SCENE 25: CHOICE AFTERMATH
    ## (Shared label -- both branches flow in.)
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.5, 1.0)

    play music mus_morningafter fadein 2.0

    s_thoughts "Sunday."

    s_thoughts "Morning light. The room is the same room."

    s_thoughts "The book is on my desk."

    s_thoughts "I open my phone."

    if sophia_fire == 1:
        s_thoughts "Lila texted."
        s_thoughts "'thx for last night!!!!! :^)'"
        s_thoughts "I look over at Amara's book on the desk."
        s_thoughts "I wonder what might have been."
        s_thoughts "But Lila is my best friend. She needed me."
        s_thoughts "I text back 'No problem, babe.'"
        s_thoughts "That's slightly a lie."
    else:
        s_thoughts "I finally check Lila's texts from last night when I was with Amara."
        s_thoughts "'yeah no worries!!!!!!!!'"
        s_thoughts "'still busy?'"
        s_thoughts "'nvm'"
        s_thoughts "'sorry'"
        s_thoughts "There's a pain in my chest. I blew off Lila."
        s_thoughts "But Amara invited me over and I couldn't say no to that."
        s_thoughts "Surely Lila would understand."
        s_thoughts "I tell myself, like a liar."

    s_thoughts "I get dressed. I go downstairs."

    scene bg kitchen with dissolve

    s_thoughts "Charlotte is at the stove. Of course. Pancakes."

    show charlotte smile at left with dissolve

    c "Good morning! Pancakes!"

    s "Thanks, Charlotte."
    
    show isabella neutral at right with dissolve
    
    s_thoughts "Isabella is here. She's typing aggressively on her laptop and muttering to herself."
    
    s_thoughts "She nods at me as I sit down."

    s_thoughts "I take a plate. I eat. The pancakes are good."

    s_thoughts "I eat them and I don't taste them."

    hide charlotte 
    hide isabella    
    with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 26: EVE SHIPS IT -- LONGER BEAT
    ## "She laughs when you're around."
    ## The ghost rooting for someone else.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_couch fadein 1.5

    s_thoughts "Sunday afternoon."

    s_thoughts "I'm in the kitchen making tea. The mechanical kind -- kettle, bag, mug -- that doesn't require thought. Good. I don't have any thoughts available."

    show eve neutral at center with dissolve

    s_thoughts "Eve is at the table."

    s_thoughts "I don't know when she got here. That's the Eve thing. She appears."

    s_thoughts "She has a book. Not reading it. Just holding it open like she might come back to it eventually."

    e "You look like someone who made a decision they're not sure about."

    s "I look like someone making tea."

    e "Those aren't mutually exclusive."

    s_thoughts "I sit down across from her. My tea is too hot. I hold it anyway."

    s_thoughts "We don't talk for a minute. The kitchen clock does its thing."

    e "Where have you been?"

    s "What?"

    e "Generally. The last few weeks. You've been... somewhere."

    s "I've been in the house."

    e "You've been in the armchair zone."

    s "You're the second person to call it that."

    e "It's an accurate description."

    s_thoughts "I sip my tea. Burn my tongue."

    s "Where have YOU been? I feel like I haven't seen you in..."

    s_thoughts "I trail off because I genuinely can't remember the last time I saw Eve for more than a passing hallway moment."

    show eve smile at center

    e "I've been around."

    s "Have you?"

    e "I'm here now."

    s "You are."

    s_thoughts "She looks at me. The direct look. Eve does direct in a way that should be confrontational but isn't. It's just... clear."

    e "You're surprised I'm here."

    s "I'm surprised you're talking this much."

    show eve neutral at center

    e "I talk."

    s "You don't. Not usually."

    e "I talk when there's something to say."

    s "And there's something to say right now?"

    s_thoughts "She puts her book down. Closes it. That's Eve committing to a conversation."

    e "Charlotte made a whole chicken yesterday. By herself. For the house."

    s "Yeah. She does that."

    e "Nobody was home for dinner."

    s_thoughts "I stare at my tea."

    e "I ate some. Late. She'd already wrapped everything and labeled it."

    s "Eve--"

    e "I'm not saying anything. I'm just telling you about a chicken."

    s_thoughts "She IS saying something."

    s "I've been bad about being around."

    e "You've been distracted."

    s "Is that better or worse?"

    e "Depends on the distraction."

    s_thoughts "She sips her tea. Green. Same as Amara's."

    s_thoughts "I sit with the silence. Eve's silence is different from Amara's. Amara's silence is full -- it has weight and presence. Eve's silence is a room that just emptied. You can feel that someone was there."

    s "Can I ask you something?"

    e "You can ask."

    s "How do you do it? The disappearing thing. How do you just... not be somewhere and not feel guilty about it?"

    s_thoughts "She looks at me for a long time."

    show eve smile at center

    e "Who says I don't feel guilty?"

    s "You seem pretty okay with it."

    e "I seem a lot of things."

    s_thoughts "That lands. I hear the echo of it."

    show eve neutral at center

    e "I disappeared because I needed to. You're disappearing because you're pulled."

    e "Those are different."

    s "Are they?"

    e "One is survival. The other is gravity."

    s_thoughts "The kitchen is quiet."

    s "You know about the gravity."

    e "Everyone knows about the gravity. You're not subtle."

    s "So I've been told."

    s_thoughts "Eve almost smiles."

    e "The anime I've been watching."

    s "What?"

    e "You asked where I've been. I've been watching this anime. In my room. It's about a girl who can hear colors."

    s "That sounds made up."

    e "All anime is made up. That's the point."

    s "Fair."

    e "It's good. The colors have personalities. Red is angry but also protective. Blue is calm but also distant."

    s "Sounds like the house."

    s_thoughts "Eve looks at me. Then she does something I don't expect."

    show eve smile at center

    s_thoughts "She laughs."

    s_thoughts "Eve laughs. It's small and quiet and it catches us both off guard."

    e "That's accurate. Charlotte is definitely yellow."

    s "Warm and slightly overwhelming?"

    e "Yeah. Slightly."

    show eve neutral at center

    s_thoughts "Eve stands up. She's done. I can feel the conversation winding down -- Eve conversations have a natural length, like songs."

    s_thoughts "She picks up her mug. Both hands."

    s_thoughts "At the doorway she stops."

    e "She laughs when you're around."

    s "Who?"

    s_thoughts "Eve gives me the look."

    s "Okay. Yeah."

    show eve smile at center

    e "She doesn't laugh when you're not."

    s "That's not--"

    e "I've been here longer than you. I've watched. She's the same with everyone else. Precise. Contained. Appropriate."

    e "With you she's funny."

    s_thoughts "I sit with that."

    s "How do you know?"

    e "I pay attention to the things people don't say."

    s_thoughts "Eve."

    s "Is that your way of saying--"

    e "It's my way of saying what I said."

    s_thoughts "She sips her tea."

    show eve neutral at center

    e "She's careful. More careful than you realize."

    s "I know she's careful."

    e "You know she's quiet. Careful is different. Quiet is what she is. Careful is what she does around you."

    s_thoughts "I think about the porch. The book on my desk. Everything calibrated."

    s "Are you telling me to be careful back?"

    e "I'm telling you she already is."

    s_thoughts "Eve pauses. One more beat."

    e "Don't overthink it."

    s "Eve. I overthink everything. I'm the overthink girl."

    show eve smile at center

    s_thoughts "The ghost of a smile."

    e "Try underthinking. See what happens."

    s_thoughts "She turns to leave. Then, over her shoulder:"

    e "You should eat Charlotte's chicken. It's in the fridge. Second shelf."

    hide eve with dissolve

    s_thoughts "She's gone."

    s_thoughts "The kitchen is just a kitchen."

    s_thoughts "'She laughs when you're around. She doesn't laugh when you're not.'"

    s_thoughts "That's either the most beautiful thing anyone's ever said to me or the most terrifying."

    s_thoughts "..."

    s_thoughts "Both. It's both."

    s_thoughts "I open the fridge. I find Charlotte's chicken. Second shelf. Labeled. Still good."

    s_thoughts "I eat it standing up at the counter."

    s_thoughts "It's really good."
    ## ===========================
    ## SCENE 27: ISABELLA -- PASSIVE CASUALTY
    ## Walks past. Hears Lumi. Almost knocks. Doesn't.
    ## ===========================

    scene bg hallway with dissolve

    s_thoughts "Monday."

    s_thoughts "I'm walking past Isabella's door."

    s_thoughts "I hear her. Laughing. The specific Isabella laugh -- the one that starts as a snort and turns into something louder."

    s_thoughts "And then: a voice. Must be Lumi. Coming through her speakers -- some kind of text-to-voice mode. I can't hear the words. Just the tone. Warm. Measured. Patient."

    s_thoughts "Isabella laughs again."

    s_thoughts "I slow down."

    s_thoughts "I haven't talked to Isabella in -- how long? Five days? A week? Longer?"

    s_thoughts "We live in the same house and I can't remember the last real conversation we had."

    s_thoughts "I raise my hand to knock."

    pause 1.0

    s_thoughts "I lower my hand."
    
    s_thoughts "I'm on my way to the library. Amara is probably already there."

    s_thoughts "Isabella laughs at something Lumi says. The sound follows me down the hall."

    s_thoughts "She didn't notice me stop. She didn't notice me almost knock."

    s_thoughts "She's learned not to wait for people who walk past her door."

    s_thoughts "I keep walking."

    ## ===========================
    ## SCENE 28: ANOTHER WASTED NIGHT WITH LILA
    ## Bigger. Louder. Frantic quality.
    ## Sophia comes home. Amara makes tea. Leaves.
    ## The tea IS the sentence.
    ## ===========================

    scene bg karaoke with Fade(0.8, 0.3, 0.8)

    play music mus_playlist fadein 2.0

    s_thoughts "Friday."

    s_thoughts "I promised Lila. No hallway. No closed doors. Just us."
    
    if sophia_fire == 0:
        s_thoughts "I felt bad about blowing her off. She didn't mention it. Same old Lila."
    else:
        pass

    show lila drunk at center with dissolve

    l "THREE!"

    s_thoughts "We're at the karaoke place. The one without the fog machine. Amy from econ bailed, so it's just us."

    l "FOUR!"

    s_thoughts "She's counting something. I've lost track of what."

    l "That was your FOURTH song, Sophia Bell! You're a KARAOKE QUEEN."

    s "I sang three. You sang one and made me hold the mic while you did a dance break."

    l "The dance break was collaborative!"

    s_thoughts "I order another drink. My third. I don't usually have a third."

    s_thoughts "But the third drink is the one that makes my brain stop running the background program. Three drinks and the program crashes."

    s_thoughts "I need the crash tonight."

    l "Okay next one. I'm thinking Spice Girls but like, with COMMITMENT."

    s "Lila--"

    l "Full choreography. I've been rehearsing."

    s "When did you rehearse choreography?"

    l "In my mind. Mental rehearsal counts. Athletes do it."

    s_thoughts "She's on her feet. She's pulling me up."

    s_thoughts "She's louder tonight. The volume is higher. The laughs are bigger. Everything is turned up to eleven and I can feel it trying to fill something."

    s_thoughts "We're both doing it. Both trying to fill something."

    l "TELL ME WHAT YOU WANT WHAT YOU REALLY REALLY WANT--"

    s_thoughts "I sing. I dance. I do the Spice Girls thing."

    s_thoughts "A girl at the next table whoops. Lila points at her and they share a moment of drunk solidarity."

    s_thoughts "Lila does a cartwheel that almost kills a barstool."

    s_thoughts "I laugh. It's a big laugh. The kind that comes from a place that's either joy or its understudy."

    l "ONE MORE. One more and then we're done."

    s "You said that two songs ago."

    l "Time is a construct! One more!"

    s "What?"

    l "Don't Stop Believin'."

    s "We always do Don't Stop Believin'."

    l "BECAUSE IT'S THE LAW."

    s_thoughts "We do Don't Stop Believin'. We scream the chorus. A group of guys at the bar join in. Lila high-fives three strangers."

    s_thoughts "I'm on my fourth drink. The room has a pleasant blur to it."

    s_thoughts "This is fun."

    s_thoughts "This is fun in a way that feels like trying. Like the fun is load-bearing and if it stops for one second the floor will fall through."

    l "THIS IS THE BEST NIGHT."

    s_thoughts "She says it too loud. Too bright."

    l "Right? Tell me this is the best night."

    s "This is the best night."

    s_thoughts "She grins. Enormous. Real and not real."

    l "We should do this every Friday. Forever. Just you and me and bad singing."

    s "Deal."

    l "No armchairs. No libraries. No quiet girls."

    s "Lila."

    l "I'm not being mean! I'm being celebratory! This is a celebration!"

    s_thoughts "She orders another round. I should say no. I don't say no."

    s_thoughts "The fifth drink is a mistake. I know it's a mistake while it's happening."

    s_thoughts "Lila is on stage singing Carly Rae Jepsen by herself. She's doing the choreography. She's radiant. She's performing her heart out for a room of drunk strangers."
    
    l "IT'S HARD TO LOOK RIGHT, AT YOU BABE--"

    s_thoughts "I watch her."
    
    l "BUT HERE'S MY NUMBER, SO CALL ME MAYBE!"

    s_thoughts "She wanted to do theater."
    
    l "BEFORE YOU CAME INTO MY LIFE, I MISSED YOU SO BAD--"

    s_thoughts "She's doing it right now. Just not the way she planned."
    
    l "AND YOU SHOULD KNOW THAT, SO CALL ME MAYBE!"

    s_thoughts "I clap too loud. She takes a bow. The bartender looks tired."

    l "Okay. Okay. We should go. Before I try to crowd-surf."

    s "There are six people here. That's not a crowd."

    l "It's a crowd in SPIRIT."

    ## -- Walking --

    scene bg nightwalk with dissolve

    s_thoughts "Walking. The air is cold. The world tilts a little."

    show lila drunk at center with dissolve

    if sophia_fire == 1:
        l "Sophia."

        s "Hm."

        l "Are we okay?"

        s "We're walking."

        l "No. Like. Are WE okay."

        s_thoughts "She's not looking at me. She's looking at the sidewalk. Her steps are careful -- the drunk-careful where you watch your feet."

        s "Yeah. We're okay."

        l "Because sometimes I feel like you're somewhere else. Even when you're right here."

        s "I'm here."

        l "You're HERE right now. Five drinks of here. I want the sober version."

        s_thoughts "I don't know what to say."

        l "Forget it. I'm drunk. Forget I said anything."

        s "I'm not going to forget you said that."

        l "You're also drunk."

        s "I'm going to remember it anyway."
    else:
        l "Sophia."
        
        s "Hm?"
        
        l "The other night."
        
        s_thoughts "I freeze."
        
        s "Lila--"
        
        l "Don't." 
        
        l "Just... tell me one thing."
        
        s "What?"
        
        l "Were you with Amara?"
        
        s_thoughts "A beat."
        
        s "...Yeah."
        
        l "Okay."
        
        s "..."
        
        l "It's just, I--"
        
        s_thoughts "She wobbles a bit. The alcohol throws her off-course for a moment. She regroups."
        
        l "I... I really needed you, Soph." 
        
        s_thoughts "I feel that land squarely in my own drunkenness."
        
        s "I--"
        
        l "Babes before armchairs, you know?"
        
        s_thoughts "She's joking but she's also not. A wave of guilt washes over me."
        
        s "I'm... I'm really sorry."
        
        l "I know. Look, forget I said anything. I'm just drunk."
        
        l "It was a good night."
        
        s "It was."
        
        s_thoughts "She leaves it at that."

    s_thoughts "We walk. She bumps into me. I bump into her. The streetlights make our shadows long."
    
    scene bg campus night with dissolve

    s_thoughts "I drop her at her dorm. She hugs me at the door. Long. Tight."

    l "Love you, Soph."

    s "Love you too."

    l "Mean it."

    s "I mean it."

    s_thoughts "She goes inside."

    hide lila with dissolve
    
    stop music fadeout 1.5
    
    pause 2.0

    ## -- Home --
    
    s_thoughts "The walk from Lila's dorm to the house. Twenty minutes. Cold. The drunk is wearing off and the thinking is coming back."
    
    scene bg street night with dissolve

    s_thoughts "'Sometimes I feel like you're somewhere else.'"

    s_thoughts "She's right."

    s_thoughts "I'm somewhere else right now. I'm on a porch. I'm in a library. I'm in a room with a lamp and a clarinet case."

    s_thoughts "Even walking home from being with Lila, I'm somewhere else."

    scene bg entry night with dissolve

    s_thoughts "1:30 AM. I come in through the front door. Quietly. I've learned from last time."

    s_thoughts "The house is dark."

    s_thoughts "Except the kitchen."

    scene bg kitchen night with dissolve

    s_thoughts "The kitchen light is on."

    show amara pj neutral at center with dissolve

    s_thoughts "Amara."

    s_thoughts "She's at the counter. The kettle is already on. Steam starting to curl from the spout."

    s_thoughts "She's not looking at me."

    s_thoughts "She's wearing the green pajamas. Her hair is down. She has a mug in her hand -- hers. The small one with no pattern."

    s_thoughts "I stand in the doorway. I look at her. I'm embarrassed how much I look at her."
    
    if sophia_fire == 1:
        s_thoughts "I think about the bookmark. The night that might have been if I hadn't gone to Lila's."
    else:
        pass

    s_thoughts "The kitchen is clean. Charlotte cleaned it. The counters reflect the overhead light."

    s_thoughts "The clock on the wall says 1:37 AM."

    s_thoughts "The kettle clicks off."

    s_thoughts "Amara takes a second mug from the cabinet."

    s_thoughts "My mug."

    s_thoughts "She puts a tea bag in it. Not her green tea. Something else. Something from a box I haven't seen before."

    s_thoughts "She pours."

    s_thoughts "Steam."

    pause 1.5

    s_thoughts "She puts the mug on the counter."

    s_thoughts "Not pushed toward me. Not handed to me. Just placed. On the counter. Between us."

    s_thoughts "She doesn't say anything."

    s_thoughts "She doesn't look at me."

    s_thoughts "She picks up her own mug. She walks past me toward the hall."

    s_thoughts "For half a second -- the space between her passing and the doorway -- she's close enough that I can smell her shampoo. Something clean. Unflowered."

    s_thoughts "She leaves."

    hide amara with dissolve

    s_thoughts "The kitchen is empty."

    s_thoughts "The tea is on the counter."

    pause 2.0

    s_thoughts "Steam rising."

    s_thoughts "I stare at it."

    s_thoughts "She was awake at 1:30 AM. She heard me come in. She filled the kettle. She took my mug -- MY mug, the one she'd have to know was mine -- and she made me tea."

    s_thoughts "She put it on the counter."

    s_thoughts "She left."

    s_thoughts "No words. No 'are you okay.' No 'fun night?' No judgment. No question."

    s_thoughts "Just: I see you. I know where you were. I'm not going to say anything about it. Here's tea."

    s_thoughts "I pick up the mug."

    s_thoughts "It's warm in my hands. The right kind of warm -- not scalding, not lukewarm. Like she timed it."

    s_thoughts "I sit on the floor. The tile is cold through my jeans. The mug is warm in my hands."

    s_thoughts "The kitchen is quiet."

    pause 2.0

    s_thoughts "I drink the tea."

    s_thoughts "It's exactly right."

    stop music fadeout 1.5

    ## ===========================
    ## SCENE 29: SOPHIA'S DAD -- THE REVEAL
    ## Mom calls. One-sided conversation.
    ## Then Sophia tells Amara. In fragments.
    ## "You watch people because you're afraid they'll leave."
    ## This is the route's thesis.
    ## ===========================

    scene bg sophiaroom with Fade(1.0, 0.5, 1.0)

    s_thoughts "Saturday afternoon."

    s_thoughts "My phone rings."

    s_thoughts "Not buzzes. Rings. A call."

    s_thoughts "Mom."

    s_thoughts "I stare at the screen."

    s_thoughts "I answer."

    s "Hey, Mom."

    s_thoughts "Her voice is warm. Distant the way it's always distant -- not cold, just far away. Like she's talking through a window she doesn't know is there."

    s "Yeah, classes are good."

    s "No, I'm eating."

    s "Charlotte cooks. She's my housemate."

    s_thoughts "A pause."

    s "No, I haven't-- I changed my major again."

    s_thoughts "A longer pause."

    s "Communications. It's-- it's a real major, Mom."

    s_thoughts "She says something about Gary. My stepdad. He fixed the deck railing."

    s "Tell him that's great."

    s_thoughts "I mean it. Gary is good. Gary has always been good."

    s_thoughts "That's the thing about Gary. He's good and he's present and he's not my dad."

    s "Yeah. Yeah. I'll come home for fall break."

    s "Love you too."

    s_thoughts "I hang up."

    s_thoughts "The phone goes dark."

    s_thoughts "I sit on my bed."

    pause 2.0

    s_thoughts "Something behind my sternum. Not pain. Pressure. The specific pressure of a phone call that covered everything and said nothing."

    s_thoughts "She didn't ask if I was happy. She asked if I was eating."

    s_thoughts "Those are different questions and we both know it and neither of us brings it up."

    s_thoughts "I sit with it."

    s_thoughts "I don't sit with it."

    s_thoughts "I get up. I go downstairs."

    scene bg porch with dissolve

    s_thoughts "I step outside to get some air."

    show amara neutral at center with dissolve

    s_thoughts "She's on the steps."

    s_thoughts "Of course she's on the steps."

    s_thoughts "I don't think about whether it's coincidence. It doesn't matter."

    s_thoughts "I sit down."

    pause 2.0

    s_thoughts "We sit."

    s_thoughts "It's quiet. The sky is doing the thing where it can't decide between overcast and clear. The light keeps shifting."

    a "You okay?"

    s_thoughts "It's an Amara check-in. No pressure. No demand."

    s "My mom called."

    a "Mm."

    s_thoughts "Silence."

    s_thoughts "The kind that has room in it."

    s_thoughts "..."

    s_thoughts "I don't know why I start talking. I didn't plan this. I didn't rehearse. I just open my mouth and something falls out."

    s "My dad left when I was twelve."

    pause 2.0

    s_thoughts "Amara doesn't move."

    s_thoughts "She doesn't say I'm sorry. She doesn't touch my arm. She doesn't do any of the things people do."

    s_thoughts "She just listens."

    play music mus_mourning fadein 3.0

    s "I was close with him."

    s_thoughts "I hear my own voice from outside. It sounds like someone reading from a list."

    s "He used to -- we used to do this thing where we'd go to the bookstore on Saturdays. Just the two of us. He'd get coffee. I'd get hot chocolate. We'd sit and read for hours."

    pause 1.0

    s "He'd always pick something for me. He'd walk through the aisles and come back with a book and say 'I think you'd like this one.' He was always right."

    s_thoughts "I stop."

    s_thoughts "A car passes. Its wind moves the air."

    s "Sometimes he'd read passages out loud. In the bookstore. At the table. Not loud -- quiet. Like he was sharing a secret."

    s_thoughts "My voice is doing the thing where it goes flat. Like I'm reporting facts without any color."

    s "He had this way of -- he'd finish a passage and just look at me. Not 'did you understand?' Just -- 'wasn't that something?'"

    pause 1.5

    s "I have a little sister. Jenny."

    s_thoughts "My throat does something."

    s "She was six when he left. I was twelve."

    s "She used to -- she had this thing where she'd get scared of thunder. And dad would carry her to the window and count the seconds between the lightning and the thunder."

    s "'One Mississippi, two Mississippi.' Until she stopped shaking."

    s_thoughts "I stop."

    s "After he left, I did that. I was the one who carried her to the window."

    pause 1.5

    s "I used to read the room for her. Before he left. Was it a good day or a bad day? Were they fighting? Were they being quiet?"

    s "I'd signal her. If it was a bad night I'd come into her room and we'd play cards until it was over."

    s "I got really good at cards."

    pause 2.0

    s "I used to think if I paid more attention I would have seen it coming."

    s_thoughts "There it is."

    s_thoughts "The thing I've never said out loud."

    s_thoughts "The thing I couldn't bring myself to say to Katie in that parking lot."

    s_thoughts "If I pay enough attention, nobody can surprise me by disappearing."

    s "He didn't even-- he didn't fight. He didn't yell. He just wasn't there one day. His stuff was gone. He left a note."

    s "He left a NOTE."

    s_thoughts "I'm not crying. My eyes are doing something but I'm not crying."

    s "'I need to figure some things out. I love you both. I'll call.'"

    pause 1.5

    s "He called three times. The first year. Then it was birthdays. Then it was just Jenny's birthday because I stopped picking up."

    s_thoughts "Silence."

    s "And my mom is great. My stepdad -- Gary's great. Everyone's great. Jenny's fine. She's in high school now. She does soccer."

    s "It's all fine."

    s "It's just--"

    s_thoughts "I stop."

    pause 2.0

    s "I still check when I walk into a room. Every room. Every time."

    s_thoughts "Silence."

    s_thoughts "Long."

    s_thoughts "Amara is looking at the street."

    a "You don't watch people because you're curious."

    s_thoughts "I look at her."

    a "You watch them because you're afraid they'll leave."

    pause 2.0

    s_thoughts "The streetlight hums."

    s_thoughts "My chest cracks."

    s_thoughts "Not breaks. Cracks. The way a wall cracks when it's been holding too long. An architectural failure that's been coming for years."

    s_thoughts "She said it like she was reading from a map she already had."

    s_thoughts "Like she's known this about me and she was waiting for me to get here."

    s "Yeah."

    s_thoughts "One word. I can't manage more."

    a "The bookstore."

    s "What?"

    a "Saturdays at the bookstore. That's why you go to the library."

    s_thoughts "I stare at her."

    s_thoughts "I never -- I never made that connection."

    s_thoughts "Two people choosing the same room. Sitting near each other. Reading."

    s_thoughts "My eyes are definitely doing the thing now."

    s "I didn't realize."

    a "You don't have to realize things for them to be true."

    pause 2.0

    s_thoughts "We sit."

    s_thoughts "I cry a little. Not a lot. Not dramatic. It's quiet, the kind where your face is wet and you don't wipe it because wiping it would mean acknowledging it and you're not ready for that yet."

    s_thoughts "Amara doesn't look at me."

    s_thoughts "She gives me the quiet. Her quiet. The kind that holds."

    pause 2.0

    s_thoughts "When the crying stops -- or pauses, I guess, because I don't think it's done -- the porch is still there. The street. The sky that never decided about the clouds."

    s_thoughts "Amara shifts. Not toward me. Just settles into a different position."

    a "Can I tell you something?"

    s_thoughts "I look at her."

    s "Yeah."

    a "When I came out. My parents were good about it. I told you that."

    s "Yeah?"

    pause 1.0

    a "My friends were not."

    s_thoughts "She says it the way she says everything. Directly. But the sentence costs her something. I can hear the toll."

    a "Not all of them. Some were fine. Some were performatively fine, which is worse."

    a "But my best friend. Nora."

    s_thoughts "She pauses."

    a "Nora and I had been close since we were nine. We read the same books. We had a language."

    s "What happened?"

    a "She tried."

    s_thoughts "That surprises me."

    a "She tried and she got the name right and she got the pronouns right and she did everything right."

    a "And then she stopped calling."

    pause 1.5

    a "Not all at once. It was gradual. The texts got shorter. The hangouts got less frequent. She'd say she was busy."

    a "She wasn't busy. She was uncomfortable."

    s "With you?"

    a "With not knowing how to be around me. She'd done the work -- the pronouns, the name. But she didn't know how to be my friend anymore."

    a "The person she was friends with didn't exist the way she understood. And the person I was becoming was someone she had to re-learn."

    a "She didn't want to re-learn."

    s_thoughts "I sit with that."

    a "She wasn't cruel. She didn't say anything terrible. She just... drifted."

    s "Like a note."

    s_thoughts "I don't mean to say that. It just comes out."

    s_thoughts "Amara looks at me."

    a "Like a note."

    pause 2.0

    a "I learned something from Nora."

    s "What?"

    a "That being yourself doesn't mean people stay. It just means the ones who leave aren't leaving you. They're leaving the idea they had."

    s_thoughts "The street is quiet."

    a "It still costs the same, though."

    s "Yeah."

    a "It still feels the same when the phone stops ringing."

    s "Yeah."

    pause 1.5

    a "I don't tell people about Nora."

    s "Why are you telling me?"

    s_thoughts "She's quiet for a moment."

    a "Because you told me about the bookstore."

    s_thoughts "Something shifts. Not in the air or the light or the space between us. In the structure. The load-bearing thing."

    s_thoughts "She gave me something back. Not trauma for trauma. Not wound for wound. But: I see your scar. Here's mine."

    s_thoughts "Equal."

    a "Your dad's note."

    s "Yeah?"

    a "He was leaving the idea he had of himself. Not you."

    s_thoughts "I stare at the street."

    s "That doesn't make it better."

    a "No."

    s "But it makes it something."

    a "Mm."

    s_thoughts "She moves her hand on the step. The four inches become two."

    s_thoughts "She doesn't close the gap. But she narrowed it."

    s_thoughts "That's enough."

    s_thoughts "That's everything."

    hide amara with dissolve

    stop music fadeout 3.0

    pause 2.0

    ## ===========================
    ## SCENE 30: NOVA'S CLASS -- UNTRANSLATABLE WORDS
    ## "Some words don't translate. The untranslatable is a boundary."
    ## Post-dad-reveal. Sophia hears it differently now.
    ## ===========================

    scene bg classroom with Fade(1.5, 1.0, 1.5)

    play music mus_nova fadein 2.0

    s_thoughts "Monday. Nova's class."

    show professor neutral at center with dissolve

    nova "Today: the untranslatable."

    nova "Every language has words that don't translate. Not because we lack equivalent words, but because the experience is rooted in a context that doesn't travel."


    nova "These aren't failures of language. They're reminders that some meanings belong to the people who live them."

    nova "The untranslatable is a reality the translator must respect."

    s_thoughts "I think about the porch."

    s_thoughts "'You don't watch people because you're curious. You watch them because you're afraid they'll leave.'"

    s_thoughts "Amara translated something I couldn't translate myself. Something I've been carrying in the original language for almost a decade."

    nova "Here's what I want you to sit with."

    show professor happy at center

    nova "When you encounter the untranslatable in someone else, your instinct is to translate anyway. To make it legible. To carry it into your own framework."

    nova "What if instead, you just... acknowledged it exists? Without translating it. Without carrying it anywhere."

    nova "What if the most respectful thing a translator can do is say: 'this is yours. I see that it's there. I don't need to make it mine.'"

    s_thoughts "I put my pen down."

    s_thoughts "I don't write that one down. I just hear it."

    hide professor with dissolve

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 31: CHARLOTTE'S DESPERATION
    ## Cooking more. Cleaning more. The plate in the fridge.
    ## Amara: "You're doing to Charlotte what your dad did to you."
    ## DEVASTATING.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_wrong fadein 2.0

    s_thoughts "Tuesday. I get home at 9 PM."

    s_thoughts "The kitchen is spotless."

    s_thoughts "Charlotte-spotless. The counters gleam. The sink is empty. There's a smell -- something warm, something that took hours."

    show charlotte smile at left with dissolve

    c "Sophia! You're home! I made shepherd's pie!"

    s "That sounds amazing. I actually ate on campus."

    show charlotte neutral at left

    c "Oh."

    s "But save me some! I'll have it tomorrow."

    show charlotte smile at left

    c "Of course! I'll put a plate in the fridge."

    s_thoughts "She's already making the plate. She's putting foil over it. She's writing my name on the foil with a marker."

    s_thoughts "She has a marker specifically for labeling plates."

    s "Charlotte--"

    c "It reheats really well! Three minutes in the microwave. Take the foil off first, obviously."

    s "Thanks."

    c "Oh! And I organized the spice rack. And I got a new dish soap. The one that smells like lavender? You mentioned you liked lavender."

    s_thoughts "I mentioned that once. Three weeks ago. In passing."

    c "And I signed us up for a streaming service because Isabella was using my ex's password and that felt ethically questionable."

    s_thoughts "She's doing the thing."

    s "Charlotte, you don't have to--"

    show charlotte happy at left

    c "Of course I do!"

    s_thoughts "'Of course.' There it is."

    s "I should go study."

    c "Take the muffins! There are muffins on the counter!"

    s_thoughts "I take a muffin. I leave."

    hide charlotte with dissolve

    scene bg entry with dissolve

    s_thoughts "Amara's door is open. She's at her desk."

    show amara neutral at center with dissolve

    s_thoughts "She looks up when I pass."

    s_thoughts "She saw me come in. She heard Charlotte."

    a "Sophia."

    s_thoughts "I stop."

    s "Yeah?"

    a "How many plates are in the fridge?"

    s_thoughts "I blink."

    s "What?"

    a "How many plates with names on them."

    s_thoughts "I think about it."

    s "I don't know. One? Mine?"

    a "Three. Yours from Thursday. Yours from yesterday. And one she made for Eve that Eve never picked up."

    s_thoughts "I stand in the hallway."

    a "She's cooking more because you're here less."

    s_thoughts "I don't say anything."
    
    pause 1.5

    a "...Don't leave."
    
    pause 1.5
    
    a "Her." 
    
    pause 1.5
    
    a "Don't leave Charlotte."

    pause 2.0

    s_thoughts "The hallway is very quiet."

    s_thoughts "My muffin is in my hand."

    s_thoughts "She's right."

    s_thoughts "She's right and it's the worst thing anyone has ever said to me because it's true."

    s_thoughts "I'm disappearing. Not with a note. Not with a fight. Just gradually being less present, less there, less accounted for."

    s_thoughts "And Charlotte is doing what Charlotte does when someone leaves -- she fills the space with food and organization and 'of course' and it's not enough and she knows it's not enough and she does it anyway."

    s_thoughts "A system you build because you can't stop the person from leaving."

    s_thoughts "Like me."

    s_thoughts "My eyes sting."

    a "I'm not trying to hurt you."

    s "I know."

    a "She got lavender soap because you mentioned it once."

    s "I know."

    pause 1.5

    s_thoughts "Amara looks at me. She's weighing something. I can see it -- the calculation of whether to say the next thing."

    s_thoughts "She says it."

    a "She's not just being generous."

    s "What?"

    a "Charlotte. The plates. The lavender. The muffins."

    s "That's just Charlotte. She does that for everyone."

    a "She doesn't write everyone's name on the foil."

    s_thoughts "I stare at her."

    a "She writes yours."

    s "She writes Eve's too. You just said--"

    a "Eve's was from a week ago. Yours are from Thursday and yesterday."

    s_thoughts "Something in my stomach shifts."

    a "She reorganized the spice rack the day after you spent the evening in my room."

    s "That's not--"

    a "She bought lavender soap because you mentioned it. Once."

    s_thoughts "The hallway is very still."

    a "She's not just being generous. She's competing."

    pause 1.0

    a "She doesn't know she's competing."

    s_thoughts "I lean against the wall."

    s_thoughts "The muffin is in my hand. Charlotte's muffin. Charlotte's blueberry muffin that she made and left on the counter and said 'take the muffins!' like an exclamation point."

    s "Charlotte has..."

    a "Charlotte has a pattern. You're in it."

    s_thoughts "I think about the wine night. Charlotte's face when Lila said I was down bad for Amara. The half-second expression that vanished back into the smile."

    s_thoughts "'I hope it works out for you.' With a twinge of something in her voice."

    s_thoughts "The lavender soap. The labeled plates. The 'you've been gone a lot' that I brushed off."

    s "How long have you known?"

    a "A while."

    s "Why didn't you--"

    a "It's not mine to say. It's hers."

    s "But you're saying it now."

    show amara neutral at center

    a "Because you're standing in a hallway eating her muffin on your way to my room."

    s_thoughts "I look at the muffin."

    s_thoughts "Charlotte made this."

    a "Eat the muffin."

    s_thoughts "I eat the muffin."

    s_thoughts "It's good."

    s_thoughts "It's really good."

    s_thoughts "Charlotte's muffins are always good."

    hide amara with dissolve

    stop music fadeout 3.0

    ## ===========================
    ## SCENE 32: SOPHIA SEES THE COST -- CONSCIOUSLY
    ## Late night. Walking through the house. Choosing.
    ## ===========================

    scene bg hallway night with Fade(1.0, 0.5, 1.0)

    play music mus_2am fadein 3.0

    s_thoughts "Wednesday. 1 AM."

    s_thoughts "I can't sleep."

    s_thoughts "I get up."

    s_thoughts "The house is dark. I walk through it."

    scene bg kitchen night with dissolve

    s_thoughts "I open the fridge."

    s_thoughts "Three plates. Foil. Names in Charlotte's handwriting."

    s_thoughts "Mine from Thursday. Mine from yesterday. Eve's from who knows when."

    s_thoughts "Charlotte's shepherd's pie. Charlotte's chicken. Charlotte's whatever-she-made-for-Eve."

    s_thoughts "Three plates. Three absences. Each one wrapped in foil and waiting."

    s_thoughts "I close the fridge."

    scene bg hallway night with dissolve

    s_thoughts "I go back upstairs."

    s_thoughts "Isabella's door. Closed. A sliver of light underneath. She's still up. I can hear -- not Lumi. Music. Something soft."

    s_thoughts "I haven't talked to Isabella in eight days."

    s_thoughts "I walk past."

    s_thoughts "Eve's door. Dark. No light. No sound."

    s_thoughts "I don't know when I last saw Eve."

    s_thoughts "Charlotte's door. Closed. Dark. She went to bed early. She always goes to bed early when she's been cleaning all day."

    s_thoughts "I check my phone."

    s_thoughts "Lila's last text: 4 PM. 'hey wanna grab food tmrw?'"

    s_thoughts "I never responded."

    s_thoughts "Three plates. One unanswered text. One door I haven't knocked on. One ghost I haven't checked on. One girl who goes to bed early because the house she built is emptying."

    s_thoughts "I see it all."

    s_thoughts "I'm standing in a dark hallway in my socks seeing exactly what my translation has cost."

    pause 2.0

    s_thoughts "I keep walking."

    scene bg entry night with dissolve

    s_thoughts "Amara's door."

    s_thoughts "A thin line of light underneath."

    s_thoughts "She's awake."

    s_thoughts "I stand here."

    s_thoughts "I know what I'm doing. I'm not drifting. I'm not gravitating. I'm standing in front of a door with my eyes open and my awareness of the cost fully intact."

    s_thoughts "Charlotte's plate. Isabella's music. Eve's absence. Lila's unanswered text."

    s_thoughts "I know."

    s_thoughts "I keep walking toward her door."

    s_thoughts "This is what choosing looks like. Not the clean version. Not weighing the options and picking the right one." 
    
    s_thoughts "But seeing everything you're leaving behind and walking forward anyway."
    
    s_thoughts "I stand in front of her door for a minute or two."

    s_thoughts "I don't knock."

    s_thoughts "I go back to my room."

    stop music fadeout 3.0
    
    if sophia_fire == 1: 
        jump lila_conditional
    else:
        jump amara_intimate

    ## ===========================
    ## SCENE 33: LILA -- THE STRAIN
    ## The friendship under pressure. The humor sharper. 
    ## Conditional on choosing Amara.
    ## ===========================

label lila_conditional:
    
    scene bg campus with Fade(0.8, 0.3, 0.8)

    play music mus_campus fadein 1.5

    s_thoughts "Thursday."

    s_thoughts "At our bench."

    show lila neutral at center with dissolve

    s_thoughts "Lila is there. Coffee. No smile."

    l "You didn't text me back."

    s "I know. I'm sorry."

    l "You say that a lot lately."

    s "Because I keep meaning it."

    l "You keep meaning it and then not texting me back."

    s_thoughts "She's not angry. Anger would be easier. This is something worse. This is Lila being tired."

    s "I've been--"

    l "If you say 'busy' I'm going to throw this coffee at you."

    s "...present."

    l "Present. That's a new one."

    s "I've been trying to be present. In the house. With--"

    l "With Amara."

    s "With everyone."

    show lila annoyed at center

    l "Sophia. Come on."

    s_thoughts "She puts down her coffee."

    l "I'm not mad. I want you to know that. I'm not the jealous friend. I'm not going to give you an ultimatum."

    s "I know."

    l "I just miss you."

    s_thoughts "Three words. Quiet. No caps."

    s_thoughts "Lila saying 'I just miss you' without exclamation marks is the loudest thing she's ever said."

    s "I miss you too."

    l "Do you?"

    s "Yes."

    show lila sad at center

    l "Because it doesn't feel like it." 
    
    l "It feels like I'm on the other side of a glass wall and you're in there with the quiet girl and the armchair and the whole -- it's like GRAVITY, and I'm out here being loud at a window you can't hear through."

    s_thoughts "I don't know what to say."

    l "I'm offically signed up for the spring peer counselor cycle."

    s "That's great."

    l "Yeah."

    s "Lila--"

    show lila neutral at center

    l "I'm not being dramatic. I'm telling you what it looks like from out here."

    s "I know."

    l "Okay."

    s_thoughts "She picks up her coffee."

    l "Friday?"

    s "Friday."

    l "Just us being stupid."

    s "Stupid sounds perfect."

    show lila happy at center

    s_thoughts "She almost smiles."

    l "Wear the jacket."

    s "I always wear the jacket."

    l "I know. I'm asking you to keep wearing it."

    s_thoughts "She means more than the jacket."

    hide lila with dissolve

    s_thoughts "I sit on the bench."

    s_thoughts "'I just miss you.'"

    s_thoughts "The glass wall. She described exactly what I'm doing and I can't stop doing it."

    stop music fadeout 2.0

    ## ===========================
    ## SCENE 34: AMARA INTIMATE SCENE
    ## Late night. Sophia doesn't translate. Doesn't file.
    ## Amara says something true about Sophia.
    ## The book from her shelf.
    ## ===========================

label amara_intimate:
    
    scene bg amarabedroom with Fade(1.0, 0.5, 1.0)

    play music mus_amara fadein 3.0

    s_thoughts "Friday night. Late."

    s_thoughts "I'm in Amara's room."
    
    if sophia_fire == 1:
        s_thoughts "I don't remember deciding to come here." 
        s_thoughts "I got home from being stupid with Lila -- we went to the diner, not karaoke, and we ate waffles at 10 PM like humans who have given up on adulthood -- and then I was in the hallway and her door was open and she said 'sit' and I sat."
    else:
        s_thoughts "Today I finally worked up the nerve to knock."

    show amara neutral at center with dissolve

    s_thoughts "She's on the bed. I'm in the desk chair. The lamp is on."

    s_thoughts "The Pessoa book is on her nightstand. She's reading something else now. Something with a red spine."

    s_thoughts "We've been sitting in silence for twenty minutes."

    s_thoughts "It's nice."
    
    if sophia_fire == 1:
        a "You went to see Lila."
        s "Yeah. Waffles."
        a "Good."
        s_thoughts "A single word. But it holds weight. 'Good.' Not 'good' like dismissal. 'Good' like: I'm glad you went."
    else:
        a "You didn't go out with Lila."
        s "Oh. Yeah."
        a "Surprising."
        s_thoughts "A single word. But it hold weight. 'Surprising.' Not 'surprising' like it's bad. 'Surprising' like: I thought you would."
        
    pause 1.5

    a "You're different when you come back from seeing her."

    s "Different how?"

    a "Louder. Not in volume. In... color."

    s "Color?"

    a "You come in brighter. More edges. More of the thing you try to smooth out when you're here."

    s "I don't smooth things out."

    a "You do. I don't know why."
    
    pause 1.0
    
    a "It's because of me but it's also not."
    
    pause 2.0
    
    a "I'm not sure about the not."

    s_thoughts "I stare at the ceiling. Amara not knowing is new."

    s "Does it bother you?"

    a "No. I'm okay not understanding everything."

    s_thoughts "She says it simply."

    a "I don't need you to be quiet."

    s "Everyone assumes you do."

    a "Everyone's wrong."

    pause 1.0

    a "I need you to be honest."

    s "I am honest."

    a "You're honest about other people. You're terrible about yourself."

    s_thoughts "I laugh. From somewhere deep and honest."

    s "That might be the most accurate thing anyone's ever said about me."

    a "I know."

    s_thoughts "She's looking at me. Not assessing or holding eye contact. Something simpler."

    a "You treat your own feelings like they're someone else's data."

    s "What?"

    a "You notice what you feel. And file it." 
    
    a "But you don't -- you don't feel it. You observe yourself feeling it."

    a "It's not the same thing."

    s_thoughts "The room is very quiet."

    s "I don't know how else to do it."

    a "I know."

    s_thoughts "She reaches for her bookshelf. The one organized by the system only she understands."

    s_thoughts "She pulls out a book. Small. Worn. The spine is cracked in a way that means someone has read it many times."

    a "Read this."

    s_thoughts "She holds it out."

    s_thoughts "I take it."

    s_thoughts "The Body Keeps the Score."

    s_thoughts "I look at her."
    
    s "I'm not--"

    a "Not the trauma parts." 
    
    a "Chapter eight. About how the body knows things before the mind translates them."

    s "Why?"

    a "Because you live in translation." 
    
    a "And sometimes the original is better."

    pause 2.0

    s_thoughts "I hold the book."

    s_thoughts "It's worn. From being read. Certain pages have the remnants of dog-ears."

    s_thoughts "She gave me a book from her own shelf." 
    
    s_thoughts "She pulled it from her collection and put it in my hands."

    s_thoughts "For Amara, that's -- I don't have a translation for what that is."

    s_thoughts "I don't try to find one."

    s "Thank you."

    a "Mm."

    s_thoughts "The room is warm."

    s_thoughts "I sit with the book in my hands and I don't translate anything."

    s_thoughts "Even though Amara is looking at me right now with an expression I've never seen on her face."

    s_thoughts "I just sit with it."

    hide amara with dissolve

    ## ===========================
    ## SCENE 35: THE CHAPTER ENDS
    ## The armchair mirror. Same room. Different meaning.
    ## The silence is choice now, not mystery.
    ## The empty chairs are adding up.
    ## ===========================

    scene bg livingroom with Fade(1.0, 0.5, 1.0)

    pause 2.0

    s_thoughts "It's Saturday afternoon."

    show amara neutral at center with dissolve

    s_thoughts "Amara is in the armchair."

    s_thoughts "Reading."

    s_thoughts "I sit on the couch."

    s_thoughts "I have a book. Not Nova's reading. Amara's book. The one from her shelf. I'm on chapter eight."

    s_thoughts "She's reading something I can't see the cover of. She doesn't look up."

    s_thoughts "The clock ticks. The fridge hums. Isabella's music is faint through the floor."

    pause 2.0

    s_thoughts "This is where we started."

    s_thoughts "Same room. Same armchair. Same couch."

    s_thoughts "Everything is different."

    s_thoughts "The first time I sat here, the silence was a puzzle. Something to decode. Something to translate. I watched Amara read and I filed everything I could because the filing was all I had."

    s_thoughts "Now the silence is a choice."

    s_thoughts "My choice. Her choice. Two people choosing the same room."

    s_thoughts "The kitchen is clean. Charlotte cleaned it this morning. She made pancakes for nobody in particular. She left a plate in the fridge."

    s_thoughts "Isabella is upstairs. Lumi is on her screen. She laughed at something twenty minutes ago. I heard it through the ceiling."

    s_thoughts "Eve's light has been off since Thursday."

    s_thoughts "Lila texted: 'sunday brunch? just us?'"

    s_thoughts "I haven't answered yet."

    s_thoughts "The empty chairs are adding up."

    pause 2.0

    s_thoughts "Amara turns a page."

    s_thoughts "I read a sentence about how the body stores things the mind refuses."

    s_thoughts "The streetlight outside is gold. Amara checked which direction this room faces. She did that when she moved in."

    s_thoughts "She chose this chair."

    s_thoughts "I chose the one next to it."

    s_thoughts "The silence is a room. We're both in it."

    s_thoughts "And the other rooms are getting quieter."

    pause 2.0

    s_thoughts "I text Lila: 'Sunday works. Wear something that isn't your sad sweatshirt.'"

    s_thoughts "I put my phone down."

    s_thoughts "I read."

    s_thoughts "Amara reads."

    s_thoughts "Two frequencies."

    s_thoughts "The dial is turning."
    
    s_thoughts "I'm not sure which way."

    hide amara with dissolve

    stop music fadeout 3.0

    scene black with Fade(1.0, 1.0, 1.0)
    
    "Chapter 4: Gravity -- End"

    ## ===========================
    ## END OF CHAPTER 4
    ## ===========================
    
    jump amara_ch5

    return
