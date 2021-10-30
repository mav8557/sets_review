# Michael Vaughan

import time

ENGLISH_WORDS = "words.txt"
DATA_FILE = "matrix.txt"


def english_count(datafile, words):
    """
    Given a filename, get the number of words
    that are english words in the file and return it.

    This works by converting every word in the file to lowercase,
    so it can be compared to the list of words from the dictionary.
    """

    count = 0

    with open(datafile) as fd:
        for line in fd:
            for word in line.split():
                if word.lower() in words:
                    count += 1
    
    return count


def get_words(wordsfile):
    """
    Open a file of newline-separated
    english words, and return a list of
    those words

    abc
    abcde      =>     [abc, abcde, apple]
    apple

    """
    words = []
    with open(wordsfile) as fd:
        for line in fd:
            words.append(line.strip())
    return words


def get_words_set(wordsfile):
    """
    Open a file of newline-separated
    english words, and return a list of
    those words

    abc
    abcde      =>     [abc, abcde, apple]
    apple

    """
    words = set()
    with open(wordsfile) as fd:
        for line in fd:
            words.add(line.strip().lower())
    return words


def main():
    
    # get words to check against
    words = get_words_set(ENGLISH_WORDS)
    
    # get time taken
    start = time.time()
    count = english_count(DATA_FILE, words)
    end = time.time()

    # print results
    print("Count:", count)
    print("Total time taken:", end-start)


if __name__ == "__main__":
    main()
