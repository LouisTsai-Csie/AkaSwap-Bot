from linebot.models import FlexSendMessage
def buyerInfo():
    content = FlexSendMessage(
        {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "買家資訊查詢",
                    "align": "center"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "最大買家查詢",
                    "text": "查詢最大買家"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "前M大買家",
                    "text": "請輸入M值"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "作品超過N件買家",
                    "text": "輸入N值"
                    }
                }
                ]
            }
        }
    )
    return content