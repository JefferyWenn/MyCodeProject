"""
File: anagram.py
Name: 溫孟哲
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
# Global variables
dictionary = []


def main():
    """
    The program prompts the user for a word and finds all the anagrams for that word.
    """
    start = time.time()
    ####################
    read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\"  (or -1 to quit)")
    while True:
        user_input = input("Find anagrams for: ")
        if user_input == EXIT:
            break
        else:
            print('Searching...')
            anagrams = find_anagrams(user_input)
            print(f'{len(anagrams)} anagrams: {anagrams}')
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as file:
        for line in file:
            word = line.strip()
            dictionary.append(word)


def find_anagrams(s):
    """
    :param s: The word to find anagrams for.
    :return: A list of all the anagrams found.
    """
    anagrams = []
    find_anagrams_helper(s, '', anagrams)
    return anagrams


def find_anagrams_helper(s, current, anagrams):
    if len(s) == 0:
        if current in dictionary and current not in anagrams:
            anagrams.append(current)
            print(f'Found: {current}')
            print('Searching...')
    else:
        for i in range(len(s)):
            # Choose
            current += s[i]
            remaining = s[:i] + s[i+1:]
            # Explore
            if has_prefix(current):
                find_anagrams_helper(remaining, current, anagrams)
            # Unchoose
            current = current[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: The prefix to check.
    :return: bool, if there are words starting with the prefix.
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()  
