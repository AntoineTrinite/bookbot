def main():
    count = 0
    word_count = {}

    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    no_l_words = file_contents.lower()
    words = no_l_words.split()
    for word in words:
        count += 1

        # partie lettres
        for letter in word:
            if letter.isalpha():
                if letter in word_count:
                    word_count[letter] += 1
                else:
                    word_count[letter] = 1
    
    wordlist = list(word_count)
    sorted_wordlist = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    for letter, letter_count in sorted_wordlist:
        print(f"The'{letter}' character was found {letter_count} times")
    print("--- End report ---")

    
main()