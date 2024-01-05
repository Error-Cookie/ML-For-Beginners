from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

extractor = ConllExtractor()

while True:
    q = input("> ")
    if q.lower() == "bye":
        break
    else:
        qb = TextBlob(q, np_extractor=extractor)
        np = qb.noun_phrases
        if qb.polarity <= -0.5:
            response = "Oh dear, that sounds bad. "
        elif qb.polarity <= 0:
            response = "Hmm, that's not great. "
        elif qb.polarity <= 0.5:
            response = "Well, that sounds positive. "
        elif qb.polarity <= 1:
            response = "Wow, that sounds great. "

        print(response)
        if len(qb.noun_phrases) > 0:
            print(f"Can you tell me more about {qb.noun_phrases[0]}?")

print("Bye!")