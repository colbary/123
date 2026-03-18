#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AI Bot - Light Version (No Torch)

import telebot
import requests
import json
import time
import random

# Токен бота
TOKEN = "8733856481:AAHx4XmepOb4htYPIxnD7ShxG3EooxuiyU4"
bot = telebot.TeleBot(TOKEN)

# Бесплатные API для AI (без торча)
class LightAI:
    def __init__(self):
        self.api_list = [
            self.gpt4free,
            self.koboldai,
            self.tgpt
        ]
    
    def gpt4free(self, prompt):
        """Использует публичные API"""
        try:
            # Быстрый публичный API
            response = requests.post(
                "https://ai.fakeopen.com/v1/chat/completions",
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                },
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
        except:
            return None
    
    def koboldai(self, prompt):
        """KoboldAI публичные инстансы"""
        instances = [
            "https://koboldai.org/api/v1/generate",
            "https://lite.koboldai.net/api/v1/generate"
        ]
        for instance in instances:
            try:
                response = requests.post(
                    instance,
                    json={
                        "prompt": prompt,
                        "max_length": 500,
                        "temperature": 0.7
                    },
                    timeout=20
                )
                if response.status_code == 200:
                    return response.json()['results'][0]['text']
            except:
                continue
        return None
    
    def tgpt(self, prompt):
        """TGPT - простой AI"""
        try:
            response = requests.get(
                f"https://tgpt.theterminal.tech/chat?prompt={requests.utils.quote(prompt)}",
                timeout=15
            )
            if response.status_code == 200:
                return response.text
        except:
            return None
    
    def generate(self, prompt):
        """Пробуем все API по очереди"""
        for api_func in self.api_list:
            result = api_func(prompt)
            if result:
                return result
        return "❌ Не удалось получить ответ. Попробуй позже."

# Создаем экземпляр AI
ai = LightAI()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 
        "🤖 **Light AI Bot**\n\n"
        "Без торча, без тяжелых моделей!\n"
        "Просто пиши вопрос - получишь ответ\n"
        "Используются публичные API"
    )

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,
        "📌 **Команды:**\n"
        "/start - начало работы\n"
        "/help - помощь\n"
        "/status - статус API\n\n"
        "Просто отправь любой текст - бот ответит!"
    )

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "✅ Бот работает, API проверяются...")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Отправляем "печатает..."
        bot.send_chat_action(message.chat.id, 'typing')
        
        # Генерируем ответ
        response = ai.generate(message.text)
        
        # Отправляем ответ
        bot.reply_to(message, response)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {str(e)}")

if __name__ == "__main__":
    print("🚀 Light AI Bot запущен (без torch)!")
    print("Используются публичные API")
    bot.infinity_polling()
