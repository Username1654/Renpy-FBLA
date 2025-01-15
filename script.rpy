# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Z = Character("Zakiya")
define D = Character("Damonica")
define T = Character("Tourist")
transform resize_bg:
    xsize 2000
    ysize 1200

transform resize_sprite:
    xsize 900
    ysize 1000
    yalign 1.0
   



transform closeright:
    xalign 0.9
    yalign 1.0
    ysize 1000
    xsize 900


image bblack ="#000000"


default dPoints = 0
default zPoints = 0
default pPoints = 0

label start:

   

    show bg forest at resize_bg 
    play music "forest.mp3"
    
    show zakiya confused at resize_sprite
    Z "zzz…"
    hide zakiya
    show damonica happy at closeright
    D "Wake up Zakiya! If you don't, I'm going to go out by myself!"
    hide damonica
    show zakiya confused at resize_sprite
    Z " I wanted to sleep a little longer…"
    hide zakiya
    show damonica happy at closeright
    D " Early bird gets the worm!"
    hide damonica
    show zakiya confused at resize_sprite
    Z "Wait…I'll get up in a second!"
    hide zakiya
    show damonica happy at closeright
    D "I'm already leaving without you!!!"
    
    # next part
    hide damonica
   
    show bg sleep at resize_bg
    with fade
    play music "sleeping.mp3"
    show zakiya confused at resize_sprite
    Z "Seriously?"
    show bblack with Dissolve(1.0)
    Z "(I'm going to take in the air a bit more then...)"
    Z "(Me and Damonica have been friends for as long as I can remember.)"
    Z "(You could say that we're childhood friends, but it's been far longer than just childhood.)"
    Z "(You could say eternal friends, it's not like we'll cease to exist anytime soon...)"
    Z "(What do we do? What can we do?)"
    Z "(Well we've been dragging others into this forest for centuries! It's what we can call our game!)"
    Z "(Though recently, I feel like somethings changed...)"
    Z "(I shouldn't indulge too much in this feeling though, I still have to meet with Damonica.)"
    Z "(Well then, I should get going!)"
    hide zakiya
    hide bblack with Dissolve(1.0)

    # next scene
    
    show bg forest at resize_bg
    with fade
    play music "forest.mp3"
    
    show damonica happy at closeright
    D "Finally! You're here! I've been waiting for you all day!"
    hide damonica
    show zakiya confused at resize_sprite
    Z "I thought you said you would go on without me?"
    hide zakiya
    show damonica happy at closeright
    D " If you were human, I would've eaten you up already!"
    hide damonica
    show zakiya confused at resize_sprite
    Z "If we were human, but we're not."
    hide zakiya
    show damonica happy at closeright
    D "If we were really, I probably would have disappeared already! Several centuries ago, actually!"
    hide damonica
    show zakiya confused at resize_sprite
    Z " Both of us…"
    hide zakiya
    show damonica happy at closeright
    D " But that's good! I like being the one to bring humans to an end, it'd just be boring if it was the other way around."
    D " Since we're like this, we can see so many humans cross to the other side! "
    D " It would just be sad if we only saw one."
    hide damonica
    show zakiya confused at resize_sprite
    Z "..."
    Z "Actually, I was thinking, isn't it getting boring just watching this though?"
    hide zakiya
    show damonica happy at closeright
    D "…What do you mean? We've always done this with no problem?"
    hide damonica
    show zakiya confused at resize_sprite
    Z "I mean, I want to see what's beyond just the end!"
    Z "It starts getting too boring if there’s just the same old scene with no feelings for us about it."
    hide zakiya
    show damonica happy at closeright
    D "Are you saying we should get to know them?"
    hide damonica
    show zakiya confused at resize_sprite
    Z "It sounds a little stupid, but we could get better results from it."
    Z "For example, the forests with certain urban legends always get super popular with influencers! Probably could drag in a couple more people here and there."
    hide zakiya
    show damonica happy at closeright
    D "I guess that's true, but I don't like associating with them, so it better be quick."
    hide damonica
    show zakiya confused at resize_sprite
    Z "Yeah, of course!"
    
    show bblack with Dissolve(1.0)
    play music "Night.mp3"
    "Some time later in the night"
    show bg night at resize_bg
    with fade
    hide bblack with Dissolve(1.0)

    

    Z "(...)"
    Z "(Somehow, feel a little bad for them...)"

    #scene 3

    hide zakiya
    show damonica happy at  closeright
    D "So, Zakiya, how do we go about this?"
    hide damonica
    show zakiya confused at resize_sprite
    Z "First, we try to scare our “guests” without making them disappear."
    Z "This gives them a chance to tell their stories and make our forest known!"
    Z "People will be dying to check out our forest after they hear of supernatural events, humans are just too curious."
    hide zakiya
    show damonica happy at resize_sprite
    D "I like that plan! Let's set up and get started!"
    hide damonica
    show zakiya confused at resize_sprite

    #next part, at night

    Z "(Is this really what I want?)"
    Z "(These humans don’t know any better, do they really deserve this?)"

    #scene 4, daytime

    hide zakiya
    show damonica happy at  closeright
    D "Wake up Zakiya! I found the perfect spot for our plan."
    hide damonica
    show zakiya confused at resize_sprite
    Z "(Actually, I haven't really been able to sleep a lot.)"
    Z "(Not that we need sleep, it just gets tiring spending every waking moment like this…)"
    hide zakiya
    show damonica happy at  closeright
    
    D "It gets boring waiting all the time!"
    hide damonica
    show zakiya confused at resize_sprite
    Z "I’m going, you have absolutely no patience…"
    D "Hurry up! They’re right around the corner!"
    hide damonica
    show zakiya confused at resize_sprite
    # placeholder "Honestly, I just wanted to get away from all this…"
    Z "(Facing troubles, huh?)"
    #placeholder "Maybe I’ll just camp out here for the night…"

    #switch bg to night

    T "The sky looks so pretty tonight… I’ll take a picture and post it, it’ll probably get lots of likes"
    hide zakiya
    show damonica happy at  closeright
    D "We didn’t even get to do anything yet…"
    hide damonica
    show zakiya confused at resize_sprite
    Z "It’s best to not reveal ourselves if we’re doing this though."
    hide zakiya
    show damonica happy at  closeright
    D "Hmph."
    hide damonica
    show zakiya confused at resize_sprite
    Z "If they are already aware that we’ll be here, they’ll be more cautious."
    Z "It’s easier to catch someone off guard."
    hide zakiya
    show damonica happy at  closeright
    D "We do have to talk to someone though, isn’t that what you wanted?"
    hide damonica
    show zakiya confused at resize_sprite
    Z "Yes, but we should get someone who is alone and troubled, so that it wouldn’t cause too much commotion as to get search parties in this place, that’d just get annoying."
    hide zakiya
    show damonica happy at  closeright
    D "Then if the tourist here already meets these requirements… We could just tempt her to come back so people could figure out that she was here last!"
    D "People could get curious and look on their own but not in a huge group because that would just be weird."
    hide damonica
    show zakiya confused at resize_sprite
    Z "This is great!"

    #scene 5

    D "How do we start scaring them?"
    menu: 
        "ghost noises":
            $ zPoints += 1
        
        "hallucinations":
            $ zPoints -= 1

