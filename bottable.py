import os
import telebot
from telebot import types

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN is not set")

bot = telebot.TeleBot(TOKEN)



# --- ДАННЫЕ ---
GROUP_NAME = "11-СРС"

schedule_11 = """
📅 *Расписание 11-СРС*

Пн — 12:00 - Організація роботи з кадрами Гончаренко В.В, 14:15 - Англійська мова Максимовська Л.І  
Вт — 8:30 - Безпека Життєдіяльності Косміна І.А, 10:25 - Історія держави і права Гончаренко В.В 
Ср — 10:25 - Історія держави і права Гончаренко В.В, 12:20 - Організація роботи з кадрами Гончаренко В.В
Чт — 10:25 - Українська мова за професійним спрямуванням Жадан Т.І, 12:20 -  Теорія держави і права Глемботцька Л.П
Пт — 8:30 - Безпека Життєдіяльності Косміна І.А, 10:25 - Фізичне виховання Кононенко О.І, 12:20 - Англійська мова Максимовська Л.І
"""

courses_11 = """
📚 *Курсы и ДЗ*

Організація роботи з кадрами Гончаренко В.В:
https://cdo24.hdadk.kharkov.ua/course/view.php?id=1052

Безпека Життєдіяльності Косміна І.А:
https://cdo24.hdadk.kharkov.ua/course/view.php?id=400

Історія держави і права Гончаренко В.В:
https://cdo24.hdadk.kharkov.ua/course/view.php?id=401

Теорія держави і права Глемботцька Л.П:
https://cdo24.hdadk.kharkov.ua/course/view.php?id=405

Українська мова за професійним спрямуванням Жадан Т.І:
https://cdo24.hdadk.kharkov.ua/course/view.php?id=394

Конституційне право України Рудаченко С.І:
https://cdo24.hdadk.kharkov.ua/course/view.php?id=406

Англійська мова Максимовська Л.І:
https://cdo24.hdadk.kharkov.ua/course/view.php?id=398

Фізичне виховання Остренко В.В:
https://cdo24.hdadk.kharkov.ua/course/view.php?id=399

Юридична деонтологія Косміна І.А:
https://cdo24.hdadk.kharkov.ua/course/view.php?id=402
"""

zoom_11 = """
🎥 *Zoom-ссылки*

Організація роботи з кадрами Гончаренко В.В:
https://zoom.us/j/7552365704

Англійська мова Максимовська Л.І:
https://zoom.us/j/87942492835  password: 5NWqwV

Безпека Життєдіяльності Косміна І.А:
https://us05web.zoom.us/j/82961818023?pwd=gqgS9GMPNnPq1ckHGc179V7rYWp6Wb.1

Історія держави і права Гончаренко В.В:
https://us05web.zoom.us/j/7552365704?pwd=RGlrTVU5ZXVuR3JtVHI0d3QyZG5OQT09

Конституційне право України Рудаченко С.І:
us05web.zoom.us/j/82251058886

Теорія держави і права Глемботцька Л.П:
https://us04web.zoom.us/j/78778985041?pwd=GdgV3sdk3DTAhSHhWd7YJWusNfjrts.1

Українська мова за професійним спрямуванням Жадан Т.І:
https://us05web.zoom.us/j/84359153269?pwd=H6GC6sYMG6GFXiKSjapKMLXjduEd19.1#success

Фізичне виховання Остренко В.В:
https://us05web.zoom.us/j/83858422904?pwd=MCvVjxfFahBafT8ZRbeFaFvo1XRNuf.1#success

Юридична деонтологія Косміна І.А:
https://us05web.zoom.us/j/82961818023?pwd=gqgS9GMPNnPq1ckHGc179V7rYWp6Wb.1
"""

# --- СТАРТ ---
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_group = types.KeyboardButton("11-СРС")
    markup.add(btn_group)

    bot.send_message(
        message.chat.id,
        "Привіт 👋\nОбери свою группу:",
        reply_markup=markup
    )

# --- ВЫБОР ГРУППЫ ---
@bot.message_handler(func=lambda message: message.text == "11-СРС")
def group_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        "📅 Расписание",
        "📚 Курсы и ДЗ",
        "🎥 Zoom-ссылки",
        "⬅️ Назад"
    )

    bot.send_message(
        message.chat.id,
        f"Группа *{GROUP_NAME}* выбрана ✅\nВыбери раздел:",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# --- МЕНЮ ---
@bot.message_handler(func=lambda message: message.text == "📅 Расписание")
def schedule(message):
    bot.send_message(message.chat.id, schedule_11, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "📚 Курсы и ДЗ")
def courses(message):
    bot.send_message(message.chat.id, courses_11, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "🎥 Zoom-ссылки")
def zoom(message):
    bot.send_message(message.chat.id, zoom_11, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "⬅️ Назад")
def back(message):
    start(message)

# --- ЗАПУСК ---
bot.infinity_polling()
