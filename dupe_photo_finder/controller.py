import model
import view


class Controller:

    @staticmethod
    def request_search(directories_list, extensions_list = ['.jpg', '.nef', '.raf']):
        Controller.validate_request_not_empty(directories_list)
        return model.find_duplicate_files_in_directories(directories_list, extensions_list)

    @staticmethod
    def validate_request_not_empty(directories_list):
        if directories_list is None or len(directories_list) == 0:
            raise ValueError("No directories have been given to search!")
