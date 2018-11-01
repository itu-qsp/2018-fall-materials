# 7-2.py
class Cleaner:
    """ Removes rude words from text. When text is a list of strings, the
    clean_line(text) method removes occurrences of rude words and replaces them by *beep!*.
    """
    def __init__(self, forbidden_word="frack"):
        """ Set the forbidden word """
        self.word = forbidden_word
    
    def clean_line(self, line):
        """Clean up a single string, replacing the forbidden word by
        *beep!*"""
        return line.replace(self.word, "*beep!*")

    def clean(self, text):
        for i in range(len(text)):
            text[i] = self.clean_line(text[i])

    def set_word(self, new_word):
        self.word = new_word
