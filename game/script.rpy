# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Maya")
define a = Character("Amma")


# The game starts here.

label start:
    play music "audio/backgroundmusic.mp3"

    scene bedroom
    with fade 
    
    "On a lazy autumn morning, Maya Anderson woke up and got out of her bed."
    show maya
    with dissolve
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


label kitchen:
    scene kitchen
    with fade
    "Maya went to the kitchen to start her cup of coffee."

    show maya
    with dissolve

    "As it was brewing, something caught her eye."

    m "Huh? What's this?"

    # Display the note interaction
    jump fridge


label fridge:
    stop music fadeout 1.0
    scene fridge 
    "There was a note on the fridge from her husband, George."

    "Maya, Janu called again. I told her you would call back later. See you tonight. - George"

    "Maya saw a number at the end of the note."

    menu:
        "Maya..."
         
        "Called the number":
            jump call

        "Crumpled the note and threw it away":
            jump crumpled


label call:
    scene fridge
    show phone
    with dissolve

    "Maya called the number."
    "As the phone rang, her fingers shivered in nervousness as she remembered why she never picks up anymore..."
    
    jump flashback


screen imageButton():
    imagebutton idle "images/phone.png" action Jump('phoneCall') pos (0.5, 0.9) anchor (0.5, 1.0)


label crumpled:
    play sound "<from 0.0 to 2.0>crumping-paper.mp3"
    show maya
    "Maya crumpled up the note and threw it away. She could not believe the audacity her grandmother had after everything."

    "A couple of hours later, her phone started to ring. It was her mother"
    hide maya
    play sound "audio/phone-ringing.mp3" loop
    call screen imageButton



label phoneCall:
    scene fridge
    stop sound

    m "Hello? Amma?"

    a "Maya? What is wrong with you? Why haven't you called Janu Pati?"

    m "You know why. She's always making some comment about me or Kunal. I can't stand it."

    a "She's sick Maya. Nobody else lives in the U.S. What will people think? Call her now."

    "The phone clicked as her mother hung up."

    "Maya sighed with frustration. She would not hear the end of it if she didn't call her grandmother."

    "Her fingers trembled as she pressed each number, remembering her Janu Pati's comments..."
    show phone
    
    jump flashback


label flashback:
    scene crochetbg
    with fade
    "Janu used to criticize Maya for every little thing, especially her choices with Kunal."
    "The sting of those comments echoed in her mind as she dialed the number..."
    
    return
