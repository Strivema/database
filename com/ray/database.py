# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/30 19:41
# @Software: PyCharm
import pymysql
import uuid
import random


def get_conn():
    conn = pymysql.connect(host='172.18.18.205', port=3306, user='root', password='root', db='demo',
                           charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return conn


def insert(sql):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()


def query(sql):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall();
    print(type(res))
    conn.commit()
    cur.close()
    conn.close()
    return res


def update(sql):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    find = 'select * from temp'
    res = query(find)
    for row in res:
        print(row)
        print(type(row))

        add = """INSERT INTO device_environment
                    (id, rainfall, temperature, humidity, wind_speed, wind_trend,soil_temperature, soil_humidity, soil_conductivity, wind_velocity, so2Value, no2Value, pm25Value, pm10Value, o31hValue, coValue, nagativeIon)
                        VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})""" \
            .format("uuid()", 0, random.uniform(20, 30),
                    random.uniform(55, 70), "'四级'", "'东南'", random.uniform(20, 30),
                    random.uniform(40, 80), random.uniform(0.3, 0.8), random.uniform(5, 7),
                    row['SO2Value'], row['NO2Value'], row['PM25Value'], row['PM10Value'], row['O31HValue'],
                    row['COValue'], random.uniform(10, 20))
        print(add)
        # insert(add)
