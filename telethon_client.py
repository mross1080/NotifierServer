from telethon import TelegramClient, events, sync
import paho.mqtt.client as mqtt

# This is the Publisher
print("HIII")
mqtt_client = mqtt.Client()
mqtt_client.connect("54.204.183.201", 1883, 60)
mqtt_client.publish("topic/clap", "Hello SID!!!!");
api_id = 1044737

api_hash = '8d611c2f3cfc5ef0caafad1fe86d3fda'

from telethon.sync import TelegramClient, events

with TelegramClient('session1', api_id, api_hash) as client:
    # msgs = client.get_messages('me')
    # print(msgs)
    print("connected and waiting for messages")


    @client.on(events.NewMessage(pattern='.*'))
    async def handler(event):

        print("got message")
        try:
            print("Sending message")
            x = mqtt_client.publish("topic/clap", "Hello SID!!!!");
            print(x)
            print("sent message")
        except Exception:
            print("Exception")
            print(Exception)

        print(event)
        print(event["message"])

        await event.reply('Hey!')


    client.run_until_disconnected()
