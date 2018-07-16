import psycopg2
from psycopg2.extensions import AsIs


class HattrickPlayerPostgreSQL():

    def select_player(self, conn, time):
        try:
            cursor = conn.cursor()
            query = ""
            query += ""
            query += "SELECT                                                                           " + "\n"
            query += "    date :: VARCHAR(10), num, player, spacial, st,                       --01 05 " + "\n"
            query += "    age, since, tsi, ls, xp,                                             --06 10 " + "\n"
            query += "    fo, stm, lo, mb, kp,                                                 --11 15 " + "\n"
            query += "    df, pm, wi, ps, sc,                                                  --16 20 " + "\n"
            query += "    sp, con, last :: VARCHAR(10), rt :: VARCHAR(3), po,                  --21 25 " + "\n"
            query += "    wage, g, kp_p :: VARCHAR(5), wb_p :: VARCHAR(5), cd_p :: VARCHAR(5), --26 30 " + "\n"
            query += "    w_p :: VARCHAR(5), im_p :: VARCHAR(5), fw_p :: VARCHAR(5)            --31 35 " + "\n"
            query += "FROM player                                                                      " + "\n"
            query += "WHERE                                                                            " + "\n"
            query += "    date = %s -- AND date = last                                                 " + "\n"
            query += "ORDER BY                                                                         " + "\n"
            query += "    num, date                                                                    "
            cursor.execute(query, (time.replace('/', '-'),))
            tuple_list = cursor.fetchall()
            return tuple_list
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(query)
            print(error)
        finally:
            if cursor.closed is False:
                cursor.close()

    def select_count_player(self, conn):
        try:
            cursor = conn.cursor()
            query = "SELECT COUNT(*) FROM player"
            cursor.execute(query)
            row = cursor.fetchone()
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(query)
            print(error)
        finally:
            if cursor.closed is False:
                cursor.close()

    def backup_player(self, conn, target_table, backup_table):
        try:
            cursor = conn.cursor()
            sql = ""
            sql += "CREATE TABLE %(backup_table)s AS ( "
            sql += "    SELECT * FROM %(target_table)s "
            sql += "    ORDER BY date, num             "
            sql += ")                                  "
            cursor.execute(sql,
                           {"backup_table": AsIs(backup_table),
                            "target_table": AsIs(target_table)})
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happend")
            print(error)
            print(sql)
        finally:
            if cursor.closed is False:
                cursor.close()

    def insert_player(self, conn, time, row):
        try:
            cursor = conn.cursor()
            sql = ""
            sql += "INSERT INTO player (                                                                    " + "\n"
            sql += "    date,                                -- 2                                           " + "\n"
            sql += "    num, nat, player, playerid, spacial, -- 3, 4, 5, 6, 7                               " + "\n"
            sql += "    st, age, since, tsi, ls,             -- 8, 9,10,11,12                               " + "\n"
            sql += "    xp, fo, stm, lo, mb,                 --13,14,15,16,17                               " + "\n"
            sql += "    kp, df, pm, wi, ps,                  --18,19,20,21,22                               " + "\n"
            sql += "    sc, sp, con,                         --23,24,25                                     " + "\n"
            sql += "    last,                                --26                                           " + "\n"
            sql += "    rt,                                  --27                                           " + "\n"
            sql += "    po, wage, g,                         --28,29,30                                     " + "\n"
            sql += "    kp_p, wb_p, cd_p, w_p, im_p,         --31,32,33,34,35                               " + "\n"
            sql += "    fw_p                                 --36                                           " + "\n"
            sql += ") (                                                                                     " + "\n"
            sql += "    SELECT                                                                              " + "\n"
            sql += "        to_date(%s, 'YYYY-MM-DD'),                                    -- 2              " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           -- 3, 4, 5, 6, 7  " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           -- 8, 9,10,11,12  " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           --13,14,15,16,17  " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           --18,19,20,21,22  " + "\n"
            sql += "        %s, %s, %s,                                                   --23,24,25        " + "\n"
            sql += "        to_date(coalesce(nullif(%s,''), '0001-01-01'), 'YYYY-MM-DD'), --26              " + "\n"
            sql += "        cast(coalesce(nullif(%s,''),'0.0') as float),                 --27              " + "\n"
            sql += "        %s, %s, %s,                                                   --28,29,30        " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           --31,32,33,34,35  " + "\n"
            sql += "        %s                                                            --36              " + "\n"
            sql += ")                                                                                       " + "\n"
            cursor.execute(sql, (time,
                                 row[0], row[1], row[2], row[3], row[4],
                                 row[5], row[6], row[7], row[8], row[9],
                                 row[10], row[11], row[12], row[13], row[14],
                                 row[15], row[16], row[17], row[18], row[19],
                                 row[20], row[21], row[22],
                                 row[23],
                                 row[24],
                                 row[25], row[26], row[27],
                                 row[30], row[31], row[32], row[33], row[34],
                                 row[35]
                                 ))
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happend")
            print(error)
            print(time)
            print(row)
            print(sql)
        finally:
            if cursor.closed is False:
                cursor.close()

    def print(self, tuple_list):
        for t in tuple_list:
            for i in range(len(t) - 1):
                print(str(t[i]) + ',', end='', flush=True)
            print(str(t[-1]))
