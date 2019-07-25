from unittest import TestCase
import psycopg2
from postgresql import ht_player_postgresql
import csv


class TestHattrickPlayerPostgreSQL(TestCase):
    def test_select_player(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        tuple_list = ht_player_pg.select_player(conn, 'player', '2018/06/27')
        ht_player_pg.print(tuple_list)
        conn.close()

    def test_backup_player(self):
        # conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        # from_table_name = 'player'
        from_table_name = 'player_tmp'
        # to_table_name = 'player_backup'
        to_table_name = 'player_tmp_backup'
        ht_player_pg.drop_table(conn=conn, target_table=to_table_name)
        ht_player_pg.backup_player(conn=conn, from_table=from_table_name, to_table=to_table_name)
        conn.close()

    def test_insert_player_from_select(self):
        # conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        # from_table_name = 'player'
        from_table_name = 'player_tmp'
        # to_table_name = 'player_tmp'
        to_table_name = 'player'
        ht_player_pg.insert_player_from_select(conn, to_table=to_table_name, from_table=from_table_name)
        conn.close()

    def test_create_player(self):
        # conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        ht_player_table_name = 'player'
        # ht_player_table_name = 'player_tmp'
        ht_player_pg.drop_table(conn=conn, target_table=ht_player_table_name)
        ht_player_pg.create_player(conn=conn, target_table=ht_player_table_name)
        # ht_player_pg.create_player_tmp(conn=conn, target_table=ht_player_table_name)
        conn.close()

    def test_insert_player_from_csv(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        with open('../2018/10/07/player.csv', 'r') as read_file:
            reader = csv.reader(read_file, delimiter=',')
            for row in reader:
                if row[0] != "Number":
                    ht_player_pg.insert_player(conn, 'player', '2018-10-07', row)
        conn.close()

    def test_insert_player_tmp_from_csv(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        # conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        with open('../2018/11/07/player.csv', 'r') as read_file:
            reader = csv.reader(read_file, delimiter=',')
            for row in reader:
                if row[0] != "Number":
                    ht_player_pg.insert_player_tmp(conn, 'player_tmp', '2018-11-07', row)
        conn.close()

    def test_select(self):
        conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        ht_player_pg.select(conn, 'player_tmp', '2018/09/12', [16, 31, 48, 55], 'fw')
        conn.close()

    def test_select_last_2dates(self):
        conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        last_2dates = ht_player_pg.select_last_2dates(conn, 'player_tmp')
        ht_player_pg.print(last_2dates)
        conn.close()

    def test_diff_player_last_2states(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        # conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        last_2dates = ht_player_pg.select_last_2dates(conn, 'player_tmp')
        nums = ht_player_pg.select_num(conn, 'player_tmp', last_2dates)
        ht_player_pg.diff_player_last_2states(conn, "player_tmp", nums, last_2dates)
        conn.close()
