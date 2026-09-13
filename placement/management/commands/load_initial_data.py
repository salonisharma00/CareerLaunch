from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Load CareerLaunch initial data from data.json"

    def handle(self, *args, **options):
        call_command("loaddata", "data.json")
        self.stdout.write(
            self.style.SUCCESS("CareerLaunch initial data loaded successfully!")
        )