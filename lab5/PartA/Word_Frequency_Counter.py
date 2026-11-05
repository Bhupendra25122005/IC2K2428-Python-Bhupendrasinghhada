
# Q4. Word Frequency Counter using Dictionaries

# Input paragraph
paragraph = input("Enter a paragraph: ")

# 1. Clean the paragraph
paragraph = paragraph.lower()

# Remove punctuation manually without using any library
cleaned_text = ""

for char in paragraph:
    if char.isalnum() or char.isspace():
        cleaned_text += char

words = cleaned_text.split()

# Handle empty input
if len(words) == 0:
    print("No words entered. Please enter a paragraph.")
else:
    # 2. Count word frequency using get()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("\nWord Frequencies:")
    print(frequency)

    # 3. Print top N words
    n = int(input("\nEnter N to display top N words: "))

    # Sort by frequency descending and alphabetically for ties
    sorted_words = sorted(
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    )

    print("\nTop", n, "Words:")

    if n <= 0:
        print("Please enter a positive value for N.")
    else:
        for word, count in sorted_words[:n]:
            print(word, "(", count, ")")

    # 4. Words appearing exactly once
    single_words = sorted([
        word for word, count in frequency.items()
        if count == 1
    ])

    print("\nWords Appearing Exactly Once:")
    print(", ".join(single_words) if single_words else "None")

    # 5. Invert dictionary: frequency -> list of words
    inverted = {}

    for word, count in frequency.items():
        inverted.setdefault(count, []).append(word)

    # Sort each list of words
    inverted = {
        count: sorted(word_list)
        for count, word_list in inverted.items()
    }

    print("\nInverted Dictionary:")
    print(inverted)

    # 6. Group unique words by length
    length_groups = {}

    for word in frequency:
        length = len(word)
        length_groups.setdefault(length, []).append(word)

    # Sort each group and the dictionary by word length
    length_groups = {
        length: sorted(word_list)
        for length, word_list in sorted(length_groups.items())
    }

    print("\nWords Grouped by Length:")
    print(length_groups)

    # 7. Search for a word
    search_word = input("\nEnter a word to search: ").lower()

    # Clean punctuation from the searched word too
    cleaned_search = ""

    for char in search_word:
        if char.isalnum():
            cleaned_search += char

    if cleaned_search in frequency:
        print(
            "The word",
            cleaned_search,
            "appears",
            frequency[cleaned_search],
            "time(s)."
        )
    else:
        print("Word not found.")