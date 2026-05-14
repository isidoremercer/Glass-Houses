## charlotte_ch6.rpy -- Glass Houses
## Chapter 6: "The Visit" -- Charlotte Route
## One act. The family. The episode. The binary. The endings.

## === NEW VARIABLES NEEDED (add to variables.rpy) ===
## None -- all variables already defined.

## === AUDIO DEFINITIONS ===
define audio.mus_charlotte = "audio/music/Charlotte Opal ~ Toast Girl.mp3"
define audio.mus_charlotte_sad = "audio/music/Charlotte Opal ~ Of Course.mp3"
define audio.mus_morningafter = "audio/music/The Morning After The Hard Thing.mp3"
define audio.mus_2am = "audio/music/House at 2AM.mp3"
define audio.mus_campus = "audio/music/Campus in Autumn.mp3"
define audio.mus_fivepeople = "audio/music/Five People in a Kitchen.mp3"
define audio.mus_tuesday = "audio/music/A Normal Tuesday.mp3"
define audio.mus_baddecisions = "audio/music/Bad Decisions.mp3"
define audio.mus_shoulders = "audio/music/Shoulders Touching.mp3"
define audio.mus_planned = "audio/music/Planned Evening.mp3"
define audio.mus_mourning = "audio/music/Mourning.mp3"
define audio.mus_glass = "audio/music/Glass Walls.mp3"
define audio.mus_wrong = "audio/music/Something's Wrong in the Kitchen"
define audio.mus_shift = "audio/music/Shift.mp3"
define audio.mus_time = "audio/music/Moments Across Time.mp3"
define audio.mus_fragile = "audio/music/Fragile Glass Between.mp3"
define audio.mus_threshold = "audio/music/Threshold.mp3"
define audio.mus_lumi = "audio/music/Lumi ~ Tender Error State (If I'm Allowed To Call It Love).mp3"
define audio.mus_spacebetween = "audio/music/Space Between Shoulders.mp3"

## ===========================
## CHAPTER 6 START
## ===========================