if zPoints == 1:
    jump silly
else :
    jump crazy

label silly:
    hide damonica
    show zakiya confused at resize_sprite
    Z "Ghost noises, we should start with something simple so we can build up to something exciting!"
    Z "This is going to be so much fun!"
    D "No…this is too boring… I’m going to give them hallucinations!!!"
    jump jump


label crazy:
    hide damonica
    show zakiya confused at resize_sprite
    Z "We could start giving them hallucinations, it could add a scarier effect and lead to more publicity!"
    hide zakiya
    show damonica happy at  closeright
    D "Sounds great!"
    hide damonica
    show zakiya confused at resize_sprite
    label jump:
    Z "Alright then!"
    hide zakiya
    T "AAAAAAAAAAAAAAAA!!!"
    
    show damonica happy at  closeright
    D "Yay!"
    hide damonica
    show zakiya confused at resize_sprite
    Z "(Seeing this is fun, but I kind of have a sinking feeling…)"
    hide zakiya
    show damonica happy at  closeright
    D "You sure you want to keep going with this? I mean we can totally end them right now! I’m sure they already posted the picture!"

    menu: 
        "KILL":
            $ dPoints += 1
        
        "Give up on him":
            $ dPoints -= 1

if dPoints == 1:
    jump murder
else :
    jump Smth

label murder:
    hide damonica
    show zakiya confused at resize_sprite
    Z " Of course not, I wouldn’t want to miss this opportunity! After all, the other option would just get too time-consuming!"
    hide zakiya
    show damonica happy at  closeright
    D "Yes! Then let’s get a move on!"
    hide Z
    show bg red at resize_bg
    with fade
    
   
return #murder end

label  Smth:
    Z "…Hey, so I was actually thinking…What if we just stopped doing all this, even for a bit? I think this is starting to drain me…"
    Z "I mean, we already are getting tired of all this, why not try for something new?"
    hide zakiya
    show damonica happy at  closeright
    D "But we were just doing so good…this is just annoying."
    hide damonica
    show zakiya confused at resize_sprite
    Z "I know but, living like this for an eternity? Doesn’t that sound boring?"
    hide zakiya
    show damonica happy at  closeright
    D "But its the only thing that we’ve been doing all this time! Why try to change now?"
    hide damonica
    show zakiya confused at resize_sprite
    Z "The times have always been changing! How long has it been since we’ve taken a moment to notice how everything has changed already?"
    Z "Even this forest that we’ve lived in for all of our lives, haven’t you noticed that half of its been destroyed by the people?"
    hide zakiya
    show damonica happy at  closeright
    D "We don’t need to change if we have each other!"
    D "What’s up with this nonsense? There’s no reason for anything to change…lets keep what we already have and protect it!"
    menu: 
        "Stop cycle":
            $ pPoints += 1
        
        "Continue cycle":
            $ pPoints -= 1

if pPoints == 1:
    jump good
else :
    jump bad

label good:
    hide damonica
    show zakiya confused at resize_sprite
    Z "Is it really okay to never change? We’re still kids because we don’t want to grow up. Isn’t it time we move on to the next level?"
    hide zakiya
    show damonica happy at  closeright
    D "I just don’t want “us” to change!!!"
    hide damonica
    show zakiya confused at resize_sprite
    Z " There’s no reason to be scared! Just because we’re changing doesn’t mean we need to separate!"
    hide zakiya
    show damonica happy at  closeright
    D "Then…I could guess it’s fine…"
    hide damonica
    show zakiya confused at resize_sprite
    Z " Let’s make it a promise then!"
    hide zakiya
    show damonica happy at  closeright
    D " A promise is good…I’m glad…"
    hide damonica
    show zakiya confused at resize_sprite
    Z "Let’s stay together for our eternity!!!"
    hide zakiya
    show damonica happy at  closeright
    D "Yes! Let’s!"
    return 

label bad:
    hide damonica
    show zakiya confused at resize_sprite
    Z " I guess I do value you more than some silly thought…"

return #ending for smth
