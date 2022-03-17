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

### Import 外部檔案
import config
import state
from mongoDB import mongoDB as db

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
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    user_name = profile.display_name #使用者名稱
    uid = profile.user_id # 發訊者ID

    #檢查用戶是否存在
    user = db.getUser(uid)
    userMode = db.userInfo.getUserMode(user)
    userState = db.userInfo.getUserState(user)

    #=============================
    if userMode == state.INIT_STATE:
        if re.match("輸入地址",msg):
            return
        if re.match("輸入信箱",msg):
            return
        if re.match("作者追蹤",msg):
            return
        if re.match("買家資訊",msg):
            return
        if re.match("作品追蹤"):
            return
    
    
    















import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)