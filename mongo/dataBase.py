import pymongo as pg
import certifi

def connectDataBase():
    CONNECTION_STRING = 'mongodb+srv://LouisTsai:Q3731722Q@cluster0.so4ff.mongodb.net/AKASWAP?retryWrites=true&w=majority'
    client = pg.MongoClient(CONNECTION_STRING,tlsCAFile=certifi.where())#,ssl=True)#,ssl_cert_reqs='CERT_NONE')
    return client['userList']

def getUserInfoDB():
    dataBase = connectDataBase()
    return dataBase['userInfo']

def getAuthorListDB():
    dataBase = connectDataBase()
    return dataBase['authorList']

def getBuyerListDB():
    dataBase = connectDataBase()
    return dataBase['buyerList']

def getTokenListDB():
    dataBase = connectDataBase()
    return dataBase['tokenList']






