import pyttsx3
engine = pyttsx3.init()

import numpy as np
filename = "srt.srt"
with open(filename,encoding="utf8") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
voices = engine.getProperty('voices')   
engine.setProperty('voice', voices[1].id)
content = [item for item in content if item != ""]
text = []
for i,value in enumerate(content):
   if (i%3 == 2):
       text.append(content[i])
text = " ".join(text)
print(text)
engine.say(text)
engine.runAndWait()


