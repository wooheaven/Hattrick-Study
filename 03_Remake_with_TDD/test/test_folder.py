from unittest import TestCase
import unittest
import os.path
from algorithms import ht_folder

class TestFolder(TestCase):
    folderStr = ''

    def setUp(self):
        TestFolder.folderStr = '2018-04-08'

    def tearDown(self):
        try:
            os.rmdir(TestFolder.folderStr)
        except:
            pass
    """
    Test create folder if it is not existed
    """
    def test_check_and_create_folder(self):
        instance = ht_folder.HattrickFolder()
        instance.check_and_create_folder(TestFolder.folderStr)
        self.assertTrue(os.path.exists(TestFolder.folderStr), 'folder is not created')

if __name__ == '__main__':
    unittest.main()
