# import csv
# import re
def exist_or_not(wod):
    try:
        if word_freq[wod]:
            print(f"frequency of '{wod}' is {word_freq[wod]} and it exists in the file")
    except KeyError:
        print(f"'{wod}' is not exist in the file")

filename = input("Enter filename: ")


# with open(filename,'r') as f:
try:
    with open(filename) as f:
        text = f.read().lower()
except FileNotFoundError:
    print("file not found")
    exit()
a_word = input("enter word: ")
#     a_words = re.findall(a_word, text)
# print(f"The word '{a_word}' is exist and it occures {len(a_words)} times in the file '{filename}'.")
words = text.split()
# print(words)
word_freq = {}

for word in words:  # words = list of all words
    word_freq[word] = word_freq.get(word, 0) + 1
# print(word_freq)
# print(word_freq.items())
# only_freq = list(word_freq.values())
sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

for wrd, freq in sorted_freq[:5]:
    print(f"{wrd}:{freq}")
# sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
# print(sorted_freq)
exist_or_not(a_word)
# print(only_freq)
# max_freq = max(only_freq)
# print(max_freq)
# i = 0
# while i < 6:
#     max_freq = max(only_freq)
    # print(max_freq)
    # for wrd in word_freq.keys():
        # print(wrd)
    #     if word_freq[wrd] == max_freq:
    #         print(f"{wrd}:{max_freq}")
    #     only_freq.remove(max_freq)
    #     word_freq[wrd].pop(wrd)
    #     break       
    # i += 1


    