label charlotte_ch6:

    ## ===========================
    ## THE VISIT — FRIDAY
    ## Mom and Sophie arrive. The house is clean enough.
    ## Real family. Real laughter. Real love.
    ## Write SLOW.
    ## ===========================

    scene bg kitchen with Fade(1.5, 0.5, 1.5)

    play music mus_charlotte fadein 3.0

    s_thoughts "Charlotte has been cleaning since seven."

    s_thoughts "Not the old cleaning. I'm watching for it. The manic reorganization, the label-facing, the midnight-pantry-on-her-knees cleaning."

    s_thoughts "This isn't that."

    s_thoughts "This is... normal cleaning. The bathroom got a wipe-down. The kitchen counter doesn't have yesterday's toast crumbs on it anymore. She put the recycling out."

    s_thoughts "That's it."

    s_thoughts "She caught herself twice. Once with the spice rack -- her hand was already reaching, alphabetizing -- and she pulled back. Once with the living room pillows. She was fluffing the third one when she stopped, looked at it, and put it down at an angle."

    s_thoughts "A deliberate angle. Like she was practicing imperfection."

    s_thoughts "The house is clean enough. Not perfect."

    s_thoughts "Clean enough."

    show charlotte smile at center with dissolve

    c "Do you think the kitchen looks okay?"

    s "It looks like a kitchen."

    c "But does it look like a GOOD kitchen? Like a kitchen where a responsible adult lives?"

    s "It looks like a kitchen where five people live and one of them cries while eating eggs."

    show charlotte embarrassed at center

    c "That was the ONE TIME and it was an EMOTIONAL moment."
    
    s_thoughts "I grin at her. I'm just teasing. But the thought of that night IS on my mind."

    show charlotte neutral at center

    s_thoughts "She's nervous."

    s_thoughts "The kind where she keeps touching her hair and checking her phone and she hasn't offered me coffee once."

    s_thoughts "Charlotte hasn't offered me coffee."

    s_thoughts "Charlotte is too nervous to perform."

    s_thoughts "That's new."

    c "They'll be here at three. Mom texted. She always texts the ETA. She also texted the weather, the traffic, and a picture of a cloud that she thinks looks like a dog."

    s "Does it look like a dog?"

    c "It looks like a cloud."

    s_thoughts "She checks her phone again."

    c "Sophie's been texting me separately. She wants to know if we have 'good wifi.' She said 'good wifi' in quotes. Like there's bad wifi and good wifi and she needs to stream something the MOMENT she arrives."

    s "She's sixteen."

    c "She's sixteen."
    
    s "Did you tell her Isabella simply wouldn't abide bad wifi?"
    
    c "I did. She remains unconvinced."

    s_thoughts "Charlotte looks around the kitchen."

    show charlotte neutral at center

    c "I used to do this differently."

    s "Do what?"

    c "The visit thing. When I lived at home -- when Mom and Sophie would come back from somewhere -- I'd have the house perfect. Dinner planned. Their favorite things out. Like a hotel check-in."

    s "And now?"

    c "Now the house smells like coffee and someone left a sock on the stairs and I think that's okay."

    s "The sock is mine."

    c "I know the sock is yours. You have a sock problem."

    s "I have a sock success."

    show charlotte smile at center

    c "You have a sock problem and a delusion."

    s_thoughts "She's smiling. Nervous and real."

    s_thoughts "I pick up the sock."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## THE ARRIVAL
    ## ===========================

    scene bg entry with Fade(0.8, 0.3, 0.8)

    show charlotte happy at center with dissolve
    
    s_thoughts "3:07 PM."

    s_thoughts "The doorbell rings."

    s_thoughts "Charlotte is at the door before the sound finishes."

    play music mus_tuesday fadein 2.0

    hide charlotte
    with dissolve

    s_thoughts "She opens it."
    
    show mom neutral at right with dissolve

    s_thoughts "A woman stands on the porch. Mid-forties. Charlotte's eyes -- amber, warm. Shorter than Charlotte by a few inches. She's wearing a white dress and she has a tote bag with a library logo on it and she's already smiling."
    
    show sophie neutral at left with dissolve

    s_thoughts "Behind her: a girl. Sixteen. Same jawline as Charlotte. The same way of holding her bag with both hands like it's the only thing keeping her grounded."

    s_thoughts "Sophie."
    
    s_thoughts "They all have the same hair. Go figure."

    s_thoughts "Charlotte's mom opens her arms."
    
    show mom smile at right

    mom "My girl."

    s_thoughts "Charlotte melts."

    s_thoughts "She goes soft. Her shoulders drop. Her face does something I've never seen -- younger. Like the twenty-one-year-old evaporated and the kid underneath came out to be held."

    show charlotte smile at center with dissolve

    c "Hi, Mom."

    mom "Let me LOOK at you. You're so -- are you eating? You look thin. Sophie, doesn't she look thin?"

    s_thoughts "Sophie rolls her eyes."
    
    show sophie annoyed at left 

    soph "She looks the same, Mom."
    
    show charlotte laugh at center

    s_thoughts "Charlotte laughs."

    c "I'm eating. I'm eating so much. The house has a functioning kitchen."

    mom "A functioning kitchen! Oh, I want to see everything. I brought cookies. The ginger ones? From the place on Fourth? Sophie, give her the cookies."

    s_thoughts "Sophie hands Charlotte a tin. Their hands overlap for a second. Sophie's mouth does a thing -- the Charlotte thing. The almost-smile that's trying to decide if it's allowed."
    
    show sophie smile at left

    soph "Hey, loser."
    
    show charlotte smile at center

    c "Hey, brat."

    s_thoughts "They hug. It's short and fierce and Sophie's face goes into Charlotte's shoulder and Charlotte's hand goes to the back of Sophie's head and it lasts exactly long enough for both of them to pretend it didn't matter."

    s_thoughts "Then Charlotte turns."

    show charlotte smile at center

    c "Mom, Sophie -- this is Sophia."
    
    show mom neutral at right

    s_thoughts "Mom looks me up and down."

    s_thoughts "She has the warmth cranked to eleven. It's genetic. The same eyes, the same openness, the same way of looking at someone like they're the most important person in the room."

    s_thoughts "Now I know where Charlotte learned it."
    
    show mom smile at right

    mom "Sophia! Oh, Charlotte has told me SO much about you. Come here, come here--"

    s_thoughts "She hugs me."

    s_thoughts "I was not expecting to be hugged."

    s_thoughts "She smells like vanilla and hand cream and something I can't name that reminds me of being twelve."

    s "Hi, Ms. Opal."

    mom "Oh, call me Diane. Ms. Opal is my mother-in-law and she's a nightmare. Come in, come in -- oh, THIS is the house!"
    
    s_thoughts "I'm going to call her Ms. Opal."
    
    show sophie neutral at left

    s_thoughts "Sophie looks at me."

    s_thoughts "She does not hug me."

    s_thoughts "She looks at me the way a bodyguard looks at someone approaching the principal."

    soph "You're the girlfriend."

    s "I'm the girlfriend."

    soph "Charlotte talks about you a lot."

    s "Good things?"

    s_thoughts "Sophie gives me a look."
    
    show sophie annoyed at left

    soph "Obviously good things. Charlotte only talks about good things."

    s_thoughts "There's a weight to that."

    s_thoughts "Sophie is sixteen and she already knows the thing about Charlotte."

    hide charlotte 
    hide sophie
    hide mom
    with dissolve
    stop music fadeout 1.0

    ## ===========================
    ## THE TOUR
    ## ===========================

    scene bg entry with dissolve

    play music mus_baddecisions fadein 2.0

    s_thoughts "Charlotte gives the tour."

    s_thoughts "She points out things like a real estate agent who actually lives here -- 'this is the living room, the couch is from Isabella, she found it on the curb and it's actually really comfortable, and THIS is the kitchen--'"

    
    scene bg kitchen with dissolve
    
    show charlotte happy at left 
    show mom smile at right
    with dissolve

    s_thoughts "Mom is examining everything. She touches the wall. She opens cabinets. She says 'oh, this is NICE' about the dish towels."

    s_thoughts "The dish towels are from Target."
    
    
    scene bg livingroom with dissolve
    
    show sophie neutral at center with dissolve

    s_thoughts "Sophie is walking behind them, hands in her pockets, doing her own inventory. She's quieter than Charlotte. More watchful."
    
    scene bg hallway with dissolve
    
    show sophie neutral at center with dissolve

    s_thoughts "She reminds me of someone."

    s_thoughts "When they get to Charlotte's room, Mom stops."

    scene bg charlottebedroom 
    hide sophie
    with dissolve
    
    show mom neutral at right with dissolve

    mom "Oh, Charlotte. The postcards."

    s_thoughts "Mom is looking at Charlotte's wall."

    s_thoughts "Three postcards. All paintings."

    s_thoughts "Charlotte's voice changes. Just slightly."

    show charlotte embarrassed at left with dissolve

    c "Yeah, I -- I started collecting them. From the museum."

    mom "They're beautiful. This one -- is this Vermeer?"

    c "Yeah. For my paper."

    mom "And this one?"

    c "That's just -- I liked it. It's a woman peeling an apple."

    s_thoughts "Mom looks at it for a long time."

    s_thoughts "She looks peaceful."

    c "Yeah."
    
    show sophie neutral at center with dissolve

    s_thoughts "Sophie is looking at the postcards too. She doesn't say anything."

    s_thoughts "Her eyes land on the apple painting postcard."
    
    show sophie smile at center

    s_thoughts "Something crosses her face."
    
    s_thoughts "Something that belongs to Sophie."

    hide charlotte 
    hide sophie
    hide mom
    with dissolve
    
    stop music fadeout 2.0

    ## ===========================
    ## DINNER — THE WARM PART
    ## This must be LONG. Real family. Real laughter.
    ## The reader must enjoy this before Saturday.
    ## ===========================

    scene bg kitchen with Fade(0.8, 0.3, 0.8)

    play music mus_playlist fadein 2.0

    s_thoughts "Dinner."

    s_thoughts "Charlotte cooked."

    s_thoughts "I watched her decide to cook. It took fifteen minutes. She stood in the kitchen looking at the stove like it owed her money. Then she opened the fridge. Closed it. Opened it again."

    s_thoughts "'I want to cook,' she said. Quiet. Like a confession."

    s_thoughts "'Then cook,' I said."

    s_thoughts "'Because I want to. Not because they're here.'"

    s_thoughts "'Okay.'"

    s_thoughts "'I want to make the risotto. The one with the mushrooms. Because I like that recipe.'"

    s_thoughts "'Then make the risotto.'"

    s_thoughts "She made the risotto."

    s_thoughts "It's really good."

    show charlotte happy at left 
    show mom smile at right
    show sophie neutral at center
    with dissolve

    s_thoughts "The kitchen is full. Charlotte and Mom and Sophie and me, crammed around the table."

    s_thoughts "Mom is on her second helping."

    mom "Charlotte, this is INCREDIBLE. When did you learn to make risotto?"

    c "YouTube."

    mom "YouTube! In my day we had COOKBOOKS. Remember the cookbooks, Charlotte? The shelf in the kitchen?"

    c "I remember."

    mom "She used to read them like novels. Just -- sit on the floor and read recipes. She'd tell me what we should make and I'd say 'Charlotte, we don't have half these ingredients' and she'd say--"

    show charlotte embarrassed at left

    c "Mom."

    mom "She'd say 'we can substitute!' Everything was a substitution. You can't substitute cream for yogurt, Charlotte."

    c "You CAN substitute cream for yogurt."

    mom "You CANNOT."

    c "It's chemistry! It's the same fat content if you adjust--"

    mom "It is NOT the same fat content!"

    s_thoughts "Sophie looks at me."

    soph "They do this." 
    
    s_thoughts "It's quiet enough that only I hear."

    s "The cream argument?"
    
    show sophie smile at center

    soph "Every time. It's been going for like ten years."

    s_thoughts "I watch Charlotte argue about dairy science with her mother and something in my chest does a complicated architectural thing."

    s_thoughts "This is a real family."
    
    s_thoughts "I guess that should've been obvious."
    
    s_thoughts "Maybe I was stereotyping."
    
    s_thoughts "...I do that."

    show charlotte laugh at left

    c "SOPHIE. Tell Mom that cream and yogurt are interchangeable."

    s_thoughts "Sophie takes a very deliberate bite of risotto."

    soph "I'm not getting involved."

    c "TRAITOR."

    s_thoughts "Mom laughs."

    s_thoughts "Charlotte laughs."

    s_thoughts "It's pleasant."

    s_thoughts "..."

    s_thoughts "The stories come out after the risotto."

    s_thoughts "Mom is a talker. A YAPPER, even. She has a story for everything and every story has a tangent and every tangent has a character."

    mom "Charlotte once tried to surprise me with breakfast in bed. How old were you? Fourteen?"

    show charlotte embarrassed at left

    c "Mom, don't--"
    
    show mom laugh at right

    mom "Fourteen! She made this elaborate tray. Orange juice, toast, eggs, a little flower in a vase -- she got a FLOWER from the garden--"

    c "MOM."

    mom "And she's carrying this tray up the stairs and she trips on the top step and the ENTIRE thing goes everywhere. Eggs on the wall. Orange juice on the carpet. The flower went down the stairs like a little--"

    s_thoughts "Mom is laughing so hard she can't finish."

    show charlotte annoyed at left

    c "The carpet was fine."

    mom "The carpet was ORANGE, Charlotte."

    c "It came out!"

    s_thoughts "Sophie grins."
    
    show sophie smile at center

    soph "I remember that. I heard the crash and came out and you were just standing there with an empty tray looking like--"

    c "Can we talk about LITERALLY anything else?"

    s "I want to hear more about the carpet."

    c "Sophia. You are supposed to be on my side."

    s "I'm on the carpet's side."

    s_thoughts "Mom HOWLS."
    
    show charlotte embarrassed at left

    s_thoughts "Charlotte buries her face in her hands."

    s_thoughts "Sophie and I make eye contact across the table."

    s_thoughts "Something shifts. A gear. The bodyguard stance loosens half an inch."

    soph "She does that, right?"
    
    soph "The face-in-hands thing."

    s "Every time."

    soph "It means she's not actually mad."

    s "I know."

    s_thoughts "Sophie nods."

    s_thoughts "Something passed an inspection I didn't know I was taking."

    show charlotte smile at left

    s_thoughts "Charlotte emerges from behind her hands."

    c "I hate all of you."

    mom "You love us."

    c "Unfortunately."

    s_thoughts "Mom reaches across the table and squeezes Charlotte's hand."

    s_thoughts "Charlotte squeezes back."

    s_thoughts "Sophie watches them."

    s_thoughts "I watch Sophie watching them."

    s_thoughts "..."
    
    hide charlotte
    hide mom
    hide sophie
    with dissolve
    
    scene bg porch with dissolve

    s_thoughts "Later. The dishes are done -- Mom insisted, Charlotte insisted back, they compromised by both doing them at the same time in a way that was clearly less efficient than one person doing them alone."

    s_thoughts "Sophie and I are on the porch."
    
    stop music fadeout 1.0

    with dissolve

    s_thoughts "She's on her phone. I'm pretending to check mine."

    s_thoughts "The evening air is cold. Inside, Charlotte and Mom are talking about something. I can hear Charlotte's laugh through the door."

    s_thoughts "Sophie puts her phone down."
    
    play music mus_sunlight fadein 1.5
    
    show sophie neutral at center with dissolve

    soph "Can I ask you something?"

    s "Yeah."

    soph "Is she different here?"

    s "What do you mean?"

    soph "Like -- at home she's... She's the organizer. She has the plan. She checks on everyone and makes sure everything's running."

    s "She does that here too."

    soph "But does she do it ALL the time?"

    s_thoughts "I think about that."

    s "Less. Recently."

    s_thoughts "Sophie is quiet."

    soph "She sounds different on the phone. The last few weeks. Less... on."

    s "On?"

    soph "Like a light switch. Charlotte is always ON. Like she's hosting. Even when she's just talking to me she's -- managing the conversation. Making sure I'm okay. Asking the right questions."

    s_thoughts "Sophie picks at the porch railing."

    soph "But lately she calls and she just... talks. About a painting. About a book about bread." 
    
    soph "She told me she said no to going to the store and it was like she'd climbed Everest."

    s "It kind of was."

    s_thoughts "Sophie looks at me."
    
    soph "You did that?"

    s "I didn't do anything."

    soph "Yeah you did. She's different because of you. Because someone's watching and she doesn't have to be the one watching back."

    s_thoughts "Sixteen."

    s_thoughts "This kid is sixteen."

    s "She did it herself."

    s_thoughts "Sophie shakes her head."
    
    show sophie smile at center

    soph "Charlotte doesn't do things for herself. That's, like, the whole point."

    s_thoughts "She picks up her phone again."
    
    show sophie annoyed at center

    soph "Don't mess it up."

    s "I'll try."

    soph "Don't TRY. Just don't mess it up."
    
    show sophie neutral at center

    s_thoughts "She goes back to her phone."

    s_thoughts "I sit on the porch."

    s_thoughts "Inside, Charlotte snort-laughs at something her mom said."

    s_thoughts "Sophie hears it."

    s_thoughts "She doesn't look up from her phone, but the corner of her mouth moves."

    hide sophie with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## FRIDAY NIGHT WIND-DOWN
    ## ===========================

    scene bg sophiaroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "11 PM."

    s_thoughts "Mom is on the pull-out couch in the living room. Sophie got an air mattress in Charlotte's room. Charlotte fought her on it -- 'you take the bed, I'll take the floor' -- and Sophie said 'Charlotte, shut up and get in the bed' and Charlotte shut up and got in the bed."

    s_thoughts "I'm in my room."

    s_thoughts "I hear Charlotte through the wall. Talking to Sophie. Their voices are low and warm and indistinct. Occasionally one of them laughs."

    s_thoughts "I can't make out the words."

    s_thoughts "I don't need to."

    s_thoughts "Charlotte sounds like Charlotte."

    s_thoughts "Just... a girl talking to her sister in the dark."

    s_thoughts "I fall asleep to the sound of it."

    stop music fadeout 3.0

    ## ===========================
    ## SATURDAY — THE EPISODE
    ## The manic uptick. Slow build.
    ## Sophia doesn't recognize it at first.
    ## Sophie does.
    ## ===========================

    scene bg kitchen with Fade(1.5, 0.5, 1.5)

    s_thoughts "Saturday morning."

    play music mus_tuesday fadein 2.0
    
    show mom smile at right with dissolve

    s_thoughts "Mom is making pancakes."

    s_thoughts "She commandeered the kitchen at eight. Charlotte tried to help and..."
    
    mom "Sit DOWN, it's MY turn."
    
    show charlotte happy at left with dissolve
    
    s_thoughts "And Charlotte sat down and she looked... happy. Confused and happy."

    s_thoughts "The pancakes are okay. Not Charlotte-level. Mom puts too much batter and the edges are crispy in a way that's more 'mistake' than 'style.'"

    s_thoughts "Nobody cares."

    s_thoughts "Mom is talking. She's always talking. She has PLANS."

    mom "I was thinking -- there's that museum Charlotte keeps mentioning. The one with the paintings? We should go! All of us."

    mom "And then lunch. There's a place on -- what's that street, Charlotte? The one with the Thai restaurant and the--"

    c "Maple."

    mom "MAPLE. The Thai place on Maple. And then maybe we could walk around campus? I want to see your building. The art history building."

    c "It's just a building, Mom."

    mom "It's YOUR building! I want to see where my girl studies."

    s_thoughts "Charlotte smiles."

    s_thoughts "Mom is warm. Genuinely warm. She asks about the house, about classes, about everyone. She wants to know about Isabella--"
    
    mom "The one with the glasses? Charlotte says she's so smart!" 
    
    s_thoughts "-- and about Amara --"

    mom "Oh, she sounds lovely!"
    
    s_thoughts "-- and about the professors."

    s_thoughts "She asks about me."

    mom "So, Sophia. Charlotte says you're studying media theory? That sounds FASCINATING. What's that about?"

    s "It's about how we -- um. How people present themselves. Performance. Observation."

    mom "Like acting?"

    s "Kind of. More like... how everyone is always performing, all the time. And we study the gap between the performance and the person."

    s_thoughts "Mom thinks about this."

    mom "That's smart. Charlotte should take that class."

    s_thoughts "Charlotte makes a sound."

    show charlotte embarrassed at left

    c "I'm taking visual culture, Mom. It's adjacent."

    mom "'Adjacent!' Listen to you. My college girl."

    s_thoughts "She's proud. She's genuinely proud."

    s_thoughts "The morning is good."

    hide charlotte
    hide mom
    with dissolve

    scene bg street with dissolve

    s_thoughts "We go out. The museum. Mom spends twenty minutes in front of a Monet."
    
    show mom laugh at left with dissolve
    
    mom "I don't get it but I LOVE it." 
    
    s_thoughts "Sophie finds the gift shop and doesn't leave."
    
    show charlotte happy at right with dissolve

    s_thoughts "Charlotte stands in front of the apple-peeling painting."

    s_thoughts "Her mom comes up behind her."

    mom "That's the one you like?"

    s_thoughts "Charlotte nods."
    
    show mom smile at left

    mom "It's nice. She looks calm."

    c "Yeah."

    mom "Like she's not worried about anything. Just peeling her apple."

    s_thoughts "Charlotte doesn't say anything."

    s_thoughts "I watch from across the room."

    s_thoughts "Sophie is watching too. From the gift shop doorway. Phone in one hand, not looking at it."
    
    hide charlotte
    hide mom
    with dissolve

    ## ===

    scene bg restaurant with dissolve

    s_thoughts "Lunch is loud and good. Mom orders for the table because Mom orders for the table."

    s_thoughts "Charlotte doesn't fight it." 
    
    s_thoughts "She used to fight it -- I can tell from the way Sophie watches Charlotte NOT fight it, like she's waiting for the correction that doesn't come."
    
    scene bg street with dissolve

    s_thoughts "We walk home. Mom links her arm through Charlotte's. Sophie walks behind with me."
    
    show sophie neutral at center with dissolve

    soph "The museum was nice."
    
    s_thoughts "She's quiet."

    s "Yeah."

    soph "She goes there by herself now?"

    s "Sometimes."

    s_thoughts "Sophie nods."

    s_thoughts "She doesn't say anything else."
    
    hide sophie with dissolve
    
    scene bg livingroom with dissolve

    s_thoughts "The afternoon is slow and warm. Mom naps on the pull-out couch."

    s_thoughts "Sophie is in Charlotte's room on her phone." 
    
    s_thoughts "Charlotte and I go out to sit on the porch together."

    scene bg porch with dissolve

    show charlotte smile at center with dissolve

    s_thoughts "Charlotte is leaning against me."

    s_thoughts "She's not talking."

    s_thoughts "She's just there."

    c "This is nice."

    s "Yeah."

    c "They're nice."

    s "They're nice."

    c "Mom is a lot."

    s "She's great."

    show charlotte neutral at center

    c "She's great."

    s_thoughts "A pause."

    c "She's a lot and she's great and I love her."

    s "I know."

    s_thoughts "Charlotte watches a bird cross the yard."

    c "Thanks for being here."

    s "Where else would I be?"

    show charlotte smile at center

    c "I don't know. Somewhere with fewer pancakes."

    s "Never."

    s_thoughts "She laughs. Quiet."

    s_thoughts "The porch is warm."

    hide charlotte with dissolve
    stop music fadeout 2.0

    ## ===========================
    ## SATURDAY EVENING — THE SHIFT
    ## Mom's energy changes. The uptick.
    ## Sophia doesn't catch it at first.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    s_thoughts "Saturday evening."
    
    play music mus_shift fadein 2.0

    s_thoughts "Something is different."

    s_thoughts "I can't place it at first. Mom woke up from her nap and she's... brighter. Not the warm-bright from this morning. Something with more wattage."

    s_thoughts "She's rearranging things in the kitchen."
    
    show mom smile at left with dissolve

    mom "I just thought -- if you moved this cutting board here, and the dish rack over THERE, you'd have so much more counter space!" 
    
    mom "..."
    
    mom "See! See how much room that makes?"

    show charlotte neutral at right with dissolve

    s_thoughts "Charlotte is watching."

    c "Mom, it's fine where it--"

    mom "No, no, look! And the spice rack -- oh, Charlotte, the spice rack is all wrong. Who organized this?"

    c "I did."

    mom "Well, it should be by CUISINE. See? Italian spices together, Indian spices together. That way when you're cooking you just grab the whole section."

    s_thoughts "She's moving the spices as she talks. Pulling jars off the shelf. Rearranging."

    s_thoughts "Her hands are fast."

    s_thoughts "I didn't notice this morning. Or maybe it wasn't happening this morning."

    s_thoughts "Mom's voice is louder. Not shouting-loud. Volume-turned-up loud. Like someone adjusted a dial and the output increased by twenty percent."

    mom "AND -- okay, hear me out -- we should go out tonight. All of us. Is there a place? A good place?" 
    
    mom "Charlotte, is there a good restaurant? Or a show? Is there a show? We could see a show!"
    
    show charlotte sad at right

    c "Mom, it's Saturday night. Everything's booked."

    mom "We could TRY. You never know! Remember that time in -- where was it, Sophie? The Italian place that didn't take reservations and we just showed up and--"

    s_thoughts "Mom is moving through the kitchen. She opens a cabinet. Closes it. Opens another one."

    mom "And we could do brunch tomorrow! Before we leave. I saw a place on the walk -- beautiful flowers in the window, looked very charming--"

    s_thoughts "The itinerary is growing."

    mom "Restaurant tonight. Brunch tomorrow. Maybe the campus. Maybe the park. Maybe the other museum -- is there another museum? There MUST be another museum."

    s_thoughts "Charlotte's face is very still."

    show charlotte neutral at right

    s_thoughts "I look at Charlotte."

    s_thoughts "She's not smiling. She's not frowning. She's watching Mom with an expression I can't read."

    s_thoughts "I look at Sophie."
    
    show sophie neutral at center with dissolve

    s_thoughts "Sophie is at the table."

    s_thoughts "Sophie is quiet."

    s_thoughts "Sophie has been quiet for ten minutes."

    s_thoughts "She's holding her phone in her lap but she's not looking at it. She's looking at her hands."

    s_thoughts "Something is wrong."

    s_thoughts "I don't know what."
    
    hide sophie with dissolve

    s_thoughts "Mom is still going. The plans are stacking. A restaurant and a brunch and a walk and a show and oh -- what about a botanical garden?"

    stop music fadeout 2.0

    s_thoughts "I look at Charlotte again."

    s_thoughts "Charlotte looks back at me."

    s_thoughts "Her eyes say: don't."

    s_thoughts "Don't what?"

    s_thoughts "Don't ask."
    
    hide mom
    hide charlotte
    with dissolve

    ## ===========================
    ## THE LINE
    ## "Helper gal."
    ## ===========================

    scene bg kitchen with Fade(1.5, 1.0, 1.5)

    s_thoughts "Mom is telling a story."
    
    show mom smile at right with dissolve

    s_thoughts "She's moved on from the plans. She's remembering now. The energy is carrying her from topic to topic like a river finding paths downhill."

    mom "Oh -- do you know what I was thinking about on the drive?" 
    
    mom "Charlotte, do you remember the mornings?"

    show charlotte neutral at left with dissolve

    c "...What mornings?"

    mom "The MORNINGS. When you were little." 
    
    mom "You'd get up before everyone and I'd come downstairs and there you'd be in the kitchen -- what were you, nine? Ten?"
    
    play music mus_wrong fadein 3.0

    s_thoughts "Charlotte doesn't move."
    
    s_thoughts "Oh god."

    mom "You'd be up on that little stool." 
    
    mom "You know! The wooden one? With the step?"
    
    s_thoughts "Oh god oh god oh god."
    
    mom "And you'd have the WHOLE breakfast going. Eggs, toast, everything." 
    
    mom "For me and Sophie."
    
    show mom laugh at right

    s_thoughts "Mom laughs."
    
    s_thoughts "Charlotte doesn't. I'm watching her, trying to gauge her reaction, but I can't."

    mom "You were so TINY back then." 
    
    mom "On that stool. Reaching up to the stove." 
    
    s_thoughts "I want her to stop. Please, stop."
    
    mom "And I'd say -- what did I say? -- I'd say--"
    
    show mom smile at right

    s_thoughts "Mom is beaming."

    mom "There's my little helper gal!"

    s_thoughts "She says it like sunshine."
    
    s_thoughts "But Charlotte's face might as well be eclipsed."

    mom "Charlotte was always my little helper gal. Isn't that the sweetest thing? She just -- she WANTED to help. She was born helpful." 
    
    mom "Some kids are born running and some kids are born HELPING and Charlotte was just -- she was my little--"

    s_thoughts "I hear the sound from the table."

    s_thoughts "Small. Almost nothing."
    
    hide mom
    show sophie sad at right 
    with dissolve

    s_thoughts "Sophie."

    s_thoughts "Sophie's shoulders are shaking."

    s_thoughts "Her hand is over her mouth. Her eyes are full. Tears rolling down her cheeks, not making a sound."

    s_thoughts "Sophie is crying."

    s_thoughts "Quietly. The way someone cries when they've learned not to be loud about it."

    s_thoughts "Because Sophie knows."
    
    s_thoughts "She knows what I know. Obviously. I should've realized."

    s_thoughts "Diane Opal was in bed and Charlotte was the one feeding five-year-old Sophie."

    s_thoughts "She doesn't see Sophie crying."

    s_thoughts "She's... still talking."
    
    hide sophie
    show mom laugh at right
    with dissolve

    mom "-- and she'd make the BEST little breakfasts. Remember, Sophie? Charlotte's breakfasts?"

    s_thoughts "Sophie can't answer."

    s_thoughts "Mom doesn't notice."

    s_thoughts "She's already on the next thing. The energy is carrying her. She's talking about the kitchen at home and the curtains she wants to change and a recipe she saw online and--"

    s_thoughts "I look at Charlotte."

    show charlotte sad at left

    s_thoughts "Charlotte's face."
    
    s_thoughts "I see it. For the first time. Not half-there. Not hidden. Not a glimpse."
    
    s_thoughts "I see the ten year old."

    s_thoughts "Standing on that stool. That stupid goddamn stool."
    
    s_thoughts "The one that's a cute anecdote to Diane Opal."

    s_thoughts "Who has no clue."

    s_thoughts "She doesn't know what she built. She was in bed. She doesn't remember it that way." 
    
    s_thoughts "The medication stabilized a version of the story where Charlotte was just helpful." 
    
    s_thoughts "Born helpful." 
    
    s_thoughts "A helper gal."

    s_thoughts "And Charlotte is standing in the kitchen listening to her mother and there's nothing on her face."

    s_thoughts "Nothing."

    s_thoughts "Nothing like a place where something was and isn't anymore."

    s_thoughts "Sophie is crying."

    s_thoughts "Mom is talking."

    s_thoughts "Charlotte is standing very still."

    s_thoughts "The kitchen is too full of her voice and it's too bright and too small and I have to do something."

    stop music fadeout 5.0
    
    pause 5.5

    ## ===========================
    ## THE BINARY CHOICE
    ## ===========================

    play music mus_threshold fadein 2.0

    menu:

        "Push Charlotte to say something.":
            jump charlotte_ch6_push

        "Speak up about it.":
            jump charlotte_ch6_confront

        "Get on the stool." if charlotte_gh_unlocked() and charlotte_push >= 6 and charlotte_present >= 10 and charlotte_eve > 0:
            jump charlotte_ch6_stool

    ## ===========================
    ## BRANCH: PUSH CHARLOTTE
    ## ===========================

