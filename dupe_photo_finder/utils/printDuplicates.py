def print_terminal(duplicates_found):
    print('Sets of duplicates found: '+ str(len(duplicates_found)))
    for f in duplicates_found:
        print('One set of duplicates found - the following are the same photo:')
        for file in f:
            print(file.path)