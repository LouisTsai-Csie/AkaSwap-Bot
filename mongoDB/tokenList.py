import pymongo as pg
import userInfo
import tokenList
import dataBase as db
import buyerList
import authorList
import certifi
'''
tokenList = {
    '_id': string
    'addressList': [adress1, address2 ...]
    'init': bool,
    'tokenId': int,
    'amount': int,
    'swapId': [swapId1, swapId2 ->int]
}
'''
def tokenListInit(userAddr,tokenId):
    tokenList = {
            'addressList': list(userAddr),
            'init': False,
            'tokenId': tokenId,
            'amount': 0,
            'swapId': []
    }
    db.tokenList.insert_one(tokenList)
    return

def getTokenList(userAddr,tokenId):
    condition = {'tokenId': tokenId}
    token = db.tokenList.find_one(condition)
    if token is None:
        tokenListInit(userAddr,tokenId)
        return db.tokenList.find_one(condition)
    return token

def tokenListUpdate(userAddr,tokenId):
    condition = {'tokenId': tokenId}
    tokenList = getTokenList(userAddr,tokenId)
    addressList = tokenList['addressList']
    addressList.append(userAddr)
    option = {"$set": {"addressList": addressList}}
    db.tokenList.update_one(condition,option)
    return