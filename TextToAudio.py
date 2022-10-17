import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()

# convert this text to speech
text = "Prueba de audio"

# get details of speaking rate
engine.setProperty("rate", 180)

# get details of all voices available
voices = engine.getProperty("voices")

# set another voice
engine.setProperty("voice", voices[0].id)
#engine.say(text)

# saving speech audio into a file
engine.save_to_file(text, 'smile.mp3')

# play the speech
engine.runAndWait()