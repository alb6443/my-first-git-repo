words = []
sortedWords=[]

with open('/usr/share/dict/words','r') as f:
    words = f.read().splitlines() #I am commenting here

words.sort(key=len, reverse=True)

print(words[:5])