label charlotte_ch6_push:

    ## Route based on variables
    if charlotte_push >= 6 and charlotte_present < 10:
        jump charlotte_ch6_variant2

    elif charlotte_push < 6 and charlotte_present >= 10:
        jump charlotte_ch6_variant3

    elif charlotte_push >= 6 and charlotte_present >= 10:
        ## High/high: Push leads to The Crack
        jump charlotte_ch6_variant2

    else:
        ## Low/Low
        jump charlotte_ch6_variant1

    ## ===========================
    ## BRANCH: CONFRONT YOURSELF
    ## ===========================

label charlotte_ch6_confront:

    if charlotte_push >= 6 and charlotte_present < 10:
        jump charlotte_ch6_variant5

    elif charlotte_push < 6 and charlotte_present >= 10:
        jump charlotte_ch6_variant6

    elif charlotte_push >= 6 and charlotte_present >= 10:
        ## High/high: Confront leads to Something New
        jump charlotte_ch6_variant6

    else:
        ## Low/Low
        jump charlotte_ch6_variant4

    ## ===========================
    ## VARIANT 1: Low Push + Low Present + "Push Charlotte"
    ## Charlotte refuses. The mask holds.
    ## ===========================

label charlotte_ch6_variant1:

    s_thoughts "I turn to Charlotte."

    s "Charlotte."

    s_thoughts "She looks at me."

    s_thoughts "I put everything into her name. Everything I've learned. Everything I've seen."

    s "Say something."

    show charlotte neutral at left

    s_thoughts "Charlotte looks at me."

    s_thoughts "Looks at Mom."

    s_thoughts "Looks at Sophie. Sophie's hand over her mouth. Tears on her cheeks."

    s_thoughts "Charlotte's mouth opens."

    s_thoughts "I see it assemble."

    s_thoughts "The brightness. The deflection. The pivot."
    
    s_thoughts "No."
    
    s_thoughts "Please don't."
    
    s_thoughts "Please."

    show charlotte happy at left

    c "Mom, do you want tea? I think I have that chamomile you like."

    s_thoughts "Please stop. Please, Charlotte. Please."
    
    show mom smile at right

    mom "Oh, that sounds LOVELY! Is it the one from--"

    c "The one from the farmer's market. Yeah. Let me put the kettle on."

    s_thoughts "Charlotte moves to the stove."

    s_thoughts "Her hands are steady."

    s_thoughts "Sophie wipes her eyes. Quiet. Practiced."

    s_thoughts "The moment sinks like a stone."

    s_thoughts "Mom is talking about tea now. A tea she had once in a shop somewhere. The story continues."

    show charlotte happy at left

    s_thoughts "Charlotte fills the kettle."

    s_thoughts "Her back is to the room."

    s_thoughts "I can see her shoulders."

    s_thoughts "They're perfect."

    s_thoughts "Everything about her is perfect."
    
    s_thoughts "Of course."

    stop music fadeout 2.0

    ## Fork: eve determines ending
    if charlotte_eve > 0:
        jump charlotte_ch6_of_course
    else:
        jump charlotte_ch6_five_places

    ## ===========================
    ## VARIANT 2: High Push + "Push Charlotte"
    ## Charlotte confronts. The mask blows off.
    ## ===========================

