from sentence_implement import SentenceImplement


class Cmd:
    def __init__(self):
        self.__sentence_treatment = SentenceImplement()
        self.__sentence = ""

    def run_command(self, folder_path):
        print("Loading the files and preparing the program...")
        self.__sentence_treatment.load_data(folder_path)
        print("The system is ready. Enter your text:")

        while True:
            text = input()
            if text == '#':
                self.__sentence = ""
                print("Enter your text:")
                continue

            self.__sentence += text
            try:
                value = self.__sentence_treatment.search(text, self.__sentence)
                if type(value) is str:
                    print(value)
                    print(self.__sentence, end='')
                elif not value:
                    raise Exception("This sentence not found")
            except Exception as error:
                print(error)
                print("Enter your text:")
                self.__sentence = ""