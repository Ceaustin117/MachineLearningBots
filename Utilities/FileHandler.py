


class FileHandler:
    f = open('C:/Users/Chris/Desktop/PythonPractice/Project1/InputData', 'r')

    def print_file(self):
        read_data = self.f.read()
        print(read_data)
