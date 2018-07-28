import re

line_list = []
with open('player.html', 'r') as read_file:
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
        line_list.append(line)

with open('player1.html', 'w') as save_file:
    for line in line_list:
        save_file.write("%s\n" % line)

import pandas as pd

df = pd.read_html('player1.html', encoding="utf-8")[0]  # get the first parsed dataframe
df = df.drop(0, axis=1)
df = df.set_value(0, 1, 'Number')
df.rename(columns={1: 'Number', 2:'Nat'},
          inplace=True)
print(df.columns)
for row in df.values.tolist():
    print(row)
