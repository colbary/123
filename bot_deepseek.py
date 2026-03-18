#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AI Bot - Uncensored Edition

import telebot
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import requests
import json
import time
import threading
from queue import Queue

# Токен бота
TOKEN = "8733856481:AAHx4XmepOb4htYPIxnD7ShxG3EooxuiyU4"
bot = telebot.TeleBot(TOKEN)

# Модели без цензуры (выбирай одну):
MODELS = {
    "wizard": "WizardLM/WizardCoder-Python-34B-V1.0",  # Для кода
    "mythomax": "Gryphe/MythoMax-L2-13b",  # Для текста (без цензуры)
    "nous": "NousResearch/Nous-Hermes-2-Yi-34B",  # Умная модель
    "llama2-uncensored": "georgesung/llama2_7b_chat_uncensored"  # Полностью без цензуры
}

# Выбираем модель (можно переключать)
current_model = "mythomax"

class UncensoredAI:
    def __init__(self, model_name):
        print(f"🔄 Загружаю модель {model_name}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            load_in_8bit=True  # Экономия памяти
        )
        print("✅ Модель загружена!")
        
    def generate(self, prompt, max_length=500, temperature=0.7):
        # Форматируем промпт в зависимости от модели
        if "llama2" in current_model:
            formatted_prompt = f"[INST] {prompt} [/INST]"
        elif "mythomax" in current_model:
            formatted_prompt = f"USER: {prompt}\nASSISTANT:"
        else:
            formatted_prompt = prompt
            
        inputs = self.tokenizer(formatted_prompt, return_tensors="pt").to("cuda")
        
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_length,
            temperature=temperature,
            do_sample=True,
            top_p=0.95,
            repetition_penalty=1.1
        )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Очищаем ответ от промпта
        response = response.replace(formatted_prompt, "").strip()
        return response

# Инициализируем AI
ai = UncensoredAI(MODELS[current_model])

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 
        "🤖 **Uncensored AI Bot**\n\n"
        "Просто пиши любой вопрос - без ограничений!\n"
        "Команды:\n"
        "/model - сменить модель\n"
        "/temp N - установить температуру (0.1-2.0)\n"
        "/clear - очистить контекст"
    )

@bot.message_handler(commands=['model'])
def change_model(message):
    models_list = "\n".join([f"{i+1}. {m}" for i, m in enumerate(MODELS.keys())])
    bot.reply_to(message, f"Доступные модели:\n{models_list}\n\nОтправь номер модели:")
    bot.register_next_step_handler(message, set_model)

def set_model(message):
    try:
        idx = int(message.text) - 1
        model_name = list(MODELS.keys())[idx]
        global current_model, ai
        current_model = model_name
        ai = UncensoredAI(MODELS[model_name])
        bot.reply_to(message, f"✅ Модель изменена на {model_name}")
    except:
        bot.reply_to(message, "❌ Неверный номер")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        msg = bot.reply_to(message, "🤔 Думаю...")
        
        # Генерируем ответ
        response = ai.generate(message.text)
        
        # Разбиваем длинные сообщения
        if len(response) > 4000:
            for i in range(0, len(response), 4000):
                bot.send_message(message.chat.id, response[i:i+4000])
        else:
            bot.edit_message_text(response, chat_id=message.chat.id, message_id=msg.message_id)
            
    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {str(e)}")

if __name__ == "__main__":
    print("🚀 AI Bot запущен!")
    bot.infinity_polling()
