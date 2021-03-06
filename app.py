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
import os

app = Flask(__name__)

#環境変数取得


line_bot_api = LineBotApi('Hh5cxnBD6LVhK2cHCyAUENwspppg+/jyzmb0N2CSbIMmd+nRhN6CsLS9Sk0gfF+VWw1kouEJGSFOylEE8Ped0e8ysn6g2zCCV2t5qamkgyaHtaZz3KKn/ye14UOaNjSpzK7SXzcZ9Nvg2uBCGBeNswdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('262e82b8892c846dadf6c1fc80d00b39')

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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    if text in ['おは']:
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text="おはようございます！"))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
