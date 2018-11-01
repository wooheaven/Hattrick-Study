import psycopg2
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
            query += "    W_P      NUMERIC(4, 2),               --39 W  Position                     " + "\n"
            query += "    IM_P     NUMERIC(4, 2),               --40 IM Position                     " + "\n"
            query += "    FW_P     NUMERIC(4, 2),               --41 FW Position                     " + "\n"
            query += "    FWd_P    NUMERIC(4, 2),               --42 FW Defensive Position           " + "\n"
            query += "    FWtw_P   NUMERIC(4, 2),               --43 FW Towards Wing Position        " + "\n"
            query += "    TDF_P    NUMERIC(4, 2),               --44 Technical Defensive FW Position " + "\n"
            query += "    B_P      VARCHAR(10),                 --45 Best Position                   " + "\n"
            query += "    B_P_V    VARCHAR(10)                  --46 Best Position Value             " + "\n"
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
            query += "    RT       NUMERIC(2, 1),               --27 Rating                          " + "\n"
            query += "    Po       VARCHAR(5),                  --28 Position                        " + "\n"
            query += "    Wage     BIGINT,                      --29                                 " + "\n"
            query += "    G        INT,                         --30                                 " + "\n"
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
            query += "    IM_P     NUMERIC(4, 2),               --43 IM Position                     " + "\n"
            query += "    FW_P     NUMERIC(4, 2),               --44 FW Position                     " + "\n"
            query += "    FWd_P    NUMERIC(4, 2),               --45 FW Defensive Position           " + "\n"
            query += "    FWtw_P   NUMERIC(4, 2),               --46 FW Towards Wing Position        " + "\n"
            query += "    TDF_P    NUMERIC(4, 2),               --47 Technical Defensive FW Position " + "\n"
            query += "    B_P      VARCHAR(10),                 --48 Best Position                   " + "\n"
            query += "    B_P_V    VARCHAR(10)                  --49 Best Position Value             " + "\n"
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
            sql += "    w_p,                                 --39,           " + "\n"
            sql += "    im_p,                                --40,           " + "\n"
            sql += "    fw_p,  fwd_p, fwtw_p, tdf_p,         --41,42,43,44   " + "\n"
            sql += "    b_p,   b_p_v)                        --45,46         " + "\n"
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
            sql += "    w_p,                                 --39,           " + "\n"
            sql += "    im_p,                                --40,           " + "\n"
            sql += "    fw_p,  fwd_p, fwtw_p, tdf_p,         --41,42,43,44   " + "\n"
            sql += "    b_p,   b_p_v                         --45,46         " + "\n"
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
            sql += "    w_p,                                      --39              " + "\n"
            sql += "    im_p,                                     --40              " + "\n"
            sql += "    fw_p,  fwd_p,  fwtw_p, tdf_p,             --41,42,43,44     " + "\n"
            sql += "    b_p,   b_p_v                              --45,46           " + "\n"
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
            sql += "        %s,                                                           --39,             " + "\n"
            sql += "        %s,                                                           --40,             " + "\n"
            sql += "        %s, %s, %s, %s,                                               --41,42,43,44     " + "\n"
            sql += "        %s, %s                                                        --45,46           " + "\n"
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
                                 row[36],
                                 row[37],
                                 row[38], row[39], row[40], row[41],
                                 row[42], row[43]))
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
            cursor = conn.cursor()
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
            sql += "FROM " + table_name + "                        \n"
            sql += "WHERE                                          \n"
            sql += "    num in " + number_list_str + "             \n"
            sql += "    AND date = '" + time.replace('/', '-') + "'\n"
            sql += "ORDER BY num                                     "
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

    def print(self, tuple_list, sep=','):
        for t in tuple_list:
            for i in range(len(t) - 1):
                print(str(t[i]) + sep, end='', flush=True)
            print(str(t[-1]))
