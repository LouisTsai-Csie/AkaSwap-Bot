from importlib.resources import contents
from linebot.models import FlexSendMessage
import json
### 基本設定的功能介面
'''
    基本資訊設定
    button:
        label: 地址輸入
        text: 輸入地址
    button:
        label: 信箱輸入
        text: 輸入信箱
    button:
        label: 追蹤作者輸入
        text: 輸入作者地址
    button:
        label: 追蹤作品輸入
        text: 輸入作品ID
'''
def basicInfo():
    flexMessage = json.load(open('template/basicInfo.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text='基本資訊介面',contents=flexMessage)
    return content

### 買家資訊查詢
'''
    買家資訊查詢
    button:
        label: 最大數量買家
        text: 查詢最大買家
    button:
        label: 數量前N大買家
        text: 輸入N值
    button:
        label: 數量超過M件買家
        text: 輸入M值
    button:
        label: 買家人數
        text: 查詢買家人數
    button:
        label: 販售總數
        text: 查詢販售總數
'''
def buyerInfo():
    flexMessage = json.load(open('template/buyerInfo.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text='買家資訊查詢',contents=flexMessage)
    return content