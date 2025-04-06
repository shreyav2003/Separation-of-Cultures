# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Maya")
define a = Character("Amma")
define j = Character("Janu")

# The game starts here.
init python:
   def drag_placed(drags, drop): 
       if not drop: 
           return 
       store.draggable = drags[0].drag_name
       store.droppable = drop.drag_name
       return True
label start:
    play music "audio/backgroundmusic.mp3"

    scene bedroom
    with fade 
    
    "On a lazy autumn morning, Maya Anderson woke up and got out of her bed."

    menu:
        "As she put on her slippers she decided to..."
         
        "Walk into her son's bedroom":
            jump kunalBed

        "Walk to the kitchen":
            jump kitchen


label kunalBed:
    scene kunal sleeping
    with fade 

    "She smiled, taking in her child. She saw herself in his ears, his skin. She saw her husband in his nose."

    "Maya always loved his nose the most."
    
    "She leaned down to his ear."

    m "I love you, Kunal."
    
    jump kitchen

screen dragKitchen:
    draggroup:
        drag:
            drag_name "mug"
            child "mug.png"
            xpos 100 ypos 100
            draggable True
            droppable False

        drag:
            drag_name "coffee"
            xpos 900 ypos 300
            child "coffee.png"
            draggable False
            droppable True
label kitchen:
    "Maya went to the kitchen to start her cup of coffee."
    scene kitchen
    call screen dragKitchen


label brewing:
    scene kitchen 
    show coffeemug
    "As it was brewing, something caught her eye."

    m "Huh? What's this?"

    # Display the note interaction
    jump fridge


label fridge:
    stop music fadeout 1.0
    scene fridge 
    "There was a note on the fridge from her husband, George."

    "Maya, Janu called again. She says she's coming tomorrow I told her you would call back later. See you tonight. - George"

    "Maya saw a number at the end of the note."

    menu:
        "Maya..."
         
        "Called the number":
            jump call

        "Crumpled the note and threw it away":
            jump crumpled


label call:
    scene fridge
    show digiphone
    with dissolve

    "Maya called the number."
    play sound "audio/dial-tone.mp3" loop
    hide digiphone
    show phone
    with dissolve
    "As the phone rang, her fingers shivered in nervousness as she remembered why she never picks up anymore..."
    
    jump flashback


screen imageButton():
    imagebutton idle "images/digiphone.png" action Jump('phoneCall') pos (0.5, 0.9) anchor (0.5, 1.0)


label crumpled:
    play sound "<from 0.0 to 2.0>crumping-paper.mp3"
    scene fridgenn
    "Maya crumpled up the note and threw it away. She didn't want to deal with Janu Pati today."

    "A couple of hours later, her phone started to ring. It was her mother"
    play sound "audio/phone-ringing.mp3" loop
    call screen imageButton



label phoneCall:
    scene kitchen
    show maya
    stop sound

    m "Hello? Amma?"

    a "Maya? What is wrong with you? Why haven't you called Janu Pati?"

    m "You know why. She's always making some comment about me or Kunal. I can't stand it."

    a "She's sick Maya. Nobody else lives in the U.S. What will people think? Call her now. She will be coming tomorrow."

    "The phone clicked as her mother hung up."

    "Maya sighed with frustration. She would not hear the end of it if she didn't call her grandmother."
    show phone
    play sound "audio/dial-tone.mp3" loop

    "Her fingers trembled as she pressed each number, remembering her Janu Pati's comments..."
   
    
    jump flashback


label flashback:
    stop sound
    scene crochetbg
    with fade
    show janucrocheted
    "Janu could never seem to leave Maya alone. There was always something to say."
   
    j "Maya kutty, your hair is so short. Why do you always have to act like them?"
    j "Maya, it's improper to wear your skirt that short. What will people say? I raised you to be better."
    j "Maya, you cannot raise Kunal like this. "
    menu:
        "Maya..."
         
        "Would fight her grandmother's comments":
            jump fightFlashback

        "Would stay silent.":
            jump silentFlashback
label fightFlashback:
    show janucrocheted
    m "Janu Pati, you are extremely disrespectful! I like who I am!"
    scene crochetredbg
    with vpunch
    show janucrocheted
    j "Who taught you how to speak like this? Was it that husband? I knew it was a bad idea to send you to America."
    m "Pati please..."
    j "No! Is this how you're going to raise Kunal? Like a disrespectful American?"
    jump present
label silentFlashback:
    scene crochetedbg
    show janucrocheted
    "Maya stayed silent. She didn't want to fight with her grandmother."
    j "Nothing to say Maya?"
    m "I'm sorry. I have to go, I'll talk to later."
    "She never called her back."
    jump present
    


label present:
    scene kitchen
    show digiphone
    with dissolve
    "Maya's eyes welled up with tears as she remembered the conversation."
    j "Hello?"
    m "Janu Pati, it's Maya. How are you?"
    j "I'm glad my granddaughter has finally called her sick grandmother back."
label present2:
    scene kitchen
    show digiphone
    with hpunch
    "Maya felt a pang of anger go through her."
    m "I'm sorry I haven't called back. It's been busy here."
    j "I'm sure you have been with that so called cooking job."
    m "Pati, I'm a chef we've been over this. Look, I heard you were coming tomorrow. What time is your flight?"
    j "I'm coming at 5, Maya. I expect everything to be ready for me."
    "Maya sighed. A wave of anxiousness flowed through her, as she pondered what to do next."

    return
