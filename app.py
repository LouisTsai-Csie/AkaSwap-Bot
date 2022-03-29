from lib2to3.pgen2 import token
from typing import Text
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
### Import 套件
import re
#import json

### Import 外部檔案
import config
import mode
import state
#from mongoDB import dataBase
from mongo import userInfo
from mongo import buyerList
from mongo import tokenList
from mongo import authorList

from mongo import buyerInfo

from reply import handle
from reply import reply

from template import flexHandler

app = Flask(__name__)

line_bot_api = LineBotApi(config.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.CHANNEL_ACESS_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text).strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    user_name = profile.display_name #使用者名稱
    uid = profile.user_id # 發訊者ID

    #檢查用戶是否存在
    user = userInfo.getUser(uid)
    userMode = userInfo.getUserMode(user)
    userState = userInfo.getUserState(user)

    #=============================
    if userMode == mode.INIT_MODE:
        ### 資訊查詢
        if re.match("資訊查詢",msg):
            address = userInfo.getUserAddr(user)
            Gmail = userInfo.getUserGmail(user)
            authorList = userInfo.getUserAutorList(user)
            tokenList = userInfo.getUserTokenList(user)
            content = handle.basicInfo(address,Gmail,authorList,tokenList)
            line_bot_api.push_message(uid,TextSendMessage(content))
            return

        ### 基本資訊設定
        if re.match("基本設定",msg):
            content = flexHandler.basicInfo()
            line_bot_api.push_message(uid,content)
            return

        elif re.match("輸入地址",msg):
            userInfo.userModeUpdate(user,mode.ADDR_INPUT)
            content = reply.addrInputMsg
            line_bot_api.push_message(uid,TextSendMessage(content))
            return 

        elif re.match("輸入信箱",msg):
            userInfo.userModeUpdate(user,mode.GMAIL_INPUT)
            content = reply.gmailInputMsg
            line_bot_api.push_message(uid,TextSendMessage(content))
            return
        
        elif re.match("輸入作者地址",msg):
            userInfo.userModeUpdate(user,mode.AUTHORLIST_INPUT)
            content = reply.authorInputMsg
            line_bot_api.push_message(uid,TextSendMessage(content))
            return
    
        elif re.match("輸入作品ID",msg):
            userInfo.userModeUpdate(user,mode.TOKENLIST_INPUT)
            content = reply.tokenInputMsg
            line_bot_api.push_message(uid,TextSendMessage(content))
            return
        
        ### 買家資訊查詢
        if re.match("買家資訊",msg):
            content = flexHandler.buyerInfo()
            line_bot_api.push_message(uid,content)
            return
        
        elif re.match("查詢最大買家",msg):
            userAddr = userInfo.getUserAddr(user)
            if not userAddr:
                content = reply.userAddrLack
                line_bot_api.push_message(uid,TextSendMessage(content))
            else:
                buyerDict = buyerList.getMaxBuyerInfo(userAddr)
                content = handle.maxBuyerInfo(buyerDict)
                line_bot_api.push_message(uid,TextSendMessage(content))
            return

        elif re.match("輸入N值",msg):
            userAddr = userInfo.getUserAddr(user)
            if userAddr:
                userInfo.userModeUpdate(user,mode.VALUE_INPUT)
                userInfo.userStateUpdate(user,state.NVAL_INPUT)
            content = reply.valueInputMsg if userAddr else reply.userAddrLack
            line_bot_api.push_message(uid,TextSendMessage(content))
            return

        elif re.match("輸入M值",msg):
            userAddr = userInfo.getUserAddr(user)
            if userAddr:
                userInfo.userModeUpdate(user,mode.VALUE_INPUT)
                userInfo.userStateUpdate(user,state.MVAL_INPUT)
            content = reply.valueInputMsg if userAddr else reply.userAddrLack
            line_bot_api.push_message(uid,TextSendMessage(content))
            return

        elif re.match("查詢買家人數",msg):
            userAddr = userInfo.getUserAddr(user)
            if not userAddr:
                content = reply.userAddrLack
                line_bot_api.push_message(uid,TextSendMessage(content))
            else:
                num = buyerList.getBuyerNum(userAddr)
                content = handle.buyerNum(num)
                line_bot_api.push_message(uid,TextSendMessage(content))
            return
            
        elif re.match("查詢販售總數",msg):
            userAddr = userInfo.getUserAddr(user)
            if not userAddr:
                content = reply.userAddrLack
                line_bot_api.push_message(uid,TextSendMessage(content))
            else:
                num = buyerList.getSellNum(userAddr)
                content = handle.sellNum(num)
                line_bot_api.push_message(uid,TextSendMessage(content))
            return

        ### 功能導覽
        else:
            content = reply.lostMsg
            line_bot_api.push_message(uid,TextSendMessage(content))
            return

    ### 基本資訊設定
    elif userMode == mode.ADDR_INPUT:
        userInfo.userModeUpdate(user,mode.INIT_MODE)
        userInfo.userAddrUpdate(user,msg)
        content = reply.InputCompleteMsg
        line_bot_api.push_message(uid,TextSendMessage(content))
        return 
    
    elif userMode == mode.GMAIL_INPUT:
        userInfo.userModeUpdate(user,mode.INIT_MODE)
        userInfo.userGmailUpdate(user,msg)
        content = reply.InputCompleteMsg
        line_bot_api.push_message(uid,TextSendMessage(content))
        return
    
    elif userMode == mode.AUTHORLIST_INPUT:
        userInfo.userModeUpdate(user,mode.INIT_MODE)
        userInfo.userAuthorListUpdate(user,msg)
        content = reply.InputCompleteMsg
        line_bot_api.push_message(uid,TextSendMessage(content))
        return

    elif userMode == mode.TOKENLIST_INPUT:
        userInfo.userModeUpdate(user,mode.INIT_MODE)
        userInfo.userTokenListUpdate(user,int(msg))
        content = reply.InputCompleteMsg
        line_bot_api.push_message(uid,TextSendMessage(content))
        return

    ### 買家資訊查詢
    elif userMode == mode.VALUE_INPUT:
        userAddr = userInfo.getUserAddr(user)
        userInfo.userModeUpdate(user,mode.INIT_MODE)
        if userState == state.NVAL_INPUT:
            buyerDict = buyerList.getNBuyer(userAddr,int(msg))
            content = handle.Nbuyer(buyerDict)
            line_bot_api.push_message(uid,TextSendMessage(content))

        elif userState == state.MVAL_INPUT:
            buyerDict = buyerList.getMBuyer(userAddr,int(msg))
            content = handle.Mbuyer(buyerDict)
            line_bot_api.push_message(uid,TextSendMessage(content))
        userInfo.userStateUpdate(user,state.INIT_STATE)
        return

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)