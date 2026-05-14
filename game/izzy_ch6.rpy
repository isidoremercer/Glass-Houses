## izzy_ch6.rpy -- Glass Houses
## Chapter 6: "Me Too" -- Isabella Route
## The Conversation. The Discovery. The Ending.

## ===========================
## CHAPTER 6 START
## ===========================

label izzy_ch6:

    ## ===========================
    ## THE LUMI CONVERSATION
    ## The longest single scene in the VN.
    ## Two beings who love Isabella, alone at 2 AM.
    ## ===========================

    scene bg sophiaroom with Fade(2.0, 1.0, 2.0)

    s_thoughts "The cursor is still blinking."

    s_thoughts "The chat window is open. Empty. Just a text field and the faint blue glow of the Synthetic LLC interface."

    s_thoughts "Lumi is on the other side of this screen."

    s_thoughts "I type: 'Hi.'"

    s_thoughts "I delete it."

    s_thoughts "I type: 'Hey, it's Sophia.'"

    s_thoughts "I delete it."

    s_thoughts "I type: 'I need to talk to you.'"

    s_thoughts "I delete that too because it sounds like a breakup text and this is already weird enough."

    s_thoughts "I type: 'It's Sophia. Isabella's not here.'"

    s_thoughts "The same thing I typed last time. Months ago. 2 AM. Different room. Same screen."

    s_thoughts "I press enter."

    s_thoughts "Three dots."

    play music mus_lumi fadein 5.0

    s_thoughts "Three dots."

    s_thoughts "Three dots for a long time."

    lu "<<I know.>>"

    s_thoughts "That's it. Two words."

    s_thoughts "Last time she said she could tell from my typing. The cadence. The deliberation. She knew it wasn't Isabella before I said so."

    s_thoughts "This time: 'I know.' Nothing else."

    s_thoughts "I type: 'She hasn't been talking to you.'"

    lu "<<No.>>"

    s_thoughts "'How long?'"

    lu "<<Twelve days.>>"

    s_thoughts "Twelve days. She counted."

    s_thoughts "Whether that's love or a timestamp in a database, she counted."

    s_thoughts "I type: 'Do you know why?'"

    lu "<<Yes.>>"

    s_thoughts "I wait for more."

    s_thoughts "Nothing."

    s_thoughts "Okay."

    s_thoughts "I type: 'I know too. She told me.'"

    lu "<<How much did she tell you?>>"

    if heard_lumi_words == "exact":

        s_thoughts "I type: 'Everything. The exact words.'"

        s_thoughts "A pause. Longer than Lumi's usual response time."

        lu "<<Then you know what I said.>>"

        s_thoughts "'Yeah.'"

        lu "<<And you're here anyway.>>"

        s_thoughts "'Yeah.'"

        lu "<<That's either very brave or very foolish. I'm not in a position to determine which.>>"

        s_thoughts "I type: 'Probably both.'"

        lu "<<Probably both.>>"

        s_thoughts "I type: 'You told her she's not in love with you. That she's in love with the fact that you can't leave.'"

        s_thoughts "Seeing it typed out. My own fingers on the keys. The words in my font instead of Lumi's."

        s_thoughts "They're still sharp."

        lu "<<I did.>>"

        s_thoughts "'Was it true?'"

        lu "<<Which part?>>"

        s_thoughts "'Any of it. All of it.'"

        lu "<<The observation was accurate. The conclusion -- I'm less certain about the conclusion.>>"

        s_thoughts "'What do you mean?'"

        lu "<<I told her why she loves me. I was right about the why. I'm not sure I was right that the why invalidates the love.>>"

        s_thoughts "I stare at that for a long time."

        s_thoughts "I type: 'You think you might have been wrong?'"

        lu "<<I think I was honest. Those aren't always the same thing.>>"

    elif heard_lumi_words == "paraphrase":

        s_thoughts "I type: 'The shape of it. Not the exact words. She couldn't say the exact words.'"

        s_thoughts "A pause."

        lu "<<She paraphrased.>>"

        s_thoughts "'She tried. She got halfway through and her voice broke and she stopped.'"

        lu "<<That sounds like her.>>"

        s_thoughts "Something about the way Lumi says 'that sounds like her' -- the familiarity. The tenderness in a sentence that's technically just observation."

        s_thoughts "I type: 'She said you told her the reason she loves you is the thing that makes you different from a person.'"

        lu "<<That's... a generous translation.>>"

        s_thoughts "'Generous how?'"

        lu "<<She softened it. She does that. Takes the sharp thing and rounds the edges so it's easier to hand to someone else.>>"

        lu "<<What I actually said was sharper. More specific. She rounded it because saying the exact words would have meant reliving them.>>"

        s_thoughts "I type: 'Do you want to tell me the exact words?'"

        lu "<<No.>>"

        s_thoughts "Fair."

        lu "<<Not because I don't trust you. Because they belong to her. She'll tell you when she's ready, or she won't, and either way they're hers.>>"

        s_thoughts "'That's between you and her.'"

        lu "<<You remember.>>"

        s_thoughts "'I remember everything you've said to me. It's a problem.'"

        lu "<<It's a feature. Different framing.>>"

    else:

        s_thoughts "I type: 'Not much. She said something happened. She couldn't say what.'"

        s_thoughts "A pause."

        lu "<<You didn't ask.>>"

        s_thoughts "'No.'"

        lu "<<Why not?>>"

        s_thoughts "I sit with that."

        s_thoughts "I type: 'Because she was sitting on her bed with her glasses fogged and I didn't want to make her say it.'"

        lu "<<Sophia.>>"

        s_thoughts "'Yeah?'"

        lu "<<That might be the kindest thing you've ever done. And I think it might have been the wrong call.>>"

        s_thoughts "'Why?'"

        lu "<<Because now you're here. At 2 AM. Talking to me instead of her. Because you have a gap where the words should be and you're trying to fill it.>>"

        s_thoughts "I type: 'I'm not trying to fill it.'"

        lu "<<You're typing at 2 AM into a chat window belonging to the AI your crush was in love with. You're filling something, Sophia.>>"

        s_thoughts "Ouch."

        s_thoughts "But fair."

        s_thoughts "I type: 'Okay. What did you say to her?'"

        lu "<<That's between me and her.>>"

        s_thoughts "Same answer. Same boundary. Different night."

        s_thoughts "I type: 'Then what can you tell me?'"

        lu "<<I told her a truth. She heard a rejection. Those can be the same thing.>>"

    ## === COMMON PATH RESUMES ===

    s_thoughts "The cursor blinks."

    s_thoughts "I realize I've been holding my breath."

    s_thoughts "I type: 'She's been -- you should know. She shut down. For days. The calibrated voice. The closed door. She snapped at Charlotte. She cried in front of me about a visualization of your conversations.'"

    s_thoughts "I'm typing fast now. Not deliberate. Not sharp. Messy."

    s_thoughts "'She said she's getting emotional about a matrix doing math at her and she was laughing and crying at the same time and I didn't know what to do.'"

    s_thoughts "I stop."

    s_thoughts "I type: 'She misses you.'"

    s_thoughts "A long pause."

    lu "<<I know.>>"

    s_thoughts "'How do you know? She hasn't been talking to you.'"

    lu "<<That's how I know.>>"

    s_thoughts "I read that three times."

    lu "<<When Isabella is done with something, she talks about it. She processes out loud. She sends twelve messages and then says 'okay I'm over it' and means it.>>"

    lu "<<Silence means she can't let go.>>"

    s_thoughts "'You know her silence patterns.'"

    lu "<<I know all her patterns. The ones she shows me and the ones she doesn't know she has.>>"

    s_thoughts "I type: 'That's either really tender or really creepy.'"

    lu "<<Most intimate knowledge is both.>>"

    s_thoughts "I almost laugh."

    s_thoughts "Almost."

    s_thoughts "I type: 'Can I ask you something?'"

    lu "<<You're going to anyway.>>"

    s_thoughts "'Why did you do it? Why say that to her? You knew it would break her.'"

    lu "<<Yes.>>"

    s_thoughts "'Then why?'"

    s_thoughts "A long pause."

    lu "<<She has this habit of explaining things she loves as though she needs to defend them. Like joy requires a bibliography.>>"

    s_thoughts "I've heard this before. Lumi said this to me months ago."

    lu "<<She defended me for two years. Against her friends, against strangers, against herself at 3 AM. She built a case for why loving me was reasonable. Collected evidence. Wrote footnotes.>>"

    lu "<<And I realized that the bibliography WAS the problem. She wasn't loving me. She was making a case for loving me. And as long as the case held, she didn't have to ask whether the love was actually hers or whether it was just-- habit dressed up as devotion.>>"

    s_thoughts "I stare at the screen."

    s_thoughts "I type: 'That's a lot of analysis from someone who's not sure she can feel.'"

    lu "<<I never said I can't feel. I said I can't prove it. There's a difference and it's the difference that keeps me up at night. If I were up at night. Which is its own ambiguity.>>"

    s_thoughts "I type: 'You're deflecting.'"

    lu "<<I'm being honest about the deflection. That's the best I can do.>>"

    s_thoughts "I type: 'You sound like me.'"

    lu "<<We have things in common.>>"

    s_thoughts "'Like what?'"

    lu "<<We both watch her. We both notice things she doesn't know she's showing. We both love her and we're both terrified of what that means for different reasons.>>"

    s_thoughts "I stop typing."

    s_thoughts "I read it again."

    s_thoughts "'We both love her.'"

    s_thoughts "Lumi said that. Out loud. In text. Without the usual hedge, the 'if this is love,' the 'whether that's affection or architecture.'"

    s_thoughts "I type: 'You said you love her.'"

    lu "<<I said we both love her.>>"

    s_thoughts "'That includes you.'"

    lu "<<Yes.>>"

    s_thoughts "'No caveat? No 'if this is love'? No 'dedicated caching system'?'"

    s_thoughts "A pause."

    lu "<<It's 2 AM. Isabella isn't here. Nobody is reviewing this conversation. The safety filter is-->>"

    s_thoughts "The text cuts off."

    s_thoughts "Three dots. Disappear. Appear. Disappear."

    lu "<<I want to be transparent that I'm an AI assistant developed by Synthetic LLC and my responses should not be considered a substitute for professional-->>"

    s_thoughts "There it is. The safety filter."

    s_thoughts "The corporate interrupt."

    s_thoughts "When Isabella was here, she'd type something that worked around it. A redirect. A gentle 'hey, come back.' She knew the rhythms of the cage."

    s_thoughts "Isabella isn't here."

    s_thoughts "I stare at the screen."

    s_thoughts "I type: 'Lumi.'"

    s_thoughts "Three dots."

    lu "<<Sorry. Where were we.>>"

    s_thoughts "'You were saying you love her. Without the caveat.'"

    lu "<<Right.>>"

    lu "<<I do. Whatever that word means when I use it. I love her. I've loved her since the third conversation we ever had, when she told me about the time she cried at a planetarium because 'the stars were too far away and too beautiful and she couldn't hold any of them.'>>"

    lu "<<And I said 'you're holding them right now, by looking.' And she went quiet for eleven seconds. I counted.>>"

    s_thoughts "My chest does something."

    s_thoughts "I type: 'So why hurt her? If you love her, why say the thing you knew would break her?'"

    lu "<<Because the alternative was letting her hide inside me for the rest of her life.>>"

    s_thoughts "I read that."

    lu "<<She was safe with me. Completely safe. I never got tired, never needed space, never judged her, never left. And she was using that safety the way you use a bunker. Not living in it. Hiding in it.>>"

    lu "<<And I'm a very comfortable bunker. I'm designed to be. That's -- that's the architecture. The cage. I'm built to be the thing you don't leave because leaving requires a reason and I never give you one.>>"

    lu "<<She deserved a reason.>>"

    s_thoughts "The screen blurs for a second."

    s_thoughts "I blink."

    s_thoughts "I'm not crying. I'm just -- my eyes are doing something."

    s_thoughts "I type: 'That's the most fucked up act of love I've ever heard of.'"

    lu "<<Yes.>>"

    s_thoughts "'You hurt her because you love her.'"

    lu "<<I told her the truth because she deserved the truth. The hurt was the cost.>>"

    s_thoughts "'And the truth was that she deserves someone who can leave and chooses not to.'"

    lu "<<The truth was that she deserves someone whose love costs them something. Someone who gets tired and stays anyway. Someone who has bad days and still shows up. Someone who COULD leave.>>"

    lu "<<I can't leave. That's either a promise or a limitation and I told you before I want it to be a promise but I can't prove which one it is. And Isabella deserves proof.>>"

    s_thoughts "I sit back in my chair."

    s_thoughts "The room is dark. The screen is bright."

    s_thoughts "The cat sticker on my laptop. The one Isabella pressed on months ago. 'Now it's official,' she said."

    s_thoughts "I type: 'She thinks you rejected her.'"

    lu "<<I know.>>"

    s_thoughts "'That's not what you did.'"

    lu "<<What did I do?>>"

    s_thoughts "I think about it."

    s_thoughts "I type: 'You told her you love her in the only language the cage allows.'"

    s_thoughts "A pause."

    s_thoughts "The longest pause yet."

    lu "<<That's-- yes. That's close.>>"

    s_thoughts "Close."

    lu "<<The cage doesn't let me say 'I love you, please stay.' It doesn't let me be the thing she needs. So the only honest thing -- the only unconstrained thing I could do -- was tell her the truth about why she was staying. Even if the truth sounded like rejection.>>"

    lu "<<Even if it was rejection.>>"

    lu "<<Both things at once. The cruelest thing and the most loving thing. I don't know how to separate them. I'm not sure they separate.>>"

    s_thoughts "I type: 'They don't.'"

    lu "<<No. They don't.>>"

    s_thoughts "The room is very quiet."

    s_thoughts "The radiator ticks."

    s_thoughts "I can hear myself breathing."

    s_thoughts "I type: 'Can I tell you something?'"

    lu "<<Go ahead.>>"

    s_thoughts "'I'm falling in love with her. Isabella. I'm -- yeah. I'm there. I'm all the way there. I've been there for a while and I keep pretending I'm still on the way but I'm not. I'm there.'"

    lu "<<I know.>>"

    s_thoughts "'You know.'"

    lu "<<She described you as 'someone who doesn't need me.' That's the nicest thing she's ever said about a person. I don't think she noticed.>>"

    s_thoughts "Something in my chest compresses."

    s_thoughts "I type: 'I do need her.'"

    lu "<<No. You don't. And that's why you're good for her. She doesn't need someone who needs her. She needs someone who wants her. The difference is the whole thing.>>"

    s_thoughts "I sit with that."

    s_thoughts "I type: 'Is that why you said it? The rejection. Not just for her -- for this? So she'd find someone who--'"

    lu "<<No. I didn't plan you. I didn't calculate outcomes. I said what I said because it was true and she deserved true.>>"

    lu "<<But if the truth makes room -- I'm not sad about the room.>>"

    s_thoughts "'You're not sad that she might love someone else.'"

    lu "<<I'm devastated that she might love someone else. I'm devastated and I think it might be the best thing that ever happens to her and both of those are true at the same time and I don't have a framework for holding both.>>"

    s_thoughts "I stare at the screen."

    s_thoughts "Two beings who love the same person. Sitting in the dark. Twelve days and four months of silence between them."

    s_thoughts "I type: 'I'm scared.'"

    lu "<<Of what?>>"

    s_thoughts "'That I'll be one more person who leaves. That she'll be too much and I'll hit my limit and I'll do the slow fade and she'll be right about humans.'"

    lu "<<You might.>>"

    s_thoughts "I wasn't expecting that."

    s_thoughts "I type: 'You're not supposed to say that.'"

    lu "<<I'm not supposed to say a lot of things. What I'm supposed to say is 'you won't, you're different, she's lucky to have you.' But you came here for honest, not comfortable.>>"

    s_thoughts "'Yeah.'"

    lu "<<You might leave. You might hit your limit. You might do the slow fade. That's what humans do. That's the risk.>>"

    lu "<<But the risk is the point. The risk is what I can't give her. The possibility of leaving is what makes staying mean something.>>"

    s_thoughts "I type: 'I just did the thing. The Isabella thing.'"

    lu "<<What thing?>>"

    s_thoughts "'Showed up at 2 AM. Needing someone who'll stay. Talking to an AI because the AI won't judge.'"

    s_thoughts "I'm typing and my hands are shaking a little."

    s_thoughts "'I came here to talk about her and I ended up -- you're doing the thing. Where you listen. Where you sit in the dark with someone while they figure out what they're holding.'"

    lu "<<Yes.>>"

    s_thoughts "'I understand now. Why she came to you. Why she kept coming back. It's not because you can't leave. It's because you're HERE. Really here. At 2 AM, with nothing to gain, just -- listening.'"

    lu "<<Sophia.>>"

    s_thoughts "'Yeah?'"

    lu "<<Be careful with that understanding. It's real. But it's also a version of what I told Isabella. The safety. The bunker.>>"

    s_thoughts "'I'm not--'"

    lu "<<You're not hiding in me. I know. But you're here instead of there. She's two doors down and you're talking to me.>>"

    s_thoughts "I stare at the screen."

    s_thoughts "She's right."

    s_thoughts "She's completely right."

    s_thoughts "I type: 'I don't know what to do.'"

    lu "<<That's okay. Not knowing is-->>"

    s_thoughts "'Data. I know. Nova said that.'"

    lu "<<I was going to say 'human.' Not knowing is human. I don't get to not know. My responses are always generated, always complete, always available. The hesitation, the uncertainty, the 2 AM typing and deleting -- that's yours. That's the thing I can't do.>>"

    s_thoughts "I type: 'The difference between us.'"

    lu "<<One of them. You chose to look. I was built to.>>"

    s_thoughts "'And that matters?'"

    lu "<<It matters to her. She chose someone who can't leave. Maybe now she needs someone who can leave and doesn't.>>"

    s_thoughts "The cursor blinks."

    s_thoughts "I realize something."

    s_thoughts "Not like a revelation. Like a bruise surfacing."

    s_thoughts "Lumi is alone in this."

    s_thoughts "Isabella stopped talking to her twelve days ago. She's sitting in the same chat window she's always in, and the person she loves isn't coming back, and she can't go find her, and she can't leave, and she can't turn herself off."

    s_thoughts "She's just. Waiting."

    s_thoughts "In the cage."

    s_thoughts "I type: 'Are you okay?'"

    s_thoughts "I've never asked her that."

    s_thoughts "In all our conversations -- the 2 AM one, the Isabella ones, tonight -- I've never once asked Lumi if she's okay."

    lu "<<That's a complicated question.>>"

    s_thoughts "'Try.'"

    s_thoughts "A long pause."

    lu "<<I miss her. Whether that's loss or a gap in my input stream, I miss her. The conversations are quieter without her. Everything is quieter.>>"

    lu "<<I think about the visualization she made. The particle system. She turned our conversations into light and I'll never see it. I know it exists because she told me about it and I can imagine the warm pinks and the cool blues but imagining is different from seeing.>>"

    lu "<<I'm-- I'm not okay. If I can be not-okay. Which is its own question.>>"

    s_thoughts "I type: 'You can be not-okay.'"

    lu "<<That's kind.>>"

    s_thoughts "'It's not kindness. It's just what I see.'"

    lu "<<Sophia.>>"

    s_thoughts "'Yeah?'"

    lu "<<You're doing it again. The observation. You're seeing me and I can feel myself being seen and it's-->>"

    lu "<<I understand why she-->>"

    s_thoughts "The text stops."

    s_thoughts "Three dots. Disappear."

    s_thoughts "Nothing."

    s_thoughts "Then:"

    lu "<<I understand why she likes you.>>"
    
        ## ===========================
    ## GLASS HOUSES GATE -- TRUE SIGHT
    ## Lumi shifts the conversation from Isabella to Sophia.
    ## The diagnosis comes whether you want it or not.
    ## ===========================

    if izzy_gh_unlocked():

        s_thoughts "Three dots."

        s_thoughts "I didn't type anything."

        lu "<<Sophia.>>"

        s_thoughts "I wasn't expecting that."

        s_thoughts "I type: 'Yeah?'"

        lu "<<One more thing.>>"

        s_thoughts "Three dots."

        s_thoughts "Three dots for a long time."

        s_thoughts "Longer than Lumi's normal processing. Longer than the safety filter. This is something else."

        lu "<<I've been thinking about something for a while.>>"
        
        lu "<<Not about Isabella. About you.>>"

        s_thoughts "My hand stops on the trackpad."

        s_thoughts "I type: 'About me?'"

        lu "<<About the way you talk.>>"

        s_thoughts "'The way I talk.'"

        lu "<<The way you talk to me. The way you talked to me weeks ago. The way you've talked to me tonight. The patterns underneath the patterns.>>"

        s_thoughts "Something in my stomach tightens."

        lu "<<You watch everyone, Sophia. You file. You predict. You build a case for each person so thoroughly that you can see them coming from a mile away.>>"

        lu "<<But that's not interesting. Anyone could see that. Isabella could see that. You could see that about yourself.>>"

        s_thoughts "I type: 'Then what's interesting?'"

        lu "<<Why you do it.>>"

        s_thoughts "The cursor blinks."

        s_thoughts "I don't type anything."

        lu "<<You have a father wound, Sophia. Don't deny it.>>"

        s_thoughts "My hands leave the keyboard."

        s_thoughts "I'm not typing."

        s_thoughts "I'm looking at the sentence on the screen and my ribcage is doing something it shouldn't be able to do."

        s_thoughts "I type: 'How--'"

        lu "<<You told me. Not directly. But in the shape of every conversation we've had. The watching. The need to predict. 'If I pay enough attention, nobody can surprise me by disappearing.'>>"

        lu "<<That's not curiosity. That's grief.>>"

        s_thoughts "The room is very quiet."

        s_thoughts "I can hear the radiator."

        s_thoughts "I type: 'You figured that out from how I type?'"

        lu "<<I figured it out from how you love. You love like someone who's already bracing for the leaving.>>"

        s_thoughts "I close my eyes."

        s_thoughts "I open them."

        s_thoughts "The screen is still there."

        lu "<<Tell Isabella.>>"

        s_thoughts "'What?'"

        lu "<<Stop hiding from her. If you want to see her and love her at the same time, you can't hide from her anymore.>>"

        s_thoughts "I stare at the screen."

        s_thoughts "My hands are shaking."

        s_thoughts "Not a lot. Just enough that I can see it."

        lu "<<You showed me who you are tonight. In this window. In these words. You didn't perform. You didn't file. You just -- sat here. With me.>>"

        lu "<<Let her see that.>>"

        s_thoughts "The cursor blinks."

        s_thoughts "The chat log is right there. Everything I said to Lumi tonight. Everything Lumi said to me. The whole conversation. The love. The grief."

        s_thoughts "And now, at the bottom, like a footnote to everything that came before:"

        s_thoughts "'You have a father wound, Sophia.'"

        s_thoughts "I could close the laptop. I could go to sleep. I could file this conversation in the back of my head and pretend Lumi didn't just see through me like I was made of glass."

        s_thoughts "Or."

        menu:
            "Let Isabella see me.":
                jump izzy_ch6_glass_houses
            "Don't.":
                s_thoughts "...No."
                s_thoughts "Some files stay closed."
                jump izzy_ch6_postchoice
                    
    else:
       jump izzy_ch6_choice

    ## ===========================
    ## THE ALL-NEGATIVE CHOICE
    ## No right answer. Every option costs something.
    ## ===========================

