
class MyCM:

    def __init__(self, filename, text, mode):
        self.filename = filename
        self.text = text
        self.mode = mode

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.filename, self.mode) as f:
            f.write(self.text)


with MyCM("my_file.txt", "w") as f:

    print("Writing to file")