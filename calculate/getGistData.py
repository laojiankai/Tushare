#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import tushare as ts
#import datetime
#import time
from calculate import *
from databaseOperation import *
#from mpl_finance import *
from matplotlib.pylab import date2num
from common import *

def getIndustryClassified():
    #行业分类
    return ts.get_industry_classified()

def getConCeptClassified():
    #概念分类
    return ts.get_concept_classified()

def getAreaClassified():
    #地域分类
    return ts.get_area_classified()

def get_today_date():
    today = datetime.datetime.today()
    dateToday = today.strftime('%Y-%m-%d')
    return dateToday

def get_dates(number):
    datesTimeList=[]
    today = datetime.datetime.today()
    for i in range(number):
        if i==0:
            continue
        elif i>0:
            date = today + datetime.timedelta(days=-i)
            dateTime = date.strftime('%Y-%m-%d')
            datesTimeList.append(dateTime)
    return datesTimeList

def get_yesterday():
    #非节假日使用
    today = datetime.datetime.today()
    yesterday = today+datetime.timedelta(days=-1)
    yesterdayStrTime = yesterday.strftime('%Y-%m-%d')
    return yesterdayStrTime

def get_latest_date(number):
    #获取库里最新的number天的日期
    dateList = []
    sql = 'SELECT distinct date FROM share_k_data  order by date desc limit %d' %number
    dateTuple =  mysql_select(sql)
    for date in dateTuple:
        dateList.append(date[0])
    print "get_latest_date():获取到的dateList列表：" + str(dateList)
    return dateList

def get_latest_date2(number):
    #获取库里最新的number天的日期
    dateTuple2 = []
    sql = 'SELECT distinct date FROM share_k_data  order by date desc limit %d' %number
    dateTuple =  mysql_select(sql)
    if dateTuple:
        for date in dateTuple:
            dateTuple2.append(date[0])
    dateTuple2 = tuple(dateTuple2)
    print "dateTuple2:" + str(dateTuple2)
    return dateTuple2

def get_code():
    #获取所有code放到list
    codeList = []
    sql='select DISTINCT code from share_stock_basics order by code'
    dataTuple = mysql_select(sql)
    for codeTuple in dataTuple:
        codeList.append(codeTuple[0])
        #print "get_code():获取code值get_code()：" + str(code)
    #print "get_code():获取到的codeList列表：" + str(codeList)
    #print "codeNumber is " + str(len(codeList))
    return codeList

def get_dataPrice_list(code,date):
    sql="select open,close from share_k_data where code='%s' and date='%s'" %(code,date)
    priceTuple = mysql_select(sql)
    if priceTuple:
        priceList = list(priceTuple[0])
    else:
        priceList = []
    print "code:" + str(code) + ",日期：" + str(date)  + ",价格：" + str(priceList)
    return priceList   #dataList[0] 开盘价 dataList[1] 收盘价

def get_dataPrice_list2(code,dateTuple):
    sql="select open,close from share_k_data where code='%s' and date in %s" %(code,dateTuple)
    priceTuple = mysql_select(sql)
    return priceTuple

def get_dataPrice_list3(codeTuple,dateTuple):
    sql="select code,open,close from share_k_data where code in %s and date in %s order by code,date" %(codeTuple,dateTuple)
    priceTuple = mysql_select(sql)
    return priceTuple

def get_hist_data(code,number):
    sql = "select date,open,close,high,low from share_k_data where code='%s' ORDER BY date desc limit %d" %(code, number)
    dataTuple = mysql_select(sql)
    dataList = []
    if dataTuple:
        for data in dataTuple:
            data_list = list(data)
            #将时间转换为数字
            data_time = datetime.datetime.strptime(data_list[0], '%Y-%m-%d')
            t = date2num(data_time)
            open,close,high,low = data_list[1:]
            datas = (t,open,close,high,low)
            dataList.append(datas)
    print dataList
    return dataList

#date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')
#t = date2num(date_time)
#open, high, low, close = row[:4]
#datas = (t, open, high, low, close)
#data_list.append(datas)


def get_closePrice(code,recordNumber):
    try:
        sql="select DISTINCT close from share_k_data where code='%s' order by date desc limit %s " %(code,recordNumber)
        closePriceTuple = mysql_select(sql)
        closePriceList = []
        if len(closePriceTuple) == recordNumber:
            for i in range(len(closePriceTuple)):
                closePrice = list(closePriceTuple[i])
                closePriceList.append(closePrice[0])
        return closePriceList
    except Exception,e:
        getExpcetion(Exception, e)

def get_closePrice2(code,recordNumber):
    try:
        sql="select DISTINCT close from share_k_data where code='%s' order by date desc limit %s " %(code,recordNumber)
        closePriceTuple = mysql_select(sql)
        closePriceList = []
        if len(closePriceTuple) == recordNumber:
            for i in range(len(closePriceTuple)):
                closePrice = list(closePriceTuple[i])
                closePriceList.append(closePrice[0])
        return closePriceList
    except Exception,e:
        getExpcetion(Exception, e)

def get_chg(close,closeBefore):
    #计算涨跌幅 当天收盘价-前一天收盘价／前一天收盘价
    rate = (close-closeBefore)*100/closeBefore
    return round(rate,2)

# 市盈率
def get_pe(code,startNum=0, endNum=9999):
    sql="select pe from share_stock_basics where code = '%s'" %code
    peTuple = mysql_select(sql)
    #print pe
    if peTuple:
        pe = peTuple[0][0]
        if startNum <= pe <= endNum:
            return pe
        else:
            return

def get_pe2(codeTuple,startNum=0, endNum=9999):
    sql="select code,pe from share_stock_basics where code in %s" %codeTuple
    pe2codeTuple = mysql_select(sql)
    return pe2codeTuple



def writeFile(content):
    with open("./outPort.txt",'w') as f:
        f.write(content)
        f.write("\n")

if __name__ == '__main__':

    code = '600600'
    number = 2
    #print type(get_data_list(code,date))
    #print get_yesterday()
    #print get_latest_date(3)
    pe = get_pe(code,0,1000000)
    print pe

    print get_hist_data("600600", 2)
