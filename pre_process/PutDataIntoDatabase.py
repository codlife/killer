
import MySQLdb

if __name__ == '__main__':


    # this method is for ccf_offline_stage1_train.csv
    # &&
    # this method is for ccf_online_stage1_train.csv
    def putDataIntoMysql1(path, table_name):
        try:
            conn = MySQLdb.connect(host="localhost", user="root", passwd='123456', port=3306)
            cur = conn.cursor()
            cur.execute("create database if not exists ccf_data")
            cur.execute('use ccf_data')
            cur.execute('create table if not exists ' + table_name+ '(user_id varchar(20), merchant_id varchar(20), coupon_id varchar(20), discount_rate varchar(20), distance varchar(20), date_received varchar(20), date varchar(20))')

            f = open(path, "r")
            i = 0
            values = []
            for line in f:
                content = line.split(",")

                values.append((content[0], content[1], content[2], content[3], content[4], content[5], content[6]))
                i += 1
                if i > 10000:
                    cur.executemany(
                        'insert into ' + table_name + '(user_id,merchant_id, coupon_id,discount_rate,distance,date_received,date) values(%s,%s,%s,%s,%s,%s,%s)', values)
                    values = []
                    print i

            cur.executemany(
                'insert into ' + table_name + '(user_id,merchant_id, coupon_id,discount_rate,distance,date_received,date) values(%s,%s,%s,%s,%s,%s,%s)',
                values)
            cur.close()
            conn.commit()
            conn.close()
        except MySQLdb.Error, e:
            print "Mysql error %d: %s" % (e.args[0], e.args[1])



    # this method is for table3
    def putDataIntoMysql2(path, table_name):
        try:
            conn = MySQLdb.connect(host="localhost", user="root", passwd='123456', port=3306)
            cur = conn.cursor()
            cur.execute("create database if not exists ccf_data")
            cur.execute('use ccf_data')
            cur.execute(
                'create table if not exists ' + table_name + '(user_id varchar(20), merchant_id varchar(20), coupon_id varchar(20), discount_rate varchar(20), distance varchar(20), date_received varchar(20))')

            f = open(path, "r")
            i = 0
            values = []
            for line in f:
                content = line.split(",")

                values.append((content[0], content[1], content[2], content[3], content[4], content[5]))
                i += 1
                if i > 10000:
                    cur.executemany(
                        'insert into ' + table_name + '(user_id,merchant_id, coupon_id,discount_rate,distance,date_received) values(%s,%s,%s,%s,%s,%s)',values)
                    values = []
                    print i

            cur.executemany(
                'insert into ' + table_name + '(user_id,merchant_id, coupon_id,discount_rate,distance,date_received) values(%s,%s,%s,%s,%s,%s)',
                values)
            cur.close()
            conn.commit()
            conn.close()
        except MySQLdb.Error, e:
            print "Mysql error %d: %s" % (e.args[0], e.args[1])

    path1 = "/usr/data/ccf_data/ccf_offline_stage1_train.csv"
    path2 = "/usr/data/ccf_data/ccf_online_stage1_train.csv"
    path3 = '/usr/data/ccf_data/ccf_offline_stage1_test_revised.csv'
    table_name1 = 'ccf_offline_train'
    table_name2 = 'ccf_online_train'
    table_name3 = 'ccf_offline_test'

    # putDataIntoMysql1(path1, table_name1)
    # putDataIntoMysql1(path2, table_name2)
    putDataIntoMysql2(path3, table_name3)











