#!/usr/bin/python
# -*- coding: UTF-8 -*-

from calculate import *
from common import getExpcetion
#import time
#import traceback


resultRate = []

def getDataDict(codeList,dateNumber):
    dataDict = {}
    codeTuple = tuple(codeList)
    latestDateTuple = get_latest_date2(dateNumber)
    priceCodeTuple = get_dataPrice_list3(codeTuple, latestDateTuple)
    print "priceCodeTuple:" + str(priceCodeTuple)
    valueList = []
    for i in range(len(priceCodeTuple)):
        if i == 0:
            key = priceCodeTuple[i][0]
            value = (priceCodeTuple[i][1],priceCodeTuple[i][2])
            valueList.append(value)
        if i > 0:
            if priceCodeTuple[i][0] == priceCodeTuple[i-1][0]:
                value = (priceCodeTuple[i][1],priceCodeTuple[i][2])
                valueList.append(value)
            else:
                valueTuple = tuple(valueList)
                #print valueTuple
                dataDict[key] = valueTuple
                key = priceCodeTuple[i][0]
                valueList = []
                value = (priceCodeTuple[i][1], priceCodeTuple[i][2])
                valueList.append(value)
    print dataDict
    return dataDict

def getCodeForPrice(codeList,dateNumber):
    try:
        priceCodeList = []
        #获取连续N的天收盘价>=开盘价的code值
        latestDateList = get_latest_date(dateNumber)
        #codeList = ['300688','300691','300693']
        for code in codeList:
            #初始值i=0
            i = 0
            for date in latestDateList:
                priceList =get_dataPrice_list(code,date)
                if priceList:
                    if priceList[0] <= priceList[1]:
                        i=i+1
                        continue
                    else:
                        break
                else:
                    break
            if i == dateNumber:
                priceCodeList.append(code)
            if not priceList or priceList[0] > priceList[1]:
                continue
            print "getCodeForPrice():当前code值：" + str(code)
        print 'priceCodeList=' + str(priceCodeList)
        print "priceCodeListLength:" + str(len(priceCodeList))
        return priceCodeList
    except Exception, e:
        getExpcetion(Exception,e)

def getCodeForPrice2(codeList,dateNumber):
    try:
        priceCodeList = []
        closePriceDict = {}
        #获取连续N的天收盘价>=开盘价的code值
        latestDateTuple = get_latest_date2(dateNumber)
        for code in codeList:
            #初始值i=0
            i = 0
            print code
            closePriceList = []
            priceCodeTuple = get_dataPrice_list2(code,latestDateTuple)
            print "priceCodeTuple:" + str(priceCodeTuple)
            if priceCodeTuple:
                if len(priceCodeTuple) < dateNumber:
                    continue
                for priceCode in priceCodeTuple:
                    if priceCode[0] <= priceCode[1]:
                        i = i + 1
                        continue
                    else:
                        break
                if i == dateNumber:
                    priceCodeList.append(code)
                    for priceCode in priceCodeTuple:
                        closePriceList.append(priceCode[1])
                    closePriceDict[code] = closePriceList
            else:
                continue
        return priceCodeList,closePriceDict
    except Exception, e:
        getExpcetion(Exception,e)

def getCodeForPrice3(dataDict,dateNumber):
    try:
        priceCodeList = []
        closePriceDict = {}
        #获取连续N的天收盘价>=开盘价的code值
        codeList = dataDict.keys()
        for code in codeList:
            #初始值i=0
            i = 0
            closePriceList = []
            priceCodeTuple = dataDict[code]
            #print "priceCodeTuple:" + str(priceCodeTuple)
            if priceCodeTuple:
                if len(priceCodeTuple) < dateNumber:
                    continue
                for priceCode in priceCodeTuple:
                    if priceCode[0] <= priceCode[1]:
                        i = i + 1
                        continue
                    else:
                        break
                if i == dateNumber:
                    priceCodeList.append(code)
                    for priceCode in priceCodeTuple:
                        closePriceList.append(priceCode[1])
                    closePriceDict[code] = closePriceList
            else:
                continue
        return priceCodeList,closePriceDict
    except Exception, e:
        getExpcetion(Exception,e)

