class FileMetadata:

    def __init__(self, path, extension):
        self.path = path
        self.extension = extension
        self.hash = None

    @property
    def hash(self):
        return self.__hash

    @hash.setter
    def hash(self, val):
        self.__hash = val

    def __eq__(self, other):
        if isinstance(other, FileMetadata):
            return self.hash == other.hash
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)
