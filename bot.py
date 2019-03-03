from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)
 
line_bot_api = LineBotApi('nDcFl4+w5pD7AwkkSPoXmILhctD/uoP62NFU0lus/Eq8O6e5HNxDWIOZ8K6pL2KSSgH9rSYLgbz84hXitQYR3c1qgDjdT9a8SXjPIPs0TIMWyZpHKidWLf3zZAqEjSDPCx3ayMJXiCRllsoh51MdLgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('851cd192f64d18ef3c9b05ae5eddaf7d')
 
@app.route("/")
def hello():
    return "Hello ถ้าข้อความนี้แสดง แสดงว่าคุณสามารถติดตั้งส่วนของHeroku สำเร็จ แล้ว ครั้งที่ 1"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
