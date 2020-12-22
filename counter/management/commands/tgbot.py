from django.core.management.base import BaseCommand
import telebot
from collections import defaultdict
from counter.models import User, Place

class Command(BaseCommand):
    help = 'Telegram Bot'

    def handle(self, *args, **options):

        token = '1413357704:AAEEgjkYYkj3ilqXibHBp848byt41Jb34cM'
        bot = telebot.TeleBot(token)

        plcs = defaultdict(list)

        @bot.message_handler(commands=['add'])
        def add_place(message):
            if User.objects.filter(tg=message.chat.id):
                c = Place(title=message.text[5:], user=User.objects.get(tg=message.chat.id))
                c.save()
            else:
                u = User(tg=message.chat.id)
                u.save()
                c = Place(title=message.text[5:], user=User.objects.get(tg=message.chat.id))
                c.save()
            bot.send_message(chat_id=message.chat.id, text="Место {} добавлено".format(message.text[5:]))

        @bot.message_handler(commands=['list'])
        def list_place(message):
            if not Place.objects.filter(user=User.objects.get(tg=message.chat.id)):
                txt = 'Вы пока не добавили ни одного места.'
            else:
                txt = ''
                for now in Place.objects.filter(user=User.objects.get(tg=message.chat.id)):
                    txt += str(now.title) + '\n'
            bot.send_message(chat_id=message.chat.id, text=txt)

        @bot.message_handler(commands=['reset'])
        def add_place(message):
            Place.objects.all().delete()
            bot.send_message(chat_id=message.chat.id, text='Все ранее добавленные локации удалены.')

        bot.polling()