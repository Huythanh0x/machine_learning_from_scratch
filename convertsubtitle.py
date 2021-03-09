import numpy as np
filename = "srt.srt"
with open(filename,encoding="utf8") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
engine.setProperty('voice', voices[1].id)
content = [item for item in content if item != ""]
text = []
for i,value in enumerate(content):
   if (i%3 == 2):
       text.append(content[i])
with open('text.txt', 'w') as filehandle:
    for t in text:
        filehandle.write('%s\n' % t)