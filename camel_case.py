"""
There is a sequence of words in CamelCase as a string of letters, s, having the following properties:

It is a concatenation of one or more words consisting of English letters.

All letters in the first word are lowercase.

For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given s, determine the number of words in s.

Example
s = oneTwoThrees=oneTwoThree

There are 3 words in the string: 'one', 'Two', 'Three'.
"""


def camelcase(s: str) -> int:
    word_count = 1

    for char in s:
        if char.isupper():
            word_count += 1

    return word_count


if __name__ == '__main__':
    print(camelcase('oneTwoThree'))
