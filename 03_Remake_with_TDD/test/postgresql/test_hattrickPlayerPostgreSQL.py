from unittest import TestCase
import psycopg2
from postgresql import ht_player_postgresql


class TestHattrickPlayerPostgreSQL(TestCase):
    def test_select_player(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        tuple_list = ht_player_pg.select_player(conn, '2018/06/27')
        ht_player_pg.print(tuple_list)
        conn.close()

    def test_backup_player(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        ht_player_pg.backup_player(conn=conn, target_table='player', backup_table='player_tmp')
        conn.close()

    def test_create_player(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        ht_player_pg.drop_table(conn=conn, target_table='player_tmp2')
        ht_player_pg.create_player(conn=conn, target_table='player_tmp2')
        conn.close()
