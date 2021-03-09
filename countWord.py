filename = "word.txt"
with open(filename, encoding="utf8") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
content = ''.join(content)
print(content)
print(len(content.split()))