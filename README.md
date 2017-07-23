# Hattric Team : LastKeeper (Korean 1944941)

## Player Parsing
[parsing_player_skill_table](00_Data/00_Player/parsing_player_skill_table.sh)

## Player Data

2017

05 [13](00_Data/00_Player/2017/05/13/player.txt), [20](00_Data/00_Player/2017/05/20/player.txt), [27](00_Data/00_Player/2017/05/27/player.txt)

06 [03](00_Data/00_Player/2017/06/03/player.txt), [10](00_Data/00_Player/2017/06/10/player.txt), [17](00_Data/00_Player/2017/06/17/player.txt), [25](00_Data/00_Player/2017/06/25/player.txt), [28](00_Data/00_Player/2017/06/28/player.txt)

07 [01](00_Data/00_Player/2017/07/01/player_skill_table.txt), [02](00_Data/00_Player/2017/07/02/player_skill_table.txt), [05](00_Data/00_Player/2017/07/05/player_skill_table.txt), [09](00_Data/00_Player/2017/07/09/player_skill_table.txt), [12](00_Data/00_Player/2017/07/12/player_skill_table.txt), [15](00_Data/00_Player/2017/07/15/player_skill_table.txt), [16](00_Data/00_Player/2017/07/16/player_skill_table.txt), [19](00_Data/00_Player/2017/07/19/player_skill_table.txt), [22](00_Data/00_Player/2017/07/22/player_skill_table.txt)

## Match Parsing
[parsing_match](00_Data/00_Player/htmlToObject.ipynb)

## Match Data

2017

05

06

07 [02](00_Data/00_Player/2017/07/02/match.txt), [05](00_Data/00_Player/2017/07/05/match.txt), [09](00_Data/00_Player/2017/07/09/match.txt), [12](00_Data/00_Player/2017/07/12/match.txt), [16](00_Data/00_Player/2017/07/16/match.txt), [19](00_Data/00_Player/2017/07/19/match.txt), [23](00_Data/00_Player/2017/07/23/match.txt)

## Line Up

[KP](00_Data/00_Player/01_KP_table.md)

# How to use python3 with jupyter for Hattric analysis

[Details of use python3 with jupyter for Hattric analysis](01_use/01_use_python3_on_jupyternotebook.md)

```{bash}
$ conda info --envs
$ source activate python3
$ conda info --envs
$ jupyter notebook --notebook-dir=`pwd` --no-browser --ip=0.0.0.0
$ source deactivate python3
$ conda info --envs
```
