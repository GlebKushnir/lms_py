# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string

text = str(input("Type in a series of words to create a #hashtag: ")).title()
for symbol in string.punctuation:
    text = text.replace(symbol, "")
text = text.replace(" ", "")

hashtag = "#" + text

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
