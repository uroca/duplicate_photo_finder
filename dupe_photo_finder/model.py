from utils import localSys
from utils import printDuplicates
from fileMetadata import FileMetadata


def find_duplicate_files_in_directories(directories_list, extensions_list, user_feedback):
    localSys.all_folders_exist(directories_list)
    local_files_found = localSys.scan_for_file_extensions(directories_list, extensions_list)
    user_feedback.update_message(''.join(['Local files found: ', str(len(local_files_found))]))
    metadata_list = retrieve_file_metadata(local_files_found, user_feedback)
    duplicates_found = scan_metadata_list_for_duplicates(metadata_list)
    printDuplicates.print_terminal(duplicates_found) # to remove functionality when gui is implemented
    return duplicates_found

def retrieve_file_metadata (list_of_files, user_feedback):
    user_feedback.change_max_value_progress_bar(len(list_of_files))
    list_file_metadata = []
    for f in list_of_files:
        file_metadata = FileMetadata(f.path, f.extension)
        file_metadata.hash = localSys.get_file_hash(f.path)
        list_file_metadata.append(file_metadata)
        user_feedback.update_message(''.join(['Retrieved ', str(len(list_file_metadata)), ' of a total of ',
                                              str(len(list_of_files)), ' files']))
        user_feedback.update_progress_bar(len(list_file_metadata))
    return list_file_metadata

def scan_metadata_list_for_duplicates(local_files):
    found = []
    while len(local_files) > 1:
        file = local_files.pop()
        copies = [x for x in local_files if x == file]
        if len(copies) > 0:
            copies.append(file)
            found.append(copies)
        local_files = [x for x in local_files if x != file]
    return found
