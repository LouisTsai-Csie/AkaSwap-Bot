from linebot.models import FlexSendMessage
def tokenInfo():
    content = FlexSendMessage(
        {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "追蹤作品資訊",
                    "align": "center"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "text": "查詢作品資訊列表",
                    "label": "特定作品資訊"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "我的追蹤列表",
                    "text": "查詢作品追蹤列表"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "新增追蹤作品",
                    "text": "輸入作品ID"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "刪除追蹤作品",
                    "text": "輸入作品ID"
                    }
                }
                ],
                "action": {
                "type": "message"
                }
            }
        }
    )
    return content