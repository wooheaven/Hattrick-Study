from unittest import TestCase
import psycopg2
from postgresql import ht_match_postgresql


class TestHattrickMatchPostgreSQL(TestCase):
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