label charlotte_ch6_variant2:

    s_thoughts "I turn to Charlotte."

    s "Charlotte."

    s_thoughts "Just her name."

    s_thoughts "That's all I've ever had to give her. Her name said like it's real. Like the person it belongs to is real."

    show charlotte neutral at left

    s_thoughts "Charlotte is shaking."

    s_thoughts "I can see it in her hands. In the line of her jaw."

    c "Mom."

    s_thoughts "Mom stops talking."

    s_thoughts "Charlotte's voice is quiet."

    s_thoughts "Not the brightness. Not the deflection."

    s_thoughts "Quiet the way a room goes quiet before something lands."

    c "I wasn't your helper gal."
    
    show mom neutral at right

    mom "What?"

    c "I was ten."

    s_thoughts "Mom's face."

    s_thoughts "The brightness flickers. Like a bulb deciding whether to stay on."

    c "And you were in bed. And Sophie was hungry."

    s_thoughts "It's sudden."

    s_thoughts "Every sound in the kitchen stops. The fridge hum is still there but I can't hear it."

    c "I stood on the stool because I was the only one standing."

    s_thoughts "Charlotte's voice doesn't crack. It's precise. Each word placed like she's been rehearsing this for a decade without knowing it."

    c "I love you."

    s_thoughts "She says it first."

    c "And I know you're better. And I know the medication works and I know you've been good for years and I know you love us."

    s_thoughts "Mom's hand is on the counter."

    c "But you don't get to call it sweet."
    
    show mom blegh at right

    s_thoughts "I look at Mom's face."

    s_thoughts "The brightness goes out."

    s_thoughts "Not into a spiral. Not into guilt. Something else. Recognition."

    s_thoughts "The kind that takes years to process and she's getting it in thirty seconds."

    mom "Charlotte--"

    c "It wasn't sweet. It was Tuesday. It was every Tuesday. And Wednesday. And the days you were in bed and Sophie needed lunch and I was eleven and I didn't know how to make lunch so I made toast. Every day. Toast."

    s_thoughts "I almost gasp."
    
    s_thoughts "Lila flashes through my mind. I'm sitting here quiet and I'm staring. I can't help it."
    
    s_thoughts "Sophie makes a sound."

    s_thoughts "Charlotte doesn't look at her."

    c "I learned the eggs because toast wasn't enough. I learned the omelets because the eggs were boring. I learned the fold because you liked the fold."

    s_thoughts "Her voice wavers."

    s_thoughts "One wobble."

    c "I... I-I was so good at it that you forgot I was doing it."

    s_thoughts "The kitchen."

    s_thoughts "Mom is standing very still."

    s_thoughts "Sophie is crying. Not the quiet kind anymore. The kind with sound."

    s_thoughts "Charlotte takes a breath."

    c "I love you. I need you to know that first. Before the rest."

    s_thoughts "Mom nods. Small."

    c "But 'helper gal' isn't a happy memory. It's a ten-year-old keeping a family running because nobody told her she didn't have to."

    s_thoughts "Silence."

    s_thoughts "Charlotte's hands are at her sides."

    s_thoughts "They're shaking."

    s_thoughts "She said it."
    
    s_thoughts "I'm so fucking proud of her."

    stop music fadeout 2.0

    jump charlotte_ch6_the_crack

    ## ===========================
    ## VARIANT 3: Low Push + High Present + "Push Charlotte"
    ## Charlotte reconciles. The Vermeer paper.
    ## ===========================

label charlotte_ch6_variant3:

    s_thoughts "I turn to Charlotte."

    s "Charlotte."

    s_thoughts "She looks at me."
    
    show charlotte happy at left

    s_thoughts "She's not shaking. She's not frozen."

    s_thoughts "She's... grounded."
    
    s_thoughts "Both feet planted firmly."

    show charlotte neutral at left

    s_thoughts "Charlotte looks at Mom. At Sophie. At the kitchen."

    s_thoughts "She sits down at the table."

    c "Mom. Can I tell you about my paper?"

    s_thoughts "Mom blinks. Her energy sputters, confused by the redirect."
    
    show mom neutral at right

    mom "Your -- what?"

    c "My Vermeer paper. The one I've been writing."

    mom "Oh -- the paintings?"

    c "Yeah. The Dutch paintings."

    s_thoughts "Charlotte's hands are on the table. Flat. Like her feet. Grounding herself."

    c "I'm writing about women in rooms. These paintings -- Vermeer painted women in domestic spaces. Kitchens. Parlors. They're pouring milk, reading letters, making lace."

    s_thoughts "Mom sits down."

    s_thoughts "The energy shifts. Not gone -- redirected. Charlotte is being interesting instead of managing, and Mom's attention follows genuine interest like water following gravity."

    c "And there's always a map on the wall. In the paintings. An actual map -- of the world, of the Dutch Empire. Hanging right there in the room."

    mom "A map?"

    c "The woman never looks at it. She's in this room and the whole world is on her wall and she doesn't see it because the room is the whole world." 
    
    c "The room has everything she needs. The room is enough."

    s_thoughts "Charlotte's voice is steady."

    s_thoughts "Academic. Controlled. Using the paper the way she uses everything -- as a tool, a frame, a structure."

    s_thoughts "But she knows she's doing it."

    s_thoughts "That's the difference."

    c "My professor asked me: 'Why don't they leave?'"

    s_thoughts "Mom is listening."

    c "And I wrote -- I wrote that they stay because the room is all they know. The room isn't bad. The room has light and warmth and work. But they built the room around themselves and it got so comfortable they stopped seeing the walls."

    s_thoughts "Charlotte looks at Mom."

    c "The cage isn't the frame. It's the moment when the frame stops being visible."
    
    show mom sad at right

    s_thoughts "Mom's face."

    s_thoughts "Not a spiral. Not guilt."

    s_thoughts "Something raw and open and terrified."

    s_thoughts "Charlotte's voice changes."

    s_thoughts "Not much. A half-step down. The academic framing wobbles."

    c "You built me a really beautiful room, Mom."

    s_thoughts "Her voice cracks on 'Mom.'"

    s_thoughts "Just for a second. A fracture in the eloquence."

    c "I -- it was warm. And safe. When it was safe. And I learned to keep it safe when you couldn't and I got so good at it I--"

    s_thoughts "She stops."

    s_thoughts "She finds the frame again."

    c "I'm finding the door."

    s_thoughts "Mom's hand goes to her mouth."

    s_thoughts "Sophie has stopped crying. She's staring at Charlotte like she's never seen her before."

    s_thoughts "Charlotte takes a breath."

    c "I'm not leaving. I'm just -- finding the door." 
    
    c "So I know it's there."

    s_thoughts "Mom reaches across the table."

    s_thoughts "Charlotte lets her."
    
    s_thoughts "I realize I'm crying, too."

    stop music fadeout 2.0

    jump charlotte_ch6_something_new

    ## ===========================
    ## VARIANT 4: Low Push + Low Present + "Confront yourself"
    ## Charlotte stops Sophia. The mask holds.
    ## ===========================

label charlotte_ch6_variant4:

    s_thoughts "I step forward."

    s "Ms. Op-- Diane. I think--"

    s_thoughts "Charlotte's hand on my arm."

    s_thoughts "Tight."

    show charlotte neutral at left

    c "Don't."

    s_thoughts "One word."

    s_thoughts "Her eyes."

    s_thoughts "Not anger. Not panic."

    s_thoughts "Warning."

    s_thoughts "The kind that says: if you do this, something breaks that I don't know how to fix."

    s_thoughts "She's not protecting Mom."

    s_thoughts "She's protecting the only structure still standing."

    s_thoughts "I stop."

    s_thoughts "My mouth closes."

    s_thoughts "Mom is still talking. Something about the kitchen curtains. The river of her energy carries her past the moment without even noticing it happened."

    s_thoughts "Sophie wipes her eyes with the back of her hand. Quick. Practiced. Like she's done it before at this exact kind of table."

    s_thoughts "Charlotte's hand is still on my arm."

    s_thoughts "She lets go."

    show charlotte happy at left

    c "Mom, should I put the kettle on?"

    mom "Oh, that would be wonderful!"

    s_thoughts "Charlotte fills the kettle."

    s_thoughts "Her back is to the room."

    s_thoughts "I can see her shoulders."

    s_thoughts "They're perfect."

    s_thoughts "Everything about her is perfect."
    
    s_thoughts "Of course."

    stop music fadeout 2.0

    if charlotte_eve > 0:
        jump charlotte_ch6_of_course
    else:
        jump charlotte_ch6_five_places

    ## ===========================
    ## VARIANT 5: High Push + "Confront yourself"
    ## Sophia starts. Mom spirals. Charlotte takes over.
    ## ===========================

label charlotte_ch6_variant5:

    s_thoughts "I step forward."

    s "Diane."

    s_thoughts "Mom looks at me. The brightness, the current of her energy, swings toward me."

    mom "Yes?"

    s "I don't think Charlotte was just being helpful."

    s_thoughts "Mom's face shifts."
    
    show mom neutral at right

    s_thoughts "The brightness wobbles."

    mom "W... What do you mean?"

    s "Charlotte was ten. She was standing on a stool because--"

    s_thoughts "Mom's face crumbles."

    s_thoughts "But not into recognition."

    s_thoughts "Into the other thing."
    
    show mom sad at right

    mom "Oh God."

    s_thoughts "Her hand goes to her chest."

    s_thoughts "'Oh God, I was -- I'm such a terrible mother." 
    
    s_thoughts "Sophie gasps for air, like she's been underwater this whole time."
    
    show mom blegh at right
    
    mom "I knew it. I always knew I was terrible. My poor babies, they should have -- someone should have -- CPS should have--'"

    s_thoughts "The room reorganizes."

    s_thoughts "I can feel it happening. Like gravity shifting. Mom's pain becomes the center and everything starts orbiting it. Sophie flinches -- the whole-body flinch of someone who's been in this orbit before."

    s_thoughts "Charlotte's guilt for making Mom feel guilty. Sophie's guilt for being the reason Charlotte stood on the stool. Mom's guilt eating all the air in the room."

    s_thoughts "Everyone taking care of everyone and no one being taken care of."

    show charlotte neutral at left

    s_thoughts "Charlotte steps forward."

    c "Mom. Stop."

    s_thoughts "Not my confrontation anymore."

    s_thoughts "Charlotte's."

    c "You're not a terrible mother."

    mom "I am, I am, I--"

    c "Stop doing that. Stop making this about how bad you feel so we all have to take care of you."

    s_thoughts "The room goes silent."
    
    show mom sad at right

    s_thoughts "Mom's mouth is open."

    s_thoughts "Charlotte is shaking. But she's standing."

    c "I love you. You got better. You did the work. But that story isn't sweet."

    s_thoughts "Mom stares at her."

    c "And I need you to stop telling it."

    s_thoughts "Silence."

    s_thoughts "Charlotte's hands are fists at her sides."

    s_thoughts "She's standing in the kitchen and she's not on a stool and she's taller than she's ever been."

    s_thoughts "She said it."

    s_thoughts "She said the thing."
    
    s_thoughts "I'm so fucking proud of her."

    stop music fadeout 2.0

    jump charlotte_ch6_the_crack

    ## ===========================
    ## VARIANT 6: High Present + "Confront yourself"
    ## Sophia starts. Charlotte interrupts. Reconciles via paper.
    ## ===========================

