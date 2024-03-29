import pymongo as pg
from mongo import dataBase as db
from mongo import buyerInfo
#from akaSwap import buyerInfo
'''
buyerList = {
    '_id': string,
    'address': string,
    'sellNum': int,
    'buyerNum': int,
    'maxBuyerInfo': {
        'maxBuyer': string,
        'maxAmount': int
    } ,
    'buyerDict': {
        'address': string,
        'amount': int
    }
}
'''
def buyerListInit(userAddr):
    buyerList = db.getBuyerListDB()
    List = {
        'address': userAddr,
        'sellNum': 0,
        'buyerNum': 0,
        'maxBuyerInfo': {},
        'buyerDict': {}
    }
    buyerList.insert_one(List)
    return

def buyerListUpdate(userAddr):
    buyerList = db.getBuyerListDB()
    condition = {'address': userAddr}
    buyerDict = buyerInfo.getBuyerDict(userAddr)
    maxBuyerAddr = ''
    maxBuyerAmount = 0
    maxBuyerDict = {}
    _buyerList = list(buyerDict.keys())
    sellNum = 0
    for i in range(len(_buyerList)):
        if buyerDict[_buyerList[i]] > maxBuyerAmount:
            maxBuyerAddr = _buyerList[i]
            maxBuyerAmount = buyerDict[_buyerList[i]]
            maxBuyerDict.clear()
            maxBuyerDict = {maxBuyerAddr: maxBuyerAmount}
        elif buyerDict[_buyerList[i]] == maxBuyerAmount:
            maxBuyerAddr = _buyerList[i]
            maxBuyerAmount = buyerDict[_buyerList[i]]
            maxBuyerDict.update({maxBuyerAddr: maxBuyerAmount})
        sellNum += buyerDict[_buyerList[i]]
    option = {'$set': {'sellNum': sellNum}}
    buyerList.update_one(condition,option)
    option = {'$set': {'buyerNum': len(buyerDict)}}
    buyerList.update_one(condition,option)
    option = {'$set': {'maxBuyerInfo': maxBuyerDict}}
    buyerList.update_one(condition,option)
    sortedBuyerList = sorted(buyerDict.items(), key=lambda item: item[1],reverse=True)
    resDict = {}
    for i in range(len(sortedBuyerList)):
        resDict.update({sortedBuyerList[i][0]:sortedBuyerList[i][1]})
    option = {'$set': {'buyerDict': resDict}}
    buyerList.update_one(condition,option)
    return 

def getBuyerList(userAddr):
    buyerList = db.getBuyerListDB()
    condition = {'address': userAddr}
    buyer = buyerList.find_one(condition)
    if buyer is None:
        buyerListInit(userAddr)
        buyerListUpdate(userAddr)
        return buyerList.find_one(condition)
    return buyer

def getMaxBuyerInfo(userAddr):
    buyer = getBuyerList(userAddr)
    return buyer['maxBuyerInfo']


def getSellNum(userAddr):
    buyer = getBuyerList(userAddr)
    return buyer['sellNum']

def getBuyerNum(userAddr):
    buyer = getBuyerList(userAddr)
    return buyer['buyerNum']

def getMaxBuyerInfo(userAddr):
    buyer = getBuyerList(userAddr)
    return buyer['maxBuyerInfo']

def getBuyerDict(userAddr):
    buyer = getBuyerList(userAddr)
    return buyer['buyerDict']

def getNBuyer(userAddr,N):
    N = int(N) if isinstance(N ,str) else N
    buyerDict = getBuyerDict(userAddr)
    if len(buyerDict) <= N:
        return buyerDict
    resDict = {}

    count = 0
    for key, val in buyerDict.items():
        count += 1
        if count >= N:
            break
        resDict.update({key:val})
    return resDict

def getMBuyer(userAddr,M):
    M = int(M) if isinstance(M ,str) else M
    buyerDict = getBuyerDict(userAddr)
    resDict = {}
    for key, val in buyerDict.items():
        if val>=M:
            resDict.update({key:val})
    return resDict
