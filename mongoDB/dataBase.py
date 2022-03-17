import pymongo as pg
import userInfo
import tokenList
import dataBase
import buyerList
import authorList
import certifi

def connectDataBase():
    CONNECTION_STRING = 'mongodb+srv://LouisTsai:Q3731722Q@cluster0.so4ff.mongodb.net/AKASWAP?retryWrites=true&w=majority'
    client = pg.MongoClient(CONNECTION_STRING,tlsCAFile=certifi.where())#,ssl=True)#,ssl_cert_reqs='CERT_NONE')
    return client['userList']

dataBase = connectDataBase()

userInfo = dataBase['userInfo']
buyerList = dataBase['buyerList']
authorList = dataBase['authorList']
tokenList = dataBase['tokenList']





