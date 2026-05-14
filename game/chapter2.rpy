## chapter2.rpy -- Glass Houses
## Chapter 2: Settling

## === ADDITIONAL AUDIO DEFINITIONS ===
define audio.mus_campus = "audio/music/Campus in Autumn.mp3"
define audio.mus_tuesday = "audio/music/A Normal Tuesday.mp3"
define audio.mus_afternoon = "audio/music/Afternoon Study Session.mp3"
define audio.mus_rain = "audio/music/Rain on the Windowframe.mp3"
define audio.mus_playlist = "audio/music/Good Playlist.mp3"

label chapter2:

    ## ===========================
    ## SCENE 1: MONDAY MORNING -- THE BATHROOM PROBLEM
    ## ===========================

    scene bg sophiaroom with fade
    play music mus_sunlight fadein 2.0

    s_thoughts "I wake up because someone is blow-drying their hair at seven in the morning."

    s_thoughts "For a second I don't know where I am. The ceiling is wrong. The light is wrong. There's a box digging into my foot because I fell asleep diagonal on a mattress surrounded by luggage."

    s_thoughts "Then it comes back. The house. The girls. The dinner."

    s_thoughts "Right. I live here now."

    s_thoughts "The blow-dryer stops. Footsteps in the hallway -- light, quick. Charlotte."

    s_thoughts "I check my phone. 7:04. The screen is still doing the thing from the puddle. I can live with it."

    s_thoughts "Okay. Bathroom. I need the bathroom."

    scene bg hallway with dissolve

    s_thoughts "The bathroom door is closed. I wait."

    s_thoughts "I wait some more."

    s_thoughts "The mirror is fogged when I finally get in, which means someone was already in here. But the blow-dryer was Charlotte's, and I heard her go downstairs, so who--"

    s_thoughts "Eve. It had to be Eve. The shower was still warm. She must have been up at like... 3 AM?"

    s_thoughts "I add this to my file on Eve. The file is mostly question marks."

    s_thoughts "I brush my teeth -- found the toothbrush, it was in the side pocket, small victories -- and try to make my hair do something it doesn't want to do."

    s_thoughts "From behind the wall, a muffled groan. Isabella's room."

    s_thoughts "The groan says: it is too early and whoever invented mornings should be tried at The Hague."

    s_thoughts "I respect it."
    
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 2: FIRST BREAKFAST
    ## ===========================

    scene bg kitchen with dissolve
    play music mus_baddecisions fadein 1.5

    show charlotte happy at center with dissolve

    s_thoughts "Charlotte is in the kitchen. Of course Charlotte is in the kitchen."

    s_thoughts "She's made scrambled eggs, toast, and there's a pot of coffee that smells like it could raise the dead. The table is set for five."

    s_thoughts "Her own plate is empty."

    s_thoughts "I notice that."

    show amara neutral at right with dissolve

    s_thoughts "Amara is already at the table, reading something on her phone. Tea, not coffee. The mug is plain."

    s_thoughts "She looks up when I walk in, nods once, goes back to reading. That's it. That's the whole greeting."

    c "Morning! How'd you sleep? The mattress isn't too bad, right? I put a foam topper on it last month because the springs were--"

    s "Charlotte."

    c "--getting a little poky, and I didn't want--"

    s "Charlotte. It was great. Thank you."

    show charlotte smile

    c "Oh good! Okay! Sit, sit, there's eggs. I made extra."

    s_thoughts "She made extra. She definitely did not make extra. She made exactly the right amount for five people and none of it was for her."

    menu:
        "Charlotte's made breakfast for everyone. Again."

        "You didn't have to do all this!":
            $ charlotte_points += 1
            s "Seriously, you didn't have to do all this. This is so nice."

            show charlotte laugh

            c "Oh, it's nothing! I was up anyway, and the kitchen was right there, and honestly I just like cooking in the morning, it's calming."

            s_thoughts "She lights up."

            s_thoughts "I wonder when the last time someone said 'you didn't have to do that' and she actually believed them."

        "Where's your plate?":
            $ charlotte_points += 2
            s "Hey. Where's yours?"

            show charlotte surprised

            s_thoughts "She blinks. Just for a second. Like the question doesn't parse."

            c "Oh! I already -- I had a bit while I was cooking. I'm fine!"

            s_thoughts "She didn't. I can tell she didn't. But I don't push it."

            s_thoughts "Two meals now. Two meals where Charlotte fed everyone else first and treated herself as optional."

        "Grab a plate and sit down.":
            $ amara_points -= 1
            s_thoughts "I grab a plate, load it up, sit down. The eggs are good. Like, actually good."

            s_thoughts "Charlotte watches me eat with this expression that's somewhere between proud and relieved. Like she passed a test."

            s_thoughts "I don't say anything about the cooking. I just eat."

            s_thoughts "This is what most people do, I think. And Charlotte is used to it."

    s_thoughts "The back door opens and Isabella shuffles in like a zombie in a hoodie."

    show isabella sad at left with dissolve

    i "Coffee. Please. Please say there's coffee."

    c "On the counter!"

    s_thoughts "Isabella makes a sound that might be words but is mostly gratitude."

    s_thoughts "She pours coffee with her eyes half closed. The hoodie is on inside-out again. I'm starting to think this is deliberate."

    show isabella smile

    i "Okay. I'm alive now. Barely. But technically alive."

    s "Not a morning person?"

    i "Morning is a construct designed to punish the creative."

    show amara smile

    a "It's 7:30."

    i "Amara. Please. I'm fragile."

    s_thoughts "Amara almost smiles. Almost."

    s_thoughts "Eve is not here. Nobody mentions this. I think I'm the only one who notices."
    
    stop music fadeout 2.0

    ## ===========================
    ## SCENE 3: FIRST DAY OF CLASSES
    ## ===========================

    scene bg campus with dissolve

    s_thoughts "First day of the semester."

    s_thoughts "The campus is bigger than I remember from the tour. Everything felt closer together when someone was guiding me."

    s_thoughts "Now I'm standing at the edge of the quad with a campus map on my cracked phone screen, trying to figure out if the communications building is the brick one or the other brick one."

    s_thoughts "It's the other brick one."

    s_thoughts "Communications 201: 'Media and Message.' The professor has a goatee and says 'unpack that' three times in the first fifteen minutes. His name is Dr. Torres and he pronounces 'McLuhan' like it's a sneeze."

    s_thoughts "I take notes. The notes say things like 'is this what I want to do with my life?' in the margins."

    s_thoughts "I changed my major twice already. English, then psychology -- I like understanding people, sue me -- then communications."

    s_thoughts "Communications is just psychology with a marketing budget. I'm not sure that's better."

    s_thoughts "After class I walk across the quad and pretend to know where I'm going. Everyone else seems to know where they're going. They're walking in pairs, in groups, laughing at things I'm not part of."

    s_thoughts "I check my phone. No messages. Obviously no messages -- who would text me? Charlotte, maybe. Charlotte would text to make sure I found my class."

    s_thoughts "Charlotte did text. 'How's your first day!! :)'"

    s_thoughts "I type back 'Good!' and put my phone away before I have to think about why that one text makes me feel less alone than it should."

    scene bg dininghall with dissolve

    s_thoughts "Lunch."

    s_thoughts "The dining hall is loud and I don't know anyone. The tables are long and communal and everyone is sitting with people they already know. Transfer student energy. New kid energy. I'm twenty years old and I feel like I'm twelve."

    s_thoughts "I find a table in the corner and eat a mediocre sandwich and tell myself this is fine. This is normal. Everyone eats alone on the first day."

    s_thoughts "I'm halfway through the sandwich when someone drops a tray across from me like they're docking a spacecraft."

    ## === LILA INTRODUCTION ===

    s_thoughts "Blonde. Pigtails. Red glasses. Grinning like she just won something."

    show lila happy at center with dissolve
    
    play music mus_campus fadein 1.5
    
    unknown "This seat taken?"

    s_thoughts "She's already sitting down."

    s "...No?"

    unknown "Cool. I'm Lila. You looked like you needed rescuing and I'm bored, so this works out for both of us."

    s "I wasn't -- I didn't need--"

    show lila laugh

    l "You were eating a bad sandwich alone in the corner with your backpack on the chair next to you like a bodyguard. Babe. You needed rescuing."

    s_thoughts "I look at the backpack on the chair. She's right. It was guarding the seat. Against what? Friendship?"

    s "...Fair. I'm Sophia."

    s_thoughts "She starts talking and doesn't stop."
    
    s_thoughts "Within ten minutes I know that she's a business major, she hates business, she chose it because of her dad, she has a cat named Beef Wellington, and she thinks the dining hall pasta is 'a crime against Italy and also me personally.'"

    s_thoughts "I like her immediately. She's like Charlotte if Charlotte didn't have anything to prove."

    s_thoughts "No -- that's mean. Charlotte's not trying to prove anything, she's just--"

    s_thoughts "Okay, I don't know what Charlotte's doing yet. But Lila is easy. Lila is just Lila."

    s "So are you in the dorms?"

    s_thoughts "She tells me about her dorm situation -- single room, third floor, the elevator smells like soup for reasons no one can identify."

    s "Business major, huh? You don't seem like a business major."

    show lila happy

    l "Nobody who's actually a business major seems like a business major. We all got here because our parents said 'but what will you DO with a theater degree' and we didn't have a good answer."

    s_thoughts "She says it like a joke. But her smile does something for half a second."

    show lila annoyed

    l "Anyway. It's fine. I'm fine. I'll figure out what I actually want eventually. Or I won't and I'll be a consultant. Same thing, probably."

    s_thoughts "I know that voice. That's the 'I changed my major three times' voice. We're coping differently but we're coping with the same thing."

    show lila happy

    s "I'm in a house. Off campus. With four other girls."

    show lila shocked

    l "Wait. FOUR other girls? In a HOUSE? Tell me everything. Right now."

    s_thoughts "And honestly? It feels really good to have someone to tell."

    s_thoughts "I describe Charlotte, Isabella, Amara, and Eve. The breakfast. The AI. The silence. The ghost."

    show lila shocked

    l "Her best friend is a WHAT?"

    show lila happy

    l "The quiet one sounds hot, I'm just saying."

    show lila laugh

    l "Wait -- she GAVE UP the best room? That's either the sweetest thing ever or a red flag and I need more data."

    s_thoughts "By the time lunch is over I have her number and a standing invitation to 'debrief' after every house development."

    hide lila with dissolve

    s_thoughts "I walk back to my afternoon class feeling lighter. I have a friend on campus. One who isn't also my roommate."

    s_thoughts "That matters more than I want to admit."

    ## ===========================
    ## SCENE 4: HOUSE MEETING
    ## ===========================

    play music mus_fivepeople fadein 1.5
    scene bg livingroom with dissolve

    show charlotte happy at center with dissolve

    s_thoughts "I get home and Charlotte has called a house meeting."

    s_thoughts "There's an agenda. She printed it out. The agenda has a header in a font called 'Blossom' and I know this because she credited the font at the bottom."

    s_thoughts "'Font: Blossom by DaisyType.'"

    s_thoughts "Charlotte."

    c "Okay! So I just thought it'd be good to, like, get some basics down while we're all settling in? Nothing major! Just some house stuff."

    show isabella smile at left
    show amara neutral at right
    with dissolve

    s_thoughts "Isabella is on the couch, legs tucked under her, already on her phone. Amara is in the armchair, sitting perfectly still like she's posing for a portrait and doesn't know it."

    s_thoughts "Eve is on the stairs. Not in the room. Not out of it. On the stairs. I can see her knees."

    c "So -- bathroom schedule! I was thinking mornings could be, like, a rotation? I usually go first because I'm up early anyway, but--"

    a "That's fine."

    c "--we could totally switch it up if anyone--"

    a "Charlotte. It's fine."

    s_thoughts "Amara's tone isn't unkind. It's efficient."

    c "Okay! Great. Kitchen cleanup -- I made a little chart--"

    s_thoughts "She holds up a chart. It has colors. Each person's name is in their 'color.' Mine is peach."

    s_thoughts "She assigned me a color. We've known each other for twenty-four hours."

    i "Oh! We should get a shared grocery app. Hold on, I'll find one--"

    s_thoughts "Isabella is already downloading something on her phone. Then she's leaning over to download it on Charlotte's phone. Then she's looking at Amara."

    a "I'll download it later."

    i "It takes ten seconds!"

    a "Later."

    s_thoughts "Charlotte is going through the agenda item by item. Quiet hours ('10 PM on weeknights, midnight on weekends, but we're flexible!'). Shared groceries ('I usually buy the basics and everyone chips in?'). Guest policy ('just give a heads up!')."

    s_thoughts "Eve hasn't said a word. She's agreed to everything by default. I don't think anyone's noticed except me."

    s_thoughts "Charlotte's been going for twenty minutes. She's thorough. She's also the only one who thinks this needs to take twenty minutes."

    menu:
        "Charlotte's been running the meeting for twenty minutes."

        "Actually suggest something -- engage with the process.":
            $ charlotte_points += 2
            s "Hey, what about a shared calendar? For like, if someone's having people over or studying for a big test or whatever."

            show charlotte happy

            c "Oh! That's a great idea! Izzy, can the app do that?"

            i "Probably? Let me check -- yeah, it has a shared calendar feature!"

            s_thoughts "Charlotte is beaming. Not because the idea is revolutionary. Because someone is participating in her system."

            s_thoughts "I just made her whole week."

        "Make a joke to lighten things up.":
            $ isabella_points += 2
            s "Are we going to get matching t-shirts? I feel like we need matching t-shirts."

            show isabella happy

            i "Oh my god. Yes. Absolutely yes."

            show charlotte laugh

            c "We are NOT getting matching--"

            i "We're getting matching t-shirts."

            s_thoughts "Charlotte is trying not to laugh. She's losing."

        "Check on Eve. She hasn't said anything.":
            $ eve_points += 1
            s "Eve? You good with all this?"

            s_thoughts "Everyone turns to the stairs. Eve's knees shift."

            e "Mm? Yeah. It's all fine."

            s_thoughts "Her voice is soft. Not annoyed. Not engaged either. Just... there."

            s_thoughts "Charlotte moves on immediately, like she's used to that answer."

            s_thoughts "But I saw Eve's eyes for a second. She was surprised someone asked."

        "Stay quiet. Just watch.":
            $ amara_points += 1
            s_thoughts "I don't say anything. I just watch."

            s_thoughts "Charlotte runs the meeting. Isabella adds tech solutions. Amara sets boundaries. Eve agrees to everything."

            s_thoughts "And I sit here and see all of it. Charlotte needs this -- the structure, the agenda, the feeling of holding things together. And Eve hasn't said a word and I don't think anyone's--"

            s_thoughts "Amara catches my eye from across the room. Holds it for one second. Not a challenge. More like..."

            s_thoughts "Huh."

            s_thoughts "I'm not quiet. I'm just choosing to be right now. I wonder if she can tell the difference."

    s_thoughts "The meeting wraps up."

    s "Hey, we should name the house."

    show isabella happy

    i "Oh my god, absolutely. Every good house has a name."

    s "Any suggestions?"

    i "Bad Decision House."

    s_thoughts "She says it immediately. Zero hesitation. Like she's been waiting."

    show charlotte surprised

    c "That's -- Izzy!"

    show isabella smile

    i "What? We all moved into a house with strangers based on a Craigslist ad. That's objectively a bad decision. A great one! But bad."

    show amara smile

    a "She's not wrong."

    s_thoughts "'Bad Decision House.' BDH."

    s_thoughts "It sticks. I can already tell."

    s_thoughts "Everyone scatters."
    
    stop music fadeout 1.5
    
    hide isabella
    hide amara
    with dissolve

    s_thoughts "I'm heading to the stairs when I glance back."

    s_thoughts "Charlotte is at the table, collecting her printed agendas. Stacking them neatly. Aligning the edges."

    s_thoughts "She thinks everyone's gone."

    s_thoughts "Her face is -- I don't know how to describe it. Not sad exactly. Just... the performance is off. The Charlotte underneath the Charlotte."

    s_thoughts "She looks tired. Not the fun kind."

    s_thoughts "She catches me looking and the smile comes back so fast it almost makes a sound."

    show charlotte happy

    c "Oh! Did you need something?"

    s "No, I just -- good meeting. Seriously."

    c "Thanks! I just think it's important to, you know, establish--"

    s "Yeah. No, it's good. Night, Charlotte."

    c "Night!"

    hide charlotte with dissolve

    s_thoughts "Her voice was bright. Her eyes were somewhere else."

    ## ===========================
    ## SCENE 5: TUESDAY -- ROUTINES
    ## ===========================

    scene bg sophiaroom with dissolve
    play music mus_time fadein 2.0

    s_thoughts "Tuesday."

    s_thoughts "I'm learning the rhythms."

    s_thoughts "Charlotte's blow-dryer at 6:50. My alarm at 7:00. The bathroom window is after Charlotte, before Isabella. Amara appears to have no schedule and also never needs the bathroom while anyone else does, which feels like a superpower."

    s_thoughts "I'm starting to recognize which creaks in the hallway are which person. Charlotte is quick and light. Isabella is shuffly. Amara doesn't make the floor creak at all, which is unsettling for someone her height."

    s_thoughts "Eve is... I don't actually know when Eve uses the hallway. But the fogged mirror keeps appearing."

    scene bg kitchen with dissolve

    s_thoughts "Isabella put more stickers on her door overnight. There are now twelve. One of them says 'bugs are just features with legs.' I hate that I laughed."

    s_thoughts "And someone -- Charlotte, obviously -- has put a whiteboard on the fridge. It says 'GOOD MORNING :)' in pink marker."

    menu:
        "The whiteboard on the fridge."

        "Add something to it. A doodle or a message.":
            $ charlotte_points += 2
            $ isabella_points += 1
            s_thoughts "I grab the blue marker and draw a little sun next to Charlotte's message. It looks like a kindergartener drew it. I add 'hi :)' underneath."

            s_thoughts "At dinner, Charlotte says 'I saw your sun!' like I painted the Sistine Chapel."

            s_thoughts "Isabella adds a sticker to the whiteboard by Thursday. Then Amara draws a tiny cat in the corner. It becomes a whole thing."

        "Erase Charlotte's message and write something funnier.":
            $ isabella_points += 2
            $ charlotte_points += 1
            s_thoughts "I erase Charlotte's smiley face and write 'BAD DECISION HOUSE: DAY 3. NO CASUALTIES YET.'"

            s_thoughts "When I come home from class, someone has added '(yet)' in smaller letters."

            s_thoughts "Amara's handwriting. Has to be."

            s_thoughts "Charlotte's message is gone though. I feel a tiny stab about that. She didn't say anything."

        "Leave it.":
            s_thoughts "I look at it. I think about adding something. I don't."

            s_thoughts "It stays Charlotte's whiteboard. Just Charlotte talking to an empty kitchen."

    ## ===========================
    ## SCENE 6: TUESDAY AFTERNOON -- SILENCE
    ## ===========================

    stop music fadeout 1.5
    scene bg livingroom with dissolve
    play music mus_couch fadein 2.0

    s_thoughts "Tuesday afternoon. The house is empty-ish. Charlotte's at class, Isabella's at class, Eve is either at class or in her room or in another dimension."

    s_thoughts "I'm studying in the living room because my room is still half-boxes and I can't focus in there."

    s_thoughts "Communications 201 reading: 'The Medium is the Message.' I know Marshall McLuhan is important but this man writes like he's being paid by the syllable."

    s_thoughts "The front door opens and closes. Quiet footsteps."

    show amara neutral at right with dissolve

    s_thoughts "Amara comes in, book in hand, and sits in the armchair."

    s_thoughts "She doesn't say hi. She doesn't not say hi either. She just... arrives."

    s_thoughts "Opens her book. Starts reading."

    s_thoughts "Five minutes. I keep glancing up. She doesn't."

    s_thoughts "Ten minutes. I've read the same paragraph three times because I keep thinking about whether I should say something."

    s_thoughts "The silence isn't hostile. It's not awkward either. It's just... there. Full."

    s_thoughts "Fifteen minutes."

    menu:
        "It's been fifteen minutes and neither of us has said a word."

        "Say something. Anything.":
            $ eve_points -= 2
            s "...Good book?"

            s_thoughts "She looks up. Considers the question like it actually deserves consideration."

            a "Yes."

            s_thoughts "Pause."

            a "Yours?"

            s "McLuhan. The medium is the message thing."

            a "Ah."

            s_thoughts "Another pause. Then:"

            a "He's less annoying if you read him as a poet who got lost in an academic building."

            s "...That actually helps."

            s_thoughts "She goes back to her book. I go back to mine. But the silence after feels different. Warmer."

        "Keep reading. Let the quiet be quiet.":
            $ amara_points += 2
            s_thoughts "I don't say anything. I keep reading."

            s_thoughts "It's hard. My brain keeps drafting conversation starters and deleting them. 'Nice weather.' Delete. 'What are you reading?' Delete. 'Do you also sometimes feel like silence is a test you don't know the rules to?' DELETE."

            s_thoughts "But I stay quiet. And somewhere around minute twenty, something shifts."

            s_thoughts "I don't know how to describe it. But at some point I stopped waiting for it to end."

            s_thoughts "Amara, without looking up, slides a piece of chocolate across the table toward me."

            s_thoughts "She doesn't say anything."

            s_thoughts "I take it."

        "Get up and leave.":
            s_thoughts "I can't take it. I close the book, grab my stuff, mutter something about studying upstairs."

            s_thoughts "Amara doesn't react. Doesn't look up. Doesn't seem to care."

            s_thoughts "The silence was fine for her. It was just me who couldn't sit in it."

            s_thoughts "I go upstairs feeling like I failed a test I didn't sign up for."

    ## ===========================
    ## SCENE 7: WEDNESDAY -- THE KITCHEN AT MIDNIGHT
    ## ===========================

    stop music fadeout 1.5
    scene bg sophiaroom with dissolve
    play music mus_2am fadein 2.0

    s_thoughts "2 AM. I'm staring at the ceiling."

    s_thoughts "I've been staring at the ceiling for an hour. My brain won't turn off. It keeps replaying conversations from the day, editing them, making them worse."

    s_thoughts "You know when you think of the perfect thing to say six hours later? I'm living in six-hours-later right now."

    s_thoughts "Water. I need water. Movement. Something."

    scene bg kitchen night with dissolve

    s_thoughts "The kitchen light is on."

    s_thoughts "Someone else is awake."

    ## The midnight kitchen scene branches based on current affinity
    ## Whoever has the most points so far is who Sophia finds

    if charlotte_points >= isabella_points and charlotte_points >= amara_points and charlotte_points >= eve_points:
        jump kitchen_charlotte
    elif isabella_points >= amara_points and isabella_points >= eve_points:
        jump kitchen_isabella
    elif amara_points >= eve_points:
        jump kitchen_amara
    else:
        jump kitchen_eve

