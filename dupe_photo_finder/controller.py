def request_search(directories_list, extensions_list):
    validate_request_not_empty(directories_list)
    # add call to initiate dupe_photo search


def validate_request_not_empty(directories_list):
    if directories_list is None or len(directories_list) == 0:
        raise ValueError("No directories have been given to search!")