# import pyperclip
# import json
# from bs4 import BeautifulSoup
#
# tmpClip = pyperclip.paste()
# print(tmpClip)
#
# html_file = 'test.html'
# soup = None
# with open(html_file, 'r') as file:
#     soup = BeautifulSoup(file.read(), "html.parser")
#
# table = soup.find('table')
# rows = table.find_all('tr')
#
# player_json = json.loads(fp=tmpClip)
# print(player_json)

from pprint import pprint
import pandas as pd
#
#
df = pd.read_html('test1.html')[0]  # get the first parsed dataframe
pprint(df.values.tolist())

# soup = None
# with open('test1.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), "html.parser")
# table = soup.find('table')
# rows = table.find('tr')
# for row in rows:
#     print(row)