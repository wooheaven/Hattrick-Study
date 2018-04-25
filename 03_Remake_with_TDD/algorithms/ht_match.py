import re
from bs4 import BeautifulSoup

class HattrickMatch():
    def findMatchList(self, filePath):
        soup = None
        with open(filePath, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")
        return soup