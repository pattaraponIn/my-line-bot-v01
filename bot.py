from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)
 
line_bot_api = LineBotApi('nMgPnrhW5yQ9V71vrj1ogdtUzjyltjfNQdVSceFeVj+ENPvKDz2NTh2MIUxC3ZzRoTfOMEdsCXC+V7XY8noc6xkvLq9gb2nLtK6JPVEZfpUxc8zaONbbNTcISYeu3zAT7eItChzE/amuV8IHjm/QdAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('79ebe82f6d81d30da6bfac188eaaa83b')
 
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
