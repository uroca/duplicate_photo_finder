import pytest
from .context import FileMetadata


def test_equality_when_only_hashes_are_equal():
    a = FileMetadata('drive1\\folder_a\\file1.aaa', '.aaa')
    a.hash = '07740ac7140e512a285608235eda995f'
    b = FileMetadata('drive2\\folder_b\\file1.bbb', '.bbb')
    b.hash = '07740ac7140e512a285608235eda995f'
    assert a == b, 'Should be equal'

def test_different_when_only_hashes_are_different():
    a = FileMetadata('drive1\\folder_a\\file1.aaa', '.aaa')
    a.hash = '07740ac7140e512a285608235eda995f'
    b = FileMetadata('drive1\\folder_a\\file1.aaa', '.aaa')
    b. hash = '0790cccb2a6d8c321509051b161fa241'
    assert a != b, 'Should be unequal'
