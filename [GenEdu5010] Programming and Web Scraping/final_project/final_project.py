import discord
import datetime
from zoneinfo import zoneinfo

# (3 min code, motivation, 4 min demo)
# format like "期末報告,2022-11-11,00:00:00,11:11:00"
class Event:
    def __init__(self, input_formatted_message: str):
        self.input_list = input_formatted_message.split(',')
        self.task_name = self.input_list[0]
        self.deadline = datetime.datetime.fromisoformat(str(self.input_list[1] + 'T' + self.input_list[2]))
        self.expect_cost_time_list = [int(i) for i in self.input_list[3].split(':')]
        self.expect_cost_time = datetime.timedelta(hours=self.expect_cost_time_list[0],
                                                   minutes=self.expect_cost_time_list[1],
                                                   seconds=self.expect_cost_time_list[2])

    def calculate_last_minute(self):
        last_minute_to_start_50 = self.deadline - 2 * self.expect_cost_time
        last_minute_to_start_150 = self.deadline - (100/150) * self.expect_cost_time
        last_minute_to_start_100 = self.deadline - self.expect_cost_time
        last_minute_to_start_200 = self.deadline - 0.5 * self.expect_cost_time
        return [last_minute_to_start_50, last_minute_to_start_100, last_minute_to_start_150, last_minute_to_start_200]

    def get_last_minute_response(self):
        current_time = datetime.datetime.now() + datetime.timedelta(hours=8)
        reply_array = []
        if current_time > self.calculate_last_minute()[0]:
            if current_time > self.calculate_last_minute()[1]:
                if current_time > self.calculate_last_minute()[2]:
                    if current_time > self.calculate_last_minute()[3]:
                        if current_time > self.deadline:
                            reply_array.append(f"{self.task_name}已經過死線了")
                        else:
                            reply_array.append(f"您需要馬上開始以"
                                               f"{round(self.expect_cost_time/(self.deadline - current_time), 4)*100}%"
                                               f"開始努力")
                    else:
                        reply_array.append(f"您需要馬上開始以"
                                           f"{round(self.expect_cost_time/(self.deadline - current_time), 4)*100}%"
                                           f"開始努力")
                        reply_array.append(f"您最晚需要於{self.calculate_last_minute()[3]}以200%努力開始進行{self.task_name}")
                else:
                    reply_array.append(f"您需要馬上開始以"
                                       f"{round(self.expect_cost_time/(self.deadline - current_time), 4)*100}%"
                                       f"開始努力")
                    reply_array.append(f"您最晚需要於{self.calculate_last_minute()[2]}以150%努力開始進行{self.task_name}")
                    reply_array.append(f"您最晚需要於{self.calculate_last_minute()[3]}以200%努力開始進行{self.task_name}")
            else:
                reply_array.append(f"您最晚需要於{self.calculate_last_minute()[1]}以100%努力開始進行{self.task_name}")
                reply_array.append(f"您最晚需要於{self.calculate_last_minute()[2]}以150%努力開始進行{self.task_name}")
                reply_array.append(f"您最晚需要於{self.calculate_last_minute()[3]}以200%努力開始進行{self.task_name}")
        else:
            reply_array.append(f"您最晚需要於{self.calculate_last_minute()[0]}以50%努力開始進行{self.task_name}")
            reply_array.append(f"您最晚需要於{self.calculate_last_minute()[1]}以100%努力開始進行{self.task_name}")
            reply_array.append(f"您最晚需要於{self.calculate_last_minute()[2]}以150%努力開始進行{self.task_name}")
            reply_array.append(f"您最晚需要於{self.calculate_last_minute()[3]}以200%努力開始進行{self.task_name}")

        return reply_array

    def remind(self):
        reply_array = self.get_last_minute_response()
        return True, reply_array


events = []

# Discord bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$in"):
        event = Event(message.content[4:])
        events.append(event)
        events.sort(key=lambda x: x.deadline)
        response_array = [f"I have recorded the deadline of {event.task_name}."] + event.get_last_minute_response()
        for i in response_array:
            await message.channel.send(i)
        if response_array[1] == f"{event.task_name}已經過死線了":
            await message.channel.send(f'Forget {events.pop(-1).task_name}.')

    elif message.content == "$help":
        response = f"若您欲計算最後時刻：\n" \
                   f"請輸入 $in任務名稱、死線日期、死線時間、若100%努力預期花費時間\n" \
                   f"Please exactly follow the format.\n" \
                   f"\n" \
                   f"格式：\n" \
                   f"$in 任務名稱,YYYY-MM-DD,hh:mm:ss,hh:mm:ss\n" \
                   f"\n" \
                   f"範例如：\n" \
                   f"$in 期末報告,2022-11-11,00:00:00,11:11:00\n"
        await message.channel.send(response)

    elif message.content == "$all":
        if events:
            response_array = ['All tasks recorded:'] + [e.task_name for e in events]
            for i in response_array:
                await message.channel.send(i)
        else:
            await message.channel.send('No tasks recorded.')
    
    elif message.content.startswith("$out"):
        count = 0
        for i, e in enumerate(events):
            if e.task_name == message.content[5:]:
                complete_event = events.pop(i)
                response = f"Congratulation! You complete {complete_event.task_name}."
                count += 1
                await message.channel.send(response)

        if count == 0:
            response = f"Oops! I hadn't record {message.content[5:]} yet."
            await message.channel.send(response)

    else:
        response_array = ['Please type $help for more info.']
        for i in events:
            if i.remind()[0]:
                response_array += i.remind()[1]
        for i in response_array:
            await message.channel.send(i)
try:
    client.run("MTA1Mzk1NDg5NzExODIzNjcxMw.GgDNO7.zdTYwXu9xEZbYzI2sTi4Ip7-3Rs7e4024qg564")
except discord.errors.HTTPException:
    print("\nblocked by discord\n")


