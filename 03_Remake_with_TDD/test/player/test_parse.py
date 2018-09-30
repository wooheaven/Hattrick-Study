from unittest import TestCase
from player import parse


class TestParse(TestCase):
    def test_parse_player_html_to_csv(self):
        p = parse.Parse()
        p.read_line_list('../2018/09/30/player.html')
        p.print_line_list()
        p.write_line_list('../2018/09/30/player_tmp.html')
        p.modify_line_list('../2018/09/30/player_tmp.html')
        p.print_df_cols()
        p.print_df()
        p.save_df('../2018/09/30/player.csv')
