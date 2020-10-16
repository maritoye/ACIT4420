"""
Marit Øye Gjersdal
s348588
"""

f = open("python.txt")

characters = ["\n", ".", ",", "(", ")", '"', "'s", "'"]
data = f.read()
for c in characters:
	data = data.replace(c, " ")
# if I use strip() instead of replace() I get the same results as the example in the task sheet
# however this solution gives a more correct result

words = data.split()
wordcount = {}

for w in words:
	if w in wordcount:
		wordcount[w] += 1
	else:
		wordcount[w] = 1

for w in wordcount:
	if wordcount[w] > 3:
		print(w + ": " + str(wordcount[w]))