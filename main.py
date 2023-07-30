import random
import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Variables 
TOKEN: Final = os.environ.get("TELEGRAM_API_KEY")
BOT_USERNAME: Final = os.environ.get("TELEGRAM_BOT_USERNAME")
TIKTOK_RESPONSES = ["https://i.imgur.com/lzWLI6A.jpg", "https://i.imgur.com/3Ytx3vy.jpeg"]
SQUADOS = ["Poop is one of life's greatest gifts.", "J'onn is getting excited."]

#### BUILD FUNCTIONS ####

#Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi, I'm Bobby Hill.")


# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'purse' in processed:
        return "That's my purse! I don't know you!"
    if 'tiktok' in processed:
        choice: int = random.randint(0,1)
        return TIKTOK_RESPONSES[choice]
    if 'pizza' in processed:
        return "I was getting ready, but I worked up an appetite looking for dress pants, so I ordered a pizza, and that ate up a chunk of time."
    if 'propane' in processed:
        return "I sell propane, and propane accessories."
    if 'middletown' in processed:
        return "To tell you the truth, Dad, that sounds boring. It's okay if you're into boring, but I'm not"
    if 'poop' in processed:
        choice: int = random.randint(0,1)
        return SQUADOS[choice]
    return ""


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    processed: str = text.lower()

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
            new_text: str = processed.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
    else:
        response: str = handle_response(processed)

    print('Bot:', response)
    if response != "":
        await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



##### Main program #####

if __name__ == '__main__':
    print('Starting bot')

    app = Application.builder().token(TOKEN).build()

# Commands
    app.add_handler(CommandHandler('start', start_command))

# Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

# Errors
    app.add_error_handler(error)

print('Polling...')
app.run_polling(poll_interval=3)

