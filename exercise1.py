words = []
sortedWords=[]

with open('words','r') as f:
    words = f.read().splitlines()

words.sort(key=len, reverse=True)

print(words[:5])


