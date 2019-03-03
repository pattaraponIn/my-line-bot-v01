from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)
 
line_bot_api = LineBotApi('IkA0NfE3wTrE7lxdnwE2DFgyAWpvOtTMTsXlNt96hJSIBtY/CZF/Tyoaa9rb2cCWqEvbWkN2o8mvlqryWqKOkaagtybWV1/KnI13+qhCBuC8o0n3ZYbvF4g254TeJivbFmnIBKl/c+wT7bP+RekmjwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7cae6d4c3810f294802285d6ccd82a77')
 
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
