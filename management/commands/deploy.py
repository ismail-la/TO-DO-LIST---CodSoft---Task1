# base/management/commands/deploy.py
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run migrations and collect static files'

    def handle(self, *args, **kwargs):
        call_command('migrate')
        call_command('collectstatic', interactive=False)