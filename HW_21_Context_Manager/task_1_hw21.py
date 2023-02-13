class FileManager:

    instance_num = 0

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        FileManager.instance_num += 1
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager("task_1.txt", "w") as f:
    f.write(f"The number of class instances is --> {FileManager.instance_num}\n\n")

with FileManager("task_1.txt", "a") as f:
    f.write(f"The number of class instances is --> {FileManager.instance_num}\n\n")

with FileManager("task_1.txt", "a") as f:
    f.write(f"The number of class instances is --> {FileManager.instance_num}\n\n")

print(f"File is closed --> {f.closed}")







