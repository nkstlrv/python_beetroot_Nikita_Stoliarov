class FileManager:

    instance_num = 0

    def __init__(self, file_name, mode, text):
        self.file_name = file_name
        self.mode = mode
        self.text = text

    def __enter__(self):
        FileManager.instance_num += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_name, self.mode) as f:
            f.write(f"Number of class instances --> {FileManager.instance_num}; Text --> {self.text}\n\n")
            f.close()


with FileManager("task_1.txt", "w", "Some text") as f:
    print("Executing my context manager")

with FileManager("task_1.txt", "a", "Some text") as f:
    print("Executing my context manager")

with FileManager("task_1.txt", "a", "Some text") as f:
    print("Executing my context manager")
