from textblob import TextBlob

blob = TextBlob("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife!")
print(blob.translate(from_lang="en", to="ru"))


quote1 = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."

quote2 = "Darcy, as well as Elizabeth, really loved them; and they were both ever sensible of the warmest gratitude towards the persons who, by bringing her into Derbyshire, had been the means of uniting them."

sentiment1 = TextBlob(quote1).sentiment
sentiment2 = TextBlob(quote2).sentiment

print(quote1 + " has a sentiment of " + str(sentiment1))
print(quote2 + " has a sentiment of " + str(sentiment2))