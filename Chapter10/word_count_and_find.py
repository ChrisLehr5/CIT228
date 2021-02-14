print("------------------------------Hands On #3-----------------------------------------")
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

#'C:/Users/Khyr/Desktop/CIT228/Chapter10/ absolute path'
filenames = ['C:/Users/Khyr/Desktop/CIT228/Chapter10/song_of_durin.txt', 'C:/Users/Khyr/Desktop/CIT228/Chapter10/bride_of_the_sea.txt', 'C:/Users/Khyr/Desktop/CIT228/Chapter10/amores.txt']
for filename in filenames:
    count_words(filename)

print("------------------------------Hands On #3, Excercise 10-10-----------------------------------------")
def count_specific_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        print(f"The word '{word}' appears in {filename} about {word_count} times.")

for filename in filenames:
    count_specific_words(filename, 'the')

print("------------------------------With a Space-----------------------------------------")
for filename in filenames:
    count_specific_words(filename, 'the ')