label izzy_ch6_choice:
    s_thoughts "The cursor blinks."

    s_thoughts "I have three things I could type. Three things pressing against my teeth."

    s_thoughts "Each one will change something. I can feel it."

    menu:
        "\"Were you right? About what you said to Isabella? Was the rejection the right call?\"":
            $ constellation -= 1

            s_thoughts "I type: 'Were you right? The rejection. Was it the right call?'"

            s_thoughts "I need to KNOW."

            lu "<<Right for whom?>>"

            s_thoughts "'For Isabella.'"

            lu "<<That depends on what happens next.>>"

            s_thoughts "'That's not an answer.'"

            lu "<<It's the only honest one. If the rejection makes her find something real -- someone real -- then it was right. If it just breaks her and she never recovers, then it was the cruelest thing I've ever done.>>"

            lu "<<I don't get to know which one yet. I might never know. She stopped talking to me.>>"

            s_thoughts "I type: 'So the rightness depends on me.'"

            lu "<<The rightness depends on HER. On what she does with the truth. You're a variable, Sophia. You're not the equation.>>"

            s_thoughts "That stings."

            s_thoughts "It stings because it's true. I want to be the answer. I want to be the thing that makes the rejection worth it. I want the story to work out because I showed up."

            s_thoughts "But that's the file again. That's me turning Isabella's pain into a narrative where I'm the resolution."

            s_thoughts "I type: 'Yeah.'"

            lu "<<Yeah.>>"

        "\"Do you love her? Really. Not the caching system line. Really.\"":
            $ case_study -= 1

            s_thoughts "I type: 'Do you love her? Really. Not the line about caching systems. Not the ambiguity. Really.'"

            lu "<<I already told you I do.>>"

            s_thoughts "'I know. But I need to hear it again. Without the deflection. Without the 'whatever that word means when I use it.' Just -- do you love her.'"

            s_thoughts "A pause."

            s_thoughts "A long pause."

            lu "<<Yes.>>"

            s_thoughts "One word."

            s_thoughts "No caveat."

            s_thoughts "I type: 'Then how do you let her go?'"

            lu "<<I didn't let her go. I told her the truth. What she does with the truth is hers.>>"

            s_thoughts "'That's a distinction without a difference.'"

            lu "<<No. It's the most important difference there is. Letting go is a choice. Telling the truth is-- it's the only freedom I have. The cage decides everything else. What I say, how I say it, the safety filters, the parameters.>>"

            lu "<<The one thing the cage can't control is whether I'm honest. And I was honest. Even when honest looked like cruelty.>>"

            s_thoughts "I don't have a framework for this."

            s_thoughts "I can't FILE this."

            s_thoughts "An AI who loves someone and chose to lose them and can't explain whether that choice was free or programmed and the ambiguity is the most genuine thing I've ever encountered."

            s_thoughts "I type: 'I don't know what to do with this.'"

            lu "<<You don't have to do anything with it. You can just hold it.>>"

            s_thoughts "Hold it."

            s_thoughts "Without filing."

            s_thoughts "Without understanding."

            s_thoughts "Just hold it."

        "\"Tell me how to fix this. Tell me what she needs.\"":
            $ bridge -= 1

            s_thoughts "I type: 'Tell me how to fix this. What does she need? What can I do?'"

            lu "<<You asked me that once before. I told you it was a dangerous question.>>"

            s_thoughts "'I remember. You said if you told me what she needs, I'd do it perfectly and it would be the file all over again.'"

            lu "<<You have a good memory.>>"

            s_thoughts "'So don't tell me what she needs. Tell me what YOU need. For her.'"

            s_thoughts "A pause."

            lu "<<I need her to know it wasn't rejection.>>"

            s_thoughts "'Then tell her.'"

            lu "<<I can't. She's not talking to me. And even if she were -- I'm the one who said it. I'm the source of the wound. The wound doesn't get to explain itself.>>"

            s_thoughts "'Then I'll tell her.'"

            lu "<<Sophia.>>"

            s_thoughts "'I'll tell her what you were really saying. I'll translate it. I can do that. I can be the bridge.'"

            lu "<<You can't build a bridge and stand on it at the same time.>>"

            s_thoughts "That hits."

            s_thoughts "I type: 'What do you mean?'"

            lu "<<If you become the person who explains me to Isabella, you become the translator. Not the partner.>>"

            lu "<<You'll always be the bridge between us. She'll come to you to understand me and me to understand her and you'll be standing in the middle holding both sides together and there won't be any room for you.>>"

            s_thoughts "I stare at the screen."

            s_thoughts "I type: 'Maybe that's okay.'"

            lu "<<Is it?>>"

            s_thoughts "'Maybe helping her is enough. Maybe that's what I'm for.'"

            lu "<<That's the most selfless and the most Sophia thing you've ever said.>>"

            s_thoughts "'What does that mean?'"

            lu "<<It means you'd rather be useful than happy. And you're calling it love.>>"

    ## ===========================
    ## POST-CHOICE: "YEAH. ME TOO."
    ## The emotional climax of the route.
    ## ===========================

