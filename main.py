def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_num_words(text)
    count_letters = get_num_letters(text)
    print(f"--- Begin report of {book_path} ---")   
    print(f"{count_words} words found in the document\n")   
   # print(f"number of letters: {count_letters}")
    
    for letter, count in count_letters.items():
        print(f"The '{letter}' character was found {count} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    letter_counts = {}
    lowered_string = text.lower()
    for letter in lowered_string:
        if letter.isalpha(): # Outer if: checks if the character is a letter
            if letter in letter_counts: # Inner if: executes if letter is already in dictionary
                letter_counts[letter] += 1
            else: # Executes if letter is not in the dictionary
                letter_counts[letter] = 1

    # Sort the dictionary by keys, and store it in a new variable
    return dict(sorted(letter_counts.items()))                      

    
def get_book_text(path):    
    with open(path) as f:
        return f.read()



main()