import asyncio
from telegram import start_bot
from client import client

# asyncio.run(start_bot())
client.start()
print(client.get_me().stringify())