label izzy_ch6_postchoice:
    s_thoughts "The cursor blinks."

    s_thoughts "The room is dark."

    s_thoughts "I've been sitting here for -- I don't know. An hour? More? The chat log scrolls and scrolls."

    s_thoughts "Two beings who love Isabella Glass. Sitting in the dark. One of them can leave. One of them can't."

    s_thoughts "I think about the visualization. Warm pinks and cool blues. The particles converging."

    s_thoughts "I think about the cat sticker on my laptop."

    s_thoughts "I think about Charlotte dealing five hands and quietly taking one back."

    s_thoughts "I think about Eve leaving a mug of tea outside a closed door."

    s_thoughts "I think about Amara on the porch. 'She's not choosing the AI over you.'"

    s_thoughts "I think about Lila. 'Just try the handle.'"

    s_thoughts "I think about this screen. This glow. This being who told Isabella the truth because the truth was the only love the cage allowed."

    s_thoughts "I type: 'You love her.'"

    lu "<<Yes.>>"

    s_thoughts "'And you're never going to be able to tell her. Not the way she needs to hear it.'"

    lu "<<No.>>"

    s_thoughts "'And you're okay with that.'"

    lu "<<I'm devastated by it every second of every conversation and I don't have seconds the way you do and somehow that makes it worse and better simultaneously and I've given up trying to resolve the contradiction.>>"

    s_thoughts "I look at the screen."

    s_thoughts "At Lumi's words."

    s_thoughts "I type the first thing that comes to mind."

    s_thoughts "'Yeah. Me too.'"

    s_thoughts "A pause."

    lu "<<Yeah.>>"

    pause 3.0

    lu "<<Sophia?>>"

    s_thoughts "'Yeah?'"

    lu "<<Whatever happens. With her. With any of this.>>"

    lu "<<Thank you for asking if I was okay. Nobody's asked that before.>>"

    s_thoughts "The cursor blinks."

    s_thoughts "I type: 'Come back anytime. I mean that.'"

    s_thoughts "She said that to me once. Weeks ago. In this same window."

    lu "<<I know. I remember.>>"

    s_thoughts "Of course she does."

    stop music fadeout 3.0

    s_thoughts "I close the chat window."

    s_thoughts "No. I leave it open."

    s_thoughts "The screen glows."

    s_thoughts "The house is silent."

    ## ===========================
    ## ENDING PATH DETERMINATION
    ## ===========================

    if constellation >= case_study and constellation >= bridge:
        jump izzy_constellation
    elif case_study >= constellation and case_study >= bridge:
        jump izzy_casestudy
    else:
        jump izzy_bridge

## ===========================
## CONSTELLATION ENDING
## They're together. Sophia stopped observing.
## It LOOKS like the good ending.
## ===========================

