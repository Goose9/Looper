

class Pedal:
    def __init__(self):
        self.is_paused = False
        self.file_path = "./"

    @property
    def is_paused(self):
        return self.is_paused

    @is_paused.setter
    def is_paused(self, status):
        self.is_paused = status

    @property
    def file_path(self):
        return self.file_path

    @file_path.setter
    def file_path(self, path):
        self.file_path = path

    @property
    def file_name(self):
        return self.file_path

    @file_name.setter
    def file_name(self, name):
        self.file_name = name