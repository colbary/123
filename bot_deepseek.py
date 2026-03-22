cat > bot_deepseek.py << 'EOF'
import telebot

TOKEN = "8733856481:AAHx4XmepOb4htYPIxnD7ShxG3EooxuiyU4"
bot = telebot.TeleBot(TOKEN)

RULES = {
    "smi": "📢 СМИ\n\nСМИ — сбор, обработка и распространение информации.\n\nФункции:\n• Выпуск газет\n• Рекламные эфиры\n• Информирование о госструктурах",
    "gcl": "🎓 ГЦЛ\n\nАвтошкола — выдача лицензий.\n\n• Сдача экзаменов\n• Покупка лицензии\n• Проверка лицензий\n• НЕ проводит техосмотр",
    "gov": "🏛️ ПРАВИТЕЛЬСТВО\n\nВысший исполнительный орган.\n\nФункции:\n• Управление штатом\n• Координация госструктур\n• Принятие нормативных актов",
    "d": """📻 КАНАЛ /d

НАЗНАЧЕНИЕ:
1. Связь с госорганами
2. Координация при ЧС
3. Контроль складов
4. Предупреждение о занятии волны

❌ ЗАПРЕЩЕНО:
• Метагейминг
• OOC-чат
• Смешивание IC/OOC
• Откаты (пиши "Упала рация")
• Оффтоп

✅ ПРИМЕРЫ:
/d [Пра-во] - [ЛСПД] Сотрудник с жетоном 0-7-5 забрал права
/d [СФПД] - [СФа] Требуется доставка боеприпасов

СЛОВАРЬ:
• БП/маты → боеприпасы
• укроп → укроптические средства

ФОРМЫ ОБРАЩЕНИЙ:
[ТСР] [ЛСПД] [СФПД] [ЛВПД] [РКШД] [ФБР] [Пра-во] [ЛСа] [СФа] [СтК] [ЛСМЦ] [ДЖМЦ] [СФМЦ] [ЛВМЦ] [ГЦЛ] [СМИ ЛС] [СМИ СФ] [СМИ ЛВ]""",
    "palatki": """📰 ПРОДАЖА ГАЗЕТ

ПРАВИЛА:
1. Палатку даёт руководство
2. После продаж вернуть
3. Продавать только в своём городе

МЕСТА:
ЛС: ЦБ, ЦР, Вокзал
СФ: АБ, Центр занятости, Вокзал
ЛВ: Казино, Вокзал, Больница
ФК: Станция Форт Карсон

ЗАПРЕЩЕНО: дороги, выходы, крыши, рядом друг с другом""",
    "expel": """🔨 /EXPEL

ПОШАГОВО:
1. /me достал дубинку
2. /me вызвал охрану
3. /do Охрана выводит
4. /expel ID Причина
5. Записать видео

МОЖНО: неадекват, срыв лекций, оружие, торговля, угрозы
НЕЛЬЗЯ: афк, причина "Помеха", мат, просто так""",
    "lekcii": "📚 ЛЕКЦИИ\n\n• Разъяснять основы\n• Доносить устав\n• Побуждать интерес\n• Разумный объём\n• Биндер\n• Интервал 5 сек",
    "opisanie": "👤 ОПИСАНИЕ\n\n1. Только РП\n2. Визуальная информация\n3. Без мата\n4. 7+ ранг — выговор\n\nПример: «Парень среднего роста с зелёными глазами, сбиты костяшки, татуировка дракона.»",
    "reklama": "💰 РЕКЛАМА\n\n• Обговорить сроки\n• Заскринить разговор\n• СМИ может отказать\n\nЦены: 500k - 3M\nШтраф: 2M - 5M",
    "obyazannosti": """⚠️ ОБЯЗАННОСТИ

• Лидер отвечает за состав
• AFK >10 мин → kick
• 6-7 рангам нельзя деморган
• 8-9 рангам нельзя деморган
• 5+ рангам нельзя на мероприятия
• Обращаться на «Вы»
• Быть на рабочем месте

ШТРАФЫ ЛИДЕРАМ:
Прогул: -25 | Нарушение устава: -10..-25""",
    "transport": "🚗 ТРАНСПОРТ\n\nНаземный: Toyota RAV4, NewsVan\nВоздушный: News Maverick",
    "advokaty": """⚖️ АДВОКАТЫ

КАК СТАТЬ:
1. Тест и лицензия в мэрии
2. Должность в правительстве (СБ+)
3. Пропуск от МЮ (3+ ранг)

ПРАВИЛА:
• Адвокат предъявляет паспорт/визитку
• МЮ обыскивает
• Доклад по рации
• Если нет МЮ 5 мин — пройти самому (видео)

ОГРАНИЧЕНИЯ:
• Нельзя на жёлтом/красном уровне
• Можно на зелёном (дороже)

ЗАКРЫТАЯ ТЕРРИТОРИЯ:
МЮ: гараж, допросная, склад, раздевалка, КПЗ
ТСР: вся кроме холла и переговорной"""
}

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "📚 Справочник Arizona RP\n\n/smi — СМИ\n/gcl — ГЦЛ\n/gov — Правительство\n/d — Канал /d\n/palatki — Палатки\n/expel — /expel\n/lekcii — Лекции\n/opisanie — Описание\n/reklama — Реклама\n/obyazannosti — Обязанности\n/transport — Транспорт\n/advokaty — Адвокаты\n\nИли напиши слово для поиска")

