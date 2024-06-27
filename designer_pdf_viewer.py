"""
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle.
In this PDF viewer, each word is highlighted independently.

There is a list of 26 character heights aligned by index to their letters.
For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string.
Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.
"""


def designer_pdf_viewer(h: list[int], word: str) -> int:
    max_height: int = 0
    for w in word:
        height = h[ord(w) - ord('a')]
        if height > max_height:
            max_height = height
    return max_height * len(word)


if __name__ == '__main__':
    result: int = designer_pdf_viewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                                      'abc')
    print(result)
