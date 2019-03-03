from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)
 
line_bot_api = LineBotApi('pLt2oeE+PTpMP6drBQIjk4v3LKxXDy8Bt6LcEmBy2cxmKaXRXWSEybUisf7T7ah+oTfOMEdsCXC+V7XY8noc6xkvLq9gb2nLtK6JPVEZfpURIhSGLhIZ5/0gGCZxy/z8UrTL5t+sU8uiRV9jhE5jhgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('56c2566c7ea135d6780d2f624fad1f15')

@app.route("/")
def hello():
    return "Hello ถ้าข้อความนี้แสดง แสดงว่าคุณสามารถติดตั้งส่วนของHeroku สำเร็จ แล้ว"

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
