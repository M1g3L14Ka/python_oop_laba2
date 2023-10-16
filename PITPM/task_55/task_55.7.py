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


text = ("Lorem Ipsum - это текст- рыба, часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "
        "рыбой для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую "
        "коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только "
        "успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в "
        "новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее "
        "время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum.")

text_processor = Text(text)

print(f"Количество символов в тексте: {text_processor.count_characters()}")
print(f"Количество букв в тексте: {text_processor.count_letters()}")
print(f"Количество пробелов в тексте: {text_processor.count_spaces()}")
print(f"Количество символов без пробелов: {text_processor.count_characters_without_spaces()}")
print(f"Массив слов в тексте: {text_processor.get_words()}")
print(f"Массив предложений в тексте: {text_processor.get_sentences()}")
