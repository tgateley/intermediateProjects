text_block = input("Enter a block of text for analysis: ")
total_char = 0
words_per_sentence = 0

# Make a list of all the words
text = text_block.split(" ")

# Get the total number of characters not including spaces
for word in text:
    total_char = total_char + len(word)

# Get the total number of words
word_count = len(text)

# get the total number of sentences
sentences = text_block.split(".")
total_sentences = len(sentences)

# get the average number of words per sentence
for sentence in sentences:
    sentence = sentence.split(" ")
    words_per_sentence = words_per_sentence + len(sentence)
avg_sentence_length = words_per_sentence/total_sentences

# Get the average word length
avg_word_length = total_char/word_count

# Most frequent word
words = {}
for word in text:
    word = word.strip(",")
    word = word.lower()
    if word in words.keys():
        words[word] = words[word] + 1
    else:
        words[word] = 1
words_list = [(value, key) for (key, value) in words.items()]
words_list = sorted(words_list, reverse=True)
key, value = words_list[0]

print(f"""
Text Analysis Results:
----------------------
Total Characters: {total_char}
Total Words: {word_count}
Most Frequent Word: '{value}' used {key} times: 
Average Word Length: {round(avg_word_length, 2)}
Average Sentence Length: {round(avg_sentence_length, 2)} words""")