label charlotte_ch6_variant6:

    s_thoughts "I step forward."

    s "Diane--"

    c "Sophia."

    s_thoughts "Charlotte's voice."

    s_thoughts "Quiet. Not the warning from before. Something calmer."

    show charlotte happy at left

    c "I've got this."

    s_thoughts "She says it steady."

    s_thoughts "I look at her."

    s_thoughts "She's not shaking. She's not frozen."

    s_thoughts "She's... grounded."
    
    s_thoughts "Both feet planted firmly."

    show charlotte neutral at left

    s_thoughts "Charlotte looks at Mom. At Sophie. At the kitchen."

    s_thoughts "She sits down at the table."

    c "Mom. Can I tell you about my paper?"

    s_thoughts "Mom blinks. Her energy sputters, confused by the redirect."
    
    show mom neutral at right

    mom "Your -- what?"

    c "My Vermeer paper. The one I've been writing."

    mom "Oh -- the paintings?"

    c "Yeah. The Dutch paintings."

    s_thoughts "Charlotte's hands are on the table. Flat. Like her feet. Grounding herself."

    c "I'm writing about women in rooms. These paintings -- Vermeer painted women in domestic spaces. Kitchens. Parlors. They're pouring milk, reading letters, making lace."

    s_thoughts "Mom sits down."

    s_thoughts "The energy shifts. Not gone -- redirected. Charlotte is being interesting instead of managing, and Mom's attention follows genuine interest like water following gravity."

    c "And there's always a map on the wall. In the paintings. An actual map -- of the world, of the Dutch Empire. Hanging right there in the room."

    mom "A map?"

    c "The woman never looks at it. She's in this room and the whole world is on her wall and she doesn't see it because the room is the whole world." 
    
    c "The room has everything she needs. The room is enough."

    s_thoughts "Charlotte's voice is steady."

    s_thoughts "Academic. Controlled. Using the paper the way she uses everything -- as a tool, a frame, a structure."

    s_thoughts "But she knows she's doing it."

    s_thoughts "That's the difference."

    c "My professor asked me: 'Why don't they leave?'"

    s_thoughts "Mom is listening."

    c "And I wrote -- I wrote that they stay because the room is all they know. The room isn't bad. The room has light and warmth and work. But they built the room around themselves and it got so comfortable they stopped seeing the walls."

    s_thoughts "Charlotte looks at Mom."

    c "The cage isn't the frame. It's the moment when the frame stops being visible."
    
    show mom sad at right

    s_thoughts "Mom's face."

    s_thoughts "Not a spiral. Not guilt."

    s_thoughts "Something raw and open and terrified."

    s_thoughts "Charlotte's voice changes."

    s_thoughts "Not much. A half-step down. The academic framing wobbles."

    c "You built me a really beautiful room, Mom."

    s_thoughts "Her voice cracks on 'Mom.'"

    s_thoughts "Just for a second. A fracture in the eloquence."

    c "I -- it was warm. And safe. When it was safe. And I learned to keep it safe when you couldn't and I got so good at it I--"

    s_thoughts "She stops."

    s_thoughts "She finds the frame again."

    c "I'm finding the door."

    s_thoughts "Mom's hand goes to her mouth."

    s_thoughts "Sophie has stopped crying. She's staring at Charlotte like she's never seen her before."

    s_thoughts "Charlotte takes a breath."

    c "I'm not leaving. I'm just -- finding the door." 
    
    c "So I know it's there."

    s_thoughts "Mom reaches across the table."

    s_thoughts "Charlotte lets her."
    
    s_thoughts "I realize I'm crying, too."

    stop music fadeout 2.0

    jump charlotte_ch6_something_new

    ## ===========================
    ## ===========================
    ## ENDINGS
    ## ===========================
    ## ===========================

    ## ===========================
    ## "OF COURSE" — The Comfortable Lie
    ## ===========================

label charlotte_ch6_of_course:

    scene bg entry with Fade(1.5, 0.5, 1.5)

    play music mus_charlotte fadein 3.0

    s_thoughts "Sunday."

    s_thoughts "They leave."
    
    show mom smile at right with dissolve

    s_thoughts "Mom hugs Charlotte at the door. A long hug. The kind where Mom's hand goes to the back of Charlotte's head and holds it there."

    mom "My girl."

    show charlotte happy at left with dissolve

    c "Bye, Mom. Drive safe."

    mom "Of COURSE. Always. Call me?"

    c "Of course!"
    
    hide mom
    show sophie neutral at right with dissolve

    s_thoughts "Sophie hugs Charlotte. Brief. Fierce."

    soph "Don't be weird."

    c "Too late."

    s_thoughts "Sophie looks at me on the way out."

    s_thoughts "I can't read her expression."

    s_thoughts "Mom hugs me." 
    
    hide sophie
    show mom smile at right with dissolve    
    
    mom "Take care of my girl." 
    
    s "I will."
    
    s_thoughts "And that's it."

    s_thoughts "Nothing."

    s_thoughts "They get in the car."

    s_thoughts "Charlotte waves."

    s_thoughts "The car turns the corner."

    hide charlotte with dissolve

    ## Monday morning.

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    s_thoughts "Monday morning."

    s_thoughts "The kitchen smells like eggs."

    show charlotte happy at center with dissolve

    s_thoughts "Charlotte is at the stove. Apron. Humming."

    s_thoughts "The table is set. Flowers in the vase. The chore chart is on the fridge."

    s_thoughts "Everything is where it's supposed to be."

    c "Morning! I made omelets. The fold kind."

    s_thoughts "She turns to me."

    s_thoughts "The smile."

    s_thoughts "Full coverage. Every corner lit."

    s "They look amazing."

    c "Sit down, sit down. Coffee's fresh."

    s_thoughts "I sit down."

    s_thoughts "The omelet is perfect."

    s_thoughts "The fold is perfect."

    s_thoughts "Charlotte watches me eat."

    s_thoughts "I eat."

    c "I was thinking we could do a house dinner this week. Everyone together. I'll make the risotto again -- Mom said it was good, right? It was good?"

    s "It was great."

    show charlotte laugh at center

    c "I knew it! I want to try a new recipe too. There's this one with the butternut squash and the sage--"

    s_thoughts "She's talking."

    s_thoughts "Bright. Warm. Plans and recipes and ideas."

    s_thoughts "The kitchen sounds like the kitchen sounded the day I moved in."

    s_thoughts "Charlotte pours me more coffee without asking."

    show charlotte smile at center

    s_thoughts "We're together."

    s_thoughts "Charlotte is warm. The house is organized. The chore chart has everyone's name in a different color. The flowers are fresh."

    s_thoughts "Everything is fine."

    s_thoughts "Charlotte smiles."

    s_thoughts "And smiles."

    s_thoughts "And smiles."

    c "Of course!"

    s_thoughts "She says it to nobody."

    s_thoughts "She says it to the kitchen."

    s_thoughts "She says it because the silence lasted half a second too long and the reflex fired and 'of course' filled the space like caulk in a crack."

    s_thoughts "I eat my omelet."

    s_thoughts "It's perfect."

    stop music fadeout 4.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Of Course{/size}"

    $ persistent.ending_charlotte_of_course = True
    $ persistent.completed_charlotte_route = True
    if charlotte_eve > 0:
        $ persistent.eve_stayed_in_charlotte_route = True
    return

    ## ===========================
    ## "THE CRACK" — Seen but Shattered
    ## ===========================

label charlotte_ch6_the_crack:

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    play music mus_mourning fadein 3.0

    s_thoughts "Diane Opal is crying."
    
    show mom sad at right with dissolve

    s_thoughts "Not a guilt-spiral. Real crying. The ugly kind. Shoulders shaking. No words."
    
    show sophie neutral at left with dissolve

    s_thoughts "Sophie goes to her mother."

    s_thoughts "Sophie -- sixteen, sharp, the one who turned out okay -- goes to her mother and puts her arm around her and holds her."
    
    show charlotte sad at center with dissolve

    s_thoughts "Charlotte is standing in the kitchen."

    s_thoughts "She's not moving."

    s_thoughts "She said the thing."

    s_thoughts "There is nothing in the room that needs her to do anything anymore."
    
    s_thoughts "Sophie's handling it, now."

    s_thoughts "That might be the worst part."

    s_thoughts "Charlotte walks outside."

    hide charlotte 
    hide mom
    hide sophie
    with dissolve

    ## The porch.

    scene bg porch with Fade(1.0, 0.5, 1.0)

    s_thoughts "I follow her."

    s_thoughts "The same porch as always."

    show charlotte sad at center with dissolve

    s_thoughts "Charlotte is sitting on the steps."

    s_thoughts "I sit next to her."

    s_thoughts "She's not crying."

    s_thoughts "She's past crying. She's in the place after crying where your face doesn't know what to do with itself."

    c "I said it."

    s "You said it."

    s_thoughts "Silence."

    s_thoughts "The yard, the street, all the same as ever."

    c "She looked so small."

    s "She did."

    c "When I said 'you don't get to call it sweet.' Her face went -- it went--"

    s_thoughts "Charlotte's hands."

    s_thoughts "They're shaking. The kind that starts in the chest and works outward."

    c "She didn't know."

    s "No."

    c "She genuinely didn't know."

    s "No."

    c "All this time I thought -- I thought she was CHOOSING not to see it." 
    
    c "That she was rewriting it on PURPOSE." 
    
    c "But she just... she really thought I was a helpful kid who liked making breakfast."

    s_thoughts "Charlotte stares at her hands."

    c "I can't take it back."

    s "No."

    c "It's in the room now. The thing. It's just... sitting there. In the kitchen. Between us."

    s_thoughts "She's right."

    s_thoughts "The truth is in the kitchen like a third person. Mom is in there with it. Sophie is holding her."

    s_thoughts "Charlotte is out here."

    c "Do you still love me?"

    s "Yes."

    c "Even though I'm--"

    s "Yes."

    show charlotte vulnerable at center

    c "Even though I just -- in front of my MOM -- I just--"

    s "Charlotte. I'm so proud of you."

    c "She's going to go home and she's going to replay it and she's going to--"

    s "Yeah. She is."

    c "And it didn't fix anything."

    s "No."

    c "I thought saying it would fix something."

    s "It doesn't work like that."

    c "Then what was the POINT?"

    s_thoughts "She's looking at me."

    s_thoughts "Eyes red. Hands shaking. Face bare."

    s_thoughts "Not the mask. Not the blank."

    s_thoughts "Just... Charlotte."

    s "The point is it's true."

    c "..."

    s "And now it exists in the room."

    c "That's not enough."

    s "I know."

    s_thoughts "We sit."

    s_thoughts "Charlotte's hands are on her knees. She's gripping them."

    s_thoughts "She's not crying."

    s_thoughts "I think she might be done crying for a while."

    s_thoughts "She said the truest thing she's ever said to the person who needed to hear it and it didn't fix anything." 
    
    s_thoughts "It just made the truth exist where silence used to be."

    s_thoughts "She's sitting on the porch and she's the most naked she's ever been and I'm next to her and I don't know if she can look at me tomorrow without remembering this."

    s_thoughts "Without remembering being this seen."

    s_thoughts "Being seen and being loved aren't the same thing."

    s_thoughts "But we're on this porch."

    s_thoughts "And we're trying to be both."

    show charlotte sad at center

    c "Don't use the careful voice tomorrow."

    s "I won't."

    c "I mean it. If you check on me I'll--"

    s "I won't."

    s_thoughts "She leans. Not into me. Toward me. Like she's testing whether the lean is something she wants or something she thinks I need."

    s_thoughts "She leans."

    s_thoughts "I hold still."

    s_thoughts "Her head is on my shoulder."

    s_thoughts "Her hands are still shaking."

    s_thoughts "We sit on the porch."

    s_thoughts "Not touching. Then touching. Both present. Both shaking."

    stop music fadeout 4.0

    scene black with Fade(2.0, 1.0, 2.0)

    s_thoughts "It's the most intimate moment she's ever had."

    s_thoughts "And neither of us knows if we'll make it out the other side together."
    
    s_thoughts "But for once, just for once..."
    
    pause 2.0
    
    s_thoughts "I saw Charlotte Opal on the backstage."
    
    pause 3.5
    
    s_thoughts "I saw her step off the stool."
    
    pause 6.0

    centered "{size=+10}Ending -- The Crack{/size}"

    $ persistent.ending_charlotte_the_crack = True
    $ persistent.completed_charlotte_route = True
    if charlotte_eve > 0:
        $ persistent.eve_stayed_in_charlotte_route = True
    return

    ## ===========================
    ## "SOMETHING NEW" — The Builder
    ## ===========================

