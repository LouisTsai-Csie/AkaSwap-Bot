import requests
import json

address = 'tz1LBMHonxg8VuShNm6BJXKwWMUsDZ5cE2QB'

def getUserCreationUrl(address):
    #https://akaswap.com/api/accounts/{address}/creations
    Url = ''
    Url += 'https://akaswap.com/api/accounts/'
    Url += address
    Url += '/creations'
    return Url

def getAkaObjUrl(tokenId):
    #https://akaswap.com/api/akaobjs/{tokenId}
    Url = ''
    Url += 'https://akaswap.com/api/akaobjs/'
    Url += tokenId
    return Url

def getAllCreationTokenId(address):
    headers = {"Accept": "application/json"}
    CreationListResponse = requests.request("GET", getUserCreationUrl(address), headers=headers)
    CreationDataList = CreationListResponse.json()['creations']
    TokenIdList = []
    for i in range(len(CreationDataList)):
        TokenIdList.append(CreationDataList[i]['tokenId'])
    return TokenIdList


def getAllCreationOwner(token):
    headers = {"Accept": "application/json"}
    AkaObjDataResponse = requests.request("GET", getAkaObjUrl(token), headers=headers)
    AkaObjData = AkaObjDataResponse.json()['token']
    AkaObjOwnerDict = AkaObjData['owners']
    return AkaObjOwnerDict

def getBuyerDict(address):
    BuyerList = {}
    tokenIdList = getAllCreationTokenId(address)
    for i in range(len(tokenIdList)):
        CreationOwnerDict = getAllCreationOwner(str(tokenIdList[i]))
        CreationOwnerList = list(CreationOwnerDict.keys())
        for j in range(len(CreationOwnerList)):
            if CreationOwnerList[j] not in BuyerList:
                BuyerList[CreationOwnerList[j]] = CreationOwnerDict[CreationOwnerList[j]]
            else:
                BuyerList[CreationOwnerList[j]] += CreationOwnerDict[CreationOwnerList[j]]
    return BuyerList

def getBuyerDictFile(address):
    BuyerList = getBuyerDict(address)
    fileName = 'BuyerList.json'
    file = open(fileName,"w")
    json.dump(BuyerList,file)
    file.close()
    return

