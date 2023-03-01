from linebot import LineBotApi
import configparser




config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))


message_content = line_bot_api.get_message_content('17331519157310')
with open('/Users/joytsai/PycharmProjects/myproject1/[IM 1011] Python Programming Foundation/app/test', 'wb') as fd:
    for chunk in message_content.iter_content():
        fd.write(chunk)
