from task_1_hw21 import FileManager


def test_writing_to_file():
    with FileManager("task_2.txt", "w") as f:
        f.write(f"The number of class instances is --> {FileManager.instance_num}\n\n")
    with open("task_2.txt", "r") as f:
        file = f.read()
        assert file == "The number of class instances is --> 4\n\n"