from googletrans import  Translator

def tarjima_qil(matn, src='Uzbek', dest="English"):
    translator = Translator()

    tarjima = translator.translate(matn, src=src, dest=dest)

    return tarjima.text


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from main import tarjima_qil

TOKEN=''

def start(update, context):
    update.message.reply_text(text="Assalomu alaykum \nBu tarjimon bot 🇻🇬🇧🇳🇧🇬")

def main(update, context):
    msg = update.message.text

    txt = msg.split(" ")[0]

    msg = msg.replace(txt, "")

    if txt == "en-uz":
        tarjima = tarjima_qil(msg, src="English", dest="Uzbek")

        update.message.reply_text(text=tarjima)
    elif txt == "uz-en":
        tarjima = tarjima_qil(msg, src="Uzbek", dest="English")

        update.message.reply_text(text=tarjima)
    elif txt == "uz-ru":
        tarjima = tarjima_qil(msg, src="Uzbek", dest="Russian")

        update.message.reply_text(text=tarjima)

    elif txt == "ru-uz":
        tarjima = tarjima_qil(msg, src="Russian", dest="Uzbek")

        update.message.reply_text(text=tarjima)
    else:
        tarjima = tarjima_qil(msg, src="Uzbek", dest="English")

        update.message.reply_text(text=tarjima)


updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, main))

updater.start_polling()
updater.idle()