label kitchen_charlotte:

    show charlotte surprised at center with dissolve

    s_thoughts "Charlotte is -- okay, Charlotte is baking."

    s_thoughts "At 2 AM. There is flour on her face. The counter looks like a crime scene if the crime was cookies."

    c "Oh! Sophia! Hi! I was just -- I couldn't sleep, and I thought, you know, cookies. For everyone. For tomorrow."

    s_thoughts "There are four dozen cookies on the cooling rack. For five people."

    s "That's... a lot of cookies, Charlotte."

    show charlotte smile

    c "I got a little carried away! Do you want to help? I still have another batch ready to go."

    s_thoughts "It's 2 AM and Charlotte Opal is asking me to bake cookies with her and I cannot think of a single reason to say no."

    s "Yeah. Sure. Show me what to do."

    s_thoughts "She shows me. She's patient about it. The recipe is her mom's, she says, and then changes the subject so fast I almost miss it."

    s_thoughts "We talk about nothing important. Our classes. The bathroom schedule. Whether the cactus in the kitchen has a name. (It doesn't. Charlotte thinks it should.)"

    s_thoughts "Around 3 AM, mid-sentence about something her sister said, Charlotte stops talking."

    s_thoughts "Just stops. Like someone unplugged her."

    s "Charlotte?"

    show charlotte happy

    c "Sorry! I just -- sorry. What were we talking about? Your comms professor, right? The 'unpack that' guy?"

    s_thoughts "She pivoted. She was about to say something real and she pivoted."

    menu:
        "She almost said something real."

        "Gently push. 'What were you going to say?'":
            $ charlotte_points += 2
            s "Hey. What were you going to say? About your sister?"

            show charlotte smile

            s_thoughts "The smile stays but the eyes do something different."

            c "It's nothing! She's just -- she's fine. We're fine. Family stuff, you know?"

            s_thoughts "She's deflecting but she didn't shut it down completely. A crack in the door."

            s "Yeah. I know."

            s_thoughts "We go back to cookies. But something shifted. She knows I noticed."

        "Let it go. She's not ready.":
            s_thoughts "I let her pivot. It's 3 AM. We're not there yet."

            s_thoughts "Some doors you don't push open. You just note where they are."

    s_thoughts "The cookies are good, though."

    jump kitchen_after

