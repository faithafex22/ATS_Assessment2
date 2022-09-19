#Write a method that takes a word and a text and returns the positions the word is in the 
#text , If the word is not in the text, return 0.
def position(word, sentence):
    index_position= []
    word_positions = []
    sentence_list = sentence.split()
    for i in range(len(sentence_list)):
        if word not in sentence_list:
            index_position = 0
        elif sentence_list[i] == word:
            index_position.append(i)
    for i in index_position:
        j = i + 1
        word_positions.append(j)
    return f"The positions of {word} in the sentence is {word_positions}"

print(position("going", "what is going on here, going"))