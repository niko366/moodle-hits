# Nama  : LMS Hits
# Desc  : program untuk mengetahui aktivitas pengunjung seperti active user,page view,unique ip di semua moodle PENABUR
# Niko M, 28/03/2020

import mysql.connector
from mysql.connector import errorcode

try:
    # database config moodle
    cnx = mysql.connector.connect(
        user="your username",
        password="your password",
        database="your database",
        host="localhost"
    )

    db_lms = cnx.cursor(buffered=True)  # Select mysql credential moodle
    CurlUpdate = cnx.cursor(buffered=True)  # Insert hasil ke dalam database

    query_config = ("SELECT nama_sekolah,hostname,db_name,username,password FROM app1_moodleconfig")
    db_lms.execute(query_config)

    for (nama_sekolah, hostname, db_name, username, password) in db_lms:
        try:
            moodle = mysql.connector.connect(
                user=username,
                password=password,
                database=db_name,
                host=hostname
            )
            cursor = moodle.cursor()
            cursor.execute("SELECT \
                               COUNT(DISTINCT userid) 'unique userid' , \
                               COUNT(*) 'page requests',\
                               COUNT(DISTINCT ip) 'unique ip' ,\
                               TIMESTAMP (FROM_UNIXTIME(timecreated)) 'time'\
                               FROM mdl_logstore_standard_log \
                               WHERE 1=1\
                               AND timecreated >  UNIX_TIMESTAMP('2020-03-16 00:00:00')\
                               AND timecreated <= UNIX_TIMESTAMP('2019-03-27 23:59:00')\
                               GROUP BY DAYOFMONTH(FROM_UNIXTIME(timecreated))")
            hits = cursor.fetchall()
            for hit in hits:
                data = (" INSERT INTO  a_hits \
                                (sekolah,unique_user,unique_page_request,unique_ip,time) \
                                VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE sekolah = sekolah")
                CurlUpdate.execute(data, (nama_sekolah, hit[0], hit[1], hit[2], hit[3]))

                cnx.commit()
            print("{} selasai!".format(nama_sekolah))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        else:
            moodle.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

else:
    cnx.close()
