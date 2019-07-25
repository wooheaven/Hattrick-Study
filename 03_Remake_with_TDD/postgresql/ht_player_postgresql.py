import psycopg2
import pandas as pd
from tabulate import tabulate

from psycopg2.extensions import AsIs


class HattrickPlayerPostgreSQL():

    def drop_table(self, conn, target_table):
        try:
            cursor = conn.cursor()
            query = "DROP TABLE IF EXISTS %(target_table)s"
            cursor.execute(query, {"target_table": AsIs(target_table)})
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(query)
            print(error)
        finally:
            if cursor.closed is False:
                cursor.close()

    def create_player_tmp(self, conn, target_table):
        try:
            cursor = conn.cursor()
            query = ""
            query += "CREATE TABLE %(target_table)s (                                                " + "\n"
            query += "    id       SERIAL NOT NULL PRIMARY KEY, --01 Prevent Duplication             " + "\n"
            query += "    Date     DATE,                        --02                                 " + "\n"
            query += "    Num      INT,                         --03                                 " + "\n"
            query += "    Nat      VARCHAR(30),                 --04                                 " + "\n"
            query += "    Player   VARCHAR(30),                 --05                                 " + "\n"
            query += "    PlayerID BIGINT,                      --06                                 " + "\n"
            query += "    Spacial  VARCHAR(30),                 --07                                 " + "\n"
            query += "    st       VARCHAR(10),                 --08 Status Yellow, Red              " + "\n"
            query += "    Age      VARCHAR(10),                 --09                                 " + "\n"
            query += "    Since    VARCHAR(30),                 --10                                 " + "\n"
            query += "    TSI      BIGINT,                      --11                                 " + "\n"
            query += "    LS       INT,                         --12                                 " + "\n"
            query += "    XP       INT,                         --13                                 " + "\n"
            query += "    Fo       INT,                         --14                                 " + "\n"
            query += "    Stm      INT,                         --15                                 " + "\n"
            query += "    Lo       INT,                         --16                                 " + "\n"
            query += "    MB       BOOLEAN,                     --17                                 " + "\n"
            query += "    KP       INT,                         --18                                 " + "\n"
            query += "    DF       INT,                         --19                                 " + "\n"
            query += "    PM       INT,                         --20                                 " + "\n"
            query += "    WI       INT,                         --21                                 " + "\n"
            query += "    PS       INT,                         --22                                 " + "\n"
            query += "    SC       INT,                         --23                                 " + "\n"
            query += "    SP       INT,                         --24                                 " + "\n"
            query += "    con      BIGINT,                      --25 Psico                           " + "\n"
            query += "    Last     DATE,                        --26                                 " + "\n"
            query += "    RT       NUMERIC(2, 1),               --27 Rating                          " + "\n"
            query += "    Po       VARCHAR(5),                  --28 Position                        " + "\n"
            query += "    Wage     BIGINT,                      --29                                 " + "\n"
            query += "    G        INT,                         --30 Goal                            " + "\n"
            query += "    KP_P     NUMERIC(4, 2),               --31 KP Position                     " + "\n"
            query += "    WBd_P    NUMERIC(4, 2),               --32 WB Defensive Position           " + "\n"
            query += "    WB_P     NUMERIC(4, 2),               --33 WB Position                     " + "\n"
            query += "    WBtm_P   NUMERIC(4, 2),               --34 WB Towards Middle Position      " + "\n"
            query += "    WBo_P    NUMERIC(4, 2),               --35 WB Offensive Position           " + "\n"
            query += "    CD_P     NUMERIC(4, 2),               --36 CD Position                     " + "\n"
            query += "    CDtw_P   NUMERIC(4, 2),               --37 CD Position                     " + "\n"
            query += "    CDo_P    NUMERIC(4, 2),               --38 CD Position                     " + "\n"
            query += "    Wd_P     NUMERIC(4, 2),               --39 W  Position                     " + "\n"
            query += "    W_P      NUMERIC(4, 2),               --40 W  Position                     " + "\n"
            query += "    Wtm_P    NUMERIC(4, 2),               --41 W  Position                     " + "\n"
            query += "    Wo_P     NUMERIC(4, 2),               --42 W  Position                     " + "\n"
            query += "    IMd_P    NUMERIC(4, 2),               --43 IM Position                     " + "\n"
            query += "    IM_P     NUMERIC(4, 2),               --44 IM Position                     " + "\n"
            query += "    IMtw_P   NUMERIC(4, 2),               --45 IM Position                     " + "\n"
            query += "    IMo_P    NUMERIC(4, 2),               --46 IM Position                     " + "\n"
            query += "    FW_P     NUMERIC(4, 2),               --47 FW Position                     " + "\n"
            query += "    FWd_P    NUMERIC(4, 2),               --48 FW Defensive Position           " + "\n"
            query += "    FWtw_P   NUMERIC(4, 2),               --49 FW Towards Wing Position        " + "\n"
            query += "    TDF_P    NUMERIC(4, 2),               --50 Technical Defensive FW Position " + "\n"
            query += "    B_P      VARCHAR(10),                 --51 Best Position                   " + "\n"
            query += "    B_P_V    VARCHAR(10)                  --52 Best Position Value             " + "\n"
            query += ") "
            cursor.execute(query, {"target_table": AsIs(target_table)})
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(query)
            print(error)
        finally:
            if cursor.closed is False:
                cursor.close()

    def create_player(self, conn, target_table):
        try:
            cursor = conn.cursor()
            query = ""
            query += "CREATE TABLE %(target_table)s (                                                " + "\n"
            query += "    id       SERIAL NOT NULL PRIMARY KEY, --01 Prevent Duplication             " + "\n"
            query += "    Date     DATE,                        --02                                 " + "\n"
            query += "    Num      INT,                         --03                                 " + "\n"
            query += "    Nat      VARCHAR(30),                 --04                                 " + "\n"
            query += "    Player   VARCHAR(30),                 --05                                 " + "\n"
            query += "    PlayerID BIGINT,                      --06                                 " + "\n"
            query += "    Spacial  VARCHAR(30),                 --07                                 " + "\n"
            query += "    st       VARCHAR(10),                 --08 Status Yellow, Red              " + "\n"
            query += "    Age      VARCHAR(10),                 --09                                 " + "\n"
            query += "    Since    VARCHAR(30),                 --10                                 " + "\n"
            query += "    TSI      BIGINT,                      --11                                 " + "\n"
            query += "    LS       INT,                         --12                                 " + "\n"
            query += "    XP       INT,                         --13                                 " + "\n"
            query += "    Fo       INT,                         --14                                 " + "\n"
            query += "    Stm      INT,                         --15                                 " + "\n"
            query += "    Lo       INT,                         --16                                 " + "\n"
            query += "    MB       BOOLEAN,                     --17                                 " + "\n"
            query += "    KP       INT,                         --18                                 " + "\n"
            query += "    DF       INT,                         --19                                 " + "\n"
            query += "    PM       INT,                         --20                                 " + "\n"
            query += "    WI       INT,                         --21                                 " + "\n"
            query += "    PS       INT,                         --22                                 " + "\n"
            query += "    SC       INT,                         --23                                 " + "\n"
            query += "    SP       INT,                         --24                                 " + "\n"
            query += "    con      BIGINT,                      --25 Psico                           " + "\n"
            query += "    Last     DATE,                        --26                                 " + "\n"
            query += "    RT       NUMERIC(3, 1),               --27 Rating                          " + "\n"
            query += "    Po       VARCHAR(5),                  --28 Position                        " + "\n"
            query += "    Wage     BIGINT,                      --29                                 " + "\n"
            query += "    G        INT,                         --30 Goal                            " + "\n"
            query += "    KP_P     NUMERIC(4, 2),               --31 KP Position                     " + "\n"
            query += "    WBd_P    NUMERIC(4, 2),               --32 WB Defensive Position           " + "\n"
            query += "    WB_P     NUMERIC(4, 2),               --33 WB Position                     " + "\n"
            query += "    WBtm_P   NUMERIC(4, 2),               --34 WB Towards Middle Position      " + "\n"
            query += "    WBo_P    NUMERIC(4, 2),               --35 WB Offensive Position           " + "\n"
            query += "    CD_P     NUMERIC(4, 2),               --36 CD Position                     " + "\n"
            query += "    CDtw_P   NUMERIC(4, 2),               --37 CD Position                     " + "\n"
            query += "    CDo_P    NUMERIC(4, 2),               --38 CD Position                     " + "\n"
            query += "    Wd_P     NUMERIC(4, 2),               --39 W  Position                     " + "\n"
            query += "    W_P      NUMERIC(4, 2),               --40 W  Position                     " + "\n"
            query += "    Wtm_P    NUMERIC(4, 2),               --41 W  Position                     " + "\n"
            query += "    Wo_P     NUMERIC(4, 2),               --42 W  Position                     " + "\n"
            query += "    IMd_P    NUMERIC(4, 2),               --43 IM Position                     " + "\n"
            query += "    IM_P     NUMERIC(4, 2),               --44 IM Position                     " + "\n"
            query += "    IMtw_P   NUMERIC(4, 2),               --45 IM Position                     " + "\n"
            query += "    IMo_P    NUMERIC(4, 2),               --46 IM Position                     " + "\n"
            query += "    FW_P     NUMERIC(4, 2),               --47 FW Position                     " + "\n"
            query += "    FWd_P    NUMERIC(4, 2),               --48 FW Defensive Position           " + "\n"
            query += "    FWtw_P   NUMERIC(4, 2),               --49 FW Towards Wing Position        " + "\n"
            query += "    TDF_P    NUMERIC(4, 2),               --50 Technical Defensive FW Position " + "\n"
            query += "    B_P      VARCHAR(10),                 --51 Best Position                   " + "\n"
            query += "    B_P_V    VARCHAR(10)                  --52 Best Position Value             " + "\n"
            query += ") "
            cursor.execute(query, {"target_table": AsIs(target_table)})
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(query)
            print(error)
        finally:
            if cursor.closed is False:
                cursor.close()

    def select_player(self, conn, table_name, time):
        try:
            cursor = conn.cursor()
            query = ""
            query += "SELECT                                                                   " + "\n"
            query += "    date :: VARCHAR(10), num, player, spacial, st,      --01 05          " + "\n"
            query += "    age, since, tsi, ls, xp,                            --06 10          " + "\n"
            query += "    fo, stm, lo, mb, kp,                                --11 15          " + "\n"
            query += "    df, pm, wi, ps, sc,                                 --16 20          " + "\n"
            query += "    sp, con, last :: VARCHAR(10), rt :: VARCHAR(3), po, --21,22,23,24,25 " + "\n"
            query += "    wage, g,                                            --26,27          " + "\n"

            query += "    kp_p :: VARCHAR(5),                                 --28,            " + "\n"

            query += "    wbd_p  :: VARCHAR(5),                               --29,            " + "\n"
            query += "    wb_p   :: VARCHAR(5),                               --30,            " + "\n"
            query += "    wbtm_p :: VARCHAR(5),                               --31             " + "\n"

            query += "    cd_p   :: VARCHAR(5),                               --32,            " + "\n"
            query += "    cdtw_p :: VARCHAR(5),                               --33,            " + "\n"
            query += "    cdo_p  :: VARCHAR(5),                               --34,            " + "\n"

            query += "    w_p    :: VARCHAR(5),                               --35,            " + "\n"
            query += "    im_p   :: VARCHAR(5),                               --36,            " + "\n"

            query += "    fw_p   :: VARCHAR(5),                               --37             " + "\n"
            query += "    fwd_p  :: VARCHAR(5),                               --38             " + "\n"
            query += "    fwtw_p :: VARCHAR(5),                               --39             " + "\n"
            query += "    tdf_p  :: VARCHAR(5),                               --40             " + "\n"

            query += "    b_p    :: VARCHAR(8),                               --41             " + "\n"
            query += "    b_p_v  :: VARCHAR(8)                                --42             " + "\n"

            query += "FROM " + table_name + "                                                  " + "\n"
            query += "WHERE                                                                    " + "\n"
            query += "    date = %s                                                            " + "\n"
            query += "ORDER BY                                                                 " + "\n"
            query += "    num, date                                                            "

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

    def select_count_player(self, conn, table_name):
        try:
            cursor = conn.cursor()
            query = "SELECT COUNT(*) FROM %(table_name)s"
            cursor.execute(query, {"table_name": AsIs(table_name)})
            row = cursor.fetchone()
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(query)
            print(error)
        finally:
            if cursor.closed is False:
                cursor.close()

    def backup_player(self, conn, from_table, to_table):
        try:
            cursor = conn.cursor()
            sql = ""
            sql += "CREATE TABLE %(to_table)s AS ( "
            sql += "    SELECT * FROM %(from_table)s "
            sql += "    ORDER BY date, num             "
            sql += ")                                  "
            cursor.execute(sql,
                           {"to_table": AsIs(to_table),
                            "from_table": AsIs(from_table)})
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error happened")
            print(error)
            print(sql)
        finally:
            if cursor.closed is False:
                cursor.close()

    def insert_player_from_select(self, conn, to_table, from_table):
        try:
            cursor = conn.cursor()
            sql = ""
            sql += "INSERT INTO %(to_table)s (                               " + "\n"
            sql += "    date,                                -- 2            " + "\n"
            sql += "    num, nat, player, playerid, spacial, -- 3, 4, 5, 6, 7" + "\n"
            sql += "    st, age, since, tsi, ls,             -- 8, 9,10,11,12" + "\n"
            sql += "    xp, fo, stm, lo, mb,                 --13,14,15,16,17" + "\n"
            sql += "    kp, df, pm, wi, ps,                  --18,19,20,21,22" + "\n"
            sql += "    sc, sp, con,                         --23,24,25      " + "\n"
            sql += "    last,                                --26            " + "\n"
            sql += "    rt,                                  --27            " + "\n"
            sql += "    po, wage, g,                         --28,29,30      " + "\n"
            sql += "    kp_p,                                --31,           " + "\n"
            sql += "    wbd_p, wb_p,   wbtm_p, wbo_p,        --32,33,34,35,  " + "\n"
            sql += "    cd_p,  cdtw_p, cdo_p,                --36,37,38      " + "\n"
            sql += "    wd_p,  w_p,    wtm_p,  wo_p,         --39,40,41,42   " + "\n"
            sql += "    im_p,                                --43,           " + "\n"
            sql += "    fw_p,  fwd_p,  fwtw_p, tdf_p,        --44,45,46,47   " + "\n"
            sql += "    b_p,   b_p_v)                        --48,49         " + "\n"
            sql += "(SELECT                                                  " + "\n"
            sql += "    date,                                -- 2            " + "\n"
            sql += "    num, nat, player, playerid, spacial, -- 3, 4, 5, 6, 7" + "\n"
            sql += "    st, age, since, tsi, ls,             -- 8, 9,10,11,12" + "\n"
            sql += "    xp, fo, stm, lo, mb,                 --13,14,15,16,17" + "\n"
            sql += "    kp, df, pm, wi, ps,                  --18,19,20,21,22" + "\n"
            sql += "    sc, sp, con,                         --23,24,25      " + "\n"
            sql += "    last,                                --26            " + "\n"
            sql += "    rt,                                  --27            " + "\n"
            sql += "    po, wage, g,                         --28,29,30      " + "\n"
            sql += "    kp_p,                                --31,           " + "\n"
            sql += "    wbd_p, wb_p,  wbtm_p, wbo_p,         --32,33,34,35,  " + "\n"
            sql += "    cd_p,  cdtw_p, cdo_p,                --36,37,38      " + "\n"
            sql += "    wd_p,  w_p,    wtm_p,  wo_p,         --39,40,41,42   " + "\n"
            sql += "    im_p,                                --43,           " + "\n"
            sql += "    fw_p,  fwd_p,  fwtw_p, tdf_p,        --44,45,46,47   " + "\n"
            sql += "    b_p,   b_p_v                         --48,49         " + "\n"
            sql += "FROM %(from_table)s                                      " + "\n"
            sql += "ORDER BY date,num)                                       " + "\n"
            cursor.execute(sql,
                           {"from_table": AsIs(from_table),
                            "to_table": AsIs(to_table)})
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error happened")
            print(error)
            print(sql)

    def insert_player(self, conn, table_name, time, row):
        try:
            cursor = conn.cursor()
            sql = ""
            sql += "INSERT INTO " + table_name + " (                                " + "\n"
            sql += "    date,                                     -- 2,             " + "\n"
            sql += "    num,   nat,    player, playerid, spacial, -- 3, 4, 5, 6, 7, " + "\n"
            sql += "    st,    age,    since,  tsi,      ls,      -- 8, 9,10,11,12, " + "\n"
            sql += "    xp,    fo,     stm,    lo,       mb,      --13,14,15,16,17, " + "\n"
            sql += "    kp,    df,     pm,     wi,       ps,      --18,19,20,21,22, " + "\n"
            sql += "    sc,    sp,     con,                       --23,24,25,       " + "\n"
            sql += "    last,                                     --26,             " + "\n"
            sql += "    rt,                                       --27,             " + "\n"
            sql += "    po,    wage,   g,                         --28,29,30,       " + "\n"
            sql += "    kp_p,                                     --31,             " + "\n"
            sql += "    wbd_p, wb_p,   wbtm_p, wbo_p,             --32,33,34,35,    " + "\n"
            sql += "    cd_p,  cdtw_p, cdo_p,                     --36,37,38,       " + "\n"
            sql += "    wd_p,   w_p,   wtm_p,   wo_p,             --39,40,41,42     " + "\n"
            sql += "    im_p,                                     --43              " + "\n"
            sql += "    fw_p,  fwd_p,  fwtw_p, tdf_p,             --44,45,46,47     " + "\n"
            sql += "    b_p,   b_p_v                              --48,49           " + "\n"
            sql += ") (                                                                                     " + "\n"
            sql += "    SELECT                                                                              " + "\n"
            sql += "        to_date(%s, 'YYYY-MM-DD'),                                    -- 2,             " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           -- 3, 4, 5, 6, 7, " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           -- 8, 9,10,11,12, " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           --13,14,15,16,17, " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           --18,19,20,21,22, " + "\n"
            sql += "        %s, %s, %s,                                                   --23,24,25,       " + "\n"
            sql += "        to_date(coalesce(nullif(%s,''), '0001-01-01'), 'YYYY-MM-DD'), --26,             " + "\n"
            sql += "        cast(coalesce(nullif(%s,''),'0.0') as float),                 --27,             " + "\n"
            sql += "        %s, %s, %s,                                                   --28,29,30,       " + "\n"
            sql += "        %s,                                                           --31,             " + "\n"
            sql += "        %s, %s, %s, %s,                                               --32,33,34,35,    " + "\n"
            sql += "        %s, %s, %s,                                                   --36,37,38,       " + "\n"
            sql += "        %s, %s, %s, %s,                                               --39,40,41,42     " + "\n"
            sql += "        %s,                                                           --43,             " + "\n"
            sql += "        %s, %s, %s, %s,                                               --44,45,46,47     " + "\n"
            sql += "        %s, %s                                                        --48,49           " + "\n"
            sql += ")                                                                                       " + "\n"
            cursor.execute(sql, (time,
                                 row[0],  row[1],  row[2],  row[3],  row[4],
                                 row[5],  row[6],  row[7],  row[8],  row[9],
                                 row[10], row[11], row[12], row[13], row[14],
                                 row[15], row[16], row[17], row[18], row[19],
                                 row[20], row[21], row[22],
                                 row[23],
                                 row[24],
                                 row[25], row[26], row[27],
                                 row[28],
                                 row[29], row[30], row[31], row[32],
                                 row[33], row[34], row[35],
                                 row[36], row[37], row[38], row[39],
                                 row[40],
                                 row[41], row[42], row[43], row[44],
                                 row[45], row[46]))
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error happened")
            print(error)
            print(time)
            print(row)
            print(sql)
        finally:
            if cursor.closed is False:
                cursor.close()

    def insert_player_tmp(self, conn, table_name, time, row):
        try:
            cursor = conn.cursor()
            sql = ""
            sql += "INSERT INTO " + table_name + " (                                " + "\n"
            sql += "    date,                                     -- 2,             " + "\n"
            sql += "    num,   nat,    player, playerid, spacial, -- 3, 4, 5, 6, 7, " + "\n"
            sql += "    st,    age,    since,  tsi,      ls,      -- 8, 9,10,11,12, " + "\n"
            sql += "    xp,    fo,     stm,    lo,       mb,      --13,14,15,16,17, " + "\n"
            sql += "    kp,    df,     pm,     wi,       ps,      --18,19,20,21,22, " + "\n"
            sql += "    sc,    sp,     con,                       --23,24,25,       " + "\n"
            sql += "    last,                                     --26,             " + "\n"
            sql += "    rt,                                       --27,             " + "\n"
            sql += "    po,    wage,   g,                         --28,29,30,       " + "\n"
            sql += "    kp_p,                                     --31,             " + "\n"
            sql += "    wbd_p, wb_p,   wbtm_p, wbo_p,             --32,33,34,35,    " + "\n"
            sql += "    cd_p,  cdtw_p, cdo_p,                     --36,37,38,       " + "\n"
            sql += "    wd_p,  w_p,    wtm_p,   wo_p,             --39,40,41,42     " + "\n"
            sql += "    imd_p, im_p,   imtw_p, imo_p,             --43,44,45,46     " + "\n"
            sql += "    fw_p,  fwd_p,  fwtw_p, tdf_p,             --47,48,49,50     " + "\n"
            sql += "    b_p,   b_p_v                              --51,52           " + "\n"
            sql += ") (                                                                                     " + "\n"
            sql += "    SELECT                                                                              " + "\n"
            sql += "        to_date(%s, 'YYYY-MM-DD'),                                    -- 2,             " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           -- 3, 4, 5, 6, 7, " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           -- 8, 9,10,11,12, " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           --13,14,15,16,17, " + "\n"
            sql += "        %s, %s, %s, %s, %s,                                           --18,19,20,21,22, " + "\n"
            sql += "        %s, %s, %s,                                                   --23,24,25,       " + "\n"
            sql += "        to_date(coalesce(nullif(%s,''), '0001-01-01'), 'YYYY-MM-DD'), --26,             " + "\n"
            sql += "        cast(coalesce(nullif(%s,''),'0.0') as float),                 --27,             " + "\n"
            sql += "        %s, %s, %s,                                                   --28,29,30,       " + "\n"
            sql += "        %s,                                                           --31,             " + "\n"
            sql += "        %s, %s, %s, %s,                                               --32,33,34,35,    " + "\n"
            sql += "        %s, %s, %s,                                                   --36,37,38,       " + "\n"
            sql += "        %s, %s, %s, %s,                                               --39,40,41,42     " + "\n"
            sql += "        %s, %s, %s, %s,                                               --43,44,45,46     " + "\n"
            sql += "        %s, %s, %s, %s,                                               --47,48,49,50     " + "\n"
            sql += "        %s, %s                                                        --51,52           " + "\n"
            sql += ")                                                                                       " + "\n"
            cursor.execute(sql, (time,
                                 row[0],  row[1],  row[2],  row[3],  row[4],
                                 row[5],  row[6],  row[7],  row[8],  row[9],
                                 row[10], row[11], row[12], row[13], row[14],
                                 row[15], row[16], row[17], row[18], row[19],
                                 row[20], row[21], row[22],
                                 row[23],
                                 row[24],
                                 row[25], row[26], row[27],
                                 row[28],
                                 row[29], row[30], row[31], row[32],
                                 row[33], row[34], row[35],
                                 row[36], row[37], row[38], row[39],
                                 row[40], row[41], row[42], row[43],
                                 row[44], row[45], row[46], row[47],
                                 row[48], row[49]))
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error happened")
            print(error)
            print(time)
            print(row)
            print(sql)
        finally:
            if cursor.closed is False:
                cursor.close()

    def select(self, conn, table_name, time, number_list, mode):
        try:
            number_list_str = "("
            for num in number_list:
                number_list_str += str(num) + ","
            number_list_str = number_list_str[:-1]
            number_list_str += ")"
            sql = ""
            sql += "SELECT                                         \n"
            if mode == "fw":
                sql += "    num, b_p, b_p_v, fw_p, fwd_p, fwtw_p, tdf_p\n"
            elif mode == "wb":
                sql += "    num, b_p, b_p_v, wbd_p, wb_p, wbtm_p, wbo_p\n"
            elif mode == "cd":
                sql += "    num, b_p, b_p_v, cd_p, cdtw_p, cdo_p\n"
            elif mode == "w":
                sql += "    num, b_p, b_p_v, wd_p, w_p, wtm_p, wo_p\n"
            elif mode == "im":
                sql += "    num, b_p, b_p_v, imd_p, im_p, imtw_p, imo_p\n"
            sql += "FROM " + table_name + "                        \n"
            sql += "WHERE                                          \n"
            sql += "    num in " + number_list_str + "             \n"
            sql += "    AND date = '" + time.replace('/', '-') + "'\n"
            sql += "ORDER BY num                                     "
            df = pd.read_sql_query(sql, conn)
            include_cols = []
            for col in df.columns:
                if col not in ['num', 'b_p', 'b_p_v']:
                    include_cols.append(col)
            idxmax_list = []
            max_list = []
            for iloc_num in range(len(df)):
                idxmax_list.append(df.iloc[iloc_num][include_cols].astype(float).idxmax())
                max_list.append(df.iloc[iloc_num][include_cols].astype(float).max())
            df['idxmax'] = pd.Series(idxmax_list)
            df['max'] = pd.Series(max_list)

            with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000,
                                   'display.colheader_justify', 'right'):
                print(tabulate(df, headers='keys', tablefmt='psql'))
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(sql)
            print(error)

    def select_last_2dates(self, conn, table_name):
        try:
            cursor = conn.cursor()
            sql = "SELECT date FROM " + table_name + " GROUP BY date ORDER BY date DESC LIMIT 2"
            cursor.execute(sql)
            tuple_list = cursor.fetchall()
            return tuple_list
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(sql)
            print(error)
        finally:
            if cursor.closed is False:
                cursor.close()

    def select_num(self, conn, table_name, last_2dates):
        try:
            sql = "SELECT num FROM " + table_name + " WHERE num < 98 and date in ("
            for tuple in last_2dates:
                sql += "\'" + str(tuple[0]) + "\',"
            sql = sql[0:-1]
            sql += ") GROUP BY num ORDER BY num"
            cursor = conn.cursor()
            cursor.execute(sql)
            tuple_list = cursor.fetchall()
            return tuple_list
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(sql)
            print(error)
        finally:
            if cursor.closed is False:
                cursor.close()

    def diff_player_last_2states(self, conn, table_name, nums, last_2dates):
        try:
            last_2dates_str = ""
            for date in last_2dates:
                last_2dates_str += "\'" + str(date[0]) + "\',"
            last_2dates_str = last_2dates_str[0:-1]
            for num in nums:
                num = num[0]
                sql = ""
                sql += "SELECT "
                sql += "    date, num, playerid, "
                sql += "    age, tsi, ls, xp, "
                sql += "    fo, stm, lo, kp, "
                sql += "    df, pm, wi, ps, sc, sp, con, last, rt, po, "
                sql += "    kp_p, wbd_p, wb_p, wbtm_p, wbo_p, cd_p, cdtw_p, cdo_p, wd_p, "
                sql += "    w_p,wtm_p,wo_p,imd_p,im_p,imtw_p,imo_p,fw_p,fwd_p,fwtw_p,tdf_p,b_p,b_p_v "
                sql += "FROM "
                sql += "    " + table_name + "\n"
                sql += "WHERE "
                sql += "    num = " + str(num) + " AND date IN (" + last_2dates_str + ") "
                sql += "ORDER BY date "
                df = pd.read_sql_query(sql, conn)
                diff_dict = dict()

                diff_dict['date'] = (df['date'][1] - df['date'][0]).days

                df.num = df.num.astype('str')
                diff_dict['num'] = df['num'][1] == df['num'][0]
                if diff_dict['num']:
                    diff_dict['num'] = ''

                diff_dict['playerid'] = ''
                diff_dict['age'] = ''
                diff_dict['last'] = ''
                diff_dict['po'] = ''
                diff_dict['b_p'] = ''
                diff_dict['b_p_v'] = ''
                diff_dict['idxmax'] = ''
                diff_dict['max'] = ''

                self.remove_column_basic(df, diff_dict)
                if df['po'][0] == 'KP':
                    self.remove_column_wb(df)
                    self.remove_column_cd(df)
                    self.remove_column_w(df)
                    self.remove_column_im(df)
                    self.remove_column_fw(df)
                    self.diff_row_to_row(df, diff_dict, ['kp_p'])
                elif df['po'][0] == 'CD':
                    self.remove_column_kp(df)
                    self.remove_column_wb(df)
                    self.remove_column_w(df)
                    self.remove_column_im(df)
                    self.remove_column_fw(df)
                    self.diff_row_to_row(df, diff_dict, ['cd_p', 'cdtw_p', 'cdo_p'])
                elif df['po'][0] == 'WB':
                    self.remove_column_kp(df)
                    self.remove_column_cd(df)
                    self.remove_column_w(df)
                    self.remove_column_im(df)
                    self.remove_column_fw(df)
                    self.diff_row_to_row(df, diff_dict, ['wbd_p', 'wb_p', 'wbtm_p', 'wbo_p'])
                elif df['po'][0] == 'W':
                    self.remove_column_kp(df)
                    self.remove_column_wb(df)
                    self.remove_column_cd(df)
                    self.remove_column_im(df)
                    self.remove_column_fw(df)
                    self.diff_row_to_row(df, diff_dict, ['wd_p', 'w_p', 'wtm_p', 'wo_p'])
                elif df['po'][0] == 'IM':
                    self.remove_column_kp(df)
                    self.remove_column_wb(df)
                    self.remove_column_cd(df)
                    self.remove_column_w(df)
                    self.remove_column_fw(df)
                    self.diff_row_to_row(df, diff_dict, ['imd_p', 'im_p', 'imtw_p', 'imo_p'])
                elif df['po'][0] == 'FW':
                    self.remove_column_kp(df)
                    self.remove_column_wb(df)
                    self.remove_column_cd(df)
                    self.remove_column_w(df)
                    self.remove_column_im(df)
                    self.diff_row_to_row(df, diff_dict, ['fw_p', 'fwd_p', 'fwtw_p', 'tdf_p'])
                elif df['po'][0] == '':
                    self.remove_column_kp(df)
                    self.remove_column_wb(df)
                    self.remove_column_cd(df)
                    self.remove_column_w(df)
                    self.remove_column_im(df)
                    self.remove_column_fw(df)

                self.remove_duplicated_value_of_last_row(df)

                df = df.append(pd.DataFrame([diff_dict]), ignore_index=True, sort=False)
                with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000,
                                       'display.colheader_justify','right'):
                    print(tabulate(df, headers='keys', tablefmt='psql'))
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happen")
            print(error)
            print(sql)

    def diff_row_to_row(self, df, diff_dict, col_names, type='float'):
        for col_name in col_names:
            if type =='int':
                df[col_name] = df[col_name].astype(int)
            elif type == 'float':
                df[col_name] = df[col_name].astype(float)
            value = df[col_name][1] - df[col_name][0]
            if value > 0:
                diff_dict[col_name] = value
            else:
                diff_dict[col_name] = ''
        df_0_idxmax = df.iloc[0][col_names].astype(type).idxmax()
        df_0_max = df.iloc[0][col_names].astype(type).max()
        df_1_idxmax = df.iloc[1][col_names].astype(type).idxmax()
        df_1_max = df.iloc[1][col_names].astype(type).max()

        df['idxmax'] = pd.Series([df_0_idxmax, df_1_idxmax])
        df['idxmax'].astype(str)
        df['max'] = pd.Series([df_0_max, df_1_max])
        df['max'].astype(str)

    def remove_column_basic(self, df, diff_dict):
        for col in ['tsi', 'ls', 'xp', 'fo', 'stm', 'lo', 'kp', 'df', 'pm', 'wi', 'ps', 'sc', 'sp', 'con']:
            df[col] = df[col].astype(int)
            value = df[col][1] - df[col][0]
            if value == 0:
                del df[col]
            else:
                diff_dict[col] = value
        for col in ['rt']:
            df['rt'] = df['rt'].astype(float)
            value = df[col][1] - df[col][0]
            if value == 0:
                del df[col]
            else:
                diff_dict[col] = value

    def remove_column_kp(self, df):
        self.remove_column_of_df(df, ['kp_p'])

    def remove_column_wb(self, df):
        self.remove_column_of_df(df, ['wbd_p', 'wb_p', 'wbtm_p', 'wbo_p'])

    def remove_column_cd(self, df):
        self.remove_column_of_df(df, ['cd_p', 'cdtw_p', 'cdo_p'])

    def remove_column_w(self, df):
        self.remove_column_of_df(df, ['wd_p', 'w_p', 'wtm_p', 'wo_p'])

    def remove_column_im(self, df):
        self.remove_column_of_df(df, ['imd_p', 'im_p', 'imtw_p', 'imo_p'])

    def remove_column_fw(self, df):
        self.remove_column_of_df(df, ['fw_p', 'fwd_p', 'fwtw_p', 'tdf_p'])

    def remove_column_of_df(self, df, column_names_to_be_remove):
        for col_name in column_names_to_be_remove:
            del df[col_name]

    def remove_duplicated_value_of_last_row(self, df):
        for col in df.columns:
            if str(df[col][0]) == str(df[col][1]):
                df[col][1] = ''

    def print(self, tuple_list, sep=','):
        for t in tuple_list:
            for i in range(len(t) - 1):
                print(str(t[i]) + sep, end='', flush=True)
            print(str(t[-1]))
