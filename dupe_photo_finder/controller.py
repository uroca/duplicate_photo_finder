import model
import view
import collections


class Controller:

    def __init__(self):
        self.directories_to_search = []
        self.sets_of_duplicates = []

    def add_directory_to_search(self, directory):
        self.directories_to_search.append(directory)

    def request_search(self, user_feedback, extensions_list = ['.jpg', '.nef', '.raf']):
        self.validate_request_not_empty(self.directories_to_search)
        self.sets_of_duplicates = model.find_duplicate_files_in_directories(self.directories_to_search, extensions_list, user_feedback)
        return self.sets_of_duplicates

    def validate_request_not_empty(self, directories_list):
        if directories_list is None or len(directories_list) == 0:
            raise ValueError("No directories have been given to search!")

    def get_paths_of_set_of_duplicates(self, index_set_of_duplicates):
        relative_paths = []
        file_num = 0
        for d in self.sets_of_duplicates[index_set_of_duplicates]:
            relative_paths.extend(self.prepare_relative_path_for_treeview(file_num, d.get_path_relative_to_folder_searched()))
            file_num+=1
        return relative_paths

    def prepare_relative_path_for_treeview(self, file_num, file_path_tuple):
        # TODO: one line added between root directory and subdirectories, REMOVE
        list_of_data = []
        counter=0
        path_for_treeview = collections.namedtuple('path_for_treeview', 'parent index text')
        current_node = str(file_num)+'_'+str(counter)
        list_of_data.append(path_for_treeview(parent = '', index=current_node, text=file_path_tuple.folder_searched))
        counter+=1
        for n in list(filter(None,file_path_tuple.relative_path.split('\\'))):
            parent_node = current_node
            current_node = str(file_num) + '_' + str(counter)
            list_of_data.append(path_for_treeview(parent=parent_node, index=current_node, text=n))
            counter+=1
        return list_of_data

