from unittest import TestCase
from player import parse


class TestParse(TestCase):
    def test_parse_player_html_to_csv_2018_10_07(self):
        p = parse.Parse()
        p.read_line_list('../2018/10/07/player.html')
        p.print_line_list()
        p.write_line_list('../2018/10/07/player_tmp.html')
        p.modify_line_list('../2018/10/07/player_tmp.html')
        p.print_df_cols()
        p.print_df()
        p.save_df('../2018/10/07/player.csv')

    def test_parse_player_html_to_csv_2018_11_07(self):
        p = parse.Parse()
        p.read_line_list('../2018/11/07/player.html')
        p.print_line_list()
        p.write_line_list('../2018/11/07/player_tmp.html')
        p.modify_line_list('../2018/11/07/player_tmp.html')
        p.print_df_cols()
        p.print_df()
        p.save_df('../2018/11/07/player.csv')

    def test_parse_player_html_to_csv_2019_03_31(self):
        p = parse.Parse()
        p.read_line_list('../2019/03/31/player.html')
        p.print_line_list()
        p.write_line_list('../2019/03/31/player_tmp.html')
        p.modify_line_list('../2019/03/31/player_tmp.html')
        p.print_df_cols()
        p.print_df()
        p.save_df('../2019/03/31/player.csv')
