class Text:
    def __init__(self, text):
        self.text = text

    def count_characters(self):
        return len(self.text)

    def count_letters(self):
        return sum(1 for char in self.text if char.isalpha())

    def count_spaces(self):
        return self.text.count(' ')

    def count_characters_without_spaces(self):
        text_without_spaces = self.text.replace(' ', '')
        return len(text_without_spaces)

    def get_words(self):
        words = self.text.split()
        return words

    def get_sentences(self):
        sentences = self.text.split('.')
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return sentences

