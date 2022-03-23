import pymongo as pg
import dataBase as db
import authorList
import tokenList
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
    userInfo = db.getUserInfoDB()
    Info = {
        'LineId': LineId,
        'address': '',
        'gmail': '',
        'mode': 0,
        'state': 0,
        'authorList': [],
        'tokenList': []
    }
    userInfo.insert_one(Info)
    return

def getUser(LineId):
    userInfo = db.getUserInfoDB()
    condition = {'LineId': LineId}
    user = userInfo.find_one(condition)
    if user is None:
        userInfoInit(LineId)
        return userInfo.find_one(condition)
    return user

def getUserAddr(user):
    return user['address']

def getUserGmail(user):
    return user['gmail']

def getUserMode(user):
    return user['mode']

def getUserState(user):
    return user['state']

def getUserAutorList(user):
    return user['authorList']

def getUserTokenList(user):
    return user['tokenList']

def userAddrUpdate(user, address):
    userInfo = db.getUserInfoDB()
    condition = {'LineId': user['LineId']}
    option = {"$set": {"address": address}}
    userInfo.update_one(condition,option)
    return

def userGmailUpdate(user,Gmail):
    userInfo = db.getUserInfoDB()
    condition = {'LineId': user['LineId']}
    option = {"$set": {"gmail": Gmail}}
    userInfo.update_one(condition,option)
    return 

def userModeUpdate(user,mode):
    userInfo = db.getUserInfoDB()
    condition = {'LineId': user['LineId']}
    option = {"$set": {"mode": mode}}
    userInfo.update_one(condition,option)
    return 

def userStateUpdate(user,state):
    userInfo = db.getUserInfoDB()
    condition = {'LineId': user['LineId']}
    option = {"$set": {"state": state}}
    userInfo.update_one(condition,option)
    return

def userAuthorListUpdate(user,authorAddr):
    userInfo = db.getUserInfoDB()
    condition = {'LineId': user['LineId']}
    author = user['authorList']
    author.append(authorAddr)
    option = {"$set": {"authorList": author}}
    userInfo.update_one(condition,option)
    userAddr = user['address']
    authorList.authorListUpdate(userAddr,authorAddr)
    return 
        
def userTokenListUpdate(user,tokenId):
    userInfo = db.getUserInfoDB()
    condition = {'LineId': user['LineId']}
    token = user['tokenList']
    token.append(tokenId)
    option = {"$set": {"tokenList": token}}
    userInfo.update_one(condition,option)
    userAddr = user['address']
    tokenList.tokenListUpdate(userAddr,tokenId)
    return


