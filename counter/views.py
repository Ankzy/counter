from django.views.generic import TemplateView
from counter.management.commands.tgbot import Command
import telebot

class IndexView(TemplateView):
    template_name = 'counter/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if 'counter' in data:
            data['counter'] = 2
        else:
            data['counter'] = 1
        a = Command()
        a.handle()

        return data