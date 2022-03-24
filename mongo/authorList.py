import pymongo as pg
from mongo import dataBase as db
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
def authorListInit(authorAddr):
    authorList = db.getAuthorListDB()
    List = {
            'addressList': [],
            'authorAddress': authorAddr,
            'init': False,
            'amount': 0,
            'tokenId': []
    }
    authorList.insert_one(List)
    return

def getAuthorList(authorAddr):
    authorList = db.getAuthorListDB()
    condition = {'authorAddress': authorAddr}
    author = authorList.find_one(condition)
    if author is None:
        authorListInit(authorAddr)
        return authorList.find_one(condition)
    return author


def authorListUpdate(userAddr,authorAddr):
    authorList = db.getAuthorListDB()
    condition = {'authorAddress': authorAddr}
    author = getAuthorList(authorAddr)
    addressList = author['addressList']
    addressList.append(userAddr)
    option = {"$set": {"addressList": addressList}}
    authorList.update_one(condition,option)
    return
