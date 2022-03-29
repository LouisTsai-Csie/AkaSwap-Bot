def maxBuyerInfo(maxBuyerDict):
    if not maxBuyerDict:
        return '您目前尚無買家'
    content = '以下為您的最大買家\n\n'
    for key in maxBuyerDict.keys():
        content += key
        content += '\n'
    content += '\n'
    num = list(maxBuyerDict.values())[0]
    content += (str(len(maxBuyerDict))+ '位買家每人購買了' + str(num) + '件您的作品')
    return content

def buyerNum(num):
    content = '您總共有' + str(num) + '位買家'
    return content
        
def sellNum(num):
    content = '您總共販售了' + str(num) + '件作品'
    return content

def Nbuyer(buyerDict):
    content = '您的前' + str(len(buyerDict)) + '買家依序為:\n\n'
    for key, value in buyerDict.items():
        content += str(key) + ' 購買 ' + str(value) + '件作品\n'
    return content

def Mbuyer(buyerDict):
    content = '目前有' + str(len(buyerDict)) + '位買家買了超過(含)數量的作品\n'
    for key, value in buyerDict.items():
        content += str(key) + ' 購買 ' + str(value) + '件作品\n'
    return content

def basicInfo(address,Gmail,authorList,tokenList):
    content = '您的基本資訊如下:\n\n'
    content += '您的錢包地址:\n' + address +'\n\n'
    content += '您的電子郵件信箱:\n' + Gmail + '\n'

    content += '\n您的追蹤作者清單如下:\n'
    for i in range(len(authorList)):
        content += str(authorList[i]) + '\n'
    
    content += '\n您的追蹤作品清單如下:\n'
    for i in range(len(tokenList)):
        content += str(tokenList[i]) + '\n'
    
    return content
