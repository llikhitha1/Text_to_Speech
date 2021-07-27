from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
language="en"
text1=input()
sp=gTTS(text=text1,lang=language,slow=False)
sp.save(audio)
playsound(audio)


