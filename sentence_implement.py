from data_sentence import Data_Sentence
from errors_sen import ErrorsSentence
from sentence_finder import SentenceFinder


class SentenceImplement:

    def __init__(self):
        self.data = Data_Sentence()
        self.finder = SentenceFinder()
        self.__changes = ErrorsSentence()
        self.__node = None
        self.__is_change = False


    def load_data(self, file_path):
        self.data.load_data(file_path)

    def search(self, sentence, full_sent, size=5):
        if self.__is_change:
            sentence = full_sent
            self.__node = None
        if sentence == '#':
            self.__node = None
            self.__is_change = False
            return 1
        try:
            result = self.finder.search(sentence, node=self.__node)
            self.__node = result[1]
            result = result[0]
        except Exception as error:
            try:
                if not self.__node and len(sentence.split(" ") == 1):
                    result = self.data.get_sub_word(sentence.split(" ")[0])
                    result = self.finder.get_search(result)[0]
                else:
                    raise

            except Exception as error:
                try:
                    result = self.__changes.search(full_sent, size)
                    self.__node = None
                    self.__is_change = True
                except Exception as error:
                    self.__node = None
                    raise error
        try:
            if len(result) < size:
                result += self.__changes.search(full_sent, size - len(result))
                self.__node = None
                self.__is_change = True
            string = ""
            for i in result:
                string += str(i)
            return string
        except Exception:
            raise Exception("not found")
