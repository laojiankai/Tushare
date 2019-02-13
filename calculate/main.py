#!/usr/bin/python
# -*- coding: UTF-8 -*-

from calculate import *
import tushare as ts


if __name__ == '__main__':

    #要读取的记录数
    dateNumber = recordNumber = 4
    codeList = get_code()
    #priceCodeList = getCodeForPrice(codeList,dateNumber)
    #rateCodeList = getCodeForRate(priceCodeList, recordNumber)
    #获取以code为key，以pe为value的dict
    #pedict = getPeForCode(rateCodeList)
    dataDict = getDataDict(codeList, dateNumber)
    priceCodeList,closePriceDict = getCodeForPrice3(dataDict, dateNumber)
    rateCodeList = getCodeForRate2(closePriceDict)
    pedict = getPeForCode2(rateCodeList)
    pedictLengthStr = str(len(pedict))
    writeFile(" code  :  pe")
    items = pedict.items()
    items.sort()
    for key, value in items:
        strPeDict = str(key) + ' : ' + str(value)
        print strPeDict
        writeFile(strPeDict)
    pedictLengthStr = "pedictLength : " + pedictLengthStr
    print pedictLengthStr
    writeFile(pedictLengthStr)
