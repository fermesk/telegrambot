
import telebot
import requests

#Bot tocken
BOT_TOKEN = "7032008610:AAE__4UsOvNNuyha_10n3V4jy5iZ1CSO4Tc"
bot = telebot.TeleBot(BOT_TOKEN)

def get_crypto_price(crypto):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    price = data.get(crypto, {}).get('usd', 'Unavailable')
    print(price,100*"-")
    return price

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hey I'm pesto rico bot i tell you about the latest cryptocurrency prcices in USD! for example type: /price bitcoin")

@bot.message_handler(commands=['price'])
def price(message):
    try:
        crypto = message.text.split()[1]  # Extract the cryptocurrency ID from the message
        price = get_crypto_price(crypto)
        bot.reply_to(message, f"The current price of {crypto} is: ${price} USD")
    except IndexError:
        bot.reply_to(message, "Please specify a cryptocurrency ID. For example, /price bitcoin")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.polling()







