from textblob import TextBlob

pap = open("../data/prideandprejudice.txt")
dat = TextBlob(pap.read())

pos = []
neg = []

for s in dat.sentences:
    if s.sentiment.polarity == 1:
        pos.append(s)
    if s.sentiment.polarity == -1:
        neg.append(s)

print("The " + str(len(pos)) + " most positive sentences:")
for sentence in pos:
    print("+ " + str(sentence.replace("\n", "").replace("      ", " ")))

print("The " + str(len(neg)) + " most negative sentences:")
for sentence in neg:
    print("- " + str(sentence.replace("\n", "").replace("      ", " ")))

