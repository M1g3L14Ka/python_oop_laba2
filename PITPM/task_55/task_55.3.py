class Text:
    def __init__(self, text):
        self.text = text

    def count_characters(self):
        return len(self.text)

    def count_letters(self):
        return sum(1 for char in self.text if char.isalpha())

    def count_spaces(self):
        return self.text.count(' ')

