from telebot import TeleBot
from ya_gpt1 import get_yadex_gpt_response
from speech import text_to_speech, speech_to_text


bot = TeleBot('6721478570:AAFbRlZQcsySyjuzbGN7ykLA2m-mol6rfaA')

bot.send_message(481408952, 'run...')


@bot.message_handler(commands=['GPT'])
def gpt(message):
    bot.send_message(message.chat.id, text='Подождите, генерирую ответ...')
    answer = get_yadex_gpt_response(message.text[4:])
    bot.send_message(message.chat.id, text=answer)




@bot.message_handler(commands=['speech'])
def speech(message):
    text = ' '.join(message.text.split(' ')[1:])

    text_to_speech(text)
    with open('text_to_speech.mp3', 'rb') as f:
        bot.send_audio(message.chat.id, f)




@bot.message_handler(content_types=['voice'])
def voice(message):
    file = bot.get_file(message.voice.file_id)
    bytes = bot.download_file(file.file_path)
    with open('voice.ogg', 'wb') as f:
        f.write(bytes)
    text = speech_to_text()
    # bot.send_message(message.chat.id, text=text)
    answer = get_yadex_gpt_response(text)
    bot.send_message(message.chat.id, text=answer)




if __name__ == '__main__':
    bot.polling(non_stop=True)