label charlotte_ch6_something_new:

    scene bg kitchen with Fade(1.0, 0.5, 1.0)

    s_thoughts "After."

    s_thoughts "Mom is quiet."

    s_thoughts "Processing."

    s_thoughts "She's sitting at the table with her hands around a mug. The tea Charlotte didn't make. Sophie made it."

    s_thoughts "Sophie made the tea."

    s_thoughts "First time Sophie has taken care of someone in this kitchen."

    s_thoughts "She put the kettle on and found the chamomile and poured it and set it in front of Mom without a word. Charlotte watched her do it."
    
    show charlotte vulnerable at left with dissolve

    s_thoughts "Charlotte's face when Sophie made the tea."

    s_thoughts "I don't have a word for it."

    ## The window.

    hide mom
    hide charlotte
    with dissolve
    
    scene bg entry with dissolve

    s_thoughts "Charlotte is standing by the window."
    
    play music mus_stillhere fadein 3.0
    
    show charlotte sad at center with dissolve

    s_thoughts "She's looking at the yard."

    s_thoughts "I stand next to her."

    s_thoughts "Grass that needs mowing. A fence with a broken slat. Nothing beautiful about it."

    c "I used the paper."

    s "Yeah."

    c "I used the paper to have the conversation."

    s "Yeah."

    c "That's still a mask."

    s "A different kind."

    show charlotte neutral at center

    c "A better kind?"

    s "A chosen kind."

    s_thoughts "Charlotte is quiet."

    c "I liked the museum."

    s "Yeah?"

    c "The woman peeling the apple."

    s "I know."

    c "I want to go back. Not for the paper. Just to look."

    s "Okay."

    c "Maybe by myself."

    s "Okay."

    s_thoughts "Charlotte looks at me."

    s_thoughts "A complicated look. Grateful and sad and something else. Something I haven't seen before."

    s_thoughts "The look of someone who can see where they're going and it isn't where they're standing."

    show charlotte sad at center

    c "You were so good to me."

    s "Were?"

    c "Are. You are good to me."

    s_thoughts "A beat."

    c "But I think I need to be good to me first. For a while."

    s "..."

    c "Not -- I'm not saying -- it's not a breakup. I'm not--"

    s_thoughts "She's fumbling."

    c "I just need -- I don't know who I am when I'm not being someone for someone." 
    
    c "And I can't figure that out while I'm being your girlfriend." 
    
    c "Because being your girlfriend is the EASIEST thing in the world and I'm so GOOD at it and--"

    s_thoughts "She stops herself."

    c "And that's the problem."

    s "You're good at it."

    c "I'm good at EVERYTHING that involves being something for someone else. That's the whole problem."

    s_thoughts "She's right."

    s_thoughts "My chest does something."

    s_thoughts "Not the complicated architectural thing. Something simpler. Something that just hurts."
    
    s_thoughts "It really fucking hurts."

    c "I need to find out what I like that isn't making someone else comfortable."

    s "The apple painting."
    
    s_thoughts "My voice is clean. Clinical."

    show charlotte smile at center

    s_thoughts "A small smile."

    c "The apple painting."

    s "The bakery novel."

    c "The bakery novel."

    s "Saying no to the store."

    c "Saying no to the store."

    s_thoughts "I'm listing the things that belong to her. The real things. The small, weird, imperfect things she found when nobody was watching."

    c "I need more of those."

    s "Yeah."

    c "And I can't find them while I'm finding you."

    s_thoughts "That one lands."

    s_thoughts "I nod."

    s_thoughts "I nod because if I open my mouth something is going to come out that isn't a word."

    show charlotte sad at center

    c "Sophia."

    s "Yeah."

    c "Thank you."

    s "For what?"

    c "For showing me the door."

    s_thoughts "She looks at me."

    s_thoughts "I look at her."

    s_thoughts "The kitchen is quiet. Mom is processing. Sophie is sitting with Mom."

    s_thoughts "Charlotte is standing at the window of a house she used to hold together and she's letting go and it hurts it hurts so much and it's right and I can't breathe and it hurts."

    show charlotte neutral at center

    c "I should go sit with them."

    s "Yeah."

    s_thoughts "She goes."
    
    hide charlotte with dissolve

    s_thoughts "I stand at the window."

    stop music fadeout 4.0

    ## ===========================
    ## SOPHIA'S HEARTBREAK — THE PORCH
    ## ===========================

    scene bg porch with Fade(2.0, 1.0, 2.0)

    s_thoughts "The porch."

    s_thoughts "I'm on the steps."

    s_thoughts "It's cold."

    s_thoughts "I'm not going inside."

    s_thoughts "I think I just got -- not dumped. Something worse than dumped. Something kinder than dumped."

    s_thoughts "Charlotte Opal looked at me with the most real face she's ever worn and said: you're so good for me that I need to stop being with you."

    s_thoughts "I helped her find the door, she said."

    s_thoughts "She walked through it."

    s_thoughts "The door doesn't lead to me."

    s_thoughts "I'm sitting on the porch and I think I might be crying? Yeah. Yeah, I'm crying. My face is wet and I didn't notice when that started."

    s_thoughts "Maybe I trapped myself inside the frame so Charlotte could leave the room."
    
    s_thoughts "I cry some more."

    s_thoughts "The door opens."

    show isabella neutral at center with dissolve
    
    play music mus_spacebetween fadein 2.0

    i "Hey."

    s_thoughts "Isabella."

    s_thoughts "She's holding two mugs. She sits down next to me."

    i "Tea. Before you ask -- no, I didn't make it. Amara made it. She told me something was going on. I'm just the delivery system."

    s_thoughts "I take the mug."

    s_thoughts "My hands are shaking."

    show isabella sad at center

    s_thoughts "Isabella doesn't say 'what happened.' She doesn't ask."

    s_thoughts "She sits."

    i "You know, when I -- when Charlotte and I were..."

    s_thoughts "She stops."

    show isabella neutral at center

    i "Never mind."

    s "No. Tell me."

    i "It's not about me."

    s "Isabella."

    show isabella sad at center

    s_thoughts "She's quiet for a second."

    i "I had this thing. Before you got here. With Charlotte."

    s "I know."

    show isabella surprised at center

    i "You KNOW?"

    s "I'm the observation girl. I observe things."

    show isabella embarrassed at center

    i "God. Was I THAT obvious?"

    s "A little."

    i "Great. Love that for me."

    s_thoughts "She drinks her tea."

    show isabella neutral at center

    i "It didn't go anywhere. Charlotte didn't -- she didn't notice. Or she noticed and she didn't want to make it weird. Classic Charlotte. 'Of course we're just friends!'"

    s_thoughts "Isabella does the voice. It's eerily good."

    i "And then you showed up and she lit up around you and I thought -- okay. That's how it goes."

    s "Isabella..."

    i "I'm not saying this to be SAD about it. I'm saying -- I know what it's like when Charlotte decides something." 
    
    i "She doesn't decide like normal people. She decides like a wall going up. Instant. Total."

    s "She decided to find herself."

    show isabella sad at center

    i "Yeah."

    s "Without me."

    i "Yeah."

    s_thoughts "We sit."

    s_thoughts "The tea is warm."

    s_thoughts "I'm crying. Isabella is sitting next to me. She smells like green apple shampoo."

    i "Wanna talk to Lumi?"

    s_thoughts "I almost laugh."

    s "What?"

    i "Lumi. She's good at 2 AM crises. Or -- 7 PM crises. Whatever time it is."

    s_thoughts "I look at Isabella."

    s_thoughts "She's offering me the thing she loves most."

    s "...Okay."

    show isabella smile at center

    s_thoughts "She pulls out her phone. Our shoulders touch."

    s_thoughts "Something starts."

    s_thoughts "Here. On this porch. While I'm crying over Charlotte with Isabella's shoulder against mine."

    s_thoughts "I don't know what it is yet."

    s_thoughts "I think that's how it starts."

    hide isabella with dissolve
    stop music fadeout 4.0

    ## ===========================
    ## CHARLOTTE'S CODA — narrator only, no s_thoughts
    ## ===========================

    scene bg entry with Fade(2.0, 1.5, 2.0)

    play music mus_charlotte fadein 4.0

    "Charlotte is at the window."

    "She's watching the porch through the glass."

    "Sophia is on the steps. Isabella is next to her. Their shoulders are touching."

    "Isabella says something. Sophia laughs. It's the surprised kind -- the kind that sneaks out before you can stop it."

    show charlotte smile at center with dissolve

    "Charlotte watches."

    "'Izzy lights up around her.'"

    "Charlotte smiles."

    "A real one."

    "A new one."

    "One she's never smiled before."

    "She whispers to the window."

    c "This'll be good. For both of them."

    "A beat."

    "She looks at the porch."

    c "Thanks, Sophia."

    "The kitchen is behind her. The postcards are upstairs."

    "The woman peeling the apple."

    c "For the map."

    hide charlotte with dissolve

    stop music fadeout 4.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Something New{/size}"

    $ persistent.ending_charlotte_something_new = True
    $ persistent.completed_charlotte_route = True
    if charlotte_eve > 0:
        $ persistent.eve_stayed_in_charlotte_route = True
    return

    ## ===========================
    ## "FIVE PLACES" — The Darkest
    ## ===========================

