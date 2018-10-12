import re
import pandas as pd
import numpy as np

# add W_Pos -> CD_Pos
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

        column_names = {0: 'Number',
                        1: 'Nat',
                        2: 'PlayerStr',
                        3: 'Special',
                        4: 'Stat',
                        5: 'Age',
                        6: 'Since',
                        7: 'TSI',
                        8: 'LS',
                        9: 'XP',
                        10: 'Fo',
                        11: 'Stm',
                        12: 'Lo',
                        13: 'MB',
                        14: 'KP',
                        15: 'DF',
                        16: 'PM',
                        17: 'WI',
                        18: 'PS',
                        19: 'SC',
                        20: 'SP',
                        21: 'Psico',
                        22: 'Last',
                        23: 'Rt',
                        24: 'Pos',
                        25: 'Wage',
                        26: 'G',
                        27: 'KPPos',
                        28: 'WBdPos',
                        29: 'WBPos',
                        30: 'WBtmPos',
                        31: 'WBoPos',
                        32: 'CDPos',
                        33: 'CDtwPos',
                        34: 'CDoPos',
                        35: 'WdPos',
                        36: 'WPos',
                        37: 'WtmPos',
                        38: 'WoPos',
                        39: 'IMPos',
                        40: 'FWPos',
                        41: 'FWdPos',
                        42: 'FWtwPos',
                        43: 'TDFPos',
                        44: 'BPo',
                        45: 'BPoV'}
        self.df.rename(columns=column_names, inplace=True)

        self.df['Number'][0] = 'Number'
        self.df['PlayerStr'][0] = 'PlayerStr'
        self.df['Special'][0] = 'Special'
        self.df['Stat'][0] = 'Stat'
        self.df['KPPos'][0] = 'KPPos'

        self.df['WBdPos'][0] = 'WBdPos'
        self.df['WBPos'][0] = 'WBPos'
        self.df['WBtmPos'][0] = 'WBtmPos'
        self.df['WBoPos'][0] = 'WBoPos'

        self.df['CDPos'][0] = 'CDPos'
        self.df['CDtwPos'][0] = 'CDtwPos'
        self.df['CDoPos'][0] = 'CDoPos'

        self.df['WdPos'][0] = 'WdPos'
        self.df['WPos'][0] = 'WPos'
        self.df['WtmPos'][0] = 'WtmPos'
        self.df['WoPos'][0] = 'WoPos'

        self.df['IMPos'][0] = 'IMPos'

        self.df['FWPos'][0] = 'FWPos'
        self.df['FWdPos'][0] = 'FWdPos'
        self.df['FWtwPos'][0] = 'FWtwPos'
        self.df['TDFPos'][0] = 'TDFPos'

        self.df['Player'] = self.df['PlayerStr'].str.extract(r'([A-Z][a-z]*\D*[a-z] [A-Z][a-z]*[a-z])')
        self.df['Player'][0] = 'Player'
        self.df['PlayerID'] = self.df['PlayerStr'].str.extract(r'\=(?P<digit>\d{9})')
        self.df['PlayerID'][0] = 'PlayerID'
        self.df['Special'] = self.df['Special'].str.replace(' 더 많은 정보를 보려면 클릭', '')
        self.df['Special'] = self.df['Special'].str.replace('예측할 수 없음', 'Unpredictable')
        self.df['Special'] = self.df['Special'].str.replace('공 마술사', 'Technical')
        self.df['Special'] = self.df['Special'].str.replace('헤딩', 'Head')
        self.df['Special'] = self.df['Special'].str.replace('힘 있음', 'Powerful')
        self.df['Special'] = self.df['Special'].str.replace('빠름', 'Quick')

        self.df['MB'] = self.df['MB'].str.replace('✔', 'TRUE')
        self.df['MB'] = self.df['MB'].apply(lambda x: x if x == 'MB' or x == 'TRUE' else 'FALSE')

        self.df['Last'] = self.df['Last'].str.extract('(....-..-..)')
        self.df['Last'][0] = 'Last'
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
