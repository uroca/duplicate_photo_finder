def find_duplicates(local_files):
    found = []
    while len(local_files) > 1:
        file = local_files.pop()
        copies = [x for x in local_files if x == file]
        if len(copies) > 0:
            copies.append(file)
            found.append(copies)
        local_files = [x for x in local_files if x != file]
    for f in found:
        print('One set of matches found:')
        for file in f:
            print(file.path)
    return found
