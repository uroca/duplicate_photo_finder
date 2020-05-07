import sys
from utils import localSys as localSys
from utils import printDuplicates
import matching
import time


def main():
    folders_to_scan = sys.argv[1:]
    print(folders_to_scan)
    # error if folder doesn't exist
    extensions_sought = ['.jpg', '.nef', '.raf']
    local_files_found = localSys.scan_for_file_extensions(folders_to_scan, extensions_sought)
    duplicates_found = matching.find_duplicates(local_files_found)
    printDuplicates.print_terminal(duplicates_found)


def processing_time():
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    taken_seconds = end - start
    taken_minutes = (end - start)/60
    print('Finalised the test in ' + str(taken_seconds) + ' seconds')
    print('Finalised the test in ' + str(taken_minutes) + ' minutes')


if __name__ == "__main__":
    processing_time()
