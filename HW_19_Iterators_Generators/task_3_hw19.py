class MyIterable:

    def __init__(self, my_object):

        self.my_object = my_object
        self.iterable_object = iter(self.my_object)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterable_object)
        except StopIteration:
            raise StopIteration

    # This method gets any item (if it exists) in the iterable by the index you pass inside
    def get_item(self, my_index):

        real_index = my_index[0]

        for val in self.my_object:
            try:
                if val == self.my_object[real_index]:
                    return val
            except IndexError:
                return f"No object with this index"


object_1 = MyIterable(['Monday', 'Tuesday', 33, [1, 2, 3]])


for item in object_1:
    print(item)

print('-' * 100)

print(object_1.get_item([1]))
print(object_1.get_item([11]))

