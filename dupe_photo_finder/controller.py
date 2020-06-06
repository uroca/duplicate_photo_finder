import model
import view


class Controller:

    def __init__(self):
        self.directories_to_search = []

    def add_directory_to_search(self, directory):
        self.directories_to_search.append(directory)

    def request_search(self, user_feedback, extensions_list = ['.jpg', '.nef', '.raf']):
        self.validate_request_not_empty(self.directories_to_search)
        return model.find_duplicate_files_in_directories(self.directories_to_search, extensions_list, user_feedback)

    def validate_request_not_empty(self, directories_list):
        if directories_list is None or len(directories_list) == 0:
            raise ValueError("No directories have been given to search!")
