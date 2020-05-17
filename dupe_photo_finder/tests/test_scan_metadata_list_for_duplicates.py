import pytest
from .context import FileMetadata
from .context import *


def test_one_set_with_two_matching_hashes_found():
    a = FileMetadata('drive1\\folder_a\\file1.aaa', '.aaa')
    a.hash = '07740ac7140e512a285608235eda995f'
    b = FileMetadata('drive2\\folder_b\\file1.bbb', '.bbb')
    b.hash = '07740ac7140e512a285608235eda995f'
    c = FileMetadata('drive2\\folder_a\\file2.ccc', '.ccc')
    c.hash = '0790cccb2a6d8c321509051b161fa241'
    files = [a, b, c]
    found = model.scan_metadata_list_for_duplicates(files)
    assert (len(found) == 1 and (a in found[0] and b in found[0])), 'Should have one result with two files'

def test_nothing_found_with_different_hashes_used():
    a = FileMetadata('drive1\\folder_a\\file1.aaa', '.aaa')
    a.hash = '07740ac7140e512a285608235eda995f'
    c = FileMetadata('drive2\\folder_a\\file2.ccc', '.ccc')
    c.hash = '0790cccb2a6d8c321509051b161fa241'
    d = FileMetadata('drive3\\folder_d\\file4.ddd', '.ddd')
    d.hash = 'dca338e2b0ea0a786a2d772211654e07'
    files = [a, c, d]
    found = model.scan_metadata_list_for_duplicates(files)
    assert (len(found) == 0), 'Should have no results'