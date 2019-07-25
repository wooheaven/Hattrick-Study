from unittest import TestCase
import psycopg2
from postgresql import ht_match_postgresql, ht_player_postgresql


class TestHattrickMatchPostgreSQL(TestCase):
    def test_backup_match(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        # conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        from_table_name = 'match'
        to_table_name = 'match_backup'
        ht_player_pg.drop_table(conn=conn, target_table=to_table_name)
        ht_player_pg.backup_player(conn=conn, from_table=from_table_name, to_table=to_table_name)
        conn.close()

    def test_insert_match_from_select(self):
        # conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_match_pg = ht_match_postgresql.HattrickMatchPostgreSQL()
        from_table_name = 'tmp'
        to_table_name = 'match'
        ht_match_pg.insert_to_match_from_select(conn, to_table=to_table_name, from_table=from_table_name)
        conn.close()

    def test_create_match(self):
        # conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
        ht_player_pg = ht_player_postgresql.HattrickPlayerPostgreSQL()
        ht_match_pg = ht_match_postgresql.HattrickMatchPostgreSQL()
        ht_match_table_name = 'match'
        ht_player_pg.drop_table(conn=conn, target_table=ht_match_table_name)
        ht_match_pg.create_match(conn=conn, target_table=ht_match_table_name)
        # ht_player_pg.create_player(conn=conn, target_table=ht_player_table_name)
        # ht_player_pg.create_player_tmp(conn=conn, target_table=ht_player_table_name)
        conn.close()

    def test_getMatchByPoNum(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        hattrickMatchPostgresql = ht_match_postgresql.HattrickMatchPostgreSQL()
        tupleList = hattrickMatchPostgresql.getMatchByPoNum(conn, 'FW', [16, 18, 31, 48, 55])
        hattrickMatchPostgresql.printMatchByPoNum(tupleList, [16, 18, 31, 48, 55])
    def test_getMatchByDate(self):
        conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")
        hattrickMatchPostgresql = ht_match_postgresql.HattrickMatchPostgreSQL()
        tupleList = hattrickMatchPostgresql.getMatchByDate("2018/06/17", conn)
        hattrickMatchPostgresql.printMatchByDate(tupleList)
