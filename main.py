import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("7632234815:AAHyD40trAo8tOdVaFoHHNH2a_f64jHXRgw")
CREATOR_CHAT_ID = int(os.getenv("5558426289"))

async def forward_to_creator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if update.message:
        if update.message.text:
            await context.bot.send_message(chat_id=CREATOR_CHAT_ID,
                                           text=f"📩 Сообщение от @{user.username or user.id}:
{update.message.text}")
        elif update.message.voice:
            await context.bot.send_voice(chat_id=CREATOR_CHAT_ID,
                                         voice=update.message.voice.file_id,
                                         caption=f"🎤 Голосовое от @{user.username or user.id}")
        elif update.message.photo:
            photo = update.message.photo[-1]
            await context.bot.send_photo(chat_id=CREATOR_CHAT_ID,
                                         photo=photo.file_id,
                                         caption=f"📸 Фото от @{user.username or user.id}")
        elif update.message.document:
            await context.bot.send_document(chat_id=CREATOR_CHAT_ID,
                                            document=update.message.document.file_id,
                                            caption=f"📎 Файл от @{user.username or user.id}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_to_creator))
    app.run_polling()
