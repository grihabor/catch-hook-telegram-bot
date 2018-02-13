
def start(bot, update):

    bot.send_message(
        chat_id=update.message.chat_id, 
        text='\n'.join([
            'Hi!',
            '',
            "I'm the bot to catch your hooks",
            '',
            'Chat id: {}'.format(update.message.chat_id),
            'Add this chat id to your server settings',
        ]),
    )
    