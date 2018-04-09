import os.path


class HattrickFolder():
    def check_and_create_folder(self, folder):
        while (not os.path.exists(folder)):
            print(folder + "\t\t : will be created")
            os.makedirs(folder)
        print(folder + '\t\t : is existed')
