import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/d8471a7e6306f5447ee51.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm GiyuBot.** \n\n"
  TEXT += "**I'm Working Properly** \n\n"
  TEXT += f"**My Master : [Eren](https://t.me/Euthanizer)** \n\n"
  TEXT += "**Thanks For Adding Me Here**"
  BUTTON = [[Button.url("Help", "https://t.me/Giyu_Superbot?start=help"), Button.url("Support", "https://t.me/GiyuSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
