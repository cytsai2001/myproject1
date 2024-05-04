from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
import datetime
import configparser
import json
import random


app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 計算死線
@handler.add(MessageEvent)
def deadline(event):
    try:
        body = request.get_data(as_text=True)
        json_data = json.loads(body)
        print(json_data)
        if json_data['events'][0]['message']['type'] == 'sticker':
            print('sticker')
            reply_array = [TextSendMessage(text=f"Are you {json_data['events'][0]['message']['keywords']}？"),
                           TextSendMessage(text=f"Please type in : help and view the instructions.")]
            line_bot_api.reply_message(
                event.reply_token,
                reply_array)
        elif json_data['events'][0]['message']['type'] == 'text':
            input_message = event.message.text
            if input_message == 'Good morning':
                reply_array = [ImageSendMessage(original_content_url='https://media.zenfs.com/zh-TW/pc3mag.com/e6487042515f97995eb5a6915799c96e',
                                                preview_image_url='https://media.zenfs.com/zh-TW/pc3mag.com/e6487042515f97995eb5a6915799c96e'),
                               TextSendMessage(text=f"Have a great day!")]
                line_bot_api.reply_message(
                    event.reply_token,
                    reply_array)
            elif input_message == 'Good afternoon':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"Have a delicious lunch!")
                )
            elif input_message == 'Good night':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"Have a good dream!")
                )
            elif input_message == 'I love you':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"I am a bot. I don't know the feeling of love.(๑•́ ₃ •̀๑)")
                )
            elif input_message == "I can't hold it anymore.":
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"That's OK! You have already tried your best!")
                )
            elif input_message == 'Finished':
                reply_array = [ImageSendMessage(original_content_url='https://previews.123rf.com/images/vanatchanan/vanatchanan1510/vanatchanan151000047/45878057-under-construction-background-vector-illustration.jpg',
                                                preview_image_url='https://previews.123rf.com/images/vanatchanan/vanatchanan1510/vanatchanan151000047/45878057-under-construction-background-vector-illustration.jpg'),
                               TextSendMessage(text=f"Amazing! Although this function is under construction, you can still take a rest and watch some anime."),
                               TextSendMessage(text=f"https://youtu.be/fi9q5jTyZq4")]
                line_bot_api.reply_message(
                    event.reply_token,
                    reply_array)
            elif input_message == 'help':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"1. If you want to calculate the last time to start your work:\n"
                                         f"Please type in :name of task,date of deadline,time of deadline,expected time for working in 100% effort.\n"
                                         f"Please exactly follow the format. \n"
                                         f"format:\n"
                                         f"name of task,YYYY-MM-DD,hh:mm:ss,hh:mm:ss\n"
                                         f":\n"
                                         f"final project,2022-11-11,00:00:00,11:11:00\n\n"
                                         f"2. The task is finished, and you want to calculate the efficiency:\n"
                                         f"Please type in : Finished\n"
                                         f"**This function is under construction.**")
                )
            else:
                text_list = [str(i) for i in input_message.split(',')]
                task_name = text_list[0]
                dead_line = datetime.datetime.fromisoformat(str(text_list[1] + 'T' + text_list[2]))
                expect_cost_time_list = [int(i) for i in text_list[3].split(':')]

                last_minute_to_start_100 = dead_line - datetime.timedelta(hours=expect_cost_time_list[0],
                                                                          minutes=expect_cost_time_list[1],
                                                                          seconds=expect_cost_time_list[2])
                last_minute_to_start_200 = dead_line - 0.5 * datetime.timedelta(hours=expect_cost_time_list[0],
                                                                                minutes=expect_cost_time_list[1],
                                                                                seconds=expect_cost_time_list[2])
                last_minute_to_start_50 = dead_line - 2 * datetime.timedelta(hours=expect_cost_time_list[0],
                                                                             minutes=expect_cost_time_list[1],
                                                                             seconds=expect_cost_time_list[2])
                last_minute_to_start_150 = dead_line - (100/150) * datetime.timedelta(hours=expect_cost_time_list[0],
                                                                                      minutes=expect_cost_time_list[1],
                                                                                      seconds=expect_cost_time_list[2])
                # 已經超過時間
                current_time = datetime.datetime.now() + datetime.timedelta(hours=8)  # in replit, the timezone is GMT+0
                reply_array = []
                if current_time > last_minute_to_start_50:
                    if current_time > last_minute_to_start_100:
                        if current_time > last_minute_to_start_150:
                            if current_time > last_minute_to_start_200:
                                if current_time > dead_line:
                                    reply_array.append(TextSendMessage(text=f"{task_name} was expired."))
                                else:
                                    reply_array.append(TextSendMessage(text=f"You have to start right now to do {task_name} in "
                                                                            f"{round((datetime.timedelta(hours=expect_cost_time_list[0],minutes=expect_cost_time_list[1],seconds=expect_cost_time_list[2])/(dead_line - current_time)*100), 2)}%"
                                                                            f"effort"))
                            else:
                                reply_array.append(TextSendMessage(text=f"You have to start right now to do {task_name} in "
                                        f"{round((datetime.timedelta(hours=expect_cost_time_list[0],minutes=expect_cost_time_list[1],seconds=expect_cost_time_list[2])/(dead_line - current_time)*100), 2)}%"
                                        f"effort"))
                                reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 200% effort at{last_minute_to_start_200}"))
                        else:
                            reply_array.append(TextSendMessage(text=f"You have to start right now to do {task_name} in "
                                        f"{round((datetime.timedelta(hours=expect_cost_time_list[0],minutes=expect_cost_time_list[1],seconds=expect_cost_time_list[2])/(dead_line - current_time)*100), 2)}%"
                                        f"effort"))
                            reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 150% effort at{last_minute_to_start_150}"))
                            reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 200% effort at{last_minute_to_start_200}"))
                    else:
                        reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 100% effort at{last_minute_to_start_100}"))
                        reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 150% effort at{last_minute_to_start_150}"))
                        reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 200% effort at{last_minute_to_start_200}"))
                else:
                    reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 50% effort at{last_minute_to_start_50}"))
                    reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 100% effort at{last_minute_to_start_100}"))
                    reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 150% effort at{last_minute_to_start_150}"))
                    reply_array.append(TextSendMessage(text=f"You have to do {task_name} in 200% effort at{last_minute_to_start_200}"))

                line_bot_api.reply_message(
                    event.reply_token,
                    reply_array)
        else:
            reply_array = [TextSendMessage(text=f"Sorry. I can't read {json_data['events'][0]['message']['type']}, and you can try stickers or text messages."),
                           TextSendMessage(text=f"Please type in : help and view the instructions.")]
            line_bot_api.reply_message(
                event.reply_token,
                reply_array)
    except KeyError:
        reply_array = [TextSendMessage(text=f"Sorry. I can't read your stickers.(´;ω;`)"),
                       TextSendMessage(text=f"Please type in : help and view the instructions.")]
        line_bot_api.reply_message(
            event.reply_token,
            reply_array)
    except AttributeError:
        pass
    except NameError:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"Please type in : help and view the instructions."))
    except ValueError:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"Please type in : help and view the instructions."))
    except TypeError:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"Please type in : help and view the instructions."))
    except OverflowError:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"I cannot afford such a large amount of calculation."))
    except IndexError:
        reply_array = [TextSendMessage(text=f"Listening to your words is like listening what you said."),
                       TextSendMessage(text=f"Please type in : help and view the instructions.")]
        line_bot_api.reply_message(
            event.reply_token,
            reply_array)


if __name__ == "__main__":
    app.run(port=5002)
