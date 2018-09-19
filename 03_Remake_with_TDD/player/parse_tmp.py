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
                        7: 'Since',
                        8: 'TSI',
                        9: 'LS',
                        10: 'XP',
                        11: 'Fo',
                        12: 'Stm',
                        13: 'Lo',
                        14: 'MB',
                        15: 'KP',
                        16: 'DF',
                        17: 'PM',
                        18: 'WI',
                        19: 'PS',
                        20: 'SC',
                        21: 'SP',
                        22: 'Psico',
                        23: 'Last',
                        24: 'Rt',
                        25: 'Pos',
                        26: 'Wage',
                        27: 'G',
                        # 27: 'TC',
                        # 28: 'PH',
                        28: 'KPPos',
                        29: 'WBdPos',
                        30: 'WBPos',
                        31: 'WBtmPos',
                        32: 'WBoPos',
                        33: 'CDPos',
                        34: 'WPos',
                        35: 'IMPos',
                        36: 'FWPos',
                        37: 'FWdPos',
                        38: 'FWtwPos',
                        39: 'TDFPos',
                        40: 'BPo',
                        41: 'BPoV'}
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
        self.df['WPos'][0] = 'WPos'
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
        self.df['MB'] = self.df['MB'].apply(lambda x: x if len(str(x)) > 3 else 'FALSE')

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
