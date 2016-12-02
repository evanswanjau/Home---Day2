def words(sentence):
  words = {}
  for w in sentence.split():
    words[w] = words.get(w, 0) + 1
  for w in words:
    print(w, words[w])