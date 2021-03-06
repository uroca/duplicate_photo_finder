import os
import hashlib
import collections


def scan_for_file_extensions(folder_paths, extensions):
    files_found = []
    file_data = collections.namedtuple('file_data', 'path extension folder_searched')
    for f in folder_paths:
        for dirpath, subdirs, files in os.walk(f):
            for x in files:
                file_extension = os.path.splitext(x)[1].lower()
                if file_extension in extensions:
                    file_path = os.path.normpath(os.path.join(dirpath, x))
                    new_file = file_data(path = file_path, extension = file_extension, folder_searched= os.path.normpath(f))
                    files_found.append(new_file)
                    print('Files found matching the extensions: ' + str(len(files_found)))
    return files_found


def get_file_hash(file_path):
    md5 = hashlib.md5()
    f = open(file_path, 'rb')
    while True:
        block = f.read(8192)
        if not block:
            break
        md5.update(block)
    return md5.hexdigest()


def all_folders_exist(list_of_folder_paths):
    for x in list_of_folder_paths:
        folder_exists(x)


def folder_exists(folder_path):
    if not os.path.isdir(folder_path):
        raise ValueError("This folder doesn't exist, it can't be scanned for duplicate photos: " + folder_path)


def get_last_modification_time(file_path):
    return os.path.getmtime(file_path)