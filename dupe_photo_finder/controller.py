import model


def request_search(directories_list, extensions_list = ['.jpg', '.nef', '.raf']):
    validate_request_not_empty(directories_list)
    return model.find_duplicate_files_in_directories(directories_list, extensions_list)


def validate_request_not_empty(directories_list):
    if directories_list is None or len(directories_list) == 0:
        raise ValueError("No directories have been given to search!")
