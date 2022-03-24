from linebot.models import FlexSendMessage
import json
### 基本設定的功能介面
def basicInfo():
    flexMessage = json.load(open('template/basicInfo.json','r+',encoding='UTF-8'))
    content = FlexSendMessage(alt_text= '基本介面',content=flexMessage)
    return content
### 