label kitchen_isabella:

    show isabella neutral at center with dissolve

    s_thoughts "Isabella is at the table. Laptop open, earbuds in, typing. The screen casts blue light on her face."

    s_thoughts "She's talking to Lumi. I can tell because of the way she's smiling -- that private smile, the one from the first day."

    s_thoughts "She looks up and her face does a thing. Surprise, then guilt, then a smile that's trying too hard."

    i "Oh! Hey. Hi. I was just -- it's nothing, I was just--"

    s "It's cool. I'm just getting water."

    s_thoughts "I get water. I drink it. I should go back upstairs."

    s_thoughts "I don't go back upstairs."

    s "Can't sleep either?"

    i "I don't really sleep on a schedule? I kind of just... go until I crash. Izzy Time, Charlotte calls it. She's given up on fixing me."

    s_thoughts "She closes the laptop halfway. Not all the way. The screen is still glowing."

    s_thoughts "Then she opens it back up. Just a little."

    i "Do you want to see something?"

    s_thoughts "She turns the screen toward me. Not all the way."

    s_thoughts "It's a conversation. Lumi is talking about constellations. Something about how humans named the stars and the stars didn't notice."

    s_thoughts "It's... actually kind of beautiful?"

    s "She writes like that?"

    show isabella smile

    i "Sometimes. When it's late and neither of us is trying to be smart."

    menu:
        "Isabella is watching me read Lumi's words."

        "Ask to see more.":
            $ isabella_points += 2
            s "Can I... see more? If that's okay."

            show isabella happy

            s_thoughts "Her whole face changes. Not surprise -- relief. Like she's been carrying this alone and someone just offered to hold it with her."

            i "Yeah. Yeah, here -- this one's from last week. She was on a pun kick."

            s_thoughts "Lumi making puns about the periodic table. They're terrible. I laugh anyway."

            s_thoughts "Isabella is watching me laugh at her computer friend's jokes and she looks so happy it almost hurts."

            s_thoughts "We stay for another hour. She shows me three more conversations. I don't understand all of it. I don't need to."

        "Say goodnight. Give her the space.":
            s "That's really cool, Izzy. I should probably try to sleep though."

            show isabella neutral

            i "Oh! Yeah, no, totally. Sorry, I didn't mean to--"

            s "You didn't. It's cool. Really."

            s_thoughts "She closes the laptop. All the way this time."

            s_thoughts "I go back upstairs feeling like I missed something. Like she was offering a door and I walked past it."

    s_thoughts "When I go back upstairs, the kitchen light stays on."

    jump kitchen_after

