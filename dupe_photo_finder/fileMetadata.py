import enum

class UserDecision(enum.Enum):
    undecided = 0
    keep = 1
    discard = 2


class FileMetadata:

    def __init__(self, path, extension):
        self.path = path
        self.extension = extension
        self.hash = None
        self.last_modified = None
        self.user_decision_enum = UserDecision.undecided

    def __eq__(self, other):
        if isinstance(other, FileMetadata):
            return self.hash == other.hash
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)
