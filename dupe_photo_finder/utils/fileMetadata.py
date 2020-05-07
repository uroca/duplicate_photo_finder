class FileMetadata:
    def __init__(self, path, file_hash, extension):
        self.path = path
        self.hash = file_hash
        self.extension = extension

    def __eq__(self, other):
        if isinstance(other, FileMetadata):
            return self.hash == other.hash
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)