def getCodeForRate(codeList,recordNumber):
    try:
        #计算当天涨跌幅
        resultList = []
        rateCodeList = []
        #计算涨跌幅（当天收盘价-前一天收盘价）获取第一天涨跌幅0 < rateList[0] < 3；其他时间涨跌幅0 < rate < 1.5 的code值
        for code in codeList:
            rateList = []
            closePriceList = get_closePrice(code,recordNumber)
            print closePriceList
            if closePriceList:
                for i in range(len(closePriceList)-1):
                    rate = get_chg(closePriceList[i],closePriceList[i+1])
                    rateList.append(rate)
                if len(rateList) == len(closePriceList)-1:
                    rateList2 = []
                    #最近一天涨跌幅
                    if 0 < rateList[0] < 5:
                        rateList2.append(rateList[0])
                        #最近一天外其他时间涨跌幅
                        for rate in rateList[1:]:
                            if 0 < rate < 2:
                                rateList2.append(rate)
                            else:
                                break
                    if len(rateList2) == len(rateList):
                        #print code, rateList2
                        rateCodeList.append(code)
                        resultList.append(code + ":" + str(rateList2))
            else:
                continue
        print 'rateCodeList=' + str(rateCodeList)
        print "rateCodeListLength:" + str(len(rateCodeList))
        return rateCodeList
    except Exception, e:
        getExpcetion(Exception, e)

def getCodeForRate2(closePriceDict):
    try:
        #计算当天涨跌幅
        resultList = []
        rateCodeList = []
        #计算涨跌幅（当天收盘价-前一天收盘价）获取第一天涨跌幅0 < rateList[0] < 3；其他时间涨跌幅0 < rate < 1.5 的code值
        for code in closePriceDict.keys():
            rateList = []
            #倒序排列
            closePriceList = closePriceDict[code]
            closePriceList.reverse()
            if closePriceList:
                for i in range(len(closePriceList)-1):
                    rate = get_chg(closePriceList[i],closePriceList[i+1])
                    rateList.append(rate)
                if len(rateList) == len(closePriceList)-1:
                    rateList2 = []
                    #最近一天涨跌幅
                    if 0 < rateList[0] < 5:
                        rateList2.append(rateList[0])
                        #最近一天外其他时间涨跌幅
                        for rate in rateList[1:]:
                            if 0 < rate < 2:
                                rateList2.append(rate)
                            else:
                                break
                    if len(rateList2) == len(rateList):
                        #print code, rateList2
                        rateCodeList.append(code)
                        resultList.append(code + ":" + str(rateList2))
            else:
                continue
        print 'rateCodeList=' + str(rateCodeList)
        print "rateCodeListLength:" + str(len(rateCodeList))
        return rateCodeList
    except Exception, e:
        getExpcetion(Exception, e)

def getCodeForPe(CodeList,startPE=0,stopPE=100):
    #获取市盈率在startPE到stopPE之间的code
    peCodeList = []
    for code in CodeList:
        #time.sleep(1)
        pe = get_pe(code,startPE,stopPE)
        if pe:
            peCodeList.append(code)
        else:
            print code +':'+ 'pe值不在startPE&stopPE范围内'
    print 'peCodeList=' + str(peCodeList)
    return peCodeList

def getPeForCode(codeList):
    #初始化dict,用code做为key，然后赋值value为pe
    peDict = dict().fromkeys(codeList)
    for code in codeList:
        pe = get_pe(code)
        if pe:
            peDict[code] = pe
    return peDict

def getPeForCode2(codeList):
    #初始化dict,用code做为key，然后赋值value为pe
    #peDict = dict().fromkeys(codeTuple)
    peDict = {}
    listLength = len(codeList)
    if listLength ==1:
        codeTupleStr = "('"+codeList[0]+"')"
    else:
        codeTuple = tuple(codeList)
        codeTupleStr = str(codeTuple)
    pe2codeTuple = get_pe2(codeTupleStr)
    for pe2code in pe2codeTuple:
        key = pe2code[0]
        value = pe2code[1]
        peDict[key] = value
    print peDict
    return peDict

def writeFile(resultList,fileName='./outPort.txt'):

    with open(fileName,'a') as f:
        if resultList:
            f.write(str(resultList) + "\n")
            #f.write('\n')
        else:
            f.write("没有查找到符合条件的数据！")
        f.close()