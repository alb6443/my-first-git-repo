words = []
sortedWords=[]
# I am making a comment
with open('words','r') as f:
    words = f.read().splitlines()

words.sort(key=len, reverse=True)

print(words[:5])


