import shutil
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
        os.mkdir(TestFile.folderStr)
        os.mkdir(TestFile.folderStr + '/match_files')
        os.mknod(TestFile.folderStr + '/match_files/sample1.txt')
        os.mknod(TestFile.folderStr + '/match_files/sample2.txt')

        TestFile.filePath = 'sample.txt'
        TestFile.instance = ht_file.HattrickFile()

    def tearDown(self):
        try:
            if (os.path.exists(TestFile.folderStr)):
                shutil.rmtree(TestFile.folderStr, ignore_errors=True)
        except:
            pass
    """
    Test create folder if it is not existed
    """
    def test_check_and_create_folder(self):
        tmp_folder_path = TestFile.folderStr + '/match_files/banner'
        TestFile.instance.check_and_create_folder(tmp_folder_path)
        self.assertTrue(os.path.exists(tmp_folder_path), 'folder is not existed')

    """
    Test delete folder if it is existed
    """
    def test_check_and_delete_folder(self):
        tmp_folder_path = TestFile.folderStr + '/match_files'
        TestFile.instance.check_and_delete_folder(tmp_folder_path)
        self.assertFalse(os.path.exists(tmp_folder_path), 'folder is existed')

    """
    Test delete file if it is existed
    """
    def test_check_and_delete_file(self):
        tmp_file_path = TestFile.folderStr + '/match_files/sample2.txt'
        TestFile.instance.check_and_delete_file(tmp_file_path)
        self.assertFalse(os.path.exists(tmp_file_path), 'file is existed')

if __name__ == '__main__':
    unittest.main()
