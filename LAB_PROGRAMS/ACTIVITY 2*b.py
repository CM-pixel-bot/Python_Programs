def count_words_and_frequencies(sentence):
    words = sentence.split()  # Split the sentence into words
    word_frequencies = {}  # Create an empty dictionary to store word counts
    
    for word in words:
        word = word.lower()  # Convert to lowercase for consistent counting
        if word in word_frequencies:
            word_frequencies[word] += 1  # Increase count if word exists
        else:
            word_frequencies[word] = 1  # Add word to dictionary if new
    
    total_words = len(words)  # Get total number of words
    return total_words, word_frequencies

# Get user input
sentence = input("Enter a sentence: ")

# Get word count and frequencies
total_words, word_frequencies = count_words_and_frequencies(sentence)

# Display results
print("Total words:", total_words)
print("Word frequencies:")
for word, count in word_frequencies.items():
    print(word, ":", count)

OUTPUT:
Enter a sentence: He is good boy
Total words: 4
Word frequencies:
he : 1
is : 1
good : 1
boy : 1
