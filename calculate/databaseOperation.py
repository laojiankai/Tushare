#!/usr/bin/python
# -*- coding: UTF-8 -*-

from calculate import *
#import MySQLdb
import pymysql
from sqlalchemy import create_engine
import tushare as ts


host = '127.0.0.1'
PORT = '3306'
user = 'root'
passwd = '1qaz!QAZ'
database = 'tushare'
# 数据库链接
#engine = create_engine('mysql://root:1qaz!QAZ@127.0.0.1/tushare?charset=utf8')
engine = create_engine('mysql+pymysql://root:1qaz!QAZ@127.0.0.1/tushare?charset=utf8')


def mysql_select(sql):
    #连接数据库
    db = pymysql.connect(host, user, passwd,database)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    cursor.execute(sql)
    list = cursor.fetchall()
    db.close()
    return list

def mysql_updateORdelete(sql):
    #连接数据库
    db = pymysql.connect(host, user, passwd,database)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        print "updateORdelete success"
        db.commit()
    except:
        db.rollback()
        print "updateORdelete failed"
    db.close()

def importIndustryDatas():

    sql='delete from share_industry_data'
    mysql_updateORdelete(sql)
    dIndustry = ts.get_industry_classified()
    # 存入数据库
    #dIndustry.to_sql('share_industry_data', engine)
    #追加数据到现有表
    dIndustry.to_sql('share_industry_data',engine,if_exists='append')
    print "share_industry_data 数据更新完成"

def importStockBasics():

    sql='delete from share_stock_basics'
    mysql_updateORdelete(sql)
    stockBasics = ts.get_stock_basics()
    # 存入数据库
    #stockBasics.to_sql('share_stock_basics', engine)
    #追加数据到现有表
    stockBasics.to_sql('share_stock_basics',engine,if_exists='append')
    print 'update share_stock_basics success'


def importKDatas(code,startDate,endDate):
    #print code,startDate
    dk = ts.get_k_data(code, start=startDate,end=endDate)
    dk.to_sql('share_k_data',engine,if_exists='append')
    print "share_k_data %s:更新完成" %code

def importHisDate(code):
    #一次性获取全部日k线数据
    hd = ts.get_hist_data(code)
    hd.to_sql('share_his_data',engine)
    print "share_his_data %s:更新完成" %code

def importHData(code):

    hd = ts.get_hist_data(code)
    print hd
    #hd.to_sql('share_h_data',engine,if_exists='append')
    #print "share_h_data %s:更新完成" %code

if __name__ == '__main__':
    importStockBasics()