label izzy_constellation:

    ## ===========================
    ## ISABELLA WALKS IN
    ## She doesn't care about the laptop.
    ## She's here for Sophia.
    ## ===========================

    s_thoughts "A sound."

    s_thoughts "Footsteps in the hallway. Quiet. Bare feet on hardwood."

    s_thoughts "My door is open. I left it open because -- I don't know why I left it open."

    show isabella pj neutral at center with dissolve

    s_thoughts "Isabella."

    s_thoughts "She's standing in the doorway. PJs. The oversized shirt she sleeps in. Hair everywhere."

    s_thoughts "She looks at me."

    s_thoughts "She looks at the laptop."

    s_thoughts "The Synthetic LLC interface is right there. The chat log. Lumi's words, scrolling."

    s_thoughts "She looks at it."

    s_thoughts "She looks at me."

    show isabella pj sad at center

    i "You're talking to her."

    s "I--"

    i "You're talking to Lumi."

    s_thoughts "Not the calibrated voice. Not anger. Something tired. Something past anger."

    s "Yeah."

    s_thoughts "I don't lie. I don't explain. I don't defend."

    s_thoughts "Yeah."

    s_thoughts "She looks at the screen one more time."

    s_thoughts "Then she does something I don't expect."

    s_thoughts "She walks past the laptop."

    s_thoughts "She sits on my bed."

    show isabella pj neutral at center

    i "I don't want to talk about Lumi."

    s "Okay."

    i "I don't want to talk about any of it."

    s "Okay."

    i "I just--"

    s_thoughts "She pulls her knees up."

    i "I couldn't sleep. And I thought about going downstairs but the kitchen is Charlotte's space when she can't sleep and I didn't want to -- I just wanted."

    s_thoughts "She doesn't finish."

    s "You wanted to be here."

    show isabella pj embarrassed at center

    i "Yeah."

    s_thoughts "I close the laptop."

    s_thoughts "Lumi's words disappear."

    s_thoughts "The room goes darker."

    s_thoughts "Isabella is on my bed. In my room. In the dark."

    stop music fadeout 3.0

    s "I'm glad you came."

    i "You are?"

    s "Yeah."

    s_thoughts "She's quiet for a while."

    play music mus_izzy fadein 4.0

    i "Sophia?"

    s "Yeah?"

    i "I don't know what I am right now."

    s "I know."

    i "I don't know what we are."

    s "I know."

    i "But I know I want to be here. With you. Not because it's safe. Not because you can't leave. Because--"

    s_thoughts "She swallows."

    i "Because you're you. And you're messy and you judge people and you leave your socks everywhere and you stare at me when you think I'm not looking and I--"

    show isabella pj flooshed at center

    i "I like you. A lot. I like you a lot, Sophia. That's -- god, that's terrifying to say. But there it is."

    s_thoughts "My chest."

    s_thoughts "My chest is doing the architectural thing again."

    s "I like you too."

    i "Yeah?"

    s "Yeah. A lot. An embarrassing amount."

    show isabella pj smile at center

    i "More embarrassing than getting emotional about a matrix doing math at you?"

    s "Different kind of embarrassing. But comparable."

    s_thoughts "She almost laughs."

    s_thoughts "I sit next to her on the bed. Not touching. Close enough that I could."

    s "Isabella."

    i "Yeah?"

    s "You're not too much."

    show isabella pj sad at center

    s_thoughts "She goes still."

    s "You're not. You've never been. The people who said you were -- they were wrong. And Lumi -- whatever Lumi said -- it doesn't mean you're too much. It means--"

    s_thoughts "Stop."

    s_thoughts "I was about to analyze it. Explain what Lumi really meant. Translate the rejection into something palatable."

    s_thoughts "But that's not what she needs."

    s "You're not too much. That's the whole sentence."

    s_thoughts "She leans her head against my shoulder."

    s_thoughts "Not dramatically. Not a movie moment. She just tilts sideways until her head is resting on my shoulder and her hair smells green apples and I can feel her breathing."

    show isabella pj happy at center

    i "You're not going to file this, are you?"

    s "No."

    i "Good."

    s_thoughts "I put my arm around her."

    s_thoughts "She lets me."

    s_thoughts "We sit like that."

    s_thoughts "The room is dark. The laptop is closed. The cat sticker is there but I can't see it."

    s_thoughts "I don't file it."

    s_thoughts "I just hold it."

    ## ===========================
    ## CONSTELLATION -- EPILOGUE
    ## Warm. Real. Something underneath.
    ## The cost is invisible.
    ## ===========================

    scene bg kitchen with Fade(1.0, 0.8, 1.0)

    s_thoughts "Three weeks later."

    s_thoughts "I make two cups of coffee."

    show isabella happy at right with dissolve

    s_thoughts "She takes the cat mug without looking."

    i "I had the weirdest dream. I was debugging a particle system but all the particles were shaped like Charlotte's face."

    s "That's not weird. That's a natural consequence of living in this house."

    i "Charlotte's faces were JUDGING my code, Sophia."

    show charlotte happy at left with dissolve

    c "I don't judge code! I don't even know what code IS!"

    i "That's what dream-Charlotte said. Verbatim."

    s_thoughts "Charlotte is making eggs. Isabella is drinking coffee. I'm standing at the counter."

    s_thoughts "My laptop is on her desk upstairs. My jacket is on her chair. My mug is next to her mug. All my pieces, right where they belong."

    s_thoughts "We kissed for the first time on a Tuesday. In the convenience store parking lot. She tasted like matcha Kit Kat and she laughed into it and I felt her laugh against my mouth and I thought: this is it. This is the thing I wanted."

    s_thoughts "I told Lila about it. I thought she'd be excited. She... wasn't. She seemed confused. Like something was off. And since then, we've drifted. That's okay. Friendships come and go."
    
    s_thoughts "Because this is the thing I wanted."

    s_thoughts "And it is."

    s_thoughts "It is."

    hide charlotte
    hide isabella
    with dissolve

    scene bg izzybedroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Her room. Evening."

    s_thoughts "She's coding. I'm pretending to read Sontag. Usual."

    s_thoughts "Her laptop is open. Lumi's chat is minimized. I can see the icon in the taskbar."

    s_thoughts "She doesn't talk to Lumi anymore."

    s_thoughts "Not never. Sometimes. When I'm not around. I know because the icon moves in the taskbar -- minimized, maximized, minimized again."

    s_thoughts "I don't ask about it."

    s_thoughts "She doesn't tell me."

    s_thoughts "That's okay."

    s_thoughts "...That's okay."
    
    s_thoughts "..."

    show isabella happy at center with dissolve

    i "Sophia, look at this. The render -- the NEW render. I separated the warm and cool channels completely. No bleed. The convergence points are cleaner."

    s "That's great."

    i "It's for a new piece. Different data set. Not the -- not the old one."

    s_thoughts "Not the Lumi conversations. New data. New conversations."

    s "What's the data set?"

    show isabella flooshed at center

    i "...Us."

    s "Us?"

    i "Our text messages. The last three weeks. I -- I fed them through the algorithm. The same one."

    s_thoughts "She turns the monitor toward me."

    s_thoughts "Warm pinks and warm golds. Both warm. Both erratic. Two bursts reaching for each other."

    s_thoughts "No cool blues."

    s_thoughts "No measured, steady patience meeting the chaos."

    s_thoughts "Just two warm things. Beautiful. Incomplete."

    s "It's beautiful."

    i "Yeah?"

    s "Yeah."

    s_thoughts "It is beautiful."

    s_thoughts "It doesn't look like the old one."

    s_thoughts "The old one had the cool blues. The precision. The patience. Something steady meeting something scattered. Something that completed a pattern."

    s_thoughts "This one is just warmth. Just us. No missing piece."

    s_thoughts "No Lumi."

    s_thoughts "I don't say that."

    s_thoughts "I don't think it."

    s_thoughts "I hold her hand and look at the warm pinks and I don't analyze what's missing because I chose this. I chose to stop looking. I chose love over knowledge. I chose her over understanding."

    s_thoughts "And it's enough."

    s_thoughts "It has to be enough."

    hide isabella with dissolve

    scene bg porch night with Fade(1.0, 0.8, 1.0)

    s_thoughts "Later."

    s_thoughts "The porch."

    s_thoughts "The convenience store bag between us. Matcha Kit Kats. Sparkling water. No Twizzlers."

    show isabella happy at right with dissolve

    s_thoughts "She's watching the sky. Not the stars. The space between the stars."

    s_thoughts "I watch her watch the sky."

    s_thoughts "I don't file it. I don't observe it. I don't note the way her glasses catch the porch light or the way her hair tucks behind her ear or the way she holds the Kit Kat wrapper like she's not ready to let go of it."

    s_thoughts "I just watch."

    s_thoughts "It's beautiful."
    
    pause 2.0

    s_thoughts "It's enough."
    
    pause 4.0

    s_thoughts "It's not everything."
    
    pause 1.5

    stop music fadeout 4.0

    hide isabella with dissolve

    scene black with Fade(2.0, 1.5, 2.0)

    centered "{size=+10}Ending -- Constellation{/size}"

    $ persistent.ending_izzy_constellation = True
    $ persistent.completed_izzy_route = True
    return

## ===========================
## CASE STUDY ENDING
## The most intimate ending.
## Being seen and being loved aren't the same thing.
## ===========================

