import pytest
from .context import FileMetadata


def test_equality_when_only_hashes_are_equal():
    a = FileMetadata('drive1\\folder_a\\file1.aaa', '07740ac7140e512a285608235eda995f', '.aaa')
    b = FileMetadata('drive2\\folder_b\\file1.bbb', '07740ac7140e512a285608235eda995f', '.bbb')
    assert a == b, 'Should be equal'

def test_different_when_only_hashes_are_different():
    a = FileMetadata('drive1\\folder_a\\file1.aaa', '07740ac7140e512a285608235eda995f', '.aaa')
    b = FileMetadata('drive1\\folder_a\\file1.aaa', '0790cccb2a6d8c321509051b161fa241', '.aaa')
    assert a != b, 'Should be unequal'
