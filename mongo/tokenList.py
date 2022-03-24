import pymongo as pg
from mongo import dataBase as db
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
def tokenListInit(tokenId):
    tokenList = db.getTokenList()
    List = {
            'addressList': [],
            'init': False,
            'tokenId': tokenId,
            'amount': 0,
            'swapId': []
    }
    tokenList.insert_one(List)
    return

def getTokenList(tokenId):
    tokenList = db.getTokenList()
    condition = {'tokenId': tokenId}
    token = tokenList.find_one(condition)
    if token is None:
        tokenListInit(tokenId)
        return tokenList.find_one(condition)
    return token

def tokenListUpdate(userAddr,tokenId):
    tokenList = db.getTokenList()
    condition = {'tokenId': tokenId}
    token = getTokenList(tokenId)
    addressList = token['addressList']
    addressList.append(userAddr)
    option = {"$set": {"addressList": addressList}}
    tokenList.update_one(condition,option)
    return
