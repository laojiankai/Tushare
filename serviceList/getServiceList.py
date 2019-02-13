#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

host = '192.168.1.246'
PORT = '3306'
user = 'root'
passwd = '*TL0ei3!io'
database = 'AutoTest'


def mysql_select(sql):
    #连接数据库
    db = pymysql.connect(host, user, passwd,database)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    cursor.execute(sql)
    list = cursor.fetchall()
    db.close()
    return list


if __name__ == '__main__':

    serviceAutoList_sql = 'SELECT distinct sev_name from  AutoTest.service_list_auto where sev_name like "%aladdin-dms%" '

    serviceList_sql = 'SELECT service_name FROM AutoTest.service_list where  system_name like "%aladdin-dms%" and del_flag = 0 order by service_name'

    serviceAutoTuple = mysql_select(serviceAutoList_sql)
    serviceTuple = mysql_select(serviceList_sql)
    #print serviceAutoTuple
    serviceAutoNameList = []
    serviceNameList = []
    settleServiceList = []
    for serviceAutoName in serviceAutoTuple:
        serviceAutoNameList.append(serviceAutoName[0])

    for serviceName in serviceTuple:
        serviceNameList.append(serviceName[0])
    #print serviceAutoNameList

    #serviceAutoNameList = ['aladdin-dms.deliverCentre.purchaseOrder.queryCargoPackageInfo']
    #serviceNameList = ['aladdin-dms.deliverCentre.purchaseOrder.queryCargoPackageInfo.{}']
    for serviceAutoName2 in serviceAutoNameList:
        for serviceName2 in serviceNameList:
            if serviceName2.find(serviceAutoName2) == 0 and serviceAutoName2.find(serviceName2) == -1:
                settleServiceList.append(serviceName2)
            else:
                continue
    print settleServiceList
    print len(settleServiceList)
    #print serviceName2.find(serviceAutoName2),serviceAutoName2.find(serviceName2)


