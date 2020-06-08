import enum
import collections

class UserDecision(enum.Enum):
    undecided = 0
    keep = 1
    discard = 2


class FileMetadata:

    def __init__(self, path, extension, folder_searched):
        self.path = path
        self.extension = extension
        self.folder_searched = folder_searched
        self.hash = None
        self.last_modified = None
        self.user_decision_enum = UserDecision.undecided

    def __eq__(self, other):
        if isinstance(other, FileMetadata):
            return self.hash == other.hash
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_path_relative_to_folder_searched(self):
        relative_path = collections.namedtuple('relative_path', 'folder_searched relative_path')
        found = self.path.find(self.folder_searched)
        if found != -1:
            text_index = len(self.folder_searched)
            return relative_path(folder_searched= self.folder_searched, relative_path=self.path[text_index:])
        else:
            return relative_path(folder_searched='', relative_path=self.path)