@bot.message_handler(commands=['smi']) def smi(m): bot.send_message(m.chat.id, RULES["smi"])
@bot.message_handler(commands=['gcl']) def gcl(m): bot.send_message(m.chat.id, RULES["gcl"])
@bot.message_handler(commands=['gov']) def gov(m): bot.send_message(m.chat.id, RULES["gov"])
@bot.message_handler(commands=['d']) def d(m): bot.send_message(m.chat.id, RULES["d"])
@bot.message_handler(commands=['palatki']) def palatki(m): bot.send_message(m.chat.id, RULES["palatki"])
@bot.message_handler(commands=['expel']) def expel(m): bot.send_message(m.chat.id, RULES["expel"])
@bot.message_handler(commands=['lekcii']) def lekcii(m): bot.send_message(m.chat.id, RULES["lekcii"])
@bot.message_handler(commands=['opisanie']) def opisanie(m): bot.send_message(m.chat.id, RULES["opisanie"])
@bot.message_handler(commands=['reklama']) def reklama(m): bot.send_message(m.chat.id, RULES["reklama"])
@bot.message_handler(commands=['obyazannosti']) def obyazannosti(m): bot.send_message(m.chat.id, RULES["obyazannosti"])
@bot.message_handler(commands=['transport']) def transport(m): bot.send_message(m.chat.id, RULES["transport"])
@bot.message_handler(commands=['advokaty']) def advokaty(m): bot.send_message(m.chat.id, RULES["advokaty"])

@bot.message_handler(func=lambda m: True)
def search(m):
    q = m.text.lower()
    found = [k for k, v in RULES.items() if q in v.lower()]
    if not found:
        bot.reply_to(m, "❌ Ничего не найдено")
    elif len(found) == 1:
        bot.send_message(m.chat.id, RULES[found[0]])
    else:
        names = {"smi":"СМИ","gcl":"ГЦЛ","gov":"Правительство","d":"/d","palatki":"Палатки","expel":"/expel","lekcii":"Лекции","opisanie":"Описание","reklama":"Реклама","obyazannosti":"Обязанности","transport":"Транспорт","advokaty":"Адвокаты"}
        reply = f"🔍 Найдено {len(found)}:\n"
        for k in found[:5]:
            reply += f"• {names[k]} — /{k}\n"
        bot.send_message(m.chat.id, reply)

print("✅ Бот запущен")
bot.infinity_polling()
EOF
