import os
from .localFile import LocalFile
import hashlib


def scan_for_file_extensions(folder_paths, extensions):
    files_found = []
    for f in folder_paths:
        for dirpath, subdirs, files in os.walk(f):
            for x in files:
                file_extension = os.path.splitext(x)[1].lower()
                if file_extension in extensions:
                    file_path = os.path.join(dirpath, x)
                    file_hash = get_file_hash(file_path)
                    files_found.append(LocalFile(file_path, file_hash, file_extension))
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
