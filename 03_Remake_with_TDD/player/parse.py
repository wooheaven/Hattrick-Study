import re
import pandas as pd
import numpy as np

class Parse():
    def __init__(self):
        self.line_list = []
        self.df = None

    def read_line_list(self, filename):
        with open(filename, 'r') as read_file:
            for line in read_file.readlines():
                # [playerid=429263806] -> (playerid=429263806)
                line = re.sub(r"=(\d{9})]", r"=\1)", line)
                line = re.sub(r"\[playerid=", r"(playerid=", line)

                # [tr]  -> <tr>
                # [/tr] -> </tr>
                # [th]  -> <th>
                # [/th] -> </th>
                # [td]  -> <td>
                # [/td] -> </td>
                line = re.sub(r"\[", r"<", line)
                line = re.sub(r"]", r">", line)

                # (playerid=429263806) -> [playerid=429263806]
                line = re.sub(r"\(", r"[", line)
                line = re.sub(r"\)", r"]", line)

                # remove newline char
                line = line.rstrip()
                self.line_list.append(line)

    def print_line_list(self):
        for line in self.line_list:
            print(line)

    def write_line_list(self, filename):
        with open(filename, 'w') as save_file:
            for line in self.line_list:
                save_file.write("%s\n" % line)

    def modify_line_list(self, filename):
        self.df = pd.read_html(filename, encoding="utf-8")[0]  # get the first parsed dataframe
        self.df = self.df.drop(0, axis=1)

        column_names = {1: 'Number',
                        2: 'Nat',
                        3: 'PlayerStr',
                        4: 'Special',
                        5: 'Stat',
                        6: 'Age',
                        23: 'Last',
                        28: 'TC',
                        29: 'PH',
                        30: 'KPPos',
                        31: 'WBPos',
                        32: 'CDPos',
                        33: 'WPos',
                        34: 'IMPos',
                        35: 'FWPos',
                        36: 'FWd',
                        37: 'FWtw',
                        38: 'TDF',
                        39: 'BPo',
                        40: 'BPoV'}
        self.df.rename(columns=column_names, inplace=True)

        self.df['Number'][0] = 'Number'
        self.df['PlayerStr'][0] = 'PlayerStr'
        self.df['Special'][0] = 'Special'
        self.df['Stat'][0] = 'Stat'
        self.df['IMPos'][0] = 'IMPos'
        self.df['FWPos'][0] = 'FWPos'

        self.df['PlayerName'] = self.df['PlayerStr'].str.extract(r'([A-Z][a-z]*\D*[a-z] [A-Z][a-z]*[a-z])')
        self.df['PlayerName'][0] = 'PlayerName'
        self.df['PlayerID'] = self.df['PlayerStr'].str.extract(r'\=(?P<digit>\d{9})')
        self.df['PlayerID'][0] = 'PlayerID'
        self.df['Special'] = self.df['Special'].str.replace(' 더 많은 정보를 보려면 클릭', '')
        self.df['Special'] = self.df['Special'].str.replace('예측할 수 없음', 'Unpredictable')
        self.df['Special'] = self.df['Special'].str.replace('공 마술사', 'Technical')
        self.df['Special'] = self.df['Special'].str.replace('헤딩', 'Head')
        self.df['Special'] = self.df['Special'].str.replace('힘 있음', 'Powerful')
        self.df['Special'] = self.df['Special'].str.replace('빠름', 'Quick')
        self.df['Last'] = self.df['Last'].str.extract('(....-..-..)')
        self.df['TC'] = self.df['TC'].str.replace('(\[playerid\=\d{9}\])', '')
        self.df['PH'] = self.df['PH'].str.replace('(\[playerid\=\d{9}\])', '')
        self.df = self.df.replace(np.nan, '', regex=True)

        cols = self.df.columns.tolist()
        cols = cols[0:2] + cols[-2:] + cols[3:-2]

        self.df = self.df[cols]

    def print_df_cols(self):
        print(self.df.columns.tolist())

    def print_df(self):
        for row in self.df.values.tolist():
            print(row)

    def save_df(self, filename):
        self.df.to_csv(filename, sep=',', header=False, index=False, encoding='utf-8')

if __name__ == "__main__":
    p = Parse()
    p.read_line_list('player.html')
    p.print_line_list()
    p.write_line_list('player1.html')
    p.modify_line_list('player1.html')
    p.print_df_cols()
    p.print_df()
    p.save_df('player.csv')