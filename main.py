from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import datetime
import os

BOT_TOKEN = os.getenv("7632234815:AAHyD40trAo8tOdVaFoHHNH2a_f64jHXRgw")
CREATOR_CHAT_ID = int(os.getenv("5558426289"))

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        try:
            user = update.message.from_user
            msg_text = update.message.text or update.message.caption or "<медиа/голосовое/стикер и т.п.>"

            await context.bot.forward_message(
                chat_id=CREATOR_CHAT_ID,
                from_chat_id=update.message.chat_id,
                message_id=update.message.message_id
            )

            await update.message.reply_text("Ваше сообщение передано администратору ✅")

            log_entry = f"[{datetime.datetime.now()}] {user.first_name} ({user.id}): {msg_text}\n"
            with open("log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(log_entry)

            print(log_entry.strip())

        except Exception as e:
            print(f"Ошибка при пересылке: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_message))
    print("Бот запущен...")
    app.run_polling()
