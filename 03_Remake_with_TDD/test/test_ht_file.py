from unittest import TestCase
import unittest
import os
from algorithms import ht_file

class TestFile(TestCase):
    folderStr = ''
    filePath = ''
    instance = None

    def setUp(self):
        TestFile.folderStr = '2018-04-08'
        TestFile.filePath = 'sample.txt'
        os.mknod(TestFile.filePath)
        TestFile.instance = ht_file.HattrickFile()

    def tearDown(self):
        try:
            os.rmdir(TestFile.folderStr)
            os.remove(TestFile.filePath)
        except:
            pass
    """
    Test create folder if it is not existed
    """
    def test_check_and_create_folder(self):
        TestFile.instance.check_and_create_folder(TestFile.folderStr)
        self.assertTrue(os.path.exists(TestFile.folderStr), 'folder is not created')

    """
    Test delete file if it is existed
    """
    def test_check_and_delete_file(self):
        TestFile.instance.check_and_delete_file(TestFile.filePath)
        self.assertFalse(os.path.exists(TestFile.filePath), 'file is existed')

if __name__ == '__main__':
    unittest.main()
