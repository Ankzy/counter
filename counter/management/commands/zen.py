from django.core.management.base import BaseCommand
from argparse import RawTextHelpFormatter

class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        if options['short']:
            import __hello__
            s = ''
            for i in args:
                s += str(i)
            return s
        else:
            import this
            s = ''
            for i in args:
                s += str(i)
            return s


    def create_parser(self, prog_name, subcommand):
        parser = super().create_parser(prog_name, subcommand)
        parser.formatter_class = RawTextHelpFormatter
        return parser

    def add_arguments(self, parser):
        parser.add_argument(
            '-s',
            '--short',
            action='store_true',
            default = False,
            help='Вывод короткого сообщения'
        )
        parser.add_argument(
            nargs='+',
            type=int,
            dest='args'
        )
