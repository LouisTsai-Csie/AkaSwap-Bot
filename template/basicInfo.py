from linebot.models import FlexSendMessage
def basicInfo():
    content = FlexSendMessage(
        {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "基本資訊設定",
                "align": "center",
                "style": "normal"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "地址輸入",
                "text": "輸入地址"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "text": "輸入信箱",
                "label": "信箱輸入"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "追蹤作者輸入",
                "text": "輸入作者地址"
                }
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "追蹤作品輸入",
                "text": "輸入作品ID"
                }
            }
            ]
        }
        }
    )
    return content

def userInfo(*arg):
    
    content = FlexSendMessage(
        {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "基本資訊",
                    "contents": [
                    {
                        "type": "span",
                        "text": "基本資訊"
                    }
                    ],
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "地址：",
                    "contents": [
                    {
                        "type": "span",
                        "text": "地址："
                    }
                    ]
                },
                {
                    "type": "text",
                    "text": "hello, world",
                    "contents": [
                    {
                        "type": "span",
                        "text": "信箱："
                    }
                    ]
                },
                {
                    "type": "text",
                    "text": "hello, world",
                    "contents": [
                    {
                        "type": "span",
                        "text": "追蹤作者列表："
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "-"
                    }
                    ]
                },
                {
                    "type": "text",
                    "text": "追蹤作品列表",
                    "contents": [
                    {
                        "type": "span",
                        "text": "追蹤作品列表"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "-"
                    }
                    ]
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": []
            }
        }
    )
    return content
