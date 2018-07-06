import psycopg2


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

    def print(self, tuple_list):
        for t in tuple_list:
            for i in range(len(t) - 1):
                print(str(t[i]) + ',', end='', flush=True)
            print(str(t[-1]))