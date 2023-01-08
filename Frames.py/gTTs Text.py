# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
from playsound import playsound
  
# The text that you want to convert to audio.
mytext = input('Enter your Text here: \n')

# Language in which you want tro convert 
language = input("Enter Language Code: \n")
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed & accent is US-en[com](default).
myobj = gTTS(text=mytext, lang=language, slow=False, tld='com') 

# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
playsound("welcome.mp3")

