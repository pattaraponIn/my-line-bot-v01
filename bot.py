from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)
 
line_bot_api = LineBotApi('FYqOxvyVPxY583IFq8UK0UptDfszGkcC4E27kz9p+NzKCVQum6jMMdtn8KGnVO2MSgH9rSYLgbz84hXitQYR3c1qgDjdT9a8SXjPIPs0TIMohZ31BMuyFmgnKrLyuytCBzIu5YKlD5IqlEsd3rxDggdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c39c9425fe01d62bb8b3f58d568d94c3')
 
@app.route("/")
def hello():
    return "Hello ถ้าข้อความนี้แสดง แสดงว่าคุณสามารถติดตั้งส่วนของHeroku สำเร็จ แล้ว ครั้งที่ 8"

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
    text=event.message.text
    if text=="s1":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("led on"))
    elif text=="s2":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("led off"))
    elif text=="s3":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("โชว์ อุณหภูมิความชื้น"))
    elif text=="s4":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("โชว์ รูปภาพ"))
    elif text=="s5":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("โชว์ โปรแกรม "))
    elif text=="s6":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("โชว์ ต้นไม้ ")) 


if __name__ == "__main__":
    app.run()