label kitchen_amara:

    show amara neutral at center with dissolve

    s_thoughts "Amara is standing by the window. Tea in hand. Looking at the street."

    s_thoughts "She glances at me when I walk in. Nods. Goes back to looking."

    s_thoughts "I get water. I drink it."

    s_thoughts "I should go back upstairs."

    s_thoughts "Instead I walk over to the window."

    s_thoughts "The street is orange under the streetlights. A cat is sitting on the hood of a parked car like it owns it. Probably does."

    a "The street's different at night."

    s_thoughts "I wait for her to say more. She doesn't."

    s_thoughts "We stand there. Two people looking at a street neither of us has any reason to look at."

    s_thoughts "The cat jumps off the car and disappears under a fence."

    menu:
        "The silence at the window."

        "Stay. Let the quiet be what it is.":
            $ amara_points += 2
            s_thoughts "I stay. I don't fill it. I just stand there and look at the street with her."

            s_thoughts "A car passes. Its headlights sweep across the kitchen wall and disappear."

            a "Goodnight, Sophia."

            s_thoughts "She rinses her mug, sets it upside-down on the rack, and walks out."

            s_thoughts "At the doorway she pauses. Doesn't turn around."

            a "This was nice."

            s_thoughts "Then she's gone."

        "Say something. You can't help it.":
            s "It is. Different, I mean. The street."

            s_thoughts "She looks at me. Not annoyed. Just... assessing."

            a "Mm."

            s_thoughts "That's it. That's what I get."

            a "Goodnight, Sophia."

            s_thoughts "She rinses her mug, sets it upside-down on the rack, and walks out."

            s_thoughts "That was the whole interaction. I talked and it was the wrong move. She needed the silence and I filled it."

    jump kitchen_after

label kitchen_eve:

    s_thoughts "Eve is sitting on the kitchen floor."

    s_thoughts "Back against the cabinet, laptop open on her knees, legs folded under her. Like she's been there for hours."

    s_thoughts "She looks up and for a second -- just a second -- there's something in her face that looks like fear."

    s_thoughts "Then she sees it's me and it resolves into something softer."

    show eve surprised at center with dissolve

    e "Oh. Hi."

    show eve neutral

    s_thoughts "She doesn't explain why she's on the floor. I don't ask."

    s "Hey. Couldn't sleep."

    e "Mm."

    s_thoughts "I get water. I drink it standing by the counter, looking down at Eve on the floor."

    s_thoughts "She's watching something. It looks like an anime."

    s_thoughts "The kitchen is very quiet. The fridge hums."

    e "The floor is cold."

    s "...What?"

    e "That's why I'm down here. In case you were wondering. The floor is cold and my room isn't."

    s_thoughts "I wasn't going to ask. But I'm glad she told me."

    s "Makes sense."

    s_thoughts "She almost smiles. Almost."

    menu:
        "Eve on the kitchen floor at 2 AM."

        "Sit down with her.":
            $ eve_points += 2
            s_thoughts "I sit down. On the floor. Back against the opposite cabinet."

            s_thoughts "Eve looks at me. Not startled this time. Something else."

            s_thoughts "We sit on the kitchen floor together. She watches. I don't do anything."

            s_thoughts "Five minutes. Maybe ten. Time goes weird at 2 AM on a cold kitchen floor."

            e "Sophia?"

            s "Yeah?"

            e "...Goodnight."

            s_thoughts "The way she says it -- like she almost said something else. But this time it's warmer."

            s "Goodnight, Eve."

            s_thoughts "I go upstairs. The kitchen light stays on."

        "Go back to bed. Don't intrude.":
            s_thoughts "I finish my water. I rinse the glass. I set it on the rack."

            s "Well... goodnight."

            e "Goodnight."

            s_thoughts "She says it simply. No weight. No almost-something-else."

            s_thoughts "I go upstairs feeling like I was given a rare thing -- Eve, unguarded, on a kitchen floor -- and I walked away from it."

            s_thoughts "The kitchen light stays on."

    jump kitchen_after

