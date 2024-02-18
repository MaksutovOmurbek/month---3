from aiogram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram import Updater, CommandHandler, MessageHandler, Filters

#
def start(update, context):
    user = update.message.from_user
    update.message.reply_text(
        f"Привет, {user.first_name}! Добро пожаловать в интернет-магазин ноутбуков.\n"
        "Чтобы посмотреть товары, нажмите кнопку 'Показать товары'.",
        reply_markup=ReplyKeyboardMarkup([['Показать товары']], one_time_keyboard=True)
    )

def show_products(update, context):
    update.message.reply_text("Список доступных товаров:\n"
                              "1. Ноутбук 1\n"
                              "2. Ноутбук 2\n"
                              "3. Ноутбук 3\n"
                              "Чтобы добавить товар в корзину, напишите его номер.")

def add_to_cart(update, context):
    product_number = update.message.text

    update.message.reply_text(f"Товар {product_number} добавлен в корзину.")


def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex('^Показать товары$'), show_products))
    dp.add_handler(MessageHandler(Filters.regex('^\d+$'), add_to_cart))

    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
