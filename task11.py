import os
from tempfile import mktemp


class WrapStrToFile:
    def __init__(self):
        self.file_path = mktemp('text.txt')

    @property
    def content(self):
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except IOError:
            print("File doesn't exist")

    @content.setter
    def content(self, value):
        with open(self.file_path, 'w') as f:
            f.write(value)

    @content.deleter
    def content(self):
        os.remove(self.file_path)


w_s_t_f = WrapStrToFile()
print(w_s_t_f.content)
w_s_t_f.content = 'test str'
print(w_s_t_f.content)
w_s_t_f.content = 'TEXT'
print(w_s_t_f.content)
del w_s_t_f.content
