from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

TELEGRAM_BOT_TOKEN = '7804893878:AAGWRLFNDt21PiQtkAhapvUmd-2YQZjYHJw'
LOG_GROUP_ID = -1002035333875

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    username = user.username if user.username else "No username"
    user_id = user.id
    name = user.full_name
    is_dm = "Yes" if update.effective_chat.type == "private" else "No"
    
    log_message = f"User started the bot:\nUsername: {username}\nUser ID: {user_id}\nName: {name}\nIn DM: {is_dm}"
    
    context.bot.send_message(chat_id=LOG_GROUP_ID, text=log_message)

    image_url = "https://i.ibb.co/kqmt7bk/file-101.jpg"
    
    caption = """
Welcome to the Tanks Arena Bot! Click the button below to play:

- Enjoy thrilling multiplayer tank battles.
- Compete with players from all around the world.
"""

    keyboard = [
        [InlineKeyboardButton("Play Tanks Arena", url="https://www.crazygames.com/game/tanks-arena-io-craft-combat")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    context.bot.send_photo(
        chat_id=update.effective_chat.id, 
        photo=image_url, 
        caption=caption, 
        reply_markup=reply_markup
    )

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    
    updater.idle()

if __name__ == '__main__':
    main()
