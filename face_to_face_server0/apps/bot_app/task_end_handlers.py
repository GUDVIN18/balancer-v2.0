from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from apps.bot_app.models import *
from apps.stickers.models import Generate_Stickers, StikerPackConfig, Stiker_target_photo, Stiker_output_photo
from apps.bot_app.models import TelegramBotConfig, BotUser, GenerationProcess, Images
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
from django.http import HttpResponse
import requests
import json


def get_bot_token():
    config = TelegramBotConfig.objects.first()
    if config:
        return config.bot_token
    raise ValueError("Bot token not found in database")


class Task_Handler():
    def __init__(self) -> None:
        # self.bot = telebot.TeleBot(get_bot_token())
        pass


    def task_end_alert(self, task):
        print('Отправка пользователю')
        ip_port = '62.68.146.176:8585' #Сервер Алексея


        url = f"http://{ip_port}/task_complete_alert/"
        data = {
            "id": task.id,
            "task_status": task.process_status
        }
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'}) 
        print('--------- task_end_alert', response)
