from contextlib import contextmanager


@contextmanager
def my_cmanager(f_name, mode):

    file = open(f_name, mode)
    yield file
    file.close()


with my_cmanager("new_test.txt", "w") as f:
    f.write("Test 2")