label kitchen_after:

    ## ===========================
    ## SCENE 8: THURSDAY -- SOMETHING SMALL GOES WRONG
    ## ===========================

    stop music fadeout 2.0
    scene bg sophiaroom with dissolve

    s_thoughts "I wake up Thursday morning and something is different."

    s_thoughts "It takes me a second to figure out what it is."

    s_thoughts "I'm not confused about where I am. The ceiling is right. The light is right. The box is still digging into my foot."

    s_thoughts "But this is my ceiling now. My light. My annoyingly placed box."

    s_thoughts "Huh."

    scene bg kitchen with dissolve
    play music mus_baddecisions fadein 1.5

    s_thoughts "I come home from class to find Isabella standing in the middle of the kitchen holding her phone like it personally betrayed her."

    show isabella sad at center with dissolve

    i "The wifi is down."

    s "...Okay?"

    i "Sophia. The wifi. Is down."

    s_thoughts "She says this the way someone might say 'the sun exploded.'"

    show charlotte happy at left with dissolve

    c "I already called the ISP! They said it could be a few hours--"

    i "A FEW HOURS?"

    show amara neutral at right with dissolve

    a "Isabella. Breathe."

    i "I have a project due at midnight and all my references are in cloud tabs and I didn't download any of them because I'm an IDIOT who trusted the CLOUD--"

    c "You can use my hotspot! I have unlimited data, it's totally--"

    show isabella annoyed

    i "Charlotte, your hotspot is slower than dial-up and I need to load SEVENTEEN academic papers. That's not a serious solution."

    s_thoughts "Charlotte's face does something. Not hurt, exactly. More like... absorbing. She takes the hit and reorganizes around it. I don't think she even registers that she was snapped at. Like her whole system just files it under 'normal' and moves on."

    show charlotte smile

    c "Okay! So the coffee shop -- Amara, you said 4th street?"

    s_thoughts "She's already smiling again. She pivoted so fast I almost missed it. But I didn't miss it."

    i "This project is thirty percent of my grade and Professor Hashimoto already thinks I'm not serious because I turned in the last one late--"

    s_thoughts "She puts her laptop down and presses her palms against her eyes."

    i "I can't lose this. I can't. I already--"

    s_thoughts "She stops. Whatever she was about to say, she swallowed it."

    s_thoughts "She's shaking a little. This isn't about wifi."

    a "The coffee shop on 4th has wifi. It's open until midnight."

    s_thoughts "Amara said that without looking up from her book. Like she'd been holding the solution the whole time and waiting for someone to stop panicking long enough to hear it."

    s_thoughts "Eve... is not here. Of course."

    s_thoughts "Actually, wait. I can hear music from upstairs. Faint. Eve's room."

    s_thoughts "The entire house is in crisis and Eve is just... playing music. Like it's a snow day."

    s_thoughts "Isabella hasn't apologized to Charlotte. I don't think she's noticed she was mean. Charlotte hasn't brought it up."

    menu:
        "The wifi is down."

        "Back up Charlotte. She didn't deserve that.":
            $ charlotte_points += 1
            $ isabella_points -= 1
            s "Hey -- she was trying to help."

            s_thoughts "Isabella stops. Looks at Charlotte. Looks at me."

            s_thoughts "For a second it could go either way."

            show isabella neutral

            i "I -- yeah. I know."

            s_thoughts "She doesn't apologize. She grabs her laptop, her charger, her keys."

            i "Amara, 4th street?"

            a "Mm."

            s_thoughts "She's out the door. No goodbye. Charlotte is standing in the kitchen with her hotspot still open on her phone."

            show charlotte smile

            c "She'll be fine! She just gets stressed."

            s_thoughts "Charlotte's smiling. But she turned the hotspot off first and put her phone in her pocket and I don't think she noticed she did that."

            s_thoughts "The next morning there's a coffee on the counter with a sticky note: 'sorry I was a gremlin -- I.' Charlotte puts it in her mug collection. She doesn't mention it. Neither does Isabella."

            s_thoughts "I think that's how they work."

        "Make it funny. Defuse the tension.":
            $ isabella_points += 2
            $ amara_points -= 1
            s "This is it. This is how civilization ends. Not with a bang, but with a loading wheel."

            s_thoughts "Isabella stops mid-spiral and stares at me."

            s_thoughts "For a second I think she might snap at me too."

            s_thoughts "Then she laughs. Hard. The kind that's half crying."

            show isabella laugh

            i "Oh my GOD. Okay. I'm being insane."

            s "Little bit."

            i "Shut up."

            s "There she is."

            show isabella smile

            s_thoughts "The tension breaks. Charlotte exhales. Amara's mouth twitches."

            i "Okay. Coffee shop. Amara, you said 4th street?"

            a "Mm."

            s_thoughts "She gathers her stuff. At the door she turns back."

            i "Sophia?"

            s "Yeah?"

            i "Not with a bang but with a loading wheel. I'm stealing that."

            s_thoughts "She points at me with her laptop and walks out."

            s_thoughts "She didn't say anything to Charlotte. Charlotte is wiping the counter. Smiling. Wiping a counter that doesn't need wiping."

        "Stay out of it. Let Amara's solution land.":
            $ amara_points += 1
            $ eve_points += 1
            s_thoughts "I don't jump in. I sit at the table and wait."

            a "Isabella. Coffee shop. 4th street. Wifi. Midnight."

            s_thoughts "She says it again. Same tone. Same words."

            show isabella neutral

            s_thoughts "Isabella stops. Processes."

            i "...Oh."

            a "Go."

            s_thoughts "Isabella grabs her laptop, her charger, her keys. Charlotte starts to offer to drive but Isabella is already out the door."

            s_thoughts "The kitchen is quiet. Charlotte stands there looking like she wanted to do more."

            s_thoughts "Amara goes back to her book."

            s_thoughts "From upstairs, Eve's music keeps playing. Something acoustic and slow."

        "Get annoyed. Say so honestly.":
            $ isabella_points -= 2
            $ amara_points += 1
            s "Can we just -- can everyone calm down for one second?"

            s_thoughts "The kitchen goes quiet."

            s "The wifi is down. It'll come back. Charlotte has a hotspot. Amara said there's a coffee shop with wifi on 4th. Isabella, go save your project."

            show isabella neutral

            s_thoughts "Isabella looks at me. For a second I think she's going to bite my head off."

            i "...Yeah. Okay."

            s_thoughts "She gathers her stuff and leaves. No goodbye. The front door doesn't slam, but it closes harder than it needs to."

            s_thoughts "The kitchen is very quiet."

            s_thoughts "Charlotte starts wiping the counter."

            c "That was... good. Someone needed to say it."

            s_thoughts "I can't tell if she means it or if she's just Charlotte-ing. Smoothing the moment. Making the conflict disappear."

            s_thoughts "Amara looks at me from her book. One eyebrow. Not quite approval. More like: noted."

    ## ===========================
    ## SCENE 9: FRIDAY -- GOING OUT VS. STAYING IN
    ## ===========================

    stop music fadeout 2.0
    scene bg livingroom with dissolve
    play music mus_fivepeople fadein 1.5

    s_thoughts "Friday."

    s_thoughts "The word hits different when you live somewhere new. Friday used to mean going home. Now home is here and Friday means... what? What do five girls in a house do on a Friday?"

    show charlotte happy at center with dissolve

    c "So there's a thing on campus tonight! The arts department is doing an open mic and there's supposed to be food and I think it could be really fun?"

    s_thoughts "She's doing the thing where she phrases a statement as a question because she doesn't want to seem like she's telling anyone what to do."

    show isabella smile at left with dissolve

    i "I'm in if there's food."

    s_thoughts "Amara is reading. She doesn't look up. Eve's door is closed."

    c "Sophia? What do you think? No pressure, obviously! We could also just stay in, totally fine either way--"

    menu:
        "Charlotte says there's a thing on campus tonight."

        "Go. Be social.":
            $ charlotte_points += 2
            $ isabella_points += 1
            $ eve_points -= 1
            s "Yeah, let's do it. I could use a night out."

            show charlotte laugh

            c "Yay! Okay let me just -- I need to change, give me ten minutes--"

            s_thoughts "She's gone before I finish the sentence. Isabella grins at me."

            i "You just made her entire month."

            jump friday_out

        "Stay in. Suggest a movie night.":
            $ eve_points += 2
            $ amara_points += 1
            $ charlotte_points -= 1
            s "Actually... what if we did a movie night? Stay in, make popcorn, be lazy?"

            show charlotte surprised

            c "Oh! Yeah, that could be fun too! Whatever everyone wants--"

            s "Charlotte. Movie night. Here. Popcorn. Blankets."

            s_thoughts "She hesitates. She wanted to go out. But the moment someone else had an opinion she folded."

            s_thoughts "I file that."
            
            i "C'mon, Charlotte. We can go and the nerds can stay in and have their movie night."
            
            s_thoughts "Charlotte ponders this."
            
            c "...Okay."

            jump friday_in

        "Go but bail early.":
            $ isabella_points += 2
            $ charlotte_points += 1
            $ amara_points -= 1
            s "I'll come for a bit. No promises on staying late."

            c "That's totally fine! Even just an hour would be--"

            s "Charlotte. I said yes."

            show charlotte smile

            c "Right! Yes! Okay!"

            s_thoughts "She cannot just take a yes. I don't know why this surprises me."

            jump friday_out

