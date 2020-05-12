from utils import localSys
from utils import printDuplicates


def find_duplicate_files_in_directories(directories_list, extensions_list):
    localSys.all_folders_exist(directories_list)
    local_files_found = localSys.scan_for_file_extensions(directories_list, extensions_list)
    duplicates_found = scan_files_found_for_duplicates(local_files_found)
    printDuplicates.print_terminal(duplicates_found) # to remove functionality when gui is implemented
    return duplicates_found


def scan_files_found_for_duplicates(local_files):
    found = []
    while len(local_files) > 1:
        file = local_files.pop()
        copies = [x for x in local_files if x == file]
        if len(copies) > 0:
            copies.append(file)
            found.append(copies)
        local_files = [x for x in local_files if x != file]
    return found
