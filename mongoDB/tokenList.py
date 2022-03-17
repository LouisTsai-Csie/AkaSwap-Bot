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
    'tokenoId': int,
    'amount': int,
    'swapId': [swapId1, swapId2 ->int]
}
'''
def tokenListUpdate(userAddr,tokenId):
    condition = {'tokenId': tokenId}
    token = db.tokenList.find_one(condition)
    if token is None:
        tokenList = {
            'addressList': list(userAddr),
            'init': False,
            'tokenId': tokenId,
            'amount': 0,
            'swapId': []
        }
        db.tokenList.insert_one(tokenList)
    else:
        token['addressList'].append(userAddr)
        db.tokenList.update(condition,token)
    return