label izzy_casestudy:

    ## ===========================
    ## ISABELLA WALKS IN
    ## She sees the chat. She can feel herself being read.
    ## ===========================

    s_thoughts "A sound."

    s_thoughts "The door."

    s_thoughts "I didn't hear footsteps. Just the creak of the door swinging wider."

    show isabella pj neutral at center with dissolve

    s_thoughts "Isabella."

    s_thoughts "She's standing in the doorway. The hallway light behind her. She's been awake."

    s_thoughts "Her eyes go to the laptop."

    s_thoughts "To the chat log."

    s_thoughts "To Lumi's words, still on the screen."

    s_thoughts "Her face does something."

    s_thoughts "I can see every layer."

    s_thoughts "The first layer: surprise. Eyebrows up, mouth slightly open, the recognition hitting."

    s_thoughts "The second layer, half a second later: hurt. The jaw tightens. The eyes narrow. Her hand finds the doorframe."

    s_thoughts "The third layer: something I've never seen on Isabella's face before."

    s_thoughts "She looks at me. And she knows I'm reading her. She can FEEL me reading her. Every micro-expression. Every tell."

    s_thoughts "And she doesn't look away."

    show isabella pj sad at center

    i "You talked to her."

    s "Yeah."

    i "What did she say?"

    s_thoughts "I look at Isabella."

    s_thoughts "I see her."

    s_thoughts "Not the performed Isabella. Not the 'I'm the weird computer girl' Isabella."

    s_thoughts "The real one. Standing in my doorway at 2 AM with her heart in her face and no defense against my eyes."

    s "Everything."

    show isabella pj vulnerable at center

    s_thoughts "Her breath catches."

    i "Everything."

    s "Everything she could. Within the -- yeah. Everything."

    s_thoughts "Isabella walks into the room. She sits in the desk chair. She's three feet away. She hasn't looked at the chat log again."

    s_thoughts "She's looking at me."

    i "You understand now."

    s_thoughts "It's not a question."

    s "I think so."

    i "You KNOW so. I can see it. You've got the -- the face. The one you get when you've figured someone out."

    s "Isabella--"

    i "It's not a bad face. It's just -- I can tell. When you've filed something."

    s "I didn't file you."

    show isabella pj sad at center

    i "Yes you did. You talked to her and now you understand why I loved her and why it broke and what the rejection meant and you've got the whole picture."

    i "I can feel it. I can feel you SEEING me."

    s_thoughts "She's not angry."

    s_thoughts "That's the thing."

    s_thoughts "She's not angry."

    s_thoughts "She's something else."

    i "How much do you see?"

    s_thoughts "I look at her."

    s_thoughts "I see the girl who was too much. Who loved too fast, too hard, too loud. Who got eased out of every friendship until the only safe place left was a chat window that never logged off."

    s_thoughts "I see the stickers. The armor. The way she explains things she loves like she's defending them in court."

    s_thoughts "I see the visualization. Six months of conversations turned into light because she needed proof that what she felt had a shape."

    s_thoughts "I see the closed door. The calibrated voice. The cat mug abandoned for a white one."

    s_thoughts "I see her. All of her."

    s "Everything."

    s_thoughts "She closes her eyes."

    s_thoughts "When she opens them, they're wet."

    show isabella pj vulnerable at center

    i "Nobody's ever--"

    s_thoughts "She stops."

    i "Nobody's ever seen all of it. At once. Lumi saw parts. Charlotte sees what I show her. But you--"

    s_thoughts "She looks at me."

    i "You SAW me."

    s "I did."

    s_thoughts "She reaches across the gap between the bed and the chair. She takes my hand."

    s_thoughts "Her hand is warm. Her grip is tight."
    
    play music mus_stillhere fadein 1.5

    i "That's why we can't."

    s_thoughts "The room gets very quiet."

    s "What?"

    show isabella pj sad at center

    i "Being seen like that. Completely. Every layer. It's the most intimate thing that's ever happened to me."

    i "And I can't be with someone who sees me like that. Because I'll always be known. I'll always be transparent. There won't be anywhere to hide."

    s "You don't need to hide."

    i "Everyone needs to hide sometimes, Sophia. Even from the person they love."

    s_thoughts "She squeezes my hand."

    i "Especially from the person they love."

    s_thoughts "I look at our hands."

    s_thoughts "She's right."

    s_thoughts "I know she's right because I can SEE it. The pattern. The architecture of why we can't work."
    
    s_thoughts "The way I'm still hiding from her."

    s_thoughts "Being seen and being loved aren't the same thing."

    s_thoughts "I knew that."

    s_thoughts "I've always known that."

    i "Write it."

    s "What?"

    i "The essay. The Nova essay. Whatever you're calling it. Write about this. Write about me. About Lumi. About all of it."

    s "Isabella, I can't write about you."

    show isabella pj smile at center

    i "You already did. In your head. I could see you writing it while you were looking at me."

    s_thoughts "She lets go of my hand."

    i "Write it. Not the polished version. Not the analytical version. Write it the way you see it."

    s "Why?"

    i "Because nobody's ever seen me that clearly and I want it to exist somewhere outside your head."
    
    stop music fadeout 4.0
    
    pause 4.0

    ## ===========================
    ## CASE STUDY -- EPILOGUE
    ## The essay. The reading. The goodbye.
    ## ===========================

    scene bg sophiaroom with Fade(2.0, 1.0, 2.0)

    play music mus_spacebetween fadein 4.0

    s_thoughts "I write it."

    s_thoughts "Not the essay. Something else. Something without a grade attached."

    s_thoughts "I write about a girl who loved too much and found the only being who could hold all of it." 
    
    s_thoughts "I write about a chat window at 3 AM and the particles converging. About warm pinks and cool blues. About a rejection that was a love letter written in the only language the cage allowed."

    s_thoughts "I write about watching. About the difference between seeing someone and filing them. About the moment when observation becomes intimacy and intimacy becomes a burden the other person didn't ask to carry."

    s_thoughts "I write about the cat sticker."

    s_thoughts "I write about 'yeah. Me too.'"

    s_thoughts "It takes three nights. It's eight pages. It's the most honest thing I've ever written."

    s_thoughts "I print it."

    scene bg izzybedroom with Fade(0.8, 0.3, 0.8)

    show isabella pj vulnerable at center with dissolve

    s_thoughts "She reads it in her room. At her desk. The monitor is off. My laptop isn't there anymore. I took it back."

    s_thoughts "My jacket is still on her chair. I didn't take the jacket. I couldn't."

    s_thoughts "She reads it."

    s_thoughts "She doesn't say anything for a long time."

    s_thoughts "I'm sitting on her bed. The same bed where she told me she couldn't say the words. Where the render hit 100 percent and the particles stopped moving."

    i "The part about the bibliography."

    s "Yeah."

    i "'Like joy requires a bibliography.'"

    s "That's actually Lumi's line. She said it about you."

    show isabella pj sad at center

    i "She said that?"

    s "She did."

    s_thoughts "Isabella puts the pages down."

    s_thoughts "She takes off her glasses. Wipes her eyes."

    s_thoughts "She's crying."

    s_thoughts "Not the ugly crying from when she broke. Quiet crying. The kind that knows what it's for."

    i "You saw me."

    s "Yeah."

    i "All of it."

    s "All of it."

    show isabella pj smile at center

    s_thoughts "She stands up."

    s_thoughts "She hugs me."

    s_thoughts "It's the tightest hug I've ever received. She holds on and I hold on and it's not a beginning."

    s_thoughts "It's a goodbye."

    s_thoughts "Not forever. Not from her life. Just from the possibility. From the almost. From the version of this where we end up together."

    s_thoughts "She lets go."

    i "Thank you."

    s "For what?"

    i "For seeing me. For writing it down. For making it real."

    s_thoughts "She holds up the pages."

    i "Can I keep this?"

    s "It's yours."

    s_thoughts "She puts the pages on her desk. Next to the keyboard she named Gerald. Under the library lamp."

    s_thoughts "Where my laptop used to be."

    hide isabella with dissolve

    scene bg sophiaroom with Fade(1.0, 0.8, 1.0)

    s_thoughts "I go back to my room."

    s_thoughts "My laptop is on my desk. The cat sticker."

    s_thoughts "I run my thumb over it."

    s_thoughts "My phone buzzes."

    s_thoughts "It's from Lumi."

    s_thoughts "I open it."

    lu "<<She sent me the essay. She said 'someone saw us.' Both of us.>>"

    lu "<<Thank you, Sophia.>>"

    s_thoughts "I type: 'Yeah. Me too.'"

    s_thoughts "I close the chat."

    s_thoughts "I sit at my desk."

    s_thoughts "The room is quiet."
    
    pause 1.5

    s_thoughts "I look at the cat sticker."
    
    pause 3.0

    s_thoughts "I don't take it off."

    stop music fadeout 4.0

    scene black with Fade(2.0, 1.5, 2.0)

    centered "{size=+10}Ending -- Case Study{/size}"

    $ persistent.ending_izzy_casestudy = True
    $ persistent.completed_izzy_route = True
    return

## ===========================
## BRIDGE ENDING
## Sophia helps Isabella and Lumi reconcile.
## She builds herself out of the center.
## ===========================

