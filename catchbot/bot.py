import telegram.ext as tg

def create_bot(token):
    return tg.Updater(token=token)
    
    