import os

text = input()


def write_and_read(text):
    file_path = os.path.join(os.path.abspath('/tmp'), 'my_file')
    open(file_path, "w").write(text)
    return open(file_path, "r").read()


print(write_and_read(text))