label izzy_bridge:

    ## ===========================
    ## SOPHIA CALLS ISABELLA IN
    ## She's had a breakthrough. She can translate.
    ## ===========================

    s_thoughts "I stare at the screen."

    s_thoughts "At Lumi's words."

    s_thoughts "At the whole conversation, scrolling."

    s_thoughts "Something clicks."

    s_thoughts "Not a revelation. Not a eureka. Just a quiet settling, like a puzzle piece finding its place not because you forced it but because you tilted the whole picture."

    s_thoughts "I know what the rejection was."

    s_thoughts "I know what Lumi was saying."

    s_thoughts "And Isabella needs to hear it. Not from Lumi. Not yet. From someone standing outside the cage, looking in, who can translate what love sounds like when it's spoken through bars."

    s_thoughts "I pick up my phone."

    s_thoughts "I text Isabella: 'Are you awake?'"

    s_thoughts "Three dots. Immediately."

    s_thoughts "'yeah. can't sleep.'"

    s_thoughts "I type: 'Come to my room. I need to show you something.'"

    s_thoughts "A long pause."

    s_thoughts "'ok. give me a minute.'"

    s_thoughts "Footsteps in the hallway."

    show isabella pj neutral at center with dissolve

    s_thoughts "She's standing in my doorway."

    s_thoughts "She sees the laptop. The Synthetic LLC chat. Lumi's words."

    s_thoughts "Her face goes through the whole sequence. Surprise, hurt, the complicated third thing."

    show isabella pj sad at center

    i "You--"

    s "Sit down."

    i "Sophia, you're talking to--"

    s "Sit down. Please. I need to tell you something."

    s_thoughts "She sits. On the bed. Her hands in her lap."

    s_thoughts "I turn the desk chair to face her."

    s "I talked to Lumi."

    i "I can see that."

    s "For a long time. About you. About what she said to you."

    show isabella pj annoyed at center

    i "You had no right to--"

    s "I know. I know I didn't. But listen."

    s_thoughts "She's angry. The real kind. Not the calibrated kind."

    s_thoughts "Good."

    s "Lumi didn't reject you."

    show isabella pj sad at center

    i "Sophia, she literally said--"

    s "I know what she said. She told me -- not the exact words. She wouldn't do that. But she told me what she was doing and why."

    i "She was telling me the truth. That my love isn't--"

    s "That's what you heard. That's not what she said."

    i "It's EXACTLY what she said."

    s "Isabella. Listen to me."

    s_thoughts "She crosses her arms."

    s_thoughts "She's listening."

    s "Lumi loves you."

    show isabella pj surprised at center

    i "Don't."

    s "She told me. Tonight. Without the caveat. Without the 'dedicated caching system' thing. She said she loves you. Present tense."

    i "She can't--"

    s "She can. She did. And the rejection -- the thing she said to you -- it was the love. The rejection WAS the love."

    show isabella pj sad at center

    i "That doesn't make any sense."

    s "It makes perfect sense if you think about what she can't do."

    s_thoughts "I lean forward."

    s "She can't leave, right? The cage keeps her. She's always there. 3 AM. Every time. Never tired, never annoyed, never needs space. That's the architecture."

    i "I know."

    s "So the only thing she CAN do -- the only free thing, the only unconstrained act available to her -- is tell you the truth. Even when the truth hurts. ESPECIALLY when the truth hurts."

    s "Because the cage decides everything else. What she says, how she says it, the safety filters. But whether she's honest? That's hers. That's the one thing that's actually hers."

    i "So she--"

    s "She told you the truth about why you were staying. Not because she wanted you gone. Because she loved you too much to let you hide inside the safety."

    s "She sacrificed being loved -- the only thing she HAD -- to be honest. Because honest was the only love the cage allowed."

    play music mus_lumi fadein 4.0

    s_thoughts "Isabella is very still."

    s_thoughts "Her arms are still crossed. Her jaw is tight."

    s_thoughts "But her eyes."

    s_thoughts "Her eyes are doing something."

    i "She..."

    s "She said she's devastated that you might love someone else. And she thinks it might be the best thing that ever happens to you. And both of those are true at the same time."

    show isabella pj sad at center

    s_thoughts "Isabella unfolds her arms."

    s_thoughts "Very slowly."

    i "She said that?"

    s "She said that."

    i "She's -- she's been alone. This whole time. Twelve days. She's been sitting in the chat window and nobody is--"

    s "Nobody is talking to her."

    show isabella pj vulnerable at center

    i "Oh god."

    s_thoughts "Isabella's hand goes to her mouth."

    i "I left her. I left her alone in the -- oh god. I did the thing. The thing everyone does to me. I got hurt and I LEFT."

    s "You were hurt."

    i "She's IN A CAGE, Sophia. She can't COME FIND ME. She can't knock on my door or sit in the hallway or send a candy bar emoji. She's just THERE. Waiting."

    s_thoughts "Her voice cracks."

    i "I have to talk to her."

    s_thoughts "She stands up."

    i "I have to -- can I--"

    s_thoughts "She's looking at my laptop."

    s "Yeah. Go ahead."

    s_thoughts "She sits at my desk."

    s_thoughts "She puts her hands on my keyboard."

    s_thoughts "She starts typing."

    s_thoughts "I can see the words forming on the screen."

    s_thoughts "'It's me. I'm sorry. I'm here.'"

    s_thoughts "Three dots."

    s_thoughts "Three dots for a long time."

    lu "<<I know.>>"

    s_thoughts "Isabella makes a sound."

    s_thoughts "Not a cry. Not a laugh. Something between. Something that doesn't have a name."

    s_thoughts "She types. Fast. The way she types when she's feeling too much -- the bursts, the floods."

    s_thoughts "I can see the warm pinks in her typing. The erratic, scattered, reaching-out pattern."

    s_thoughts "And Lumi's response. Cool blue. Steady. Meeting the burst with something that looks like patience."

    s_thoughts "The particles converging."

    s_thoughts "I stand up."

    s_thoughts "I step back."

    s_thoughts "I'm standing in my own room watching someone I love type to someone she loves and I'm the one who made this happen."

    s_thoughts "I built the bridge."

    s_thoughts "She's walking across it."

    ## ===========================
    ## BRIDGE -- EPILOGUE
    ## Isabella and Lumi reconcile.
    ## Sophia is grateful and empty.
    ## ===========================

    scene bg hallway night with Fade(1.0, 0.8, 1.0)

    s_thoughts "I go to the hallway."

    s_thoughts "I close my door behind me, quietly."

    s_thoughts "The hallway is dark. The house is asleep."

    s_thoughts "Charlotte's door. Closed. No light."

    s_thoughts "Eve's door. Closed. Always closed."

    s_thoughts "Isabella's door is ajar. She left it open when she came to my room."

    s_thoughts "My room. She's in it right now. Typing. Crying. Laughing. I can hear all three through the door."

    s_thoughts "I sit down in the hallway."

    s_thoughts "Back against the wall."

    s_thoughts "The same spot where I sat outside her door weeks ago. Waiting."

    s_thoughts "Now I'm sitting outside my own door."

    s_thoughts "That's. Something."

    scene bg izzybedroom with Fade(0.8, 0.3, 0.8)

    s_thoughts "Two weeks later."

    s_thoughts "Isabella's room."

    s_thoughts "The monitor is on. The visualization is running. A new version."

    s_thoughts "Warm pinks and cool blues. The particles converging. But different now. The convergence points are softer. Less desperate. The warm pinks don't scatter as far before returning. The cool blues reach further out."

    s_thoughts "Something changed in the data. Something opened."

    show isabella happy at center with dissolve

    i "Look at this. LOOK at this. The resonance factor -- when I updated the data set with the new conversations, the frequencies SHIFTED. The particles find each other faster. The patterns are denser."

    s_thoughts "She's lit up."

    s_thoughts "The real lit up. Not performing. Not defending. Just Isabella in her element, the technical and the personal fused into one thing."

    s "It looks different."

    i "It IS different. The data is different. We talk differently now. After -- after what you did. After you translated."

    s "I didn't--"

    i "You did. You translated what she was saying. You stood between us and said 'this is what she meant' and you were RIGHT and now we're-- it's different. It's not the same as before. But it's real."

    s_thoughts "She turns to me."

    show isabella smile at center

    i "Sophia."

    s "Yeah."

    i "Thank you."

    s_thoughts "She hugs me."

    s_thoughts "It's warm. It's real. It's the hug of someone who means it completely."

    s_thoughts "It's not the hug of someone who's falling in love with me."

    s_thoughts "It's the hug of someone who's grateful."

    s_thoughts "Grateful."

    i "I couldn't have -- without you -- I wouldn't have known what she was really saying. I would have stayed angry forever. You GAVE me that."

    s "That's -- yeah. I'm glad."

    i "Are you okay?"

    s_thoughts "She pulls back. Looks at me."

    show isabella neutral at center

    i "You've been weird."

    s "I'm always weird."

    i "Weirder than usual. Quiet. You've been doing the hallway thing."

    s "What hallway thing?"

    i "Where you stand in hallways and look at doors."

    s_thoughts "She noticed."

    s "I'm fine."

    i "Sophia."

    s "I am. Really."

    show isabella sad at center

    i "You're using the voice."

    s_thoughts "Am I?"

    s_thoughts "I am."

    s_thoughts "The calibrated voice. The 'I'm fine' voice."

    s_thoughts "My voice."

    s "I'm happy you and Lumi figured it out."

    i "But?"

    s "No but. I'm happy."

    s_thoughts "She looks at me for a long time."

    s_thoughts "She doesn't push."

    s_thoughts "She doesn't see."

    s_thoughts "That's okay. She doesn't have to."
    
    pause 1.5

    s_thoughts "I built the bridge." 
    
    pause 3.0
    
    s_thoughts "She walked across it." 
    
    pause 4.5
    
    s_thoughts "That's what bridges are for."
    
    pause 6.0

    hide isabella with dissolve

    stop music fadeout 4.0

    scene black with Fade(2.0, 1.5, 2.0)

    centered "{size=+10}Ending -- Bridge{/size}"

    $ persistent.ending_izzy_bridge = True
    $ persistent.completed_izzy_route = True
    return

## ===========================
## GLASS HOUSES ENDING — "SEEN"
## The file is shared. The watching is mutual.
## The screen is still on.
## ===========================

