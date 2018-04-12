import os.path


class HattrickFile():
    def check_and_create_folder(self, folder):
        while (not os.path.exists(folder)):
            print(folder + "\t\t : will be created")
            os.makedirs(folder)
        print(folder + '\t\t : is existed')

    def check_and_delete_file(self, filePath):
        while (os.path.exists(filePath)):
            print(filePath + '\t : will be removed')
            os.remove(filePath)
        print(filePath + '\t : is not existed')