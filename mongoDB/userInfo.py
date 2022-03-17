from lib2to3.pgen2 import token
from multiprocessing import Condition
import pymongo as pg
import userInfo
import tokenList
import dataBase as db
import buyerList
import authorList
import certifi
'''
userInfo = {
    '_id': string,
    'LineId': string,
    'address': string,
    'gmail': string,
    'mode': int,
    'state': int,
    'authorList':[address1, address2 -> string],
    'tokenList':[tokenId1, tokenId2 ->int]
}
'''

def userInfoInit(LineId):
    userInfo = {
        'LineId': LineId,
        'address': '',
        'gmail': '',
        'mode': 0,
        'state': 0,
        'authorList': [],
        'tokenList': []
    }
    db.userInfo.insert_one(userInfo)
    return

def getUser(LineId):
    condition = {'LineId': LineId}
    user = db.userInfo.find_one(condition)
    if user is None:
        userInfoInit(LineId)
        return db.userInfo.find_one(condition)
    return user

def userAddrUpdate(user, address):
    condition = {'LineId': user['LineId']}
    option = {"$set": {"address": address}}
    db.userInfo.update_one(condition,option)
    return 


def userGmailUpdate(user,Gmail):
    condition = {'LineId': user['LineId']}
    option = {"$set": {"gmail": Gmail}}
    db.userInfo.update_one(condition,option)
    return 

def userAuthorListUpdate(user,authorAddr):
    condition = {'LineId': user['LineId']}
    authorList = user['authorList']
    authorList.append(authorAddr)
    option = {"$set": {"authorList": authorList}}
    db.userInfo.update_one(condition,option)
    userAddr = user['address']
    authorList.authorListUpdate(userAddr,authorAddr)
    return 
        
def userTokenListUpdate(user,tokenId):
    condition = {'LineId': user['LineId']}
    tokenList = user['tokenList']
    tokenList.append(tokenId)
    option = {"$set": {"tokenList": tokenList}}
    db.userInfo.update_one(condition,option)
    userAddr = user['address']
    tokenList.tokenListUpdate(userAddr,tokenId)
    return

def userModeUpdate(user,tokenId):
    return 

def getUserAddr(user):
    return user['address']

def getUserGmail(user):
    return user['gmail']

def getUserMode(user):
    return user['mode']

def getUserState(user):
    return user['state']