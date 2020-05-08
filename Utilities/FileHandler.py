# This class handles all file functionality


class FileHandler:
    # change this path to your own local path, the input data file comes with the git code
    f = open('C:/Users/ceaus/PycharmProjects/MachineLearningBots/LocalFiles/InputData', 'r')

    def print_file(self):
        read_data = self.f.read()
        print(read_data)
