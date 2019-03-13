#!/usr/bin/python
# -*- coding: UTF-8 -*-

from calculate import *

def importData():
    # 每天凌晨定时获取前一天的数据入库
    # startDate= get_yesterday()
    startDate = '2019-02-15'
    endDate = '2019-02-30'
    # 基础数据更新
    # importIndustryDatas()
    # importStockBasics()
    # 根据code更新历史交易数据
    codeList = get_code()
    for code in codeList:
        importKDatas(code, startDate, endDate)
    print "share_k_data 更新完成"

if __name__ == '__main__':
    importData()