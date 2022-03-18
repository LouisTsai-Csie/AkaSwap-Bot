from linebot.models import FlexSendMessage

def authorInfo():
    content = FlexSendMessage(
        {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "追蹤作者資訊",
                    "align": "center"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "最新作品",
                    "text": "查詢最新作品"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "下架作品",
                    "text": "查詢下架作品"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "特定作者資訊",
                    "text": "查詢特定作者"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "我的追蹤列表",
                    "text": "查詢作者追蹤列表"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "新增追蹤作者",
                    "text": "輸入作者地址"
                    }
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "刪除追蹤作者",
                    "text": "輸入作者地址"
                    }
                }
                ]
            }
        }
    )
    return content

    