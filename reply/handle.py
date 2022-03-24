def maxBuyerInfo(maxBuyerDict):
    if not maxBuyerDict:
        return '您目前尚無買家'
    content = '以下為您的最大買家\n\n'
    for key in maxBuyerDict.keys():
        content += key
        content += '\n'
    num = list(maxBuyerDict.values())[0]
    content += (str(len(maxBuyerDict))+ '位買家每人購買了' + str(num) + '件您的作品')
    return content

        