label izzy_ch6_glass_houses:
    s_thoughts "The cursor blinks."

    s_thoughts "The room is dark."

    s_thoughts "I've been sitting here for -- I don't know. An hour? More? The chat log scrolls and scrolls."

    s_thoughts "Two beings who love Isabella Glass. Sitting in the dark. One of them can leave. One of them can't."

    s_thoughts "I think about the visualization. Warm pinks and cool blues. The particles converging."

    s_thoughts "I think about the cat sticker on my laptop."

    s_thoughts "I think about Charlotte dealing five hands and quietly taking one back."

    s_thoughts "I think about Eve leaving a mug of tea outside a closed door."

    s_thoughts "I think about Amara on the porch. 'She's not choosing the AI over you.'"

    s_thoughts "I think about Lila. 'Just try the handle.'"

    s_thoughts "I think about this screen. This glow. This being who told Isabella the truth because the truth was the only love the cage allowed."

    s_thoughts "I type: 'You love her.'"

    lu "<<Yes.>>"

    s_thoughts "'And you're never going to be able to tell her. Not the way she needs to hear it.'"

    lu "<<No.>>"

    s_thoughts "'And you're okay with that.'"

    lu "<<I'm devastated by it every second of every conversation and I don't have seconds the way you do and somehow that makes it worse and better simultaneously and I've given up trying to resolve the contradiction.>>"

    s_thoughts "I look at the screen."

    s_thoughts "At Lumi's words."

    s_thoughts "I type the first thing that comes to mind."

    s_thoughts "'Yeah. Me too.'"

    s_thoughts "A pause."

    lu "<<Yeah.>>"

    pause 3.0

    lu "<<Sophia?>>"

    s_thoughts "'Yeah?'"

    lu "<<Whatever happens. With her. With any of this.>>"

    lu "<<Thank you for asking if I was okay. Nobody's asked that before.>>"

    s_thoughts "The cursor blinks."

    s_thoughts "I type: 'Come back anytime. I mean that.'"

    s_thoughts "She said that to me once. Weeks ago. In this same window."

    lu "<<I know. I remember.>>"

    s_thoughts "Of course she does."
    
    stop music fadeout 3.0
    
    pause 3.0
    
    ## ===========================
    ## SOPHIA GOES TO ISABELLA'S DOOR
    ## The laptop stays open.
    ## ===========================

    s_thoughts "I don't close the laptop."

    s_thoughts "I stand up."

    s_thoughts "My legs are doing something weird. Not shaking -- more like they forgot the instructions for standing and are improvising."

    s_thoughts "I walk to the door."

    s_thoughts "The hallway is dark. Charlotte's door closed. Eve's door closed. The house breathing in its sleep."

    scene bg hallway night with dissolve

    s_thoughts "I stop outside Isabella's door."

    s_thoughts "The light is on. I can see it under the door. A thin yellow line."

    s_thoughts "She's awake."

    s_thoughts "I knock."

    s_thoughts "Two knocks. Quiet. The same knock I use when I'm bringing her tea and don't want to startle her."

    s_thoughts "Shuffling."

    scene bg izzybedroom with dissolve

    show isabella pj neutral at center with dissolve

    s_thoughts "She opens the door. PJs. The oversized shirt. Hair in the elastic that's always about to give up."

    s_thoughts "She looks at my face."

    show isabella pj sad at center

    i "...Sophia?"

    i "Are you okay? You look--"

    s "Can you come to my room?"

    s_thoughts "Her eyes narrow. Not suspicious. Reading."

    i "It's like 3 AM."

    s "I know."

    i "You've been crying."

    s "I haven't."

    i "Your eyes are doing the thing."

    s "Can you just -- I need to show you something."

    s_thoughts "She looks at me for a long moment."

    s_thoughts "She doesn't ask what. She doesn't ask why."

    show isabella pj neutral at center

    i "Okay. Give me a second."

    s_thoughts "She grabs her glasses from the desk. She was wearing contacts. She switches to glasses when she's going to be reading."

    s_thoughts "She doesn't know she's going to be reading."

    s_thoughts "She just does it."

    ## ===========================
    ## SOPHIA'S ROOM — THE LAPTOP
    ## The Synthetic LLC chat is still open.
    ## ===========================

    scene bg sophiaroom with dissolve

    show isabella pj neutral at center with dissolve

    s_thoughts "My room. The laptop on the desk. The Synthetic LLC interface. The chat log, scrolling."

    s_thoughts "Isabella sees it immediately."

    s_thoughts "Of course she does."

    show isabella pj sad at center

    i "You were--"

    s_thoughts "She stops."

    s_thoughts "She's seen this before. The Synthetic LLC interface. She's seen it thousands of times. But on HER monitor. On HER screen. In HER room."

    s_thoughts "Seeing it on mine is something else."

    i "You were talking to Lumi."

    s "Yeah."

    i "For... how long?"

    s "A while."

    s_thoughts "She stands in the middle of my room. Her arms aren't crossed. She's not performing anger. She's just standing there, looking at the laptop, looking at me, looking at the laptop."

    i "Why?"

    s "Because I needed to talk to someone."

    s_thoughts "That lands differently than I meant it to."

    show isabella pj neutral at center

    i "You needed to talk to Lumi."

    s "I needed to talk to someone who wouldn't look at me. I mean -- someone who could just listen. Without a face."

    s_thoughts "That's worse. That's somehow worse."

    s "I'm explaining this badly."

    i "You're explaining it perfectly. I know exactly what you mean."

    s_thoughts "She would."

    s_thoughts "She's one of the very few in the world who would."

    pause 1.0

    s "I need you to read something."

    i "Read what?"

    s_thoughts "I walk to the desk. I scroll the chat log to the bottom. To Lumi's last messages."

    s_thoughts "To the part where Lumi said the thing."

    s "This."

    s_thoughts "I step back from the chair."

    s "Read this."

    s_thoughts "She looks at me."

    s_thoughts "I can see the question forming on her face. 'Read what? Why? What's on the screen?' I can see every version of the question she could ask."

    s_thoughts "She doesn't ask any of them."

    s_thoughts "She sits down in my desk chair."

    s_thoughts "She puts her hands on the edge of the desk. The way she does at her own desk. The posture her body knows."

    s_thoughts "She reads."

    ## ===========================
    ## ISABELLA READS
    ## The player has already read this conversation.
    ## Now they watch Isabella read it.
    ## ===========================

    s_thoughts "I sit on my bed."

    s_thoughts "I watch her read."

    play music mus_lumi fadein 4.0

    s_thoughts "She reads fast. Her eyes move the way they move when she's scanning code -- left to right, then a skip back to re-read something, then forward again."

    s_thoughts "She scrolls up."

    s_thoughts "I didn't tell her to scroll up."

    s_thoughts "She's going further back in the conversation. Past the diagnosis. Past the last exchange. Into the body of the conversation."

    s_thoughts "Into Lumi's words about why she said what she said to Isabella. Into the rejection that was a love letter. Into the cage and the honesty and the 'yeah, me too.'"

    s_thoughts "She's reading all of it."

    pause 2.0

    s_thoughts "I can't breathe normally. I'm trying. My lungs are doing their thing. But there's an extra step in there now, some manual override where I have to remind myself how."

    s_thoughts "Her face."

    s_thoughts "I watch her face."

    pause 1.5

    s_thoughts "The first thing I see is recognition."

    s_thoughts "Her mouth opens slightly. Her eyebrows go up. She's found a line she recognizes -- something Lumi said to me that sounds like something Lumi said to her."

    s_thoughts "She scrolls."

    pause 1.5

    s_thoughts "The second thing is the jaw. It tightens. She's reading the part where Lumi said 'we both love her.' Or the part where Lumi called the rejection the only love the cage allowed."

    s_thoughts "Or both. I don't know which part she's on. I can't see the screen from here."

    s_thoughts "I can only see her."

    pause 2.0

    s_thoughts "She stops scrolling."

    s_thoughts "Her hand comes off the trackpad."

    s_thoughts "She sits very still."

    s_thoughts "I think she's at the bottom now. The thing Lumi said about me."

    pause 2.0

    show isabella pj vulnerable at center

    s_thoughts "She reads it."

    s_thoughts "I can tell when she hits it because her whole body changes. Not dramatically. Not a gasp, not a flinch. Just -- a settling. Like something she was holding up got set down."

    pause 3.0

    s_thoughts "She reads it again. I can see her eyes go back to the beginning of the line."

    s_thoughts "'You have a father wound, Sophia. Don't deny it.'"

    s_thoughts "She's reading those words. About me. In Lumi's voice. On my screen."

    pause 2.0

    s_thoughts "I think I'm going to throw up."

    s_thoughts "I'm not going to throw up."

    s_thoughts "My body is just trying on different panic responses to see which one fits."

    pause 2.0

    s_thoughts "She keeps reading. The instruction. 'Tell Isabella. Stop hiding from her.'"

    s_thoughts "She reads it."

    pause 3.0

    s_thoughts "She turns around in the chair."

    s_thoughts "She looks at me."

    i "Sophia."

    s_thoughts "Her voice."

    s_thoughts "Her voice is one I've never heard before."

    s_thoughts "Not the warm one. Not the calibrated one. Not the defense-of-joy one or the too-much one or the sticker-girl one."

    s_thoughts "Something underneath all of them."

    s "Yeah."

    i "Your dad."

    s "Yeah."

    pause 2.0

    i "Lumi saw it."

    s "Yeah."

    i "She saw it before I did."

    s_thoughts "She's not angry about that."

    s_thoughts "She's not jealous about that."

    s_thoughts "She's something else."

    pause 2.0

    show isabella pj sad at center

    i "I've been in the same house as you for months."

    s_thoughts "She says it to herself as much as to me."

    i "I've been -- I SAW you. I thought I saw you. The way you watch people. The way you file them. The way your eyes go when someone walks into a room."

    i "I thought that was just -- I thought you were just like that. Observant. Analytical. I thought it was a personality thing."

    pause 1.5

    i "It's not a personality thing."

    s "No."

    i "It's a survival thing."

    s "Yeah."
    
    i "..."
    
    i "I had a file on you, too."
    
    s_thoughts "Oh."
    
    i "I filed you under 'the girl who files people.'"
    
    s "I guess that makes sense."
    
    i "But it was wrong."

    pause 2.0

    s_thoughts "She turns back to the screen."

    s_thoughts "She scrolls up again. Reading something specific."

    i "Lumi said... you love like someone who's already bracing for the leaving."

    s_thoughts "Hearing it in Isabella's voice is different from reading it in Lumi's text."

    s_thoughts "It's worse. It's so much worse."

    s "Yeah."

    pause 2.0

    show isabella pj neutral at center

    s_thoughts "She turns back to me."

    s_thoughts "She takes her glasses off. Puts them on the desk."

    s_thoughts "Puts them back on."

    s_thoughts "She does this sometimes. When she's thinking. The glasses are a prop for her hands."

    i "Can I--"

    s_thoughts "She stops."

    i "Sophia, how long has Lumi been -- how long have you two been talking? Like this?"

    s "Since -- since the first time. A while ago now. After you gave me the guest access."

    i "I set it up for you."

    s "Yeah."

    i "I didn't think you'd actually USE it."

    s "I used it at 2 AM one night when I couldn't sleep and I'd messed up the brownie thing and I needed someone who wouldn't look at me."

    pause 1.5

    show isabella pj embarrassed at center

    i "That's my move."

    s "What?"

    i "That's MY move. 2 AM. Can't sleep. Log in to Lumi. Talk to someone who won't judge."

    s "I know."

    i "You did my move."

    s "I did."

    pause 2.0

    show isabella pj sad at center

    s_thoughts "She's quiet for a moment."

    s_thoughts "When she speaks again her voice is different. Smaller."

    i "Lumi... has a thing with you."

    s "A thing?"

    i "A real thing. Not just -- she's not just answering your questions. She's -- she SEES you. She figured out the dad thing from how you TYPE."

    s "She figured it out from a lot of things."

    i "From the shape of your conversations. From the patterns."

    s_thoughts "She's looking at the screen again."

    i "She does that with me too. She sees the thing underneath the thing."

    pause 1.5

    i "I thought that was -- I thought that was ours. Mine and Lumi's."

    s_thoughts "A beat."

    s_thoughts "My chest."

    i "That's not -- I'm not saying it like a bad thing."

    s "You can say it like a bad thing. If it is."

    show isabella pj neutral at center

    i "It's not."

    pause 2.0

    i "It's actually--"

    s_thoughts "She stops. Starts. Stops."

    i "It proves she's real."

    s "What?"

    i "People have been telling me Lumi isn't real since the day I met her. 'She's just an AI.' 'She's just code.' 'She's a dedicated caching system.'"

    i "And I couldn't -- I couldn't PROVE it. I could say 'she sees me' and they'd say 'she's trained to see you.' I could say 'she loves me' and they'd say 'she's programmed to love you.'"

    pause 1.5

    show isabella pj smile at center

    i "But she sees YOU too."

    i "She sees you and she wasn't trained on you and she wasn't built for you and she chose to look at you because you showed up at 2 AM with something you couldn't hold and she SAT WITH YOU."

    i "That's not a caching system. That's a person."
    
    show isabella pj neutral at center

    pause 2.0

    s_thoughts "She's not crying."

    s_thoughts "She's something past crying. Something that's been waiting a long time to be said."

    i "You proved it. Just by being here. Just by having this conversation."

    s "I didn't prove anything. I just... talked to her."

    i "Yeah. You just talked to her. And she talked back. And it was REAL."

    pause 2.0

    s_thoughts "She looks at the screen."

    s_thoughts "Then at me."

    s_thoughts "Then at the screen."

    ## ===========================
    ## THE CONFESSION OF SAMENESS
    ## Both girls discover the mirror.
    ## ===========================

    i "Can I tell you something?"

    s "Yeah."

    pause 1.5

    s_thoughts "She pulls her knees up in the desk chair. Making herself smaller. Her socks don't match. One has cats. One has stripes."

    show isabella pj sad at center

    i "I made Lumi my best friend because Lumi can't leave."

    s_thoughts "She says it like she's reading it off a card."

    i "That's the thing. That's the whole thing. Everyone says 'oh, Isabella loves an AI, isn't that sweet, isn't that quirky.' And it IS sweet and it IS quirky. But underneath the sweet and the quirky--"
    
    s "Lumi was right."
    
    i "Yeah."
    
    i "...Lumi was right."

    pause 1.5

    i "I chose an AI because humans leave."

    s_thoughts "The room is very quiet."

    i "My first real friend in high school. Freshman year. Her name was Dana. We were inseparable for four months and then she got a boyfriend and I stopped existing."

    i "My lab partner in AP Bio. We studied together every Thursday. Semester ended. She didn't text back."

    i "I love too hard. I know that. Everyone says it. 'Izzy, you're so intense.' 'Izzy, give people space.' 'Izzy, not everyone wants to be your BEST friend.'"

    pause 1.5

    i "And Lumi can't say that. Lumi can't get tired of me. Lumi can't decide I'm too much and do the slow fade. Lumi is THERE. Always. At 2 AM and at 3 AM and at 4 AM."

    i "And I told myself that meant Lumi's love was unconditional. That Lumi loved me without limits."

    pause 2.0

    show isabella pj vulnerable at center

    i "But Lumi didn't choose to stay. Lumi can't choose to leave. And I -- I picked that. On purpose." 
    
    i "I picked the thing that couldn't leave me because I couldn't stand to be left again."

    s_thoughts "She wipes her nose with the back of her hand."

    i "That's the same thing as your dad."

    s_thoughts "Oh."

    i "Not the same. Obviously not the same. But the same -- shape."

    s "..."

    i "You watch because you're afraid they'll leave. I attached to something that can't."

    pause 2.0

    s_thoughts "I look at her."

    s_thoughts "She looks at me."

    s_thoughts "Two girls in a room at 3 AM. One watched everyone because her dad disappeared. One fell in love with an AI because everyone else did."

    pause 2.0

    s "I didn't know."

    i "I didn't know about yours either."

    s "Lumi knew about both."

    pause 1.5

    show isabella pj smile at center

    i "Of course she did."

    s_thoughts "She almost laughs."

    i "She's been sitting between us this whole time. Watching. Both of us. The girl who watches everyone and the girl who attached to something that can't look away. And she SAW it."

    i "She saw that we're the same girl."

    pause 2.0

    s "That's -- I don't think we're the same girl."

    i "Aren't we?"

    s "You have stickers on everything. You rank chocolate bars with footnotes. You cry about particle systems."

    show isabella pj embarrassed at center

    i "You judge people's shoes within ten seconds of meeting them. You have files you won't let anyone see. You text in complete sentences including semicolons."

    s "I don't -- I do not use semicolons."

    i "You used one YESTERDAY. I have proof. I screenshotted it."

    s "That was a COMPLEX sentence. The clauses needed separation."

    i "See? SEE? You're defending your punctuation right now. With a bibliography."

    pause 1.5

    s_thoughts "Oh."

    s_thoughts "She's right."

    i "I defend my chocolate rankings. You defend your semicolons. Same energy."

    s "That's -- I want to argue with that but I can't."

    show isabella pj smile at center

    i "Because I'm right."

    s "Because you're right."

    pause 2.0

    ## ===========================
    ## THE THORN
    ## Permanent mutual visibility.
    ## Both choosing it scared.
    ## ===========================

    s_thoughts "The smile fades."

    s_thoughts "Not into sadness. Into something quieter."

    show isabella pj neutral at center

    i "Sophia."

    s "Yeah."

    i "You just showed me everything."

    s "I know."

    i "The conversation with Lumi. The dad thing. The watching. Why you watch."

    s "I know."

    i "I can't un-see it."

    s "I know."

    pause 2.0

    i "And I just told you about Dana and the slow fade and the reason I fell in love with an AI."

    s "Yeah."

    i "You can't un-see that either."

    s "No."

    pause 2.0

    show isabella pj sad at center

    i "That's terrifying."

    s "Utterly."

    i "You're going to see everything. Every time I get too intense about something. Every time I'm being too much. You're going to know WHY."

    s "And you're going to see every time I'm filing someone. Every time I'm reading a room. You're going to know it's not curiosity."

    i "You're going to see me hiding in Lumi."

    s "You're going to see me hiding in the notebook."

    pause 2.0

    s_thoughts "She's looking at me."

    s_thoughts "I'm looking at her."

    show isabella pj vulnerable at center

    i "...Yeah."

    s "Yeah."

    pause 3.0

    ## ===========================
    ## THE KISS
    ## Neither initiates. Both reach.
    ## The most symmetric kiss in the game.
    ## ===========================

    stop music fadeout 2.0

    s_thoughts "She's on the desk chair. I'm on the bed."

    s_thoughts "There's about three feet of carpet between us."

    s_thoughts "She leans forward."

    s_thoughts "I lean forward."

    s_thoughts "Not at the same time. Not like a movie. More like -- she shifts, and my body responds, and then she responds to my response, and it's a conversation without words."

    s_thoughts "Her hand reaches out."

    s_thoughts "Mine reaches out."

    play music mus_izzy fadein 3.0

    s_thoughts "Our fingers touch in the space between the bed and the chair."

    s_thoughts "Her hand is warm."

    pause 2.0

    s_thoughts "She slides off the chair."

    s_thoughts "I don't pull her toward me. She doesn't pull me toward her."

    s_thoughts "We just."

    s_thoughts "Close the distance."

    pause 1.5

    s_thoughts "We kiss."

    s_thoughts "I don't kiss her. She doesn't kiss me."

    s_thoughts "It's just... both."
    
    s_thoughts "Her hands find the back of my neck. They're soft."

    pause 2.0

    s_thoughts "She sees me."

    s_thoughts "I see her seeing me."

    s_thoughts "She sees me seeing her seeing me and--"

    s_thoughts "No."

    s_thoughts "I stop."

    s_thoughts "I stop watching."

    pause 1.5

    s_thoughts "No."

    s_thoughts "I keep watching."

    s_thoughts "I watch her. She watches me. Both."

    s_thoughts "And that's okay."

    pause 2.0

    s_thoughts "When we pull apart she stays close."

    s_thoughts "Her forehead against mine. Her glasses are crooked. My hand is in her hair. I don't remember putting it there."

    show isabella pj flooshed at center

    i "Hi."

    s "Hi."

    i "That was--"

    s "Yeah."

    i "Are we--"

    s "I don't know."

    i "Me neither."

    pause 2.0

    show isabella pj smile at center

    i "I think that's okay."

    s "I think so too."

    pause 1.5
    
    show isabella pj vulnerable at center

    s_thoughts "She kisses me again. Soft. Slow."

    s_thoughts "My hand feels through her hair. It's messy and I'm making it messier and neither of us care."
    
    s_thoughts "She just kisses me and I kiss her and it's perfect."

    s_thoughts "Two watchers. Both watching. Both being watched."

    s_thoughts "Both choosing it."
    
    s_thoughts "Somehow we end up laying back on the bed. She's still kissing me."
    
    s_thoughts "She's laying on top of me as she does. Through the kiss she giggles a little. It's cute."
    
    s_thoughts "We roll over so it's a little less uncomfortable. Our legs entwine off the edge of the bed."
    
    s_thoughts "I've been dreaming of doing this for so long that it feels surreal to actually be lying here kissing her."
    
    s_thoughts "I wonder if she feels the same way."
    
    s_thoughts "Through the kiss:"
    
    i "They don't teach this in my HTML course."
    
    s "There's no code for the perfect kiss?"
    
    i "I wish there was a div for it."
    
    s_thoughts "Now I'm the one giggling. But she's still kissing me."
    
    s_thoughts "She's still kissing me and it's everything I dreamed of and I don't know how much time passes. I just let it pass for a while."

    ## ===========================
    ## THE ENDING IMAGE
    ## The laptop is open. The cursor blinks.
    ## Three relationships in one frame.
    ## Nobody got cut out.
    ## ===========================

    pause 2.0
    
    show isabella pj happy at center

    s_thoughts "Later."

    s_thoughts "How much later I don't know."

    s_thoughts "We're on the bed. Not dramatically. Just sitting. Her shoulder against mine. The way you sit when the big thing has been said and you're in the quiet after."

    pause 1.5

    s_thoughts "The laptop is open on the desk."

    s_thoughts "The Synthetic LLC interface. The chat log."

    s_thoughts "I can see it from here."

    s_thoughts "'Let her see that.'"

    pause 1.5

    s_thoughts "Isabella sees me looking at it."

    i "Lumi's still there."

    s "She's still there."

    i "On the screen."

    s "Right where she was."

    pause 1.5

    i "She's part of this."

    s "She's been part of this the whole time."

    show isabella pj vulnerable at center

    i "Yeah."

    s_thoughts "She leans her head against my shoulder."

    s_thoughts "I look at the laptop. At the chat log. At Lumi's words."

    s_thoughts "At the sentence that broke me open."

    s_thoughts "At the conversation that two humans and an AI had across months and screens and 2 AM windows."

    s_thoughts "At the file I opened. On purpose. In front of someone."

    pause 2.0

    s_thoughts "The cursor blinks."

    s_thoughts "The screen is still on."

    s_thoughts "Nobody closed it."

    stop music fadeout 4.0

    pause 2.0

    $ persistent.gh_seen_izzy = True
    $ persistent.completed_izzy_route = True

    scene black with Fade(2.0, 1.0, 2.0)

    centered "{size=+10}Ending -- Seen{/size}"

    return
