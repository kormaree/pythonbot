import os
from telegram import Update, BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Добро пожаловать, {0}!\nЯ - {1}, бот созданный, чтобы рассылать своим ученикам задания для подготовки к экзаменам. Пока нахожусь в разработке(".format(update.effective_user.username, context.bot.first_name), parse_mode='html')

async def sendpicture(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    photo_path = "https://avatars.mds.yandex.net/i?id=679720f2a94327342bb6a0e160ce7bb8_l-8497208-images-thumbs&n=13"
    await context.bot.send_photo(chat_id=chat_id, photo=photo_path)


# Функция для регистрации команд в BotFather
async def post_init(application: Application) -> None:
    bot_commands = [
        BotCommand("start", "Начало работы с ботом"),
        BotCommand("sendcat", "Прислать котика"),
    ]
    await application.bot.set_my_commands(bot_commands)

def main() -> None:  
    # создаем приложение 
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).post_init(post_init).build()

    # добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    
    application.add_handler(CommandHandler("sendcat", sendpicture))

    # Запускаем до нажатия Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()