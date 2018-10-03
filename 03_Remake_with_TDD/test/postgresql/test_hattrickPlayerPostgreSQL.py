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
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        ht_player_pg.backup_player(conn=conn, target_table='player_tmp', backup_table='player_tmp_backup')
        conn.close()

    def test_insert_player_from_select(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        ht_player_pg.insert_player_from_select(conn, target_table='player_tmp', from_table='player')
        conn.close()

    def test_create_player(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        # conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        ht_player_pg.drop_table(conn=conn, target_table='player_tmp')
        # ht_player_pg.create_player(conn=conn, target_table='player')
        ht_player_pg.create_player_tmp(conn=conn, target_table='player_tmp')
        conn.close()

    def test_insert_player_tmp_from_csv(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        with open('../2018/10/02/player.csv', 'r') as read_file:
            reader = csv.reader(read_file, delimiter=',')
            for row in reader:
                if row[0] != "Number":
                    ht_player_pg.insert_player_tmp(conn, 'player_tmp', '2018-10-02', row)
        conn.close()

    def test_insert_player_from_csv(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        with open('../2018/09/18/player.csv', 'r') as read_file:
            reader = csv.reader(read_file, delimiter=',')
            for row in reader:
                if row[0] != "Number":
                    ht_player_pg.insert_player(conn, 'player', '2018-09-18', row)
        conn.close()

    def test_select(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        tuple_list = ht_player_pg.select(conn, 'player_tmp', '2018/09/12', [16, 31, 48, 55], 'fw')
        ht_player_pg.print(tuple_list)
        conn.close()
