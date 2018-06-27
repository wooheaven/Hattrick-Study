from unittest import TestCase
import psycopg2
from postgresql import ht_player_postgresql

class TestHattrickPlayerPostgreSQL(TestCase):
    def test_select_player(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        tuple_list = ht_player_pg.select_player(conn, '2018/06/27')
        ht_player_pg.print(tuple_list)