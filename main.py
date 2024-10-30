import os
from telegram import Update, BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот созданный, чтобы рассылать своим ученикам задания для подготовки к экзаменам. Пока нахожусь в разработке(".format(update.effective_user.username, context.bot.first_name), parse_mode='html')

async def sendpicture(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Команда 1 выполнена.")


# Функция для регистрации команд в BotFather
async def post_init(application: Application) -> None:
    bot_commands = [
        BotCommand("start", "Начало работы с ботом"),
        BotCommand("command1", "Выполнить команду 1"),
    ]
    await application.bot.set_my_commands(bot_commands)

def main() -> None:
    """Запуск бота"""   
    # создаем приложение 
    token = os.getenv("TELEGRAM_BOT_TOKEN")  # Убедитесь, что эта переменная окружения установлена
    application = Application.builder().token(token).post_init(post_init).build()

    # добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    
    application.add_handler(CommandHandler("command1", sendpicture))

    # Запускаем до нажатия Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()