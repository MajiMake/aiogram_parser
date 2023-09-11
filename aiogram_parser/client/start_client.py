from telethon import TelegramClient, sync
from aiogram_parser.client.configs import load_config

# Вставляем api_id и api_hash
conf = load_config('../.env')
api_id = conf.cl_bot.cl_id
api_hash = conf.cl_bot.cl_hash

client = TelegramClient('phone_sellers', api_id, api_hash)