from pyrogram import Client, filters
import time

api_id = сюдаапиайди
api_hash = "сюда апи хеш"

app = Client('my_account', api_id=api_id, api_hash=api_hash)

print('АНТИ СВИНОСОБАКИ V1\nTikTok: strainxx')

repeat_range = int(input('Введіть кількість повторів: '))
speed_range = int(input('Введіть режим швидкості(1 - швидко, 2 - середньо, 3 - повільно): '))
repeat_range += 1

if speed_range == 1:
    speed_range = 0
    
elif speed_range == 2:
    speed_range = 0.2

elif speed_range == 3:
    speed_range = 0.5

else:
    print('Введіть правильну швидкість')

    exit()

@app.on_message(filters.me)

async def echo(client, message):
    
    print('Спам був успішно надісланий')
    for i in range(0, repeat_range):
        await message.reply_text(message.text)
        time.sleep(speed_range)
        

app.run()