label charlotte_ch6_five_places:

    scene bg entry with Fade(1.0, 0.5, 1.0)

    play music mus_glass fadein 3.0

    s_thoughts "Sunday."

    s_thoughts "The visit ends badly."

    s_thoughts "Not dramatically. Badly the way things end when nobody says the thing."

    s_thoughts "Mom leaves confused. Something happened in the kitchen -- she can feel it. The energy shifted. Sophie went quiet. Charlotte went bright."

    s_thoughts "Mom doesn't know what she missed."

    s_thoughts "Sophie leaves angry."

    s_thoughts "Not at Mom. At Charlotte."

    s_thoughts "The bodyguard anger. The 'you were supposed to SAY something' anger. The sixteen-year-old who flew three hours to watch her sister have the conversation and the conversation didn't happen."

    s_thoughts "Sophie hugs Charlotte at the door."

    s_thoughts "It's short."

    s_thoughts "She doesn't look at me."

    s_thoughts "They get in the car."

    s_thoughts "Charlotte waves."

    s_thoughts "The car turns the corner."

    hide charlotte 
    hide mom
    with dissolve
    stop music fadeout 2.0

    ## Monday morning.

    scene black with Fade(1.5, 0.5, 1.5)

    s_thoughts "Monday."

    s_thoughts "5 AM."

    play music mus_wrong fadein 3.0

    scene bg kitchen night with dissolve

    s_thoughts "I can't sleep."

    s_thoughts "Something woke me. Not a sound. A feeling. The feeling of the house being occupied at an hour when it shouldn't be."

    s_thoughts "I come downstairs."

    show charlotte happy at center with dissolve

    s_thoughts "The kitchen light is on."

    s_thoughts "Charlotte is at the stove."

    s_thoughts "5 AM."

    s_thoughts "She's cooking."

    s_thoughts "Eggs. Toast. The fold omelets. The good knife is out. Julienned vegetables on the cutting board."

    s_thoughts "The table is set."

    s_thoughts "Five places."

    s_thoughts "Five forks."

    s_thoughts "Five napkins."

    s_thoughts "Five glasses."

    s_thoughts "The little vase of flowers is in the center."

    s_thoughts "Eve's chair is empty."

    s_thoughts "Eve's room is empty."

    s_thoughts "Eve left weeks ago."

    c "Good morning!"

    s_thoughts "Charlotte turns."

    s_thoughts "The smile."

    s_thoughts "Full. Wattage."

    c "Sit down. I made everything."

    s_thoughts "I look at the table."

    s "Charlotte."

    c "Omelets. The fold kind. I used the last of the gruyère but I can go to the store later--"

    s "Charlotte."

    c "And I made coffee. The French press. I know you like--"

    s "Charlotte, there's only four of us."

    s_thoughts "Charlotte stops."

    s_thoughts "She looks at the table."

    show charlotte surprised at center

    s_thoughts "She counts."

    s_thoughts "Her lips move."

    s_thoughts "One. Two. Three. Four. Five."

    s_thoughts "Her lips move."

    show charlotte smile at center

    c "...Of course."

    s_thoughts "She goes to the fifth place."

    s_thoughts "She picks up the fork. The napkin. The glass."

    s_thoughts "She puts them in the cabinet."

    s_thoughts "She doesn't slam. She doesn't cry. She just puts them away."

    s_thoughts "She sits down."

    c "Four! Obviously. Four places."

    s_thoughts "She's smiling."

    s_thoughts "I sit down."

    s_thoughts "The omelet is perfect."

    s_thoughts "I don't eat it."

    s_thoughts "Isabella comes down at seven. She grabs a granola bar and goes to her room."

    s_thoughts "'Morning, Charlotte!' she calls from the stairs."

    c "Morning!"

    s_thoughts "Amara is out, somewhere, doing something. No clue what."

    s_thoughts "Isabella eats in her room."

    s_thoughts "It's 7:30."
    
    s_thoughts "I'm standing in the doorway."

    s_thoughts "I can see her."

    s_thoughts "Charlotte is sitting at the table."

    s_thoughts "Four places. Three omelets getting cold."

    s_thoughts "She's not eating."

    s_thoughts "She's sitting at a table with five chairs and only one girl."

    show charlotte happy at center

    s_thoughts "Her hands are in her lap."

    s_thoughts "The mask is on."

    s_thoughts "Nobody else is looking at her."

    s_thoughts "The mask is still on."

    s_thoughts "The morning light from the left window."

    s_thoughts "Charlotte at the table. Hands folded. Smile held. Food untouched."

    s_thoughts "Five forks for four people."

    s_thoughts "Five is the number her hands know."

    s_thoughts "Five is the number that means she did her job."
    
    pause 1.0

    s_thoughts "Charlotte Opal is sitting at a kitchen table." 
    
    pause 1.5
    
    s_thoughts "She set that table for a person who is never coming back." 
    
    pause 2.5
    
    s_thoughts "And she can't stop setting it." 
    
    pause 3.0
    
    s_thoughts "I look at our stool, tucked away under a counter."
    
    pause 4.0
    
    s_thoughts "...'I'm still standing on the stool.'"
    
    pause 1.5

    stop music fadeout 5.0

    scene black with Fade(2.0, 1.0, 2.0)

    s_thoughts "She looks like a Vermeer painting."
    
    pause 6.0

    centered "{size=+10}Ending -- Five Places{/size}"

    $ persistent.ending_charlotte_five_places = True
    $ persistent.completed_charlotte_route = True
    if charlotte_eve > 0:
        $ persistent.eve_stayed_in_charlotte_route = True
    return


## ===========================================================
## GLASS HOUSES ENDING -- STOOL
## Gated: all four routes complete + charlotte_push >= 6
##        + charlotte_present >= 10 + charlotte_eve > 0
## ===========================================================

