# 7-3.py
class Cleaner:
    """ Removes rude words from text. When text is a list of strings, the
    clean_line(text) method removes occurrences of rude words and replaces them by *beep!*.
    """
    def __init__(self, forbidden_words=["frack"]):
        """ Set the forbidden words """
        self.words = forbidden_words
    
    def clean_line(self, line):
        """Clean up a single string, replacing any forbidden words by
        *beep!*"""
        for word in self.words:
            line = line.replace(word, "*beep!*")
        return line

    def clean(self, text):
        for i in range(len(text)):
            text[i] = self.clean_line(text[i])

    def set_words(self, new_words):
        self.words = new_words

c = Cleaner(['shit', 'frack', 'bloody'])
print(c.clean_line('What a piece of bloody frack shit work'))
