# from nltk.corpus import stopwords
import string

class PreProcessText:
    """
    A class for preprocessing text data, including removing punctuation,
    removing stopwords, and tokenizing text.
    """
    def __init__(self):
        # with open("stopwords.txt", "w") as f:
        #     f.write("\n".join(stopwords.words("english")))
        with open("stopwords.txt", "r") as f:
            self.stop_words = set(f.read().splitlines())


    @staticmethod
    def __remove_punctuation(text: str) -> str:
        return ''.join(char for char in text if char not in string.punctuation)

    def __remove_stopwords(self, text: str) -> list[str]:
        return [word for word in text.split() if word.lower() not in self.stop_words]

    def tokenize(self, text: str) -> list[str]:
        text_no_punctuation = self.__remove_punctuation(text)
        return self.__remove_stopwords(text_no_punctuation)