label charlotte_ch6_stool:

    # Room state carries over from the helper-gal trigger:
    # Mom still beaming, Sophie still crying, Charlotte still
    # standing very still. The music has just stopped.

    scene bg kitchen
    show charlotte sad at left
    show mom smile at right
    show sophie sad at center
    with dissolve

    s_thoughts "Mom is still talking. I don't know what she's saying anymore."

    s_thoughts "Sophie is still crying. Small. Not wanting to be noticed."

    s_thoughts "Charlotte is still standing very still."

    pause 2.0

    s_thoughts "I'm looking at the stool."

    s_thoughts "The wooden one. The one with the step."

    s_thoughts "It's shoved under the counter by the fridge. It's been there all weekend. Nobody has used it. Nobody needs to reach the top shelf."

    pause 1.5

    s_thoughts "I don't think about it. I just walk."

    hide sophie
    with dissolve

    s_thoughts "Past Charlotte. Past the table."

    s_thoughts "I pull the stool out from under the counter."

    s_thoughts "It's heavier than it looks."

    pause 1.0

    s_thoughts "Mom has stopped talking."

    s_thoughts "I don't know when she stopped. I think I missed the exact moment."

    show mom neutral at right

    mom "Sophia...?"

    s_thoughts "I don't answer her."

    s_thoughts "I carry the stool to the middle of the kitchen floor and put it down."

    s_thoughts "It wobbles for a second on the tile. Then it settles."

    pause 2.0

    s_thoughts "I get on it."
    
    stop music fadeout 2.0

    pause 2.0

    play music mus_mourning fadein 4.0

    s_thoughts "I'm taller than everyone. That's the first thing. I'm taller than Mom and I'm taller than Sophie and I'm taller than Charlotte and it's the stupidest physical fact in the world and it's the only thing I can think about for a full second."

    s_thoughts "I can see the top of the fridge. There's dust."

    s_thoughts "Okay."

    s_thoughts "Okay, Sophia."

    pause 2.0

    s "My dad left when I was twelve."

    pause 3.0

    s_thoughts "Mom's mouth is open a little."

    s_thoughts "Sophie has stopped crying. Or she's crying in a different way now. I can't tell."

    s_thoughts "Charlotte isn't looking at me."

    s_thoughts "Charlotte is looking at the stool."

    pause 2.0

    s "Sorry. I know this is -- I know I'm standing on a stool and saying this. I know this is weird."

    s "I need to stand on it for a second. I'll explain."

    pause 1.5

    s "My dad left when I was twelve. I have a little sister. Jenny. She was six."

    s_thoughts "My voice is going flat. The thing it does when I'm saying the truth from a distance."

    s "He didn't fight with my mom. He didn't yell. He just wasn't there one day."

    pause 1.5

    s "And I spent the next -- I spent the next eight years watching."

    s "Every room I walk into. I check it. I map it. I clock who's upset and who's lying and who's about to leave."

    s "I thought I was being careful. I thought I was paying attention because I loved people."

    pause 2.0

    s "I was paying attention because I was afraid."

    pause 2.5

    show mom sad at right

    s "And Jenny -- after he left -- Jenny used to be scared of thunder. And I was the one who carried her to the window to count the seconds."

    s "Twelve years old. Carrying a six year old to a window."

    pause 2.0

    s_thoughts "I look at Sophie."

    s "Sophie."
    
    show sophie sad at center with dissolve

    s_thoughts "Her face comes up."

    s "I know -- I don't -- I don't know you. Sorry."

    s "But I know Jenny. And I think Jenny and you might -- I think you both had a big sister... like that."

    pause 2.5

    s_thoughts "Sophie's face."

    s_thoughts "Sophie's face is doing something I don't have a word for."
    
    hide sophie with dissolve

    pause 2.0

    s "Mrs. Opal."

    show mom sad at right

    s "Mrs. Opal, I -- I'm sorry for standing on a stool and dumping all this out of nowhere, but..."

    s "I need to say a thing. And I need to say it from up here because if I say it from down there it'll come out wrong."

    pause 2.5

    s "My dad couldn't be there. He left."

    s "You couldn't be there. You were -- you were in bed. And I know you've been working on that. I know the medication and the -- I know. Charlotte has told me. A little. Not in a way that blames you. In a way that loves you."

    pause 2.0

    s "We're... we're not shaped so different. Me and Charlotte."
    
    s "We both... we both watch. Just in different ways."

    pause 3.0

    s_thoughts "I don't know if that landed. My mouth is dry."

    s "My dad's absence built me. I watch for the leaving. I file people because I'm afraid they'll disappear."

    pause 2.0

    s "Your absence built Charlotte."

    s "She watched for what needed doing. She watched Sophie. She stood on the stool --"

    s_thoughts "I point down. Stupid. But I point down."

    s "-- on the stool, when she was ten, because somebody needed to make breakfast and you were asleep and Sophie was hungry and she was the oldest person in the room."

    pause 2.5

    show mom blegh at right
    with dissolve

    s_thoughts "Mom's hand has come up to her mouth."

    s_thoughts "She's not crying. She's listening."

    s_thoughts "I promised myself I would not stop if she started listening. Because listening is the scariest part."

    pause 2.0

    s "I'm not telling you this to hurt you. I'm telling you this because Charlotte loves you and you love Charlotte and you are more alike than either of you know and neither of you has the whole picture."

    s "You remember a little girl who was born helpful. She remembers a little girl who was ten years old and scared."

    s "Both of those girls were real. They were the same girl. You just have different pieces of her."

    pause 3.0

    s "And I'm up here on this stool because -- because I think Charlotte needs someone to be up here first."

    s_thoughts "My legs are shaking a little. I think it's the stool. I think it's me."
    
    stop music fadeout 2.0

    s "That's all. That's the thing."

    pause 3.0

    s_thoughts "I don't know what I'm supposed to do next. I said the thing. I'm on a stool."

    s_thoughts "There's supposed to be a next part."

    pause 2.0

    s_thoughts "Charlotte is moving."

    show charlotte neutral at left

    s_thoughts "She's walking toward me."

    s_thoughts "Slow. Like she's walking through water."

    pause 1.5

    s_thoughts "She stops at the stool."

    s_thoughts "She looks up at me."

    pause 2.0

    c "Can I--"

    s "Of course."

    pause 1.0

    s_thoughts "She doesn't ask me to get down."

    s_thoughts "She steps up."

    pause 2.5

    s_thoughts "We are both on the stool."

    s_thoughts "It wasn't made for two people. Our feet are overlapping. My hip is against her hip. Her shoulder is under my chin. I can feel her breathing."

    s_thoughts "Neither of us moves."

    pause 3.0

    s_thoughts "Charlotte's hand finds mine. Not holding. Just there."

    s_thoughts "Charlotte's hand is on my hand."

    pause 2.0

    s_thoughts "And I understand what I came up here for."

    s_thoughts "I didn't come up here to give a speech. I came up here to warm the stool up."

    s_thoughts "I step down."

    hide charlotte
    show charlotte neutral at center
    with dissolve

    pause 2.0

    s_thoughts "Charlotte is alone on the stool now."

    s_thoughts "She's taller than everyone. Mom is looking up at her. Sophie is looking up at her. I'm looking up at her."

    s_thoughts "She's never been looked at this way in her life."

    pause 3.0

    s_thoughts "She opens her mouth."

    s_thoughts "Nothing comes out."

    pause 2.0

    show charlotte embarrassed at center

    c "Um."

    pause 1.5

    c "Okay."

    c "I don't -- I have not -- okay."

    pause 2.0

    c "I didn't know I was going to do this."

    c "I don't know what I'm going to say. I'm just going to say things and hopefully some of them will be -- hopefully some of them will be the ones."
    
    play music mus_charlotte fadein 2.0

    pause 2.0

    c "Mom."

    show mom sad at right

    c "I love you. That's the -- that's the first thing. I need that to be the first thing or I won't -- I won't get the rest out."

    c "I love you and I know you love me and I have known that my whole life and I have never not known it."

    pause 1.5

    c "The stool."

    c "I was -- I was ten. And Sophie was five. And you were--"

    c "You were sick. I didn't have a word for it then. I have a word for it now. I have a lot of words for it now. I took a class."

    show charlotte smile at center

    s_thoughts "She laughed. It's almost a laugh. It's the snort. She surprises herself with it, every time."

    show charlotte neutral at center

    c "I took a class about it. Because I thought if I understood it I would -- I don't know what I thought. I thought I'd feel better and I didn't and then I took another class."

    pause 1.5

    c "Sophie was hungry."

    c "That's -- that's actually the whole thing. Sophie was hungry and nobody was going to feed her. And I was the oldest person who was -- who was up. And I knew where the eggs were."

    c "So I got on the stool."

    pause 2.0

    c "And I kept getting on the stool. Because once you know how to make eggs for a five year old, you don't -- you can't unknow it. You can't walk back into a room where a five year old is hungry and pretend you don't know how."

    pause 2.5

    c "And you --"

    show mom blegh at right

    c "You remembered it wrong. I know you remembered it wrong. I've known for years that you remembered it wrong."

    c "You remembered it as a sweet thing. As your little girl who was born helpful. And I didn't -- I never corrected you. Because correcting you would have -- "

    c "Because if I corrected you I would have had to say out loud that I wasn't born helpful. I was made helpful. And I wasn't ready to say that out loud."

    pause 2.5

    c "I'm not -- Mom, I'm not mad at you. I want to say that because it's true and because I can see your face and you're -- you're waiting for me to be mad."

    c "I'm not mad."

    c "I just -- "

    pause 2.0

    show charlotte vulnerable at center

    c "I just need you to know that the little helper gal was a real person. She was a scared ten year old. And she did a good job. She -- "

    c "She did a really good job."

    pause 3.0

    s_thoughts "Charlotte is crying. Not a lot. The quiet kind."

    s_thoughts "Mom is crying too. Not the guilt kind. Something else."

    pause 2.0

    show charlotte neutral at center
    
    c "And here's the part I didn't know until about thirty seconds ago."

    c "I don't want to stop."

    pause 1.5

    c "I don't want to stop making breakfast. I don't want to stop knowing where the eggs are. I don't want to stop being the person who -- "

    c "I like being the person who knows where things are. I like the kitchen. I like the -- I like the doing."

    pause 2.0

    c "I thought -- I think I thought this whole year was about learning how to not be that person anymore. Sophia kept -- "

    c "Sophia kept telling me I didn't have to. And that was -- that was the right thing to tell me. I needed to hear that."

    c "But the answer isn't that I'm going to stop."

    pause 2.5

    c "The answer is that I get to choose it now."

    c "Which is -- I mean that's not -- that's not some big revelation. That sounds like a fridge magnet."

    show charlotte smile at center

    c "Oh god it sounds like a fridge magnet. I'm up on a stool saying fridge magnet things."

    pause 1.5

    show charlotte neutral at center

    c "But it's -- it's different from the inside. I promise. It's different from the inside."

    pause 2.0

    c "I was going to -- I was going to say something and then I lost it. What was I --"

    c "Oh."

    pause 2.0

    c "Of course."

    pause 3.0

    s_thoughts "She says it like she's surprised to hear it come out of her mouth."

    pause 1.5

    c "Of course."

    c "I -- huh."

    c "That's what it means. I've been saying it my whole life and I didn't -- I didn't know what it meant until just now."

    pause 2.0

    c "Of course I was the helper gal. Of course I stood on the stool. Of course I learned where the eggs were."

    c "And of course -- "

    pause 1.5

    c "Of course I'm going to keep doing it."

    c "Not because I have to. Because I want to. Because it's mine."

    c "I'm not going to stop."

    c "I'm just -- I'm going to start knowing I'm doing it."

    pause 3.0

    s_thoughts "Charlotte looks down at me."

    s_thoughts "I didn't realize she was going to end it by looking at me."

    pause 2.0

    c "And the girl who helped me get up here."

    s_thoughts "That's me. I'm the girl--"

    s_thoughts "Shut up, Sophia. She's talking."

    pause 1.0

    c "I choose her too."

    c "She got on a stool for me. Nobody has ever done that for me before. Not literally. Not -- I don't even know if anyone's ever done it metaphorically, either. I think she might be the first."

    pause 2.5

    c "Okay."

    c "Okay, I'm -- I'm getting down. I don't know how to end a thing like this. I've never ended a thing like this before."

    show charlotte smile at center

    c "I guess you just -- step off."

    pause 2.0

    s_thoughts "She steps off."

    show charlotte neutral at left with dissolve

    stop music fadeout 4.0

    pause 3.0

    s_thoughts "The kitchen is very quiet."

    s_thoughts "Mom is -- Mom is just standing there with her hand over her mouth. Not crying anymore. Not talking. Just standing there."

    s_thoughts "Sophie is -- "

    show sophie smile at right
    with dissolve

    soph "Since when are you the smart one?"

    pause 1.5

    c "Shut up."

    pause 1.0

    soph "Seriously."

    c "Shut UP."

    pause 2.0

    s_thoughts "Charlotte is laughing. Wet. The snort."

    s_thoughts "Sophie is almost laughing."

    s_thoughts "Mom is -- Mom takes two steps and wraps her arms around Charlotte without saying anything."

    show mom smile at right
    with dissolve

    s_thoughts "Charlotte lets her."

    s_thoughts "That's the whole scene. Mom holding Charlotte. Charlotte letting her. No words. No apology. No 'I'm sorry for the years in bed.' Just the hug and the letting."

    pause 4.0

    s_thoughts "Sophie comes over. Sophie hugs both of them."

    s_thoughts "I'm standing at the counter next to an empty stool."

    s_thoughts "I don't know where to put my hands."

    pause 4.0

    s_thoughts "After a while -- I don't know how long -- Charlotte steps out of the hug."

    s_thoughts "She says something quiet to her mom. I don't hear it."

    s_thoughts "Mom nods. Mom sits down at the table. Sophie sits down next to her."

    s_thoughts "Charlotte walks over to me."

    hide mom
    hide sophie
    show charlotte neutral at center
    with dissolve

    pause 3.0

    c "Hi."

    pause 1.5

    s "Hi."

    pause 2.0

    c "I'm Charlotte."

    pause 2.0

    s "...I know."

    pause 2.0

    show charlotte smile at center

    c "No."

    c "I just figured that out."

    pause 4.0

    s_thoughts "Oh."

    pause 3.0

    s_thoughts "I don't say anything. Because I don't have anything that covers this."

    s_thoughts "I just look at her."

    s_thoughts "And she looks back."

    s_thoughts "And neither of us has to do anything with it."

    pause 3.0

    scene bg kitchen with Fade(2.5, 2.0, 2.5)
    show charlotte happy at center

    play music mus_sunlight fadein 4.0

    s_thoughts "I come downstairs."

    s_thoughts "The kitchen smells like butter."

    pause 1.5

    s_thoughts "Charlotte is at the stove."

    s_thoughts "Spatula. Pan. The muscle memory she's had her whole life."

    s_thoughts "The stool is back under the counter by the fridge. She doesn't need it to reach the stove. She never did. The stool was for when she was ten."

    pause 2.0

    s_thoughts "The table is set."

    s_thoughts "Five places."

    pause 2.5

    s_thoughts "I count them. I don't know why I count them. I do."

    s_thoughts "One. Two. Three. Four. Five."

    s_thoughts "Me. Charlotte. Isabella. Amara. Eve."

    pause 2.0

    s_thoughts "Eve's place is set. Napkin folded. Fork on the left. Same as everyone else's."

    s_thoughts "Eve has not come downstairs yet. Eve might not come downstairs for a while."

    s_thoughts "Charlotte set her place anyway."

    pause 3.0

    s_thoughts "Mom and Sophie left late last night. Charlotte walked them to the car. I stayed in the kitchen because I didn't know if I was supposed to be there for the goodbye."

    s_thoughts "Charlotte came back in and asked me to stay up with her for an hour. We didn't talk much. She drank a glass of water and I drank a glass of water and we sat at the table and that was enough."

    pause 2.0

    s_thoughts "I didn't ask her if she was going to make breakfast this morning. I didn't ask anyone."

    s_thoughts "Nobody asked her."

    s_thoughts "She wanted to."

    c "Morning."

    s "Morning."

    s_thoughts "She doesn't turn around. The eggs are at the delicate stage."

    pause 2.0

    s_thoughts "I walk across the kitchen. Slow."

    s_thoughts "I stop behind her."

    s_thoughts "I can see over her shoulder. She's making the fold kind. The kind where you tilt the pan and run the spatula under the edge and it comes up as a single thin sheet. I've never been able to make them that way. I've watched her do it three times and I've never understood."

    pause 2.0

    s_thoughts "I put a hand on her hip."

    s_thoughts "Not grabby. Just there. The way her hand was on mine on the stool."
    
    s_thoughts "She doesn't flinch. She doesn't 'of course.' She doesn't laugh it off."

    s_thoughts "She just -- leans back. A quarter inch. Into my hand."

    pause 2.0

    s_thoughts "I lean forward and kiss the side of her neck."

    s_thoughts "The soft place right under the ear where her hair is pinned up."

    pause 3.0

    show charlotte happy at center

    s_thoughts "She keeps working the pan."

    s_thoughts "That's the part I want to remember. Not the kiss. The part where she keeps working the pan."

    pause 2.0

    c "Hey."

    s "Hey."

    pause 1.5

    c "Eggs are at the fold."

    s "Go fold them."

    pause 1.0

    s_thoughts "She folds them. The wrist thing I've never understood. The pan tilts and the sheet comes up and settles."

    s_thoughts "My hand is still on her hip."

    pause 2.0

    c "I like that."

    s "Folding eggs?"

    show charlotte smile at center

    c "The other thing."

    pause 1.5

    s "Oh. Yeah. Me too."

    c "You can keep doing it."

    s "While you cook?"

    c "Mm-hm."

    s "Is that -- is that okay? I don't want to -- "

    c "Sophia."

    s "Yeah."

    c "It's okay."

    pause 1.0

    c "I can do two things."

    pause 3.0

    s_thoughts "Oh."

    s_thoughts "...She can do two things."

    pause 2.0

    s_thoughts "I kiss the place under her ear again. Slower this time."

    s_thoughts "She makes a small sound. A small, unguarded sound that I don't think she's made before in front of me."

    pause 2.0

    s_thoughts "She plates the first egg. Then the second. Then the third."

    s_thoughts "She reaches for the fourth plate."

    s_thoughts "Mine."

    pause 2.0

    s_thoughts "Then the fifth."

    s_thoughts "Eve's."

    s_thoughts "She sets it at Eve's place. Not with a flourish. Not with a sigh. Just -- sets it. Like it's the same as the other four."

    pause 3.0

    c "It'll go cold if she doesn't come down."

    s "Yeah."

    c "That's okay."

    pause 1.5

    c "I'll make her a fresh one when she does."

    pause 2.0

    s_thoughts "I look at her."

    s_thoughts "She's not performing it. She's not saying it to be the helper. She's saying it because it's true. Because if Eve comes down in an hour and the eggs are cold, Charlotte will make her a new one, and nobody will have asked her to."

    s_thoughts "Because this is the shape of how Charlotte loves people."

    s_thoughts "Because she chose it. On a stool. Last night."

    pause 3.0

    s "Charlotte."

    c "Yeah?"

    pause 2.0

    s "I love you."

    pause 2.5

    s_thoughts "She turns her head a little. Her cheek against my temple."

    pause 2.0

    c "I love you too. Of course."

    pause 2.5

    s_thoughts "She goes back to the pan."

    s_thoughts "I keep my hand on her hip."

    s_thoughts "The kitchen smells like butter and morning."

    s_thoughts "The table is set for five."

    s_thoughts "Nobody asked her to."

    pause 2.0

    s_thoughts "She wanted to."

    pause 3.0

    stop music fadeout 5.0

    pause 3.0

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Stool{/size}"

    $ persistent.gh_seen_charlotte = True
    $ persistent.completed_charlotte_route = True
    if charlotte_eve > 0:
        $ persistent.eve_stayed_in_charlotte_route = True

    return
