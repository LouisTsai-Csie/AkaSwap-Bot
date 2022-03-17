from multiprocessing import Condition
import pymongo as pg
import userInfo
import tokenList
import dataBase as db
import buyerList
import authorList
import certifi
'''
authorList = {
    '_id': string,
    'addressList': [address1, address2 ->string]
    'authorAddress': string,
    'init': bool
    'amount': int,
    'tokenId': [tokenId1, tokenId2 ->int]
}
'''
def authorListInit(userAddr,authorAddr):
    authorList = {
            'addressList': list(userAddr),
            'authorAddress': authorAddr,
            'init': False,
            'amount': 0,
            'tokenId': []
    }
    db.authorList.insert_one(authorList)
    return

def getAuthorList(userAddr,authorAddr):
    condition = {'authorAddress': authorAddr}
    author = db.authorList.find_one(condition)
    if author is None:
        authorListInit(userAddr,authorAddr)
        return db.authorList.find_one(condition)
    return author


def authorListUpdate(userAddr,authorAddr):
    condition = {'authorAddress': authorAddr}
    authorList = getAuthorList(userAddr,authorAddr)
    addressList = authorList['addressList']
    addressList.append(userAddr)
    option = {"$set": {"addressList": addressList}}
    db.authorList.update_one(condition,option)
    return