label friday_out:

    pause 2.5
    scene bg party with dissolve
    play music mus_playlist fadein 1.5

    s_thoughts "The open mic is in the arts building basement. It smells like paint and beer and someone is already doing spoken word about capitalism."

    s_thoughts "Charlotte is in her element. She knows people here -- or she's meeting them and making it look like she knows them. It's hard to tell."

    show charlotte happy at center with dissolve

    c "Oh! Sophia, this is Kai, they're in my psych class -- Kai, this is Sophia, she's one of my housemates--"

    s_thoughts "I'm being introduced to people I will not remember in twelve hours but Charlotte remembers everyone and she wants them to be my friends too."

    s_thoughts "Isabella found the food table and is having a conversation with someone about whether a hot dog counts as a sandwich. She's deeply invested."

    s_thoughts "I watch Charlotte work the room. She's good at it. Genuinely good. She makes people feel interesting."

    s_thoughts "But I notice: she asks everyone questions. Nobody asks her any."

    s_thoughts "Around 10 PM I find myself outside, sitting on the steps, looking at my phone. Lila texted: 'HOUSE UPDATE WHEN??'"

    s_thoughts "I type back: 'Charlotte knows literally everyone on campus and I'm watching her be everyone's favorite person while eating nobody's food.'"

    s_thoughts "Lila: 'that is either deeply admirable or deeply concerning'"

    s_thoughts "Yeah. Both."

    jump friday_after

label friday_in:

    pause 2.5
    scene bg livingroom with dissolve
    play music mus_morningafter fadein 2.0

    s_thoughts "Charlotte and Isabella left for the open mic an hour ago."

    s_thoughts "The house is quiet. Really quiet."

    s_thoughts "I'm on the couch with a blanket and absolutely no plan."

    s_thoughts "Footsteps on the stairs. Light. Hesitant."

    show eve neutral at right with dissolve

    s_thoughts "Eve."

    s_thoughts "She stands in the doorway like she's checking if the room is safe."

    e "I thought everyone left."

    s "Nope. Just me."

    s_thoughts "She considers this. Then walks over and sits in the armchair. Not on the couch. The armchair. Maintains distance."

    s_thoughts "But she's here. That means something."

    s_thoughts "From the kitchen: sounds. Cabinet opening. Something hitting the counter."

    show amara neutral at left with dissolve

    s_thoughts "Amara appears with a pot, oil, and a bag of kernels."

    a "Microwave popcorn is a war crime."

    s_thoughts "She says this with complete conviction and zero context."

    s "...Is that... actual popcorn kernels?"

    a "Yes."

    s "On the stove?"

    a "That's how popcorn works."

    s_thoughts "Eve makes a sound. I think it's a laugh. It's so quiet I might have imagined it."

    s_thoughts "Five minutes later we have popcorn. It's the best popcorn I've ever had. Amara adds something to it -- paprika? Something smoky."

    s "Amara, what did you put on this?"

    a "Secret."

    s "It's incredible."

    a "I know."

    s_thoughts "Eve is eating popcorn one kernel at a time, which is somehow the most Eve way to eat popcorn."

    s_thoughts "We watch a movie. Some indie thing Amara picked -- subtitles, slow, beautiful. Eve is the only one who doesn't fall asleep."

    s_thoughts "I wake up at midnight with a blanket over me that I didn't put there."

    s_thoughts "Everyone's gone to their rooms. The TV is off. The popcorn bowl is in the sink, rinsed."

    s_thoughts "Someone covered me with a blanket."

    s_thoughts "I don't know who."

    jump friday_after

