from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext

TELEGRAM_BOT_TOKEN = "7804893878:AAGWRLFNDt21PiQtkAhapvUmd-2YQZjYHJw"

def start(update: Update, context: CallbackContext) -> None:
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
    # Create the Updater and pass it your bot's token
    updater = Updater(TELEGRAM_BOT_TOKEN)
    
    dispatcher = updater.dispatcher
    
    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
