from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextSendMessage, ImageSendMessage
import datetime
import configparser
import json


app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# user_data = {}


# 接收 LINE 的資訊
@app.route("/callback", methods=(['POST'] or ['GET']))
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
            reply_array = [TextSendMessage(text=f"請問您{json_data['events'][0]['message']['keywords']}嗎？"),
                           TextSendMessage(text=f"請輸入help查看指令")]
            line_bot_api.reply_message(
                event.reply_token,
                reply_array)
        elif json_data['events'][0]['message']['type'] == 'text':
            input_message = event.message.text
            if input_message == '早安':
                reply_array = [ImageSendMessage(original_content_url='https://media.zenfs.com/zh-TW/pc3mag.com/e6487042515f97995eb5a6915799c96e',
                                                preview_image_url='https://media.zenfs.com/zh-TW/pc3mag.com/e6487042515f97995eb5a6915799c96e'),
                               TextSendMessage(text=f"早安你好哈囉")]
                line_bot_api.reply_message(
                    event.reply_token,
                    reply_array)
            elif input_message == '午安':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"午安你好哈囉")
                )
            elif input_message == '晚安':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"晚安你好哈囉")
                )
            elif input_message == '我愛你':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"我是機器人，會愛的話就太可怕了")
                )
            elif input_message == '我不行了':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"沒關係，一起加油！你最棒！")
                )
            elif input_message == '完成':
                reply_array = [ImageSendMessage(original_content_url='https://www.junyu3133525.com/archive/image/product1/images/cm0104_thumb_630_499.jpg',
                                                preview_image_url='https://www.junyu3133525.com/archive/image/product1/images/cm0104_thumb_630_499.jpg'),
                               TextSendMessage(text=f"完成了你好棒，雖然這個功能施工中，但還是可以看jojo！"),
                               TextSendMessage(text=f"https://youtu.be/fi9q5jTyZq4")]
                line_bot_api.reply_message(
                    event.reply_token,
                    reply_array)
            elif input_message == 'help':
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"1. 若您欲計算最後時刻：\n"
                                         f"請輸入任務名稱、死線日期、死線時間、若100%努力預期花費時間\n"
                                         f"Please exactly follow the format.\n"
                                         f"\n"
                                         f"格式：\n"
                                         f"任務名稱,YYYY-MM-DD,hh:mm:ss,hh:mm:ss\n"
                                         f"\n"
                                         f"範例如：\n"
                                         f"期末報告,2022-11-11,00:00:00,11:11:00\n"
                                         f"\n"
                                         f"2. 若您已完成工作，欲計算效率：\n"
                                         f"請輸入：完成\n"
                                         f"**此功能施工中**")
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
                                    reply_array.append(TextSendMessage(text=f"{task_name}已經過死線了"))
                                else:
                                    reply_array.append(TextSendMessage(text=f"您需要馬上開始以"
                                                                            f"{round((datetime.timedelta(hours=expect_cost_time_list[0],minutes=expect_cost_time_list[1],seconds=expect_cost_time_list[2])/(dead_line - current_time)*100), 2)}%"
                                                                            f"開始努力"))
                            else:
                                reply_array.append(TextSendMessage(text=f"您需要馬上開始以"
                                        f"{round((datetime.timedelta(hours=expect_cost_time_list[0],minutes=expect_cost_time_list[1],seconds=expect_cost_time_list[2])/(dead_line - current_time)*100), 2)}%"
                                        f"開始努力"))
                                reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_200}以200%努力開始進行{task_name}"))
                        else:
                            reply_array.append(TextSendMessage(text=f"您需要馬上開始以"
                                        f"{round((datetime.timedelta(hours=expect_cost_time_list[0],minutes=expect_cost_time_list[1],seconds=expect_cost_time_list[2])/(dead_line - current_time)*100), 2)}%"
                                        f"開始努力"))
                            reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_150}以150%努力開始進行{task_name}"))
                            reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_200}以200%努力開始進行{task_name}"))
                    else:
                        reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_100}以100%努力開始進行{task_name}"))
                        reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_150}以150%努力開始進行{task_name}"))
                        reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_200}以200%努力開始進行{task_name}"))
                else:
                    reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_50}以50%努力開始進行{task_name}"))
                    reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_100}以100%努力開始進行{task_name}"))
                    reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_150}以150%努力開始進行{task_name}"))
                    reply_array.append(TextSendMessage(text=f"您最晚需要於{last_minute_to_start_200}以200%努力開始進行{task_name}"))

                line_bot_api.reply_message(
                    event.reply_token,
                    reply_array)
        else:
            reply_array = [TextSendMessage(text=f"很抱歉，我看不懂{json_data['events'][0]['message']['type']}，我只看得懂文字訊息和貼圖"),
                           TextSendMessage(text=f"請輸入help查看指令")]
            line_bot_api.reply_message(
                event.reply_token,
                reply_array)
    except KeyError:
        reply_array = [TextSendMessage(text=f"很抱歉，我讀不懂您的貼圖"),
                       TextSendMessage(text=f"請輸入help查看指令")]
        line_bot_api.reply_message(
            event.reply_token,
            reply_array)
    except AttributeError:
        pass
    except NameError:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"請輸入help查看指令"))
    except ValueError:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"請輸入help查看指令"))
    except TypeError:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"請輸入help查看指令"))
    except OverflowError:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"您輸入的數值太大，算不動ㄌ"))
    except IndexError:
        reply_array = [TextSendMessage(text=f"聽君一席話，如聽一席話。"),
                       TextSendMessage(text=f"請輸入help查看指令")]
        line_bot_api.reply_message(
            event.reply_token,
            reply_array)



### 可以用global來存變數，這樣就不會每次不見。
### 或用另一個變數，存條件
if __name__ == "__main__":
    app.run(port=5002)
