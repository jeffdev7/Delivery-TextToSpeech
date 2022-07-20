import voice
import customers

voice.engine.say("Hi! May you confirm your ID, please.")
voice.engine.runAndWait()
ID = input('Your ID with punctuation, please.\n')

def Again():
    newChance = input('Try it again.\n')
    if newChance in customers.setCustomersId:
     print(newChance + " confirmed.")
     voice.engine.say("Thank you! Have a nice day")
    else:
        voice.engine.say("There might've been a misunderstanding. I'm sorry.")

if ID in customers.setCustomersId:
    print(ID + " confirmed.")
    voice.engine.say("Thank you! Have a nice day")
else:
    print("That's not in our database.")
    voice.engine.say("That's not in our database.") 
    voice.engine.runAndWait()
    Again()

voice.engine.runAndWait()
voice.engine.stop()