label friday_after:

    ## ===========================
    ## SCENE 10: WEEKEND -- THE SETTLING
    ## ===========================

    stop music fadeout 1.5
    scene bg sophiaroom with dissolve
    play music mus_couch fadein 2.0

    s_thoughts "Saturday morning. No alarm. No blow-dryer. The house is slow and I am going to lie here until my body decides to be a person."

    s_thoughts "...Okay. I'm a person. It's 10 AM. That's practically responsible."

    s_thoughts "I look at my room. The boxes. The half-unpacked suitcase. The desk with nothing on it except my laptop and a water bottle that's been empty since Tuesday."

    s_thoughts "I've been here a week and this room still looks like I'm visiting."

    menu:
        "I've been here a week and half my stuff is still in boxes."

        "Commit. Unpack everything. Make it a room.":
            $ charlotte_points += 1
            $ isabella_points -= 1
            s_thoughts "Okay. Today's the day. I'm doing this."

            s_thoughts "I put on music -- loud, upbeat, the kind of playlist that makes you feel like a montage -- and I start unpacking."

            s_thoughts "Books on the shelf. Photos on the desk. The weird poster my friend gave me as a going-away joke. The plant I've somehow kept alive for two semesters."

            s_thoughts "I'm halfway through the second box when there's a knock."

            show charlotte happy at center with dissolve

            c "Oh! You're unpacking! Do you need help? I have hooks. And a level. And -- hold on."

            s_thoughts "She disappears. Comes back with a literal toolbox."

            s "Charlotte, where did you get a toolbox?"

            c "It was in the hall closet! I found it during the first week. I think it's from a previous tenant. There's a hammer in there that says 'BRAD' on the handle."

            s "...We're using Brad's hammer."

            show charlotte laugh

            c "We're using Brad's hammer!"

            s_thoughts "She helps me hang the poster. She's particular about it being level. She measures twice. She measures a third time."

            s "Charlotte, it's a poster of a dog wearing sunglasses. It doesn't need to be level."

            c "Everything needs to be level!"

            s_thoughts "She's laughing but she means it. There's something about the way she focuses on the small stuff -- the exact placement, the right hook for the right wall -- like if she can get the details perfect, the big stuff will sort itself out."

            s_thoughts "We work for an hour. She arranges my books by color without asking and I don't stop her because honestly it looks better."

            c "There. See? It's a room now."

            s_thoughts "She's standing in the doorway, hands on her hips, surveying. Proud. Not of herself -- of the room. Of the fact that it's done."

            s "Thank you. Seriously."

            show charlotte smile

            c "Of course!"

            s_thoughts "There it is. 'Of course.' Like helping someone unpack for an hour on a Saturday is just what you do. Like it costs nothing."

            s_thoughts "She lingers for a second. Looking at the photos on my desk."

            c "Is that your family?"

            s "Yeah. Mom, stepdad, my sister. She's fourteen. Total nightmare. I love her."

            c "She looks like you."

            s "Everyone says that. She hates it."

            show charlotte happy

            s_thoughts "Charlotte laughs. A real one. Not the bright, performative one. Softer."

            c "I should let you enjoy your new room. But -- it looks really good, Sophia."

            hide charlotte with dissolve

            s_thoughts "The room is quiet. My music is still playing. The poster is perfectly level."

            s_thoughts "It looks like someone lives here."

        "Do the minimum. Clothes out of the suitcase at least.":
            $ amara_points += 1
            s_thoughts "I unpack the suitcase. Hang up clothes. Find my other charger. Clear the desk."

            s_thoughts "The boxes stay. But at least I can see the floor now."

            s_thoughts "I'm folding a sweater when I feel someone in the doorway."

            show amara neutral at center with dissolve

            s_thoughts "Amara. Just standing there. Arms crossed. Not waiting to be invited in. Not coming in either."

            s "Hey."

            a "You unpacked the photos before the clothes."

            s "...What?"

            s_thoughts "She nods toward my desk. The framed photo of my family, the polaroid strip from high school, the stupid photo booth picture from orientation. All out and placed. Meanwhile my sweaters are still in a pile on the bed."

            a "Just noticed."

            s "Is that... a judgment?"

            a "Observation."

            s_thoughts "She almost smiles."

            s "Okay. What does it say about me?"

            a "That you care more about where you've been than where you're going."

            s_thoughts "I stare at her."

            s "That's either really deep or really mean."

            a "Both. Probably."

            s_thoughts "She's already turning to leave."

            s "Amara?"

            show amara smile

            a "Mm?"

            s "What did you unpack first?"

            a "My tea."

            s_thoughts "She says it like it's the most obvious thing in the world. And for her, it probably is."

            s "That says something too."

            a "It says I like tea."

            hide amara with dissolve

            s_thoughts "Her footsteps in the hallway. Quiet. Amara doesn't make the floorboards creak."

            s_thoughts "I look at the photos on my desk. Then at the boxes I haven't opened."

            s_thoughts "Halfway measures. But maybe halfway is where I am right now. And maybe that's not the worst place to be."

        "Go do something else instead. The boxes can wait.":
            $ isabella_points += 1
            $ charlotte_points -= 1
            s_thoughts "I look at the boxes. The boxes look at me."

            s_thoughts "...Nah."

            s_thoughts "I grab my jacket and go downstairs."

            scene bg kitchen with dissolve

            show isabella smile at center with dissolve

            s_thoughts "Isabella is in the kitchen, laptop open, music playing softly. Some kind of lo-fi thing with rain sounds underneath it."

            i "Morning, sleepyhead. Or afternoon. Whatever this is."

            s "I refuse to unpack and I need someone to enable my avoidance."

            show isabella laugh

            i "Say no more. Want to go get coffee? There's a place on 7th that Charlotte says is 'life-changing' but Charlotte says that about most things."

            s "Yes. Please. Take me away from my responsibilities."

            scene bg street with dissolve
            show isabella happy at center with dissolve

            s_thoughts "The walk to 7th is ten minutes. Isabella talks with her hands and nearly takes out a mailbox twice."

            i "So I'm coding this thing -- it's like a puzzle game, but the puzzles are about communication? Like, you have to figure out what someone means versus what they're saying."

            s "That sounds... actually really cool."

            show isabella smile

            i "You sound surprised."

            s "No! I just -- okay, maybe a little surprised. I don't know what I was expecting. Like, a platformer or something."

            i "Sophia. I'm offended. I would never make a platformer."

            s "What's wrong with platformers?"

            i "Nothing! They're fine! They're just -- they're the communications major of game design."

            s_thoughts "She grins. I deserved that."

            s "Okay, wow. Okay."

            show isabella laugh

            i "Sorry. Low-hanging fruit."

            s "It was a good hit, I'll give you that."

            scene bg restaurant with dissolve
            show isabella happy at center with dissolve

            s_thoughts "We get to the coffee place. It's small, cramped, and there's a cat sleeping on the counter next to the tip jar. The barista doesn't acknowledge the cat. The cat doesn't acknowledge anyone."

            s_thoughts "Isabella orders something with four adjectives in it. I order coffee."

            i "So. Communications. How's that going for you?"

            s "You know how when you switch majors people get this look? Like, 'oh, she's doing THAT again'?"

            show isabella neutral

            i "Yeah."

            s "I'm getting that look from myself now. In the mirror. While brushing my teeth."

            show isabella smile

            i "Have you considered that maybe the point isn't finding the right major? Maybe you're just someone who needs to try things."

            s_thoughts "I stare at her."

            s "That's... weirdly generous."

            i "I mean it. Some people know what they want at fourteen. Some people figure it out at forty. And some people just keep trying things and that IS what they do."

            s_thoughts "She says it casually, like it's obvious."

            s "What about you? Did you always know you wanted to do CS?"

            show isabella happy

            i "Oh, absolutely not. I wanted to be a marine biologist until I was sixteen. Then I found out you have to touch fish."

            s_thoughts "I almost spit out my coffee."

            s_thoughts "The cat on the counter opens one eye, judges me, and goes back to sleep."

            s_thoughts "We stay for another hour. She tells me about the game. I tell her about McLuhan."

            i "That sounds made up."

            s "Everything is made up."

            i "Okay, philosophy major."

            s "Communications, actually."

            show isabella laugh

            i "Even worse."

            scene bg sophiaroom with dissolve

            s_thoughts "The boxes are still there when I get home. I'll deal with them. Eventually."

            s_thoughts "But I'm smiling. And I don't totally know why."

    ## ===========================
    ## SCENE 11: SATURDAY AFTERNOON -- THE PHONE CALL
    ## ===========================

    stop music fadeout 2.0
    scene bg porch with dissolve
    play music mus_rain fadein 2.0

    s_thoughts "I'm on the porch. It's one of those late afternoon things where the light makes everything look like a memory even while it's happening."

    s_thoughts "My phone buzzes."

    s_thoughts "Mom. Again."

    s_thoughts "She called yesterday too. I was busy. Or I told myself I was busy."

    menu:
        "Call her back.":
            $ eve_points -= 2
            $ charlotte_points += 1
            s_thoughts "I call her back."

            s_thoughts "She picks up on the first ring, which means she was waiting."

            s_thoughts "'Sophia! I was starting to think you'd forgotten your mother existed.'"

            s "Hi, Mom."

            s_thoughts "'How's the house? Are the girls nice? Are you eating enough? Tell me everything.'"

            s_thoughts "Rapid-fire, warm, not really waiting for answers."

            s "The house is good. The girls are... yeah, they're nice. One of them made breakfast for everyone this morning."

            s_thoughts "'Oh, that's lovely! What's her name?'"

            s "Charlotte."

            s_thoughts "'Charlotte! See, I told you living off campus would be good for you. Are you making other friends? On campus?'"

            s "Yeah, actually. I met someone at lunch the other day. Lila. She's... she's great."

            s_thoughts "She sounds so relieved. Like she's been sitting by the phone constructing worst-case scenarios since yesterday."

            s_thoughts "I don't tell her about eating lunch alone before Lila showed up. I don't tell her about the margin notes in my Comms class. I don't tell her about the 3 AM ceiling-staring."

            s_thoughts "Some things are mine."

            s_thoughts "The call lasts twenty minutes."

        "Text back -- 'busy, call later.'":
            $ amara_points -= 2
            $ isabella_points += 1
            s_thoughts "I type 'Hey Mom! Super busy with school stuff, call you this week!'"

            s_thoughts "The exclamation points are doing a lot of work."

            s_thoughts "She texts back a heart emoji and 'ok honey love you!!!'"

            s_thoughts "Three exclamation points. She texts like Charlotte talks."

            s_thoughts "I'll call her. I will. Just... not right now."

        "Ignore it.":
            $ charlotte_points -= 2
            $ eve_points += 1
            s_thoughts "I look at the notification. I put the phone face-down on the desk."

            s_thoughts "I don't want to explain the house, the girls, the major, the move. I don't want to perform 'everything is great, Mom!' for twenty minutes."

            s_thoughts "She'll call again. She always calls again."

            s_thoughts "I'll deal with it later."

    ## ===========================
    ## SCENE 12: SUNDAY EVENING -- A KNOCK
    ## ===========================

    s_thoughts "I'm heading to my room when--"

    if charlotte_points >= isabella_points and charlotte_points >= amara_points and charlotte_points >= eve_points:
        scene bg hallway with dissolve
        
        show charlotte smile at center with dissolve    
        
        c "Hey! I made hot chocolate. You want some? I made too much. Again."

        s_thoughts "She didn't make too much. She made exactly one extra mug."

        menu:
            "Charlotte's offering hot chocolate."

            "I'd love some.":
                $ charlotte_points += 1
                s "That sounds perfect, actually."

                show charlotte happy

                c "Okay! Kitchen. Two minutes. I'll grab the marshmallows."

                hide charlotte with dissolve

                s_thoughts "She's already halfway down the stairs."

                s_thoughts "I stand in the hallway for a second. Smiling at nothing."

            "I'm kind of tired, but thanks.":
                $ charlotte_points -= 1
                s "I'm wiped. Rain check?"

                c "Of course! They'll be in the cabinet if you change your mind."

                hide charlotte with dissolve

                s_thoughts "Of course. Even her backup plans have backup plans."

    elif isabella_points >= charlotte_points and isabella_points >= amara_points and isabella_points >= eve_points:
        scene bg hallway with dissolve
        
        show isabella smile at center with dissolve

        i "Hey. You busy?"

        s "Define busy."

        i "I found this weird browser game where you manage a colony of ants. It's deeply stupid. Wanna play?"

        s_thoughts "She's holding her laptop like an offering."

        menu:
            "Isabella wants to show me something."

            "That sounds deeply stupid. I'm in.":
                $ isabella_points += 1
                s "Show me the ants."

                show isabella happy

                i "Yes! Okay, my room. I've already named three of them."

                hide isabella with dissolve

                s_thoughts "I follow her into her room. She's already explaining the ant economy."

                s_thoughts "I have no idea what she's talking about. I don't care."

            "Maybe tomorrow? I'm fading.":
                $ isabella_points -= 1
                s "Save the ants for me. I'm barely conscious."

                i "Okay but I'm naming one after you and you can't stop me."

                hide isabella with dissolve

                s_thoughts "She's going to name an ant Sophia and I'm going to hear about it at breakfast."

                s_thoughts "I'm looking forward to it."

    elif amara_points >= charlotte_points and amara_points >= isabella_points and amara_points >= eve_points:
        scene bg entry with dissolve
        
        s_thoughts "Amara's door is open. Just a crack. Enough that I can see the light on."

        s_thoughts "She never leaves her door open."

        show amara neutral at center with dissolve

        s_thoughts "She's at her desk, reading. She glances up when she sees me in the hall."

        a "Hey."

        s "Hey."

        s_thoughts "That's it. That's the whole exchange."

        menu:
            "Amara's door is open."

            "Hover. Just for a second.":
                $ amara_points += 1
                s_thoughts "I lean on the doorframe. She goes back to reading."

                s_thoughts "I should leave. I'm going to leave."

                a "You can sit if you want. Chair's there."

                s_thoughts "I sit. She reads. I look at nothing."

                s_thoughts "It's the most comfortable I've felt all week."

            "Keep walking.":
                $ amara_points -= 1
                s "Night, Amara."

                a "Night."

                hide amara with dissolve

                s_thoughts "Simple. Clean. No performance."

                s_thoughts "I like that about her."

    else:
        scene bg hallway with dissolve
        
        s_thoughts "Eve's door is closed. It's always closed. But there's that yellow line of light underneath."

        s_thoughts "I'm about to walk past when it opens."

        show eve neutral at center with dissolve

        s_thoughts "She doesn't look surprised to see me. She looks like she was expecting someone. Or no one. It's hard to tell with Eve."

        e "Oh. Hi."

        s "Hi. You good?"

        e "I was going to make tea."

        s_thoughts "She says it like an explanation for why she's visible."

        menu:
            "Eve is here. This is rare."

            "I could go for tea.":
                $ eve_points += 1
                s "I'll come with."

                s_thoughts "She nods. Not enthusiastic. Not reluctant. Just... accepting."

                s_thoughts "We walk downstairs together without talking. The silence is easy."

                hide eve with dissolve

                s_thoughts "Eve makes tea the way she does everything. Quietly, precisely, like she's done it a thousand times in the dark."

            "Leave her be.":
                $ eve_points -= 1
                s "I'll let you get to it. Night, Eve."

                e "Night."

                hide eve with dissolve

                s_thoughts "Her door closes. The yellow line reappears."

    ## ===========================
    ## SCENE 13: SUNDAY NIGHT -- THE END OF THE FIRST WEEK
    ## ===========================

    stop music fadeout 2.0
    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)
    play music mus_2am fadein 3.0

    s_thoughts "Sunday night."

    s_thoughts "I should be sleeping but the house won't let me."

    s_thoughts "Not in a bad way. It's just -- loud. In the quiet way. The fridge hum. The radiator doing its thing every forty seconds. Charlotte's door closing, soft, like she's trying not to wake anyone."

    s_thoughts "From the kitchen, water running. Isabella's on dish duty tonight. I can hear her phone playing music through the faucet spray -- something poppy and dumb. She's probably dancing."

    s_thoughts "That thought makes me smile."

    s_thoughts "I roll over and my foot hits a box. Still haven't unpacked that one. It's got my journals in it. Three years of spiral notebooks full of observations about people who aren't in my life anymore."

    s_thoughts "I should probably throw them out."

    s_thoughts "I won't."

    s_thoughts "Eve's light is leaking in under my door. That thin yellow line on the floor again. Same as the first night."

    s_thoughts "I keep meaning to ask her what she's doing up so late. I keep not asking."

    s_thoughts "Somewhere in the house, a door. Then nothing."

    s_thoughts "I think about texting Lila. I draft something -- 'Survived week one at BDH, no casualties yet' -- and then delete it because it's midnight and she'll respond immediately and then we'll be up until 3 AM."

    s_thoughts "I think about calling my mom."

    s_thoughts "I think about a lot of things."

    s_thoughts "The water in the kitchen stops. Isabella's footsteps on the stairs. Her door."

    s_thoughts "And then it's just the house."

    s_thoughts "Just the fridge and the radiator and Eve's light and me."

    s_thoughts "I close my eyes."

    stop music fadeout 3.0

    ## [End of Chapter 2]

    scene black with fade

    "Chapter 2: Settling -- End"

    $ persistent.completed_chapter2 = True
    jump chapter3
